# Useful images

```shell
# htop
docker run --rm -it --pid host frapsoft/htop

# pgadmin
docker run -d --rm -p 5050:80 --name pgadmin -e "PGADMIN_DEFAULT_EMAIL=<email>" -e "PGADMIN_DEFAULT_PASSWORD=<pass>" -d dpage/pgadmin4

# postgresql
docker run -d --rm -p5432:5432 --name psql -e POSTGRES_USER=qwerty -e POSTGRES_DB=qwerty_db -e POSTGRES_PASSWORD=qwerty postgres:10
psql -h localhost  -U qwerty -W qwerty_db

# Cadvisor - monitoring docker containers https://github.com/google/cadvisor
```