# 🔗 Ambil Data Asli dari MT4/MT5 — ORIONCORE

Solusi terbaik untuk data real-time: ambil langsung dari **MetaTrader 5** Anda.
Harga + candle ASLI dari broker, semua simbol, tanpa CORS, tanpa simulasi.

## Kenapa MT5 (bukan TradingView/Koyfin)?
- ✅ Harga real-time dari broker Anda sendiri (yang akan Anda trade)
- ✅ Candle OHLC historis asli (semua timeframe M1–W1)
- ✅ Tanpa CORS / tanpa diblokir (bridge lokal di PC Anda)
- ✅ Sekaligus bisa eksekusi order (BUY/SELL/close)

## Langkah Setup

### 1. Di PC (Windows) — siapkan bridge
```bash
pip install MetaTrader5 flask flask-cors
```

### 2. Buka MT5, login akun broker Anda
(Pastikan simbol yang mau dipantau ada di Market Watch)

### 3. Jalankan bridge
```bash
python orion_mt_bridge.py
```
Akan muncul: `🚀 ORION MT Bridge jalan di http://0.0.0.0:8765`

### 4. Hubungkan di app ORIONCORE
Buka **Settings → 🔗 Data dari MT4/MT5**:

| Buka app di mana | Host | Port |
|------------------|------|------|
| PC yang sama | `localhost` | `8765` |
| **HP (WiFi sama)** | **IP LAN PC** (mis. `192.168.1.5`) | `8765` |

> Cek IP LAN PC: buka CMD → ketik `ipconfig` → lihat "IPv4 Address"

Tap **🔗 Hubungkan ke MT4/MT5**. Kalau hijau "Terhubung" → data broker asli aktif!

## Yang Didapat Setelah Terhubung
- **Harga** semua simbol update tiap 5 detik dari broker
- **Candle** chart ORIONCORE pakai OHLC asli broker (bukan simulasi)
- **Account** balance/equity real (verifikasi di tab Risiko)
- **Eksekusi** order langsung ke MT5 (mode LIVE)

## Endpoint Bridge (untuk developer)
- `GET /ping` — cek koneksi
- `GET /prices` — harga semua simbol watch
- `GET /candles?symbol=EURUSD&tf=H1&count=200` — candle OHLC asli
- `GET /account` — info akun
- `POST /order` — eksekusi/close order

## Catatan MT4
MT4 tidak punya Python API resmi. Untuk MT4, perlu EA (Expert Advisor) yang
buka socket/file bridge. File `OrionBridge.mq4` (versi lama) bisa dipakai,
atau gunakan MT5 yang jauh lebih mudah (Python API resmi).

## Keamanan
- Bridge hanya jalan di jaringan LOKAL Anda (PC/WiFi sendiri)
- Tidak ada data keluar ke internet
- Order tetap butuh konfirmasi di app (mode LIVE + preflight)

---
**Mulai DEMO dulu** sebelum LIVE. © Azrijal Asep Abdullah / AAA Research
