import os
import pyuac
import psutil

x=int(input("Type (1) to get parition data or (2) to benchmark the disk"))

if x== 1:
   print("Getting partition data")
   for disk in psutil.disk_partitions():
    if disk.fstype:
        print(disk.device, psutil.disk_usage(disk.mountpoint))

def main():
  print("Running Benchmarks")
  os.system('cmd /k "winsat disk -drive c' )
    # The window will disappear as soon as the program exits!
input("Press enter to continue. >")



if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main()  # Already an admin here.
elif x== 2:
   main()

