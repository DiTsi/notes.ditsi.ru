# virtualbox

## Installing Guest Additions

```bash
apt-get install build-essential module-assistant
```

you can download [here](https://download.virtualbox.org/virtualbox/6.0.2/)

## ssh access to guest VM

```bash
VBoxManage modifyvm "debian 9" --natpf1 "ssh,tcp,,3022,,22"
apt-get install openssh-server
ssh -p 3022 user@127.0.0.1
```

## Mount shared folder in Linux guest

Set permanent shared folder in VB

```bash
mount -t vboxsf shared_folder_name ~/path_to_guest_folder
```

## Errors

- VirtualBox: mount.vboxsf: mounting failed with the error: No such device
  ```bash
  cd /opt/VBoxGuestAdditions-\*/init   
  sudo ./vboxadd setup
  ```

## setting up work with usb (like for a Linux machine)

In short, you need to do this:
Add yourself to the vboxusers group (if you haven’t already):

```bash
nano /etc/group...
```

or

```bash
sudo usermod -a -G vboxusers %username%
```

Then we find out the GID of the vboxusers group:

```bash
cat /etc/group | grep vboxusers
```

/etc/fstab

```bash
none /proc/bus/usb usbfs devgid=%vboxusers_gid%,devmode=664 0 0
```

## using a real hard drive

In the documentation you can find a description of how to connect a real hard drive to run Windows or Linux.

### Linux
On Linux you need to write the following command:
VBoxManage internalcommands createrawvmdk -filename ~/.VirtualBox/VDI/localhost.vmdk -rawdisk /dev/sda

  
### Windows XP  
For Windows the situation is similar: 
"C:\\Program Files\\Sun\\xVM VirtualBox\\VBoxManage" internalcommands createrawvmdk -filename "%USERPROFILE%\\.VirtualBox\\VDI\\localhost.vmdk" -rawdisk \\\\.\\PhysicalDrive0

\######### from forum:

But when added to VirtualBox for some reason it says

The medium '/home/denis/VirtualBox VMs/Windows/win1.vmdk' can't be used as the requested device type.
How to fix?

  
Added after 13 minutes
Got it. Added myself to the disk group. And connected it to Windows. But for some reason he saw it, but did not connect it.
What to do?

  
Added after 1 hour 12 minutes
I solved the problem like this:
Added the hard drive to the VirtualBox shared folders. And I configured this disk like a share via vboxserv.

\#########