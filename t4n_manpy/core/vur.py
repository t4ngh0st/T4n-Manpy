import os, subprocess
from pathlib import Path

VUR_REPO = "https://github.com/t4ngh0st/VUR.git"
VUR_DIR = Path.home() / ".vur"
VOID_PKGS = Path.home() / "void-packages" / "srcpkgs"

def update_vur():
    if not VUR_DIR.exists():
        subprocess.run(["git", "clone", VUR_REPO, str(VUR_DIR)], check=True)
    else:
        subprocess.run(["git", "-C", str(VUR_DIR), "pull"], check=True)

def install_from_vur(pkgname):
    update_vur()
    for root, dirs, files in os.walk(VUR_DIR):
        if "template" in files and pkgname in root:
            src = Path(root) / "template"
            dest = VOID_PKGS / pkgname
            dest.mkdir(parents=True, exist_ok=True)
            subprocess.run(["cp", str(src), str(dest / "template")])
            subprocess.run(["./xbps-src", "pkg", pkgname], cwd=str(VOID_PKGS.parent))
            subprocess.run(["sudo", "xbps-install", "-R", "hostdir/binpkgs", pkgname])
            print(f"[+] Installed {pkgname} from VUR")
            return
    print(f"[!] Package {pkgname} not found in VUR")
