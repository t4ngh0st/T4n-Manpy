# 🌱 T4n-Manpy  
**Simple Python-based Package Manager for T4n OS**

T4n-Manpy adalah package manager minimalis berbasis **Python** untuk T4n OS.
Dibuat untuk mempermudah interaksi dengan [**xbps**](https://github.com/void-linux/xbps), [**xbps-src**](https://github.com/void-linux/void-packages) dan [**XDEB**](https://github.com/xdeb-org/xdeb), serta menambahkan beberapa utilitas tambahan.

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
GPL-3.0 License © 2025 T4n-Manpy
