### 私有网络
私有网络（Virtual Private Cloud）在腾讯云构建出独立的网络空间，与您在数据中心运行的传统网络极其相似，但是托管在腾讯云私有网络内的是您在腾讯云上的服务资源，包括：<a href="https://cloud.tencent.com/doc/product/213/495" target="_blank">云服务器</a>、<a href="https://cloud.tencent.com/doc/product/214/524" target="_blank">负载均衡</a>、<a href="https://cloud.tencent.com/document/product/236" target="_blank">云数据库</a> 等云服务资源。您完全不用关心网络设备的采购和运维，而是通过软件自定义网段划分、IP 地址、路由策略等。您不仅可以通过 <a href="https://cloud.tencent.com/doc/product/213/1941" target="_blank">弹性 IP</a>、<a href="https://cloud.tencent.com/doc/product/215/4975" target="_blank">NAT 网关</a> 和 <a href="https://cloud.tencent.com/doc/product/215/4972" target="_blank">公网网关</a> 等灵活访问 Internet，您也可以通过 <a href="https://cloud.tencent.com/doc/product/215/4956" target="_blank"> VPN</a> / <a href="https://cloud.tencent.com/doc/product/215/4976" target="_blank">专线接入</a> 将私有网络与您的数据中心连通。同时，腾讯云私有网络的 <a href="https://cloud.tencent.com/doc/product/215/5000" target="_blank">对等连接</a> 服务可以帮助您轻松实现全球同服和两地三中心容灾。另外，腾讯云私有网络中的 <a href="https://cloud.tencent.com/doc/product/213/500" target="_blank">安全组</a> 和 <a href="https://cloud.tencent.com/doc/product/215/5132" target="_blank">网络 ACL</a> 可以多维度、全方位的满足您的网络安全需求。
### 安全组
<a href="https://cloud.tencent.com/doc/product/213/500" target="_blank">安全组</a>（Security Group）是一种有状态的包过滤功能的虚拟防火墙，它用于设置单台或多台云服务器的网络访问控制，可以将同一地域内具有相同网络安全隔离需求的云服务器实例加到同一个安全组内，通过安全组的网络策略对云服务器的出入流量进行安全过滤。
### 路由表
<a href="https://cloud.tencent.com/doc/product/215/4954" target="_blank">路由表</a>（Routing Table）包含一系列路由策略，用于定义私有网络内每个子网的网络流量走向。每个子网有且只有一个关联路由表，每个路由表可以关联同一个私有网络中的多个子网。
### 内网 IP
内网 IP（Private IP）在腾讯云 VPC 或基础网络内分配给实例 IP 地址，内网 IP 地址无法访问 Internet，但内网 IP 可用于 VPC 中或基础网络实例之间的通信。 
### 弹性 IP
<a href="https://cloud.tencent.com/doc/product/213/1941" target="_blank">弹性 IP</a>（Elastic IP，EIP）可以独立申请的公网 IP 地址，支持动态绑定和解绑。您可以将其与账户中的云服务器（或 NAT 网关实例）绑定或者解绑。主要作用是：</br>1. 保留 IP，因为国内的 IP 和 DNS 之间是需要域名备案的。</br>2. 屏蔽实例故障，例如：动态 DNS 映射把 DNS 名称映射到 IP 地址，传播这个映射变化到整个 Internet 可能需花费24小时，而弹性 IP 实现了 IP 从一个云服务器到另一个云服务器的漂移。在任何云服务器出现故障时，只需启动另一个实例并重新映射它，从而快速响应实例故障。
### 子网
<a href="https://cloud.tencent.com/doc/product/215/4927" target="_blank">子网</a>（Subnet）是对私有网络网段的灵活划分，可以在不同子网内部署应用程序和服务，安全灵活地在腾讯云 VPC 中托管多层 Web 应用程序。




