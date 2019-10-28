腾讯云私有网络（Virtual Private Cloud，VPC）是一块您在腾讯云上自定义的逻辑隔离网络空间，与您在数据中心运行的传统网络相似，托管在腾讯云私有网络内的是您在腾讯云上的服务资源，包括 [云服务器](https://cloud.tencent.com/doc/product/213/495)、[负载均衡](https://cloud.tencent.com/doc/product/214/524)、[云数据库](https://cloud.tencent.com/doc/product/236) 等。
>?每个私有网络内的服务资源默认内网互通，不同私有网络之间内网默认不通，如果您需要与您账户下或其他账户下的私有网络子网互通，需要通过 [对等连接](https://cloud.tencent.com/document/product/553) 和 [云联网](https://cloud.tencent.com/document/product/877) 来实现。

## 组成成分
私有网络有三个核心组成成分：私有网络网段、子网、路由表。
### 私有网络网段
用户在创建 VPC 时，需要用 [CIDR（无类别域间路由）](https://cloud.tencent.com/document/product/215/18509#cidr)（例如`10.0.0.0/16`）作为 VPC 指定 IP 地址组。
>!私有网络网段创建后无法修改，如果您有不同私有网络之间内网通信的需要，请在创建时，注意两端 CIDR 不要重叠。更多信息请参见 [网络规划](https://cloud.tencent.com/document/product/215/30313)。

腾讯云私有网络 CIDR 支持使用以下私有网段中的任意一个：
- **10.0**.0.0 - **10.255**.255.255（**掩码范围需在16 - 28**之间）
- **172.16**.0.0 - **172.31**.255.255（**掩码范围需在16 - 28**之间）
- **192.168**.0.0 - **192.168**.255.255 （**掩码范围需在16 - 28**之间）

### 子网
一个私有网络由至少一个子网组成。子网的 CIDR 必须在 VPC 的 CIDR 内。私有网络中的所有云资源（例如云服务器、云数据库等）都必须部署在子网内。
私有网络具有 [地域（Region）](https://cloud.tencent.com/document/product/215/20057#.E5.9C.B0.E5.9F.9F.EF.BC.88region.EF.BC.89) 属性（例如广州、上海）。而子网具有 [可用区（Zone）](https://cloud.tencent.com/document/product/215/20057#.E5.8F.AF.E7.94.A8.E5.8C.BA.EF.BC.88zone.EF.BC.89) 属性，一个私有网络下的子网可以属于该地域下不同可用区，同一私有网络下各个子网内资源无论是否在同一可用区内，均默认内网互通。
![](https://main.qcloudimg.com/raw/5124f94e309948afbb2998fdf92f463c.png)

### 路由表
每个私有网络有一个默认路由表，用户还可以创建自定义路由表。路由表由多条路由策略组成，用于控制私有网络 VPC 内子网的出流量走向，每个子网能且只能关联一个路由表，一个路由表可以关联多个子网。您可以为不同流量走向的子网创建多个路由表。
路由策略由目的端、下一跳类型、下一跳组成。
更多信息详情请参见 [路由表](https://cloud.tencent.com/document/product/215/20060)。

## 默认私有网络和子网
默认私有网络和子网可以帮助您更快速地部署业务。
默认私有网络与您自行创建的私有网络功能**完全一致**，且默认 VPC 不会占用您在某个地域下的 VPC 配额。如果您不再需要默认私有网络和子网，可以自行删除。
>?在您没有 VPC 或子网的情况下，购买 CVM 等实例时，系统会为您在相应地域创建默认 VPC 及子网，为您节省了解 VPC 及子网的功能细节的时间。

## VPC 连接
腾讯云私有网络能实现以下功能：
- 通过控制台或 API 自定义网段划分、IP 地址、路由策略等。
- 通过 [对等连接](https://cloud.tencent.com/document/product/553) 或 [云联网](https://cloud.tencent.com/document/product/877) 服务可实现不同私有网络间资源的内网互通。
- 通过 [云联网](https://cloud.tencent.com/document/product/877)、[VPN 连接](https://cloud.tencent.com/document/product/554) 或 [专线接入](https://cloud.tencent.com/document/product/216) 将私有网络与您的数据中心连通。
- 通过 [弹性公网 IP](https://cloud.tencent.com/document/product/215/20080) 、[NAT 网关](https://cloud.tencent.com/document/product/552) 或 [公网网关](https://cloud.tencent.com/document/product/215/20078) 等灵活访问 Internet。
- 通过 [基础网络互通](https://cloud.tencent.com/document/product/215/20083)，使得基础网络内服务器可以和私有网络内服务器通过内网通信。
- 通过 [安全组](https://cloud.tencent.com/document/product/215/20089) 和 [网络 ACL](https://cloud.tencent.com/document/product/215/20088) 可以多维度、全方位的满足您的网络安全需求。

![](https://main.qcloudimg.com/raw/a1cf55fb2e99601e415d4c950b53def9.png)

## 功能特性
### DHCP
动态主机设置协议（DHCP，Dynamic Host Configuration Protocol）是一种局域网的网络协议， 提供了将配置信息传递到 TCP / IP 网络服务器的标准。
腾讯云 VPC 内的云服务器支持 DHCP 协议，支持配置的 DHCP Options 字段包括：DNS 地址、Domain Name。您可在 VPC 详情页配置这两个参数，该配置将对该 VPC 下的所有云服务器生效。
- DNS 地址
	- DNS 最多支持4个 IP，IP 之间请用逗号隔开。
	- 虽然可以指定4个 IP，但某些操作系统可能无法支持4个 DNS 地址。
	- 腾讯云默认 DNS 为：`183.60.83.19`，`183.60.82.98`。如不使用腾讯云默认 DNS，将无法使用内部服务，例如 Windows 激活、NTP、YUM 等。
- Domain Name
	- 云服务器 hostname 后缀，例如 example.com。

>!
>- 2018年4月1日前创建的 VPC 暂不支持 DHCP 特性，若您在控制台无法修改 DNS 地址和 Domain Name，即说明您的 VPC 不支持该特性。
>- 为了保证配置修改后及时生效，已有的云服务器需重启机器或 dhclient，新增的云服务器修改该配置立即生效。

### 广播和组播
#### 什么是广播和组播？
广播和组播是一对多的通信方式，通过单点到多点的高效数据传送，可以为企业节约网络带宽、降低网络负载。
- 广播：腾讯云支持子网维度的广播。
- 组播：腾讯云支持私有网络维度的组播。

>!广播和组播功能处于内测阶段，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/tgsh6ztuc4) 。

#### 适用行业
广播和组播较多应用于金融和游戏行业：
- 金融行业主要用于广播业务或行情数据。例如，获取股票价格等实时数据时，券商可通过广播，对多台 client 实时发送股票数据，有效降低网络负载。
- 游戏行业主要用于多台服务器之间的心跳保持。

如果使用单播技术，发送主机需要分别向 N 个主机发送，共发送 N 次。如果使用组播，主机向 N 个主机发送相同的数据时，只要发送1次，既节省服务器资源，也节省了网络主干的带宽资源。

## 使用约束
关于私有网络与子网，您需要注意以下几点：
- 腾讯云保留了各个子网的前面两个 IP 地址和最后一个 IP 地址，以作 IP 联网之用。 例如，子网 CIDR 为`172.16.0.0/24`，则腾讯云保留的 IP 地址为：`172.16.0.0`、`172.16.0.1`和`172.16.0.255`。
- 向私有网络中添加云服务器时，系统会在指定子网内为该实例默认随机分配一个内网 IP，用户可以在云服务器创建后，重新指定每台云服务器的内网 IP。
- 在私有网络内，一台云服务器只能绑定一个内网 IP 和一个公网 IP。

## 操作指南
控制台操作，详情请参见 [操作总览](https://cloud.tencent.com/document/product/215/20188)。
