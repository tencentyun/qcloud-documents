
## 简介

在 Kuberentes 集群中，因为容器化的方式，可以在一个节点上运行更多的业务，但这样也会引发业务之间资源的竞争。此时会使用 Request 来保证 Pod 申请资源的最小量，以防止在发生资源竞争时，没有足够的资源可用。但是这部分通过 Request 申请的资源量被永久“占用”，无法被别的业务使用，在流量波谷时，会造成较大浪费。因此 TKE 推出了可抢占式 Job，该类型 Job 使用的资源是集群中的闲置资源，不占用集群/节点真实的剩余可调度量，在发生资源竞争时，该部分资源会被优先回收，保证正常使用 Request 资源的业务的稳定性。

## 部署在集群内的资源对象

可抢占式 Job 需要首先在集群中安装 QoSAgent 组件，该组件在集群中部署的资源对象包括：

| Kubernetes 对象名称                       | 类型                     | 默认占用资源 | 所属 Namespaces |
| ----------------------------------------- | ------------------------ | ------------ | --------------- |
| avoidanceactions.ensurance.crane.io       | CustomResourceDefinition | -            | -               |
| nodeqoss.ensurance.crane.io               | CustomResourceDefinition | -            | -               |
| podqoss.ensurance.crane.io                | CustomResourceDefinition | -            | -               |
| timeseriespredictions.prediction.crane.io | CustomResourceDefinition | -            | -               |
| kube-system                               | Namespace                | -            | -               |
| all-be-pods                               | PodQOS                   | -            | kube-system     |
| qos-agent                                 | ClusterRole              | -            | -               |
| qos-agent                                 | ClusterRoleBinding       | -            | -               |
| crane-agent                               | Service                  | -            | kube-system     |
| qos-agent                                 | ServiceAccount           | -            | kube-system     |
| qos-agent                                 | Daemonset                | -            | kube-system     |

## 功能说明

  - 因为只有原生节点才有闲置资源，所以该功能仅支持在 [原生节点](https://cloud.tencent.com/document/product/457/78197) 中使用。
  - 支持为 Job、CronJob 分配集群中的闲置资源。
  - 该部分闲置资源不占用集群中的剩余可调度资源。
  - 当发生资源竞争时，闲置资源会被优先回收，因此被称之为可抢占式 Job。
  - 节点和集群的闲置资源数值是动态变化的，根据实际的负载动态变化。当集群/节点闲置资源小于 Job 对闲置资源申请时，导致 Pod 会 Pending。

## Request 推荐原理

- 闲置资源的分配方式是根据 Kubernetes 原生的 [Extended Resource](https://kubernetes.io/docs/tasks/administer-cluster/extended-resource-node/) 实现。通过 Extended Resource 回收节点的剩余可用资源形成共享资源池，共享资源池不占用实际集群/节点的 CPU/RAM 可调度资源量。
- 如下图所示，QoS Agent 组件将集群中所有没有被真正使用的资源中抽取一部分资源，根据节点历史负载画像情况预测出安全的 Extended Resource 数值，该部分资源可以被声明使用 Extended Resource 的 Job/CronJob 使用。
![](https://qcloudimg.tencent-cloud.cn/raw/b9e760173edcde5ece66d3a81a1f031f.png)

## 使用可抢占式 Job

### 安装组件
   
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 **QoS Agent**。
5. 单击**完成**即可安装组件。

### 部署可抢占式 Job

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**工作负载**，单击 Job/CronJob。
4. 在 Job/CronJob 资源列表页面，单击**新建**。
5. 在“新建组件”页面中开启**可抢占**功能。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4f215680cdea0e6527424aba0dec02c3.png)
 开启可抢占的能力之后，Job/CronJob 的资源输入方式发生了变化，无需输入 Request/Limit 变为了 Extended CPU 和 Extended 内存：
   - **Extended CPU**：申请原生节点中的空闲 CPU 资源。Extended CPU 限制只能是整数。
   - **Extended 内存**：申请原生节点中的空闲内存资源。Extended 内存限制只能是整数。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b0cdbaba186756766140493753261bc8.png) 
6. 通过声明使用 Extended Resource 的闲置资源创建出来的可抢占类型的 Job：
![](https://qcloudimg.tencent-cloud.cn/raw/a487a0d33b2fbbcb5ef93131def3309b.png)
>! 若您没有原生节点，或原生节点没有足够多的闲置资源，则可能有如下报错："Insufficient gocran.io/memory"，表示没有足够的闲置内存资源；如果是"Insufficient gocran.io/cpu"，表示没有足够的闲置 CPU 资源。此时需要增加 [原生节点](https://cloud.tencent.com/document/product/457/78197) 数量。
报错信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d4ebd169fb320ce102495cdac73835ea.png)
