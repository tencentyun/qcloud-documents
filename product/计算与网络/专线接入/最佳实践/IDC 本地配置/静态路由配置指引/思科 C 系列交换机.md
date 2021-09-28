腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。

## 路由配置
``` 
# 配置物理接口
interfaces <interface_number>
description <interface_desc>
switchport mode trunk
no shutdown
speed <interface_speed>
duplex full
no negotiation auto

# 配置虚拟通道
vlan <subinterface_vlanid>
description <subinterface_desc>
!
interface Vlan <subinterface_vlanid>
description <subinterface_desc>
ip address <subinterface_ipaddress> <subinterface_netmask>
!
interfaces <interface_number>
switchport trunk allowed vlan <subinterface_vlanid> add

# 设置静态路由
ip route <ip_prefix> <netmask> <interface_number | vlan_id> <next_hop_ip> <name
nexthop_name> <distance> <tag tag_value>
```
