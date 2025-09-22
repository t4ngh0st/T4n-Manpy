#!/bin/bash
set -e

echo "[+] Checking for xbps..."

if ! command -v xbps-install &> /dev/null; then
    echo "[!] xbps not found, installing..."

    if command -v yay &> /dev/null; then
        echo "[+] Detected Arch Linux with yay, installing xbps..."
        yay -S xbps --noconfirm

    elif command -v paru &> /dev/null; then
        echo "[+] Detected Arch Linux with paru, installing xbps..."
        paru -S xbps --noconfirm

    elif command -v apk &> /dev/null; then
        echo "[+] Detected Alpine Linux, installing xbps..."
        sudo apk add xbps

    else
        echo "[x] Could not auto-install xbps."
        echo "👉 Please install xbps manually for your distro:"
        echo "   - Void Linux: already available by default"
        echo "   - Arch Linux: use yay/paru (AUR package)"
        echo "   - Alpine Linux: apk add xbps"
        echo "   - Other distros: build from source https://github.com/void-linux/xbps"
        exit 1
    fi
else
    echo "[OK] xbps already installed."
fi

echo "[+] Installing Python dependencies..."
pip install rich

echo "[+] Installing T4n-Manpy..."
pip install .

echo "[✔] Installation complete. Try running: t4n -h"
