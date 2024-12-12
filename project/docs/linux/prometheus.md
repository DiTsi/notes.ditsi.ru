# prometheus

## warnings
- duplicate sample for timestamp
  see metrics `prometheus_target_scrapes_sample_duplicate_timestamp_total`

## federation

Check with curl:
```bash
curl -s http://localhost:9090/prometheus/federate?match[]=%7B__name__%3D~%22.%2B%22%7D
```
