# fping

*tool to check host is alive*

## Commands
check subnetwork hosts 
```bash
fping -g 192.168.1.0/24
```

just 1 retry (-r1) and only show alive hosts (-a) 
```bash
fping -a -g -r1 10.99.1.0/24
```
