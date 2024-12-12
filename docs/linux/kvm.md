# kvm

### Share directory

#### Windows 10

- enable Memory -> Shared Memory in kvm settings
- add device Filesystem virtiofs in kvm settings

- install winfsp (from github)
- install latest virtio-win-guest-tools.exe 
```powershell
sc.exe create VirtioFsSvc binpath="C:\Program Files\Virtio-Win\VioFS\virtiofs.exe" start=auto depend="WinFsp.Launcher/VirtioFsDrv" DisplayName="Virtio FS Service"
sc.exe start VirtioFsSvc
```
- if error "A device attached to the system is not functioning" add 'queue="1024"' to filesystem share, to be: '<driver type="virtiofs" queue="1024"/>'

#### Linux

1. Enable shared memory
2. Add Hardware (File system), add you folder (target path should be just simple name)
3. Mount folder in VM: `sudo mount -t virtiofs target_path_name /mnt/pictures`


### Share clipboard

#### Windows

- download https://www.spice-space.org/download/windows/spice-guest-tools/spice-guest-tools-latest.exe
- install it

#### Linix

- install spice-vdagent, start agent


### Create disk image

```bash
cd /var/lib/libvirt/images/
qemu-img create -f raw ubuntu-box1-vm-disk1-5G 5G
dd if=/dev/zero of=ubuntu-box1-vm-disk1-5G bs=1M count=5120 status=progress
```

### Create new VM

```bash
virt-install -n myRHELVM1 --description "Test VM with RHEL 6" --os-type=Linux --os-variant=rhel6 --ram=2048 --vcpus=2 --disk path=/var/lib/libvirt/images/myRHELVM1.img,bus=virtio,size=10 --graphics none --cdrom /var/rhel-server-6.5-x86_64-dvd.iso --network bridge:br0
```

```bash
virt-install -n ubuntu20.04 --description "Ubuntu 20.04" --os-variant=ubuntu20.04 --ram=4096 --vcpus=1 --disk path=/data/kvm/ubuntu20.04/ubuntu20.04.img,bus=virtio,size=50 --graphics vnc,listen=127.0.0.1,port=-1 --console pty,target_type=serial --cdrom '/data/kvm/ubuntu20.04/ubuntu-20.04.6-live-server-amd64.iso' --network bridge:virbr0
```

### VM creating process

```bash
# ON THE REMOTE HOST
qemu-img create -f raw /storage/<image> 40G
dd if=/dev/zero of=/storage/<image> bs=1048576 count=40960 status=progress
virt-install -n <domain> -r 4096 -f /storage/<image> -s 40 -c <iso> --accelerate --os-type=linux --os-variant=<os-variant> -v --graphics vnc,port=5601 -w bridge:br0

# ON THE LOCAL MACHINE:
ssh -L 55555:127.0.0.1:5601 dtsybus@<remote_ip_address>
# connect with vnc to 127.0.0.1:55555 with your app
```

### VM remove

```bash
virsh destroy <VM>
virsh undefine <VM>
```

### Change VM settings with boot iso

```bash
virt-install -n just --description "Test VM with RHEL 6" --os-type=Linux --ram=2048 --vcpus=2 --disk path=<img>,bus=virtio --graphics vnc,port=55603 --cdrom <iso> --network bridge:br0 --check path_in_use=off

# on local host
ssh -L 55555:127.0.0.1:5601 dtsybus@<remote_ip_address>

virsh destroy <VM>
virsh undefine <VM>
```

### clone

```bash
virt-clone --original rabbit1 --name rabbit2 --file /home/ditsi/.qemu/img/rabbit2.img
```

## virsh

#### Commands

```bash
# displays the block statistics for the first block device defined for the domain
virsh domblklist

# information about VM
virsh dominfo <VM>

# list vms
virsh list [--all]

# show settings
virsh dumpxml gitlab

# edit VM (RAM, CPU, etc)
virsh edit name_vhost

# shutdown
virsh shutdown <vm>

# force shutdown
virsh destroy <vm>

# remove VM
virsh undefine <vm>

# create snapshot
virsh snapshot-create-as --domain webserver --name webserver_snap

# change RAM for VM
virsh setmem DOMAIN_NAME 4G --live # --live, --config, --current
```

VNC port

```bash
# connect to vnc
[root@ultrabook ditsi]# virsh list
 Id   Name      State
-------------------------
 7    rabbit2   running
 9    rabbit1   running
 10   rabbit3   running

[root@ultrabook ditsi]# virsh vncdisplay 10
127.0.0.1:0
# 0 means port 5900


```

#### VNC

[https://linux-notes.org/vnc-dostup-k-virtual-noj-mashine-kvm/](https://linux-notes.org/vnc-dostup-k-virtual-noj-mashine-kvm/)
