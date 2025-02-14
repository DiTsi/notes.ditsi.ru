# Debian

## networking

static IP
```ini
# /etc/network/interfaces
auto lo
iface lo inet loopback

allow-hotplug ens3
iface ens3 inet static
  address 54.54.13.52
  netmask 255.255.254.0
  gateway 54.54.13.1
  dns-nameservers 8.8.8.8
```

routing configures by scripts in /etc/uf-up.d/