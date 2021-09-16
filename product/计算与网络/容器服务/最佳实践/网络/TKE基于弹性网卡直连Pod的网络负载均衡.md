## 概述
Kubernetes 在集群接入层设计并提供了 `Service` 及 `Ingress` 两种原生资源，分别负责四层和七层的网络接入层配置。传统方案是创建 Ingress 或 LoadBalancer 类型的 Service 来绑定腾讯云负载均衡，将服务对外暴露。此方式将用户流量负载至用户节点的 NodePort 上，再通过 KubeProxy 组件转发到容器网络中，此方案在业务性能和能力方面的支持会有所局限。

为解决此问题，腾讯云容器 TKE 团队为**使用独立或托管集群的用户提供了一种新的网络模式：TKE 基于弹性网卡直连 Pod 的网络负载均衡**。此模式增强了性能和业务能力的支持，您可通过本文了解两种模式的区别，及如何开始使用直连模式。

## 方案对比

| 对比项             | 直连方案                         | NodePort 转发                     | Local 转发                  |
| ------------ | -------------------------------- | -------------------------------- | -------------------------- |
| 性能         | 无损失                           | NAT 转发+节点间转发               | 少量损失                   |
| Pod 更新      | 接入层后端主动同步更新，更新稳定 | 接入层后端 NodePort 保持不变       | 更新不同步可能导致服务中断 |
| 集群依赖     | 集群版本及 VPC-CNI 网络要求    | -                                | -                          |
| 业务能力限制 | 最佳                             | 无法获取来源 IP，无法进行会话保持 | 有条件的会话保持           |



## 传统模式问题分析

### 性能与特性
`KubeProxy` 在集群中会将用户 `NodePort` 的流量通过 NAT 的方式转发到集群网络中。存在以下问题：
- NAT 转发导致请求在性能上有一定的损失。
- 进行 NAT 操作本身会带来性能上的损失。
- NAT 转发的目的地址可能会使得流量在容器网络内跨节点转发。
- NAT 转发导致请求的来源 IP 被修改，客户端无法获取来源 IP。
- 当负载均衡的流量集中到几个 NodePort 时，过于集中的流量会导致 NodePort 的 SNAT 转发过多，使得源端口耗尽流量异常。还可能导致 conntrack 插入冲突导致丢包，影响性能。
- `KubeProxy` 的转发具有随机性，无法支持会话保持。
- `KubeProxy` 的每个 NodePort 具有独立的负载均衡作用，由于负载均衡无法收敛至一处，难以达到全局的负载均衡。

针对以上问题，以前提供给用户的技术建议为：通过 Local 转发的方式，避免 `KubeProxy` NAT 转发带来的问题。但因为转发的随机性，一个节点上部署多个副本时会话保持依旧无法支持，且在 Local 转发在滚动更新时，容易出现服务的闪断，对业务的滚动更新策略以及停机提出了更高的要求。

### 业务可用性

通过 NodePort 接入服务时，NodePort 的设计存在极大的容错性。负载均衡会绑定集群所有节点的 NodePort 作为后端，集群任意一个节点的访问服务时，流量将随机分配到集群的工作负载中。则表明 NodePort 或 Pod 的不可用均不会影响服务的流量接入。

和 Local 访问相同，在直接将负载均衡后端连接至用户 Pod 的情况下，当业务在滚动更新时，如果负载均衡不能够及时绑定至新的 Pod，业务的快速滚动可能导致业务入口的负载均衡后端数量严重不足甚至被清空。因此在业务滚动更新时，接入层的负载均衡的状态良好，即保证滚动更新的安全平稳。

### 负载均衡的控制面性能

负载均衡的控制面接口，包括创建、删除、修改四层及七层监听器、创建及删除七层规则、绑定各个监听器或者规则的后端。这些接口大部分为异步接口，需要轮询请求结果，接口的调用时间相对较长。当用户集群规模较大时，大量的接入层资源同步会导致组件存在很大时延上的压力。

## 新旧模式对比

### 性能对比

