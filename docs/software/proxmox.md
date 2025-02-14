# proxmox

## Boot order

To change boot order press ESC at boot PROXMOX LOGO

## Commands

```bash
# stop all machines (that tries to shutdown first)
qm stopall

# list all machines
qm list

# shutdown machine
qm shutdown <id>
```

## Backup and restore

```bash
# backup
vzdump 103 --dumpdir /home/user/backup -tmpdir /root/

# restore
qmrestore vzdump-qemu-019-2018_10_14-15_13_31.vma 501
```
