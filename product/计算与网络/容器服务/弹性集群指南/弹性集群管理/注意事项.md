
弹性集群属于弹性容器服务（EKS）提供的集群服务，请务必于使用前阅读以下信息。

## 计费方式
弹性容器服务 EKS 是付费产品，采取按量计费模式。计费详情请参见 [计费概述](https://cloud.tencent.com/document/product/457/39807)、[产品定价](https://cloud.tencent.com/document/product/457/39806)、[购买限制](https://cloud.tencent.com/document/product/457/39821)。

## Pod 规格配置
Pod 的规格配置是容器运行时可用资源和使用服务计费的依据，请务必了解弹性集群支持的 Pod 规格配置和指定方法，详情请参见 [资源规格](https://cloud.tencent.com/document/product/457/39808) 和 [指定资源规格](https://cloud.tencent.com/document/product/457/44174)。


## Pod 临时存储
每个 Pod 创建时会分配不超过20GiB的临时镜像存储。

>!
>- 临时镜像存储将于 Pod 生命周期结束时删除，请勿用于存储重要数据。
>- 由于存储镜像，实际可用空间小于20GiB。
>- 重要数据、超大文件等推荐挂载 Volume 持久化存储。

## Kubernetes 版本
不支持 1.12 以下版本。

## 暂不支持功能列表
弹性集群没有 Node，所以不支持部分依赖 Node 组件，例如 Kubelet、Kube-proxy 的功能。
### Node
暂不支持添加、管理物理节点。

### 内核
仅支持自定义 net 开头的内核参数。

### Workload
不支持部署 DaemonSet 类型的工作负载。

### Service
不支持部署 NodePort 类型的服务。

### Volume
不支持 hostpath 类型的数据卷。
