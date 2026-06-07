#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════
#  ORIONCORE JETSON SERVER — host app + data crypto 24/7
#  Untuk NVIDIA Jetson Nano (Linux ARM)
#  © Azrijal Asep Abdullah / AAA Research
# ═══════════════════════════════════════════════════════════════
#  Host app ORIONCORE via HTTP + proxy data crypto (Binance)
#  Akses dari HP/PC mana saja: http://[IP-JETSON]:8080
# ═══════════════════════════════════════════════════════════════

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json, urllib.request, os, socket

PORT = 8080
APP_FILE = 'orioncore-ai-trading.html'

class OrionHandler(SimpleHTTPRequestHandler):
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200); self._cors(); self.end_headers()

    def do_GET(self):
        # Root → serve app
        if self.path == '/' or self.path == '':
            self.path = '/' + APP_FILE

        # Proxy data crypto Binance (hindari CORS)
        if self.path.startswith('/api/price/'):
            sym = self.path.split('/api/price/')[1].upper()
            try:
                url = f'https://api.binance.com/api/v3/ticker/price?symbol={sym}'
                data = urllib.request.urlopen(url, timeout=8).read()
                self.send_response(200); self._cors()
                self.send_header('Content-Type','application/json'); self.end_headers()
                self.wfile.write(data); return
            except Exception as e:
                self.send_response(502); self._cors(); self.end_headers()
                self.wfile.write(json.dumps({'error':str(e)}).encode()); return

        # Proxy candle/kline Binance
        if self.path.startswith('/api/klines/'):
            parts = self.path.split('/api/klines/')[1].split('/')
            sym = parts[0].upper(); interval = parts[1] if len(parts)>1 else '1h'
            try:
                url = f'https://api.binance.com/api/v3/klines?symbol={sym}&interval={interval}&limit=100'
                data = urllib.request.urlopen(url, timeout=8).read()
                self.send_response(200); self._cors()
                self.send_header('Content-Type','application/json'); self.end_headers()
                self.wfile.write(data); return
            except Exception as e:
                self.send_response(502); self._cors(); self.end_headers()
                self.wfile.write(json.dumps({'error':str(e)}).encode()); return

        # Proxy order book Binance
        if self.path.startswith('/api/depth/'):
            sym = self.path.split('/api/depth/')[1].upper()
            try:
                url = f'https://api.binance.com/api/v3/depth?symbol={sym}&limit=10'
                data = urllib.request.urlopen(url, timeout=8).read()
                self.send_response(200); self._cors()
                self.send_header('Content-Type','application/json'); self.end_headers()
                self.wfile.write(data); return
            except Exception as e:
                self.send_response(502); self._cors(); self.end_headers()
                self.wfile.write(json.dumps({'error':str(e)}).encode()); return

        # Health check
        if self.path == '/health':
            self.send_response(200); self._cors()
            self.send_header('Content-Type','application/json'); self.end_headers()
            self.wfile.write(json.dumps({'status':'ok','server':'jetson'}).encode()); return

        # Default: serve files (app)
        return SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        # tambah CORS ke semua response file
        if not self.path.startswith('/api/'):
            self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

    def log_message(self, fmt, *args):
        pass  # diam, biar log bersih

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80)); ip = s.getsockname()[0]; s.close()
        return ip
    except: return 'localhost'

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.exists(APP_FILE):
        print(f'❌ {APP_FILE} tidak ditemukan! Letakkan di folder sama.')
        exit(1)
    ip = get_ip()
    print('═' * 55)
    print('  🚀 ORIONCORE JETSON SERVER')
    print('═' * 55)
    print(f'  ✅ Server jalan!')
    print(f'  📱 Akses dari HP/PC (WiFi sama):')
    print(f'      http://{ip}:{PORT}')
    print(f'  💻 Akses lokal di Jetson:')
    print(f'      http://localhost:{PORT}')
    print(f'  🟢 Proxy data crypto: AKTIF (anti-CORS)')
    print(f'  ⏹  Stop: Ctrl+C')
    print('═' * 55)
    HTTPServer(('0.0.0.0', PORT), OrionHandler).serve_forever()
