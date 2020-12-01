

## 使用场景

适用于依赖容器固定 IP 的场景。例如，传统架构迁移到容器平台及针对 IP 做安全策略限制。 对 IP 无限制的业务不推荐您使用固定 IP 模式。

## 能力和限制

- 支持 Pod 销毁 IP 保留，Pod 迁移 IP 不变，从而实现固定 IP。
- 支持多子网，但不支持跨子网调度固定 IP 的 Pod， 因此固定 IP 模式的 Pod 不支持跨可用区调度。
- 支持 Pod IP 自动关联弹性公网 IP，从而可支持 Pod 外访。
- 共享网卡的固定 IP 模式，固定 IP 的 Pod 销毁后，其 IP 只在集群范围内保留。若有其他集群或者业务（如 CVM、CDB、CLB 等）使用了同一子网，可能会导致保留的固定 IP 被占用，Pod 再启动的时候会拿不到 IP。**因此请保证该模式的容器子网是独占使用。**

## 使用方法

您可以通过以下两种方式使用固定 IP：
- 创建集群选择固定 IP 模式的 VPC-CNI。
- 为 GlobalRouter 模式附加固定 IP VPC-CNI 模式。

### 创建固定 Pod IP 类型 StatefulSet<span id=""></span>

如果您存在业务需要在容器服务 TKE 中部署，并存在固定 Pod IP 的需求， 您可以使用固定 IP 类型的 StatefulSet。容器服务 TKE 提供扩展 StatefulSet 固定 IP 的能力，该类型的 StatefulSet 创建的 Pod 将通过弹性网卡分配真实的 VPC 内的 IP 地址。容器服务 TKE VPC-CNI 的插件负责 IP 分配，当 Pod 重启或迁移，可实现 IP 地址不变。

您可以通过创建固定 IP 类型 StatefulSet 来满足以下场景：
- 通过来源 IP 授权。
- 基于 IP 做流程审核。
- 基于 Pod IP 做日志查询等。

## 操作步骤

### 通过控制台使用固定 IP 模式

