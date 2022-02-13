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
os.system("hwclock --systohc --utc")
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
    os.system("ls /usr/share/kbd/keymaps/i386")
    key = input("Enter the keyboard standard(QWERTY/DVORAK/etc):")
    print("Note: press q to exit the list")
    input("Press Enter to continue ")
    os.system("ls /usr/share/kbd/keymaps/i386/**/*.map.gz | grep "+key.lower()+" | less")
    keymap = input("Enter the layout name (Exclude the .map.gz extention)(Ex:us/uk/etc):")
    os.system('''echo "KEYMAP='''+keymap.lower()+'''" > /etc/vconsole.conf''')
    os.system("cd")
    input("Press Enter to continue ")
os.system("clear")
parallel=input("Enable parallel downloads?(Y/n):")
if parallel.lower()!="n":
    parallel_num = input("Enter the number of parallel downloads to be enabled(2-7):")
    if parallel_num > 7:
        parallel_num = 7
    elif parallel_num < 2:
        parallel_num = 2
    os.system('echo "ParallelDownloads='+str(parallel_num)+'" > /etc/pacman.conf')
os.system("clear")
print("Installing Reflector to update the mirror list...")
os.system("pacman -S reflector")
os.system("sudo systemctl enable reflector.service reflector.timer")
os.system("clear")
print("\nUpdating mirror list")
os.system("sudo systemctl start reflector.service reflector.timer")
os.system("clear")
print("Installing necessary files and dependencies\n")
os.system('''pacman -S --needed dhcpcd pacman-contrib archlinux-keyring base-devel systemd usbutils lsof dialog \
                    zip unzip p7zip unrar lzop rsync traceroute bind-tools linux linux-headers \
                    networkmanager openssh cronie xdg-user-dirs haveged grub libinput dosfstools ntfs-3g btrfs-progs \
                    exfat-utils gptfdisk fuse2 fuse3 fuseiso pulseaudio pulseaudio-alsa alsa-utils alsa-plugins \
                    pulseaudio-bluetooth pulseaudio-equalizer xorg-server xorg-xinit git''')
vendor_name=['amd','intel','other']
while True:
    vendor=str(input("Enter the processor vendor name (AMD/Intel):"))
    if vendor.lower() in vendor_name:
        if vendor.lower() == 'other':
            break
        os.system("pacman -S --needed "+vendor.lower()+"-ucode")
        break
    else:
        print("Invalid Option! Try again...(If your processor vendor is other than AMD and Intel, Enter 'other' as the vendor name)")
os.system("clear")
aur_list=["yay","paru","trizen","aura","none"]
ans=input("Do you want to install an AUR helper(Ex:yay)?(Y/n):")
y=1
if ans.lower() != "n":
    while True:
        print("List of AUR helpers:")
        for x in aur_list:
            print(str(y)+")"+x)
        aur_helper = input("Enter the name of the AUR helper from the above list:")
        if aur_helper.lower() in aur_list:
            if aur_helper.lower() == "none":
                break
            os.system("git clone https://aur.archlinux.org/"+aur_helper+".git")
            os.system("cd "+aur_helper)
            os.system("makepkg -si")
            os.system("cd")
            os.system("rm -rf "+aur_helper)
        else:
            print("Invalid option! To cancel the AUR helper installation, enter 'none' ")
            y=1
os.system("clear")
os.system("systemctl disable dhcpcd")
os.system("systemctl enable sshd")
os.system("systemctl enable cronie")
os.system("systemctl enable NetworkManager")
os.system("systemctl enable numlockon")
print("Configuring GRUB...\n")
os.system("mkdir /boot/grub")
os.system("grub-mkconfig -o /boot/grub/grub.cfg")
input("Press Enter to continue ")
os.system("clear")
print("Set the root password")
os.system("passwd root")
os.system("clear")
account_name=input("Enter the user account name:")
os.system("useradd -m "+account_name)
print("Set the password for user account "+account_name)
os.system("passwd "+account_name)
os.system("exit")

