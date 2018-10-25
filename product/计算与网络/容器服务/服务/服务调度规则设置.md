## 简介
通过设置服务下告警设置的调度规则，可以指定该服务下的容器如何在集群内进行调度， 存在以下应用场景：
- 将  Pod  运行在指定的节点上。
- 将  Pod  运行在某一作用域的节点上。
>注：作用域可以是可用区、机型等属性。
- 将 Pod  强制打散到节点上（每个节点一个，不符合条件的 Pod 停止调度）。
- 指定 Pod 与其他的 Pod 的共存规则。

## 使用方法
### 前置条件
1. 设置服务高级设置中的调度规则， 集群的 Kubernetes 版本必须是 1.7 以上的版本。
2. 为确保您的 Pod 能够调度成功，请确保您设置的调度规则完成后，节点有空余的资源用于容器的调度。

### 设置调度规则
如果您的集群是 1.7 或更高的版本，您可以在创建服务或者更新服务中设置调度规则。
![][1]
您可以选择以下两种调度类型：
- 指定节点调度：可设置实例（ Pod ）调度到指定规则的节点上，匹配节点标签
- 指定实例调度：可设置实例（ Pod ）和其他服务下的实例之间的调度规则，匹配实例标签

两种调度类型均可以添加多条调度规则， 各规则的含义如下：
- In ：Label 的 value 在列表中。
- NotIn：Label 的 value 不在列表中。
- Exists：Label 的 key 存在。
- DoesNotExits：Label 的 key 不存在。
- Gt：Label 的值大于列表值 （字符串匹配）。
- Lt： Label 的值小于列表值 （字符串匹配）。

强制调度开关可以强制要求相同实例，不会运行在同一个节点上，不符合条件的实例会停止调度。开启后每个节点有且仅有分配一个该服务下的 Pod。

## 原理介绍
服务的调度规则主要通过下发 Yaml 到 Kubernetes 集群， kubernetes 的 Affinity and anti-affinity 机制会使得 Pod 按一定规则进行调度。更多 kubernetes 的 Affinity and anti-affinity 机制介绍可 [查看详情](https://kubernetes.io/docs/concepts/configuration/assign-Pod-node/)。

[1]:https://main.qcloudimg.com/raw/8dda9c19080b2a5beda3133b13fa3ace.png
