# curl

## Examples

```bash
curl -I wiki.domain.com

curl -X POST "http://127.0.0.1:8888/api/auth/login" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "username=user&password=password"

curl -X POST "http://127.0.0.1:8888/api/transformations" -H "accept: application/json" -H  "Content-Type: application/json" -H  "Authorization: Bearer 377..dad" -d '{"devices":false,"hp":false,"hrd_mails":false}'

# Using certs
curl --cacert ... --cert ... --key ... "http://127.0.0.1:8080"
```