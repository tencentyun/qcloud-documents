本文档介绍可能导致 Pod 一直处于 Pending 状态的几种情形，以及如何通过排查步骤定位异常原因。请按照以下步骤依次进行排查，定位问题后恢复正确配置即可。


## 现象描述
当 Pod 一直处于 Pending 状态时，说明该 Pod 还未被调度到某个节点上，需查看 Pod 分析问题原因。例如执行 `kubectl describe pod <pod-name>` 命令，则获取到的事件信息如下：
``` bash
$ kubectl describe pod tikv-0
...
Events:
  Type     Reason            Age                 From               Message
  ----     ------            ----                ----               -------
  Warning  FailedScheduling  3m (x106 over 33m)  default-scheduler  0/4 nodes are available: 1 node(s) had no available volume zone, 2 Insufficient cpu, 3 Insufficient memory.
```

## 可能原因
- 节点资源不足
- 不满足 nodeSelector 与 affinity
- Node 存在 Pod 没有容忍的污点
- 低版本 kube-scheduler 的 bug
- kube-scheduler 未正常运行
- 驱逐后其他可用节点与当前节点的有状态应用不在相同可用区

## 排查方法
### 检查节点是否资源不足
#### 问题分析
节点资源不足有以下几种情况：
* CPU 负载过高。
* 剩余可以被分配的内存不足。
* 剩余可用 GPU 数量不足（通常在机器学习场景、GPU 集群环境）。

为进一步判断某个 Node 资源是否足够，可执行以下命令获取资源分配信息：
```
kubectl describe node <node-name>
```
在返回信息中，请注意关注以下内容：
* `Allocatable`：表示此节点能够申请的资源总和。
* `Allocated resources`：表示此节点已分配的资源（Allocatable 减去节点上所有 Pod 总的 Request）。

#### 造成影响
前者与后者相减，即可得出剩余可申请的资源大小。如果该值小于 Pod 的 Request，则不满足 Pod 的资源要求，Scheduler 在 Predicates（预选）阶段就会剔除掉该 Node，不会调度 Pod 到该 Node。


### 检查 nodeSelector 及 affinity 的配置

假设 Pod 中 nodeSelector 指定了节点 Label，则调度器将只考虑调度 Pod 到包含该 Label 的 Node 上。当不存在符合该条件的 Node 时，Pod 将无法被调度。更多相关信息可前往 [Kubernetes 官方网站](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) 进行查看。

此外，如果 Pod 配置了 affinity（亲和性），则调度器根据调度算法可能无法发现符合条件的 Node，从而无法调度。affinity 包括以下几类：

* `nodeAffinity`：节点亲和性，可以看作增强版的 nodeSelector，用于限制 Pod 只允许被调度到某一部分符合条件的 Node。
* `podAffinity`：Pod 亲和性，用于将一系列有关联的 Pod 调度到同一个地方，即同一个节点或同一个可用区的节点等。
* `podAntiAffinity`：Pod 反亲和性，防止某一类 Pod 调度到同一个地方，可以有效避免单点故障。例如，将集群 DNS 服务的 Pod 副本分别调度到不同节点，可避免因一个节点出现故障而造成整个集群 DNS 解析失败，甚至使业务中断。

