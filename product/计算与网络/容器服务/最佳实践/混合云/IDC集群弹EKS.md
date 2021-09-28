## 使用场景
IDC 的资源有限，当需要应对业务突发流量，IDC 内的算力资源不足以应对时，可以选择使用公有云资源应对临时流量。TKE Resilience Chart 利用 <a href="https://cloud.tencent.com/product/eks"> 腾讯云弹性容器服务 EKS</a>，基于自定义的调度策略，通过添加虚拟节点的方式，将用户集群中的工作负载弹性上云，使用户 IDC 集群获得极大的弹性拓展能力，优势如下：

1. 用户 IDC / 私有云的硬件和维护成本保持不变。
2. 实现了用户 IDC / 私有云和公有云级别的应用高可用。
3. 用户按需使用公有云的资源，按需付费。

## 使用须知
1. 已开通 [弹性容器服务 EKS](https://console.cloud.tencent.com/tke2/ecluster/startUp?rid=1)。
2. 用户 IDC 与腾讯云 VPC 通过专线内网互联。
3. IDC 集群的 API Server 地址，腾讯云 VPC 网络可达。
4. 用户自有 IDC 集群可以访问公网，需要通过公网调用云 API。

## TKE Resilience Chart 特性说明
### 组件说明
TKE Resilience Chart 主要是由虚拟节点管理器，调度器，容忍控制器3部分组成，如表格所示：

| 简称                 | 组件名称       | 描述                                                                 |
| -------------------- | -------------- | -------------------------------------------------------------------- |
| eklet                | 虚拟节点管理器 | 负责 Podsandbox 生命周期的管理，并对外提供原生 kubelet 与节点相关的接口。  |
| tke-scheduler        | 调度器         | 负责根据调度策略将 workload 弹性上云，仅会安装在非 TKE 发行版的 K8S 集群上，TKE 发行版集群不会安装此组件。其中 TKE 发行版（TKE Kubernetes Distro）是由腾讯云 TKE 发布的 K8S 发行版本，用于帮助用户创建与云上 TKE 完全一致的 K8S 集群，目前 TKE 发行版集群已经在 GitHub 开源，详情见 <a href="https://github.com/tkestack/tke-K8S-distro" target="_blank">TKE Kubernetes Distro</a>。|
| admission-controller | 容忍控制器     | 负责为处于 `pending` 状态的 Pod 添加容忍，使其可以调度到虚拟节点上。       |

### 主要特性
1. 如需要 EKS Pod 和本地集群的 Pod 互通，则要求本地集群是 Underlay 的网络模型（使用 Calico 之类的基于 BGP 路由，而不是 SDN 封装的 CNI 插件），并且需要在腾讯云 VPC 中添加本地 Pod CIDR 的路由信息，详情见 [路由配置](https://cloud.tencent.com/document/product/457/32199)。
2. Workload resilience 特性控制开关 `AUTO_SCALE_EKS=true|false` 分为全局开关和局部开关，用来控制 workload 在 `pending` 的情况下是否弹性调度到腾讯云 EKS，如表格所示：
 - 全局开关：`kubectl get cm -n kube-system eks-config` 中 `AUTO_SCALE_EKS`，默认开启。
 - 局部开关：`spec.template.metadata.annotations ['AUTO_SCALE_EKS']`
<table>
<thead>
<tr>
<th>全局开关</th>
<th>局部开关</th>
<th>行为</th>
</tr>
</thead>
<tbody><tr>
<td>AUTO_SCALE_EKS=true</td>
<td>AUTO_SCALE_EKS=false</td>
<td>调度成功 </td>
</tr>
<tr>
<td> AUTO_SCALE_EKS=true </td>
<td> 未定义 </td>
<td> 调度成功 </td>
</tr>
<tr>
<td> AUTO_SCALE_EKS=true </td>
<td> AUTO_SCALE_EKS=true </td>
<td> 调度成功 </td>
</tr>
<tr>
<td> AUTO_SCALE_EKS=false </td>
<td> AUTO_SCALE_EKS=false </td>
<td> 调度失败 </td>
</tr>
<tr>
<td> AUTO_SCALE_EKS=false </td>
<td> 未定义 </td>
<td> 调度失败 </td>
</tr>
<tr>
<td> AUTO_SCALE_EKS=false </td>
<td> AUTO_SCALE_EKS=true </td>
<td> 调度成功 </td>
</tr>
<tr>
<td> 未定义 </td>
<td> AUTO_SCALE_EKS=false </td>
<td> 调度成功 </td>
</tr>
<tr>
<td> 未定义 </td>
<td> 未定义 </td>
<td> 调度成功 </td>
</tr>
<tr>
<td> 未定义 </td>
<td> AUTO_SCALE_EKS=true </td>
<td> 调度成功 </td>
</tr>
</tbody></table>

3. 当使用社区版 K8S 的时候，需要在 workload 中指定调度器为 `tke-scheduler`，TKE 发行版 K8S 则不需要指定调度器。
4. Workload 设定本地集群保留副本数量 `LOCAL_REPLICAS: N`。
5. Workload 扩容：
  - 当本地集群资源不足，并满足全局和局部开关中**调度成功**的行为设定，`pending` 的 workload 将扩容到腾讯云 EKS。
  - 当实际创建 workload 副本数量达到 N 后，并满足全局和局部开关中**调度成功**的行为设定，`pending` 的 workload 将扩容到腾讯云 EKS。
6. Workload 缩容：
  - TKE 发行版 K8S 会优先缩容腾讯云 EKS 上的实例。
  - 社区版 K8S 会随机缩容。
7. 调度规则的限制条件：
  - 无法调度 DaemonSet Pod 到虚拟节点，此特性只在 TKE 发行版 K8S 有效，社区版 K8S DaemonSet Pod 会调度到虚拟节点，但会显示 `DaemonsetForbidden`。
  - 无法调度 kube-system，tke-eni-ip-webhook 命名空间下的 Pod 到虚拟节点。
  - 无法调度 securityContext.sysctls ["net.ipv4.ip_local_port_range"] 的值包含61000 - 65534的端口。
  - 无法调度 Pod.Annotations [tke.cloud.tencent.com/vpc-ip-claim-delete-policy] 的 Pod。
  - 无法调度 container (initContainer).ports [].containerPort (hostPort) 包含61000 - 65534的端口。
  - 无法调度 container (initContainer) 中探针指定61000 - 65534的端口。
  - 无法调度除了 nfs，Cephfs，hostPath，qcloudcbs 以外的 PV。
  - 无法调度启用固定 IP 特性的 Pod 到虚拟节点。
8. 虚拟节点支持自定义默认 DNS 配置：用户在虚拟节点上新增 `eks.tke.cloud.tencent.com/resolv-conf` 的 annotation 后，生成的 cxm 子机里的 /etc/resolv.conf 就会被更新成用户定义的内容。**注意**：会覆盖原来虚拟节点的 dns 配置，最终以用户的配置为准。
```
eks.tke.cloud.tencent.com/resolv-conf: |
   nameserver 4.4.4.4
   nameserver 8.8.8.8
```


## 操作步骤

### 获取 tke-resilience helm chart
```bash
 git clone https://github.com/tkestack/charts.git
```

### 配置相关信息

编辑 charts/incubator/tke-resilience/values.yaml，配置以下信息：
```bash
cloud:
  appID: "{腾讯云账号 APPID}"
  ownerUIN: "{腾讯云用户账号 ID}"
  secretID: "{腾讯云账号 secretID}"
  secretKey: "{腾讯云账号 secretKey}"
  vpcID: "{EKS Pod 放置的 VPC ID}"
  regionShort: "{EKS Pod 放置的 region 简称}"
  regionLong: "{EKS Pod 放置的 region 全称}"
  subnets:
    - id: "{EKS Pod 放置的子网 ID}"
      zone: "{EKS Pod 放置的可用区}" 
eklet:
  PodUsedApiserver: "{当前集群的 API Server 地址}"
```
>? 弹性容器服务支持售卖的地域和可用区请参见 [地域和可用区](https://cloud.tencent.com/document/product/457/58172)。 

### 安装 TKE Resilience Chart
您可通过 [本地 Helm 客户端连接集群](https://cloud.tencent.com/document/product/457/32731)。

执行以下命令，在第三方集群中通过 Helm Chart 安装 TKE Resilience Chart。
```bash
helm install tke-resilience --namespace kube-system ./tke-resilience --debug
```
执行以下命令，确认 Helm 应用中组件是否安装完成。本文以 TKE 发行版的集群为例，未安装 tke-scheduler。
```bash
# kubectl get Pod -n kube-system | grep resilience
eklet-tke-resilience-5f9dcd99df-rgsmc           1/1     Running   0          43h
eks-admission-tke-resilience-5bb588dc44-9hvhs   1/1     Running   0          44h
```
查看集群中已经部署了1个虚拟节点。
```bash
# kubectl get node
NAME                    STATUS   ROLES    AGE    VERSION
10.0.1.xx               Ready    <none>   2d4h   v1.20.4-tke.1
10.0.1.xx               Ready    master   2d4h   v1.20.4-tke.1
eklet-subnet-xxxxxxxx   Ready    <none>   43h    v2.4.6
```

### 创建测试用例
创建 demo 应用 `nginx-deployment`，该应用有4个副本，其中3个在腾讯云 EKS，1个在本地集群，Yaml 示例如下：
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
        LOCAL_REPLICAS: "1" #设置本地集群运行的副本数为 1
      labels:
        app: nginx
    spec:
      #schedulerName: tke-scheduler 如果是第三方集群则需要执行调度器为 tke-scheduler
      containers:
      - name: nginx
        image: nginx
        imagePullPolicy: IfNotPresent
```
验证副本的状态以及分布，符合预期。
```bash
# kubectl get Pod -owide
NAME                                READY   STATUS    RESTARTS   AGE   IP            NODE                    NOMINATED NODE   READINESS GATES
nginx-deployment-77b9b9bc97-cq9ds   1/1     Running   0          27s   10.232.1.88   10.0.1.xxx              <none>           <none>
nginx-deployment-77b9b9bc97-s9vzc   1/1     Running   0          27s   10.0.1.118    eklet-subnet-xxxxxxxx   <none>           <none>
nginx-deployment-77b9b9bc97-sd4z5   1/1     Running   0          27s   10.0.1.7      eklet-subnet-xxxxxxxx   <none>           <none>
nginx-deployment-77b9b9bc97-z86tx   1/1     Running   0          27s   10.0.1.133    eklet-subnet-xxxxxxxx   <none>           <none>
```

并验证缩容的特性，由于使用的是 TKE 发行版的集群，会优先缩容腾讯云 EKS 的实例。这里应用的副本数从4调整为3。
```bash
# kubectl scale deployment nginx-deployment --replicas=3
```
由以下结果可以看出，优先缩容了云上的副本，符合预期。
```bash
# kubectl get Pod -owide
NAME                                READY   STATUS    RESTARTS   AGE     IP            NODE                    NOMINATED NODE   READINESS GATES
nginx-deployment-77b9b9bc97-cq9ds   1/1     Running   0          7m38s   10.232.1.88   10.0.1.xxx              <none>           <none>
nginx-deployment-77b9b9bc97-s9vzc   1/1     Running   0          7m38s   10.0.1.118    eklet-subnet-xxxxxxxx   <none>           <none>
nginx-deployment-77b9b9bc97-sd4z5   1/1     Running   0          7m38s   10.0.1.7      eklet-subnet-xxxxxxxx   <none>           <none>
```
