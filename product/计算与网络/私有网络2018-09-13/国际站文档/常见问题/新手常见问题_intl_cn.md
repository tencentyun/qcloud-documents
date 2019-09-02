## 1. VPC（私有网络） 有哪些组成部分？
腾讯云 VPC 由多个不同的服务组成，它们对拥有私有网络的客户而言并不陌生：
**1)  软件定义网络**：您可以自定义私有网络网段、子网网段和路由策略：
- **私有网络 (VPC)** 是腾讯云中逻辑隔离的虚拟网络。从所选的范围内定义 VPC 的 IP 地址空间。
- **子网**是 VPC 的 IP 地址范围内的一个区段，其中可放入各组隔离的资源。
- ** 路由器**包含一系列路由策略，用于定义私有网络内每个子网的网络流量走向。


**2)  Internet 连接**：灵活、高性能的Internet连接方式包含以下三中：
- **NAT 网关** 是一项高度可用的托管网络地址转换 (NAT) 服务，可便于私有子网中的资源访问 Internet。
- **弹性IP**（EIP）是可以独立申请的公网IP地址，用于公网访问，支持与实例（如：云主机、NAT 网关）的动态绑定和解绑，主要用于屏蔽实例故障。
- **公网网关**是一种云主机，具备转发Internet和私有网络之间流量的能力，没有外网IP但需要进行Internet访问的云服务器可通过公网网关来访问Internet。

**3)  部署混合云**连接您的数据中心和VPC。
- **VPN连接**是一种通过公网加密通道连接您的IDC和私有网络的方式，包括三个组成部分：VPN网关、对端网关、VPN通道。
- **专线接入**是一种快速连接腾讯云与本地数据中心的方法，您可以通过一条物理专线一次性打通位于多地域的腾讯云计算资源，包括三个组成部分：物理专线、专线通道、 专线网关：

**4) 云上资源互通**可以实现与其它VPC和基础网络中的资源通信。
- **对等连接**：对等连接是一种连接两个私有网络的服务，支持跨账户和跨地域的私有网络之间流量互通，两端的云主机和云数据库等资源可以相互访问
- **基础网络互通**：是指将基础网络内的云服务器关联至指定私有网络的服务，可以打通基础网络中的云服务器与私有网络之间的网络通信

**5)  安全控制**
- **安全组**：是一种有状态的包过滤虚拟防火墙，它用于控制单台或多台云服务器的出入流量，可以精确协议和端口维度。
- **网络ACL**：是一个子网级别的无状态可选包过滤虚拟防火墙，用于控制进出子网的数据流，可以精确到协议和端口维度。



