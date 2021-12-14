

## 固定 IP 的保留和回收

固定 IP 模式下，创建使用 VPC-CNI 模式的 Pod 以后，网络组件会为该 Pod 在同 namespace 下创建同名的 CRD 对象 `VpcIPClaim`。该对象描述 Pod 对 IP 的需求。网络组件随后会根据这个对象创建 CRD 对象 `VpcIP`，并关联对应的 `VpcIPClaim`。`VpcIP` 以实际的 IP 地址为名，表示实际的 IP 地址占用。

您可以通过以下命令查看集群使用的容器子网内 IP 的使用情况：

```
kubectl get vip
```

对于非固定 IP 的 Pod，其 Pod 销毁后 `VpcIPClaim` 也会被销毁，`VpcIP` 随之销毁回收。而对于固定 IP 的 Pod，其 Pod 销毁后 `VpcIPClaim` 仍然保留，`VpcIP` 也因此保留。同名的 Pod 启动后会使用同名的 `VpcIPClaim` 关联的 `VpcIP`，从而实现 IP 地址保留。

由于网络组件在集群范围内分配 IP 时会依据 `VpcIP` 信息找寻可用 IP，因此固定 IP 的地址若不使用需要及时回收（目前默认策略是永不回收），否则会导致 IP 浪费而无 IP 可用。本文介绍过期回收、手动回收及级联回收的 IP 回收方法。

### 过期回收（默认支持）
在 [创建集群](https://cloud.tencent.com/document/product/457/32189) 页面，容器网络插件选择**VPC-CNI**模式并且勾选**开启支持**固定Pod IP 支持，如下图所示：
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


## 相关问题

### 节点不能分配到弹性网卡，无法正常调度 Pod（共享网卡模式）

当节点加入到集群后，ipamd 会尝试从和节点相同可用区的子网（配置给 ipamd 的子网）中为节点绑定一个弹性网卡，如果 ipamd 异常或者没有给 ipamd 配置和节点相同可用区的子网，ipamd 将无法给节点分配辅助网卡。此外，如果当前 VPC 使用的辅助网卡数目超过上限，则无法给节点分配辅助网卡。
执行以下命令，确认问题原因：
```shell
kubectl get event
```

- event 中显示 ENILimit，则是配额问题，可以通过为 VPC 调大弹性网卡数目配额来解决问题。
- event 中显示下图信息则说明子网中的 IP 不足。
![](https://main.qcloudimg.com/raw/1dc81abb2404b4add1941609b1214944.png)
可以通过执行以下命令获取当前子网 IP 使用数目。
```shell
kubectl get vip | wc -l
```

若已确认子网 IP 充足，但仍存在问题，则可能与底层的软限制有关。分析如下：
以高配机型（每个节点关联的弹性网卡可以额外分配29个 IP）和配置的子网是 `/23` 为例，当集群有17个节点时，这些节点上理论能使用的 IP 资源为 17 *（29 + 1），即已经超过500了，可把 `/23` 的子网填满，此时 ipamd 会限制新的节点不再分配弹性网卡。为解决这个问题，可再添加一些子网，弹性网卡可以从新子网中创建并绑定到新添加的节点上，新的节点虽然能够加入集群，但是 Pod 不会调度到没有绑定弹性网卡的节点。
如果不加限制，节点越加越多会导致能分给 Pod 的 IP 越来越少，因为弹性网卡本身会占用一个主 IP，这个主 IP 不能用于 Pod，所以添加一个节点，实际上子网可以分给 Pod 的 IP 会少一个。在极端情况下，存在分配给节点的辅助网卡都集中在一个子网中的情况，会限制整个集群中 Pod 的规模，并且只能通过驱逐旧的节点，添加子网后，再将节点加入集群才能恢复。


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

若命令返回成功则报错 VIP 状态为 Attaching，报错信息如下图所示：
![](https://main.qcloudimg.com/raw/d7df85621d613f30e5109395de4c92bb.png)

#### 解决方案
目前腾讯云弹性网卡限制一个 VPC 下面最多绑定50个弹性网卡。您可 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 申请提高配额，配额按地域生效。

