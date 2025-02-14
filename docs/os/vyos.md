# VyOS

## Installation

```bash
install image
```

## Configuration

### basic

```bash
configure
commit
save
exit
```

### configuration

```bash
# show current configuration
show configuration

# show current configuration commands
show configuration commands
```

### commits

```bash
# show commits
show system commit

# compare commits
compare 14 # compare current with commit 14

# rollback
rollback 14 # revert all newer commit to make actual commit # 14
```

## Interfaces

```bash
set interfaces ethernet eth0 address 155.138.160.89/23 
set protocols static route 0.0.0.0/0 next-hop 155.138.160.1
```

## DNS

```bash
set system name-server 8.8.8.8
set system name-server 8.8.4.4
```

## SSH

```bash
set service ssh port 22
set service ssh listen-address 155.138.160.89
set service ssh disable-host-validation
```

## OpenConnect

```bash
run generate pki ca install <CA name>
run generate pki certificate sign <CA name> install <Server name>

set vpn openconnect authentication local-users username <username> password <password>
set vpn openconnect authentication mode local password
set vpn openconnect network-settings client-ip-settings subnet <subnet>
set vpn openconnect network-settings name-server <address>
set vpn openconnect network-settings name-server <address>
set vpn openconnect ssl ca-certificate <pki-ca-name>
set vpn openconnect ssl certificate <pki-cert-name>
set vpn openconnect ssl passphrase <pki-password>
```
