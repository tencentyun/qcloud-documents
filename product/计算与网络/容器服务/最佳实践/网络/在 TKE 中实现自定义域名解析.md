## 背景

在使用 TKE 或 EKS (弹性容器集群) 时，有时可能会有解析自定义的内部域名的需求，比如：

1. 在集群外自建了集中存储服务，需要将集群中的监控或日志数据采集并统一通过固定内部域名发送到存储服务。
2. 传统业务在做容器化改造的过程中，部分服务的代码写死了用固定域名调用内部其它服务，并且不可配，无法使用 K8S 的 Service 名称进行调用。

本文将介绍一些在集群中使用自定义域名解析的方法。

## 方案一: 使用 CoreDNS Hosts 插件配置任意域名解析

修改 coredns 的 configmap:

``` bash
kubectl edit configmap coredns -n kube-system
```

加入 hosts 配置:

```
hosts {
    192.168.1.6     harbor.oa.com
    192.168.1.8     es.oa.com
    fallthrough
}
```

> 将 `harbor.oa.com` 指向 192.168.1.6；`es.oa.com` 指向 192.168.1.8。

完整配置示例:

``` yaml
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

## 方案二: 使用 CoreDNS Rewrite 插件指向域名到集群内服务

如果需要使用自定义域名的服务部署在集群中，可以使用 coredns 的 rewirte 插件，将指定域名解析到某个 Service 的 ClusterIP。

修改  coredns 的 configmap:

``` bash
kubectl edit configmap coredns -n kube-system
```

加入 rewrite 配置:

```
rewrite name es.oa.com es.logging.svc.cluster.local
```

> 将 `es.oa.com` 指向部署在 `logging` 命名空间下的 `es` 服务，如有多个可添加多行。

完整配置示例:

``` yaml
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

## 方案三: 使用 CoreDNS Forward 插件将自建 DNS 设为上游 DNS

默认情况下，forward 的配置是这样的:

``` yaml
forward . /etc/resolv.conf
```

意思是非集群内域名解析走 coredns 所在节点上 `/etc/resolv.conf` 中配置的 nameserver，我们将其显式替换成自建的 DNS 服务器地址:

```
forward . 10.10.10.10
```

完整配置示例:

``` yaml
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

然后将自定义域名的解析记录配置到自建 DNS 中即可。建议将节点上 `/etc/resolv.conf` 中的 nameserver 添加到自建 DNS 的上游，因为有些服务依赖腾讯云内部 DNS 解析，如果不将其设为自建 DNS 的上游，可能导致部分服务无法正常工作。这里以 [BIND 9](https://www.bind9.net/) 为例，修改配置文件，将上游 DNS 地址放入 `forwarders` 中:

```
options {
        forwarders {
                183.60.83.19;
                183.60.82.98;
        };
        ...
```

## 小结

本文介绍了在 TKE 上实现自定义域名解析的三种方案。对于方案一和方案二，每次添加解析记录都需要修改 coredns 配置文件 (无需重启)，方案一的好处是简单直观，可以添加任意解析记录，方案二的好处是无需提前知道解析记录的 IP 地址，但要求解析记录指向的地址必须部署在集群中。方案三的好处是可以管理大量的解析记录，记录的管理都在自建 DNS 中，增删记录无需修改 coredns 配置。具体采用哪种方案，请根据自身需求来评估。

## 参考资料

* CoreDNS Hosts 插件文档: https://coredns.io/plugins/hosts/
* CoreDNS Rewrite 插件文档: https://coredns.io/plugins/rewrite/
* CoreDNS Forward 插件文档: https://coredns.io/plugins/forward/