## 操作场景

在腾讯云容器服务 TKE 中，Pod Networking 的功能是由基于 IaaS 层私有网络 VPC 的高性能容器网络实现，而 service proxy 功能是由 kube-proxy 所支持的 ipvs/iptables 两种模式提供。TKE 通过 Network Policy 扩展组件提供网络隔离能力。




## 相关概念

### Network Policy

[Network Policy ](https://kubernetes.io/docs/concepts/services-networking/network-policies/) 是 Kubernetes 提供的一种资源，用于定义基于 Pod 的网络隔离策略。描述了一组 Pod 是否可以与其他组 Pod，以及其他 network endpoints 进行通信。


## 操作步骤

### 在 TKE 上启用 NetworkPolicy 扩展组件
具体操作步骤可参见 [NetworkPolicy 说明](https://cloud.tencent.com/document/product/457/50841)。

### NetworkPolicy 配置示例
<dx-alert infotype="explain" title="">
资源对象的 apiVersion 可能因为您集群的 Kubernetes 版本不同而不同，您可通过 `kubectl api-versions` 命令查看当前资源对象的 apiVersion。
</dx-alert>


- nsa namespace 下的 Pod 可互相访问，而不能被其他任何 Pod 访问。
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
     name: npa
     namespace: nsa
spec:
     ingress: 
     - from:
       - podSelector: {} 
     podSelector: {} 
     policyTypes:
     - Ingress
```
- nsa namespace 下的 Pod 不能被任何 Pod 访问。
 ```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
      name: npa
      namespace: nsa
spec:
      podSelector: {}
      policyTypes:
      - Ingress
```
- nsa namespace 下的 Pod 只在 6379/TCP 端口可以被带有标签 app: nsb 的 namespace 下的 Pod 访问，而不能被其他任何 Pod 访问。
```yaml
apiVersion: networking.k8s.io/v1
   kind: NetworkPolicy
   metadata:
     name: npa
     namespace: nsa
   spec:
     ingress:
     - from:
       - namespaceSelector:
           matchLabels:
             app: nsb
       ports:
       - protocol: TCP
         port: 6379
     podSelector: {}
     policyTypes:
     - Ingress
```
- nsa namespace 下的 pod 可以访问 CIDR 为14.215.0.0/16的 network endpoint 的5978/TCP 端口，而不能访问其他任何 network endpoints（此方式可以用来为集群内的服务开访问外部 network endpoints 的白名单）。
```yaml
apiVersion: networking.k8s.io/v1
   kind: NetworkPolicy
   metadata:
     name: npa
     namespace: nsa
   spec:
     egress:
     - to:
       - ipBlock:
           cidr: 14.215.0.0/16
       ports:
       - protocol: TCP
         port: 5978
     podSelector: {}
     policyTypes:
     - Egress
```
- default namespace 下的 Pod 只在80/TCP 端口可以被 CIDR 为14.215.0.0/16的 network endpoint 访问，而不能被其他任何 network endpoints 访问。
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
     name: npd
     namespace: default
spec:
     ingress:
     - from:
       - ipBlock:
           cidr: 14.215.0.0/16
       ports:
       - protocol: TCP
         port: 80
     podSelector: {}
     policyTypes:
     - Ingress
```

## 性能测试方案
### NetworkPolicy 扩展组件功能测试
运行 K8S 社区针对 `NetworkPolicy` 的 [e2e 测试](https://github.com/kubernetes/kubernetes/blob/release-1.18/test/e2e/network/network_policy.go)，结果如下：

| NetworkPolicy Feature| 是否支持 |
|---------|---------|
| should support a 'default-deny' policy | 支持 |
| should enforce policy to allow traffic from pods within server namespace based on PodSelector | 支持 |
| should enforce policy to allow traffic only from a different namespace, based on NamespaceSelector | 支持 |
| should enforce policy based on PodSelector with MatchExpressions | 支持 |
| should enforce policy based on NamespaceSelector with MatchExpressions | 支持 |
| should enforce policy based on PodSelector or NamespaceSelector | 支持 |
| should enforce policy based on PodSelector and NamespaceSelector | 支持 |
| should enforce policy to allow traffic only from a pod in a different namespace based on PodSelector and NamespaceSelector | 支持 |
| should enforce policy based on Ports | 支持 |
| should enforce multiple, stacked policies with overlapping podSelectors | 支持 |
| should support allow-all policy | 支持 |
| should allow ingress access on one named port | 支持 |
| should allow ingress access from namespace on one named port | 支持 |
| should allow egress access on one named port | 不支持 |
| should enforce updated policy | 支持 |
| should allow ingress access from updated namespace | 支持 |
| should allow ingress access from updated pod | 支持 |
| should deny ingress access to updated pod | 支持 |
| should enforce egress policy allowing traffic to a server in a different namespace based on PodSelector and NamespaceSelector | 支持 |
| should enforce multiple ingress policies with ingress allow-all policy taking precedence | 支持 |
| should enforce multiple egress policies with egress allow-all policy taking precedence | 支持 |
| should stop enforcing policies after they are deleted | 支持 |
| should allow egress access to server in CIDR block | 支持 |
| should enforce except clause while egress access to server in CIDR block  | 支持 |
|should enforce policies to check ingress and egress policies can be controlled independently based on PodSelector | 支持 |




### NetworkPolicy 扩展组件功能测试（旧版）

在 k8s 集群中部署大量的 Nginx 服务，通过 ApacheBench 工具压测固定的一个服务，对比开启和不开启 kube-router 场景下的 QPS，衡量 kube-router 带来的性能损耗。

### 测试环境

- VM 数量：100
- VM 配置：2核4G
- VM OS：Ubuntu
- k8s：1.10.5
- kube-router version：0.2.0 

### 测试流程
1. 部署1个 service，对应两个 Pod（Nginx），作为测试组。
2. 部署1000个 service，每个分别对应 2/6/8 个 Pod（Nginx），作为干扰组。
3. 部署 NetworkPolicy 规则，使得所有 Pod 都被选中，以便产生足够数量的 iptables 规则：
```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
      name: npd
      namespace: default
spec:
      ingress:
      - from:
        - ipBlock:
            cidr: 14.215.0.0/16
        ports:
        - protocol: TCP
         port: 9090
      - from:
        - ipBlock:
            cidr: 14.215.0.0/16
       ports:
        - protocol: TCP
          port: 8080
      - from:
        - ipBlock:
            cidr: 14.215.0.0/16
        ports:
        - protocol: TCP
          port: 80
      podSelector: {}
      policyTypes:
      - Ingress
```
4. 使用 ab 压测测试组的服务，记录 QPS。
得出性能曲线如下：
![](https://main.qcloudimg.com/raw/c6502fe1cffbda36c35f76626bc876c7.png)
 - 图例中：
    - 1000service2000pod、1000service6000pod、1000service8000pod 为 pod 未开启 kube-route
    - 1000service2000pod-kube-route、1000service6000pod-kube-route、1000service8000pod-kube-route 为 pod 已开启 kube-route
 - X轴：ab 并发数
 - Y轴：QPS

### 测试结论

Pod 数量从2000增长到8000，开启 kube-router 时的性能比不开启时要下降10% - 20%。


## 相关说明

#### 腾讯云提供的 kube-router 版本

NetworkPolicy 扩展组件基于社区的[ Kube-Router ](https://github.com/cloudnativelabs/kube-router)项目，在该组件的开发过程中，腾讯云 PaaS 团队积极建设社区，持续贡献了一些 feature support 及 bug fix，提交 PR 均已被社区合并，列表如下：

- [processing k8s version for NPC #488](https://github.com/cloudnativelabs/kube-router/pull/488)
- [Improve health check for cache synchronization #498](https://github.com/cloudnativelabs/kube-router/pull/498)
- [Make the comments of the iptables rules in NWPLCY chains more accurate and reasonable #527](https://github.com/cloudnativelabs/kube-router/pull/527)
- [Use ipset to manage multiple CIDRs in a network policy rule #529](https://github.com/cloudnativelabs/kube-router/pull/529)
- [Add support for 'except' feature of network policy rule#543](https://github.com/cloudnativelabs/kube-router/pull/543)
- [Avoid duplicate peer pods in npc rules variables #634](https://github.com/cloudnativelabs/kube-router/pull/634)
- [Support named port of network policy #679](https://github.com/cloudnativelabs/kube-router/pull/679)

