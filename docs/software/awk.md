# awk

## Commands

```bash
# sum third column and print
awk '{sum += $3} END{print sum;}'

# print 5 column if 4 column is equal to 0
awk '$4 == 0 {print $5}'

# Show first 5 rows and all rows with regex match
watch -d -n 10 "nats stream list | awk 'NR<=5 {print; next} /netwo/'"
```
