
## 使用原理
VPC-CNI 模式是容器服务 TKE 基于 CNI 和 VPC 弹性网卡实现的容器网络能力，适用于对时延有较高要求的场景。该网络模式下，容器与节点分布在同一网络平面，容器 IP 为 IPAMD 组件所分配的弹性网卡 IP。VPC-CNI 模式使用原理图如下所示：
![](https://main.qcloudimg.com/raw/76fce8d2541f9a91a1a2ecdc89403390.jpg)


其中 VPC-CNI 模式分为共享网卡模式和独占网卡模式，两种网络模式适用于不同的场景。您可以根据业务需要选择不同的网络模式。
- [共享网卡模式](https://cloud.tencent.com/document/product/457/50356)：Pod 共享一张弹性网卡，IPAMD 组件为弹性网卡申请多个 IP 给到不同的 Pod。可固定 Pod IP，详情请参见 [固定 IP 模式使用说明](https://cloud.tencent.com/document/product/457/50358)。
- [独占网卡模式](https://cloud.tencent.com/document/product/457/50357)：每个 Pod 有独立的弹性网卡，性能更高。受机型影响，不同节点可使用的弹性网卡数量有限，单节点 Pod 密度更低。


## 使用限制
- 仅支持 TKE kubernetes 版本在1.10及以上版本。
- 集群需要开启 cni 支持。
- 当前 VPC-CNI 模式的子网不能与其他云上资源共用（如云服务器、负载均衡等）。
- 和子网处于相同可用区的节点才支持创建 VPC-CNI 模式的 Pod，请提前规划 VPC-CNI 模式子网。
- 您需要指定单节点下 VPC-CNI 模式的 Pod 数量上限，创建后不可修改。建议集群中节点配置相同。