TKE 已上线 Pod 直连模式，此模式是对负载均衡的控制面优化。针对整个同步流程，重点优化了批量调用和后端实例查询两个远程调用较频繁的地方。**优化完成后，Ingress 典型场景下的控制面性能较优化前版本有了95% - 97%左右的性能提升。**目前同步的耗时主要集中在异步接口的等待上。

#### 后端节点突增数据
应对集群扩容的场景，数据如下：

| 七层规则数量 | 集群节点数量 | 集群节点数量（更新） | 优化前（秒）| 优化批量调用（秒） | 再优化后端实例查询（秒）| 耗时减少（百分比） |
| ------------ | ------------ | -------------------- | ----------- | ----------------- | ----------------------- | ----------------- |
| 200          | 1            | 10                   | 1313.056    | 227.908           | 31.548                  | 97.597%           |
| 200          | 1            | 20                   | 1715.053    | 449.795           | 51.248                  | 97.011%           |
| 200          | 1            | 30                   | 2826.913    | 665.619           | 69.118                  | 97.555%           |
| 200          | 1            | 40                   | 3373.148    | 861.583           | 90.723                  | 97.310%           |
| 200          | 1            | 50                   | 4240.311    | 1085.03           | 106.353                 | 97.491%           |

#### 七层规则突增数据
应对业务第一次上线部署到集群的场景，数据如下：

| 七层规则数量 | 七层规则数量（更新） | 集群节点数量 | 优化前（秒）| 优化批量调用（秒） | 再优化后端实例查询（秒）| 耗时减少（百分比）|
| ------------ | ------------------- | ------------ | ----------- | ----------------- | ----------------------- | ----------------- |
| 1            | 100                 | 50           | 1631.787    | 451.644           | 68.63                   | 95.79%            |
| 1            | 200                 | 50           | 3399.833    | 693.207           | 141.004                 | 95.85%            |
| 1            | 300                 | 50           | 5630.398    | 847.796           | 236.91                  | 95.79%            |
| 1            | 400                 | 50           | 7562.615    | 1028.75           | 335.674                 | 95.56%            |


