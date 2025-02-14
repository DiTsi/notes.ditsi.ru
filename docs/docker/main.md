# Main

## DNS

Для включения DNS нужно добавить код в `/etc/docker/daemon.json`

```json
{
  "dns": ["XX.XX.1.1"],
  "dns-search": ["companydomain"]
}
```

## Healthcheck

**health-cmd**: this defines what command to run in order to check the health status. Health check commands should return 0 if healthy and 1 if unhealthy. Note that the command you use to validate health must be present in the image. In this example, we are using curl to check the built-in Elasticsearch health endpoint.

**health-interval**: this controls the initial delay before the first health check runs and then how often the health check command is executed thereafter. The default is 30 seconds.

**health-retries**: the health check will retry up to this many times before marking the container as unhealthy. The default is 3 retries.

**health-timeout**: if the health check command takes longer than this to complete, it will be considered a failure. The default timeout is 30 seconds.

## Volumes

### Script for copying data to volume

```shell
#!/bin/bash
# Script creates volume and copy data to it

DATA=$1
VOLUME_NAME=$2

docker create -v $VOLUME_NAME:/data --name move_data_to_volume busybox
cd $DATA
docker cp . move_data_to_volume:/data
cd -
docker rm move_data_to_volume
```

## Move all Docker images

```shell
# save
docker save $(docker images -q) -o /path/to/save/mydockersimages.tar
docker images | sed '1d' | awk '{print $1 " " $2 " " $3}' > mydockersimages.list

# move file to another host

# load
docker load -i /path/to/save/mydockersimages.tar
while read REPOSITORY TAG IMAGE_ID
do
  echo "== Tagging $REPOSITORY $TAG $IMAGE_ID =="
  docker tag "$IMAGE_ID" "$REPOSITORY:$TAG"
done < mydockersimages.list
```
