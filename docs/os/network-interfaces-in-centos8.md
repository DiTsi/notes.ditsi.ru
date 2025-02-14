# Network interfaces in CentOS8

```shell
vim /etc/sysconfig/network-scripts/ifcfg-ens7
vim /etc/sysconfig/network-scripts/ifcfg-ens3 
cd /etc/sysconfig/network-scripts/
vim ifcfg-ens7
ifconfig ens7 10.100.2.4/24
vim /etc/sysconfig/network-scripts/ifcfg-ens3 
vim /etc/sysconfig/network-scripts/ifcfg-ens7
systemctl enable NetworkManager
systemctl start NetworkManager
nmcli con show
nmcli dev connect ens7
nmcli con add type ethernet con-name ens7 ifname ens7 ip4 10.100.2.4/24 gw4 10.100.2.1
nmcli connection reload 
nmcli connection show 
```

tags: network interfaces centos networkmanager