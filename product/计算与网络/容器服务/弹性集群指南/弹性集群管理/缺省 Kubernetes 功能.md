## 说明事项
弹性容器集群（EKS）由于没有集群 Node，部分依赖 Node、Kubelet、Kube-proxy 的原生功能暂不支持。

## 暂不支持功能列表
### Kubernetes 版本
不支持 1.12 以下版本。

### Node
不支持添加、管理物理节点。

### 内核
不支持自定义非 net 开头的内核参数。

### Workload
- 不支持部署 DaemonSet 类型的工作负载。
- 不支持 hostPath 作为数据卷。

### Service
不支持部署 NodePort 类型的服务。

### Volume
不支持共享卷（emptyDir）的 Linux filesystem event（INOTIFY）特性。
