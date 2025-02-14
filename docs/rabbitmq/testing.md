# Testing

docker-compose.yml:

```YAML
version: "2.1"
services:

  rabbitmq1:
    container_name: rabbitmq1
    image: rabbitmq:3.8-management
    ports:
      - "16672:15672"
      - "6672:5672"
    environment:
      RABBITMQ_DEFAULT_USER: rabbitmq
      RABBITMQ_DEFAULT_PASS: rabbitmq
      RABBITMQ_ERLANG_COOKIE: lJzQwkzj790Pct2IUMOFsyvWTy75kh
      RABBITMQ_NODENAME: rabbit@rabbitmq1
    volumes:
      - "rabbitmq-var-1:/var/lib/rabbitmq"
    networks:
      - rabbitmq

  rabbitmq2:
    container_name: rabbitmq2
    image: rabbitmq:3.8-management
    ports:
      - "16673:15672"
      - "6673:5672"
    environment:
      RABBITMQ_DEFAULT_USER: rabbitmq
      RABBITMQ_DEFAULT_PASS: rabbitmq
      RABBITMQ_ERLANG_COOKIE: lJzQwkzj790Pct2IUMOFsyvWTy75kh
      RABBITMQ_NODENAME: rabbit@rabbitmq2
    volumes:
      - "rabbitmq-var-1:/var/lib/rabbitmq"
    networks:
      - rabbitmq

networks:
  rabbitmq:
```

haproxy.cfg:

```
global
    maxconn     20000
    log         127.0.0.1 local0
    user        haproxy
    chroot      /usr/share/haproxy
    pidfile     /run/haproxy.pid
    daemon

frontend  main
    bind :5672
    mode                 tcp
    log                  global
    option               httplog
    option               dontlognull
    option               http_proxy
    option forwardfor    except 127.0.0.0/8
    maxconn              8000
    timeout              client  30s

    acl url_static       path_beg       -i /static /images /javascript /stylesheets
    acl url_static       path_end       -i .jpg .gif .png .css .js

    #use_backend static          if url_static
    default_backend             rab

backend static
    mode        http
    balance     roundrobin
    timeout     connect 5s
    timeout     server  5s
    server      static 127.0.0.1:4331 check

backend rab
    mode        tcp
    balance     leastconn
    timeout     connect 5s
    timeout     server  30s
    timeout     queue   30s
    server  app1 127.0.0.1:8988 check
    server  app2 127.0.0.1:8989 check

```

python.py:

```Python
#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost', 5672, 'bim', credentials))
channel = connection.channel()

channel.queue_declare(queue='test', durable=True)

channel.basic_publish(exchange='',
                      routing_key='test',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
```