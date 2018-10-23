### 没有公网 IP 地址的实例（云服务器、数据库）如何访问 Internet？
没有公网 IP 的实例可以通过 NAT 网关/公网网关访问 Internet。
- [NAT网关](https://cloud.tencent.com/document/product/552) 
通过创建 NAT 网关、配置相关子网所关联的路由表，子网内的实例即可访问 Internet。
- [公网网关](https://cloud.tencent.com/document/product/215/20078) 
没有外网 IP 的云服务器，可通过位于不同子网的公网网关来实现 Internet 的访问。

### 什么是公网网关？
公网网关是开启了转发功能的云服务器，无外网 IP 但需进行 Internet 访问的云服务器，可通过位于不同子网的公网网关来访问 Internet。更多信息，请参见 [公网网关概述](https://cloud.tencent.com/document/product/215/11119#.E7.AE.80.E4.BB.8B)。
 >**注意：**
 >公网网关子网和普通子网不能关联同一个路由表，需要新建一个独立的网关路由表来关联网关子网。详情请参见 [公网网关使用限制](https://cloud.tencent.com/document/product/215/20078#.E4.BD.BF.E7.94.A8.E9.99.90.E5.88.B6)。

### 如果云服务器有公网 IP/EIP，所在子网又关联了 NAT 网关，将如何实现 Internet 的访问?
如果一台云服务器有公网 IP/EIP（弹性公网 IP），同时，子网又关联了 NAT 网关（即路由表中设置了该子网访问 Internet 流量的下一跳是 NAT 网关），那么，默认该云服务器访问 Internet 的流量会全部通过 NAT 网关实现。

### 云服务器通过公网网关、NAT 网关访问 Internet，网络费用是否会收取双份？
不会，网络费用只收取一份。通过公网网关、NAT 网关访问 Internet，收取的是公网网关和 NAT 网关的网络费用。

