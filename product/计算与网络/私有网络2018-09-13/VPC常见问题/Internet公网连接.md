#Internet/公网连接
####没有公网 IP 地址的实例（云主机、数据库）如何访问 Internet？
没有公网IP的实例可以通过 NAT 网关/ 公网网关访问 Internet。

- [NAT网关](https://cloud.tencent.com/document/product/552) ，通过创建 NAT 网关和配置相关子网所关联的路由表，那么子网内的实例即可访问 Internet。
- [公网网关](https://cloud.tencent.com/document/product/215/20078) ，没有外网 IP 但需要进行 Internet 访问的云服务器可通过位于不同子网的公网网关来访问 Internet。

####什么是公网网关？
公网网关是开启了转发功能的云服务器，无外网 IP 但需进行 Internet访问的云服务器可通过位于非相同子网公网网关转发来访问 Internet。更多信息请参见[公网网关概述](https://cloud.tencent.com/document/product/215/11119#.E7.AE.80.E4.BB.8B)
 > 注意：公网网关有一定使用限制，公网网关子网和普通子网不能关联同一个路由表，需要新建一个独立的网关路由表关联网关子网。

####如果我的云服务器有公网IP/弹性公网IP，所在子网又关联了NAT网关，将如何访问Internet?
如果一台云服务器有公网IP/弹性公网IP，同时又在关联了NAT网关的子网内（路由表中设置了该子网访问Internet流量的下跳是NAT网关），那么默认该云服务器访问Internet的流量会全部通过NAT网关实现。

####云服务器通过公网网关、NAT网关访问Internet，流量是否会双份收取？
不会，网络费用只收取一份。通过公网网关、NAT 网关访问 Internet，收取的是公网网关和 NAT 网关的网络费用。

