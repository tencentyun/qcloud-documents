Namespaces 是 Kubernetes 在同一个集群中进行逻辑环境划分的对象， 您可以通过 Namespaces 进行管理多个团队多个项目的划分。在 Namespaces 下，Kubernetes 对象的名称必须唯一。您可以通过资源配额进行可用资源的分配，还可以进行不同 Namespaces 网络的访问控制。

## 使用方法

- 通过 TKE 控制台使用：TKE 控制台提供 Namespaces 的增删改查功能。
- 通过 Kubectl 使用：更多详情可查看 [Kubernetes 官网文档](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/)。

## 通过 ResourceQuota 设置 Namespaces 资源的使用配额

一个命名空间下可以拥有多个 ResourceQuota 资源，每个 ResourceQuota 可以设置每个 Namespace 资源的使用约束。可以设置 Namespaces 资源的使用约束如下：
- 计算资源的配额，例如 CPU、内存。
- 存储资源的配额，例如请求存储的总存储。
- Kubernetes 对象的计数，例如 Deployment 个数配额。

不同的 Kubernetes 版本，ResourceQuota 支持的配额设置略有差异，更多详情可查看 [Kubernetes ResourceQuota 官方文档](https://kubernetes.io/docs/concepts/policy/resource-quotas/)。
ResourceQuota 的示例如下所示：
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: object-counts
  namespace: default
spec:
  hard:
    configmaps: "10"  ## 最多10个 ConfigMap
    replicationcontrollers: "20" ## 最多20个 replicationcontroller
    secrets: "10" ## 最多10个 secret
    services: "10" ## 最多10个 service
    services.loadbalancers: "2"  ## 最多2个 Loadbanlacer 模式的 service
    cpu: "1000" ## 该 Namespaces 下最多使用1000个 CPU 的资源
    memory: 200Gi ## 该 Namespaces 下最多使用200Gi的内存
```

## 通过 NetWorkPolicy 设置 Namespaces 网络的访问控制

Network Policy 是 k8s 提供的一种资源，用于定义基于 Pod 的网络隔离策略。不仅可以限制 Namespaces， 还可以控制 Pod 与 Pod 之间的网络访问控制，即控制一组 Pod 是否可以与其它组 Pod，以及其它 network endpoints 进行通信。

在集群内部署 NetworkPolicy Controller，并通过 NetworkPolicy 实现 Namespaces 之间的网络控制的操作详情可查看 [使用 Network Policy 进行网络访问控制](https://cloud.tencent.com/document/product/457/19793)。

