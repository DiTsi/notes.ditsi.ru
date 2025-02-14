# Active Directory

## Commands

Show roles:
```Powershell
netdom query fsmo
```

Move roles to another DC:
```Powershell
# run cmd as Administrator
regsvr32 schmmgmt.dll
ntdsutil
```

Domain controller:
```Powershell
# show DHCP servers
.\netsh.exe dhcp show server
```

Get-ADUser:
```Powershell
Get-ADUser -Filter '(objectclass -eq "Person" ) -and (SamAccountName -like "vsroman9")'
```