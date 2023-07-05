通过在本地 IDC 中心的网络交换机上启动 BGP 路由协议，以及在腾讯云专线网关上配置双向转发检测（BFD），实现本地 IDC 与专有网络之间的路由快速收敛。

## 背景信息
![](https://qcloudimg.tencent-cloud.cn/raw/1ed97d1e2029f35759a4a7a8fea17fe7.png)
>! 静态路由对接场景下，推荐静态路由 +BFD/NQA 实现路由收敛。
>
- 物理专线分别连接 IDC 侧交换机与腾讯云交换机的三层网络子接口，打通 IDC 与 腾讯云网络。 
- 通过 VPC/CCN 实现资源互访。
- 通过 BGP+BFD/NQA 实现路由收敛。

## 前提条件
- 已创建腾讯云 VPC，具体操作请参见[ 快速搭建 IPv4 私有网络](https://cloud.tencent.com/document/product/215/30716)。
- 已[ 申请物理专线](https://cloud.tencent.com/document/product/216/48586) ，并完成建设。


## 配置指引
### 步骤一：创建专线网关
详细操作，请参见 [创建专线网关](https://cloud.tencent.com/document/product/216/19256)。

### 步骤二：创建专用通道
物理专线接入方式不同，则在其上创建的通道不同。
- 使用自主独占型物理专线创建的通道为独占型专用通道，即独占专用通道，适用于大带宽接入、业务独享等场景，创建详情，请参见 [独享专用通道](https://cloud.tencent.com/document/product/216/74769)。
- 使用合作伙伴与腾讯预连接的物理专线创建的专用通道为共享型专用通道，即共享专用通道，适用于无大带宽入云需求、上云时间要求较短的场景，创建详情，请参见 [共享专用通道](https://cloud.tencent.com/document/product/216/74570)。

### 步骤三：配置健康检查
详细操作，请参见 [配置健康检查](https://cloud.tencent.com/document/product/216/56667)。


### 步骤四：[IDC 本地配置](https://cloud.tencent.com/document/product/216/61998) 
本文以华为 CE 交换机为例，其他本地配置请参见[ IDC 本地配置](https://cloud.tencent.com/document/product/216/61998)  。
如果您因特殊原因无法实现三层子接口对接，只能通过二层子接口对接，您可以参见方式二。
- **（推荐）方式一：三层子接口+BGP**：
``` 
# 设置三层对接子接口
interfaces
<interface_number>.<sub_number>
description <interface_desc>
dot1q termination vid <vlan id>
ip address <subinterface_ipaddress>
<subinterface_netmask>
speed <interface_speed>
duplex full
undo negotiation auto
commit
# 设置 eBGP 
bgp <as_number>
router-id <route_id>
peer <bgp_peer_address> as-number
<bgp_peer_as_number>
peer <bgp_peer_address> password cipher
<bgp_auth_key>
peer <bgp_peer_address> description
<bgp_desc>
ipv4-family unicast
peer <bgp_peer_address> enable
commit
# 设置 eBGP 的BFD配置
bgp <as_number>
router-id <route_id>
peer <bgp_peer_address> bfd min-tx-interval
1000 min-rx-interval 1000 detect-multiplier 3
```


- **方式二：二层Vlanif口+BGP（二层接口建议关闭 STP 生成树协议）**：
``` 
# 设置物理接口
interfaces
<interface_number>
description
<interface_desc>
port link-type
trunk
undo shutdown
speed
<interface_speed>
duplex full
undo negotiation
auto
stp disable ** (****关闭****stp****生成树协议****)**
commit
# 设置虚拟通道
vlan
<subinterface_vlanid>
description
<subinterface_desc>
#设置逻辑接口
interface Vlanif
<subinterface_vlanid>
description <subinterface_desc>
ip address
<subinterface_ipaddress> <subinterface_netmask>
#配置接口 VLAN
interfaces
<interface_number>
port trunk
allow-pass vlan <subinterface_vlanid>
commit
# 设置 eBGP 
bgp
<as_number>
router-id
<route_id>
peer
<bgp_peer_address> as-number <bgp_peer_as_number>
peer
<bgp_peer_address> password cipher <bgp_auth_key>
peer
<bgp_peer_address> description <bgp_desc>
ipv4-family
unicast
peer
<bgp_peer_address> enable
# 设置 eBGP 的BFD配置
bgp <as_number>
router-id <route_id>
peer <bgp_peer_address> bfd min-tx-interval
1000 min-rx-interval 1000 detect-multiplier 3
commit
```



## 关于 Keepalive 及 holdtime 参数配置指南
对等体间建立了 BGP 连接后，会定时向对端发送 Keepalive 消息，以维持 BGP 连接的有效性。如果路由器在设定的连接保持时间（Holdtime）内未收到对端的 Keepalive 消息或任何其它类型的报文，则认为此 BGP 连接已中断，从而中断此 BGP 连接。

keepalive-time 值和 hold-time 值是通过双方协商来确定。其中，取双方 Open 报文中的 hold-time 较小值为最终的 hold-time 值；取**协商的 hold-time 值 ÷ 3**和本地配置的 keepalive-time 值中较小者作为最终 keepalive-time 值。
接入时推荐配置的 Holdtime 时间60 x 3=180秒（大部分厂商的缺省值）。

如果配置的保持时间小于30秒，链路正常情况下也可能会造成邻居会话的中断，需要进行链路抖动检测，建议通过使用 BFD 来提高收敛性能。
