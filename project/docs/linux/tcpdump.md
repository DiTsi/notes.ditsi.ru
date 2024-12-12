# tcpdump

```bash
# listen on port:
tcpdump -i eth0 port 8080

# show all traffic:
tcpdump -A -i eth0 port 8080

# UDP
tcpdump -nn -i lo host localhost and udp

```