# mdadm

```bash
# Create RAID1 (mirror) array:
sudo mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 /dev/sda /dev/sdb

# Show create progress
cat /proc/mdstat

# Save the array layout
# To make sure that the array is reassembled automatically at boot, we will have to adjust the /etc/mdadm/mdadm.conf file. You can automatically scan the active array and append the file by typing:
mdadm --detail --scan | tee -a /etc/mdadm/mdadm.conf

# Show RAID details
mdadm --detail /dev/md0

# Stop RAID
mdadm --stop /dev/md0

# Remove RAID
mdadm --remove /dev/md0

# Remove superblock to prevent automatically build raid after load
mdadm --zero-superblock /dev/md0 /dev/md1
```
