# rclone

```bash
# stop sync job
kill -s STOP $(ps aux | grep "rclone sync" | awk 'NR==1{print $2}')

# continue sync job
kill -s CONT $(ps aux | grep "rclone sync" | awk 'NR==1{print $2}')
```
