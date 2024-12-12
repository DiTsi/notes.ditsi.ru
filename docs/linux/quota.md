# quota

[link](https://serverfault.com/questions/37737/quotas-in-vsftpd)

Preparing Mount Points

Will will now install and enable quotas

This shows how to do this per user and per group. By the way, quota support is enabled as the file systems are mounted so you’ll need to reboot your server when you complete the following steps. Please don’t do the on a remote machine unless you know exactly what you’re doing.

Perform the following as root or use sudo:

```bash
nano /etc/fstab
```

You need to have the following in your fstab file (usrquota or grpquota). Here are some examples depending on how you installed your ubuntu server:

```
/dev/hda1 /home ext2 defaults,usrquota 1 1
```

or

```bash
# /home was on /dev/sda3 during installation
UUID=fce47086-925c-4164-80a4-4ba6b307123b /home ext4 defaults,usrquota 0 2
```

or

```bash
# /home was on /dev/sda3 during installation
UUID=fce47086-925c-4164-80a4-4ba6b307123b /home ext4 defaults,usrquota,grpquota 0 2
```

You can remount by rebooting or using the following example:

```bash
mount -o remount,usrquota /home
```

Check your mounts:

```bash
mount | grep quota
```

Load the quota kernel module:

```bash
modprobe quota_v2 echo 'quota_v2' >> /etc/modules
```

Setting up you Quotas

Install the quota package.

```bash
apt-get install quota quotatool
```

Create the following files if they do not already exist. These files store your quota limits:

```bash
touch /home/aquota.user
touch /home/aquota.group
chmod 600 /home/aquota.user /home/aquota.group
```

turn on quatacheck without rebooting:

```bash
quotacheck -vagum
```

If your kernel supports journaled quota but you are not using it you’ll probably get an error. Use this command in that case:

```bash
quotacheck -fvagum
```

Set limits for user:

```bash
quotatool -u someusername -bq 100M -l 200M /mount_point
```

The first value is a soft limit, the second is a hard limit. Note that if a user attempts to load a 100Mb text file and they are already over their softlimit by 20Mb, their text file will be truncated by 20Mb to keep them under the 200Mb hard limit.

Check quotas:

```bash
repquota /home
```

If ever you wish to remove a quota for a user simply set their hard and soft limits to '0'.

I know it's a lot but that should do it! I ran through the process from scratch before publishing this just to be sure.

<p class="callout info">Do not remember:</p>

```bash
quotaon /dev/sda1
```

Show quota settings

```bash
repquota -s /mount_point
```
