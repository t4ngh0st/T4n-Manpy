# core/utils.py
import sys
import time

def print_step(msg: str):
    print(f"[+] {msg}")

def realtime_progress(task: str, size: int = 100, step: int = 5, delay: float = 0.1):
    for i in range(0, size + 1, step):
        sys.stdout.write(f"\r[+] {task} [{i}%]")
        sys.stdout.flush()
        time.sleep(delay)
    print(" [DONE]")

def handle_error(msg: str, exit_code: int = 1):
    print(f"[x] ERROR: {msg}")
    sys.exit(exit_code)

