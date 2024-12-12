# strongswan
I set up a VPN for Android via the Strongswan client application, but it didn’t work, although many problems were fixed along the way. In Uzbekistan, obviously the packages just don’t reach me, so I gave it up.

## Install on Debian

```bash
apt install strongswan strongswan-pki strongswan-swanctl
```

## Configure

### Script to create certs

```bash
#!/bin/bash

SWANCTL_PATH=/etc/swanctl
KEY_TYPE=ed25519
TMP_PATH=/tmp
CA_LIFETIME=3652
CN="95.179.191.126"
PHONE_LIFETIME=1820
SERVER_LIFETIME=1820
CA_KEY_PATH=/etc/swanctl/private
CA_CERT_PATH=/etc/swanctl/x509ca
SERVER_CERT_PATH=/etc/swanctl/x509

# CA
pki --gen --type ${KEY_TYPE} --outform pem > ${TMP_PATH}/strongswanKey.pem
pki --self --ca --lifetime ${CA_LIFETIME} --in ${TMP_PATH}/strongswanKey.pem \
    --dn "C=CH, O=strongSwan, CN=strongSwan Root CA" \
    --outform pem > ${TMP_PATH}/strongswanCert.pem

# SERVER
pki --gen --type ${KEY_TYPE} --outform pem > ${TMP_PATH}/serverKey.pem
pki --req --type priv --in ${TMP_PATH}/serverKey.pem \
    --dn "C=CH, O=strongswan, CN=${CN}" \
    --san ${CN} --outform pem > ${TMP_PATH}/serverReq.pem
pki --issue --cacert ${TMP_PATH}/strongswanCert.pem --cakey ${TMP_PATH}/strongswanKey.pem \
    --type pkcs10 --in ${TMP_PATH}/serverReq.pem --serial 01 --lifetime ${SERVER_LIFETIME} \
    --outform pem > ${TMP_PATH}/serverCert.pem

# PHONE
pki --gen --type ${KEY_TYPE} --outform pem > ${TMP_PATH}/phoneKey.pem
pki --req --type priv --in ${TMP_PATH}/phoneKey.pem \
    --dn "C=CH, O=strongswan, CN=${CN}" \
    --san ${CN} --outform pem > ${TMP_PATH}/phoneReq.pem
pki --issue --cacert ${TMP_PATH}/strongswanCert.pem --cakey ${TMP_PATH}/strongswanKey.pem \
    --type pkcs10 --in ${TMP_PATH}/phoneReq.pem --serial 01 --lifetime ${PHONE_LIFETIME} \
    --outform pem > ${TMP_PATH}/phoneCert.pem
openssl pkcs12 -export -inkey ${TMP_PATH}/phoneKey.pem \
    -in ${TMP_PATH}/phoneCert.pem -name "phone" \
    -certfile ${TMP_PATH}/strongswanCert.pem -caname "strongSwan Root CA" \
    -out ${TMP_PATH}/phone.p12

# Move to folders
mv ${TMP_PATH}/strongswanKey.pem ${CA_KEY_PATH}/strongswanKey.pem
mv ${TMP_PATH}/strongswanCert.pem ${CA_CERT_PATH}/strongswanCert.pem
mv ${TMP_PATH}/serverCert.pem ${SERVER_CERT_PATH}/serverCert.pem
```

### /etc/swanctl/swanctl.conf 
```bash
root@strongswan:~# cat /etc/swanctl/swanctl.conf 
connections {
    rw {
        local {
            auth = pubkey
            certs = serverCert.pem
            id = 95.179.191.126
        }
        remote {
            auth = pubkey
        }
        children {
            net-net {
                local_ts  = 10.1.0.0/16
            }
        }
    }
}
```

### /etc/ipsec.conf
```bash
root@strongswan:~# cat /etc/ipsec.conf 
config setup
conn main
    leftsubnet=10.1.0.0/16
    leftcert=/etc/swanctl/x509/serverCert.pem
    leftsendcert=never
    rightsubnet=10.2.0.0/16
    rightcert=/tmp/phoneCert.pem
    auto=start
```

## Run
```bash
systemct start strongswan-starter.service
```

## Logs
```bash
tail -f /var/log/syslog
```

