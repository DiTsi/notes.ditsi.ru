# network-manager

*Network Manager - default Ubuntu network manager*

## Commands

```bash
# Show Wi-Fi status:
nmcli radio

# Show Wi-Fi networks
nmcli device wifi list

# Rescan Wi-Fi:
nmcli device wifi rescan

# Show interfaces status:
nmcli d

# Connect to Wi-Fi:
nmcli device wifi connect onlime_90 password ahjcz177

# Disconnect from Wi-Fi:
nmcli con down id "onlime_90 1"

# Show all connections:
nmcli c show

# Connect to VPN connection vpn_connection with password prompt
nmcli --ask c up vpn_connection
```
