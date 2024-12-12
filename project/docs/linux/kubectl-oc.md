# kubectl / oc

## Commands

#### configmap

```bash
# create or replace configmap
oc create configmap grafana-ini --from-file=grafana-config-dev/grafana.ini --dry-run -o yaml | oc apply -f -
```

```bash
# MAIN
kubectl cluster-info
kubectl run nginx --image=nginx
kubectl get namespaces

# PODS
kubectl get pods
kubectl get pods -o wide
kubectl delete pod test-8bf6fc5db-b5hbf
kubectl exec -it <Pod_Name>  -- /bin/bash

kubectl get deployments
kubectl delete deployment test

# CONFIG
kubectl config view
kubectl config view --flatten
kubectl config set-context second-cluster
kubectl config use-context second-cluster

kubectl proxy
```

```bash
# pod output
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
kubectl proxy
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/

# pod logs
kubectl logs $POD_NAME
```

## Scenarios

### **Create user with token**

**create .yml file with content**

```YAML
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin
  namespace: default
secrets:
- name: admin-secret
---
apiVersion: v1
kind: Secret
metadata:
  name: admin-secret
  annotations:
    kubernetes.io/service-account.name: admin
type: kubernetes.io/service-account-token
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: admin-role
rules:
- apiGroups: [""]
  resources: ["pods", "nodes", "replicationcontrollers", "events", "limitranges", "services"]
  verbs: ["get", "delete", "list", "patch", "update"]
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: admin-role-binding
roleRef:
  kind: ClusterRole
  name: admin-role
  apiGroup: rbac.authorization.k8s.io
subjects:
- kind: ServiceAccount
  name: admin
  namespace: default
```

```bash
kubectl apply -f <filename.yml>
kubectl apply -k ./
```

get token with command

```bash
kubectl describe secret admin-secret
```

to delete token run

```bash
kubectl delete -f <filename.yml>
```

to use this token run

```bash
curl -H "Authorization: Bearer ${TOKEN}" https://<ip>:8443/api
```