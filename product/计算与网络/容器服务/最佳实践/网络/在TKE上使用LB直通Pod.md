## 概述

Kubernetes 官方提供了 NodePort 类型的 Service，即给所有节点开通一个相同端口用于暴露该 Service。大多云上负载均衡 （Cloud Load Balancer，CLB） 类型 Service 的传统实现也都是基于 NodePort。即 CLB 后端绑定各节点的 NodePort，CLB 接收外界流量，转发到其中一个节点的 NodePort 上，再通过 Kubernetes 内部的负载均衡，使用 iptables 或 ipvs 转发到 Pod。示意图如下：
<img style="width:80%" src="https://main.qcloudimg.com/raw/dd6fa146520ca178ab17bc94e7f0fb1f.png" data-nonescope="true">
容器服务 TKE 使用相同的方式实现默认 CLB 类型 Service 与 Ingress，但目前还支持 CLB 直通 Pod 的方式，即 CLB  后端直接绑定 Pod IP + Port，不绑定节点的 NodePort。示意图如下：
<img style="width:35%" src="https://main.qcloudimg.com/raw/26a46cfd9e9687ec455260028b19353f.png" data-nonescope="true">



## 实现方式分析

### 传统 NodePort 方式问题分析
通常会使用 CLB 直接绑定 NortPort 此方式来创建云上 Ingress 或 LB 类型的 Service，但此传统 NodePort 实现方式会存在以下问题：
- 流量从 CLB 转发到 NodePort 后还需进行 SNAT 再转发到 Pod，造成额外的性能损耗。
- 如果流量过于集中到某几个 NodePort 时（例如，使用 nodeSelector 部署网关到固定几台节点上），可能导致源端口耗尽或 conntrack 插入冲突。
- NodePort 本身也充当负载均衡器，CLB 绑定过多节点 NodePort 时可能导致负载均衡状态过于分散，导致全局负载不均。


### CLB 直通 Pod 方式优势
使用 CLB 直通 Pod 的方式不但不会存在传统 NodePort 方式的问题，还具备以下优势：
- 由于没有 SNAT，获取源 IP 不再需要 `externalTrafficPolicy: Local`。
- 实现会话保持更简单，仅需让 CLB 开启会话保持即可，不需要设置 Service 的 `sessionAffinity`。


## 操作场景
使用 CLB 直通 Pod 通常有如下场景：
- 需在四层获取客户端真实源 IP，但不期望使用 `externalTrafficPolicy: Local` 的方式。
- 需进一步提升网络性能。
- 需会话保持更容易。
- 解决全局连接调度的负载不均。

## 前提条件
- Kubernetes 集群版本需高于1.12。
CLB 直接绑定 Pod 时检查 Pod 是否 Ready，需查看 Pod 是否 Running、是否通过 readinessProbe，及是否通过 CLB 对 Pod 的健康监测，此项依赖于 `ReadinessGate` 特性，该特性在 Kubernetes 1.12 开始支持。
- 集群网络模式必须开启 `VPC-CNI` 弹性网卡模式。可参考 [确认是否开启弹性网卡](#ElasticNetworkCard) 步骤进行确认。
目前 CLB 直通 Pod 的实现基于弹性网卡，暂不支持普通的网络模式。

## 操作步骤
### 确认是否开启弹性网卡[](id:ElasticNetworkCard)
请对应您的实际情况，按照以下步骤进行操作：
- 若您在创建集群时，“容器网络插件”选择为**VPC-CNI**，则创建的 Pod 已默认使用了弹性网卡，请跳过此步骤。
- 若您在创建集群时，“容器网络插件”选择为**Global Router**后开启了 VPC-CNI 支持。则为两种模式混用，创建的 Pod 默认不适用弹性网卡，需使用 YAML 创建工作负载，为 Pod 指定 `tke.cloud.tencent.com/networks: tke-route-eni` 该 annotation 来声明使用弹性网卡，并为其中一个容器添加例如 `tke.cloud.tencent.com/eni-ip: "1"`  的 requests 与 limits。YAML 示例如下：
``` yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     labels:
       app: nginx
     name: nginx-deployment-eni
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         annotations:
           tke.cloud.tencent.com/networks: tke-route-eni
         labels:
           app: nginx
       spec:
         containers:
           - image: nginx
             name: nginx
             resources:
               requests:
                 tke.cloud.tencent.com/eni-ip: "1"
               limits:
                 tke.cloud.tencent.com/eni-ip: "1"
```


### 创建 Service 时声明直连模式
当使用 CLB 的 Service 暴露服务时，需要声明使用直连模式。步骤如下：

#### 通过控制台创建 Service
如果通过控制台创建 Service，可以勾选“采用负载均衡直连Pod模式”，详情请参见 [创建 Service](https://cloud.tencent.com/document/product/457/45489#.E5.88.9B.E5.BB.BA-service)。如下图所示：
![](https://main.qcloudimg.com/raw/c8e40576c9108346a475ed0b7e1387fb.png)

#### 通过 YAML 创建 Service
如果通过 YAML 创建 Service，需要为 Service 加上 `service.cloud.tencent.com/direct-access: "true"` 的 annotation。示例如下：
>?如何使用 YAML 创建 Service 请参见 [创建 Service](https://cloud.tencent.com/document/product/457/45489#.E5.88.9B.E5.BB.BA-service2)。
>
``` yaml
   apiVersion: v1
   kind: Service
   metadata:
     annotations:
       service.cloud.tencent.com/direct-access: "true"
     labels:
       app: nginx
     name: nginx-service-eni
   spec:
     externalTrafficPolicy: Cluster
     ports:
     - name: 80-80-no
       port: 80
       protocol: TCP
       targetPort: 80
     selector:
       app: nginx
     sessionAffinity: None
     type: LoadBalancer
```


### 创建 Ingress 时声明直连模式
当使用 Ingress 暴露服务时，同样也需要声明使用直连模式。步骤如下：

#### 通过控制台创建 Ingress
如果通过控制台创建 Ingress，可以勾选“采用负载均衡直连Pod模式”，详情请参见 [创建 Ingress](https://cloud.tencent.com/document/product/457/31711#.E5.88.9B.E5.BB.BA-ingress)。如下图所示：
![](https://main.qcloudimg.com/raw/bdc245ba5b772f0def860448dcf5d007.png)

#### 通过 YAML 创建 Ingress
如果通过 YAML 创建 Ingress，需要为 Ingress 加上 `ingress.cloud.tencent.com/direct-access: "true"` 的 annotation。示例如下：
>?如何使用 YAML 创建 Ingress 请参见 [创建 Ingress](https://cloud.tencent.com/document/product/457/31711#.E5.88.9B.E5.BB.BA-ingress2)。
>
``` yaml
   apiVersion: networking.k8s.io/v1beta1
   kind: Ingress
   metadata:
     annotations:
       ingress.cloud.tencent.com/direct-access: "true"
       kubernetes.io/ingress.class: qcloud
     name: test-ingress
     namespace: default
   spec:
     rules:
     - http:
         paths:
         - backend:
             serviceName: nginx
             servicePort: 80
           path: /
```

## 参考资料

* [TKE 基于弹性网卡直连 Pod 的网络负载均衡](https://mp.weixin.qq.com/s/fJtlm5Qjm2BfzekC4RegCQ)
* [集群开启 VPC-CNI 模式网络](https://cloud.tencent.com/document/product/457/34993)
* [VPC-CNI 网络模式使用指引](https://cloud.tencent.com/document/product/457/48040)
