import os

def clear():
    os.system("clear")

def install(packages):
    os.system("pacman -S --needed "+packages)


def wm():
    clear()
    wm_list =  [["Stacking","fluxbox","openbox"],
                ["Manual Tiling","bspwm","herbstluftwm","i3"],
                ["Dynamic","awesome","spectrwm","qtile","xmonad"]]
    while True:
        print("List of Window Managers:")
        for x in wm_list:
            print(x[0]+":")
            for y in x[1:]:
                print("    ",y)
            print()
        wm_ans = input("Enter the name of the WM(Leave the input blank to cancel): ")
        if wm_ans == "":
            return
        for x in wm_list:
            if wm_ans.lower() in x:
                    install(wm_ans.lower())
                    return wm()
        clear()
        print("\nInvalid Input!\n")


def de():
    clear()
    de_list =  [["Gnome",["gnome","(Standard)"],["gnome-shell","(Minimal)"],["gnome-extra","(Standard with extra packages)"]],
                ["KDE plasma",["plasma","(Standard)"],["plasma-desktop","(Minimal)"]],
                ["Cinnamon",["cinnamon","(Standard)"]],
                ["XFCE",["xfce4","(Standard)"]],
                ["Budgie",["budgie-desktop","(Standard)"]],
                ["LXQT",["lxqt","(Standard)"]],
                ["MATE",["mate","(Standard)"]],
                ["Deepin",["deepin","(Standard)"],["deepin-extra","(Standard with extra packages)"]]]
    while True:
        print("List of Desktop Environments:")
        for x in de_list:
            print(x[0]+":")
            for y in x[1:]:
                print("    ",y[0],y[1])
            print()
        de_ans = input("Enter the name of the DE(Leave the input blank to cancel): ")
        if de_ans == "":
            return
        for x in de_list:
            for y in x[1:]:
                if de_ans.lower() in y:
                    install(y[0])
                    return de()
        clear()
        print("\nInvalid Input!\n")


def de_wm():
    clear()
    ans=input("Install a Desktop Environment/Window Manager?(Y/n):")
    while True:
        if ans.lower() != "n":
            print('''Select one of the options:
                1)DE (Desktop Environment)
                2)WM (Window Manager)''')
            de_or_wm=input("Enter the option(Leave the input blank to cancel): ")
            if ("de" in de_or_wm.lower()) or ("1" in de_or_wm.lower()):
                de()
            elif ("wm" in de_or_wm.lower()) or ("2" in de_or_wm.lower()):
                wm()
            elif de_or_wm == "":
                return
            else:
                print("\nInvalid Input!\n")

def open_video():
    clear()
    open_driver_list =     [["1","xf86-video-amdgpu","amd"],
                            ["2","xf86-video-intel","intel"],
                            ["3","xf86-video-ati","ati"],
                            ["4","xf86-video-nouveau","nvidia"],
                            ["5","xf86-video-dummy","dummy"],
                            ["6","xf86-video-fbdev","frame buffer"],
                            ["7","xf86-video-vesa","vesa"],
                            ["8","xf86-video-voodoo","voodoo"]]
    while True:
        print("List of Open Source video driver:")
        for x in open_driver_list:
            print(x[0]+")"+x[1]+" ("+x[2].upper()+")")
        driver_ans = input("Enter the name/number of the option(Leave the input blank to cancel): ")
        if driver_ans == "":
            return
        for x in open_driver_list:
            if driver_ans.lower() in x:
                install(x[1])
                return open_video()        
        clear()
        print("\nInvalid Input!\n")



def closed_video():
    clear()
    closed_driver_list  =  [["1","nvidia","nvidia"]]
    while True:
        print("List of Closed Source video driver:")
        for x in closed_driver_list:
            print(x[0]+")"+x[1]+" ("+x[2].upper()+")")
        driver_ans = input("Enter the name/number of the option(Leave the input blank to cancel): ")
        if driver_ans == "":
            return
        for x in closed_driver_list:
            if driver_ans.lower() in x:
                install(x[1])
                return closed_video()        
        clear()
        print("\nInvalid Input!\n")

def xorg_input():
    clear()
    xorg_input_list  = [["1","xf86-input-evdev","evdev input driver"],
                        ["2","xf86-input-libinput","Generic input driver for the Xorg server based on libinput"],
                        ["3","xf86-input-synaptics","Synaptics driver for notebook touchpads"],
                        ["4","xf86-input-vmmouse","VMWare mouse input driver"],
                        ["5","xf86-input-void","void input driver"]]
    while True:
        print("List of Xorg input driver:")
        for x in xorg_input_list:
            print(x[0]+")"+x[1]+" ("+x[2].capitalize()+")")
        input_ans = input("Enter the name/number of the option(Leave the input blank to cancel): ")
        if input_ans == "":
            return
        for x in xor_input_list:
            if input_ans.lower() in x:
                install(x[1])
                return xorg_input()        
        clear()
        print("\nInvalid Input!\n")


