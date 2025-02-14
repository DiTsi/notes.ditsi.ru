# Replication

## **Replication**

### **master**

**create replication user "replicate"**

```SQL
CREATE ROLE replicate WITH REPLICATION LOGIN;
\password replicate
```

set parameters correctly

```INI
listen_addresses = '*'
wal_level = replica
max_wal_senders = 3 # max number of walsender processes
wal_keep_segments = 64 # in logfile segments, 16MB each; 0 disables
synchronous_standby_names = 'appname'
```

maybe you want enable archive

```INI
archive_mode = on
archive_command = 'rsync -a %p postgres@slave:/home/postgresql_wal/%f' 
   # placeholders: %p = path of file to archive
   #               %f = file name only
```

enable slave access to master. Edit pg_hba.conf

```INI
hostssl     replication     replicate       xxx.xxx.xxx.xxx/yy      scram-sha-256
```

### **slave**

 **stop postgresql**

**edit postgresql.conf and pg_hba.conf and report the changes you made on the master (like this, your slave will have the same configuration and could act as a master)**

**postgresql.conf**

```INI
hot_standby = on
```

go to your PGDATA directory and delete all the files

copy all the data from the master with the pg_basebackup command

```shell
su postgres
pg_basebackup -h 172.17.0.2 -D /var/lib/postgresql/10/main/ -P -U replicate --wal-method=stream
```

create a file recovery.conf in your PGDATA (/var/lib/postgresql/9.6/main/recovery.conf) directory

```INI
standby_mode          = 'on'
primary_conninfo      = 'host=172.17.0.2 port=5432 user=replicate password=MySuperPassword application_name=appname'
trigger_file = '/tmp/MasterNow'
restore_command = 'cp /var/lib/postgresql/9.6/main/archive/%f %p'

# standby_mode=on : specifies that the server must start as a standby server
# primary_conninfo : the parameters to use to connect to the master
# trigger_file : if this file exists, the server will stop the replication and act as a master
# restore_command : this command is only needed if you have used the archive_command on the master
```

```shell
chmod 600 recovery.conf
```

### check sync on master

```SQL
select * from pg_stat_activity  where usename = 'replicate' ;
```

### check replication done 0

```SQL
select pg_is_in_recovery();
```

### check replication done 1

#### on master

```SQL
SELECT pg_current_xlog_location();
```

#### on slave

```SQL
SELECT pg_last_xlog_receive_location();
```

see [solution #3](https://postgrespro.com/list/thread-id/1163227)

### check replication done 2

If your database has frequent writes, then the below query is a close approximation to get the slave lag

```SQL
select now() - pg_last_xact_replay_timestamp() AS replication_delay;
```

Below is a more accurate query for calculating replication lag for databases with very few writes. If the master doesnt sent down any write to the slave, then pg_last_xact_replay_timestamp() can be constant and hence may not accurately determine the slave lag using the above query.

```SQL
SELECT CASE WHEN pg_last_xlog_receive_location() =
pg_last_xlog_replay_location() THEN 0 ELSE EXTRACT (EPOCH FROM now() -
pg_last_xact_replay_timestamp()) END AS log_delay;
```