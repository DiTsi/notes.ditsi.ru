# ceph

## Commands

```bash
# Main
ceph status
ceph health detail

# OSD
ceph osd tree
ceph osd pool ls detail
ceph osd df
ceph osd crush reweight osd.0 0.8
# check replication factor
ceph osd pool ls detail

# PG
ceph pg stat

# add host?
ceph orch host add ceph-03 192.168.1.4
```
