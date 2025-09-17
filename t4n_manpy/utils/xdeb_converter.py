import subprocess
import os

def convert_deb(deb_file):
    if not os.path.exists(deb_file):
        raise FileNotFoundError(f"Deb file {deb_file} not found!")
    subprocess.run(["/usr/bin/t4n/xdeb", deb_file], check=True)
