import subprocess

def install_package(package):
    subprocess.run(["sudo", "xbps-install", "-S", package], check=True)
