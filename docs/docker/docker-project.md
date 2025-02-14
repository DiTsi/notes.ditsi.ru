# docker project

## Create new instance with docker

1. Create new user for docker project ([useradd](https://wiki.ditsi.ru/#useradd))
2. Add user to **docker** group ([usermod](https://wiki.ditsi.ru/#usermod))
3. <sup>**replace it!**</sup>Modify docker-compose.yml with new absolute path
4. Add <sup>**replace it!**</sup>host backup mechanism
5. If project uses **letsencrypt** add certbot renew in host crontab

## Useful bash scripts

```
# Check volume content
docker run -t --rm -v mysql-data:/data busybox ls /data
```

## Crontab

```
0 3 * * * username docker run -it --rm debian:9 sh -c "long command to run" 
```

## Services

### letsencrypt

[link](https://miki725.github.io/docker/crypto/2017/01/29/docker+nginx+letsencrypt.html)

```shell
# get new certificate
docker run -it --rm -v /home/nginx/letsencrypt:/etc/letsencrypt -v /home/nginx/letsencrypt-data:/data/letsencrypt deliverous/certbot certonly --webroot --webroot-path=/data/letsencrypt -d site1.com -d site2.com

# renew command
docker run -t --rm -v /home/redmine/letsencrypt:/etc/letsencrypt -v /home/redmine/letsencrypt-data:/data/letsencrypt certbot/certbot renew --webroot --webroot-path=/data/letsencrypt
```

### mysql

```shell
# Backup
docker exec CONTAINER /usr/bin/mysqldump -u root --password=root DATABASE > backup.sql

# Restore
cat backup.sql | docker exec -i CONTAINER /usr/bin/mysql -u root --password=root DATABASE
```

### nginx

nginx configuration (default.conf file):

```Nginx
server {
    listen 80;
    #server_name blog.zeroxzed.ru;
    #access_log /var/log/nginx/blog.zeroxzed.ru-access.log;
    #error_log /var/log/nginx/blog.zeroxzed.ru-error.log;

location / {
    proxy_pass http://172.23.0.3:3000;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Real-IP $remote_addr;
    }
}
```

run nginx with existing overlay network:

```shell
docker run -it --rm -v ./default.conf:/etc/nginx/conf.d/default.conf --name nginx_test -p 80:80 --network existing_docker_network nginx:latest
```

### jungledisk

Dockerfile

```
FROM debian:9

RUN apt-get update -y
RUN apt-get install -y psmisc wget libfuse2
RUN wget https://downloads.jungledisk.com/jungledisk/junglediskserver_330-3_amd64.deb
RUN dpkg -i junglediskserver_330-3_amd64.deb
COPY junglediskserver-license.xml /etc/jungledisk/junglediskserver-license.xml

RUN ln -sf /proc/self/fd/1 /var/log/junglediskserver.log

CMD /usr/local/bin/junglediskserver -f -d
```

junglediskserver-license.xml

```XML
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
<LicenseConfig>
<licenseKey>PUT_LICENSE_KEY_HERE</licenseKey>
<proxyServer>
<enabled>0</enabled>
<proxyServer></proxyServer>
<userName></userName>
<password></password>
<!--
The following values can be used to change
the type of proxy to be connected to.  

0 = HTTP/1.1 (most common proxy type) 
1 = HTTP/1.0 
2 = SOCKS4 
3 = SOCKS4A 
4 = SOCKS5
5 = SOCKS5 (send hostnames instead of IPs)
--> 
<proxyType>0</proxyType> 
</proxyServer>
</LicenseConfig>
</configuration>
```