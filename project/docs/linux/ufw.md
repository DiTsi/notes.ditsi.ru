# ufw

## Commands

​Change default settings:

```
ufw default deny incoming
```

Deny access from `15.15.15.51`:
```
ufw deny from 15.15.15.51
```

Other commands:
```bash
ufw deny in on eth0 from 15.15.15.51
ufw allow 22
```