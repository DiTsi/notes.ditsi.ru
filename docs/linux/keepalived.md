# keepalived

## Theory

- Load balancing - IPVS
- High availability - VRRP

## Configuration

Master

```JSON
global_defs {
   notification_email {
      email1@rambler.ru
      email2@rambler.ru
   }
   notification_email_from email3@rambler.ru
   smtp_server 10.10.10.1
   smtp_connect_timeout 30
}

vrrp_instance INST1 {
    state MASTER
    interface bond0
    virtual_router_id 51
    priority 100
    advert_int 1
    virtual_ipaddress {
        172.16.3.44
    }
}
```

Slave

```JSON
! Configuration File for keepalived

global_defs {
   notification_email {
      email1@rambler.ru
      email2@rambler.ru
   }
   notification_email_from email3@rambler.ru
   smtp_server 10.10.10.2
   smtp_connect_timeout 30
}

vrrp_instance INST2 {
    state BACKUP
    interface bond1
    virtual_router_id 51
    priority 99
    advert_int 1
    virtual_ipaddress {
        172.16.3.44
    }
}
```

[link](https://www.redhat.com/sysadmin/keepalived-basics)
