# iptables

info: [https://eax.me/iptables/](https://eax.me/iptables/)

## Make persistent

### **save and restore**

save current rules

```bash
iptables-save > /etc/iptables/rules.v4
```

add /etc/network/if-pre-up.d/iptables

```bash
#!/bin/bash
/sbin/iptables-restore < /etc/iptables/rules.v4
```

### **netfilter-persistent**

install netfilter-persistent and iptables-persistent

run `netfilter-persistent save` to save current iptables

## Keys

```
-I insert
-A append

-p - protocol (tcp, udp, icmp.. or number [see file /etc/protocols])
-d, --destination address[/mask][,...]
-s, --source address[/mask][,...]
-j, --jump target
--line-numbers
```

## Commands

```bash
# Show all rules:
iptables -S

# Remove all rules:
iptables -F

# Show all rules by chains:
iptables -L --line-numbers

# Remove rule by number:
iptables -D INPUT 1

# Change default action
iptables -P INPUT DROP

# Remove rule by action:
iptables -D INPUT -s 123.45.67.89 -j DROP

# Append rule to position:
iptables -I INPUT 3 ...

# Save rules:
iptables-save > /etc/iptables/rules.v4

# Restore rules:
iptables-restore < /etc/iptables/rules.v4
```

## Logs

[https://tecadmin.net/enable-logging-in-iptables-on-linux/](https://tecadmin.net/enable-logging-in-iptables-on-linux/)

## Examples

```bash
iptables -A INPUT -p tcp -m tcp --dport 21 -j ACCEPT
iptables -A INPUT -s 123.45.67.89 -j DROP
iptables -A INPUT -s example.ru -j DROP
iptables -A INPUT -p tcp --sport 80 -j ACCEPT
```