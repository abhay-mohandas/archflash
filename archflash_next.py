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
os.system("clear")
pc_name=input("Enter the name of the computer:")
os.system('''echo "'''+ pc_name +'''" > /etc/hostname''')
os.system("clear")
print("The default keyboard layout is QWERTY/US")
ans=input("Change the keyboard layout?(Y/n)")
if ans.lower()!="n":
    print("Select a keyboard layout from the list(Showing only the most common ones)")
    os.system("ls /usr/share/kbd/keymaps/i386")
    key = input("Enter the keyboard standard(QWERTY/DVORAK/etc):")
    print("\nNote: press q to exit the list")
    input("\nPress Enter to show the list ")
    os.system("ls /usr/share/kbd/keymaps/i386/**/*.map.gz | grep "+key.lower()+" | less")
    keymap = input("Enter the layout name (Exclude the .map.gz extention)(Ex:us/uk/etc):")
    os.system('''echo "KEYMAP='''+keymap.lower()+'''" > /etc/vconsole.conf''')
    os.system("cd")
    input("Press Enter to continue ")
os.system("clear")
parallel=input("Enable parallel downloads?(Y/n):")
if parallel.lower()!="n":
    parallel_num = int(input("Enter the number of parallel downloads to be enabled(2-10):"))
    if parallel_num > 10:
        parallel_num = 10
    elif parallel_num < 2:
        parallel_num = 2
    os.system('echo "[options]" >> /etc/pacman.conf')
    os.system('echo "ParallelDownloads='+str(parallel_num)+'" >> /etc/pacman.conf')
os.system("clear")
print("Installing Reflector to update the mirror list...")
os.system("pacman -S reflector")
os.system("sudo systemctl enable reflector.service reflector.timer")
os.system("clear")
print("\nUpdating mirror list")
os.system("sudo systemctl start reflector.service reflector.timer")
os.system("clear")
basic_programs = '''pacman-contrib archlinux-keyring base-devel systemd usbutils lsof dialog \
zip unzip p7zip unrar lzop rsync traceroute bind-tools linux linux-headers \
networkmanager openssh cronie xdg-user-dirs haveged grub libinput dosfstools ntfs-3g btrfs-progs \
exfat-utils gptfdisk fuse2 fuse3 fuseiso pulseaudio pulseaudio-alsa alsa-utils alsa-plugins \
pulseaudio-bluetooth pulseaudio-equalizer xorg-server xorg-xinit git efibootmgr'''

print("Installing necessary/basic programs and dependencies\n")
print("The following programs will be installed:\n"+basic_programs)
while True:    
    os.system('pacman -S --needed '+basic_programs)
    ans=input("\nWas the above programs installed successfully?(Y/n):")
    if ans.lower() != "n":
        break
    print("Retrying installation...")
ans=input("Install additional software?(Y/n):")
if ans.lower() != "n":
    soft_list=input("Enter the package name to be installed(separate by space for multiple packages):")
    os.system("pacman -S "+soft_list)
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
os.system("systemctl enable sshd cronie NetworkManager")
os.system("clear")
print("GRUB Configuration...\n")
ans = input("Enter the name of the boot partition:")
os.system("pacman -S --needed efibootmgr")
os.system("mkdir /boot/efi")
os.system("mount /dev/"+ans+" /boot/efi")
os.system("grub-install --target=x86_64-efi --bootloader-id=GRUB --efi-directory=/boot/efi")
os.system("mkdir /boot/grub")
os.system("grub-mkconfig -o /boot/grub/grub.cfg")
input("Press Enter to continue ")
os.system("clear")
print("Set the root password")
os.system("passwd root")
os.system("clear")
user_list = []
while True:
    account_name=input("Enter the user account name(Leave blank to continue):")
    if account_name.lower() == "":
        break
    os.system("useradd -m "+account_name)
    print("Set the password for user account "+account_name)
    os.system("passwd "+account_name)
    ans=input("\nAdd user "+account_name+" to sudoers file?(Y/n):")
    if ans.lower()!="n":
        os.system('echo "'+account_name+' ALL= (ALL)ALL" >> /etc/sudoers')
    user_list.append(account_name)
os.system("clear")
aur_list=["yay","paru","trizen","aura","none"]
ans=input("Do you want to install an AUR helper?(Y/n):")
if ans.lower() != "n":
    y=1
    print("Since root users are not allowed to build/install AUR helper directly, one of the previously created user accounts will be used")
    if len(user_list) <= 1:
        aur_account = user_list[0]
        print("Using user account '"+aur_account+"'")
    else:
        while True:
            print("Multiple user accounts found:")
            for x in user_list:
                print(str(y)+")"+x)
                y+=1
            aur_account = input("Enter the account name to be used(Requires sudo previlages):")
            if aur_account in user_list:
                print("Using user account '"+aur_account+"'")
                break
            print("Invalid Input! Try again")
            y=1
    y=1
    while True:
        print("List of AUR helpers:")
        for x in aur_list:
            print(str(y)+")"+x)
            y += 1
        aur_helper = input("Enter the name of the AUR helper from the above list:")
        if aur_helper.lower() in aur_list:
            if aur_helper.lower() == "none":
                break
            os.system("sudo -u "+aur_account+" -- git clone https://aur.archlinux.org/"+aur_helper+".git /home/"+aur_account+"aurbuilder")
            os.system("sudo -u "+aur_account+" -- bash -c 'cd /home/"+aur_account+"/aurbuilder && makepkg -si'")
        else:
            print("Invalid option! To cancel the AUR helper installation, enter 'none' ")
        y=1
while True:
    a = input("Custom command(Leave blank to skip): ")
    if a == "":
        break
    os.system(a)
