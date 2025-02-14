# Security

## **Brief**

[ **Linux kernel capabilities**](https://docs.docker.com/engine/security/security/#linux-kernel-capabilities)

**cgroups (resource limiting)**

**user namespace**

**–security-opt=no-new-privileges**

**AppArmor (включает в себя Linux kernel capabilities) <span style="color: #ff0000;">should be installed on host</span>**

## **Проверка безопасности хоста \[docker security host\]**

[ссылка на проект](https://github.com/docker/docker-bench-security)

[статья-расшифровка отчёта](https://www.digitalocean.com/community/tutorials/how-to-audit-docker-host-security-with-docker-bench-for-security-on-ubuntu-16-04)

```shell
# run tests
docker run -it --net host --pid host --userns host --cap-add audit_control \
    -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
    -v /etc:/etc:ro \
    -v /usr/bin/docker-containerd:/usr/bin/docker-containerd:ro \
    -v /usr/bin/docker-runc:/usr/bin/docker-runc:ro \
    -v /usr/lib/systemd:/usr/lib/systemd:ro \
    -v /var/lib:/var/lib:ro \
    -v /var/run/docker.sock:/var/run/docker.sock:ro \
    --label docker_bench_security \
    docker/docker-bench-security
```

## **Enable security features**

### **Run with another namespace**

edit /etc/docker/daemon.json

```
{
  "userns-remap": "default"
}
```

**add line to /etc/subuid and /etc/subgid**

```
dockremap:265536:65536
```

```
systemctl restart docker
```

**check you have no previous docker images**

### **Enable auditing**

> to suppress docker-bench-security message Ensure auditing is configured for the Docker daemon

install and enable audit

create `/etc/audit/rules.d/docker.rules` with

```
# First rule - delete all
-D

# Increase the buffers to survive stress events.
# Make this bigger for busy systems
-b 320

-w /usr/bin/docker -p wa
-w /var/lib/docker -p wa
-w /etc/docker -p wa
-w /lib/systemd/system/docker.service -p wa
-w /etc/systemd/system/docker.service -p wa
-w /lib/systemd/system/docker.socket -p wa
-w /usr/lib/systemd/system/docker.socket -p wa
-w /etc/default/docker -p wa
-w /etc/docker/daemon.json -p wa
-w /usr/bin/docker-containerd -p wa
-w /usr/bin/docker-runc -p wa
```

generate `/etc/audit/audit.rules` with `augenrules` command

restart audit

### **Disable network traffic between containers**

> to suppress docker-bench-security message
> 
> Ensure network traffic is restricted between containers on the default bridge

add to `/etc/docker/daemon.json`:

```
"icc": false
```

### **Enable logging**

**/etc/docker/daemon.json**

```
"log-driver": "syslog"
"log-opts": { "syslog-address": "udp://10.10.10.10:514" }
```