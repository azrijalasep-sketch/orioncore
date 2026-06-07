<div align="center">

# 🌌 ORIONCORE

### AI Trading Dashboard & Hybrid Hedge Fund System

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)]()
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)]()
[![Platform](https://img.shields.io/badge/platform-Web%20%7C%20Windows%20%7C%20Jetson-green.svg)]()

*Single-file AI trading dashboard dengan 15+ sistem AI hybrid, backtesting, dan multi-market analysis.*

**© 2025–2026 Azrijal Asep Abdullah · AAA Research**

</div>

---

## ✨ Fitur Utama

### 🤖 AI & Machine Learning (Hybrid — 10 Paradigma)
- **Neural Network** (MoField) — prediksi harga dengan field-based NN
- **Associative Memory** (Hopfield) — ingat pola pasar
- **DNA/Genetic Encoding** — encoding pola pasar
- **Ensemble/Fusion** — voting multi-strategi
- **Reinforcement Learning** (Omega) — belajar dari hasil
- **Anomaly/Black-Swan Detection** — deteksi kejadian ekstrem
- **Self-Learn ALL** — semua AI belajar otomatis 24/7

### 📊 Analisa Pasar
- Multi-timeframe confluence (MTF)
- Candlestick pattern recognition
- Order book / market depth (Binance L2 real)
- Market regime classification
- Support/Resistance & Divergence detection
- Currency strength matrix
- **AI Bubble Chart** — peta peluang pasar visual
- Market sentiment engine

### 💼 Hedge Fund Tools
- Backtesting + **Walk-Forward Validation** (anti-overfit)
- **Strategy Lab** — buat, simpan, & auto-pilih strategi per pasar
- Risk-Reward, Sharpe, Profit Factor, Max Drawdown
- Portfolio manager + NAV tracking
- Kelly position sizing
- Risk engine + kill switch
- Economic calendar

### 💾 Data & Persistence
- IndexedDB big-data storage
- Auto-save semua state AI
- Real candle data (crypto via Binance)
- MT5 data bridge (forex + eksekusi order)

---

## 🚀 Cara Pakai

### Opsi 1: Buka Langsung (Paling Mudah)
Download `orioncore-ai-trading.html` → buka di browser. Selesai.

### Opsi 2: Host di Server (Jetson Nano / PC) — Direkomendasikan
Akses dari perangkat mana saja + chart embed jalan + AI 24/7.
Lihat [`docs/PANDUAN_JETSON.md`](docs/PANDUAN_JETSON.md)

### Opsi 3: Auto-Trading dengan MT5
Untuk data forex asli + eksekusi order ke broker.
Lihat [`docs/PANDUAN_AUTO_TRADING.md`](docs/PANDUAN_AUTO_TRADING.md)

---

## 📁 Struktur

```
ORIONCORE/
├── orioncore-ai-trading.html   # App utama (single-file)
├── bridge/                     # MT5 bridge (forex + order)
│   ├── orion_mt_bridge.py
│   ├── OrionBridge.mq5
│   └── OrionBridge.mq4
├── jetson/                     # Server Jetson Nano 24/7
│   ├── orion_jetson_server.py
│   ├── install_jetson.sh
│   └── JALANKAN.sh
└── docs/                       # Panduan lengkap
    ├── PANDUAN_AUTO_TRADING.md
    ├── PANDUAN_JETSON.md
    ├── PANDUAN_MT5_DATA.md
    └── CARA_INSTALL_WINDOWS.md
```

---

## 🖥️ Platform Support

| Platform | Status |
|----------|--------|
| Browser (HP/PC) | ✅ Buka langsung |
| Windows (PWA/Electron) | ✅ Installable |
| Jetson Nano (server 24/7) | ✅ Host via HTTP |
| MT5 (forex + order) | ✅ Via bridge (Windows) |

---

## ⚠️ Disclaimer

> ORIONCORE adalah **alat bantu analisa**, **BUKAN jaminan profit**.
>
> - Trading forex/crypto/CFD **berisiko tinggi** — bisa rugi melebihi modal
> - Sinyal AI **belum terbukti profit** di pasar nyata
> - **WAJIB uji akun DEMO** dulu (minimal 1-2 bulan)
> - Keputusan trading & risiko **sepenuhnya tanggung jawab Anda**
>
> Penulis tidak bertanggung jawab atas kerugian apa pun.

---

## 📜 Lisensi

Proprietary © 2025–2026 **Azrijal Asep Abdullah / AAA Research**.
Lihat [LICENSE](LICENSE). Semua hak dilindungi.

---

<div align="center">

**Dibuat dengan dedikasi oleh Azrijal Asep Abdullah · AAA Research**

*Generation #5,000 · Version 2.0*

</div>
