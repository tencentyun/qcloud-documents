私有网络（Virtual Private Cloud，VPC）是基于腾讯云构建的专属云上网络空间，为您在腾讯云上的资源提供网络服务，不同私有网络间完全逻辑隔离。针对不同场景，腾讯云提供了不同的 VPC 内网互联产品和服务，如云联网、对等连接、专线接入、VPN 连接等。

<table>
<thead>
<tr>
<th>场景</th>
<th>产品</th>
<th>功能</th>
<th>特点</th>
<th>限制</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2"><a href="#vpcCoon">连接其他 VPC</a></td>
<td><a href="https://cloud.tencent.com/document/product/553" target="_blank">对等连接</a></td>
<td>用于两个 VPC 间内网通信。</td>
<td><li>两个 VPC 的 CIDR 不能重叠。</li> <li>需要手动配置路由。</li><li>支持不同账号、不同地域下 VPC 的互通。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/877" target="_blank">云联网</a></td>
<td>用于两个或多个 VPC 间内网通信。</td>
<td><li>CIDR 限制缩小到子网范围。</li><li>配置简单，路由自动下发。</li><li>一次加入，所有实例默认互通，支持路由开启和关闭。</li><li>支持不同账号、不同地域下 VPC 的互通，同时支持 VPC 与数据中心互通。</li></td>
</tr>
<tr>
<td rowspan="3"><a href="#vpcIDC">连接本地数据中心</a></td>
<td><a href="https://cloud.tencent.com/document/product/554/19276#vpn-.E7.BD.91.E5.85.B3" target="_blank">VPN 连接</a></td>
<td>通过公网加密通道连接本地数据中心和 VPC。</td>
<td><li>网络质量依赖于公网。</li><li>网络传输基于 IKE 协议的预共享密钥加密。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/216" target="_blank">专线接入</a></td>
<td>通过使用专线接入的物理专线连接 VPC 和本地数据中心。</td>
<td><li>网络延时有可靠保证。</li><li>独占网络链路，安全性高。</li><li>支持在网关上配置网络地址转换服务，可解决地址冲突问题。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/877" target="_blank">云联网</a></td>
<td>通过腾讯云内网连接 VPC 和本地数据中心，可实现与所有  VPC、数据中心间的通信。</td>
<td><li>配置简单、路由自动下发。</li><li>一次加入，可与多个 VPC、数据中心互通，支持路由开启和关闭。</li><li>同地域实例互通免费。</li></td>
</tr>
<tr>
<td rowspan="2"><a href="#moreConn">连接多方网络</a></td>
<td><a href="https://cloud.tencent.com/document/product/554/19276#vpn-.E7.BD.91.E5.85.B3" target="_blank">VPN 连接</a></td>
<td>通过在 VPC 内建立 VPN 网关，每个 VPN 网关建立多个 VPN 通道，每个 VPN 通道可以打通一个连接本地数据中心或 VPC。</td>
<td><li>网络质量依赖于公网。</li><li>网络传输基于 IKE 协议的预共享密钥加密。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/216" target="_blank">专线接入</a> + <a href="https://cloud.tencent.com/document/product/877" target="_blank">云联网</a></td>
<td>通过创建一个专线接入的专用通道连接云联网的专线网关，然后把专线网关加载到云联网，即可实现云联网内的多个网络实例间全互通。</td>
<td><li>网络延时有可靠保证。</li><li>独占网络链路，安全性高。</li><li>支持在网关上配置网络地址转换服务，可解决地址冲突问题。</li></td>
</tr>
<tr>
<td ><a href="#moreConn">连接远程客户端</a></td>
<td>云市场的 SSL-VPN 产品。</td>
<td>云市场购买 SSL-VPN 产品并部署到 VPC 后，通过远程拨号连接腾讯云 VPN 服务器。</td>
<td><li>成本高。</li><li>可靠性低。</li><li>需自行搭建、运维。</li></td>
</tr>
</tbody></table>
