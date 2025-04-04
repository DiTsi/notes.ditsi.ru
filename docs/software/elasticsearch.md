# elasticsearch

## Commands

### nodes

```bash
# get nodes
curl -X GET "http://elastic:password@localhost:9200/_cat/nodes?h=name,ip,node.role,master" | sort
```

### indices

```bash
# show all indexes
curl "http://elastic:password@localhost:9200/_cat/indices?v"

# show health
curl -X GET "http://localhost:9200/_cluster/health?pretty"

# list indices by size
curl "http://elastic:password@localhost:9200/_cat/indices?pretty&s=store.size:desc"

# remove index
curl -X DELETE "http://elastic:password@localhost:9200/metrics-2024.06?pretty"
```

### shards
```bash
# show all shards 
curl -k http://elastic:password@localhost:9200/_cat/shards?pretty

curl -X POST "http://<elasticsearch_host>:9200/_cluster/reroute" -H 'Content-Type: application/json' -d '{
  "commands": [
    {
      "allocate_stale_primary": {
        "index": "<index_name>",
        "shard": 0,
        "node": "<node_name>",
        "accept_data_loss": false
      }
    }
  ]
}'

# show allocation for unassigned shards
curl "http://elastic:password@localhost:9200/_cluster/allocation/explain?pretty"
```

## links
[Heap Size](https://www.elastic.co/guide/en/elasticsearch/reference/master/heap-size.html)

[Shrinking an index](https://www.elastic.co/guide/en/elasticsearch/reference/6.8/indices-shrink-index.html)

[Show all indices](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/cat-indices.html)

[Reindex](https://www.elastic.co/guide/en/elasticsearch/reference/5.4/docs-reindex.html)
