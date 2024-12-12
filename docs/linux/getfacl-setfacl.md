# getfacl, setfacl

```bash
# recursively remove user from folder 
setfacl -R -x u:username  ./folder

# get current permissions
getfacl ./folder

setfacl -R -m d:u:apetrov:rwx,u:apetrov:rwX folder
```