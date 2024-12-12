# samba

## links
[https://computingforgeeks.com/how-to-configure-samba-share-on-debian/](https://computingforgeeks.com/how-to-configure-samba-share-on-debian/)

you need to configure static ip... 192.168.0. !!!It’s important not to forget to set write permissions on the shared folder

/etc/samba/smb.conf

```INI
[global]
workgroup = MSHOME
server string = DiTsi
# interfaces = eth0 192.168.0.1/255.255.255.0
# bind interfaces only = yes
invalid users = root @root
#hosts deny = ALL
hosts allow = 192.168.0.
display charset = CP1251
dos charset = CP866
security = share
guest only = yes
#guest account = nobody
#encrypt passwords = yes
log file = /var/log/samba/log.%m
smb passwd file = /etc/samba/smbpasswd
#printer name = Canon MP160 Printer
#create mask = 0775

[share]
path = /home/ditsi/temp/share/
#writeable=yes
#browseable = yes
#public = yes
read only = no
```
