腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。
>

## 路由配置
``` 
# 配置物理接口
interfaces <interface_number>
description <interface_desc>
port link-mode route
undo shutdown
speed <interface_speed>
duplex full

# 配置三层子接口
interface  interface-number.subnumber
description <vlan_description>
dot1q termination vid <vlanid>
ip address <subinterface_ipaddress> <subinterface_netmask>

# 配置静态路由NQA探测
nqa entry <admin-name> < test-name>
type icmp-echo  //默认测试类型
destination-address  x.x.x.x（nexthop-address ）//探测地址
interval seconds 2 //探测间隔
frequency <value> //探测实例执行间隔
history-record enable
probe count  <value> //每次探测包数
probe timeout <value> //超时时间 

#配置track 
track <number> nqa entry  <admin-name>< test-name> //track关联nqa

# 设置静态路由
ip route-static <Destination_IP_address> <Mask_of_the-IP_address> <VLAN_interface> track <number> 

```
