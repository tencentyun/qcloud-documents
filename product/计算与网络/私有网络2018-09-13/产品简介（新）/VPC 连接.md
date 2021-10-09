腾讯云为您提供丰富的解决方案，可以满足 VPC 内的云服务器、数据库等实例连接公网（Internet）、连接其他 VPC 内实例、或与本地数据中心（IDC）互联的需求。您可通过如下视频了解私有网络 VPC 及其多种连接方式。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2571-44483?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>
 
## 连接公网
您可使用如下产品或功能，实现 VPC 与公网间的访问。
<table>
<thead>
<tr>
<th width="12%">产品</th>
<th width="40%">功能</th>
<th width="48%">特点</th>
</tr>
</thead>
<tbody><tr>
<td>普通公网 IP</td>
<td>支持云服务器访问公网或用户从公网访问云服务器。</td>
<td>只有在购买云服务器时可以选择是否分配普通公网 IP，如购买时未分配，可使用 <a href="https://cloud.tencent.com/document/product/1199" target="_blank">弹性公网 IP</a> 或 <a href="https://cloud.tencent.com/document/product/552" target="_blank">NAT 网关</a>。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199" target="_blank">弹性公网 IP<br>（EIP）</a></td>
<td>单台云服务器可以绑定一个或多个 EIP，以访问公网或被公网访问。</td>
<td><li>一种可独立购买和持有的 IP 资源，详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41692" target="_blank">弹性公网 IP-计费说明</a>。</li><li>可与云服务器、NAT 网关动态绑定、解绑。</li><li>您可以根据业务随时 <a href="https://cloud.tencent.com/document/product/1199/41705" target="_blank">调整 EIP 的带宽限制</a>。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/552" target="_blank">NAT 网关</a></td>
<td><li>SNAT：支持一个 VPC 下多台云服务器通过同一公网 IP 主动访问公网。</li><li>DNAT：可以将 VPC 内的云服务器内网 IP、协议、端口映射成外网 IP、协议、端口，使云服务器上的服务可被公网访问。</li></td>
<td><li>NAT 网关可以用于多台云服务器访问公网。</li><li>您可以根据业务随时 <a href="https://cloud.tencent.com/document/product/552/18179" target="_blank">调整 NAT 网关的带宽限制</a>。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214" target="_blank">负载均衡</a></td>
<td>通过将访问流量均衡分发到多台云服务器上的方式对外提供服务。</td>
<td><li>基于端口提供四层和七层负载均衡功能，支持用户从公网通过负载均衡（CLB）访问云服务器。</li><li>可以消除单点故障，提升应用系统的可用性。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/213/38839" target="_blank">公网网关</a></td>
<td>一种开启了转发功能的云服务器。没有公网 IP 的云服务器，可以通过位于不同子网的公网网关访问公网。</td>
<td><li>与具有普通公网 IP 的云服务器差别在于，公网网关可以转发其它子网内云服务器访问公网的流量，而有普通公网 IP 的云服务器只能满足自身访问公网的需求。</li><li>您只有在购买云服务器时可以选择是否将云服务器作为公网网关，如购买时未创建为公网网关，建议您使用 <a href="https://cloud.tencent.com/document/product/552" target="_blank">NAT 网关</a>。</li></td>
</tr>
</tbody></table>

## 连接其它 VPC
您可使用如下产品或功能，实现 VPC 间的通信。

| 产品 | 功能 | 特点 |
|---------|---------|---------|
| [对等连接](https://cloud.tencent.com/document/product/553) | 用于两个 VPC 间内网通信。 |<li>两个 VPC 的 CIDR 不能重叠。</li> <li>需要手动配置路由。</li><li>支持不同账号、不同地域下 VPC 的互通。</li>|
|[云联网](https://cloud.tencent.com/document/product/877)|用于两个或多个 VPC 间内网通信。|<li>CIDR 限制缩小到子网范围。</li><li>配置简单，路由自动下发。</li><li>一次加入，所有实例默认互通，支持路由开启和关闭。</li><li>支持不同账号、不同地域下 VPC 的互通，同时支持 VPC 与数据中心互通。</li>|

## 连接本地数据中心
您可使用如下产品或功能，实现 VPC 与本地数据中心的互联。

<table>
<thead>
<tr>
<th width="10%">产品</th>
<th width="40%">功能</th>
<th width="50%">特点</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/554/19276#vpn-.E7.BD.91.E5.85.B3" target="_blank">VPN 连接</a></td>
<td>通过公网加密通道连接本地数据中心和 VPC。</td>
<td><li>网络质量依赖于公网。</li><li>网络传输基于 IKE 协议的预共享密钥加密。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/216" target="_blank">专线接入</a></td>
<td>通过使用物理专线连接 VPC 和本地数据中心。</td>
<td><li>网络延时有可靠保证。</li><li>独占网络链路，安全性高。</li><li>支持在网关上配置网络地址转换服务，可解决地址冲突问题。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/877" target="_blank">云联网</a></td>
<td>通过腾讯云内网连接 VPC 和本地数据中心，可实现与所有  VPC、数据中心间的通信。</td>
<td><li>配置简单、路由自动下发。</li><li>一次加入，可与多个 VPC、数据中心互通，支持路由开启和关闭。</li><li>同地域实例互通免费。</li></td>
</tr>
</tbody></table>

## 连接基础网络
您可使用如下产品或功能，实现 VPC与基础网络的互联。

| 产品 | 功能 | 特点 |
|---------|---------|---------|
| 基础网络互通| 将基础网络内的云服务器关联至指定私有网络，使基础网络中的云服务器可以与私有网络内的云服务器、数据库等云服务通信。 |<li>基础网络中的云服务器可以访问私有网络中的云服务器、云数据库、内网负载均衡、云缓存等云资源。</li> <li>私有网络内的云服务器，仅能访问互通的基础网络云服务器，无法访问基础网络中的其他计算资源。</li>|
|终端连接|实现私有网络内实例通过内网与基础网络内非云服务器实例通信的功能。|<li>支持连接的基础网络产品包括：CLB、MySQL、Memcached、Redis、MariaDB、SQL Server、PostgreSQL、MongoDB、TDSQL。</li><li>终端连接不支持跨地域、跨账号，如您有建立终端连接的需要，请提交 <a href="https://console.cloud.tencent.com/workorder/category" target="_blank">工单申请</a>。</li>|

## 后续操作
- 如何通过普通公网 IP、弹性公网 IP、NAT 网关、负载均衡等实现访问公网（Internet），详情请参见 [连接公网](https://cloud.tencent.com/document/product/215/36697)。
- 如何通过对等连接、云联网实现连接不同的 VPC，详情请参见 [连接其它 VPC](https://cloud.tencent.com/document/product/215/36698)。
- 如何通过 VPN 连接、专线接入、云联网实现 VPC 与本地数据中心的通信，详情请参见 [连接本地数据中心](https://cloud.tencent.com/document/product/215/36699)。
- 如何通过基础网络互通实现 VPC 与基础网络通信，详情请参见 [与基础网络通信](https://cloud.tencent.com/document/product/215/38124)。
