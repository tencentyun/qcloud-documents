腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。
>

## 路由配置
``` 
# 配置物理接口
interfaces <interface_number>
description <interface_desc>
undo shutdown
speed <interface_speed>
duplex full
undo negotiation auto
commit

# 配置虚拟通道
interfaces <interface_number>.<subinterface_number>
description <subinterface_desc>
vlan-type dot1q <subinterface_vlanid>
ip address <subinterface_ipaddress> <subinterface_netmask>
commit

# 设置静态路由
# 设置全局静态路由
ip route-static <ip-address> <mask | mask-length> <nexthop-address>//<ip-address>为用户需要访问 Tencent 网络服务的目的网段
例如:ip route-static 172.16.0.192 255.255.255.192 10.128.152.1

# 设置 VRF 下用户访问 Tencent 静态路由
ip route-static <vpn-instance vpn-instance-name> <ip-address> <mask | mask-length> <nexthop-
address>
例如:ip route-static vpn-instance GLOBAL 9.0.0.0 255.0.0.0 10.128.152.1
Commit
```
