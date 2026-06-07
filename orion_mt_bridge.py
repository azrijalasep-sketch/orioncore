#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════
#  ORION MT5 DATA BRIDGE — serve harga + candle + account + order
#  ke ORIONCORE AI Trading dari MetaTrader 5
#  © Azrijal Asep Abdullah / AAA Research
# ═══════════════════════════════════════════════════════════════
#  CARA PAKAI:
#  1. Install: pip install MetaTrader5 flask flask-cors
#  2. Buka MT5, login akun broker
#  3. Jalankan: python orion_mt_bridge.py
#  4. Di app ORIONCORE → Settings → MT4/MT5 Data Bridge:
#     - Di PC sama: host = localhost, port = 8765
#     - Dari HP (WiFi sama): host = IP LAN PC (cek: ipconfig), port = 8765
# ═══════════════════════════════════════════════════════════════

from flask import Flask, request, jsonify
from flask_cors import CORS
import MetaTrader5 as mt5
from datetime import datetime

app = Flask(__name__)
CORS(app)  # izinkan akses dari app (termasuk file lokal/LAN)

# Inisialisasi koneksi MT5
if not mt5.initialize():
    print("❌ Gagal connect MT5. Pastikan MT5 terbuka & login.")
    quit()
print("✅ MT5 terhubung:", mt5.account_info().login if mt5.account_info() else "?")

# Map timeframe ORIONCORE → MT5
TF_MAP = {
    'M1': mt5.TIMEFRAME_M1, 'M5': mt5.TIMEFRAME_M5, 'M15': mt5.TIMEFRAME_M15,
    'M30': mt5.TIMEFRAME_M30, 'H1': mt5.TIMEFRAME_H1, 'H4': mt5.TIMEFRAME_H4,
    'D1': mt5.TIMEFRAME_D1, 'W1': mt5.TIMEFRAME_W1,
}

# Daftar simbol yang dipantau (sesuaikan dengan broker Anda)
WATCH = ['EURUSD','GBPUSD','USDJPY','USDCHF','USDCAD','AUDUSD','NZDUSD',
         'EURGBP','EURJPY','GBPJPY','XAUUSD','XAGUSD','BTCUSD','ETHUSD',
         'US30','US500','NAS100','USOIL']

@app.route('/ping')
def ping():
    return jsonify({'status':'ok', 'mt5':mt5.terminal_info()._asdict() if mt5.terminal_info() else None})

@app.route('/prices')
def prices():
    """Harga bid/ask semua simbol watch."""
    out = {}
    for s in WATCH:
        t = mt5.symbol_info_tick(s)
        info = mt5.symbol_info(s)
        if t and info:
            # % change dari open harian
            bars = mt5.copy_rates_from_pos(s, mt5.TIMEFRAME_D1, 0, 1)
            chg = 0
            if bars is not None and len(bars):
                op = bars[0]['open']
                if op: chg = (t.bid - op)/op*100
            out[s] = {'bid':t.bid, 'ask':t.ask, 'chg':round(chg,2)}
    return jsonify(out)

@app.route('/price')
def price():
    s = request.args.get('symbol','EURUSD')
    t = mt5.symbol_info_tick(s)
    if not t: return jsonify({'error':'no symbol'}), 404
    return jsonify({'symbol':s, 'bid':t.bid, 'ask':t.ask})

@app.route('/candles')
def candles():
    """Candle OHLC ASLI dari broker."""
    s = request.args.get('symbol','EURUSD')
    tf = request.args.get('tf','H1')
    count = int(request.args.get('count','200'))
    rates = mt5.copy_rates_from_pos(s, TF_MAP.get(tf, mt5.TIMEFRAME_H1), 0, count)
    if rates is None: return jsonify([]), 200
    out = [{'time':int(r['time']), 'open':float(r['open']), 'high':float(r['high']),
            'low':float(r['low']), 'close':float(r['close']), 'volume':int(r['tick_volume'])}
           for r in rates]
    return jsonify(out)

@app.route('/account')
def account():
    a = mt5.account_info()
    if not a: return jsonify({'error':'no account'}), 404
    return jsonify({'login':a.login, 'balance':a.balance, 'equity':a.equity,
                    'margin':a.margin, 'free_margin':a.margin_free, 'profit':a.profit,
                    'currency':a.currency, 'leverage':a.leverage, 'server':a.server})

@app.route('/order', methods=['POST'])
def order():
    """Eksekusi/close order. Body: {action, symbol, lot, sl, tp, type, magic}"""
    d = request.json or {}
    act = d.get('action')
    if act == 'closeall':
        positions = mt5.positions_get()
        closed = 0
        for p in (positions or []):
            tick = mt5.symbol_info_tick(p.symbol)
            req = {'action':mt5.TRADE_ACTION_DEAL, 'symbol':p.symbol, 'volume':p.volume,
                   'type':mt5.ORDER_TYPE_SELL if p.type==0 else mt5.ORDER_TYPE_BUY,
                   'position':p.ticket, 'price':tick.bid if p.type==0 else tick.ask,
                   'magic':d.get('magic',202501), 'comment':'ORION close'}
            if mt5.order_send(req).retcode == mt5.TRADE_RETCODE_DONE: closed += 1
        return jsonify({'closed':closed})
    # New market order
    sym = d.get('symbol','EURUSD'); lot = float(d.get('lot',0.01))
    is_buy = d.get('type','BUY').upper()=='BUY'
    tick = mt5.symbol_info_tick(sym)
    req = {'action':mt5.TRADE_ACTION_DEAL, 'symbol':sym, 'volume':lot,
           'type':mt5.ORDER_TYPE_BUY if is_buy else mt5.ORDER_TYPE_SELL,
           'price':tick.ask if is_buy else tick.bid,
           'sl':float(d.get('sl',0)), 'tp':float(d.get('tp',0)),
           'magic':d.get('magic',202501), 'comment':'ORION AI', 'type_filling':mt5.ORDER_FILLING_IOC}
    res = mt5.order_send(req)
    return jsonify({'retcode':res.retcode, 'order':res.order, 'ok':res.retcode==mt5.TRADE_RETCODE_DONE})

if __name__ == '__main__':
    print("🚀 ORION MT Bridge jalan di http://0.0.0.0:8765")
    print("   PC sama  → host: localhost")
    print("   Dari HP  → host: IP LAN PC (cek 'ipconfig')")
    app.run(host='0.0.0.0', port=8765, threaded=True)
