# Secrets

To encode data into base64 use this command

```bash
echo -n "someDataShouldBeEncode" | base64
```


## dockerconfigjson
Создаём 1.json с таким содержимым

```json
{
  "auths": {
    "test.ditsi.ru": {
      "username": "test",
      "password": "test",
      "email": "test@ditsi.ru"
    }
  }
}
```

`oc create secret generic docker-dev.ditsi.ru --from-file=.dockerconfigjson=$HOME/1.json --type=kubernetes.io/dockerconfigjson`
