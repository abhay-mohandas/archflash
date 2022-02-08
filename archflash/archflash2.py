import os

print("Setting up Locaton and Language information...")
region=input("Enter the location region(Ex:Asia/Europe/America):")
os.system("ls /usr/share/zoneinfo/"+region.capitalize())
city=input("Enter the city name from the list")
os.system("ln -sf /usr/share/zoneinfo/"+region.capitalize()+"/"+city.capitalize()+" /etc/localtime")
os.system("hwclock --systohc")
os.system("locale-gen")
