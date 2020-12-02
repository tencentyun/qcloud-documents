
## 使用原理
VPC-CNI 模式是容器服务 TKE 基于 CNI 和 VPC 弹性网卡实现的容器网络能力，适用于对时延有较高要求的场景。该网络模式下，容器与节点分布在同一网络平面，容器 IP 为 IPAMD 组件所分配的弹性网卡 IP。VPC-CNI 模式使用原理图如下所示：
![](https://main.qcloudimg.com/raw/76fce8d2541f9a91a1a2ecdc89403390.jpg)


其中 VPC-CNI 模式分为共享网卡模式和独占网卡模式。两种网络模式适用于不同的场景。您可以根据业务需要选择不同的网络模式。
- [共享网卡模式](https://cloud.tencent.com/document/product/457/50356)：Pod 共享一张弹性网卡，IPAMD 组件为弹性网卡申请多个 IP 给到不同的 Pod。
- [独占网卡模式](https://cloud.tencent.com/document/product/457/50357)：每个 Pod 有独立的弹性网卡，性能更高。受机型影响，不同节点可使用的弹性网卡数量有限，单节点 Pod 密度更低。


## 相关操作
### 开启支持固定 Pod IP

>! 
> - 默认情况下，VPC-CNI 模式**不支持固定 Pod IP 能力**，且该能力仅支持在 [创建集群](https://cloud.tencent.com/document/product/457/32189) 时设置，集群创建完成后无法更改。如需开启支持固定 Pod IP，请参见 [固定 IP 模式使用说明](https://cloud.tencent.com/document/product/457/50358)。
> - 开启固定 Pod IP 能力后，仅支持选择空子网作为集群网络。
> - 固定 IP 的 Pod 不支持跨子网迁移。

在配置“集群信息”步骤中，选择“容器网络插件”为【VPC-CNI】，并勾选“开启支持”即可。如下图所示：
![](https://main.qcloudimg.com/raw/f36911bf904ebd35867e24e3b6bb6bb1.png)



