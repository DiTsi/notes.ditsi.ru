# etcd

## Commands

```bash
etcdctl --endpoints=192.168.5.1:2380,192.168.5.2:2380,192.168.5.3:2380 --write-out=table endpoint status
```

## Information

Variable docs: [https://etcd.io/docs/v3.4.0/op-guide/configuration/](https://etcd.io/docs/v3.4.0/op-guide/configuration/)

Space quota info: [https://etcd.io/docs/v3.2.17/op-guide/maintenance/](https://etcd.io/docs/v3.2.17/op-guide/maintenance/)

## Errors

#### No space

<p class="callout warning">2020-12-09 23:13:30.509732 W | etcdserver: failed to apply request "header:&lt;ID:17070461351733445769 &gt; lease_grant:&lt;ttl:20-second id:6ce67627fe1b4488&gt;" with response "" took (2.78µs) to execute, err is etcdserver: no space</p>

<p class="callout success">Steps to fix:</p>

1\. Find leader of cluster. Use command

```bash
ETCDCTL_API=3 etcdctl --write-out=table endpoint status
```

2\. Execute commands

```bash
rev=$(ETCDCTL_API=3 etcdctl --endpoints=:2379 endpoint status --write-out="json" | egrep -o '"revision":[0-9]*' | egrep -o '[0-9]*')
ETCDCTL_API=3 etcdctl compact $rev
ETCDCTL_API=3 etcdctl defrag
ETCDCTL_API=3 etcdctl alarm disarm
```

from [here](https://etcd.io/docs/v3.2.17/op-guide/maintenance/)