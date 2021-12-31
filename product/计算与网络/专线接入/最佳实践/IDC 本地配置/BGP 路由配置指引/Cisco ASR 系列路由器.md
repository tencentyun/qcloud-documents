腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。

## 路由配置
``` 
# 配置物理接口
interfaces <interface_number>
description <interface_desc>
no shutdown
speed <interface_speed>
duplex full
no negotiation auto
commit

# 配置虚拟通道
interfaces <interface_number>.<subinterface_number>
description <subinterface_desc>
encapsulation dot1q <subinterface_vlanid>
ipv4 address <subinterface_ipaddress> <subinterface_netmask>
bfd interval <value> min_rx <value> multiplier <value> //BFD 参数
commit

# 设置 eBGP
router bgp <as_number>
#bgp router-id <router_id>
neighbor <bgp_peer_address>
remote-as <bgp_peer_as_number>
password encrypted <bgp_auth_key>
description <bgp_peer_desc>
remote-as <bgp_peer_as_number> fall-over bfd //设置 BGP 联动 BFD
commit

```
