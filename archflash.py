import os
import time

def clear():
    os.system("clear")

def invalid():
    print("\033[31m Invalid input! Try again...\033[0m")

clear()
print('''\033[31m
!!!  WARNING  !!!

This installer can potentially wipe the drive completely... So backup any data before continuing this program

Press Ctrl+C or Ctrl+D to Terminate the program \033[0m \n''')

while True:
    res = input("Continue?(yes/no): ")
    if res.lower()=="no":
        exit()
    elif res.lower()=="yes":
        break
    else:
        invalid()
clear()
print("""Running Archflash Installation...

(Make sure you're connected to the Internet)

""")
os.system("timedatectl set-ntp true")
print("Listing connected devices and available RAM")
print("Devices and their partitions:\n")
os.system("lsblk")
print("\nRAM installed:\n")
os.system("lsmem | grep Total")
temp=input("\nContinue?(Y/n):")
if temp.lower()=="n":
    exit()
clear()
print("""This step will be of partitions...

Recommended settings:   1Gb for boot (/boot)
                        6 to 10 Gb for Swap if RAM size is 8Gb(-/+2Gb the size of RAM installed) 
                        The rest of the storage for root (/)

                        
Minimum settings:       500Mb for boot (/boot)
                        1-2Gb for swap (Optional)
                        The rest of the storage for root (/)

System Types:
                /boot   : EFI System
                swap    : Linux swap
                /       : Linux filesystem

[supports UEFI system only]

Partitioning will be done manually in cfdisk.
""")
print("\033[31m Caution! This program(at the moment) does not support separate /home partition\033[0m \n")
while True:
    os.system("lsblk")
    ans = input("Enter the drive name(Ex:sda):")
    if ans == '':
        invalid()
        continue
    try:
        open("/dev/"+ans)
    except:
        invalid()
    break
input("\nEnter to continue")
os.system("cfdisk /dev/"+ans)
while True:
    clear()
    print("Enter the partition name(Leave blank if none)")
    os.system("lsblk")
    boot = input("Partition for boot(Ex: sda1):")
    if boot != "":
        try:
            open("/dev/"+boot)
        except:
            invalid()
            continue
        os.system("mkfs.fat -F 32 /dev/"+boot)
        os.system("mkdir /mnt/boot")
        os.system("mount /dev/"+boot+" /mnt/boot")
        file_boot = open("archflash/memfile","w")
        file_boot.write(boot)
        break
while True:
    clear()
    print("Enter the partition name(Leave blank if none)")
    os.system("lsblk")
    swap = input("Partition for swap(Ex: sda2):")
    if swap != "":
        try:
            open("/dev/"+swap)
        except:
            invalid()
            continue
        os.system("mkswap /dev/"+swap)
        os.system("swapon /dev/"+swap)
        break
while True:
    clear()
    print("Enter the partition name(Leave blank if none)")
    os.system("lsblk")
    root = input("Partition for root(Ex: sda3):")
    if root != "":
        try:
            open("/dev/"+root)
        except:
            invalid()
            continue
        os.system("mkfs.ext4 /dev/"+root)
        os.system("mount /dev/"+root+" /mnt") 
        break
clear()
print("\nBuilding the base system\n")
while True:
    os.system("pacstrap /mnt base linux linux-firmware dosfstools python nano less grep")
    ans=input("\nDid the above programs installed successfully?(Y/n):")
    if ans.lower() != "n":
        break
os.system("genfstab -U -p /mnt >> /mnt/etc/fstab")
os.system("cp -r /root/archflash /mnt")
os.system("arch-chroot /mnt/ python archflash/archflash_next.py")
os.system("arch-chroot /mnt/ rm -rf archflash")
clear()
print("***Installation Complete!***\n\n")
ans = input("Reboot the system?(Y/n):")
if ans.lower() != "n":
    print("Rebooting in 5 seconds")
    time.sleep(5)
    os.system('reboot')
else:
    clear()
