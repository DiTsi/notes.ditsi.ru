# rsyslog

## **Forwarding syslog**

**Add line to /etc/rsyslog.conf**

```
# udp
*.* @127.0.0.1:2002

# or tcp
*.* @@127.0.0.1:2002
```

### **Generate test event**

```bash
logger -p auth.notice "Some message for the auth.log file"
logger -p kern.error "Test event"
```

### **Using custom format**

**RFC3339 format**

```
$template CustomFormat,"%TIMESTAMP:::date-rfc3339% %HOSTNAME% %syslogtag%%msg%0\n"
$ActionFileDefaultTemplate CustomFormat
```

**other custom format**

```
$template CustomFormat,"%timestamp:::date-year%-%timestamp:::date-month%-%timestamp:::date-day% %timestamp:::date-hour%:%timestamp:::date-minute%:%timestamp:::date-second% %HOSTNAME% %syslogtag%%msg%0\n"
$ActionFileDefaultTemplate CustomFormat
```

### **Change timezone for rsyslog**

 **run `systemctl edit --full rsyslog`**

**add Environment="TZ=Etc/UTC" to Service section**

```
systemctl restart rsyslog
```