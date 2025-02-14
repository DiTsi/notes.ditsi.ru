# mount

Mounting encrypted NTFS drive in Linux

```
/dev/nvme0n1p4 /home/ditsi/.mnt/dislocker-file  fuse.dislocker  recovery-password=107415-179267-473825-204952-351582-127215-631598-303699  0  0
/home/ditsi/.mnt/dislocker-file/dislocker-file  /home/ditsi/.mnt/windows  auto  user,rw,nofail,x-gvfs-show  0  0
/home/ditsi/.mnt/windows/Users/ditsi/Desktop  /home/ditsi/windows  none  defaults,bind  0  0
```
