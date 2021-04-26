## 概述
Kubernetes Pod 垂直自动扩缩（[Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/vpa-release-0.8/vertical-pod-autoscaler)，以下简称 VPA）可以自动调整 Pod 的 CPU 和内存预留，帮助提高集群资源利用率并释放 CPU 和内存供其它 Pod 使用。本文介绍如何在腾讯云容器服务 TKE 上使用社区版 VPA 功能实现 Pod 垂直扩缩容。

## 使用场景

VPA 自动伸缩特性使容器服务具有非常灵活的自适应能力。应对业务负载急剧飙升的情况，VPA 能够在用户设定范围内快速扩大容器的 Request。在业务负载变小的情况下，VPA 可根据实际情况适当缩小 Request 节省计算资源。整个过程自动化无须人为干预，适用于需要快速扩容、有状态应用扩容等场景。此外，VPA 可用于向用户推荐更合理的 Request，在保证容器有足够使用的资源的情况下，提升容器的资源利用率。


## VPA 优势
相较于 [自动伸缩功能 HPA](https://cloud.tencent.com/document/product/457/37384)，VPA 具有以下优势：
- VPA 扩容不需要调整 Pod 副本数量，扩容速度更快。
- VPA 可为有状态应用实现扩容，HPA 则不适合有状态应用的水平扩容。
- Request 设置过大，使用 HPA 水平缩容至一个 Pod 时集群资源利用率仍然很低，此时可以通过 VPA 进行垂直缩容提高集群资源利用率。



## VPA 限制

<dx-alert infotype="notice" title="">
社区版 VPA 功能当前处于试验阶段，请谨慎使用。推荐您将 “updateMode” 设置为 “Off”，以确保 VPA 不会自动为您更换 Request 数值。您仍然可以在 VPA 对象中查看已绑定负载的 Request 推荐值。
</dx-alert>

- 自动更新正在运行的 Pod 资源是 VPA 的一项实验功能。当 VPA 更新 Pod 资源时，会导致 Pod 的重建和重启，并且有可能被调度到其他节点上。
- VPA 不会驱逐不在控制器下运行的 Pod。对于此类 Pod，`Auto` 模式等效于 `Initial`。
- VPA 与 HPA 不可同时在 CPU 和内存预留上运行。如需同时运行 **VPA** 与 **HPA**，则 HPA 需使用除 CPU 和内存以外的指标，详情可参见 [在 TKE 上使用自定义指标进行弹性伸缩](https://cloud.tencent.com/document/product/457/50125)。
- VPA 使用 Admission Webhook 作为其准入控制器。如果集群中存在其他的 Admission Webhook，需要确保它们不会与 VPA 的 Admission Webhook 发生冲突。准入控制器的执行顺序定义在 API Server 的配置参数中。
- VPA 会处理大多数 OOM（Out Of Memory）事件。
- VPA 性能尚未在大型群集中进行测试。
- VPA 对 Pod 资源 Request 的建议值可能会超出可用资源（例如节点资源上限、空闲资源或资源配额），并导致 Pod 处于 Pending 状态无法被调度。同时使用 VPA 与 [Cluster Autoscaler](https://cloud.tencent.com/document/product/457/43719) 可以部分解决此问题。
- 与同一个 Pod 匹配的多个 VPA 资源具有未定义的行为。

更多 VPA 限制请参见 [VPA Known limitations](https://github.com/kubernetes/autoscaler/tree/vpa-release-0.8/vertical-pod-autoscaler#known-limitations)。

## 前提条件
- 已创建容器服务 TKE 集群。如果您还未创建集群，请参考 [快速创建一个标准集群](https://cloud.tencent.com/document/product/457/54231)。
- 已使用命令行工具 Kubectl 连接集群。如果您还未连接集群，请参考 [连接集群](https://cloud.tencent.com/document/product/457/32191)。


## 操作步骤

### 部署 VPA[](id:VPA)
1. 登录集群中的云服务器。 
2. 通过命令行工具 Kubectl 从本地客户端机器连接到 TKE 集群。
3. 执行以下命令，克隆 [kubernetes/autoscaler](https://github.com/kubernetes/autoscaler) GitHub Repository。
```sh
git clone https://github.com/kubernetes/autoscaler.git
```
4. 执行以下命令，切换至 `vertical-pod-autoscaler` 目录。
```
cd autoscaler/vertical-pod-autoscaler/
```
5. （可选）如果您已经部署其他版本的 VPA，执行以下命令将其删除。否则将会产生异常影响。
```
./hack/vpa-down.sh
```
6. 执行以下命令，将 VPA 相关组件部署到您的集群。
```
./hack/vpa-up.sh
```
7. 执行以下命令，验证是否成功创建 VPA 组件。
```
kubectl get deploy -n kube-system | grep vpa
```
成功创建 VPA 组件后，您可在 kube-system 命名空间中查阅三个 Deployment，分别为 vpa-admission-controller、vpa-recommender、vpa-updater。如下图所示：
![](https://main.qcloudimg.com/raw/fb4cdfb049c81f5ca3c0e535acbf0d75.png)




### 示例1：使用 VPA 获取 Request 推荐值

>? 
- 不建议在生产环境中使用 VPA 自动更新 Request。
- 您可以利用 VPA 查看 Request 推荐值，在合适条件下手动触发更新。



在本示例中，您将创建 `updateMode` 为 `Off` 的 VPA 对象，并创建具有两个 Pod 的 Deployment，每个 Pod 各有一个容器。在创建 Pod 后，VPA 会分析容器的 CPU 和内存需求，并在 `status` 字段中记录 Request 推荐值。VPA 不会自动更新正在运行的容器的资源请求。

在终端中执行以下命令，生成一个名为 `tke-vpa` 的 VPA 对象，指向一个名为 `tke-deployment` 的 Deployment：

```shell
cat <<EOF | kubectl apply -f -
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
    name: tke-vpa
spec:
    targetRef:
      apiVersion: "apps/v1"
      kind: Deployment
      name: tke-deployment
    updatePolicy:
      updateMode: "Off"
EOF
```

执行以下命令，生成一个名为 `tke-deployment` 的 Deployment 对象：

```shell
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
    name: tke-deployment
spec:
    replicas: 2
    selector:
      matchLabels:
        app: tke-deployment
    template:
      metadata:
        labels:
          app: tke-deployment
      spec:
        containers:
        - name: tke-container
          image: nginx
EOF
```

生成的 Deployment 对象如下图所示：
![](https://main.qcloudimg.com/raw/556334a46666d4f74c18432ed6083c55.png)

>! 上述操作创建 `tke-deployment` 时并没有设置 CPU 或内存的 Request，Pod 中的 [Qos](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/) 为 BestEffort，此时 Pod 容易被驱逐。建议您在创建业务的 Deployment 时设置 Request 及 Limit。如果您通过容器服务控制台创建工作负载，控制台将自动为每个容器的 Request 和 Limits 设置默认值。
![](https://main.qcloudimg.com/raw/3adff8df7f72b5bdc65734e5d3c7ba98.png)
>


执行以下命令，您可以查看 VPA 推荐的 CPU 和内存 Request：
```shell
kubectl get vpa tke-vpa -o yaml
```

执行结果如下所示：
```yaml
...
recommendation:
      containerRecommendations:
      - containerName: tke-container
        lowerBound:
          cpu: 25m
          memory: 262144k
        target:	# 推荐值
          cpu: 25m
          memory: 262144k
        uncappedTarget:
          cpu: 25m
          memory: 262144k
        upperBound:
          cpu: 1771m
          memory: 1851500k
```

其中 `target` 对应的 CPU 和内存为推荐 Request。您可以选择删除之前的 Deployment，并使用推荐的 Request 值创建新的 Deployment。

| 字段 | 释义 | 
|---------|---------|
|  **lowerBound** | 推荐的最小值。使用小于该值的 Request 可能会对性能或可用性产生重大影响。 | 
| **target** | 推荐值。由 VPA 计算出最合适的 Request。 | 
| **uncappedTarget** | 最新建议值。仅基于实际资源使用情况，不考虑  `.spec.resourcePolicy.containerPolicies` 中设置的容器可以被推荐的数值范围。uncappedTarget 可能与推荐上下界限不同。该字段仅用作状态指示，不会影响实际的资源分配。 | 
| **upperBound** |推荐的最大值。使用高于该值的 Request 可能造成浪费。 | 



### 示例2：停用特定容器

如果您的 Pod 中有多个容器，例如一个是真正的业务容器，另一个是辅助容器。为了节省集群资源，您可以选择停止为辅助容器推荐 Request。

在示例中，您将创建一个停用了特定容器的 VPA，并创建一个 Deployment。Deployment 中包含一个 Pod，该 Pod 内包含两个容器。在创建 Pod 后，VPA 仅为一个容器创建并计算推荐值，另外一个容器被停用 VPA 的推荐能力。

在终端中执行以下命令，生成一个名为 `tke-opt-vpa` 的 VPA 对象，指向一个名为 `tke-opt-deployment` 的 Deployment：

```shell
cat <<EOF | kubectl apply -f -
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
    name: tke-opt-vpa
spec:
    targetRef:
      apiVersion: "apps/v1"
      kind: Deployment
      name: tke-opt-deployment
    updatePolicy:
      updateMode: "Off"
    resourcePolicy:
      containerPolicies:
      - containerName: tke-opt-sidecar
        mode: "Off"
EOF
```

>! 该 VPA 的 `.spec.resourcePolicy.containerPolicies` 中，指定了 `tke-opt-sidecar` 的 `mode` 为 “Off”，VPA 将不会为 `tke-opt-sidecar` 计算和推荐新的 Request。


执行以下命令，生成一个名为 `tke-deployment` 的 Deployment 对象：
```sh
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
    name: tke-opt-deployment
spec:
    replicas: 1
    selector:
      matchLabels:
        app: tke-opt-deployment
    template:
      metadata:
        labels:
          app: tke-opt-deployment
      spec:
        containers:
        - name: tke-opt-container
          image: nginx
        - name: tke-opt-sidecar
          image: busybox
          command: ["sh","-c","while true; do echo TKE VPA; sleep 60; done"]
EOF
```

生成的 Deployment 对象如下图所示：
![](https://main.qcloudimg.com/raw/54c88b647bfe17489cf8cea1cc1ca95e.png)


执行以下命令，您可以查看 VPA 推荐的 CPU 和内存 Request：
```shell
kubectl get vpa tke-opt-vpa -o yaml
```

执行结果如下所示：

```yaml
...
    recommendation:
      containerRecommendations:
      - containerName: tke-opt-container
        lowerBound:
          cpu: 25m
          memory: 262144k
        target:
          cpu: 25m
          memory: 262144k
        uncappedTarget:
          cpu: 25m
          memory: 262144k
        upperBound:
          cpu: 1595m
          memory: 1667500k
```

在执行结果中，仅有 `tke-opt-container` 的推荐值，没有 `tke-opt-sidecar` 的推荐值。

### 示例3：自动更新 Request

>! 自动更新正在运行的 Pod 资源是 VPA 的一项实验功能，建议不要在生产环境中使用该功能。


在本示例中，您将创建一个自动调整 CPU 和内存请求的 VPA，并创建具有两个 Pod 的 Deployment。每个 Pod 都会设置资源的 Request 和 Limits。


在终端中执行以下命令，生成一个名为 `tke-auto-vpa` 的 VPA 对象，指向一个名为 `tke-auto-deployment` 的 Deployment：
```yaml
cat <<EOF | kubectl apply -f - 
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
    name: tke-auto-vpa
spec:
    targetRef:
      apiVersion: "apps/v1"
      kind: Deployment
      name: tke-auto-deployment
    updatePolicy:
      updateMode: "Auto"
EOF
```

>! 该 VPA 的 `updateMode` 字段的值为 `Auto`，表示 VPA 可以在 Pod 的生命周期内更新 CPU 和内存请求。VPA 可以删除 Pod，调整 CPU 和内存请求，然后启动一个新 Pod。


执行以下命令，生成一个名为 `tke-auto-deployment` 的 Deployment 对象：
```shell
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
    name: tke-auto-deployment
spec:
    replicas: 2
    selector:
      matchLabels:
        app: tke-auto-deployment
    template:
      metadata:
        labels:
          app: tke-auto-deployment
      spec:
        containers:
        - name: tke-container
          image: nginx
          resources:
            requests:
              cpu: 100m
              memory: 100Mi
            limits:
              cpu: 200m
              memory: 200Mi
EOF
```


>! 上述操作创建 Deployment 时设置了资源的 Request 和 Limits，VPA 此时不仅会推荐 Request 值，还会按照 Request 和 Limits 的初始比例自动推荐 Limits 值。例如，YAML 中 CPU 的 Request 和 Limits 的初始比例为 100m:200m = 1:2，那么 VPA 推荐的 Limits 数值则是 VPA 对象中推荐的 Request 数值的两倍。



生成的 Deployment 对象如下图所示：
![](https://main.qcloudimg.com/raw/10b6c1a69ea1a3270bd3b9b286a561b3.png)



执行以下命令，获取正在运行中的 Pod 的详细信息：

```sh
kubectl get pod pod-name -o yaml
```

执行结果如下所示。VPA 修改了原来设置的 Request 和 Limits，更新为 VPA 的推荐值，并维持了初始的 Request 和 Limits 比例。同时生成一个记录更新的 Annotation：

```yaml
apiVersion: v1
kind: Pod
metadata:
    annotations:
      ...
      vpaObservedContainers: tke-container
      vpaUpdates: Pod resources updated by tke-auto-vpa: container 0: memory request, cpu request
...
spec:
    containers:
    ...
      resources:
        limits:		# 新的 Request 和 Limits 会维持初始设置的比例
          cpu: 50m	
          memory: 500Mi
        requests:
          cpu: 25m
          memory: 262144k
      ...
```

执行以下命令，获取相关 VPA 的详细信息：

```sh
kubectl get vpa tke-auto-vpa -o yaml
```

执行结果如下所示：

```yaml
...
    recommendation:
      containerRecommendations:
      - containerName: tke-container
        Lower Bound:
          Cpu:     25m
          Memory:  262144k
        Target:
          Cpu:     25m
          Memory:  262144k
        Uncapped Target:
          Cpu:     25m
          Memory:  262144k
        Upper Bound:
          Cpu:     101m
          Memory:  262144k
```

其中 `target` 表示容器请求 25m CPU 和 262144k 的内存时将以最佳状态运行。

VPA 使用 `lowerBound` 和 `upperBound` 推荐值来决定是否驱逐 Pod 并将其替换为新 Pod。如果 Pod 的请求小于下限或大于上限，则 VPA 将删除 Pod 并将其替换为具有目标推荐值的 Pod。

## 故障处理

### 1. 执行 `vpa-up.sh` 脚本时报错

#### 报错信息
```shell
ERROR: Failed to create CA certificate for self-signing. If the error is "unknown option -addext", update your openssl version or deploy VPA from the vpa-release-0.8 branch.
```

#### 解决方案
1. 如果您没有通过集群中的云服务器执行命令，建议您在云服务器中下载 Autoscaler 项目，并执行完整的 [部署 VPA](#VPA) 操作。如需为您的云服务器连接集群，详情可参见 [连接集群](https://cloud.tencent.com/document/product/457/32191)。
2. 如出现继续报错的情况，请检查是否存在以下问题：
 - 检查集群 CVM 的 `openssl` 版本是否大于 1.1.1。
 - 是否使用 Autoscaler 项目的 `vpa-release-0.8` 分支。

### 2. VPA 相关负载无法启动

#### 报错信息
如果您的 VPA 相关负载无法启动，并产生如下图所示信息：
![](https://main.qcloudimg.com/raw/026ae791429cb584fa1c61af3ac8340f.png)
**信息1**：表示负载中的 Pod 没有成功运行。
**信息2**：表示镜像的地址。


#### 解决方案
VPA 相关负载无法启动的原因是位于 GCR 的镜像无法被下载，为解决问题您可尝试以下步骤：
1. **下载镜像**。
    访问 “k8s.gcr.io/” 镜像仓库，下载 vpa-admission-controller、vpa-recommender、vpa-updater 的镜像。
2. **更换标签及推送**。
    将 vpa-admission-controller、vpa-recommender、vpa-updater 的镜像更换标签后推送到您的镜像仓库中。上传镜像操作详情可参见 [容器镜像服务个人版快速入门](https://cloud.tencent.com/document/product/1141/50332)。
3. **更改 YAML 镜像地址**。
    在 YAML 文件中将 vpa-admission-controller、vpa-recommender、vpa-updater 的镜像地址更新为您设定的新地址。

