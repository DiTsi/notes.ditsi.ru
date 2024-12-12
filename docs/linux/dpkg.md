# dpkg

## Commands

```bash
# installing the package
dpkg -i package.deb # will not install the package if there are external dependencies that require installation from the repositories
apt-get install package.deb
```

## Preparing to build the package

Create a /deb directory and make the following structure in it

```bash
/deb/DEBIAN/control
/deb/DEBIAN/postinst # script executing after install
/deb/etc/apache2/sites-available/
/deb/etc/nginx/sites-available/
/dev/var/
/dev/var/www/html
```

файл /dev/DEBIAN/control:

```
Package: 
Version:
Section:
Architecture:
Pre-Depends: bash, sed
Depends: nginx (>= 1.9.15), apache (>= 2.4.18)
Priority: optional
...
```

## Building the package

```bash
fakeroot dpkg-deb --build /dev
```

## Local repository

In the /opt/rep directory

```bash
# a file with which something needs to be done
/opt/rep/conf/distributions

# command of repository initialization
reprepro export

# creating some symlinks
reprepro createsymlinks
```

/etc/apt/source.list

```
deb file:///opt/rep xenial soft
```