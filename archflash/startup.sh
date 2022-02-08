#! /bin/sh

exec python /root/archflash/archflash1.py
exec cp /root/archflash2.py /mnt/
exec arch-chroot /mnt /bin/python archflash2.py