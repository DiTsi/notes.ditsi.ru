# mysql

## Commands

```SQL
USE <database>
SHOW TABLES;
```

Delete all tables from database

```SQL
SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;')
FROM information_schema.tables
WHERE table_schema = 'MyDatabaseName';
```

Privileges

```SQL
-- Update Host privileges for user
update mysql.user set Host='%' WHERE Host='localhost' and User='username';
```

create MySQL database

```SQL
create database `seahub-db` character set = 'utf8';
create user 'seafile'@'localhost' identified by 'your secure password';
GRANT ALL PRIVILEGES ON `seahub-db`.* to `seafile`;
```

Backup/restore

```bash
# backup
mysqldump -p -u root some_database > some_database_dump.sql

# restore
mysql -p -u username database_name < file.sql
```

## Useful commands

databases size

```SQL
SELECT table_schema "DB Name",
        ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB" 
FROM information_schema.tables 
GROUP BY table_schema; 
```

change full database collation BASH script

```bash
DB="seahub-db"; ( echo 'ALTER DATABASE `'"$DB"'` CHARACTER SET utf8 COLLATE utf8_general_ci;'; mysql "$DB" -e "SHOW TABLES" --batch --skip-column-names | xargs -I{} echo 'ALTER TABLE `'{}'` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;' ) | mysql "$DB"
```