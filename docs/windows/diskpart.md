# diskpart

## Clean disk and create partition
Run PowerShell as Administrator
and run:

```batch
diskpart
  list disk
  select disk 1
  clean
  create partition primary
  format fs=fat32
  assign
```