## 2. 如何开始使用 VPC？
您可以选择在腾讯云控制台或者利用云API使用VPC。
- [**控制台** 快速使用向导](https://cloud.tencent.com/document/product/215/8119)
- [**API** 快速使用向导](https://cloud.tencent.com/doc/api/245/5157)

## 3. VPC是否可以与基础网络 / 公网 / 其它VPC（跨地域跨账号）/ 我的数据中心通信？
均可以，您的需求和对等功能如下表所示：

| 用户需求 | VPC对应功能 | 
|---------|---------|
| VPC与基础网络内云主机通信 |  [基础网络互通](https://cloud.tencent.com/doc/product/215/5002)|
|访问公网|[弹性IP](https://cloud.tencent.com/doc/product/215/4958) / [NAT网关](https://cloud.tencent.com/doc/product/215/4975)（高性能 ）/ [公网网关](https://cloud.tencent.com/doc/product/215/4972) |
|其它VPC|[对等连接](https://cloud.tencent.com/doc/product/215/5000)（支持跨地域 和 跨账号） |
|我的数据中心|[VPN连接 ](https://cloud.tencent.com/doc/product/215/4956)/[ 专线接入](https://cloud.tencent.com/doc/product/215/4976) |


## 4. 我可以创建多少个 VPC、子网、路由表、公网网关、NAT网关、对等连接、VPN网关、VPN通道、网络ACL？
[查看VPC内的资源配额详情](https://cloud.tencent.com/doc/product/215/537)，如果您有更多的需要，请填工单申请。

## 5. 基础网络和 VPC 有什么区别？
VPC能满足基础网络能提供的所有功能，不额外收费。
VPC能满足更多网络自定义需求，[具体可查看基础网络与VPC的区别详情](https://cloud.tencent.com/doc/product/215/535#.E9.80.89.E6.8B.A9.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C-or-.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C.EF.BC.9F)。


## 6. 我有一个 VPC ，只想让里面部分云主机通过网关出公网，该怎么配置？
将需要访问公网的云主机放于某个子网内，并在该子网所绑定的路由表上配置路由策略，让目的地址为公网的数据包通过网关访问。具体操作步骤如下：
1) **[创建子网](https://cloud.tencent.com/doc/product/215/4927#.E6.96.B0.E5.A2.9E.E5.AD.90.E7.BD.91)**，并将需要访问公网的云主机放于该子网：在[子网控制台](https://console.cloud.tencent.com/vpc/subnet)内购买云主机 / 在[云主机介绍页](https://cloud.tencent.com/product/cvm.html) 购买网络配置中选择该子网。
2) **购买对应的网关设备**，腾讯云VPC内的可以访问公网的网关设备分为两种：[NAT网关](https://cloud.tencent.com/doc/product/215/4975)和[公网网关](https://cloud.tencent.com/doc/product/215/4972)，[点击查看它们的区别](https://cloud.tencent.com/doc/product/215/4975#nat.E7.BD.91.E5.85.B3.E5.92.8C.E5.85.AC.E7.BD.91.E7.BD.91.E5.85.B3.E7.9A.84.E5.8C.BA.E5.88.AB)，您可以需要根据业务需要购买对应的网关设备。[无外网 IP云主机通过公网网关访问外网](https://cloud.tencent.com/doc/product/215/4972#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97)操作指南 / [使用 NAT 网关访问 Internet](https://cloud.tencent.com/doc/product/215/4975#.E4.BD.BF.E7.94.A8-nat-.E7.BD.91.E5.85.B3.E8.AE.BF.E9.97.AE-internet)操作指南。

## 7. 我有一个 VPC ，是否可以在不同可用区创建云主机，该如何操作？比如：在广州二区和广州三区创建云主机。
可以，但是有两个前提条件：
1) 只能在该VPC所在地域的可用区下创建。比如，您的VPC所属地域是广州，那么您可以创建广州二区和三区的云主机，但是您不可以在该VPC中同时创建广州二区和北京一区的云主机，[点击查看地域和可用区分布详情](https://cloud.tencent.com/doc/product/215/4927#.E5.8F.AF.E7.94.A8.E5.8C.BA.EF.BC.88zone.EF.BC.89)
2) 在某可用区创建云主机，必须先创建该可用区的子网。

在不同可用区创建云主机具体操作步骤如下：
1) 在该VPC下的**不同**可用区[创建子网](https://cloud.tencent.com/doc/product/215/4927#.E6.96.B0.E5.A2.9E.E5.AD.90.E7.BD.91)。
2) 创建云主机。在[子网控制台](https://console.cloud.tencent.com/vpc/subnet)内购买云主机 / 在[云主机介绍页](https://cloud.tencent.com/product/cvm.html) 购买网络配置中选择**不同可用区**的子网。

## 8.云主机(CVM) / 内网负载均衡(LB) / 云数据库(CDB)是否支持修改内网IP？
云主机主网卡的主内网IP支持修改，辅助网卡的主内网IP不支持修改，[点击查看操作指南](https://cloud.tencent.com/doc/product/215/6508#4.-.E5.A6.82.E4.BD.95.E4.BF.AE.E6.94.B9.E4.BA.91.E4.B8.BB.E6.9C.BA.E5.86.85.E7.BD.91ip.EF.BC.9F)。
内网负载均衡(LB) / 云数据库(CDB)不支持修改内网IP。