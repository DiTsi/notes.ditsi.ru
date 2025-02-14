# apt

## Commands

```bash
# disable upgrade for package
apt-mark hold <package_name>
# search specific version of package
apt-cache madison <package_name>
# install specific version
apt install gitlab-ce=12.2.0-ce.0
```

## Proxy config
```bash
# cat /etc/apt/apt.conf.d/proxy.conf
Acquire::http::Proxy "http://tsibous2431:fbf043@51.89.94.97:10285";
Acquire::https::Proxy "http://tsibous2431:fbf043@51.89.94.97:10285";
Acquire::::Proxy "true";
```

## Preferences

/etc/apt/preferences.d/stable.pref
```bash
# 500 <= P < 990: causes a version to be installed unless there is a
# version available belonging to the target release or the installed
# version is more recent

Package: *
Pin: release a=stable
Pin-Priority: 400
```

/etc/apt/preferences.d/restic.pref
```bash
# 0 < P < 100: causes a version to be installed only if there is no
# installed version of the package

Package: restic
Pin: release a=testing
Pin-Priority: 900
```
