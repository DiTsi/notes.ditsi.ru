# fdisk

```bash
Disk /dev/sda: 465.76 GiB, 500107862016 bytes, 976773168 sectors
Disk model: Samsung SSD 850 
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: A89BC90C-6B0B-4EEB-AECF-EF8368247834
```

Partition alignment is used to align the logical and physical sizes of sectors

The processor reads the first sector. Of them:
```
446 bytes for loader (for processor) 
64 bytes 4x16 bytes allocated for (CHS):
 1 - 0x00, 0x80 (boot)  
 5 - disk id
 8-12 - start sector  
 13-16 - sectors  
2 bytes - for MBR signature:  
 0x55 0xaa - this seems to mean that everything is OK
```

Question about superblock

cat /proc/partitions

\#block = 1024b

## Resize partition

- fdisk  
- recreate the partition, specifying a new size
- cat /proc/partitions  
- partprobe  
- resize2fs /dev/sda1
---
- lvresize /dev/mapper/disk -L 25G  
- virsh blockresize ...  
- delete a partition, create a partition 
- partprobe