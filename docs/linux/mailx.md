# mailx

## Commands

```bash
# Send message
echo "letter" | mailx -s "theme" -A ditsi nix9@gmail.com
```

## Account

~/.mailrc

```
account ditsi {
set smtp-use-starttls
set smtp=smtp://smtp.gmail.com:587
set smtp-auth=login
set smtp-auth-user=tsibous14
set smtp-auth-password=23dui23uibdh
set from="DiTsi <tsibous14@gmail.com>"
}
```