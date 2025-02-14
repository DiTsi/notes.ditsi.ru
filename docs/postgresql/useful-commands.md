# Useful Commands

#### Show database size:

```SQL
SELECT pg_size_pretty( pg_database_size('dbname') );
```

#### Drop all tables:

```SQL
DO $$ DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP;
END $$;
```

#### Change role password

```SQL
ALTER ROLE rolename WITH PASSWORD 'passwd';
```

#### Select all types

```
\dT
```

#### Save result to file

```shell
echo "COPY (SELECT * from foo) TO STDOUT with CSV HEADER" | psql -o '/tmp/test.csv' database_name
```

#### Number of clients

```SQL
select client_addr, count(client_addr) from pg_stat_activity where datname = 'database' group by client_addr;
```

#### Change type of column (char varying length)

```SQL
/* show current length */
SELECT column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_name = 'connection' ORDER BY column_name;

/* update to the new value */
ALTER TABLE connection ALTER COLUMN "user" TYPE character varying(20);
```

#### Sort tables by size

```SQL
select table_name, pg_relation_size(quote_ident(table_name)) from information_schema.tables where table_schema = 'public' order by 2 desc;
```