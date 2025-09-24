# 🌱 T4n-Manpy Version 1.0.0
**Simple Python-based Package Manager for T4n OS**

T4n-Manpy adalah package manager minimalis berbasis **Python** untuk T4n OS.
Dibuat untuk mempermudah interaksi dengan [**xbps**](https://github.com/void-linux/xbps), [**xbps-src**](https://github.com/void-linux/void-packages) dan [**XDEB**](https://github.com/xdeb-org/xdeb), serta menambahkan beberapa utilitas tambahan.

---

## ✨ Fitur Utama
- 📦 **Install software**
  ```bash
  tan -i <software>
  ```
- 🔄 **Update software tertentu**
  ```bash
  tan -u <software>
  ```
- ⚡ **Update semua software/system**
  ```bash
  tan -ua
  ```
- 🔍 **Query database package**
  ```bash
  tan -q <keyword>
  ```
- ❌ **Remove/uninstall software**
  ```bash
  tan -r <software>
  ```

---

## 🛠️ Utilitas Tambahan
- **Convert `.deb` → `.xbps`** menggunakan wrapper `xdeb`
  ```bash
  tan -xdeb <file.deb>
  ```
- **Membuat template** menggunakan `xbps-src`
  ```bash
  tan -src <template-name>
  ```

---

## 📂 Struktur Proyek
```
T4n-Manpy/
├─ README.md
├─ pyproject.toml
├─ install.sh
└─ t4n_manpy/
   ├─ __init__.py
   ├─ cli.py
   ├─ config.py
   ├─ core/
   │  ├─ __init__.py
   │  ├─ installer.py
   │  ├─ converter.py
   │  ├─ src_generator.py
   │  ├─ database.py
   │  └─ utils.py
   ├─ wrappers/
   │  ├─ xdeb/
   │  │  └─ xdeb
   │  └─ void-packages/
   │     └─ xbps-src
   └─ templates/
      ├─ btop.xbps
      └─ example.template
```

---

## 🚀 Instalasi
Clone repo dan install ke sistem:
```bash
git clone https://github.com/t4ngh0st/t4n-manpy.git
cd T4n-Manpy/t4n-manpy
pip install .
```

Atau gunakan script installer:
```bash
chmod +x install.sh
./install.sh
```

---

## 🖥️ Contoh Penggunaan
- install software dari repo resmi
```bash
tan -i neovim
```

- update software tertentu
```bash
tan -u curl
```

- update semua software & system
```bash
tan -ua
```

- query package database resmi
```bash
tan -q python
```

- remove/uninstall software
```bash
tan -r firefox
```

- **Convert `.deb` → `.xbps`** menggunakan wrapper `xdeb`
```bash
tan -xdeb package.deb
```

- buat template baru
```bash
tan -src my-template
```

- Query package di VUR (Void User Repository)
```bash
tan -vq bspwm
```

- install package dari VUR
```bash
tan -vur bspwm
```
---

## 📜 Lisensi
GPL-3.0 License © 2025 T4n-Manpy
