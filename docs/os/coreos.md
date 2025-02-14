# CoreOS

## Static IP

```bash
$ cat /etc/systemd/network/static.network
[Match]
Name=eth1

[Network]
Address=10.101.16.8/23
Gateway=10.101.16.1
DNS=10.101.16.10

[Route]
Gateway=10.101.16.1
Destination=10.0.0.0/8
```

## Disable static IP

```bash
# cat /etc/systemd/network/eth0.network 
[Match]
Name=eth0

[Network]
DHCP=no
```
