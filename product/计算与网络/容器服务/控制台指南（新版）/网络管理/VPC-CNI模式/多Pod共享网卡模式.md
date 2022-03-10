
## 使用原理

VPC-CNI 多 Pod 共享网卡模式使用原理图如下所示：
![](https://main.qcloudimg.com/raw/76fce8d2541f9a91a1a2ecdc89403390.jpg)

- 集群网络是用户的 VPC，节点和容器子网属于该 VPC。
- 容器子网可以选择多个 VPC 内的子网。
- 可设置是否开启固定 IP。您可参考 [固定 IP 模式使用说明](https://cloud.tencent.com/document/product/457/50358)。

### IP 地址管理原理

#### 非固定 IP 模式

![](https://qcloudimg.tencent-cloud.cn/raw/f506c98ab54db316e468f88f5cca8b96.png)

- TKE 组件在每个节点维护一个可弹性伸缩的 IP 池。已绑定的 IP 数量将被维持在 **Pod 数量 + 最小预绑定数量**及 **Pod 数量 + 最大预绑定数量**之间：
	- 当**已绑定数量 < Pod 数量 + 最小预绑定数量**时，会绑定 IP 使得**已绑定数量 = Pod 数量 + 最小预绑定数量**。
	- 当**已绑定数量 > Pod 数量 + 最大预绑定数量**时，会定时释放IP（约2分钟一次），直到**已绑定数量 = Pod 数量 + 最大预绑定数量**。
	- 当**最大可绑定数量 < 当前已绑定数量**时，会直接释放多余的空闲 IP，使得**已绑定数量 = 最大可绑定数量**。
- 共享网卡的 Pod 创建时，从节点可用 IP 池中随机分配一个可用 IP。
- 共享网卡的 Pod 销毁时，IP 释放回节点的 IP 池，留给下一个 Pod 使用，不会在 VPC 侧释放（删除）。
- IP 和网卡的分配和释放目前基于**最少网卡原则**，即保证使用的弹性网卡尽量的少：
	- **IP 分配给 Pod**：优先分配已分配 IP 数量最多的网卡上的 IP
	- **IP 释放**：优先释放已分配 IP 数量最少的网卡上的 IP
    - **新网卡绑定**：若当前已绑定网卡 IP 配额用尽或网卡所在的子网 IP 用完，则申请新网卡绑定 IP
	- **网卡释放**：若已绑定网卡的辅助 IP 都已解绑，且不再需要新增 IP，则解绑并删除网卡
- 节点会注册扩展资源 `tke.cloud.tencent.com/eni-ip`，资源的可分配数(Allocatable) 为实际的已绑定 IP 资源数，总量(Capacity) 为节点可绑定的 IP 资源上限。因此，当 Pod 调度到某节点失败时，说明节点的 IP 已用尽。
- 新网卡的子网选择：新网卡优先选择可用 ip 最多的子网。
- 各节点最大可绑定 IP = 最大绑定网卡数 * 单网卡可绑定 IP 数
- 当前**最小预绑定数量**和**最大预绑定数量**的默认值为5

#### 固定 IP 模式
- TKE 网络组件维护一个集群维度的可用 IP 池。
- 集群每新增一个节点，将申请一张弹性网卡。不会提前绑定任何辅助 IP，但会在网络组件内给此节点预留网卡 IP 配额数量的 IP。
- 新建一个使用 VPC-CNI 模式的 Pod 时，IPAMD 组件会依据节点绑定网卡所在的子网分配1个 IP，然后才会即时申请绑定该辅助 IP 到相应节点的网卡上。
- Pod 销毁时，IP 地址回归集群的可用 IP 池，并触发网卡解绑 IP，IP 地址将释放回 VPC 子网内。
- 固定 IP 的 Pod 的 IP 仅在 TKE 集群内部保留，保证下一次创建同名 Pod 的时候仍使用这个 IP。
- 节点删除时，将释放网卡占用的 IP 资源。
- 多容器子网的情况下，网卡优先分配到可用 IP 数量最多且能完全满足网卡 IP 配额需求的子网内，若没有完全满足需求的子网，则节点绑定网卡失败。

### 多网卡数据面原理

>! 当前仅非固定 IP 模式支持多网卡。

当节点绑定了多张网卡时，Pod 发出的网络包遵循策略路由转发到对应的网卡上：
- 在节点上执行 `ip link` 可看到节点所有的网络设备信息，通过弹性网卡的 mac 地址比对，可知道其中弹性网卡对应的网络设备。一般情况下，`eth0`为主网卡，`eth1`、`eth2`等为辅助弹性网卡：
![](https://qcloudimg.tencent-cloud.cn/raw/b4b357d3b4991195c8a618e817bc8c81.jpg)

- 在节点上执行 `ip rule` 可看到策略路由表的信息，TKE 网络组件通过弹性网卡的 `<link index>+2000` 得到路由表号，绑定了对应网卡 IP 的 Pod 网络包都将转发到该路由表，如此例中，eth1 对应的路由表即为 2003，eth2 对应的路由表即为 2010：
![](https://qcloudimg.tencent-cloud.cn/raw/0c3a14cb4402a5c108ac6f9b1f72f5cf.png)

- 对应的路由表则设置了到对应网卡的默认路由，节点上执行 `ip route show table <id>` 可查看：
![](https://qcloudimg.tencent-cloud.cn/raw/881653493b4188b34a78e3b3e769adc6.png)

而欲发送给 Pod 的网络包到达节点时，同样遵循策略路由，直接通过主路由表发送给 Pod 的 Veth 网卡。


## 使用方法


使用 VPC-CNI 需要确保 `rp_filter` 处于关闭状态。可参考以下代码示例：
``` bash
sysctl -w net.ipv4.conf.all.rp_filter=0
# 假设 eth0 为主网卡
sysctl -w net.ipv4.conf.eth0.rp_filter=0
```
>! `tke-eni-agent` 组件自动设置节点的内核参数。若您自己有维护内核参数且打开 `rpfilter`，则会导致网络不通。


### 开启 VPC-CNI

#### 创建集群时开启 VPC-CNI

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击左侧导航栏中**集群**。
2. 在“集群管理”页面，单击集群列表上方的**新建**。
3. 在“创建集群”页面，在容器网络插件中选择 “VPC-CNI”。如下图所示：
![](https://main.qcloudimg.com/raw/d3d84cfc2ede5be4c67d698c03b18c6a.png)

>? 默认情况下，VPC-CNI 模式**不支持固定 Pod IP 能力**，且该能力仅支持在 [创建集群](https://cloud.tencent.com/document/product/457/32189) 时设置。如需为集群开启支持固定 Pod IP，请参见 [固定 IP 模式使用说明](https://cloud.tencent.com/document/product/457/50358)。




#### 为已有集群开启 VPC-CNI
创建集群时选择 Global Router 网络插件，后续在集群基本信息页面开启 VPC-CNI 模式（两种默认混用）。
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，单击左侧导航栏中**集群**。
2. 在“集群管理”页面，选择需开启 VPC-CNI 的集群 ID，进入集群详情页。
3. 在集群详情页面，选择左侧**基本信息**。
4. 在集群“基本信息”页面的集群信息模块，在 VPC-CNI 字段中单击开启。
5. 在弹出窗口中选择子网，并确认 IP 回收策略。如下图所示：
![](https://main.qcloudimg.com/raw/cda22252025915b5bb264570c924958a.png)
>! 
>- 针对固定 IP 场景，启用 VPC-CNI 后需要设置 IP 回收策略，即设置 Pod 销毁后需要退还 IP 的时长。
>- 非固定 IP 的 Pod 销毁后可立即释放 IP（非释放回 VPC，释放回容器管理的 IP 池），不受此设置的影响。
6. 单击**提交**，即可完成为已有集群开启 VPC-CNI。

### 关闭 VPC-CNI
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，单击左侧导航栏中**集群**。
2. 在“集群管理”页面，选择需开启 VPC-CNI 的集群 ID，进入集群详情页。
3. 在集群详情页面，选择左侧**基本信息**。
4. 在集群“基本信息”页面的集群信息模块，在 VPC-CNI 字段中单击关闭。
5. 在弹出窗口中选择**提交**，即可关闭 VPC-CNI。









