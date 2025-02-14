# Two ISP With Load Balancing

```shell
# may/30/2019 15:17:55 by RouterOS 6.44
# software id = 6UZS-TEHT
#
# model = 2011iL
# serial number = 
/interface bridge
add name=LAN
/interface ethernet
set [ find default-name=ether1 ] name=ISP1
set [ find default-name=ether2 ] name=ISP2
/interface list
add name=WAN
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=dhcp_pool0 ranges=192.168.56.2-192.168.56.254
/ip dhcp-server
add address-pool=dhcp_pool0 disabled=no interface=LAN name=dhcp1
/interface bridge port
add bridge=LAN interface=ether6
add bridge=LAN interface=ether7
add bridge=LAN interface=ether8
add bridge=LAN interface=ether9
add bridge=LAN interface=ether10
/interface list member
add interface=ISP1 list=WAN
add interface=ISP2 list=WAN
/ip address
add address=10.10.5.1/24 interface=ether5 network=10.10.5.0
add address=192.168.56.1/24 interface=LAN network=192.168.56.0
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=ISP1
add dhcp-options=hostname,clientid disabled=no interface=ISP2
/ip dhcp-server network
add address=192.168.56.0/24 gateway=192.168.56.1
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,9.9.9.9
/ip firewall mangle
add action=accept chain=prerouting dst-address=192.168.4.0/24 in-interface=LAN
add action=mark-connection chain=prerouting connection-mark=no-mark in-interface=ISP1 new-connection-mark=ISP1_conn
add action=mark-connection chain=prerouting connection-mark=no-mark in-interface=ISP2 new-connection-mark=ISP2_conn
add action=mark-connection chain=prerouting connection-mark=no-mark dst-address-type=!local in-interface=LAN new-connection-mark=ISP1_conn \
    per-connection-classifier=src-address:2/0
add action=mark-connection chain=prerouting connection-mark=no-mark dst-address-type=!local in-interface=LAN new-connection-mark=ISP2_conn \
    per-connection-classifier=src-address:2/1
add action=mark-routing chain=prerouting connection-mark=ISP1_conn in-interface=LAN new-routing-mark=to_ISP1
add action=mark-routing chain=prerouting connection-mark=ISP2_conn in-interface=LAN new-routing-mark=to_ISP2
add action=mark-routing chain=output connection-mark=ISP1_conn new-routing-mark=to_ISP1
add action=mark-routing chain=output connection-mark=ISP2_conn new-routing-mark=to_ISP2
/ip firewall nat
add action=masquerade chain=srcnat out-interface=ISP1
add action=masquerade chain=srcnat out-interface=ISP2
/ip route
add check-gateway=ping distance=1 gateway=192.168.4.1 routing-mark=to_ISP1
add check-gateway=ping distance=1 gateway=192.168.134.1 routing-mark=to_ISP2
add check-gateway=ping distance=1 gateway=192.168.4.1
add check-gateway=ping distance=2 gateway=192.168.134.1
/ip route rule
add routing-mark=isp1_route table=main
add routing-mark=isp2_route table=main
/system clock
set time-zone-name=Europe/Amsterdam
```