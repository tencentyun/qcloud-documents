## 操作场景

本文档指导您对集群进行扩缩容。TKE 容器集群支持以下扩缩容方法：
- [手动添加/移除节点](#ManuallyAddAndRemove)
- [通过弹性伸缩自动添加/移除节点](#AutomaticAddAndRemove)

## 前提条件

已登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。

## 操作步骤

<span id="ManuallyAddAndRemove"></span>
### 手动添加/移除节点

#### 新建节点

具体操作请参考 [新建节点](https://cloud.tencent.com/document/product/457/32203#createNode)。
创建过程中，您可以在 “云主机配置” 页面，配置云服务器，并对集群进行扩缩容。

#### 添加已有节点

>?
> - 当前仅支持添加同一 VPC 下的云服务器。
> - 添加已有节点到集群，将重装改云服务器的操作系统。
> - 添加已有节点到集群，将迁移服务器所属项目到集群所设置的项目。
> - 有且仅有一块数据盘的节点加入到集群，可以选择是否设置容器目录，设置容器目录会格式化数据盘。无数据盘或多块数据盘的云服务器设置容器目录不生效。

具体操作请参考 [添加已有节点](https://cloud.tencent.com/document/product/457/32203#addExistingNode)。
添加过程中，您可以在 “云主机配置” 页面，配置需要添加到集群的云服务器，并对集群进行扩缩容。

#### 移除节点

具体操作请参考 [移除节点](https://cloud.tencent.com/document/product/457/32204)。

<span id="AutomaticAddAndRemove"></span>
### 通过弹性伸缩自动添加/移除节点

集群自动扩缩容，又称 Cluster Autoscaler（CA），是一个独立的程序。它可以动态地调整集群的节点数量来满足需求。当集群中出现因资源不足而无法调度的 Pod 时，自动触发扩容，为您减少人力成本。当满足节点空闲等缩容条件时，自动触发缩容，为您节约资源成本。

#### 开启集群自动伸缩

##### 创建单个伸缩组
1. 参考 [创建集群](https://cloud.tencent.com/document/product/457/32189) 的 [步骤1](https://cloud.tencent.com/document/product/457/32189#step1) - [步骤7](https://cloud.tencent.com/document/product/457/32189#step7)，创建集群。
2. 在 “云主机配置” 中，配置云服务器的其他配置，并勾选 “自动调节” 的 “开启”。如下图所示：
![自动调节](https://main.qcloudimg.com/raw/77104e22ff19a1e62cb090f12631118c.png)
3. 单击【下一步】。
4. 单击【完成】，完成创建可自动伸缩的集群。

##### 创建多个伸缩组

1. <span id="step1">在左侧导航栏中，单击【[集群](https://console.cloud.tencent.com/tke2/cluster?rid=4)】，进入 “集群管理” 页面。</span>
2. 单击需要创建多个伸缩组的集群 ID/名称，进入该集群的管理页面。如下图所示：
![管理页面](https://main.qcloudimg.com/raw/a81fa565be60dbddafe55010319a4e08.png)
3. 在左侧导航栏中，选择 “节点管理” > “伸缩组”，进入“伸缩组列表” 页面。
4. 单击【新建伸缩组】，弹出 “新建伸缩组” 窗口。如下图所示：
![新建伸缩组](https://main.qcloudimg.com/raw/ac9eca87504a40515746f5a499369ff7.png)
5. 根据实际需求，设置伸缩组。主要参数信息如下：
 - 名称：自定义。
 - 启动配置：根据实际需求进行设置。
 - 节点数量范围：限制伸缩组内节点的数量范围。
 - Label：为伸缩组设置 Label，会在自动扩容出的节点上设置 Label，从而实现服务的灵活调度策略。
6. <span id="step6">单击【提交】，完成创建。</span>
7. 重复执行 [步骤1](#step1) - [步骤6](#step6)，创建多个伸缩组。

>! 
> - 需要配置服务下容器的 request 值：自动扩容的触发条件是集群中存在由于资源不足而无法调度的 Pod，而判断资源是否充足正是基于 Pod 的 request 来进行的。
> - 不要直接修改属于伸缩组内的节点。
> - 同一伸缩组内的所有节点需具有相同的配置（机型和 Label 等）。
> - 可以使用 PodDisruptionBudget 防止 Pod 在缩容时被删除，。
> - 在指定伸缩组的最小/最大值节点数量设置之前，检查所在可用区的配额是否足够大。
> - 建议不要启用基于监控指标的节点弹性伸缩。
> - 删除伸缩组会同时销毁伸缩组内的 CVM，请谨慎操作。

#### 扩容缩容触发条件

##### 扩容条件

集群中出现因为缺少可用资源而无法调度的容器实例时，将触发自动扩容策略，尝试扩容节点来运行这些实例。
每当 kubernetes 调度程序找不到一个运行 Pod 的地方，它会将 Pod 的 PodCondition 设置为 false，并将原因设置为 “不可调度的”。集群自动扩缩容程序每隔一段时间扫描一次是否有不可调度的 Pod 来进行扩容，如果有，则尝试扩容节点来运行这些 Pod。

##### 缩容条件

当节点上所有 Pod（实例）的 CPU 和内存 request 占比同时小于50%时，作为备选缩容节点尝试缩容。如果满足以下所有缩容条件，需将该节点上的所有 Pod 都可调度到其他节点上，才可以进行缩容。
- 当您设置了严格的 PodDisruptionBudget 的 Pod 不满足 PDB 时，不会缩容。
- Kube-system 下的 Pod。
- 节点上有非 deployment，replica set，job，stateful set 等控制器创建的 Pod。
- Pod 有本地存储。
- Pod 不能被调度到其他节点上。

## 常见问题

扩容缩容的相关问题可参见 [扩容缩容相关](https://cloud.tencent.com/document/product/457/32316)。
