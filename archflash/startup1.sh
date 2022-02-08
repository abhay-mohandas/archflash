#! /bin/sh

exec python /root/archflash/archflash/archflash1.py
exec cp /root/archflash/archflash/* /mnt/
exec arch-chroot /mnt ./startup2.sh