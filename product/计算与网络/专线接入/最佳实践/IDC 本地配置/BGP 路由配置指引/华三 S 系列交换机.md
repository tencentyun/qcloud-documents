腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。（推荐使用三层子接口对接腾讯云侧）

>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。

## 路由配置
``` 
# 配置物理接口
interfaces <interface_number>
description <interface_desc>
port link-mode route
undo shutdown
speed <interface_speed>
duplex full

# 配置三层子接口
interface  interface-number.subnumber
description <vlan_description>
dot1q termination vid <vlanid>
ip address <subinterface_ipaddress> <subinterface_netmask>
bfd min-transmit-interval <value> //配置 BFD 参数
bfd min-receive-interval <value>  //配置 BFD 参数
bfd detect-multiplier <value>  //配置 BFD 参数


# 设置 eBGP
bgp <as_number>
#router-id <route_id>
peer <bgp_peer_address> as-number <bgp_peer_as_number>
peer <bgp_peer_address> password cipher <bgp_auth_key>
peer <bgp_peer_address> description <bgp_desc>

# 设置 eBGP 的 BFD 配置
peer <bgp_peer_address> bfd
```
