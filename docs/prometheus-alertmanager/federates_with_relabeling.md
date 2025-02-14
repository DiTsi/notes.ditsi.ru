Конфиг для сбора метрик с прометеуса с переименованием label'ов, которые появились из-за федерации

```yml
- job_name: 'regional_federate'
  scheme: https
  params:
    'match[]':
      - '{job=~".+"}'
  relabel_configs:
  - source_labels: [job]
    target_label: federation_job
  - source_labels: [__address__]
    target_label: federation_instance
  metric_relabel_configs:
  - source_labels: [exported_job]
    target_label: job
  - source_labels: [exported_instance]
    target_label: instance
  - regex: "exported_job|exported_instance"
    action: labeldrop
  file_sd_configs:
  - files:
    - 'regional_federate.yml'
  scrape_timeout: 20s
```
