


>? DNS Forward 配置的入口将不再开放。此前关于 DNS Forward 配置的参数会同步更新在 CoreDNS 的 Corefile 中，若需要修改集群的 DNS 服务，请参考以下操作，或可参考原生 Kubernetes CoreDNS 的使用方式。

## 操作场景
本文主要介绍如何通过修改 CoreDNS 配置文件，更改集群的 DNS 服务。

## 操作前提
已经 [创建弹性集群](https://cloud.tencent.com/document/product/457/39813)，创建时需要在高级配置中选择**部署CoreDNS支持集群内服务发现**，以支持集群内服务发现。

## 操作指引

### 默认 Corefile 配置说明

在弹性集群中，部署 CoreDNS 会默认挂载一个 Configmap 作为 CoreDNS 的配置文件，即 Corefile。
CoreDNS 安装时默认的 Corefile 配置如下：

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health :8081
        kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
           ttl 30
        }
        prometheus :9153
        forward . 183.60.83.19 183.60.82.98
        cache 30
        loop
        reload
        loadbalance
    }    
```

其中各个配置项均采用原生 Kubernetes 的配置，详情见 [CoreDNS](https://kubernetes.io/zh/docs/tasks/administer-cluster/dns-custom-nameservers/#coredns)。需注意：

- `forward`：183.60.83.19，183.60.82.98 为腾讯云默认 DNS 地址。


### 自定义配置 Corefile
您可以通过修改 CoreDNS Corefile 的 ConfigMap，以更改服务发现的相关配置。其用法与原生 kubernates 使用方式保持一致，详情见 [自定义 DNS 服务](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/)。
