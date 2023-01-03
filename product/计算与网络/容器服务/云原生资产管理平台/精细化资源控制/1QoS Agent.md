QoS Agent 是腾讯云基于服务质量增强的扩展组件。提供丰富的能力，在提升集群资源利用率的同时，提供稳定性质量保障。 

>! QoS 相关的能力仅支持在 [原生节点](https://cloud.tencent.com/document/product/457/78197) 上使用，若您的节点不是原生节点，或工作负载不在原生节点上，相关能力无法生效。

## 部署在集群内的 Kubernetes 对象

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

| 功能            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| CPU 使用优先级  | CPU 使用优先级的功能可以通过对工作负载设置优先级，保证高优先级业务在发生资源竞争时的资源供给量，并压制低优先级业务。详情见 [CPU 使用优先级](https://cloud.tencent.com/document/product/457/79775)。 |
| CPU Burst       | CPU Burst 可以临时给延迟敏感型应用提供超过 Limit 数量的资源，保证其稳定性。详情见 [CPU Burst](https://cloud.tencent.com/document/product/457/79776)。 |
| CPU 超线程隔离  | 避免高优先级容器线程的 L2 Cache 受到运行在同一个 CPU 物理核上的低优先级线程的影响。详情见 [CPU 超线程隔离](https://cloud.tencent.com/document/product/457/79777)。 |
| 内存 QoS 增强   | 全方位提升内存表现，以及灵活限制容器对内存的使用。详情见 [内存 QoS 增强](https://cloud.tencent.com/document/product/457/79778)。 |
| 网络 QoS 增强   | 全方位提升网络表现，以及灵活限制容器对网络的使用。详情见 [网络 QoS 增强](https://cloud.tencent.com/document/product/457/79780)。 |
| 磁盘 IO QoS 增强 | 全方位提升磁盘表现，以及灵活限制容器对磁盘的使用。详情见 [磁盘 IO QoS 增强](https://cloud.tencent.com/document/product/457/79781)。 |





## 部署方式

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，在“组件列表”页面中选择**新建**。
4. 在“新建组件”页面中勾选 QoS Agent。
5. 单击**完成**即可安装组件。

>! 在部署完成之后，因为集群的 cgroup 驱动可能不同，需要您手动选择对应的驱动。操作方式如下：
1. 在集群里的**扩展组件**里，找到部署成功的 QoS Agent，单击右侧的**更新配置**。
2. 在修改 QoS Agent 的组件配置页面，选择 cgroupDrive 选项右侧的下拉框，选择与自己集群匹配的 cgroupDrive。
3. 单击**完成**。



## 常见问题

### 如何确认自己集群的 cgroupDrive？

集群的 cgroupDrive 只可能是 cgroupfs 或 systemd。

确认方式：

* 首先查看集群的运行时，可以在集群的“基本信息”页里的“运行时组件”判断当前集群是 docker 还是 containerd。
  * 如果运行时是 docker 的话，在集群的任意节点上执行 `docker info` 查看 `Cgroup Driver` 的字段内容。
  * 如果运行时是 containerd，在集群的任意节点的 /etc/containerd/config.toml 文件里，如果字段：`SystemdCgroup = true`，代表是 systemd，否则是 cgroup。

### 如何选择作用的业务或者节点？

支持通过标签或者世界选择某种资源对象。
>! 当同时存在下面两种 selector 的时候，会取“与”，也即满足所有条件。

#### labelSelector

labelSelector 通过关联资源对象的 label 对资源对象进行筛选，常用的使用方式是，业务侧在指定的工作负载上打上特定的标签，并将该标签提供给运维侧，运维在创建 PodQOS 时通过 labelSelector 字段关联该标签，即可赋予不同的业务不同的 QoS 能力。

#### scopeSelector

scopeSelector 由多个 MatchExpressions 组成，这些 MatchExpressions 之间是“与”的关系，MatchExpressions 中有三个字段，分别是 ScopeName，Operator 和 ScopeName 对应的 Values；

其中 ScopeName 包括 QOSClass，Priority，Namespace 三种；

* QOSClass 是指希望关联具有特定的 QOSClass 的 Workload，Values 可以填：Guaranteed，Burstable，BestEffort 中的一种或多种；
* Priority 是指希望关联具有特定的 Priority 的 workload，Values 可以填特定的 priority 数值，如["1000", "2000-3000"]，支持 priority 范围；
* Namespace 是指希望关联特定的 Namespace 的 Workload，Values 可以填一个或个多。

Operator 包含两种，分别是 In 和 NotIn，不填默认为 In。

如下面的例子，表示将满足 app-type=offline 的 BestEffortPod，CPU 优先级设置为7：

```yaml
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: offline-task
spec:
  allowedActions:
  - eviction
  resourceQOS:
    cpuQOS:
      cpuPriority: 7
  scopeSelector:
    matchExpressions:
    - operator: In
      scopeName: QOSClass
      values:
      - BestEffort
  labelSelector:
    matchLabels:
      app-type: offline
```

