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

# 设置 eBGP 
set protocols bgp group ebgp type external //定义协议组，ebgp 名称可以更换
set protocols bgp group ebgp neighbor <bgp_peer_address> loacal-as <as_number> //如果不配
置，默认使用设备全局(set routing-options autonomous-system XX)
set protocols bgp group ebgp neighbor <bgp_peer_address> peer-as <bgp_peer_as_number>
set protocols bgp group ebgp neighbor <bgp_peer_address> authentication-key <bgp_auth_key>
set protocols bgp group ebgp neighbor <bgp_peer_address> description <bgp_peer_desc>
commit

# 设置 eBGP 的 BFD 配置
set protocols bgp group ebgp neighbor <bgp_peer_address> bfd-liveness-detection minimum-interval <value>
```
