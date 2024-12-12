# journalctl

## **Configuration**

/etc/systemd/journald.conf

```INI
[Journal]
#Storage=auto
#Compress=yes
#Seal=yes
#SplitMode=uid
#SyncIntervalSec=5m
#RateLimitIntervalSec=30s
#RateLimitBurst=1000
#SystemMaxUse=
#SystemKeepFree=
#SystemMaxFileSize=
#SystemMaxFiles=100
#RuntimeMaxUse=
#RuntimeKeepFree=
#RuntimeMaxFileSize=
#RuntimeMaxFiles=100
#MaxRetentionSec=
#MaxFileSec=1month
#ForwardToSyslog=yes ## Forward to rsyslog
#ForwardToKMsg=no
#ForwardToConsole=no
#ForwardToWall=yes
#TTYPath=/dev/console
#MaxLevelStore=debug
#MaxLevelSyslog=debug
#MaxLevelKMsg=notice
#MaxLevelConsole=info
#MaxLevelWall=emerg
#LineMax=48K
```

## Limits

```bash
# current disk usage
journalctl --disk-usage
```

## **Commands**

```bash
# show boot log
journalctl -p 4

# time interval
journalctl --since today -u alertmanager
journalctl --since="2016-12-20 13:17:16"
journalctl --since="2016-12-19" --until="2016-12-20"

# colored output
journalctl -f --output cat -u liberajmanoj
```
