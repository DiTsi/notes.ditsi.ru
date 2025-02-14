# Commands

### Clusters

```shell
### creating new cluster "other" ###
pg_createcluster -p 5435 11 other

### start cluster "clusterName" ###
systemctl start postgresql@11-clusterName
```

### Roles

```SQL
CREATE ROLE xuser LOGIN ENCRYPTED PASSWORD 'XXX' INHERIT;
GRANT read_only TO xuser;

DROP ROLE test;
```

#### Problems

<p class="callout warning">cannot be dropped because some objects depend on it</p>

<p class="callout success">CREATE ROLE &lt;newuser&gt;;  
REASSIGN OWNED BY &lt;olduser&gt; TO &lt;newuser&gt;;  
DROP OWNED BY &lt;olduser&gt;;  
DROP ROLE &lt;olduser&gt;;</p>

### Database

```SQL
createdb myDatabaseName # Create Database
\l # List all Databases
DROP DATABASE test_db; # Drop database
psql test_db # run psql with test_db database
GRANT ALL ON DATABASE database_name TO username; # grant privileges
```

### Table

```SQL
\dt # Show all tables
# Create table
CREATE TABLE table1
(
  host_id bigserial NOT NULL, -- The primary key
  host_ip inet NOT NULL, -- The IP of the host
  host_name character varying(255) NOT NULL, -- The name of the host
  CONSTRAINT "host" PRIMARY KEY (host_id )
)
WITH (
  OIDS=FALSE
);

DROP TABLE if exists table; # Drop table
ALTER TABLE table OWNER TO owner_new; # Change table OWNER
```

### Data

```SQL
INSERT INTO table1 (host_id, host_ip, host_name) VALUES (1, '10.10.2.1', 'b'); # Insert data to table
SELECT * FROM test_table; # Show all data
```

### Schema

```SQL
SELECT schema_name FROM information_schema.schemata; # list all schemas
```