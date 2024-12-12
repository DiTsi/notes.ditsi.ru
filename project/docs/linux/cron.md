# cron

## Commands

#### crontab for all users

```bash
for user in $(cut -f1 -d: /etc/passwd); do crontab -u $user -l; done
```

## syntax

```bash
 ┌────────── minute (0 - 59)
 │ ┌──────── hour (0 - 23)
 │ │ ┌────── day of month (1 - 31)
 │ │ │ ┌──── month (1 - 12)
 │ │ │ │ ┌── day of week (0 - 6 => Sunday - Saturday, or
 │ │ │ │ │                1 - 7 => Monday - Sunday)
 ↓ ↓ ↓ ↓ ↓
 * * * * * command to be executed
```

day of week number:
```bash
0 - Sun - Sunday
1 - Mon - Monday
2 - Tue - Tuesday
3 - Wed - Wednesday
4 - Thu - Thursday
5 - Fri - Friday
6 - Sat - Saturday
7 - Sun - Sunday
```