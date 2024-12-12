# fluentd

*Project to get logs from syslog and send it to elasticsearch*

## server

Dockerfile
```docker
FROM fluent/fluentd:v0.12-debian
COPY fluent.conf /fluentd/etc/fluent.conf

RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri", "--version", "1.9.7"]
```

fluent.conf
```python
<source>
  @type syslog
  port 24224
  bind 0.0.0.0
  tag system.local
</source>

<match **>
  @type copy
  <store>
    @type elasticsearch
    host 127.0.0.1
    port 9200
    logstash_format true
    logstash_prefix fluentd
    logstash_dateformat %Y%m%d
    include_tag_key true
    type_name access_log
    tag_key @log_name
    flush_interval 1s
  </store>
  <store>
    @type stdout
  </store>
</match>
```

docker run command

```bash
docker run --rm -it --network="host" -p 24224:24224 fluentd-image:latest
```

## client

/etc/syslog.conf
```
#...
*.* @10.110.10.10:24224
```

## get logs from docker container

```YAML
version: '2'
services:
  web:
    image: httpd
    ports:
      - "80:80"
    links:
      - fluentd
    logging:
      driver: "fluentd"
      options:
        fluentd-address: localhost:24224
        tag: httpd.access

  fluentd:
    build: ./fluentd
    volumes:
      - ./fluentd/conf:/fluentd/etc
    links:
      - "elasticsearch"
    ports:
      - "24224:24224"
      - "24224:24224/udp"

  elasticsearch:
    image: elasticsearch:5.3.0
    expose:
      - 9200
    ports:
      - "9200:9200"

  kibana:
    image: kibana:5.3.0
    links:
      - "elasticsearch"
    ports:
      - "5601:5601"
```

fluentd Dockerfile

```docker
# fluentd/Dockerfile
FROM fluent/fluentd:v0.12-debian
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri", "--version", "1.9.7"]
```

fluent.conf file

```python
# fluentd/conf/fluent.conf
<source>
  @type forward
  port 24224
  bind 0.0.0.0
</source>
<match *.**>
  @type copy
  <store>
    @type elasticsearch
    host elasticsearch
    port 9200
    logstash_format true
    logstash_prefix fluentd
    logstash_dateformat %Y%m%d
    include_tag_key true
    type_name access_log
    tag_key @log_name
    flush_interval 1s
  </store>
  <store>
    @type stdout
  </store>
</match>
```

[link](https://docs.fluentd.org/v0.12/articles/docker-logging-efk-compose)
