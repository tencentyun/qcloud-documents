# 使用场景
IDC 的资源是有限的，当有业务突发流量需要应对时，IDC内的算力资源不足以应对，使用公有云资源应对临时流量是不错的选择。TKE Resilience Chart 利用 <a href="https://cloud.tencent.com/product/eks" target="_blank">腾讯云弹性容器服务EKS</a> ,基于自定义的调度策略，通过添加虚拟节点的方式，将用户集群中的工作负载弹性上云，使用户IDC集群获得极大的弹性拓展能力，并带来以下好处：

1. 用户 IDC/私有云的硬件和维护成本保持不变
2. 实现了用户 IDC/私有云和公有云级别的应用高可用
3. 用户对公有云的资源是按需使用，按需付费

# 使用须知
1. 已经开通弹性容器服务 EKS。登陆 <a href="https://console.cloud.tencent.com/tke2/ecluster/startUp?rid=1" target="_blank">弹性容器服务控制台</a> 开通
2. 用户 IDC 与腾讯云 VPC 通过专线内网互联
3. IDC 集群的 API Server 地址，腾讯云 VPC 网络可达
4. 用户自有 IDC 集群可以访问公网，需要通过公网调用云 API

# TKE Resilience Chart 特性说明
## 组件说明
TKE Resilience Chart 主要是由虚拟节点管理器，调度器，容忍控制器3部分组成，如下表格：

| 简称                 | 组件名称       | 描述                                                                 |
| -------------------- | -------------- | -------------------------------------------------------------------- |
| eklet                | 虚拟节点管理器 | 负责 podsandbox 生命周期的管理，并对外提供原生kubelet与节点相关的接口  |
| tke-scheduler        | 调度器         | 负责根据调度策略将 workload 弹性上云, 仅会安装在非 TKE 发行版的 k8s 集群上,TKE 发行版集群不会安装此组件。其中 TKE 发行版（TKE Kubernetes Distro）是由腾讯云 TKE 发布的 k8s 发行版本，用于帮助用户创建与云上 TKE 完全一致的 K8s 集群，目前 TKE 发行版集群已经在GitHub开源，详情请参考 <a href="https://github.com/tkestack/tke-k8s-distro" target="_blank">这里</a>|
| admission-controller | 容忍控制器     | 负将处于 `pending` 状态的 pod 添加容忍，使其可以调度到虚拟节点上       |

## 主要特性
1. 如需要 EKS Pod 和本地集群的 Pod 互通，则要求本地集群是 Underlay 的网络模型（使用Calico之类的基于BGP路由而不是SDN封装的CNI插件），并且需要在腾讯云VPC中添加本地 Pod CIDR 的路由信息，请参考<a href="https://cloud.tencent.com/document/product/457/32199" target="_blank">路由配置</a>

2. Workload resilience 特性控制开关`AUTO_SCALE_EKS=true|false`分为全局开关和局部开关, 用来控制 workload 在`pending`的情况下是否弹性调度到腾讯云 EKS，如下表格：
- 全局开关：`kubectl get cm -n kube-system eks-config` 中 `AUTO_SCALE_EKS`,默认开启
- 局部开关：`spec.template.metadata.annotations['AUTO_SCALE_EKS']`

| 全局开关               | 局部开关               | 行为       |
| ---------------------- | ---------------------- | ---------- |
| `AUTO_SCALE_EKS=true`  | `AUTO_SCALE_EKS=false` | `调度成功` |
| `AUTO_SCALE_EKS=true`  | `未定义`               | `调度成功` |
| `AUTO_SCALE_EKS=true`  | `AUTO_SCALE_EKS=true`  | `调度成功` |
| `AUTO_SCALE_EKS=false` | `AUTO_SCALE_EKS=false` | `调度失败` |
| `AUTO_SCALE_EKS=false` | `未定义`               | `调度失败` |
| `AUTO_SCALE_EKS=false` | `AUTO_SCALE_EKS=true`  | `调度成功` |
| `未定义`               | `AUTO_SCALE_EKS=false` | `调度成功` |
| `未定义`               | `未定义`               | `调度成功` |
| `未定义`               | `AUTO_SCALE_EKS=true`  | `调度成功` |


2. 当使用社区版 K8S 的时候，需要在 workload 中指定调度器为 `tke-scheduler`, TKE 发行版 K8S 则不需要指定调度器
3. Workload 设定本地集群保留副本数量 `LOCAL_REPLICAS: N`
4. Workload`扩容`
- 当本地集群资源不足，并满足全局和局部开关中`调度成功`的行为设定，`pending`的 workload 将扩容到腾讯云 EKS
- 当实际创建 workload 副本数量达到N后，并满足全局和局部开关中`调度成功`的行为设定, `pending`的 workload 将扩容到腾讯云 EKS
5. Workload`缩容`
- TKE发行版 K8S 会优先缩容腾讯云 EKS 上的实例
- 社区版 K8S 会随机缩容
6. 调度规则的限制条件
- 无法调度 DaemonSet Pod到虚拟节点,此特性只在TKE发行版K8S有效，社区版K8S DaemonSet Pod会调度到虚拟节点，但会显示`DaemonsetForbidden`
- 无法调度 kube-system, tke-eni-ip-webhook 命名空间下的Pod到虚拟节点
- 无法调度 securityContext.sysctls["net.ipv4.ip_local_port_range"]的值包含61000 - 65534的端口
- 无法调度 pod.Annotations[tke.cloud.tencent.com/vpc-ip-claim-delete-policy]的Pod
- 无法调度 container(initContainer).ports[].containerPort(hostPort)包含61000 - 65534 的端口
- 无法调度 container(initContainer)中探针指定61000 - 65534的端口
- 无法调度除了 nfs，Cephfs，hostPath，qcloudcbs 以外的 PV
- 无法调度启用固定IP特性的pod到虚拟节点
7. 虚拟节点支持自定义默认 DNS 配置：用户可以在虚拟节点上新增 `eks.tke.cloud.tencent.com/resolv-conf`的 annotation 后，生成的 cxm 子机里的/etc/resolv.conf就会被更新成用户定义的内容。注意会覆盖原来虚拟节点的dns配置,最终会以用户的配置为准。
```
eks.tke.cloud.tencent.com/resolv-conf: |
   nameserver 4.4.4.4
   nameserver 8.8.8.8
```


