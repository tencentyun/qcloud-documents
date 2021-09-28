## 问题描述
用户使用容器服务 TKE 时，会遇到因 CLB 回环问题导致服务访问不通或访问 Ingress 存在几秒延时的现象，本文档介绍该问题的相关现象、原因，并提供解决方法。


## 现象描述

CLB 回环问题可能导致存在以下现象：

- 无论是 iptables 或是 ipvs 模式，访问本集群内网 Ingress 会出现4秒延时或不通。
- ipvs 模式下，集群内访问本集群 LoadBanacer 类型的内网 Service 出现完全不通，或者联通不稳定。

## 问题原因

根本原因在于 CLB 将请求转发到后端 RS 时，报文的源目的 IP 都在同一节点内，而 Linux 默认忽略收到源 IP 是本机 IP 的报文，导致数据包在子机内部回环，如下图所示：
![](https://main.qcloudimg.com/raw/7cdff4fde69e4e95e75002ae47379d01.png)



### 分析 Ingress 回环

使用 TKE CLB 类型的 Ingress，会为每个 Ingress 资源创建一个 CLB 以及80、443的7层监听器规则（HTTP/HTTPS），并为 Ingress 每个 location 绑定对应 TKE 各个节点某个相同的 NodePort 作为 RS（每个 location 对应一个 Service，每个 Service 都通过各个节点的某个相同 NodePort 暴露流量），CLB 根据请求匹配 location 转发到相应的 RS（即 NodePort），流量经过 NodePort 后会再经过 Kubernetes 的 iptables 或 ipvs 转发给对应的后端 Pod。集群中的 Pod 访问本集群的内网 Ingress，CLB 将请求转发给其中一台节点的对应 NodePort：
![img](https://main.qcloudimg.com/raw/cf3003d32c45aeea25330400e4827ad7.png)

如上图，当被转发的这台节点恰好也是发请求的 Client 所在节点时：
1. 集群中的 Pod 访问 CLB，CLB 将请求转发到任意一台节点的对应 NodePort。
2. 报文到达 NodePort 时，目的 IP 是节点 IP，源 IP 是 Client Pod 的真实 IP， 因为 CLB 不进行 SNAT，会将真实源 IP 透传过去。
3. 由于源 IP 与目的 IP 都在这台机器内，因此将导致回环，CLB 将收不到来自 RS 的响应。

访问集群内 Ingress 的故障现象大多为几秒延时，原因是7层 CLB 如果请求 RS 后端超时（大概4s），会重试下一个 RS，所以如果 Client 设置的超时时间较长，出现回环问题的现象就是请求响应慢，有几秒的延时。如果集群只有一个节点，CLB 没有可以重试的 RS，则现象为访问不通。


### 分析 LoadBalancer Service 回环

当使用 LoadBalancer 类型的内网 Service 时暴露服务时，会创建内网 CLB 并创建对应的4层监听器（TCP/UDP）。当集群内 Pod 访问 LoadBalancer 类型 Service 的 `EXTERNAL-IP` 时（即 CLB IP），原生 Kubernetes 实际上不会去真正访问 LB，而是直接通过 iptables 或 ipvs 转发到后端 Pod （不经过 CLB），如下图所示：
![](https://main.qcloudimg.com/raw/c116a45c8cf269764e31d4317d31c366.png)

因此原生 Kubernetes 的逻辑不存在回环问题。但在 TKE 的 ipvs 模式下，Client 访问 CLB IP 的包会真正到 CLB，如果在 ipvs 模式下，Pod 访问本集群 LoadBalancer 类型 Service 的 CLB IP 将存在回环问题，情况跟上述内网 Ingress 回环类似，如下图所示：
![img](https://main.qcloudimg.com/raw/c5a2e4c087df8089c3f3f50397e107e2.png)


不同的是，四层 CLB 不会重试下一个 RS，当遇到回环时，现象通常是联通不稳定。如果集群只有一个节点，那将导致完全不通。

**为什么 TKE 的 ipvs 模式不用原生 Kubernetes 类似的转发逻辑（不经过 LB，直接转发到后端 Pod）？**

背景是因为以前 TKE 的 ipvs 模式集群使用 LoadBalancer 内网 Service 暴露服务，内网 CLB 对后端 NodePort 的健康探测会全部失败，原因如下：

- ipvs 主要工作在 INPUT 链，需要将要转发的 VIP（Service 的 Cluster IP 和 EXTERNAL-IP）当成本机 IP，才好让报文进入 INPUT 链交给 ipvs 处理。
- kube-proxy 的做法是将 Cluster IP 和 EXTERNAL-IP 都绑到名称为 `kube-ipvs0` 的 dummy 网卡，该网卡仅仅用来绑定 VIP (内核自动为其生成 local 路由)，不用于接收流量。
- 内网 CLB 对 NodePort 的探测报文源 IP 是 CLB 自身的 VIP，目的 IP 是 Node IP。当探测报文到达节点时，节点发现源 IP 为本机 IP （因为其被绑定到了 `kube-ipvs0`），就将其丢弃掉。所以 CLB 的探测报文永远无法收到响应，也就全部探测失败，虽然 CLB 有全死全活逻辑（全部探测失败视为全部可以被转发），但也相当于探测未起到任何作用，在某些情况下将造成一些异常。

为解决上述问题，TKE 的修复策略是：ipvs 模式不绑定 EXTERNAL-IP 到 `kube-ipvs0` 。也就是集群内 Pod 访问 CLB IP 的报文不会进入 INPUT 链，而是直接出节点网卡，真正到达 CLB，这样健康探测的报文进入节点时将不会被当成本机 IP 而丢弃，同时探测响应报文也不会进入 INPUT 链导致出不去。

虽然这种方法修复了 CLB 健康探测失败的问题，但也导致集群内 Pod 访问 CLB 的包真正到了 CLB，由于访问集群内的服务，报文又会被转发回其中一台节点，也就存在了回环的可能性。

>?相关问题已提交至 [社区](https://github.com/kubernetes/kubernetes/issues/79783)，但目前还未有效解决。



## 相关答疑
### 为什么公网 CLB 不存在回环问题？

使用公网 Ingress 和 LoadBalancer 类型公网 Service 不存在回环问题，主要是公网 CLB 收到的报文源 IP 是子机的出口公网 IP，而子机内部无法感知自己的公网 IP，当报文转发回子机时，不认为公网源 IP 是本机 IP，也就不存在回环。

### CLB 是否有避免回环机制？

有。CLB 会判断源 IP，如果发现后端 RS 也有相同 IP，就不考虑转发给这个 RS，而是选择其他 RS。但是源 Pod IP 跟后端 RS IP 并不相同，CLB 也不知道这两个 IP 是在同一节点，所以同样可能会转发过去，也就可能发生回环。

### Client 与 Server 反亲和部署能否规避？

如果将 Client 与 Server 通过反亲和性部署，避免 Client 跟 Server 部署在同一节点，能否规避 CLB 回环问题？

默认情况下，LB 通过节点 NodePort 绑定 RS，可能转发给任意节点 NodePort，此时 Client 与 Server 是否在同一节点都可能发生回环。但如果为 Service 设置 `externalTrafficPolicy: Local`， LB 就只会转发到有 Server Pod 的节点，如果 Client 与 Server 通过反亲和调度在不同节点，则此时不会发生回环，所以反亲和 + `externalTrafficPolicy: Local` 可以规避回环问题（包括内网 Ingress 和 LoadBalancer 类型内网 Service）。

### VPC-CNI 的 LB 直通 Pod 是否也存在 CLB 回环问题？

TKE 通常用的 Global Router 网络模式（网桥方案），还有一种是 VPC-CNI（弹性网卡方案）。目前 LB 直通 Pod 只支持 VPC-CNI 的 Pod，即 LB 不绑 NodePort 作为 RS，而是直接绑定后端 Pod 作为 RS，如下图所示：
![](https://main.qcloudimg.com/raw/e21903a2d23aef3cad564a44954a9aa4.png)

这样即可绕过 NodePort，不再像之前一样可能会转发给任意节点。但如果 Client 与 Server 在同一节点，同样可能会发生回环问题，通过反亲和可以规避。


### 有什么建议？

反亲和与 `externalTrafficPolicy: Local` 的规避方式不太优雅。一般来讲，访问集群内的服务避免访问本集群的 CLB，因为服务本身在集群内部，从 CLB 绕一圈不仅会增加网络链路的长度，还会引发回环问题。

访问集群内服务尽量使用 Service 名称，例如 `server.prod.svc.cluster.local` ，通过这样的配置将不会经过 CLB，也不会导致回环问题。

如果业务有耦合域名，不能使用 Service 名称，可以使用 coredns 的 rewirte 插件，将域名指向集群内的 Service，coredns 配置示例如下：
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |2-
        .:53 {
            rewrite name roc.oa.com server.prod.svc.cluster.local
        ...
```

如果多个 Service 共用一个域名，可以自行部署 Ingress Controller (例如 nginx-ingress)：
1. 用上述 rewrite 的方法将域名指向自建的 Ingress Controller。
2. 将自建的 Ingress 根据请求 location (域名+路径) 匹配 Service，再转发给后端 Pod。整段链路不经过 CLB，同意能规避回环问题。
