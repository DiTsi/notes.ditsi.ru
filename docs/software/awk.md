# awk

## Commands

```bash
# sum third column and print
awk '{sum += $3} END{print sum;}'
# Show first 5 rows and all rows with regex match
watch -d -n 10 "nats stream list | awk 'NR<=5 {print; next} /netwo/'"
```
