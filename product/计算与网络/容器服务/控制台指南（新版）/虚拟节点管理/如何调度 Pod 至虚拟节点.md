
本篇文章主要介绍在容器服务 TKE 集群中，如何调度 Pod 至虚拟节点，主要有两种调度方式：
- 自动扩容
- 手动调度

### 自动扩容
若集群配置了虚拟节点，当业务高峰且已有节点资源不足时，会自动调度 Pod 至虚拟节点，无需购买服务器；业务恢复平稳，自动释放在虚拟节点中的 Pod 资源，也无需再进行退还机器操作。

如果集群同时开启了 [Cluster Autoscaler](https://cloud.tencent.com/document/product/457/32190#AutomaticAddAndRemove) 和虚拟节点，则会尽量优先将 Pod 调度到虚拟节点上，而非触发集群节点扩容。如果受上述调度限制影响，Pod 无法调度到虚拟节点上，则会依然正常触发集群节点扩容。而服务器节点资源充足时，会优先缩容虚拟节点上的 Pod。


### 手动调度

虚拟节点支持手动将 Pod 调度至虚拟节点，默认虚拟节点会自动添加 Taints 以降低调度优先级，如需手动调度 Pod 到虚拟节点或指定虚拟节点，通常需要为 Pod 添加对应的 Tolerations。但并非所有的 Pod 均可以调度到虚拟节点上，详情请参见 [虚拟节点调度说明](https://cloud.tencent.com/document/product/457/53030)。为方便使用，您可以在 Pod Spec 中指定 nodeselector 。示例如下：

```yaml
spec:    
    nodeSelector:
      node.kubernetes.io/instance-type: eklet
```

或在 Pod Spec 指定 nodename。示例如下：
```yaml
spec:
   nodeName: $虚拟节点名称
```

容器服务 TKE 的管控组件会判断该 Pod 是否可以调度到虚拟节点，若不支持则不会调度到虚拟节点。详情请见 [手动调度 Pod 至虚拟节点](https://cloud.tencent.com/document/product/457/54754#.E5.A6.82.E4.BD.95.E6.89.8B.E5.8A.A8.E8.B0.83.E5.BA.A6-pod-.E5.88.B0.E8.99.9A.E6.8B.9F.E8.8A.82.E7.82.B9.EF.BC.9F.3Ca-id.3D.22pod1.22.3E.3C.2Fa.3E)。


