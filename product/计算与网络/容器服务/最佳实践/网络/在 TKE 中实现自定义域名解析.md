## 操作场景

在使用容器服务 TKE 或弹性容器集群 EKS 时，可能会有解析自定义内部域名的需求，例如：

- 在集群外自建了集中存储服务，需要将集群中的监控或日志数据采集通过固定内部域名发送到存储服务。
- 传统业务在进行容器化改造过程中，部分服务的代码配置了用固定域名调用内部其他服务，且无法修改配置，即无法使用 Kubernetes 的 Service 名称进行调用。



## 方案选择
本文将介绍以下3种在集群中使用自定义域名解析的方案示例：

| 方案 | 优势 | 
|---------|---------|
| [方案1：使用 CoreDNS Hosts 插件配置任意域名解析](#scheme1) | 简单直观，可以添加任意解析记录。 | 
| [方案2：使用 CoreDNS Rewrite 插件指向域名到集群内服务](#scheme2) | 无需提前知道解析记录的 IP 地址，但要求解析记录指向的地址必须部署在集群中。 | 
| [方案3：使用 CoreDNS Forward 插件将自建 DNS 设为上游 DNS](#scheme3) | 可以管理大量的解析记录，记录的管理都在自建 DNS 中，增删记录无需修改 CoreDNS 配置。 | 

>? 方案1和方案2，每次添加解析记录都需要修改 CoreDNS 配置文件（无需重启）。请根据自身需求评估并选择具体方案。


## 方案示例



### 方案1：使用 CoreDNS Hosts 插件配置任意域名解析[](id:scheme1)

1. 执行以下命令，修改 CoreDNS 的 configmap。示例如下：
``` bash
kubectl edit configmap coredns -n kube-system
```
2. 修改 hosts 配置，将域名加入 hosts，示例如下：
```
hosts {
        192.168.1.6     harbor.oa.com
        192.168.1.8     es.oa.com
        fallthrough
}
```
>?将 `harbor.oa.com` 指向192.168.1.6；`es.oa.com` 指向192.168.1.8。

 **完整配置示例如下：**
```yaml
apiVersion: v1
data:
      Corefile: |2-
        .:53 {
            errors
            health
            kubernetes cluster.local. in-addr.arpa ip6.arpa {
                pods insecure
                upstream
                fallthrough in-addr.arpa ip6.arpa
            }
            hosts {
                192.168.1.6     harbor.oa.com
                192.168.1.8     es.oa.com
                fallthrough
            }
            prometheus :9153
            forward . /etc/resolv.conf
            cache 30
            reload
            loadbalance
        }
kind: ConfigMap
metadata:
      labels:
        addonmanager.kubernetes.io/mode: EnsureExists
      name: coredns
      namespace: kube-system
```



### 方案2：使用 CoreDNS Rewrite 插件指向域名到集群内服务[](id:scheme2)



如果需要使用自定义域名的服务部署在集群中，可以使用 CoreDNS 的 Rewrite 插件，将指定域名解析到某个 Service 的 ClusterIP。

1. 执行以下命令，修改 CoreDNS 的 configmap。示例如下：
```bash
kubectl edit configmap coredns -n kube-system
```
2. 执行以下命令，加入 Rewrite 配置。示例如下：
```bash
rewrite name es.oa.com es.logging.svc.cluster.local
```
>?将 `es.oa.com` 指向部署在 `logging` 命名空间下的 `es` 服务，如有多个域名可添加多行。

 **完整配置示例如下：**
```yaml
apiVersion: v1
data:
      Corefile: |2-
        .:53 {
            errors
            health
            kubernetes cluster.local. in-addr.arpa ip6.arpa {
                pods insecure
                upstream
                fallthrough in-addr.arpa ip6.arpa
            }
            rewrite name es.oa.com es.logging.svc.cluster.local
            prometheus :9153
            forward . /etc/resolv.conf
            cache 30
            reload
            loadbalance
        }
kind: ConfigMap
metadata:
      labels:
        addonmanager.kubernetes.io/mode: EnsureExists
      name: coredns
      namespace: kube-system
```



### 方案3：使用 CoreDNS Forward 插件将自建 DNS 设为上游 DNS[](id:scheme3)

1. 查看 forward 配置。forward 默认配置如下所示，指非集群内域名通过 CoreDNS 所在节点 `/etc/resolv.conf` 文件中配置的 nameserver 解析。
```yaml
forward . /etc/resolv.conf
```
2. 配置 forward，将 `/etc/resolv.conf` 显式替换为自建的 DNS 服务器地址。示例如下：
```yaml
forward . 10.10.10.10
```
 **完整配置示例如下：**
```yaml
apiVersion: v1
data:
      Corefile: |2-
        .:53 {
            errors
            health
            kubernetes cluster.local. in-addr.arpa ip6.arpa {
                pods insecure
                upstream
                fallthrough in-addr.arpa ip6.arpa
            }
            prometheus :9153
            forward . 10.10.10.10
            cache 30
            reload
            loadbalance
        }
kind: ConfigMap
metadata:
      labels:
        addonmanager.kubernetes.io/mode: EnsureExists
      name: coredns
      namespace: kube-system
```
3. 将自定义域名的解析记录配置到自建 DNS。建议将节点上 `/etc/resolv.conf` 中的 nameserver 添加到自建 DNS 的上游，因为部分服务依赖腾讯云内部 DNS 解析，如果未将其设为自建 DNS 的上游，可能导致部分服务无法正常工作。本文以 [BIND 9](https://www.isc.org/bind/) 为例修改配置文件，将上游 DNS 地址写入 forwarders 中。示例如下：
>! 自建 DNS Server 和请求源不在同个 Region，可能会导致部分不支持跨域访问的腾讯域名失效。
>
```yaml
options {
        forwarders {
                183.60.83.19;
                183.60.82.98;
        };
        ...
```



## 参考文档

- [CoreDNS Hosts 插件文档](https://coredns.io/plugins/hosts/)
- [CoreDNS Rewrite 插件文档](https://coredns.io/plugins/rewrite/)
- [CoreDNS Forward 插件文档](https://coredns.io/plugins/forward/)