对比图如下：
![](https://main.qcloudimg.com/raw/db8eaca82632a61fe34080543df741e4.png)
除控制面性能优化外，负载均衡能够直接访问容器网络的 Pod 即为组件业务能力最重要的组成部分，不仅避免了 NAT 转发性能上的损失，同时避免了 NAT 转发带来的各种对集群内业务功能影响，但在启动该项目时还不具备最优访问容器网络的支持。
新模式结合集群 CN I网络模式下 Pod 有弹性网卡入口这一特性，实现直接接入到负载均衡以达到直接访问的目的。负载均衡直接后端访问到容器网络，目前已经有通过云联网解决的方案。

在能够直接访问后，还需保证滚动更新时的可用性。我们采用官方提供的特性 `ReadinessGate`，此特性于1.12版本正式发布，主要用于控制 Pod 的状态。
默认情况下，Pod 有 PodScheduled、Initialized 及 ContainersReady 三种 Condition，当状态均为 Ready 时，Pod Ready 即通过了 Condition。但在云原生场景下，Pod 的状态需结合其他因素判断。而 `ReadinessGate` 提供允许为 Pod 状态判断增加栅栏，由第三方来进行判断与控制，Pod 的状态即可与第三方关联。



### 负载均衡流量对比

#### 传统 NodePort 模式
![](https://main.qcloudimg.com/raw/bec1eb64b73563129767536fc7bd4f66.png)
请求过程：
1. 请求流量进入负载均衡。
2. 请求被负载均衡转发到某一个节点的 NodePort。
3. KubeProxy 将来自 NodePort 的流量进行 NAT 转发，目的地址是随机的一个 Pod。
4. 请求进入容器网络，并根据 Pod 地址转发到对应节点。
5. 请求来到 Pod 所属节点，转发到 Pod。

#### Pod 新直连模式
![](https://main.qcloudimg.com/raw/2bfdf03dd24b359448c11915d70439cb.png)
请求过程：
1. 请求流量进入负载均衡。
2. 请求被负载均衡转发到某一个 Pod 的 ENI 弹性网卡。

### 直连与 Local 访问的区别
-  从性能上区别不大，开启 Local 访问时，流量不会进行 NAT 操作也不会进行跨节点转发，仅多了一个到容器网络的路由。
- 没有进行 NAT 操作，即可正确获取来源 IP。会话保持功能可能会有问题：当一个节点上存在多个 Pod 时，流量随机到达 Pod，此机制可能会使会话保持出现问题。

### 引入 ReadinessGate 
#### 滚动更新相关问题
如需引入 ReadinessGate，集群版本需高于1.12。
当用户开始为应用做滚动更新的时，`Kubernetes` 会根据更新策略进行滚动更新。但其判断一批 Pod 启动的标识仅包括 Pod 自身的状态，并不会考虑该 Pod 在负载均衡上是否配置健康检查且通过。如在接入层组件高负载时，不能及时对此类 Pod 进行及时调度，则滚动更新成功的 Pod 可能并没有正在对外提供服务，从而导致服务的中断。
为了关联滚动更新和负载均衡的后端状态，TKE 接入层组件引入了 Kubernetes 1.12中引入的新特性 `ReadinessGate`。TKE 接入层组件仅在确认后端绑定成功并且健康检查通过时，通过配置 `ReadinessGate `的状态来使 Pod 达到 Ready 的状态，从而推动整个工作负载的滚动更新。


#### 在集群中使用 ReadinessGate
Kubernetes 集群提供了服务注册的机制，只需要将您的服务以 `MutatingWebhookConfigurations` 资源的形式注册至集群即可。集群会在 Pod 创建的时候按照配置的回调路径进行通知，此时可对 Pod 进行创建前的操作，即给 Pod 加上 `ReadinessGate`。
>!此回调过程必须是 HTTPS 的，即需要在 `MutatingWebhookConfigurations` 中配置签发请求的 CA，并在服务端配置该 CA 签发的证书。


#### ReadinessGate 机制的灾难恢复
用户集群中的服务注册或证书有可能被用户删除，虽然这些系统组件资源不应该被用户修改或破坏。但在用户对集群的探索或是误操作下，这类问题会不可避免的出现。
接入层组件在启动时会检查以上资源的完整性，在完整性受到破坏时会重建以上资源，加强系统的鲁棒性。


### QPS 和网络时延对比

直连与 NodePort 是服务应用的接入层方案，其实最终参与工作的仍为用户部署的工作负载，用户工作负载的能力直接决定了业务的 QPS 等指标。
我们针对这两种接入层方案，在工作负载压力较低的情况下，重点对网络链路的时延进行了一些对比测试。直连在接入层的网络链路上能够优化10%左右的时间，且减少了大量 VPC 网络内的流量。测试场景从20节点到80节点，逐步增大集群规模，通过 wrk 工具对集群进行网络延时的测试。针对 QPS 和网络时延，直连场景与 NodePort 的对比测试如下图所示：
![](https://main.qcloudimg.com/raw/efaa648da5b1be6c99de635cc33c9779.png)

### KubeProxy 设计思路
`KubeProxy` 具备一定的缺点，但基于云上负载均衡、VPC 网络的各种特性，我们具有更加本地化的接入层方案。`KubeProxy` 对集群接入层的设计极具普适性及容错性，基本适用于所有业务场景下的集群，作为一个官方提供的组件此设计是非常合适的。

## 新模式使用指引

### 前置要求
- `Kubernetes` 集群版本需高于 1.12。
2. 集群网络模式需开启 `VPC-CNI` 弹性网卡模式。
3. 直连模式 `Service` 使用的工作负载需为 `VPC-CNI` 弹性网卡模式。

### 控制台操作指引
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 参考控制台[ 创建 Service ](https://cloud.tencent.com/document/product/457/45489#.E5.88.9B.E5.BB.BA-service)步骤，进入 “新建Service” 页面，根据实际需求设置 Service 参数。
主要参数信息需进行如下设置，如下图所示：

![](https://main.qcloudimg.com/raw/1e52f535cd9eb5712ddf6c4760952e70.png)
 - **服务访问方式**：选择为**提供公网访问**或**VPC内网访问**。
 - **网络模式**：勾选**采用负载均衡直连Pod模式**。
 - **Workload绑定**：选择**引用Worklocad**，并在弹出窗口中选择 VPC-CNI 模式的后端工作负载。
3. 单击**创建服务**即可完成创建。

### Kubectl 操作指引
- **Workload 示例：nginx-deployment-eni.yaml**
>! 注意 `spec.template.metadata.annotations` 中声明了 `tke.cloud.tencent.com/networks: tke-route-eni`，即表示在工作负载使用 VPC-CNI 弹性网卡模式。
>
```yaml
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
        - image: nginx:1.7.9
          name: nginx
          ports:
            - containerPort: 80
              protocol: TCP
```
- **Service 示例：nginx-service-eni.yaml**
> !`metadata.annotations` 中声明了 `service.cloud.tencent.com/direct-access: "true"`，Service 在同步负载均衡时将采用直连的方式配置访问后端。
>
```yaml
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
- **部署以上内容到集群**
>!在环境中您首先需要连接到集群（没有集群的需要先创建集群），可以参考 [帮助文档](#helpDoc) 配置 kubectl 连接集群。
>
```shell
  ➜  ~ kubectl apply -f nginx-deployment-eni.yaml
  deployment.apps/nginx-deployment-eni created
  
  ➜  ~ kubectl apply -f nginx-service-eni.yaml
  service/nginx-service-eni configured
  
  ➜  ~ kubectl get pod -o wide
  NAME                                   READY   STATUS    RESTARTS   AGE   IP               NODE          NOMINATED NODE   READINESS GATES
  nginx-deployment-eni-bb7544db8-6ljkm   1/1     Running   0          24s   172.17.160.191   172.17.0.3    <none>           1/1
  nginx-deployment-eni-bb7544db8-xqqtv   1/1     Running   0          24s   172.17.160.190   172.17.0.46   <none>           1/1
  nginx-deployment-eni-bb7544db8-zk2cx   1/1     Running   0          24s   172.17.160.189   172.17.0.9    <none>           1/1
  ➜  ~ kubectl get service -o wide
NAME                TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)        AGE    SELECTOR
kubernetes          ClusterIP      10.187.252.1    <none>           443/TCP        6d4h   <none>
  nginx-service-eni   LoadBalancer   10.187.254.62   150.158.221.31   80:32693/TCP   6d1h   app=nginx
```

## 总结
目前 TKE 利用弹性网卡实现了 Pod 直连的网络模式，我们还将对这个特性进行更多优化，包括但不限于：
- 不依赖 VPC-ENI 的网络模式，实现普通容器网络下的 Pod 直连。
- 支持在 Pod 删除之前，摘除负载均衡后端。

与业界对比：
- AWS 有类似方案，通过弹性网卡的方式实现了 Pod 直连。
- Google Kubernetes Engine，GKE 也有类似方案，结合 Google Cloud Load Balancing，CLB 的 Network Endpoint Groups，NEG 特性实现接入层直连 Pod。


## 参考资料[](id:helpDoc)

- [Kubernetes Service 介绍](https://kubernetes.io/docs/concepts/services-networking/service)
2. [Kubernetes Ingress 介绍](https://kubernetes.io/docs/concepts/services-networking/ingress)
3. [Kubernetes Deployments 滚动更新策略](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy)
4. [Kubernetes Pods ReadinessGate 特性](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate)
5. [Kubernetes 通过 Local 转发获取来源 IP](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip)
6. [TKE 容器服务 网络模式选型](https://cloud.tencent.com/document/product/457/41636)
7. [TKE 容器服务 VPC-CNI网络模式](https://cloud.tencent.com/document/product/457/34993)
8. [TKE 容器服务 配置kubectl并连接集群](https://cloud.tencent.com/document/product/457/32191)
9. [AWS ALB Ingress Controller](https://aws.amazon.com/cn/blogs/opensource/kubernetes-ingress-aws-alb-ingress-controller/)
10. [GKE 通过独立 NEG 配置容器原生负载平衡](https://cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg)
