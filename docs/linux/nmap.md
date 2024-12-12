# nmap

[https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/](https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/)

```bash
# Scan a single Port
nmap -p 22 192.168.1.1
# Scan a range of ports
nmap -p 1-100 192.168.1.1
# Scan 100 most common ports (Fast)
nmap -F 192.168.1.1
# Scan all 65535 ports
nmap -p- 192.168.1.1


# Scan using TCP connect
nmap -sT 192.168.1.1
# Scan using TCP SYN scan (default)
nmap -sS 192.168.1.1
# Scan UDP ports
nmap -sU -p 123,161,162 192.168.1.1
# Scan selected ports - ignore discovery
nmap -Pn -F 192.168.1.1
```