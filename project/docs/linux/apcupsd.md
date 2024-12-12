# apcupsd

## Commands

```bash
# get status
apcaccess status
```

## Configs

### APC SmartUPS 750 example

```ini
UPSNAME smartups750
UPSCABLE usb
UPSTYPE usb
LOCKFILE /var/lock
SCRIPTDIR /etc/apcupsd
PWRFAILDIR /etc/apcupsd
NOLOGINDIR /etc
ONBATTERYDELAY 6
BATTERYLEVEL 20
MINUTES 10
TIMEOUT 0
ANNOY 300
ANNOYDELAY 60
NOLOGON disable
KILLDELAY 0
NETSERVER on
NISIP 127.0.0.1
NISPORT 3551
EVENTSFILE /var/log/apcupsd.events
EVENTSFILEMAX 10
UPSCLASS standalone
UPSMODE disable
STATTIME 0
STATFILE /var/log/apcupsd.status
LOGSTATS off
DATATIME 0
```