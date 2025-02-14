# CD, DVD

## Commands

```bash
# Make an ISO of a directory. Type to make an ISO from files on your hard drive:
mkisofs -o /tmp/cd.iso /tmp/directory/

# erase disk:
dvd+rw-format -force /dev/scd0

# burn ISO image:
growisofs -speed=1 -Z /dev/scd0=/home/ditsi/temp/archlinux-2010.05-core-i686.iso

# check md5sum:
blocks=$(expr $(du -b image.iso | awk '{print $1}') / 2048)
dd if=/dev/sr0 bs=2048 count=$blocks | md5sum
```

## Old commands:

```bash
# erase disk
wodim dev=/dev/scd0 -force -blank=all

#write ISO image
wodim dev=/dev/scd0 speed=4 install-x86-minimal-20110208.iso
```
