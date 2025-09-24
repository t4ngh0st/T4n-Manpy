# core/vur.py
import json
import os
import subprocess
import tempfile
import logging
import urllib.request

VUR_REPO = "https://github.com/t4ngh0st/VUR"
VUR_INDEX = "https://raw.githubusercontent.com/t4ngh0st/VUR/main/packages.json"

log = logging.getLogger("t4n-vur")

def fetch_index():
    try:
        with urllib.request.urlopen(VUR_INDEX) as resp:
            return json.load(resp)
    except Exception as e:
        log.error(f"Gagal fetch index VUR: {e}")
        return {}

def query(pkgname: str):
    index = fetch_index()
    found = []
    for category, pkgs in index.items():
        for name, data in pkgs.items():
            if pkgname.lower() in name.lower():
                found.append((category, data))
    if not found:
        print(f"[x] Package '{pkgname}' tidak ditemukan di VUR.")
    else:
        print(f"[+] Hasil pencarian '{pkgname}':")
        for cat, data in found:
            print(f" - {data['name']} ({data['version']}) [{cat}] : {data['desc']}")

def install_from_vur(pkgname: str):
    index = fetch_index()
    target = None
    category = None
    for cat, pkgs in index.items():
        if pkgname in pkgs:
            target = pkgs[pkgname]
            category = cat
            break

    if not target:
        log.error(f"Package {pkgname} tidak ditemukan di VUR.")
        return

    log.info(f"Menyiapkan install {pkgname} dari VUR ({category})")

    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        # clone repo VUR
        subprocess.run(["git", "clone", VUR_REPO], check=True)
        pkg_path = os.path.join(tmpdir, "VUR", target["path"])

        # build dengan xbps-src
        try:
            subprocess.run(
                ["./xbps-src", "pkg", pkgname],
                cwd=pkg_path,
                check=True
            )
        except subprocess.CalledProcessError:
            log.error(f"Gagal build {pkgname} dari template VUR.")
            return

        # install hasil build
        try:
            subprocess.run(
                ["xbps-install", "-y", f"{pkgname}"],
                check=True
            )
        except subprocess.CalledProcessError:
            log.error(f"Gagal install {pkgname} ke sistem.")
            return

    log.info(f"[✓] Package {pkgname} berhasil terinstall dari VUR.")
