# systemd

## Commands

```bash
# clear failed service from systemctl list
systemctl reset-failed <service_name>
```

## Config

Get config
```bash
systemd-analyze cat-config systemd/journald.conf
```

## Units

xbacklight\_permissions.service

```ini
[Unit]
After=systemd-logind.service

[Service]
ExecStart=/usr/bin/chmod o+w /sys/class/backlight/intel_backlight/brightness

[Install]
WantedBy=default.target
```

hdparm.service

```ini
[Unit]
Description=Local system resume actions
After=systemd-logind.service suspend.target hybrid-sleep.target hibernate.target

[Service]
Type=simple
ExecStart=/usr/bin/hdparm -B 255 /dev/sda

[Install]
WantedBy=sleep.target
```

cpufreq\_permissions.service

```ini
[Unit]
After=systemd-logind.service suspend.target hybrid-sleep.target hibernate.target

[Service]
ExecStart=/usr/bin/chown ditsi:users /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor /sys/devices/system/cpu/cpu3/cpufreq/scaling_governor

[Install]
WantedBy=sleep.target
```

apm.service

```ini
[Unit]
Description=Local system resume actions
After=suspend.target hybrid-sleep.target hibernate.target

[Service]
Type=simple
ExecStart=/usr/bin/hdparm -B 255 /dev/sda

[Install]
WantedBy=sleep.target
```

## Timers

```bash
# Show Timers
systemctl list-timers
```

### Example

/etc/systemd/system/docker-prune.service

```ini
[Unit]
Description=Run docker image prune -af
Wants=docker-prune.timer

[Service]
Type=oneshot
User=ditsi
ExecStart="/usr/bin/docker image prune -af"
```

/etc/systemd/system/docker-prune.timer

```ini
[Unit]
Description=Run docker image prune -af

[Timer]
OnCalendar=Sun 15:00
Persistent=true
```

To check that the units are written correctly, use:

```bash
systemd-analyze verify /etc/systemd/system/downloads-clear.timer
systemd-analyze verify /etc/systemd/system/downloads-clear.service
```

don't forget to enable and start timer: 'systemctl enable some.timer && systemctl start some.timer'

check the timers with the command `systemctl list-timers`

### One timer, two services

`/etc/systemd/system/downloads-clear.timer`
```ini
[Unit]
Description=Clear Downloads directories

[Timer]
OnCalendar=*-*-* 00:00:00
Unit=downloads-clear.target

[Install]
WantedBy=timers.target[root@nb work]# 
```

`/etc/systemd/system/downloads-clear.target`
```ini
[Unit]
Description= My target unit, that groups my two services xxx.service and yyy.service
BindsTo=downloads-clear-ditsi.service downloads-clear-work.service
After=downloads-clear-ditsi.service downloads-clear-work.service

[Install]
Also=downloads-clear.timer
WantedBy=timers.target
```

`/etc/systemd/system/downloads-clear-ditsi.service`
```ini
[Unit]
Description=Clear ditsi Downloads dorectory
Wants=downloads-clear.timer

[Service]
Type=oneshot
User=ditsi
ExecStart=/usr/bin/find /home/ditsi/Downloads -type f -mtime +30 -exec rm '{}' \;

[Install]
Also=downloads-clear.timer
```

`/etc/systemd/system/downloads-clear-work.service`
```ini
[Unit]
Description=Clear work Downloads dorectory

[Service]
Type=oneshot
User=work
ExecStart=/usr/bin/find /home/work/Downloads -type f -mtime +90 -exec rm '{}' \;

[Install]
Also=downloads-clear.timer
```

## Units

```bash
# Edit units
systemctl edit --full rsyslog
```

## Examples

```bash
# If you want unit A to reboot when unit B reboots
# + when loading the system was launched only after unit B, then you need to add
After = docker.target
PartOf = docker.target
# to the [Unit] section
```

tags: systemctl
