## Namespaces
Namespaces是Kubernetes支持在同一个集群中进行逻辑环境划分的对象， 您可以通过Namespaces进行管理多个团队多个项目的划分，Namespaces下Kubernetes对象的名称必须唯一，可以通过资源配额进行可用资源的分配，还可以实现不同Namespaces的网络访问控制。

### Namespaces使用方法

1. TKE控制台使用：TKE控制台提供Namespaces的增删改查功能.
2. 直接通过kubectl使用 ：更多详情可查看[Kubernetes官网文档](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/)

### 使用ResourceQuota设置Namespaces资源使用配额
一个命名空间下可以拥有多个ResourceQuota资源，每个ResourceQuota可以定义提供给每个Namespace的资源使用约束，可以设置Namespces：

- 计算资源如CPU内存的配额
- 存储资源如请求存储的总存储配额
- Kubernetes对象计数 如 Deployment个数配额

不同Kubernetes版本ResourceQuota支持的配额设置略有差异，更多详情查看[Kubernetes ResourceQuota官方文档](https://kubernetes.io/docs/concepts/policy/resource-quotas/)， 下述为ResourceQuota示例：
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: object-counts
  namespace: default
spec:
  hard:
    configmaps: "10"  ##最多10个ConfigMap
    replicationcontrollers: "20" ##最多20个replicationcontroller
    secrets: "10" ##最多10个secret
    services: "10"##最多10个service
    services.loadbalancers: "2"  ##最多2个Loadbanlacer模式的service
    cpu: "1000" ##该Namespaces下最多使用1000个CPU的资源
    memory: 200Gi ##该Namespaces下最多使用200Gi的内存
```


### 使用NetWorkPolicy设置Namespaces网络访问控制
Network Policy 是 k8s 提供的一种资源，用于定义基于 pod 的网络隔离策略，不局限限制Namespaces， 还可以更细粒度的控制Pod与Pod之间的网络访问控制，它描述了一组 pod 是否可以与其它组 pod，以及其它 network endpoints 进行通信。

使用NetworkPolicy需要在集群内部署NetworkPolicy Controller， 详细安装步骤可查看[使用 Network Policy 进行网络访问控制](https://cloud.tencent.com/document/product/457/19793), 此次介绍如何通过NetworkPolicy实现Namespaces间的网络控制。
