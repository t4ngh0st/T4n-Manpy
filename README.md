# 🌱 T4n-Manpy  
**Simple Python-based Package Manager for Void Linux**

T4n-Manpy adalah package manager minimalis berbasis **Python** untuk Void Linux.  
Dibuat untuk mempermudah interaksi dengan **xbps** dan **xbps-src**, serta menambahkan beberapa utilitas tambahan.

---

## ✨ Fitur Utama
- 📦 **Install software**
  ```bash
  t4n -i <software>
  ```
- 🔄 **Update software tertentu**
  ```bash
  t4n -u <software>
  ```
- ⚡ **Update semua software/system**
  ```bash
  t4n -ua
  ```
- 🔍 **Query database package**
  ```bash
  t4n -q <keyword>
  ```
- ❌ **Remove/uninstall software**
  ```bash
  t4n -r <software>
  ```

---

## 🛠️ Utilitas Tambahan
- **Convert `.deb` → `.xbps`** menggunakan wrapper `xdeb`
  ```bash
  t4n -xdeb <file.deb>
  ```
- **Membuat template** menggunakan `xbps-src`
  ```bash
  t4n -src <template-name>
  ```

---

## 📂 Struktur Proyek
```
t4n-manpy/
├─ README.md
├─ pyproject.toml
├─ scripts/
│  └─ install-system.sh
├─ t4n_manpy/
│  ├─ cli.py
│  ├─ config.py
│  ├─ core/
│  │  ├─ installer.py
│  │  ├─ converter.py
│  │  └─ src_generator.py
│  └─ wrappers/
│     ├─ xdeb
│     └─ xbps-src
└─ tests/
   └─ test_cli.py
```

---

## 🚀 Instalasi
Clone repo dan install ke sistem:
```bash
git clone https://github.com/yourname/t4n-manpy.git
cd t4n-manpy
pip install .
```

Atau gunakan script installer:
```bash
sudo bash scripts/install-system.sh
```

---

## 🖥️ Contoh Penggunaan
```bash
t4n -i neovim
t4n -u curl
t4n -ua
t4n -q python
t4n -r firefox
t4n -xdeb package.deb
t4n -src my-template
```

---

## 📜 Lisensi
MIT License © 2025 T4n-Manpy
