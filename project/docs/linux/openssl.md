# openssl

## Commands

Create key and certificate ([link](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-on-centos-7))

```bash
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /etc/ssl/private/jenkins.key -out /etc/ssl/certs/jenkins.crt
```

Create PKCS12 file

```bash
openssl pkcs12 -export -out keyStore.p12 -inkey myKey.pem -in cert.pem
```

Check expirity date

```bash
## remote
openssl s_client -servername "google.com" -connect "google.com:443" 2>/dev/null | openssl x509 -noout -dates

## file
openssl x509 -enddate -noout -in /etc/pki/nginx/google.com.crt
```
