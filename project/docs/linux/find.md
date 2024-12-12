# find

## Commands

Find directories and change their permissions:
```bash
find ./ -type d -exec chmod -x '{}' \;
```

## Examples:

```bash
# Remove ...?
find $HOME \( -name a.out -o -name '*.o' \) \-atime +7 -exec rm {} \;

# Remove files older than 15 days
find ./ -mtime +15 -exec rm '{}' \;
```