# nfs

/etc/fstab

```
10.10.10.10:/home/ditsi/share /home/ditsi/mount_nfs nfs4 defaults,noauto 0 0
```

/etc/exports

```
<export> <host1>(<options>) <hostN>(<options>)...
/exported/directory bob.example.com(sync, rw, no_subtree_check)
```

## The goal is to organize the movement of files from one machine to another

First, we register the ip and network mask in the “network settings” (system administration). On one of the machines we register ip 10.0.0.1 and mask 255.0.0.0, on the other – ip 10.0.0.2 and mask 255.0.0.0 Now it is important to designate which computer will be server i.e. where the shared folder will be located, and which one will be the client. On the machine that will be the server, install nfs packages

```bash
sudo apt-get install nfs-kernel-server nfs-common portmap
```

Then we create a folder, which will be the shared folder visible on the client machine. I created it in my home directory called files. Setting access rights

```bash
sudo chmod -R 777 /home/имя пользователя/files
```

then we write the path to it in the nfs configuration

```bash
sudo gedit /etc/exports
```

in the file we write (this is for the machine whose address is 10.0.0.2): /home/username/files 10.0.0.1(rw) save

run the following commands:

```bash
sudo exportfs -a
sudo /etc/init.d/portmap restart
sudo /etc/init.d/nfs-kernel-server restart
```

go to the client computer and mount the files folder to the desired location. I mounted it in media/share so that it would appear on the desktop. The main thing is to create it before mounting.

```bash
sudo mount 10.0.0.2:/home/имя пользователя/files /media/share
```

You can unmount it with the command:

```bash
sudo umount /media/share
```