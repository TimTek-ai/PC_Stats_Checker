import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('C:\\').percent

    print(f"CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")

    time.sleep(1)