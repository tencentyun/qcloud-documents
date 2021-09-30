腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。
>

## 路由配置
``` 
# 配置 VLAN
vlan <vlanid>
description <vlan_description>

# 设置物理接口
interface <interface_name>
port link-mode bridge
description <XXXX>
port link-type trunk
undo port trunk permit vlan 1
port trunk permit vlan <vlanid>
speed <interface_speed>
duplex full

# 配置 vlan-interface
interface Vlan-interface<vlanid>
description <vlan_description>
ip address <subinterface_ipaddress> <subinterface_netmask>

# 设置静态路由
ip route-static <Destination_IP_address> <Mask_of_the-IP_address> <VLAN_interface>
```
