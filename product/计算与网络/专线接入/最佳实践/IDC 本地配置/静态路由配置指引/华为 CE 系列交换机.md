腾讯云专线通过物理专线将腾讯云和用户 IDC 连接，用户在腾讯云侧配置专线网关、专用通道等完成后，还需要在本地 IDC 进行路由配置。（推荐使用三层子接口对接腾讯云侧）
>?本文仅介绍与腾讯云专线相关的用户本地路由配置项，其他不做介绍，如需了解其他内容请查阅本地路由器文档或者联系各自路由器商咨询。
>

## 路由配置
``` 
# 设置物理接口
interfaces <interface_number>
description <interface_desc>
undo portswitch
undo shutdown
speed <interface_speed>
duplex full
undo negotiation auto
commit

# 设置虚拟通道(三层子接口)
interface  <interface_number>.subinterface-number
description <subinterface_desc>
dot1q termination vid <vlanid>
ip address <subinterface_ipaddress> <subinterface_netmask>

# 配置静态路由NQA探测
nqa test-instance <admin-name>< test-name>
 test-type icmp  //默认测试类型
 destination-address  x.x.x.x（nexthop-address ）//探测地址
 interval seconds <value> //探测间隔
 timeout <value> //超时时间
 probe-count <value> //每次探测包数
 frequency <value> //探测实例执行间隔
 start now


# 设置静态路由
# 设置全局静态路由
ip route-static <ip-address> <mask | mask-length> <nexthop-address>track nqa  <admin-name>< test-name>//<ip-address>为用户需
要访问 Tencent 网络服务的目的网段
例如:ip route-static 172.16.0.192 255.255.255.192 10.128.152.1 track nqa user test

# 设置 VRF 下用户访问 Tencent 静态路由
ip route-static <vpn-instance vpn-instance-name> <ip-address> <mask | mask-length> <nexthop-
address>track nqa  <admin-name>< test-name>
例如:ip route-static vpn-instance GLOBAL 9.0.0.0 255.0.0.0 10.128.152.1 track nqa user test
commit

```
