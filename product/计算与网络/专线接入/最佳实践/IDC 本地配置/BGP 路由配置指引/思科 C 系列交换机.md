腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。（推荐使用三层子接口对接腾讯云侧）

>!本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。

## 路由配置
``` 
# 配置物理接口
interfaces <interface_number>
description <interface_desc>
no shutdown
no switchport
speed <interface_speed>
duplex full
no negotiation auto
end

# 配置三层子接口
interface  interface-number.subnumber
description <vlan_description>
encapsulation dot1q <vlanid>
ip address <subinterface_ipaddress> <subinterface_netmask>
bfd interval <value> min_rx <value> multiplier <value> //BFD参数
end

# 设置 eBGP 
router bgp <as_number>
bgp router-id <router_id>
neighbor <bgp_peer_address> remote-as <bgp_peer_as_number>
neighbor <bgp_peer_address> password encrypted <bgp_auth_key>
neighbor <bgp_peer_address> description <bgp_peer_desc>
neighbor <bgp_peer_address> activate
neighbor <bgp_peer_address> fall-over bfd single-hop //设置 BGP 联动 BFD
```