# 操作步骤

## 获取 tke-resilience helm chart
```bash
 git clone https://github.com/tkestack/charts.git
```

## 配置相关信息

编辑 charts/incubator/tke-resilience/values.yaml，配置以下信息：
```bash
cloud:
  appID: "{腾讯云账号APPID}"
  ownerUIN: "{腾讯云用户账号ID}"
  secretID: "{腾讯云账号secretID}"
  secretKey: "{腾讯云账号secretKey}"
  vpcID: "{EKS POD放置的VPC ID}"
  regionShort: "{EKS POD 放置的region简称}"
  regionLong: "{EKS POD 放置的region全称}"
  subnets:
    - id: "{EKS POD 放置的子网ID}"
      zone: "{EKS POD 放置的可用区}" 
eklet:
  podUsedApiserver: "{当前集群的API Server地址}"
```
>?弹性容器服务支持售卖的地域和可用区请参考<a href="https://cloud.tencent.com/document/product/457/58172" target="_blank">这里</a>


## 安装 TKE Resilience Chart
在第三方集群中通过helm chart安装。安装Helm客户端连接集群，请参考<a href="https://cloud.tencent.com/document/product/457/32731" target="_blank">这里</a>

```bash
helm install tke-resilience --namespace kube-system ./tke-resilience --debug
```
确认 Helm 应用中是否安装完成。这里我使用的是 TKE 发行版的集群，所以没有安装 tke-scheduler.
```bash
# kubectl get pod -n kube-system | grep resilience
eklet-tke-resilience-5f9dcd99df-rgsmc           1/1     Running   0          43h
eks-admission-tke-resilience-5bb588dc44-9hvhs   1/1     Running   0          44h
```
查看集群中已经部署了1个虚拟节点
```bash
# kubectl get node
NAME                    STATUS   ROLES    AGE    VERSION
10.0.1.xx               Ready    <none>   2d4h   v1.20.4-tke.1
10.0.1.xx               Ready    master   2d4h   v1.20.4-tke.1
eklet-subnet-xxxxxxxx   Ready    <none>   43h    v2.4.6
```

## 创建测试用例
创建 demo 应用`nginx-deployment`,该应用有4个副本，其中3个在腾讯云 EKS，1个在本地集群，Yaml如下：
```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      annotations:
        AUTO_SCALE_EKS: "true"
        LOCAL_REPLICAS: "1" #设置本地集群运行的副本数为1
      labels:
        app: nginx
    spec:
      #schedulerName: tke-scheduler 如果是第三方集群则需要执行调度器为tke-scheduler
      containers:
      - name: nginx
        image: nginx
        imagePullPolicy: IfNotPresent
```
验证副本的状态以及分布，符合预期。
```bash
# kubectl get pod -owide
NAME                                READY   STATUS    RESTARTS   AGE   IP            NODE                    NOMINATED NODE   READINESS GATES
nginx-deployment-77b9b9bc97-cq9ds   1/1     Running   0          27s   10.232.1.88   10.0.1.xxx              <none>           <none>
nginx-deployment-77b9b9bc97-s9vzc   1/1     Running   0          27s   10.0.1.118    eklet-subnet-xxxxxxxx   <none>           <none>
nginx-deployment-77b9b9bc97-sd4z5   1/1     Running   0          27s   10.0.1.7      eklet-subnet-xxxxxxxx   <none>           <none>
nginx-deployment-77b9b9bc97-z86tx   1/1     Running   0          27s   10.0.1.133    eklet-subnet-xxxxxxxx   <none>           <none>
```

然后验证下缩容的特性，由于使用的是TKE发行版的集群，则会优先缩容腾讯云EKS的实例。这里应用的副本数从4调整为3。
```bash
# kubectl scale deployment nginx-deployment --replicas=3
```
这里我们可以看出，优先缩容云上的副本，符合预期。
```bash
# kubectl get pod -owide
NAME                                READY   STATUS    RESTARTS   AGE     IP            NODE                    NOMINATED NODE   READINESS GATES
nginx-deployment-77b9b9bc97-cq9ds   1/1     Running   0          7m38s   10.232.1.88   10.0.1.xxx              <none>           <none>
nginx-deployment-77b9b9bc97-s9vzc   1/1     Running   0          7m38s   10.0.1.118    eklet-subnet-xxxxxxxx   <none>           <none>
nginx-deployment-77b9b9bc97-sd4z5   1/1     Running   0          7m38s   10.0.1.7      eklet-subnet-xxxxxxxx   <none>           <none>
```
