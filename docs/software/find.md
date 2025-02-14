# find

## Commands

```bash
# Find directories and change their permissions:
find ./ -type d -exec chmod -x '{}' \;

# number of files in the folder
find . -xdev -type f | cut -d "/" -f 2 | sort | uniq -c | sort -n
```

## Examples:

```bash
# Remove ...?
find $HOME \( -name a.out -o -name '*.o' \) \-atime +7 -exec rm {} \;

# Remove files older than 15 days
find ./ -mtime +15 -exec rm '{}' \;
```