本文结合实际生产经验介绍如何在业务中结合弹性伸缩使资源得到充分利用，您可参考下文并进行相应的配置调整。

## 应对流量突发型业务
通常业务会有高峰和低谷，为了更合理的利用资源，可为服务定义 HPA，实现根据 Pod 的资源实际使用情况来对服务进行自动扩缩容。在业务高峰期时自动扩容 Pod 数量来支撑服务，在业务低谷时自动缩容 Pod 释放资源，以供其他服务使用。例如，夜间线上业务低峰，自动缩容释放资源以供大数据类的离线任务运行。


使用 HPA 前，需安装 resource metrics（metrics.k8s.io）或 custom metrics（custom.metrics.k8s.io），使 hpa controller 通过查询相关 API 获取到服务资源的占用情况，即 K8s 先获取服务的实际资源占用情况（指标数据）。
早期 HPA 使用 resource metrics 获取指标数据，后推出的 custom metrics 可通过更灵活的指标来控制扩缩容。Kubernetes 官方相关实现为 metrics-server，而社区通常使用基于 prometheus 的 实现 prometheus-adapter，云厂商托管的 Kubernetes 集群通常集成自身的实现。例如容器服务，实现了 CPU、内存、硬盘、网络等维度的指标，可在网页端可视化创建 HPA，最终转化为 Kubernetes 的 yaml。示例如下：
```
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta2
    kind: Deployment
    name: nginx
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Pods
    pods:
      metric:
        name: k8s_pod_rate_cpu_core_used_request
      target:
        averageValue: "100"
        type: AverageValue
```

### 节约成本
HPA 能够实现 Pod 水平扩缩容，但如果节点资源不足，则扩容出的 Pod 状态仍会 Pending。如果提前准备好大量节点，使资源冗余，即使不会发生 Pod Pending 问题，但成本可能过高。
通常云厂商托管的 Kubernetes 集群均会实现 cluster-autoscaler，即根据资源使用情况，动态增删节点，使计算资源能够被最大化弹性使用，并通过按量计费的计费模式节约成本。例如，容器服务中的伸缩组，及包含伸缩组功能的拓展特性（节点池）。


### 使用垂直伸缩 
对于无法适配水平伸缩的单体应用，或不确定最佳 request 与 limit 超卖比的应用，可尝试使用 VPA 来进行垂直伸缩。即自动更新 request 与 limit，并重启 pod。该特性容易导致服务出现短暂的不可用，不建议在生产环境中大规模使用。 
