# ulimit

## Commands

```bash
# check user descriptors
su nginx -s /bin/bash
ulimit -n

# calculate opened descriptors by process
for i in $(ps axu | grep celery | grep worker | awk '{print $2}'); do n=$(ls -1 /proc/$i/fd/ | wc -l); echo $i $n; done
```
