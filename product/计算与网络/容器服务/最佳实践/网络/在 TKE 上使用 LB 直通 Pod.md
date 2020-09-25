## 什么是 LB 直通 Pod ?

Kubernetes 官方提供了 NodePort 类型的 Service，即给所有节点开一个相同端口用于暴露这个 Service，大多云上 LoadBalancer 类型 Service 的传统实现也都基于 NodePort，即 LB 后端绑各节点的 NodePort，LB 接收外界流量，转发大其中其中一个节点的 NodePort 上，再通过 Kubernetes 内部的负载均衡，使用 iptables 或 ipvs 转发到 Pod:

<img style="width:450px" src="https://main.qcloudimg.com/raw/dd6fa146520ca178ab17bc94e7f0fb1f.png" data-nonescope="true">

TKE 默认的 LoadBalancer 类型 Service 与默认的 Ingress 也都是这样实现的，但目前也支持了 LB 直通 Pod 的方式，即 LB 后端直接绑 Pod IP+Port，不绑节点的 NodePort:

<img style="width:450px" src="https://main.qcloudimg.com/raw/26a46cfd9e9687ec455260028b19353f.png" data-nonescope="true">

## 为什么需要 LB 直通 Pod ?

LB 直接绑 NodePort 来实现云上的 Ingress 或 LoadBalancer 类型 Service 是最简单通用的方法，那为什么有了这种实现还不够，还要搞个 LB 直通 Pod 的模式？

首先，我们分析下传统 NodePort 实现方式存在的一些问题：

1. 流量从 LB 转发到 NodePort 之后还需要进行 SNAT，再转发到 Pod，带来一些额外的性能损耗。
2. 如果流量过于集中到某几个 NodePort 时(比如使用 nodeSelector 部署网关到固定几台节点上)，可能导致源端口耗尽，或者 conntrack 插入冲突。
3. NodePort 本身也充当负载均衡器，LB 绑定过多节点 NodePort 可能导致负载均衡状态过于分散，导致全局负载不均。

如果使用 LB 直通 Pod 的方式，以上问题都将消失，并且还有一些其它好处：

1. 由于没有 SNAT，获取源 IP 不再需要 `externalTrafficPolicy: Local` 。
2. 实现会话保持更简单，只需要让 CLB 开启会话保持即可，不需要设置 Service 的 `sessionAffinity`。

所以使用 LB 直通 Pod 的场景通常有:

1. 在四层获取客户端真实源 IP，但又不希望通过使用 `externalTrafficPolicy: Local` 的方式。
2. 希望进一步提升网络性能。
3. 让会话保持更容易。
4. 解决全局连接调度的负载不均。

## 需要什么前提条件 ?

使用 LB 直通 Pod，需要满足以下前提条件：

1. `Kubernetes`集群版本需要高于 1.12，因为 LB 直绑 Pod，检查 Pod 是否 Ready，除了看 Pod 是否 Running、是否通过 readinessProbe 外， 还需要看 LB 对 Pod 的健康探测是否通过，这依赖于 `ReadinessGate`  特性，该特性在 Kubernetes 1.12 才开始支持。

2. 集群网络模式必须开启`VPC-CNI`弹性网卡模式，因为目前 LB 直通 Pod 的实现是基于弹性网卡的，普通的网络模式暂时不支持，这个在未来将会支持。

## 怎么用 ?

由于目前 LB 直通 Pod 依赖 VPC-CNI，需要保证 Pod 使用了弹性网卡:

1. 如果集群创建时选择的是 VPC-CNI 网络插件，那么创建的 Pod 默认就使用了弹性网卡。

2. 如果集群创建时选择的是 Global Router 网络创建，后来开启了 VPC-CNI 支持，即两种模式混用，创建的 Pod 默认不使用弹性网卡，需要使用 yaml 创建工作负载，为 Pod 指定 `tke.cloud.tencent.com/networks: tke-route-eni` 这个 annotation 来声明使用弹性网卡，并且为其中一个容器加上 `tke.cloud.tencent.com/eni-ip: "1"`  这样的 requests 与 limits，示例:

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

当你用 LoadBalancer 的 Service 暴露服务时，需要声明使用直连模式：

1. 如果通过控制台创建 Service，可以勾选 `采用负载均衡直连Pod模式`:

<img style="width:450px" src="https://main.qcloudimg.com/raw/245579f6dda2e8ab04ed84fbc51967ff.png" data-nonescope="true">

2. 如果通过 yaml 创建 Service，需要为 Service 加上 `service.cloud.tencent.com/direct-access: "true"` 的 annotation:

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


当使用 Ingress 暴露服务时，同样也需要声明使用直连模式:

1. 如果通过控制台创建 Ingress，可以勾选 `采用负载均衡直连Pod模式`:

<img style="width:450px" src="https://main.qcloudimg.com/raw/9fedf829f71a37234994f9921cf9fe39.png" data-nonescope="true">

2. 如果通过 yaml 创建 Ingress，需要为 Ingress 加上 `ingress.cloud.tencent.com/direct-access: "true"` 的 annotation:

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

* TKE 基于弹性网卡直连 Pod 的网络负载均衡: https://mp.weixin.qq.com/s/fJtlm5Qjm2BfzekC4RegCQ
* 集群开启 VPC-CNI 模式网络: https://cloud.tencent.com/document/product/457/34993
* VPC-CNI 网络模式使用指引: https://cloud.tencent.com/document/product/457/48040