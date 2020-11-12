## VPC-CNI网络 - 多Pod共享网卡模式

VPC-CNI 模式是 TKE 基于 CNI 和 VPC 弹性网卡实现的容器网络能力，适用于对时延有较高要求的场景。该网络模式下，容器与节点分布在同一网络平面，容器 IP 为 IPAMD 组件所分配的弹性网卡 IP。

VPC-CNI 多Pod共享网卡模式使用原理图如下所示：
![](https://main.qcloudimg.com/raw/76fce8d2541f9a91a1a2ecdc89403390.jpg)



### VPC-CNI 模式应用场景
相比 Global Router，VPC-CNI 具有以下优势及适用场景：
- 少了一层网桥，网络转发性能更高，大约提升10%, 适用于对网络时延要求较高的场景。
- 支持 Pod 固定 IP， 适用于依赖容器固定 IP 的场景。例如，传统架构迁移到容器平台及针对 IP 做安全策略限制。
- 支持 LB 直通 Pod 

### VPC-CNI 模式使用限制
- 需要为容器专门规划子网，子网不建议其他云上资源共用（如云服务器、负载均衡等）。
- 集群内的节点需要和子网处于相同可用区，如果节点可用区与容器子网不在相同，Pod 将无法调度。
- 节点上可调度的 VPC-CNI 模式的 Pod 数量受限于节点所支持插入弹性网卡能绑定 IP 的最大数量。配置越高的机器可插入的弹性网卡数量越多，可以通过查看节点的 Allocatable 来确认。



### VPC-CNI网络 - 多Pod共享网卡模式的Pod IP分配机制
![](https://main.qcloudimg.com/raw/96f2d2c978aaa37146a7035a0c3eadd9.png)
- 集群网络是用户的 VPC, 节点和容器子网属于该VPC.
- 容器子网可以选择多个VPC内的子网。
- 集群每新增一个节点，申请一张弹性网卡，同时为该网卡一次性申请该网卡能绑定IP数量上限的IP资源，用于该节点上PodIP地址。
- 节点删除时，释放网卡占用的IP资源。


### VPC-CNI模式使用方法
>! 
使用 VPC-CNI 需要确保 rp_filter 处于关闭状态。可参考以下代码示例：
``` bash
sysctl -w net.ipv4.conf.all.rp_filter=0
sysctl -w net.ipv4.conf.default.rp_filter=0
```
`tke-cni-agent` 组件自动设置节点的内核参数。若您自己有维护内核参数且打开 rp_filter，会导致网络不通。
>
#### VPC-CNI 模式操作步骤
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 创建集群时选择 VPC-CNI 网络插件。如下图所示：
![](https://main.qcloudimg.com/raw/d3d84cfc2ede5be4c67d698c03b18c6a.png)





