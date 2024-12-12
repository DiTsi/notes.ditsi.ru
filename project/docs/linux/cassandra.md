# cassandra

## Commands
```bash
# connect
cqlsh <IP> 9042 -u username -p password

# keyspaces
describe keyspaces
SELECT * FROM system_schema.keyspaces;

# select keyspace
use keyspacename;

# print tables of current keyspace
desc tables;

# create snapshot
nodetool -h localhost -p 7199 snapshot owner

# check cluster status
nodetool status

# 'Space used' by a table
nodetool cfstats -- <keyspace>.<table>
```

## Backup & restore

Main commands
```bash
# export schema (here: https://stackoverflow.com/questions/49008626/cassandra-backup-including-schema)
cqlsh 10.0.0.1 -u username -e "DESC keyspace testkeyspace" > testkeyspace.cql

# backup
nodetool -h localhost -p 7199 snapshot mykeyspace

# import schema (in cqlsh)
source 'testkeyspace.cql';

# restore
MAX_HEAP_SIZE=12G sstableloader -d  100.126.5.241 -u cassandra -pw cassandra mykeyspace/tablename
```

### Backup

In order to create a backup, you need to create a snapshot and export the data schema:
```bash
# snapshot
nodetool -h 10.0.0.1 -p 7199 snapshot keyspace
 
# export schema
cqlsh 10.0.0.1 -u username -e "DESC keyspace keyspace" > keyspace.cql
```

 While creating a snapshot, you need to pay attention to what its number was created and copy only this snapshot from the corresponding tables. There will be as many directories as there are tables in keyspace.


After copying data schemas and snapshots to one of the servers in the new cluster, they need to be restored.

### Restore

For snapshots restoration, the directory hierarchy on the server of the new cluster must be as follows:
```bash
./keyspace/table_name_1/файлы_snapshot'а_для_table_name_1
./keyspace/table_name_2/файлы_snapshot'а_для_table_name_2
```

> **Attention**
The restoration from “100%” snapshot may take quite a long time, you need to wait. Need to run via nohup or screen

```bash
# data schema recovery #!была ошибка в русском слове воостановление
cqlsh <IP> 9042 -u <username> -p <password> # run cqlsh
source 'owner.cql'; # data schema recovery

# data schema recovery from snapshots
MAX_HEAP_SIZE=12G sstableloader -d <IP> -u <username> -pw <password> ./keyspace/table_name_1 # the directory with the snapshot must be specified
# and so on for each table
```