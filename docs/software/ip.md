# ip

## Commands

```bash
# Create a new bridge and change its state to up:
ip link add name bridge_name type bridge
ip link set bridge_name up

# To add an interface (e.g. eth0) into the bridge, its state must be up:
ip link set eth0 up

# Adding the interface into the bridge is done by setting its master to bridge_name:
ip link set eth0 master bridge_name

# To show the existing bridges and associated interfaces, use the bridge utility (also part of iproute2). See bridge(8) for details.
bridge link

# This is how to remove an interface from a bridge:
ip link set eth0 nomaster

# The interface will still be up, so you may also want to bring it down:
ip link set eth0 down

# To delete a bridge issue the following command:
ip link delete bridge_name type bridge

# show current status of interface
ip link show dev eth0

# show interaface address
ip addr

# delete device ip address
ip addr del 192.168.0.1/24 dev ppp0
```