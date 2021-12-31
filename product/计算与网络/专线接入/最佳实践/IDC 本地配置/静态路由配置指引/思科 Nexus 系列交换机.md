腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。（推荐使用三层子接口对接腾讯云侧）
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。
>

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
end

# 配置 IP SLA（NQA）
ip sla <operation-number>
icmp-echo x.x.x.x<nexthop_address> source-ip x.x.x.x <source_address>
frequency <value> //设置探测频率
timeout <value> //设置超时时间
ip sla schedule <operation-number> life forever start-time now
end

# 配置 TRACK 关联 IP SLA
track <operation-number> ip sla <operation-number> reachability
end

# 设置静态路由并联动 track
ip route <ip_prefix/netmask> <interface_number | vlan_id> <next_hop_ip> <name nexthop_name><distance> <tag tag_value> track <operation-number>

```
