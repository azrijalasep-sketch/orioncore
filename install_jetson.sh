#!/bin/bash
# ═══════════════════════════════════════════════════════════════
#  INSTALL ORIONCORE sebagai service auto-start 24/7 di Jetson Nano
#  © Azrijal Asep Abdullah / AAA Research
# ═══════════════════════════════════════════════════════════════
#  Jalankan: bash install_jetson.sh
# ═══════════════════════════════════════════════════════════════

set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
USER_NAME="$(whoami)"

echo "═══════════════════════════════════════════"
echo "  INSTALL ORIONCORE 24/7 di Jetson Nano"
echo "═══════════════════════════════════════════"

# 1. Pastikan Python3 ada
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 belum ada. Install dulu: sudo apt install python3"
    exit 1
fi
echo "✅ Python3 ditemukan"

# 2. Buat systemd service (auto-start saat Jetson nyala)
SERVICE_FILE="/etc/systemd/system/orioncore.service"
echo "📝 Membuat service auto-start..."

sudo tee "$SERVICE_FILE" > /dev/null <<EOF
[Unit]
Description=ORIONCORE AI Trading Server
After=network.target

[Service]
Type=simple
User=$USER_NAME
WorkingDirectory=$DIR
ExecStart=/usr/bin/python3 $DIR/orion_jetson_server.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# 3. Aktifkan service
sudo systemctl daemon-reload
sudo systemctl enable orioncore.service
sudo systemctl restart orioncore.service

sleep 2
echo ""
echo "═══════════════════════════════════════════"
echo "  ✅ SELESAI! ORIONCORE jalan 24/7"
echo "═══════════════════════════════════════════"
IP=$(hostname -I | awk '{print $1}')
echo "  📱 Akses dari HP/PC: http://$IP:8080"
echo ""
echo "  Perintah berguna:"
echo "    Status:  sudo systemctl status orioncore"
echo "    Stop:    sudo systemctl stop orioncore"
echo "    Start:   sudo systemctl start orioncore"
echo "    Log:     journalctl -u orioncore -f"
echo "═══════════════════════════════════════════"
