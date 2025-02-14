# Firewall

## Structure

1. **connection type**: established, related, invalid, ...
2. **protocol**: udp, **port**: 53, ALLOW not from WAN
3. **protocol**: icmp, **interface**: WAN, ALLOW
4. **port**: winbox (8291), ALLOW from...
5. **jump**: internal input, internal forward, external input, external forward
6. **chains**: input, forward, DROP ALL (test rule, because all DROP rules should be in additional chains)
7. **chains**: internal input, internal forward, external input, external forward
