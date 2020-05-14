私有网络（Virtual Private Cloud，VPC）是基于腾讯云构建的专属云上网络空间，为您在腾讯云上的资源提供网络服务，不同私有网络间完全逻辑隔离。针对不同场景，腾讯云提供了不同的 VPC 内网互联产品和服务，如云联网、对等连接、专线接入、VPN 连接等。

<table>
<thead>
<tr>
<th width="16%">场景</th>
<th width="20%">产品</th>
<th width="34%">功能</th>
<th width="30%">特点</th>
</tr>
</thead>
<tbody>
<tr>
<tr>
<td rowspan="2"><a href="#vpcConn">连接其他 VPC</a></td>
<td><a href="https://cloud.tencent.com/document/product/877" target="_blank">云联网</a><br>（推荐使用）</td>
<td>用于两个或多个 VPC 间内网通信。</td>
<td><li>CIDR 限制缩小到子网范围。</li><li>配置简单，路由自动下发。</li><li>一次加入，所有实例默认互通，支持路由开启和关闭。</li><li>支持不同账号、不同地域下 VPC 的互通，同时支持 VPC 与数据中心互通。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/553" target="_blank">对等连接</a></td>
<td>用于两个 VPC 或多个 VPC 间内网通信。</td>
<td><li>两个 VPC 或多个 VPC 间的 CIDR 不能重叠。</li> <li>需要手动配置路由。</li><li>支持不同账号、不同地域下 VPC 间的互通。</li><li>多个 VPC 间的互通，需创建多个对等连接实例，配置繁琐。</li></td>
</tr>
</tr>
<tr>
<td rowspan="3"><a href="#vpcIDC">连接本地数据中心</a></td>
<td><a href="https://cloud.tencent.com/document/product/877" target="_blank">云联网</a> + <a href="https://cloud.tencent.com/document/product/216" target="_blank">专线接入</a><br>（推荐使用）</td>
<td>通过创建一个专线接入的专用通道连接云联网的专线网关，然后把专线网关加载到云联网，即可实现云联网内的多个网络实例间全互通。</td>
<td><li>配置简单、路由自动下发。</li><li>一次加入，可与多个 VPC、数据中心互通，支持路由开启和关闭。</li><li>同地域实例互通免费。</li></td>
</tr><tr>
<td><a href="https://cloud.tencent.com/document/product/554" target="_blank">VPN 连接</a></td>
<td>通过 VPN 连接帮您在 Internet 上快速构建一条安全、可靠的加密通道，连接 VPC 和本地数据中心。</td>
<td><li>网络质量依赖于公网。</li><li>网络传输基于 IKE 协议的预共享密钥加密。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/216" target="_blank">专线接入</a></td>
<td>通过共享或独占的物理专线连接 VPC 和本地数据中心。</td>
<td><li>独占网络链路，网络时延小、安全性高。</li><li>支持多条物理链路备份，可靠性高。</li><li>支持在网关上配置网络地址转换服务，可解决地址冲突问题。</li></td>
</tr>
</tr>
<tr>
<td rowspan="2"><a href="#moreConn">连接多方网络</a></td>
<td><a href="https://cloud.tencent.com/document/product/554/19276#vpn-.E7.BD.91.E5.85.B3" target="_blank">VPN 连接</a></td>
<td>通过在 VPC 内建立 VPN 网关，每个 VPN 网关建立多个 VPN 通道，每个 VPN 通道可以打通一个连接本地数据中心或 VPC。</td>
<td><li>网络质量依赖于公网。</li><li>网络传输基于 IKE 协议的预共享密钥加密。</li></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/554/19276#vpn-.E7.BD.91.E5.85.B3" target="_blank">VPN 连接</a> + <a href="https://cloud.tencent.com/document/product/553" target="_blank">对等连接</a></td>
<td>通过组合使用 VPN 连接和对等连接，实现多方网络互连。</td>
<td><li>网络质量依赖于公网。</li><li>网络传输基于 IKE 协议的预共享密钥加密。</li><li>两个 VPC 的 CIDR 不能重叠。</li> <li>需要手动配置路由。</li><li>支持不同账号、不同地域下 VPC 的互通。</li></td>
</tr>
<tr>
<td ><a href="#moreConn">连接远程客户端</a></td>
<td>云市场的 SSL-VPN 产品。</td>
<td>云市场购买 SSL-VPN 产品并部署到 VPC 后，通过远程拨号连接腾讯云 VPN 服务器。</td>
<td><li>成本高。</li><li>可靠性低。</li><li>需自行搭建、运维。</li></td>
</tr>
</tbody></table>

