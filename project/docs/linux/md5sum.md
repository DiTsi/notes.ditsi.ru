# md5sum

```bash
# Check CD/DVD iso image
blocks=$(expr $(du -b image.iso | awk '{print $1}') / 2048)
dd if=/dev/sr0 bs=2048 count=$blocks | md5sum
```