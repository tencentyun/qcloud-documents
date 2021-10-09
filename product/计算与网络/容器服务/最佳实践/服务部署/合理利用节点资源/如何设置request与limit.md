容器的 request 及 limit 需根据服务类型、需求及场景进行灵活设置。本文结合实际生产经验进行分析总结，您可参考下文并进行相应的配置调整。



## Request 工作原理
Request 的值并不代表给容器实际分配的资源大小，而是用于提供给调度器。调度器会检测每个节点可用于分配的资源（节点可分配资源 = 节点资源总额 - 已调度到节点上的 Pod 内容器 request 之和），同时记录每个节点已经被分配的资源（节点上所有 Pod 中定义的容器 request 之和）。如发现节点剩余的可分配资源已小于当前需被调度的 Pod 的 request，则该 Pod 就不会被调度到此节点。反之，则会被调度到此节点。

若不配置 request，调度器就无法感知节点资源使用情况，无法做出合理的调度决策，可能会造成调度不合理，引起节点状态混乱。建议给所有容器设置 request，使调度器可感知节点资源情况，以便做出合理的调度决策。集群的节点资源能够被合理的分配使用，避免因资源分配不均而导致发生故障。




## 设置 request 与 limit 默认值
可使用 LimitRange 来设置 nameapsace 的 request 与 limit 默认值，也可设定 request 与 limit 的最大值与最小值。示例如下：
<dx-codeblock>
::: yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: mem-limit-range
  namespace: test
spec:
  limits:
  - default:
      memory: 512Mi
      cpu: 500m
    defaultRequest:
      memory: 256Mi
      cpu: 100m
    type: Container
:::
</dx-codeblock>


## 重要线上应用配置
节点资源不足时，会触发自动驱逐，删除低优先级的 Pod 以释放资源使节点自愈。Pod 优先级**由低到高**排序如下：
1. 未设置 request 及 limit 的 Pod。
2. 设置 request 值不等于 limit 值的 Pod。
3. 设置 request 值等于 limit 值的 Pod。

建议重要线上应用设置 request 值等于 limit 值，此类 Pod 优先级较高，在节点故障时不易被驱逐导致线上业务受到影响。



## 提高资源利用率
如应用设置了较高的 request 值，而实际占用资源远小于设定值，会导致节点整体的资源利用率较低。除对时延非常敏感的业务外，敏感的业务本身并不期望节点利用率过高，影响网络包收发速度。

建议对非核心，并且资源非长期占用的应用，适当减少 request 以提高资源利用率。若您的服务支持水平扩容，则除 CPU 密集型应用外，单副本的 request 值通常可设置为不大于1核。例如，coredns 设置为0.1核，即100m即可。


## 避免 request 与 limit 值过大
若您的服务使用单副本或少量副本，且 request 及 limit 的值设置过大，使服务可分配到足够多的资源去支撑业务。则某个副本发生故障时，可能会给业务带来较大影响。当 Pod 所在节点发生故障时，由于 request 值过大，且集群内资源分配的较为碎片化，其余节点无足够可分配资源满足该 Pod 的 request，则该 Pod 无法实现漂移，无法自愈，会加重对业务的影响。 

建议尽量减小 request 及 limit，通过增加副本的方式对您的服务支撑能力进行水平扩容，使系统更加灵活可靠。



## 避免测试 namespace 消耗过多资源


若生产集群有用于测试的 namespace，如不加以限制，则可能导致集群负载过高，影响生产业务。可以使用 `ResourceQuota` 限制测试 namespace 的 request 与 limit 的总大小。示例如下：
<dx-codeblock>
::: yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: quota-test
  namespace: test
spec:
  hard:
    requests.cpu: "1"
    requests.memory: 1Gi
    limits.cpu: "2"
    limits.memory: 2Gi
:::
</dx-codeblock>


