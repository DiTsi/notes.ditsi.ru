# Install over Debian

link: [https://medium.com/@kvapss/easy-way-for-install-mikrotiks-cloud-hosted-router-on-any-cloud-vm-fb1cf7302b85](https://medium.com/@kvapss/easy-way-for-install-mikrotiks-cloud-hosted-router-on-any-cloud-vm-fb1cf7302b85)

```
# install unzip
apt-get update
apt-get -y install unzip

mount -t tmpfs tmpfs /tmp/
cd /tmp
# go to https://www.mikrotik.com/download and download “Cloud Hosted Router” raw-image
wget https://download.mikrotik.com/routeros/6.44.3/chr-6.44.3.img.zip
unzip chr-6.44.3.img.zip

### CHECK TARGET DEVICE!
dd if=chr-6.44.3.img of=/dev/vda bs=4M oflag=sync
#echo 1 > /proc/sys/kernel/sysrq 
echo b > /proc/sysrq-trigger
```