# 🚀 PANDUAN AUTO-TRADING ORIONCORE + MT5

**© Azrijal Asep Abdullah / AAA Research**

Panduan lengkap menyambungkan ORIONCORE ke MetaTrader 5 agar bisa eksekusi order ke broker.

---

## ⚠️ BACA DULU — PERINGATAN PENTING

> **JANGAN langsung pakai akun uang asli.**
>
> - Uji di **akun DEMO** broker minimal **1-2 bulan** dulu
> - Auto-trading dengan uang asli **sangat berisiko** — saldo bisa habis cepat
> - Sinyal AI **belum terbukti profit** di pasar nyata
> - Anda bertanggung jawab **penuh** atas setiap order & kerugian
> - Mulai dengan lot **terkecil** (0.01) kalaupun nanti pakai real

---

## 📋 YANG DIBUTUHKAN

1. **PC/Laptop Windows** (MT5 + Python jalan di sini)
2. **MetaTrader 5** terinstall + akun broker (DEMO dulu!)
3. **Python 3.8+** terinstall
4. File **orion_mt_bridge.py** (ada di ZIP)
5. App **ORIONCORE** (HTML)

---

## LANGKAH 1 — Install MetaTrader 5

1. Download MT5 dari broker Anda (atau metatrader5.com)
2. Install & login akun **DEMO** dulu
3. Di MT5: **Tools → Options → Expert Advisors**
   - ✅ Centang "Allow algorithmic trading"
   - ✅ Centang "Allow DLL imports"
4. Pastikan tombol **"Algo Trading"** di toolbar MT5 **hijau/aktif**

---

## LANGKAH 2 — Install Python + Library

1. Download Python dari python.org (centang "Add to PATH" saat install)
2. Buka **Command Prompt** (cmd), ketik:

```
pip install MetaTrader5 flask flask-cors
```

3. Tunggu sampai selesai (semua "Successfully installed")

---

## LANGKAH 3 — Jalankan Bridge

1. Pastikan **MT5 sudah terbuka & login**
2. Letakkan `orion_mt_bridge.py` di folder mudah (mis. Desktop)
3. Buka cmd di folder itu, ketik:

```
python orion_mt_bridge.py
```

4. Kalau berhasil muncul:
```
✅ MT5 terhubung: [nomor akun Anda]
🚀 ORION MT Bridge jalan di http://0.0.0.0:8765
```

> Kalau gagal "Gagal connect MT5" → pastikan MT5 terbuka, login, dan Algo Trading aktif.

---

## LANGKAH 4 — Sambungkan App ke Bridge

### Kalau app dibuka di PC yang SAMA dengan MT5:
1. Buka ORIONCORE → **Settings → MT4/MT5 Data Bridge**
2. Host: `localhost`
3. Port: `8765`
4. Tap **Connect** → harus muncul 🟢 terhubung

### Kalau app dibuka di HP (WiFi sama dengan PC):
1. Di PC, buka cmd ketik `ipconfig` → catat **IPv4 Address** (mis. `192.168.1.5`)
2. Di app HP → Settings → MT Bridge
3. Host: `192.168.1.5` (IP PC Anda)
4. Port: `8765`
5. Tap **Connect**

> Pastikan PC & HP di **WiFi yang sama**. Firewall Windows mungkin minta izin — klik **Allow**.

---

## LANGKAH 5 — Verifikasi Data Asli

Setelah terhubung:
- Harga di app berubah jadi **data broker asli** (bukan simulasi)
- Badge data source jadi 🟢 (CANDLE ASLI / MT5)
- Candle chart pakai OHLC asli dari broker

---

## LANGKAH 6 — Aktifkan Eksekusi Order (HATI-HATI)

> **Pastikan masih akun DEMO!**

1. Di app → tab **Chart** atau **Analisa**
2. Mode trading: pastikan **OPEN/LIVE** (bukan demo internal app)
3. Saat AI kasih sinyal + Anda setuju → eksekusi
4. Order dikirim: App → Bridge → MT5 → Broker
5. Cek di MT5 tab **"Trade"** → order Anda muncul di sana

### Pengaman yang Disarankan:
- **Lot kecil**: set 0.01 dulu
- **Selalu pakai SL (Stop Loss)** — jangan trading tanpa SL
- **Kill switch**: app punya tombol darurat tutup semua posisi
- **Pantau terus** — jangan tinggalkan auto-trading tanpa diawasi

---

## 🛡️ CHECKLIST SEBELUM PAKAI UANG ASLI

Jangan pindah ke akun real sebelum SEMUA ini ✅:

- [ ] Sudah uji DEMO minimal 1-2 bulan
- [ ] Win-rate DEMO konsisten > 55% (catat hasilnya)
- [ ] Sudah paham cara kerja SL/TP
- [ ] Kill switch sudah dites (bisa tutup semua posisi)
- [ ] Paham berapa maksimal rugi yang sanggup ditanggung
- [ ] Mulai modal KECIL (uang yang siap hilang)
- [ ] Lot terkecil (0.01)

---

## 🔧 TROUBLESHOOTING

| Masalah | Solusi |
|---------|--------|
| "Gagal connect MT5" | MT5 belum terbuka / belum login / Algo Trading off |
| App tak bisa connect bridge | Cek IP benar, WiFi sama, firewall allow |
| Order ditolak (retcode error) | Algo Trading off, lot terlalu kecil/besar, market tutup |
| Harga tidak update | Bridge mati, restart `python orion_mt_bridge.py` |
| "pip not recognized" | Python belum di PATH, install ulang centang "Add to PATH" |

---

## 📞 ENDPOINT BRIDGE (teknis)

Bridge menyediakan:
- `/ping` — cek koneksi
- `/prices` — harga semua simbol
- `/candles` — data OHLC
- `/account` — info akun (balance, equity)
- `/order` — kirim/tutup order (action: BUY/SELL/closeall)

---

## ⚖️ DISCLAIMER

ORIONCORE adalah alat bantu analisa. **Bukan jaminan profit.** Trading forex/crypto/CFD berisiko tinggi dan bisa menyebabkan kerugian melebihi modal. Keputusan trading sepenuhnya tanggung jawab Anda. Penulis tidak bertanggung jawab atas kerugian apa pun.

**Uji DEMO dulu. Selalu.**

---

*ORIONCORE v2.0 · © 2025-2026 Azrijal Asep Abdullah / AAA Research*
