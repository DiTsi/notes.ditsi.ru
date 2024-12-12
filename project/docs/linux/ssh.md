# ssh

```bash
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no user@host
```

## Port Forwarding

```bash
# There is a remote server 192.168.139.7 on which ssh listens on port 36152.
# It is necessary to forward port 55555 on the local machine to the machine
# having address 10.14.3.1, accessible from host 192.168.139.7, on port 8291
ssh -p 36152 -L 55555:10.14.3.1:8291 root@192.168.139.7
```

Port 9091 on `machine` will forward to local port 9090
```bash
ssh -R 9091:localhost:9090 machine
```

Details here: [https://habr.com/post/331348/](https://habr.com/post/331348/)

## Socks proxy
```bash
ssh -D 1337 -C server
```

## Automation

```bash
# create file pas with user password
echo password > pas

# execute command
sshpass -f pas ssh user@tarantool "sudo rm /opt/tarantool/logs/*.gz -f"
```

## Config example

```
Host *
    User dmitry

Host hh_resumes_searcher
    HostName 10.43.24.43
    User username4

Host phplist
    HostName 104.248.241.242
    User username2

Host zoran
    HostName kuku.rambler.ru
    User username1

Host metabase
    HostName 10.110.16.70

Host x5.ru
  IdentityFile ~/.ssh/work/id_rsa.x5

Host x5
  User dmitry.tsybus-3
  Hostname 192.168.139.237
  IdentityFile /home/ditsi/.ssh/work/id_rsa.x5
  IdentitiesOnly yes

Host v1*
  User deployer
  ProxyJump x5
  IdentitiesOnly yes

Host jh-test
  User ubuntu
  ProxyJump x5
  IdentityFile /home/ditsi/.ssh/work/deployer_id_rsa
  IdentitiesOnly yes
  Hostname 100.64.166.192
```

## Connect to Ubuntu 14.04

add to Host in `~/.ssh/config`
```bash
  PubkeyAcceptedKeyTypes=+ssh-rsa
```

## Errors

```bash
# error:
Access denied for user by PAM account configuration [preauth]
# solution:
add line '+:username:ALL' to /etc/security/access.conf
```
