# kubernetes / k8s (Google Cloud)

## Requirements

Docker image must be in Google Container Registry

## Process

Create configuration file

```YAML
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: hh-resumes-searcher
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hhresumessearcher
  template:
    metadata:
      labels:
        app: hhresumessearcher
    spec:
      containers:
      - name: hh-resumes-searcher-container
        image: gcr.io/hh-resumes-searcher/hh-resumes-searcher:latest
        ports:
        - containerPort: 5000
          name: http
        env:
        - name: EMAIL
          value: email@ditsi.ru
        - name: PASSWORD
          value: Mypassword
```

## Commands

```shell
gcloud config get-value project
gcloud config set project hh-resumes-searcher

gcloud container clusters create hh-resumes-searcher
kubectl run my-app --image=gcr.io/hh-resumes-searcher/hh-resumes-searcher:latest --port=5000 --expose=true --env="EMAIL=email@email.com" --env="PASSWORD=pass" --env="LANG=en_US.UTF-8" --env="PYTHONIOENCODING=utf-8"

#show external ip addresses of nodes
kubectl get nodes --output wide

# port forwarding
kubectl port-forward aqua-csp-766689745b-4ln7q 8080:8080

# attach to pod
kubectl exec -it pod-name -- /bin/sh

# show logs
kubectl logs -f gitea-pod

# get kubernetes deployments
kubectl get deployments

# 
kubectl describe deployment

# show ports information

# port-forwarding
kubectl port-forward $PODNAME 5000:5000

# expose ports
kubectl expose deployments hh-resumes-searcher --port=80 --target-port=5000 --type=LoadBalancer --name=hh-service

# Information about service
describe services hh-resumes-searcher

# Delete Service 
kubectl delete svc hh-resumes-searcher
```

### gcloud commands

```shell
# show all available images in google compute engine
gcloud compute images list
```

## Errors

```shell
# Error
Unable to connect to the server: x509: certificate signed by unknown authority
# Solution
```

## Links

[https://medium.com/google-cloud/kubernetes-110-your-first-deployment-bf123c1d3f8](https://medium.com/google-cloud/kubernetes-110-your-first-deployment-bf123c1d3f8)