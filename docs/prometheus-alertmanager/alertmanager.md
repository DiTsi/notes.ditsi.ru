# Alertmanager

Смотреть логи можно через

```
journalctl -u alertmanager --since today
```
  
Чтобы найти события по которым были отправлены уведомления, нужно фильтровать логи по "firing_alerts"

## alertmanager.yml

### Example of flexible alert structure

```YAML
- match:
    project: myteam
  receiver: myteam_errors
  repeat_interval: 12h
  routes:
    - match:
        severity: call
      repeat_interval: 24h
      receiver: Krasnodar_2020
    - match:
        resp: all
      repeat_interval: 24h
      receiver: myteam_errors
      routes:
        - match:
            resp: devops
          receiver: myteam_devops
    - match:
        severity: high
      repeat_interval: 3h
      routes:
        - match:
            resp: devops
          receiver: myteam_devops
        - match:
            resp: ditsi
          receiver: ditsi
    - match:
        severity: low
      repeat_interval: 12h
      routes:
        - match:
            resp: devops
          receiver: myteam_devops
        - match:
            resp: ditsi
          receiver: ditsi         
```
