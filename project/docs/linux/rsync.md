# rsync

```bash
rsync -avz --exclude .htaccess --exclude .htaccess_server ---exclude .git\
 --exclude .gitignore --exclude button.sh --exclude .htpasswd $SOURCE $DEST\
 --delete --info=progress2
```

```bash
# check what will be synced
rsync -n -avz --ignore-existing ~/src ~/dest
```