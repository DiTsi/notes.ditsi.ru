# lvm-tools

[https://habr.com/post/67283/](https://habr.com/post/67283/)

## Theory

**PV (Physical Volume)** - these can be partitions or entire “unpartitioned” disks

**VG (Volume Group)** - we combine physical volumes (PV) into a group, create a single disk, which we will further partition as we want

**LV (Logical Volume)** - logical partitions, the actual partition of our new “single disk” aka Volume Group, which we then format and use as a regular partition, a regular hard drive.

## Work sequence

It is best to contact the Pallas's manual by command. Help's are poor and designed to help people who already know

```bash
# if you use whole disk drive, clear first sector of disk. For more information: man pvcreate
dd if=/dev/zero of=/dev/sdz bs=512 count=1

# Create PV
pvcreate /dev/sdb

# Create VG "data"
vgcreate data /dev/sdz

# Create Logical Volume
lvcreate -n data0 -l 100%VG data

mkfs.ext4 /dev/data/data0
```

## Useful commands

```bash
lvextend --resize -l +100%FREE /dev/volgroup/logvol
```
