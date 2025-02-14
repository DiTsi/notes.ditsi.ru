# lightdm

## autologin

Add lines to `/usr/share/lightdm/lightdm.conf.d/01_debian.conf`

```INI
[SeatDefaults]
autologin-user=username
autologin-user-timeout=0
```