# loki

## Query

```bash
rate({filename=~"/var/log/nginx/access.log"}[10m] |= "\"http_status\": \"200\"") / rate({filename=~"/var/log/nginx/access.log"}[10m])

# json, regex
{filename="/var/log/service/service.log"} | json | level="warn" ts=~"2024-11-26T10:31:46.*"
```
