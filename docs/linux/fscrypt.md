# fscrypt

## 0. Encrypt /home/\<user\>

### 0.1 Encrypt /home/\<user\> directory
```bash
xbps-install elogind fscrypt
ln -s /etc/sv/elogind /var/service/
ln -s /etc/sv/dbus /var/service/
sv up dbus
sv up elogind
tune2fs -O encrypt <root_dev>
fscrypt setup

useradd -s /bin/bash -g users -m <user>
passwd <user>
cd /home/<user>
rm .* # remove hidden files in /home/<user> for next step

fscrypt encrypt /home/<user> --user=<user>
```

### 0.2 Enable fscript in PAM
Edit `/etc/pam.d/system-login`
- append line 
  ```
  auth       optional   pam_fscrypt.so
  ```
  in the end of `auth` section

- insert line
  ```
  session    optional   pam_fscrypt.so
  ```
  before
  ```
  session    include    system-auth
  ```

For more info see [https://wiki.archlinux.org/title/Fscrypt](link)