def drivers():
    clear()
    ans=input("Install video drivers?(Y/n):")
    if ans.lower() == "n":
        return
    while True:
        print("""List of types of video driver to install:
    1) Open Source video driver (AMD,ATI,Intel,Other Xorg video drivers) 
    2) Closed Source video driver(Nvidia)
    3) Xorg input drivers (Ex:libinput)

Note:Open source Nvidia drivers are also listed(Under Open Source option) but installing it is depreciated
     Drivers available in the AUR needs to be installed manually\n""")
        video_type = input("Enter the option number (1/2/3):")
        if video_type == "1":
            open_video()
        elif video_type == "2":
            closed_video()
        elif video_type == "3":
            xorg_input()
        elif video_type == "":
            return
        else:
            clear()
            print("\nInvalid Input!(Leave the input blank to cancel)\n")



clear()
print("Configuration and setup...")
print("Setting up Locaton and Language information...")
zone_dir=['Africa','America','Antartica','Arctic','Asia','Atlantic','Australia','Brazil','Canada','Chile','Etc','Europe','Indian','Mexico','Pacific','US']
os.system("ls /usr/share/zoneinfo")
region=input("Enter the location region(Ex:Asia/Europe/America):")
clear()
if region.capitalize() in zone_dir or region.upper()=="US":
    os.system("ls /usr/share/zoneinfo/"+region.capitalize())
    city=input("Enter the city name from the list(Ex:Kolkata/London/Phoenix):")
    os.system("ln -sf /usr/share/zoneinfo/"+region.capitalize()+"/"+city.capitalize()+" /etc/localtime")
else:
    os.system("ln -sf /usr/share/zoneinfo/"+region.capitalize()+" /etc/localtime")
clear()
os.system("hwclock --systohc --utc")
print("Next step is to edit the locale file by uncommenting the necessary locales and saving the file...")
input("Press Enter to continue")
os.system("nano /etc/locale.gen")
os.system("locale-gen")
clear()
pc_name=input("Enter the name of the computer:")
os.system('''echo "'''+ pc_name +'''" > /etc/hostname''')
clear()
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
clear()
parallel=input("Enable parallel downloads?(Y/n):")
if parallel.lower()!="n":
    parallel_num = int(input("Enter the number of parallel downloads to be enabled(2-10):"))
    if parallel_num > 10:
        parallel_num = 10
    elif parallel_num < 2:
        parallel_num = 2
    os.system('echo "[options]" >> /etc/pacman.conf')
    os.system('echo "ParallelDownloads='+str(parallel_num)+'" >> /etc/pacman.conf')
clear()
print("Installing Reflector to update the mirror list...")
os.system("pacman -S reflector")
os.system("sudo systemctl enable reflector.service reflector.timer")
clear()
print("\nUpdating mirror list")
os.system("sudo systemctl start reflector.service reflector.timer")
clear()
basic_programs = '''pacman-contrib archlinux-keyring base-devel systemd usbutils lsof dialog \
zip unzip p7zip unrar lzop rsync traceroute bind-tools linux linux-headers \
networkmanager openssh cronie xdg-user-dirs haveged grub libinput dosfstools ntfs-3g btrfs-progs \
exfat-utils gptfdisk fuse2 fuse3 fuseiso pulseaudio pulseaudio-alsa alsa-utils alsa-plugins \
pulseaudio-bluetooth pulseaudio-equalizer xorg-server xorg-xinit git efibootmgr'''
print("\nInstalling necessary/basic programs and dependencies\n")
print("The following programs will be installed:\n"+basic_programs+"\n")
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
clear()
os.system("systemctl enable sshd cronie NetworkManager")
clear()
print("GRUB Configuration...\n")
ans = input("Enter the name of the boot partition:")
os.system("pacman -S --needed efibootmgr")
os.system("mkdir /boot/efi")
os.system("mount /dev/"+ans+" /boot/efi")
os.system("grub-install --target=x86_64-efi --bootloader-id=GRUB --efi-directory=/boot/efi")
os.system("mkdir /boot/grub")
os.system("grub-mkconfig -o /boot/grub/grub.cfg")
input("Press Enter to continue ")
clear()
print("Set the root password")
os.system("passwd root")
clear()
user_list = []
while True:
    account_name=input("\nEnter the user account name(Leave blank to continue):")
    if account_name.lower() == "":
        break
    os.system("useradd -m "+account_name)
    print("Set the password for user account "+account_name)
    os.system("passwd "+account_name)
    ans=input("\nAdd user "+account_name+" to sudoers file?(Y/n):")
    if ans.lower()!="n":
        os.system('echo "'+account_name+' ALL= (ALL)ALL" >> /etc/sudoers')
    user_list.append(account_name)
clear()
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
            aur_account = input("Enter the account name to be used(Requires users with sudo previlages):")
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
            os.system("sudo -u "+aur_account+" -- bash -c 'git clone https://aur.archlinux.org/"+aur_helper+".git /home/"+aur_account+"/"+aur_helper+"'")
            os.system("sudo -u "+aur_account+" -- bash -c 'cd /home/"+aur_account+"/"+aur_helper+" && makepkg -si'")
            break
        else:
            print("Invalid option! To cancel the AUR helper installation, enter 'none' ")
        y=1
clear()
de_wm()
drivers()
while True:
    a = input("Enter custom command to be executed(Leave blank to skip): ")
    if a == "":
        break
    os.system(a)
