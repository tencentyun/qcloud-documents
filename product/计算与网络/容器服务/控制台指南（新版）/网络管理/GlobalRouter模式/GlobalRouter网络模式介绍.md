## GlobalRouter网络模式介绍

GlobalRouter 网络模式是容器服务 TKE 基于底层私有网络 VPC 的全局路由能力，实现了容器网络和 VPC 互访的路由策略。该网络模式特征包含以下几点：

- 容器路由直接通过 VPC。
- 容器与节点分布在同一网络平面。
- 容器网段分配灵活，容器 IP 段不占用 VPC 的其他网段。

GlobalRouter 网络模式适用于常规场景，可与标准 Kuberentes 功能无缝使用。使用原理图如下所示：
![](https://main.qcloudimg.com/raw/eb19847fdd0de5f3ebb8381f33a885e8.png)


## GlobalRouter网络模式容器IP分配机制

### 名词介绍
![](https://main.qcloudimg.com/raw/bcc67451f63004fa8dd982dc17a48a6c.png)
- **容器 CIDR**：集群内 Sevice、 Pod 等资源所在网段。
- **Services 数量上限/集群**：决定分配给 Sevice 的 CIDR 大小。
>? 容器服务 TKE 集群默认创建3个 Sevice：kubernetes、hpa-metrics-service、kube-dns，同时还有2个广播地址和网络号，因此用户可以使用的 Services 数量上限/集群是 serviceMax - 5。
>
- **Pod 数量上限/Node**：决定分配给每个 Node 的 CIDR 的大小。
>? 腾讯云容器服务 TKE 集群默认创建2个 kube-dns 的 Pod 和1个 l7-lb-controller 的 Pod。
> 对于一个 Node 上的 Pod，有三个地址不能分配分别是：网络号、广播地址和网关地址，因此 Node 最大的 Pod 数目 = podMax - 3。
> 集群节点数量计算方法：（CIDR IP数量 - Services 数量上限）/ 单节点Pod数量上限

### Pod IP 分配
工作原理如下图所示：
![](https://main.qcloudimg.com/raw/9d9fe92dd9d9d11ada9b24c66ce640fb.png)
1. 集群的每一个节点会使用容器 CIDR 中的指定大小的网段用于该节点下 Pod 的 IP 地址分配。
2. 集群的 Service 网段会选用容器 CIDR 中最后一段指定大小的网段用于 Service 的 IP 地址分配。
3. 节点释放后，使用的容器网段也会释放回 IP 段池。
4. 扩容节点自动按顺序循环选择容器 CIDR 大段中可用的 IP 段。


## GlobalRouter网络模式使用限制

- 集群网络和容器网络网段不能重叠。
- 同一 VPC 内，不同集群的容器网络网段不能重叠。
- 容器网络和 VPC 路由重叠时，优先在容器网络内转发。
- 不支持固定 Pod IP。
