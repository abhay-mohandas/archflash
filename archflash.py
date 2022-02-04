import os
import time

os.system('clear')
print("""Running Archflash Installation...
(Make sure you're connected to the Internet)
""")
os.system("timedatectl set-ntp true")
print("Listing connected devices")
os.system("fdisk -l")
temp=input("Continue?(y/n):")
if temp.lower()=="n":
    exit()
print("""Next step will be of partitions
Recommended settings:   1Gb for boot (/boot)
                        4-6Gb for swap (Values close to the RAM installed in the system) 
                        The rest of the storage for root (/)
                        
Minimum settings:       500Mb for boot (/boot)
                        2Gb for swap (Values close to the RAM installed in the system) 
                        The rest of the storage for root (/)""")
input("Enter to continue")
os.system("cfdisk")
boot = input("Partition for boot(Ex: sda1):")
swap = input("Partition for swap(Ex: sda2):")
root = input("Partition for root(Ex: sda3):")
print("Formatting the partitions...")
os.system("mkfs.ext4 /dev/"+root)
os.system("mkswap /dev/"+swap)
os.system("mkfs.fat -F 32 /dev/"+boot)
os.system("mount /dev/"+root+" /mnt")
os.system("mkdir /mnt/boot")
os.system("mount /dev/"+boot+" /mnt/boot")
os.system("swapon /dev/"+swap)
print("Updating mirror list")
os.system("reflector")
print("Building the base system")
os.system("pacstrap /mnt base linux linux-firmware ")
