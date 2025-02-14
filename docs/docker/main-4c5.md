# Main

## healthcheck

```YAML
version: "3"

services:
  metabase:
    build:
      context: ./3
    ports:
      - 5050:3000
    healthcheck:
      test: "curl --fail http://localhost:3000/ || exit 1"
      interval: 15s
      timeout: 3s
      retries: 1
    restart: always
```