### 检查 Node 是否存在 Pod 没有容忍的污点
#### 问题分析
假如节点上存在污点（Taints），而 Pod 上没有相应的容忍（Tolerations），Pod 将不会调度到该 Node。在调度之前，可以先通过 `kubectl describe node <node-name>` 命令查看 Node 已设置污点。示例如下：
``` bash
$ kubectl describe nodes host1
...
Taints:             special=true:NoSchedule
...
```
Node 上已设置的污点可通过手动或自动的方式添加，详情请参见 [添加污点](#addTaints)。

#### 解决方法

本文提供以下两种方法，通常选择方法2解决该问题：
- 方法1：删除污点
执行以下命令，删除污点 `special`。
```
kubectl taint nodes host1 special-
```
- 方法2：在 Pod 上增加污点容忍
  >?本文以向 Deployment 中已创建的 Pod（名称为 `nginx`）添加容忍为例。
  >
  1. 参考 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，登录 `nginx` 所在的云服务器。 
  4. 执行以下命令，编辑 Yaml。
  ```
	kubectl edit deployment nginx
	```
  4. 在 Yaml 文件 `template` 中的 `spec` 处添加容忍。例如，增加已存在 `special` 污点所对应的容忍：
```yaml
	tolerations:
	- key: "special"
	  operator: "Equal"
	  value: "true"
	  effect: "NoSchedule"
```
添加完成后如下图所示：
![](https://main.qcloudimg.com/raw/2cee1098136df94cdc64039792da17d7.png)
  5. 保存并退出编辑即可成功创建容忍。

### 检查是否存在低版本 kube-scheduler 的 bug

Pod 一直处于 Pending 状态可能是低版本 `kube-scheduler` 的 bug 导致的，该情况可以通过升级调度器版本进行解决。

### 检查 kube-scheduler 是否正常运行
请注意时检查 Master 上的 `kube-scheduler` 是否运行正常，如异常可尝试重启临时恢复。

### 检查驱逐后其他可用节点与当前节点的有状态应用是否不在相同可用区

服务部署成功且正在运行时，若此时节点突发故障，就会触发 Pod 驱逐，并创建新的 Pod 副本调度到其他节点上。对于已挂载了磁盘的 Pod，通常需要被调度到与当前故障节点和挂载磁盘所处同一个可用区的新的节点上。若集群中同一个可用区内不具备满足可调度条件的节点时，即使其他可用区内具有满足条件的节点，此类 Pod 仍不会调度。


限制已挂载磁盘的 Pod 不能调度到其他可用区的节点的原因如下：
云上磁盘允许被动态挂载到同一个数据中心上的不同机器，为了有效避免网络时延极大地降低 IO 速率，通常不允许跨数据中心挂载磁盘设备。


## 相关操作
### 添加污点[](id:addTaints)
#### 手动添加污点
通过以下或类似方式，可以手动为节点添加指定污点：
``` bash
$ kubectl taint node host1 special=true:NoSchedule
node "host1" tainted
```
>?在某些场景下，可能期望新加入的节点在调整好某些配置之前默认不允许调度 Pod。此时，可以给该新节点添加 `node.kubernetes.io/unschedulable` 污点。

#### 自动添加污点
从 v1.12 开始，Beta 默认开启 `TaintNodesByCondition` 特性，controller manager 将会检查 Node 的 Condition。Node 运行状态异常时，当检查的 Condition 符合如下条件（即符合 Condition 与 Taints 的对应关系），将自动给 Node 加上相应的污点。
例如，检查 Condition 为 `OutOfDisk` 且 Value 为 `True`，则 Node 会自动添加 `node.kubernetes.io/out-of-disk` 污点。
Condition 与污点的对应关系如下：
```
Conditon               Value       Taints
 --------               -----       ------
OutOfDisk              True        node.kubernetes.io/out-of-disk
Ready                  False       node.kubernetes.io/not-ready
Ready                  Unknown     node.kubernetes.io/unreachable
MemoryPressure         True        node.kubernetes.io/memory-pressure
PIDPressure            True        node.kubernetes.io/pid-pressure
DiskPressure           True        node.kubernetes.io/disk-pressure
NetworkUnavailable     True        node.kubernetes.io/network-unavailable
```
当每种 Condition 取特定的值时，将表示以下含义：
* `OutOfDisk` 为 True，表示节点磁盘空间不足。
* `Ready` 为 False，表示节点不健康。
* `Ready `为 Unknown，表示节点失联。在 `node-monitor-grace-period` 所确定的时间周期内（默认40s）若节点没有上报状态，controller-manager 就会将 Node 状态置为 Unknown。
* `MemoryPressure` 为 True，表示节点内存压力大，实际可用内存很少。
* `PIDPressure` 为 True，表示节点上运行了太多进程，PID 数量不足。
* `DiskPressure` 为 True，表示节点上的磁盘可用空间不足。
* `NetworkUnavailable` 为 True，表示节点上的网络没有正确配置，无法跟其他 Pod 正常通信。
>?上述情况一般属于被动添加污点，但在容器服务中，存在一个主动添加/移出污点的过程：
>在新增节点时，首先为该节点添加 `node.cloudprovider.kubernetes.io/uninitialized` 污点，待节点初始化成功后再自动移除此污点，以避免 Pod 被调度到未初始化好的节点。
