

## 组件介绍

ENI-IPAMD 运行在特定节点或 master 上，是一个 IP 资源分配管理的 GRPC server。其职责为实现 IP 资源分配管理、为 Statefulset 控制器预留 IP 资源，及为节点控制器分配管理主机辅助网卡。

**当集群选择 VPC-CNI 网络模式后，会自动安装该组件。**VPC-CNI 模式具备以下特点：
- VPC-CNI 模式是容器服务 TKE 支持的扩展网络模式，利用腾讯云的多弹性网卡能力，为集群内的 Pod 分配 VPC 内的 IP 地址。由腾讯云 VPC 功能负责路由，可实现 Pod 和 Node 的控制面和数据面完全在同一网络层面，该模式下的 Pod 能够复用腾讯云 VPC 所有产品特性。
- 集群开启 VPC-CNI 模式后，StatefulSet 支持固定 IP 类型的 Pod。该类型的 Pod 重启和迁移保持 IP 不变。适用于需要对 IP 来源做访问限制、通过 IP 查询日志等场景。
>! VPC-CNI 模式存在使用限制，建议您提前考虑是否适配您的业务场景。





## 在集群内部署的 kubernetes 对象

| kubernetes 对象名称 | 类型       | 默认占用资源             | 所属 Namespaces |
| ------------------- | ---------- | ------------------------ | --------------- |
| tke-eni-ipamd       | Deployment | CPU：100m<br>memory：100Mi | kube-system     |
| tke-eni-agent       | DaemonSet  | CPU：10m                 | kube-system     |
| tke-eni-ipamd       | Service    | -                        | kube-system     |
| tke-cni-agent-conf  | ConfigMap  | -                        | kube-system     |

## 相关文档
- [VPC-CNI 网络模式使用指引](https://cloud.tencent.com/document/product/457/48040)
- [GlobalRouter 附加 VPC-CNI 模式说明](https://cloud.tencent.com/document/product/457/34993)
