import os


os.system("clear")
print("Configuration and setup...")
print("Setting up Locaton and Language information...")
zone_dir=['Africa','America','Antartica','Arctic','Asia','Atlantic','Australia','Brazil','Canada','Chile','Etc','Europe','Indian','Mexico','Pacific','US']
os.system("ls /usr/share/zoneinfo")
region=input("Enter the location region(Ex:Asia/Europe/America):")
os.system("clear")
if region.capitalize() in zone_dir or region.upper()=="US":
    os.system("ls /usr/share/zoneinfo/"+region.capitalize())
    city=input("Enter the city name from the list(Ex:Kolkata/London/Phoenix):")
    os.system("ln -sf /usr/share/zoneinfo/"+region.capitalize()+"/"+city.capitalize()+" /etc/localtime")
else:
    os.system("ln -sf /usr/share/zoneinfo/"+region.capitalize()+" /etc/localtime")
os.system("clear")
os.system("hwclock --systohc")
print("Next step is to edit the locale file by uncommenting the necessary locales and saving the file...")
input("Press Enter to continue")
os.system("nano /etc/locale.gen")
os.system("locale-gen")
pc_name=input("Enter the name of the computer:")
os.system('''echo "'''+ pc_name +'''" > /etc/hostname''')
os.system("clear")
print("The default keyboard layout is QWERTY/US")
ans=input("Change the keyboard layout?(Y/n)")
if ans.lower()!="n":
    print("Select a keyboard layout from the list(Showing only the most common ones)")
    key = input("Enter the keyboard standard(QWERTY/DVORAK/etc):")
    print("Note: press q to exit the list")
    input("Press Enter to continue ")
    os.system("cd /usr/share/kbd/keymaps/i386")
    os.system("ls **/*.map.gz | grep "+key.lower()+" | less")
    keymap = input("Enter the layout name (Exclude the .map.gz extention)(Ex:us/uk/etc):")
    os.system('''echo "KEYMAP='''+keymap.lower()+'''" > /etc/vconsole.conf''')
    input("Press Enter to continue ")
os.system("clear")
print("Installing necessary files and dependencies\n")
os.system('''pacman -S --needed dhcpcd pacman-contrib archlinux-keyring base-devel usbutils lsof dialog \
                    zip unzip p7zip unrar lzop rsync traceroute bind-tools linux linux-headers \
                    networkmanager openssh cronie xdg-user-dirs haveged''')


