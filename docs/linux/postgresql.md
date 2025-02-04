# postgresql

## Commands

```sql
/* Show activities */
SELECT user, pid, client_addr, application_name, state, now() - state_change AS duration FROM pg_stat_activity;
```
