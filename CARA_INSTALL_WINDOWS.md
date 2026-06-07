# 🖥️ Cara Install ORIONCORE di Windows

Ada **2 cara** — pilih sesuai kebutuhan.

---

## CARA 1: PWA Install (PALING MUDAH — 30 detik) ⭐

Tidak perlu install apapun. Langsung jadi aplikasi desktop.

1. Buka file **`orioncore-ai-trading.html`** dengan **Chrome** atau **Edge**
   (klik kanan file → Open with → Chrome/Edge)
2. Di pojok kanan atas address bar, klik ikon **Install** (⊕ atau monitor kecil)
   - Atau menu ⋮ → **"Install ORIONCORE..."** / **"Apps → Install this site as an app"**
3. Klik **Install**

✅ Selesai! ORIONCORE muncul sebagai aplikasi:
- Ada ikon di Desktop & Start Menu
- Buka di window sendiri (tanpa address bar browser)
- Bisa di-pin ke taskbar

**Kelebihan**: instan, ringan, auto-update kalau file diganti.

---

## CARA 2: Aplikasi .EXE Asli (Electron) 🔧

Buat installer .exe sungguhan (seperti software pada umumnya).

### Syarat:
- Install **Node.js** dulu (https://nodejs.org — versi LTS)

### Langkah:
1. Taruh semua file ini dalam **satu folder**:
   - `orioncore-ai-trading.html`
   - `main.js`
   - `package.json`
   - `orioncore-icon-512.png`
   - `orioncore-icon-192.png`

2. Buka **CMD/PowerShell** di folder itu (Shift + klik kanan → "Open PowerShell here")

3. Install dependency:
   ```bash
   npm install
   ```

4. **Coba jalankan** (tanpa build):
   ```bash
   npm start
   ```
   ORIONCORE akan terbuka sebagai aplikasi desktop.

5. **Buat installer .exe**:
   ```bash
   npm run build
   ```
   Hasil ada di folder **`dist/`**:
   - `ORIONCORE AI Trading Setup 2.0.0.exe` → installer (klik untuk install)
   - Atau versi **portable** (.exe langsung jalan tanpa install): `npm run build-portable`

✅ Hasilnya aplikasi Windows asli dengan ikon, shortcut Desktop & Start Menu.

**Kelebihan**: .exe asli, bisa dibagikan, jalan tanpa browser.

---

## Mana yang Dipilih?

| | PWA (Cara 1) | Electron (Cara 2) |
|---|---|---|
| Kemudahan | ⭐⭐⭐ Instan | ⭐⭐ Perlu Node.js |
| Hasil | App di Start Menu | Installer .exe asli |
| Ukuran | Sangat ringan | ~150MB (termasuk runtime) |
| Bisa dibagikan | ❌ (per-PC) | ✅ (.exe) |
| Untuk pakai sendiri | ✅ Cukup | — |
| Untuk distribusi | — | ✅ Ideal |

**Saran**: Untuk pakai pribadi → **PWA (Cara 1)**. Untuk dibagikan/dijual → **Electron (Cara 2)**.

---

## Bonus: Data MT5 di Windows
Setelah install, sambungkan ke MetaTrader 5 (lihat `PANDUAN_MT5_DATA.md`):
- Jalankan `python orion_mt_bridge.py`
- App → Settings → MT4/MT5 Bridge → host: `localhost`, port: `8765`
- Dapat harga + candle asli broker langsung di PC

---

© Azrijal Asep Abdullah / AAA Research · ORIONCORE v2.0

---

## 🚀 CARA TERCEPAT BUAT .EXE (Klik 1 File)

Setelah install **Node.js** (https://nodejs.org, versi LTS):

1. Taruh semua file dalam 1 folder (html, main.js, package.json, 2 ikon PNG, BUILD_EXE.bat)
2. **Double-click `BUILD_EXE.bat`**
3. Tunggu (otomatis install + build), folder `dist\` akan terbuka berisi .exe

Selesai — tidak perlu ketik perintah apapun.

> Catatan: .exe tidak bisa dibuat di server pembuat app (CDN Electron diblokir),
> jadi build dilakukan di PC Anda. Hanya perlu sekali, dan BUILD_EXE.bat
> mengotomatiskan semuanya.
