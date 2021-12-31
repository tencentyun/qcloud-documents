腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。
>

## 路由配置
``` 
# 配置物理接口
set interfaces <interface_number> description <interface_desc>
set interfaces <interface_number> vlan-tagging
set interfaces <interface_number> link-mode full-duplex
set interfaces <interface_number> speed <interface_speed> //需要看模块是否支持
set interfaces <interface_number> gigether-options no-auto-negotiation //建议结合上一条命令
使用
commit

# 配置虚拟通道
set interfaces <interface_number> unit <subinterface_number> vlan-id <subinterface_vlanid>
set interfaces <interface_number> unit <subinterface_number> description <subinterface_desc>
set interfaces <interface_number> unit <subinterface_number> family inet address
<subinterface_ipaddress>/<subinterface_netmask>
commit

# 设置静态路由
# 全局下配置到用户 IP 的静态路由
set routing-options static route <customer_prefix/mask> next-hop <customer_interface_ip>
# 设置静态路由联动 BFD，RPM 模式可咨询设备商，此处以 BFD 为例
set routing-options static route <customer_prefix/mask>bfd-liveness-detection minimum-interval <value> 

例如:set routing-options static route 1.1.1.0/24 next-hop 192.168.1.2 bfd-liveness-detection minimum-interval 1000 

# VRF 下配置到用户 IP 的静态路由:
set routing-instances <vrf_name> routing-options static route <customer_prefix/mask> next-hop
<customer_interface_ip>
例如:set routing-instances cap routing-options static route 1.1.1.0/24 next-hop 192.168.1.2
commit

```
