### BGP ASN
用于 BGP 路由中的每个自治系统都被分配一个唯一的自治系统编号。自治系统编号（ASN）由互联网地址分派机构（Internet Assigned Numbers Authority，简称为IANA，该机构也负责分配互联网IP地址）成批地分配给各个区域互联网注册管理机构（RIR）。各地区的 RIR 则进一步再从 IANA 分配到的整批 ASN 里为一个实体分配一个 ASN。希望获得 ASN 的实体必须按其所属的地区中心规定的程序进行申请，在申请得到批准后才会分配到一个 ASN。


### 对等连接
<a href="https://cloud.tencent.com/doc/product/215/5000" target="_blank">对等连接</a>（peering connection）是不同私有网络建立的连接，支持跨账户和跨地域的私有网络之间流量互通。

### IPsec
IPsec（Internet Protocol Security）又叫互联网安全协议，是一个协议包，透过对 IP 协议的分组进行加密和认证来保护 IP 协议的网络传输协议族（一些相互关联的协议的集合）。
IPsec 主要由以下协议组成：
- **认证头**：为 IP 数据报提供无连接数据完整性、消息认证以及防重放攻击保护。
- **封装安全载荷**：提供机密性、数据源认证、无连接完整性、防重放和有限的传输流机密性。
- **安全关联**：提供算法和数据包，提供认证头、封装安全载荷操作所需的参数。


### 路由表
<a href="https://cloud.tencent.com/doc/product/215/4954" target="_blank">路由表</a>（routing table）包含一系列路由策略，用于定义私有网络内每个子网的网络流量走向。每个子网有且只有一个关联路由表，每个路由表可以关联同一个私有网络中的多个子网。

### 私有网络
私有网络（Virtual Private Cloud）在腾讯云构建出独立的网络空间，与您在数据中心运行的传统网络极其相似，但是托管在腾讯云私有网络内的是您在腾讯云上的服务资源，包括：<a href="https://cloud.tencent.com/doc/product/213/495" target="_blank">云服务器</a>、<a href="https://cloud.tencent.com/doc/product/214/524" target="_blank">负载均衡</a>、<a href="https://cloud.tencent.com/document/product/236" target="_blank">云数据库</a> 等云服务资源。您完全不用关心网络设备的采购和运维，而是通过软件自定义网段划分、IP 地址、路由策略等。您不仅可以通过 <a href="https://cloud.tencent.com/doc/product/213/1941" target="_blank">弹性 IP</a>、<a href="https://cloud.tencent.com/doc/product/215/4975" target="_blank">NAT 网关</a> 和 <a href="https://cloud.tencent.com/doc/product/215/4972" target="_blank">公网网关</a> 等灵活访问 Internet，您也可以通过 <a href="https://cloud.tencent.com/doc/product/215/4956" target="_blank"> VPN</a> / <a href="https://cloud.tencent.com/doc/product/215/4976" target="_blank">专线接入</a> 将私有网络与您的数据中心连通。同时，腾讯云私有网络的 <a href="https://cloud.tencent.com/doc/product/215/5000" target="_blank">对等连接</a> 服务可以帮助您轻松实现全球同服和两地三中心容灾。另外，腾讯云私有网络中的 <a href="https://cloud.tencent.com/doc/product/213/500" target="_blank">安全组</a> 和 <a href="https://cloud.tencent.com/doc/product/215/5132" target="_blank">网络 ACL</a> 可以多维度、全方位的满足您的网络安全需求。

### VLAN ID
VLAN（Virtual Local Area Network），又称虚拟局域网，是一种建构于局域网交换技术的网络管理的技术。交换机一般可以划分 255 个 VLAN。每个 VLAN 的 ID，可以是 1 - 4096 之间的任意数字。ID 的作用就是用于区分不同 VLAN，可以设置 TAG UNTag member 属性，可以让该端口的下行或上行数据报打上标签。


### 物理专线
物理专线是连接腾讯云与本地数据中心的物理线路连接，一个物理专线可以与多个地域的专线网关建立专用通道。

### 子网
<a href="https://cloud.tencent.com/doc/product/215/4927" target="_blank">子网</a>（subnet）是对私有网络网段的灵活划分，可以在不同子网内部署应用程序和服务，安全灵活地在腾讯云 VPC 中托管多层 Web 应用程序。

### 专线接入
<a href="https://cloud.tencent.com/doc/product/215/4976" target="_blank">专线接入</a>（Direct Connect）是一种快速连接腾讯云与本地数据中心的方法，您可以通过一条物理专线一次性打通位于多地域的腾讯云计算资源，实现灵活可靠的混合云部署。专线接入支持无单点的双线热备接入方式，满足金融等高网络互联要求。

### 专用通道
专用通道是物理专线的网络链路划分，可以创建连接至不同专线网关的专用通道实现本地数据中心与多个私有网络的互联。

### 专线网关
专线网关是私有网络的专线流量入口，可以接入多个专用通道与多个本地数据中心互联。




