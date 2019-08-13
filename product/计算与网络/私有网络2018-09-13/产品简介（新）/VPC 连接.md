腾讯云为您提供丰富的解决方案，可以满足您 VPC 内的云服务器/数据库等实例访问公网（Internet）、访问其他 VPC 内实例、或与本地数据中心（IDC）互连的需求。
## 访问公网
您可使用如下产品或功能，实现公网访问。

<table>
<thead>
<tr>
<th width="15%">产品</th>
<th width="35%">功能</th>
<th width="50%">特点</th>
</tr>
</thead>
<tbody><tr>
<td>普通公网 IP</td>
<td>支持云服务器访问公网或用户从公网访问云服务器。</td>
<td>只有在购买云服务器时可以选择是否分配普通公网 IP，如购买时未分配，可使用 <a href="https://cloud.tencent.com/document/product/213/5733" target="_blank">弹性公网 IP</a> 或 <a href="https://cloud.tencent.com/document/product/552" target="_blank">NAT 网关</a>。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/213/5733" target="_blank">弹性公网 IP<br>（EIP）</a></td>
<td>单台云服务器可以绑定一个或多个 EIP，以访问公网或被公网访问。</td>
<td><li>一种可独立购买和持有的 IP 资源，详情请参见 <a href="https://cloud.tencent.com/document/product/213/17156" target="_blank">EIP 计费说明</a>。</li><li>可与云服务器、NAT 网关动态绑定、解绑。</li><li>您可以根据业务随时 <a href="https://cloud.tencent.com/document/product/213/16586#.E8.B0.83.E6.95.B4.E5.B8.A6.E5.AE.BD" target="_blank">调整 EIP 的带宽限制</a>。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/552" target="_blank">NAT 网关</a></td>
<td><li>SNAT：支持一个 VPC 下多台云服务器通过同一公网 IP 主动访问公网。</li><li>DNAT：可以将 VPC 内的云服务器内网 IP、协议、端口映射成外网 IP、协议、端口，使云服务器上的服务可被公网访问。</li></td>
<td><li>NAT 网关可以用于多台云服务器访问公网。</li><li>您可以根据业务随时 <a href="https://cloud.tencent.com/document/product/552/18179" target="_blank">调整 NAT 网关的带宽限制</a>。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/215/20078" target="_blank">公网网关</a></td>
<td>一种开启了转发功能的云服务器。没有公网 IP 的云服务器，可以通过位于不同子网的公网网关访问公网。</td>
<td><li>与具有普通公网 IP 的云服务器差别在于，公网网关可以转发其它子网内云服务器访问公网的流量，而又普通公网 IP 的云服务器只能满足自身访问公网的需求。</li><li>您只有在购买云服务器时可以选择是否将云服务器作为公网网关，如购买时未创建为公网网关，建议您使用 <a href="https://cloud.tencent.com/document/product/552" target="_blank">NAT 网关</a>。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214" target="_blank">负载均衡</a></td>
<td>通过将访问流量均衡分发到多台云服务器上的方式对外提供服务。</td>
<td><li>基于端口提供四层和七层负载均衡功能，支持用户从公网通过负载均衡（CLB）访问云服务器。</li><li>可以消除单点故障，提升应用系统的可用性。</li></td>
</tr>
</tbody></table>

## VPC 间通信
您可使用如下产品或功能，实现 VPC 间的通信。

| 产品 | 功能 | 特点 |
|---------|---------|---------|
| [对等连接](https://cloud.tencent.com/document/product/553) | 用于两个 VPC 间内网通信。 |<li>两个 VPC 的CIDR 不能重叠。</li> <li>需要手动配置路由。</li><li>支持不同账号、不同地域下 VPC 的互通。</li>|
|[云联网](https://cloud.tencent.com/document/product/877)|用于两个或多个 VPC 间内网通信。|<li>CIDR 限制缩小到子网范围。</li><li>配置简单，路由自动下发。</li><li>一次加入，所有实例默认互通，支持路由开启和关闭。</li><li>支持不同账号、不同地域下 VPC 的互通，同时支持 VPC 与数据中心互通。</li>|

## 与本地数据中心通信
您可使用如下产品或功能，实现 VPC 与本地数据中心的通信。

<table>
<thead>
<tr>
<th width="10%">产品</th>
<th width="40%">功能</th>
<th width="50%">特点</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/554/19276#vpn-.E7.BD.91.E5.85.B3" target="_blank">VPN 网关</a></td>
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

