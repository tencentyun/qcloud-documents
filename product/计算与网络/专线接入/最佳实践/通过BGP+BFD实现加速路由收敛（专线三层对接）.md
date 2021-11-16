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
### 步骤一：[创建专线网关](https://cloud.tencent.com/document/product/216/19256) 
1. 在左侧导航栏单击**专线网关**。
2. 在**专线网关**页面上方选择地域和私有网络，然后单击**+新建**。
![](https://main.qcloudimg.com/raw/637f6131afd200c2c83b7c3091c2cee4.png)
3. 在**创建专线网关**对话框中配置网关详情，完成后单击**确定**。
![](https://main.qcloudimg.com/raw/8bd22fc9a503c1dbd09d5c5bd0b75158.png)

### 步骤二：[创建专用通道](https://cloud.tencent.com/document/product/216/19250) 
1. 登录 [专线接入 - 专用通道](https://console.cloud.tencent.com/dc/dcConn) 控制台。
2. 在**专用通道**页面上方单击**+新建**，并配置名称、专线类型、接入网络、地域、关联的专线网关等基名称本配置，完成后单击**下一步**。
 <img src="https://main.qcloudimg.com/raw/d08f49d3be4b3513c0ab663cdda8512a.png" width="70%">
3. 在**高级配置**页面配置以下参数，然后单击**确定**。
 <img src="https://qcloudimg.tencent-cloud.cn/raw/324ab047e029238098ec728a2b2b4950.png" width="70%">


### 步骤三：[配置健康检查](https://cloud.tencent.com/document/product/216/56667)
1. 在**专用通道**页面，单击创建好的通道名称。
 ![](https://main.qcloudimg.com/raw/2cb0d8961eb1c91772db03439fbe3ee4.png)
2. 在通道详情页的**高级通道**页签中，单击**路由模式**右侧**编辑**。
3. 在**健康检查**所在行开启该功能。
4. 配置健康检查参数，并单击**保存**。</br>
 <img src="https://qcloudimg.tencent-cloud.cn/raw/99c5541f59d138caf1968ae7a390a6af.png" width="70%">

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
