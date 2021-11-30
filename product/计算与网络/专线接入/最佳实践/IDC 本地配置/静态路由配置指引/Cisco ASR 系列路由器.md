腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。
>

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
commit

# 配置IP SLA（NQA）
ip sla <operation-number>
icmp-echo x.x.x.x<nexthop_address> source-ip x.x.x.x <source_address>
frequency <value> //设置探测频率
timeout <value> //设置超时时间
ip sla schedule <operation-number> life forever start-time now
en

# 配置TRACK 关联 IP SLA
track <operation-number> ip sla <operation-number> reachability
end

# 设置静态路由
router static
vrf <vrf-name> //如果没有指定 VRF，静态路由在 default VRF 下
  address-family <ipv4 | ipv6> unicast
  <ip-prefix/netmask> <next_hop_ip> <interface_number> <description_text> <distance> <tag tag_value> track <operation-number>
commit

```