## <span id="vpcConn" />连接其他 VPC
您可以在不同地域的 VPC 内部署应用，构建多地域跨 VPC 网络互联服务，实现就近提供服务、降低网络时延、相互容灾备份、提高服务可靠性。
腾讯云的对等连接和云联网支持同地域和跨地域互通。
#### 对等连接
对等连接是一种大带宽、高质量的云上资源互通服务，可以帮助您打通腾讯云上的资源通信链路。对等连接具有多区域、多账户、多种网络异构互通等特点，轻松实现云上两地三中心、游戏同服等复杂网络场景，支持私有网络间互通、私有网络和黑石私有网络互通，满足您不同业务的部署需求。
![](https://main.qcloudimg.com/raw/5f84c46b5766ade11dc1712302ec1281.png)

#### 云联网
云联网为您提供云上私有网络间（VPC）、VPC 与本地数据中心间（IDC）内网互联的服务，具备全网多点互联、路由自学习、链路选优及故障快速收敛等能力。云联网覆盖全球20+地域，支持100+Gbps带宽以及99.99%高可用性，为您轻松构建极速、稳定、安全、灵活的全球互联网络。
![](https://main.qcloudimg.com/raw/f1cc143a7f77681b152323fbb8488ab9.png)

## <span id="vpcIDC" />连接本地数据中心
您可使用 VPN 连接、专线接入、云联网将云上 VPC 与云下本地数据中心进行连接，构建混合云网络，实现资源互联。
#### VPN 连接
VPN 连接是一种通过公网加密通道连接您对端 IDC 和私有网络（Virtual Private Cloud，VPC）的方式。
![](https://main.qcloudimg.com/raw/726547ca165912c2c687eeb5ebcdfd01.png)

#### 专线接入
专线接入提供了一种快速安全连接腾讯云与本地数据中心的方法。用户可以通过一条物理专线，一次性打通位于多地域的腾讯云计算资源，实现灵活可靠的混合云部署。
![](https://main.qcloudimg.com/raw/34846c629692151017f5359487cc9c0a.png)

#### 云联网 + 专线接入
云联网为您提供云上私有网络间（VPC）、VPC 与本地数据中心间（IDC）内网互联的服务，具备全网多点互联、路由自学习、链路选优及故障快速收敛等能力。通过专线接入的专用通道与云联网专线网关的连接，并将专线网关加载到云联网，即可实现单个专用通道连接多个 VPC。
![](https://main.qcloudimg.com/raw/ccc0f0dfcbfeec2bf97e107b377ac838.png)

## <span id="moreConn" />连接多方网络
您可使用 VPN 连接、对等连接，将多方网络进行互连互通。
#### VPN 连接
VPN 连接是一种通过公网加密通道连接您对端 IDC 和私有网络（Virtual Private Cloud，VPC）的方式，通过 VPN 连接功能在多方网络之间建立安全通信，满足多方内网互连的需求。
![](https://main.qcloudimg.com/raw/b58f9a2fef59c258309c5ef245180cc6.png)

#### VPN 连接 + 对等连接
您可以通过 VPN 连接和对等连接，连接各地各个本地数据中心（IDC），该方案安全性高、网络质量好、成本低。
如下图所示，若要实现广州和上海各 IDC 的内网互连需求，可以通过对等连接进行广州和上海 VPC 间连接，并分别通过 VPN 连接对广州和上海两个地域的本地数据中心进行连接。
![](https://main.qcloudimg.com/raw/d98efb6cc0a166eaabb24343f9023e99.png)

## <span id="vpcIDC" />连接远程客户端
您可在云市场购买 SSL-VPN 产品，并部署到 VPC 内有公网 IP 的云服务器上，从客户端通过公网远程拨号连接对应的云服务器。