1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，单击左侧导航栏中【集群】。
2. 选择需要使用固定 IP 模式的集群 ID 名称，进入该集群的管理页面。
3. 选择【工作负载】>【StatefulSet】，进入【StatefulSet】的集群管理页面。
4. 单击【新建】，查看【实例数量】。如下图所示：
   ![](https://main.qcloudimg.com/raw/2dbd219d6bd76b8fe90971390daacc3c.png)
5. 单击【显示高级设置】，根据您实际需求，设置【StatefulSet】参数。关键参数信息如下：
   ![创建StatefulSet](https://main.qcloudimg.com/raw/2a5bf4e7b3e5c85c62fef2b7b09e02f3.png)
 - 网络模式：勾选【使用 VPC-CNI 模式】。
    - IP 地址范围：目前仅支持随机。
    - 固定 Pod IP：选择【开启】。

### 通过 Yaml 使用固定 IP 模式
以下代码为 Yaml 示例：

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    k8s-app: busybox
  name: busybox
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      k8s-app: busybox
      qcloud-app: busybox
  serviceName: ""
  template:
    metadata:
      annotations:
        tke.cloud.tencent.com/networks: "tke-route-eni"
        tke.cloud.tencent.com/vpc-ip-claim-delete-policy: Never
      creationTimestamp: null
      labels:
        k8s-app: busybox
        qcloud-app: busybox
    spec:
      containers:
      - args:
        - "10000000000"
        command:
        - sleep
        image: busybox
        imagePullPolicy: Always
        name: busybox
        resources:
          limits:
            tke.cloud.tencent.com/eni-ip: "1"
          requests:
            tke.cloud.tencent.com/eni-ip: "1" 
```
>? spec.template.annotations：`tke.cloud.tencent.com/networks: "tke-route-eni"` 表明 Pod 使用共享网卡的 VPC-CNI 模式，如果使用的是独立网卡的 VPC-CNI 模式，请将值修改成 `"tke-direct-eni"`。
>
- **spec.template.annotations**：创建 VPC-CNI 模式的 Pod，您需要设置 annotations，即 `tke.cloud.tencent.com/vpc-ip-claim-delete-policy`，默认是 “Immediate”，Pod 销毁后，关联的 IP 同时被销毁，如需固定 IP，则需设置成 “Never”，Pod 销毁后 IP 也将会保留，那么下一次同名的 Pod 拉起后，会使用之前的 IP。
- **spec.template.spec.containers.0.resources**：创建共享网卡的 VPC-CNI 模式的 Pod，您需要添加 requests 和 limits 限制，即`tke.cloud.tencent.com/eni-ip`。如果是独立网卡的 VPC-CNI 模式，则添加 `tke.cloud.tencent.com/direct-eni`。

### 固定 IP 的保留和回收

固定 IP 模式下，使用 VPC-CNI 模式的 Pod 创建以后，网络组件会为该 Pod 在同一个 namespace 下创建同名的 CRD 对象 `VpcIPClaim`。该对象描述 Pod 对 IP 的需求。网络组件随后会根据这个对象创建 CRD 对象 `VpcIP`，并关联对应的 `VpcIPClaim`。`VpcIP` 以实际的 IP 地址为名，表示实际的 IP 地址占用。
用户可以通过以下命令查看集群使用的容器子网内 IP 的使用情况：

```
kubectl get vip
```

对于非固定 IP 的 Pod，其 Pod 销毁后 `VpcIPClaim` 也会被销毁，`VpcIP` 随之销毁回收。而对于固定 IP 的 Pod，其 Pod 销毁后 `VpcIPClaim` 仍然保留，`VpcIP` 也因此保留。同名的 Pod 启动后会使用同名的 `VpcIPClaim` 关联的 `VpcIP`，从而实现 IP 地址保留。

由于网络组件在集群范围内分配 IP 时会依据 `VpcIP` 信息找寻可用 IP，因此固定 IP 的地址若不使用需要及时回收（目前默认策略是永不回收），否则会导致 IP 浪费而无 IP 可用。以下是几种 IP 回收方法。

### 过期回收（默认支持）

在 [创建集群](https://cloud.tencent.com/document/product/457/32189) 页面，容器网络插件选择【VPC-CNI】模式并且勾选【开启支持】固定Pod IP 支持，如下图所示：
![](https://main.qcloudimg.com/raw/ad1290436fa0ff66d8bb17abd2bab161.png)
在高级设置中设置 IP 回收策略，可以设置 Pod 销毁后多少秒回收保留的固定 IP。如下图所示：
![](https://main.qcloudimg.com/raw/a9adcfc9618452c4afd45dfdd27c050f.png)

### 手动回收

对于急需回收的 IP 地址，需要先确定需回收的 IP 被哪个 Pod 占用，找到对应的 Pod 的名称空间和名称，执行以下命令通过手动回收：
>! 需保证回收的 IP 对应的 Pod 已经销毁，否则会导致该 Pod 网络不可用。
>
```
kubectl delete vipc <podname> -n <namespace>
```


### 级联回收

目前的固定 IP 与 Pod 强绑定，而与具体的 Workload 无关（例如 deployment、statefulset 等）。Pod 销毁后，固定 IP 不确定何时回收。TKE 现已实现删除 Pod 所属的 Workload 后即刻删除固定 IP。

以下步骤介绍如何开启级联回收：
1. 修改现存的 **tke-eni-ipamd deployment：`kubectl edit deploy tke-eni-ipamd -n kube-system`**。
2. 执行以下命令，在 `spec.template.spec.containers[0].args` 中加入启动参数：
```yaml
        - --enable-ownerref
```

修改后，ipamd 会自动重启并生效。生效后，增量 Workload 可实现级联删除固定 IP，存量 Workload 暂不能支持。

## 相关特性

### 共享网卡模式的 Pod IP 自动关联弹性公网 IP（EIP）

目前共享网卡的固定 IP 模式默认支持 Pod IP 自动关联 EIP。
如需关联 EIP，可参考以下 Yaml 示例：
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    k8s-app: busybox
  name: busybox
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      k8s-app: busybox
      qcloud-app: busybox
  serviceName: ""
  template:
    metadata:
      annotations:
        tke.cloud.tencent.com/networks: "tke-route-eni"
        tke.cloud.tencent.com/vpc-ip-claim-delete-policy: Never
        tke.cloud.tencent.com/eip-attributes: ""
        tke.cloud.tencent.com/eip-claim-delete-policy: "Never"
      creationTimestamp: null
      labels:
        k8s-app: busybox
        qcloud-app: busybox
    spec:
      containers:
      - args:
        - "10000000000"
        command:
        - sleep
        image: busybox
        imagePullPolicy: Always
        name: busybox
        resources:
          limits:
            tke.cloud.tencent.com/eni-ip: "1"
            tke.cloud.tencent.com/eip: "1"
          requests:
            tke.cloud.tencent.com/eni-ip: "1"
            tke.cloud.tencent.com/eip: "1"
```

- **spec.template.annotations：tke.cloud.tencent.com/eip-attributes: ""** 表明该 Workload 的 Pod 需要关联 EIP。
- **spec.template.annotations：tke.cloud.tencent.com/eip-claim-delete-policy: "Never"** 表明 Workload 的 Pod 的 EIP 也需要固定，Pod 销毁后不能变更。若不需要固定，则不添加该注解。
- **spec.template.spec.containers.0.resources**：关联 EIP 的 Pod，您需要添加 requests 和 limits 限制，即 `tke.cloud.tencent.com/eip`，从而让调度器保证 Pod 调度到的节点仍有 EIP 资源可使用。

## 使用限制
各节点可绑定的 EIP 资源受到相关配额限制和云服务器的绑定数量限制，详情可参考 [EIP使用限制](https://cloud.tencent.com/document/product/1199/41648#eip-.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6)。
各节点可绑定的最大 EIP 数量为**云服务器绑定数量 - 1**。


## 常见问题

### 节点不能分配到弹性网卡，无法正常调度 Pod（共享网卡模式）

当节点加入到集群后，ipamd 会尝试从和节点相同可用区的子网（配置给 ipamd 的子网）中为节点绑定一个弹性网卡，如果 ipamd 异常或者没有给 ipamd 配置和节点相同可用区的子网，ipamd 将无法给节点分配辅助网卡。此外，如果当前 vpc 使用的辅助网卡数目超过上限，则无法给节点分配辅助网卡，可以通过以下命令确认问题：
```shell
kubectl get event
```

如果 event 中显示 ENILimit，则是配额问题，可以通过为 VPC 调大弹性网卡数目配额来解决问题。
如果 event 中显示下图信息则说明子网中的 IP 不够用了，
![](https://main.qcloudimg.com/raw/1dc81abb2404b4add1941609b1214944.png)
可以通过执行以下命令获取当前子网 IP 使用数目。
```shell
kubectl get vip | wc -l
```

如果已明确子网中使用的 IP 还未达到子网的理论上限，但问题依然存在，可能和底层做的软限制有关。原因如下：
以高配机型（每个节点关联的弹性网卡可以额外分配29个 IP）和配置的子网是 `/23` 为例，当集群有17个节点时，这些节点上理论能使用的 IP 资源为 17 *（29 + 1），即已经超过500了，可把 `/23` 的子网填满，此时 ipamd 会限制新的节点不再分配弹性网卡。为解决这个问题，可再添加一些子网，弹性网卡可以从新子网中创建并绑定到新添加的节点上，新的节点虽然能够加入集群，但是 Pod 不会调度到没有绑定弹性网卡的节点。
如果不加限制，节点越加越多会导致能分给 Pod 的 IP越来越少，因为弹性网卡本身会占用一个主 IP，这个主 IP 不能用于 Pod，所以添加一个节点，实际上子网可以分给 Pod 的 IP 会少一个，并且在极端情况下，可能分配给节点的辅助网卡都集中在一个子网中，会限制整个集群中 Pod 的规模，并且只能通过驱逐旧的节点，添加子网后，再将节点加入集群才能恢复.


### 节点不能分配到弹性网卡，提示弹性网卡数量超出限制
#### 现象
节点配置的弹性网卡无法绑定，nec 关联的 vip attach 失败。查看 nec 则看到节点关联的 nec status 为空。
执行以下代码可查看 nec：
```shell
kubectl get nec -o yaml
```

当节点关联的 nec status 为空时返回结果如下图所示：
![](https://main.qcloudimg.com/raw/8af59f6b986e844e7aa6dd776f9a0bc0.png)

执行以下代码查看 nec 关联的 VIP：
```shell
kubectl get vip -oyaml
```

若命令返回成功则可看到报错 VIP 状态为 Attaching，报错信息如下图所示：
![](https://main.qcloudimg.com/raw/d7df85621d613f30e5109395de4c92bb.png)

#### 解决方案
目前腾讯云弹性网卡限制一个 VPC 下面最多绑定50个弹性网卡。您可 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请提高配额，配额按地域生效。

