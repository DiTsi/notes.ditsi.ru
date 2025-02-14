# Resize EXT4 Drive

```bash
# 0. Stop Instance
# 1. Resize Virtual Drive
# 2. Mount archlinux boot CD
# 3. Resize partitions on /dev/vda
    # 3.1 check partitions
    fdisk -l
    # 3.2 run parted with you drive
    parted /dev/vda
        # 3.2.1 resize partition (check number with "print" command)
        resizepart 2 100%
        # 3.2.3 quit
        quit
    # 3.3 resize ext4 filesystem
    resize2fs /dev/sda2
    # 3.4 run check 
    e2fsck /dev/sda2
# 4. poweroff
poweroff
# 5. Unmount archlinux boot CD
# 6. Run Instance
```
