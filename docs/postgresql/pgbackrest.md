# pgbackrest

<p class="callout info">postgresql backup and restore utility</p>

restore cluster

```shell
# check /var/lib/postgresql/10/main is empty
# stop cluster
pg_ctlcluster 10 main stop
# restore cluster
su -c 'pgbackrest --stanza=prod restore' postgres
# start cluster 
pg_ctlcluster 10 main start
```