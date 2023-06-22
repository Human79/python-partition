import os

x=int(input("Press(1)to check read speeds,(2) to check write speeds or (3) to get partition data: "))

if x==1:
    print("Getting Read Speeds")
    os.system('dd if=tstfile bs=1024k of=/dev/null count=1024')

elif x==2:
    print("Getting write speeds")
    os.system('dd if=/dev/zero bs=1024k of=tstfile count=1024')

elif x==3:
    print("Getting Partiton Data")
    os.system('diskutil list')

else:
    exit()