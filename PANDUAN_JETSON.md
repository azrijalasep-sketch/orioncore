# 🤖 PANDUAN ORIONCORE di JETSON NANO

**Server mini 24/7 — host app + data crypto asli**
**© Azrijal Asep Abdullah / AAA Research**

---

## 🎯 APA YANG ANDA DAPAT

Jetson Nano jadi **server ORIONCORE 24/7**:
- ✅ Host app via HTTP → akses dari HP/PC mana saja
- ✅ AI self-learn **24/7** (tak perlu HP nyala terus)
- ✅ Data crypto **asli** (Binance) via proxy (anti-CORS)
- ✅ Chart embed bisa jalan (karena http, bukan file lokal!)
- ✅ Auto-start saat Jetson nyala
- ✅ Auto-restart kalau crash

---

## ⚠️ KETERBATASAN (jujur)

| Fungsi | Jetson Nano |
|--------|-------------|
| Host app + AI ringan | ✅ Bisa |
| Data crypto asli | ✅ Bisa (Binance) |
| **Data forex + eksekusi order MT5** | ❌ TIDAK (MT5 = Windows only) |
| Training AI berat | ⚠️ Terbatas (GPU kecil) |

> **Untuk MT5 (forex + order):** butuh PC Windows terpisah jalankan `orion_mt_bridge.py`. Jetson host app, PC Windows jalankan MT5 — saling sambung via jaringan.

---

## 📦 ISI PAKET

| File | Fungsi |
|------|--------|
| `orioncore-ai-trading.html` | App utama |
| `orion_jetson_server.py` | Web server + proxy crypto |
| `install_jetson.sh` | Install auto-start 24/7 |
| `JALANKAN.sh` | Jalankan manual (test cepat) |

---

## 🚀 CARA INSTALL

### Persiapan (sekali saja):
1. Jetson Nano sudah ter-setup (JetPack OS, terhubung WiFi/LAN)
2. Buka **Terminal** di Jetson

### Langkah:
1. Salin folder `ORIONCORE_JETSON` ke Jetson (USB/SCP/download)
2. Buka terminal di folder itu:
```bash
cd ORIONCORE_JETSON
```

3. **Test dulu (manual):**
```bash
bash JALANKAN.sh
```
Akan muncul alamat: `http://[IP-Jetson]:8080`
Buka alamat itu di HP/PC → app muncul. Tekan Ctrl+C untuk stop.

4. **Install 24/7 (auto-start):**
```bash
bash install_jetson.sh
```
Sekarang ORIONCORE jalan otomatis tiap Jetson nyala.

---

## 📱 CARA AKSES

Dari HP/PC/tablet (WiFi/LAN sama dengan Jetson):
```
http://[IP-JETSON]:8080
```
Contoh: `http://192.168.1.10:8080`

> Cek IP Jetson: ketik `hostname -I` di terminal Jetson

---

## 🔧 PERINTAH BERGUNA

```bash
# Cek status
sudo systemctl status orioncore

# Stop / Start
sudo systemctl stop orioncore
sudo systemctl start orioncore

# Lihat log real-time
journalctl -u orioncore -f

# Restart
sudo systemctl restart orioncore
```

---

## 🌡️ TIPS JETSON NANO

- **Pakai mode 5W kalau panas:** `sudo nvpmodel -m 1`
- **Pakai mode max performa:** `sudo nvpmodel -m 0 && sudo jetson_clocks`
- **Pendingin:** pasang fan/heatsink kalau jalan 24/7
- **Power supply:** pakai adaptor 5V/4A (barrel jack), bukan microUSB, untuk stabil
- **SD card:** pakai yang cepat (A1/A2) min 32GB

---

## 🔗 SAMBUNG KE MT5 (opsional, untuk forex + order)

Kalau mau forex + eksekusi order:
1. Siapkan **1 PC Windows** dengan MT5
2. Di PC itu jalankan `orion_mt_bridge.py` (dari ZIP utama)
3. Di app (yang di-host Jetson) → Settings → MT Bridge
4. Host: IP PC Windows, Port: 8765
5. Jetson host app + crypto, PC Windows kasih forex + order

```
        Jetson Nano (host app + crypto 24/7)
              ↕ (jaringan)
   PC Windows (MT5 bridge: forex + order)
              ↕
          Broker
```

---

## ⚖️ DISCLAIMER

ORIONCORE alat bantu analisa, **bukan jaminan profit**. Uji DEMO dulu. Trading berisiko tinggi. Keputusan & risiko di tangan Anda.

---

*ORIONCORE v2.0 · © 2025-2026 Azrijal Asep Abdullah / AAA Research*
