腾讯云专线通过物理专线将腾讯云和用户 IDC连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。（推荐使用三层子接口对接腾讯云侧）
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。
>

## 路由配置
``` 
# 设置物理接口
interfaces <interface_number>
description <interface_desc>
undo portswitch
undo shutdown
speed <interface_speed>
duplex full
undo negotiation auto
commit

# 设置虚拟通道(三层子接口)
interface  <interface_number>.subinterface-number
description <subinterface_desc>
dot1q termination vid <vlanid>
ip address <subinterface_ipaddress> <subinterface_netmask>

# 设置 eBGP 
bgp <as_number>
#router-id <route_id>
peer <bgp_peer_address> as-number <bgp_peer_as_number>
peer <bgp_peer_address> password cipher <bgp_auth_key>
peer <bgp_peer_address> description <bgp_desc>
ipv4-family unicast
peer <bgp_peer_address> enable
commit

# 设置 eBGP 的 BFD 配置
bgp <as_number>
router-id <route_id>
peer <bgp_peer_address> bfd min-tx-interval <time value> min-rx-interval <time value> detect-multiplier <value>

```
