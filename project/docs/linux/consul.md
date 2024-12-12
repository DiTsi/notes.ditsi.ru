# consul

## Commands

```bash
consul agent -dev -bind 10.10.10.1  
consul members -detailed
# deregister service:
curl --header "X-Consul-Token: xxxxxxx-xxx" --request PUT http://consul.domain.ru:8600/v1/agent/service/deregister/beats-exporter-server-9479.consul
```

## Links

[howto](https://www.8host.com/blog/osnovy-raboty-s-sistemoj-obnaruzheniya-servisov-consul/)
