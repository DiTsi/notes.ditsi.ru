https://help.hcltechsw.com/connections/v6/admin/install/cp_prereq_kubernetes_dns.html

```bash
kubectl create -f https://k8s.io/examples/admin/dns/busybox.yaml

kubectl get pods busybox

kubectl exec -ti busybox -- nslookup docker-registry.cluster.local
```
