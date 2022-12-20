Namespaces 是 Kubernetes 在同一个集群中进行逻辑环境划分的对象， 您可以通过 Namespaces 进行管理多个团队多个项目的划分。在 Namespaces 下，Kubernetes 对象的名称必须唯一。您可以通过资源配额进行可用资源的分配，还可以进行不同 Namespaces 网络的访问控制。

## 使用方法

### 通过控制台使用
容器服务控制台提供 Namespaces 的增删改查功能。操作步骤如下：

#### 创建命名空间
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)，选择左侧导航栏中的**集群**。
2. 在集群列表中单击集群 ID，进入集群详情页。
3. 选择“命名空间”，在命名空间页面单击**新建**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a4c7e0a2324a723a5bc945cb061e52bc.png)
4. 在新建命名空间页面，设置命名空间名称，并选择镜像仓库密钥下发方式。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9e2aaa8b10705286de0727682bf65d17.png)
5. 单击**创建Namespace**。完成创建后，您可以在命名空间页面进行查看。

#### 设置资源配额和限制
1. 在命名空间页面，单击目标命名空间右侧操作列的**配额管理**。
![](https://qcloudimg.tencent-cloud.cn/raw/9ae5996cdb3bdb9c3d45233f777ee23b.png)
2. 在“资源配额与限制”中，您可快速设置计算资源限制、存储资源限制和其他资源限制。为命名空间配置资源配额，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/605c3baa98d119663796dae82c1c7688.png)
3. 在“编辑 LimitRange”中，您可快速设置默认资源限制。为该命名空间下的容器设置默认资源限制，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e8801e5ad9e00681ce1ff08cd3389ece.png)
>? 对命名空间设置 CPU/内存 limit/request 配额后，创建工作负载時，必须指定 CPU/内存 limit/request，或为命名空间配置 LimitRange，更多请参考 [ResourceQuotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)。
>
4. 编辑完成后单击**确定**即可。

#### 删除命名空间
1. 在命名空间页面，单击目标命名空间右侧操作列的**删除**。
2. 在“删除资源”弹窗中，确认资源信息，单击**确定**可删除对应的命名空间，且该命名空间下的资源对象也会被删除。

### 通过 Kubectl 使用
通过 Kubectl 使用：更多详情可查看 [Kubernetes 官网文档](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/)。

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

Network Policy 是 K8s 提供的一种资源，用于定义基于 Pod 的网络隔离策略。不仅可以限制 Namespaces， 还可以控制 Pod 与 Pod 之间的网络访问控制，即控制一组 Pod 是否可以与其它组 Pod，以及其它 network endpoints 进行通信。

在集群内部署 NetworkPolicy Controller，并通过 NetworkPolicy 实现 Namespaces 之间的网络控制的操作详情可查看 [使用 Network Policy 进行网络访问控制](https://cloud.tencent.com/document/product/457/19793)。


