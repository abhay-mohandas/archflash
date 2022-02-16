import os

os.system('clear')
print('''
!!!  WARNING  !!!

This installer can potentially wipe the drive completely... So backup any data before continuing this program

Press Ctrl+C or Ctrl+D to Terminate the program''')

while True:
    res = input("Continue?(yes/no): ")
    if res.lower()=="no":
        exit()
    elif res.lower()=="yes":
        break
    else:
        print("Invalid option")
os.system("clear")
print("""Running Archflash Installation...
(Make sure you're connected to the Internet)
""")
os.system("timedatectl set-ntp true")
print("Listing connected devices and available RAM")
print("Devices:")
os.system("fdisk -l")
print("\nRAM installed:")
os.system("lsmem | grep Total")
temp=input("\nContinue?(Y/n):")
if temp.lower()=="n":
    exit()
os.system("clear")
print("""Next step will be of partitions...

Recommended settings:   1Gb for boot (/boot)
                        6 to 10 Gb for Swap if RAM size is 8Gb(-/+2Gb the size of RAM installed) 
                        The rest of the storage for root (/)

                        
Minimum settings:       500Mb for boot (/boot)
                        1-2Gb for swap (Values close to the RAM installed in the system) 
                        The rest of the storage for root (/)

System Types:
                /boot   : EFI System(If efi is available)
                 swap   : Linux swap
                /       : Linux filesystem

Partitioning will be done manually in cfdisk.
""")
print("Caution! This program(at the moment) does not support separate /home partition\n")
ans = input("Enter the device name(Ex:sda):")
input("Enter to continue")
os.system("cfdisk /dev/"+ans)
print("Enter the partition names(Leave blank if none)")
boot = input("Partition for boot(Ex: sda1):")
swap = input("Partition for swap(Ex: sda2):")
root = input("Partition for root(Ex: sda3):")
print("Formatting the partitions...")
if boot != "":
    os.system("mkfs.fat -F 32 /dev/"+boot)
    os.system("mkdir /mnt/boot")
    os.system("mount /dev/"+boot+" /mnt/boot")
if swap != "":
    os.system("mkswap /dev/"+swap)
    os.system("swapon /dev/"+swap)
if root != "":
    os.system("mkfs.ext4 /dev/"+root)
    os.system("mount /dev/"+root+" /mnt")

print("\nBuilding the base system\n")
os.system("pacstrap /mnt base linux linux-firmware dosfstools python nano less grep")
os.system("genfstab -U -p /mnt >> /mnt/etc/fstab")
os.system("cp /root/archflash/archflash_next.py /mnt")
print("Mounting drives...")
os.system("arch-chroot /mnt/ python archflash_next.py")
os.system("clear")
print("Installation Complete!\n")
ans = input("Reboot the system?(Y/n):")
if ans.lower() != "n":
    os.system('reboot')
else:
    os.system("clear")
