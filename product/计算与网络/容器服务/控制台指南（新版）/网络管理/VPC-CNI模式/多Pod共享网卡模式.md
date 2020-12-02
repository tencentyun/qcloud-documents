
## 多 Pod 共享网卡模式的 Pod IP 分配机制
多 Pod 共享网卡模式的 Pod IP 分配机制如下图所示：
![](https://main.qcloudimg.com/raw/96f2d2c978aaa37146a7035a0c3eadd9.png)

- 集群网络是用户的 VPC，节点和容器子网属于该 VPC。
- 容器子网可以选择多个 VPC 内的子网。
- 非固定 IP 模式下（默认模式），集群每新增一个节点，申请一张弹性网卡，同时为该网卡一次性申请该网卡能绑定 IP 数量上限的 IP 资源，用于该节点上 Pod IP 地址。
- 固定 IP 模式下，集群每新增一个节点，申请一张弹性网卡，不会提前绑定任何辅助 IP。集群中每次新建一个使用 VPC-CNI 模式的 Pod，才会即时申请绑定辅助 IP 到相应节点的网卡上。
- 节点删除时，将释放网卡占用的 IP 资源。


## 使用方法


使用 VPC-CNI 需要确保 `rp_filter` 处于关闭状态。可参考以下代码示例：
``` bash
sysctl -w net.ipv4.conf.all.rp_filter=0
# 假设 eth0 为主网卡
sysctl -w net.ipv4.conf.eth0.rp_filter=0
```
`tke-eni-agent` 组件自动设置节点的内核参数。若您自己有维护内核参数且打开 `rpfilter`，则会导致网络不通。

>? 如需在创建集群时开启 VPC-CNI 模式，可参考 


### VPC-CNI 模式操作步骤

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 创建集群时选择 VPC-CNI 网络插件。如下图所示：
![](https://main.qcloudimg.com/raw/d3d84cfc2ede5be4c67d698c03b18c6a.png)






