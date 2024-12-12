# barman

## **Backup (streaming configuration)**

### **Warning**

Don't forget to backup these files:
```bash
/etc/postgresql/10/main/postgresql.conf
/etc/postgresql/10/main/pg_hba.conf
/etc/postgresql/10/main/pg_ident.conf
```

- **barman** - barman server
- **pg** - postgres server to backup

### **pg side**

**/etc/hosts:**

```bash
<barman_ip> barman
```

generate key for postgres user

```bash
su postgres
ssh-keygen -t rsa
```

add barman public key to ~/.ssh/authorized\_keys  
install barman-cli and create barman role

```bash
apt install barman-cli
createuser -s -P barman
```

/etc/postgresql/9.6/main/postgresql.conf:

```bash
wal_level = replica
max_wal_senders = 10
max_replication_slots = 2
synchronous_standby_names = 'barman_receive_wal'
synchronous_commit = local
```

/etc/postgresql/9.6/main/pg\_hba.conf:

```bash
host replication barman <barman's ip>/32 md5
host all barman <barman's ip>/32 md5
```

restart postgresql

```bash
systemctl restart postgresql
```

### **barman side**

install barman and postgresql-client

```bash
apt install -y barman postgresql-client
```

/etc/hosts:

```bash
<pg's ip> pg
```

generate key for barman user:

```bash
su barman
ssh-keygen -t rsa
```

add pg public key to ~/.ssh/authorized\_keys

setup barman

```bash
su barman
echo pg:5432:postgres:barman:<password> > ~/.pgpass
chmod 0600 ~/.pgpass
```

create /etc/barman.d/pg.conf with:

```ini
[test]
description = "Example of PostgreSQL Database (Streaming-Only)"
conninfo = "host=test user=barman dbname=postgres password=<password>"
streaming_conninfo = "host=test user=barman password=<password>"
backup_method = postgres
# backup_method = rsync
# ssh_command = ssh postgres@test
streaming_archiver = on
slot_name = barman
```

check the connection

```bash
psql -c 'SELECT version()' -U barman -h pg postgres
```

### **CHECK IT!**

```bash
barman receive-wal --create-slot test # create barman slot on "pg"
barman switch-xlog --force --archive test

barman switch-wal pg
barman rebuild-xlogdb pg
barman backup test
```

## **Backup (archiver configuration)**

### **Warning**

Don't forget to backup these files:
```bash
/etc/postgresql/10/main/postgresql.conf
/etc/postgresql/10/main/pg_hba.conf
/etc/postgresql/10/main/pg_ident.conf
```

- **barman** - barman server
- **pg** - postgres server to backup

### **pg side**

/etc/hosts:

```bash
<barman_ip> barman
```

generate key for postgres user:

```bash
su postgres
ssh-keygen -t rsa
```

add barman public key to ~/.ssh/authorized\_keys  
install barman-cli and create barman role

```bash
apt install barman-cli
createuser -s -P barman
```

/etc/postgresql/9.6/main/postgresql.conf:

```ini
wal_level = replica
max_wal_senders = 10
# max_replication_slots = 2
# synchronous_standby_names = 'barman_receive_wal'
# synchronous_commit = local
```

/etc/postgresql/9.6/main/pg\_hba.conf:

```ini
host replication barman <barman's ip>/32 md5
host all barman <barman's ip>/32 md5
```

restart postgresql

```bash
systemctl restart postgresql
```

### **barman side**

install barman and postgresql-client

```bash
apt install -y barman postgresql-client
```

/etc/hosts:

```bash
<pg's ip> pg
```

generate key for barman user:

```bash
su barman
ssh-keygen -t rsa
```

add pg public key to ~/.ssh/authorized\_keys

setup barman

```bash
su barman
echo pg:5432:postgres:barman:<password> > ~/.pgpass
chmod 0600 ~/.pgpass
```

create /etc/barman.d/pg.cont with:

```ini
[test]
description = "Example of archiver"
conninfo = "host=test user=barman dbname=postgres password=<password>"
ssh_command = ssh postgres@pg
archiver = on
```

check the connection

```bash
psql -c 'SELECT version()' -U barman -h pg postgres
```

### <span style="color: #ff0000;">**Check It!**</span>

```bash
barman switch-wal pg
barman rebuild-xlogdb pg
barman receive-wal --create-slot test # create barman slot on "pg"
barman switch-xlog --force --archive test
barman backup test
```

## **Restore**

> when recover PITR use corresponding backup ID (see barman list-backup pg to specify)

### **postgres side**

**mv old main folder**

```bash
cd /var/lib/postgresql/10
mv main main_old
```

### **barman side**

**restore database**

```bash
barman recover --remote-ssh-command="ssh postgres@pg" pg2 latest /var/lib/postgresql/10/main
```

**<span style="color: #ff0000;">OR</span> restore with timestamp (postgres server timestamp)**

```bash
barman recover --target-time="2019-09-25 12:40:00" --remote-ssh-command="ssh postgres@pg" pg2 latest /var/lib/postgresql/10/main
```

**After restore to latest don't forget to recreate repliaction slot (see barman logs):**

```bash
barman receive-wal --create-slot pg
```

If you recover to **not latest** timestamp you will see the error requested starting point 0/16000000 is ahead of the WAL flush position of this server 0/15000968 and your database will be in readonly state. To avoid this make database writable by

```SQL
select pg_wal_replay_resume();
```

SQL command on the postgres side. And on the barman side rename server in /etc/barman.d/pg.conf to pg2 (for example) and rename file **/etc/barman.d/pg.conf** to **/etc/barman.d/pg2.conf**

## **Commands**

```bash
barman backup test # create backup
barman list-backup test # list backups
barman delete test 20190918T143933 # delete backup
barman delete test latest # delete latest backup
barman check test # check test server
barman status test
barman show-backup test <backup_id>
barman replication-status pg
```