print("Getting partition data")
import psutil

for disk in psutil.disk_partitions():
    if disk.fstype:
        print(disk.device, psutil.disk_usage(disk.mountpoint))