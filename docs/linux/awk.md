# awk

## Commands

```bash
# sum third column and print
awk '{sum += $3} END{print sum;}'
```