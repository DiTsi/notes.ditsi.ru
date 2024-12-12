# bind

## Commands

```bash
# check zone configuration
/usr/sbin/named-checkzone example.com /etc/bind/db.example.com
```

## Custom zone configuration file

```ini
$TTL            86400
;
; The example.com domain database
;
@               IN      SOA    server.example.com. example.com. (
                        2006012501      ; Serial Year,Month,Day,Version
                        21600           ; Refreash
                        1800            ; Retry
                        604800          ; Expire
                        86400           ; Minimum
                        )
; Define name servers
                IN      NS      server.example.com.
; Define mail servers
                IN      MX      10 server.example.com.
                IN      MX      20 server.example.com.
;
; Define localhost
;
localhost       IN      A       127.0.0.1
;
; Define the static hosts
;
 
linux.internal  IN      A       12.34.56.78
linux           IN      A       10.10.0.1
firewall        IN      A       10.0.0.254
tigerswitch     IN      A       10.0.0.2
laptop          IN      A       10.10.1.24
;
; Define the dynamic hosts
;
 
server          IN      A       10.123.4.8
;
; Define some aliases
;
ns1             IN      CNAME   server.example.com.
ns2             IN      CNAME   server.example.com.
```