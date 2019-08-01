集群网络与容器网络是集群的基本属性。通过设置集群网络和容器网络可以规划集群的网络划分。
- **集群网络**：为集群内主机分配在节点网络地址范围内的 IP 地址，您可以选择私有网络中的子网用于集群的节点网络。更多私有网络的介绍可参看 [私有网络和子网](/doc/product/215/4927) 。
- **容器网络**：为集群内容器分配在容器网络地址范围内的 IP 地址，您可以自定义三大私有网段作为容器网络， 根据您选择的集群内服务数量的上限，自动分配适当大小的 CIDR 段用于 kubernetes service；也可以根据您选择的 每个节点的pod数量上限，自动为集群内每台云服务器分配一个适当大小的网段用于该主机分配 Pod 的 IP 地址。

### 集群网络与容器网络的关系

- 集群网络和容器网络网段不能重叠。
- 同一 VPC 内，不同集群的容器网络网段不能重叠。
- 容器网络和 VPC 路由重叠时，优先在容器网络内转发。

### 集群网络与腾讯云其他资源通信

- 集群内容器与容器之间互通。
- 集群内容器与节点直接互通。
- 集群内容器与 [云数据库 TencentDB](https://cloud.tencent.com/product/cdb-overview)、[云存储 Redis](/doc/product/239/3205)、[云数据库 Memcached](/doc/product/241/7489) 等资源同一 VPC 下内网互通。
- [设置同地域集群间互通](https://cloud.tencent.com/document/product/457/32197)。
- [设置跨地域集群间互通](https://cloud.tencent.com/document/product/457/32198)。
- [设置容器集群与 IDC 互通](https://cloud.tencent.com/document/product/457/32199)。
- [设置 CVM 容器集群与黑石容器集群互通](https://cloud.tencent.com/document/product/457/32200)。

### 容器网络说明

- 容器 CIDR：集群内 Sevice、 Pod 等资源所在网段。
- Services 数量上限/集群：决定分配给 Sevice 的 CIDR 大小。
>? 腾讯云容器服务 TKE 集群默认创建3个 Sevice：kubernetes、hpa-metrics-serviceube-dns，kube-dns，同时还有2个广播地址和网络号，因此用户可以使用的Services 数量上限/集群是 serviceMax - 5。
- Pod 数量上限/Node：决定分配给每个 Node 的 CIDR 的大小。
>? 腾讯云容器服务 TKE 集群默认创建2个 kube-dns 的 Pod 和1个 l7-lb-controller 的 Pod。
对于一个 Node 上的 Pod，有三个地址不能分配分别是：网络号，广播地址和网关地址，因此 Node 最大的 Pod 数目 = podMax - 3。
