from rich.console import Console
import time, random

console = Console()

class DownloadError(Exception):
    pass

def simulate_download(pkg, realtime=False):
    size = random.randint(20, 120)
    for i in range(1, 101, 10):
        time.sleep(0.1)
        if random.random() < 0.05:
            raise DownloadError(f"Download failed for {pkg} (network/corrupt error)")
        if realtime:
            console.log(f"[+] {pkg} [{i}%] [{size} Mb]")
    return size

def install_package(pkg, realtime=False):
    console.print(f"[+] Preparing to install {pkg}...")
    try:
        size = simulate_download(pkg, realtime=realtime)
        console.print(f"[green][✔][/green] {pkg} installed successfully ({size} Mb).")
    except DownloadError as e:
        console.print(f"[red][x][/red] {e}")

def update_package(pkg):
    console.print(f"[yellow]Updating {pkg}...[/yellow]")
    time.sleep(0.5)
    console.print(f"[green][✔][/green] {pkg} updated.")

def update_all():
    console.print("[yellow]Updating all packages...[/yellow]")
    time.sleep(0.5)
    console.print("[green][✔][/green] All packages updated.")

def query_packages():
    console.print("Installed packages: btop, fish, tmux")

def remove_package(pkg):
    console.print(f"[red]Removing {pkg}...[/red]")
    time.sleep(0.5)
    console.print(f"[green][✔][/green] {pkg} removed.")
