# vsftpd

## Generate Key

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout /etc/ssl/private/vsftpd.pem -out /etc/ssl/private/vsftpd.pem
```

## Config

```ini
listen=YES
listen_port=21
#listen_ipv6=NO
allow_writeable_chroot=YES
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=NO
use_localtime=YES
connect_from_port_20=NO
chroot_local_user=YES

# USER WHITE LIST
userlist_enable=YES
userlist_deny=NO
userlist_file=/etc/vsftpd.user_list

secure_chroot_dir=/var/run/vsftpd/empty
pam_service_name=ftp
#rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
#rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
rsa_cert_file=/etc/ssl/private/vsftpd.pem
rsa_private_key_file=/etc/ssl/private/vsftpd.pem

# LOG
xferlog_enable=YES
#xferlog_file=/var/log/vsftpd.log

# SSL
ssl_enable=YES
ssl_tlsv1=YES

pasv_enable=YES
pasv_min_port=11111
pasv_max_port=22222
```

## Limit FTP access only to the /var/www

### Method 1

```
chroot_local_user=YES
```

```
usermod --home /var/www/ username
```

### Method 2 (Using `user_sub_token`)

```ini
chroot_local_user=YES
local_root=/ftphome/$USER
user_sub_token=$USER
```

See `man vsftpd.conf`