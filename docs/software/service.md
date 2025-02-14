# service

Ubuntu 14.04 uses service instead systemd

## Autostart

See `/etc/rc2.d/README`

```bash
cd /etc/rc2.d
ln -s ../init.d/prometheus-node-exporter ./S20-prometheus-node-exproter
```

Disable autostart

```bash
cd /etc/rc2.d
mv ./S20-prometheus-node-exproter ./K20-prometheus-node-exproter
```
