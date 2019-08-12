## 访问公网
您可使用以下产品或功能，实现公网访问。

| 产品 | 功能 | 特点 |
|---------|---------|---------|
| 普通公网 IP | 支持云服务器访问公网和用户从公网访问云服务器。| 只有在购买云服务器时可以选择是否分配普通公网 IP，如购买时未分配，可使用 [弹性公网 IP](https://cloud.tencent.com/document/product/213/5733) 或 [NAT 网关](https://cloud.tencent.com/document/product/552)。 |
| [弹性公网 IP（EIP）](https://cloud.tencent.com/document/product/213/5733) | 单台云服务器可以绑定一个或多个 EIP，以访问公网和被公网访问。| <li>一种可独立购买和持有的 IP 资源，详情请参见 [EIP 计费说明](https://cloud.tencent.com/document/product/213/17156)。</li><li>可与云服务器、NAT 网关动态绑定、解绑。</li><li>您可以根据业务随时 [调整 EIP 的带宽限制](https://cloud.tencent.com/document/product/213/16586#.E8.B0.83.E6.95.B4.E5.B8.A6.E5.AE.BD)。</li>|
|[NAT 网关](https://cloud.tencent.com/document/product/552)|SNAT：支持一个 VPC 下多台云服务器通过同一公网 IP 主动访问公网。<br>DNAT：可以将 VPC 内的云服务器内网 IP、协议、端口映射成外网 IP、协议端口，使云服务器上的服务可被公网访问。|<li>NAT 网关可以用于多台云服务器访问公网。</li><li>您可以根据业务随时 [调整 NAT 网关的带宽限制](https://cloud.tencent.com/document/product/552/18179)。|
|[公网网关](https://cloud.tencent.com/document/product/215/20078)|一种开启了转发功能的云服务器。没有公网 IP 的云服务器，可以通过位于不同子网的公网网关访问公网。|<li>与具有普通公网 IP 的云服务器差别在于，公网网关可以转发其它子网内云服务器访问公网的流量，而又普通公网 IP 的云服务器只能满足自身访问公网的需求。</li><li>您只有在购买云服务器时可以选择是否将云服务器作为公网网关，如购买时未创建为公网网关，建议您使用 [NAT 网关](https://cloud.tencent.com/document/product/552)。</li>|
|[负载均衡](https://cloud.tencent.com/document/product/214)|通过将访问流量均衡分发到多台云服务器上的方式对外提供服务。|<li>基于端口提供四层和七层负载均衡功能，支持用户从公网通过负载均衡（CLB）访问云服务器。</li><li>可以消除单点故障，提升应用系统的可用性。</li>

## 私有网络通信
您可使用以下产品或功能，实现私有网络间的通信。

| 产品 | 功能 | 特点 |
|---------|---------|---------|
| [对等连接](https://cloud.tencent.com/document/product/553) | 用于两个 VPC 间内网通信。 |<li>两个 VPC 的CIDR 不能重叠</li> <li>需要手动配置路由。</li><li>支持不同账号、不同地域下 VPC 的互通。</li>|
|[云联网](https://cloud.tencent.com/document/product/877)|用于两个或多个 VPC 间内网通信。|<li>CIDR 限制缩小到子网范围。</li><li>配置简单，路由自动下发。</li><li>一次加入，所有实例默认互通，支持路由开启和关闭。</li><li>支持不同账号、不同地域下 VPC 的互通，同事支持 VPC 与数据中心互联。</li>|

## 与数据中心通信
您可使用以下产品或功能，实现 VPC 与数据中心的通信。

| 产品 | 功能 | 特点 |
|---------|---------|---------|
| [VPN 网关](https://cloud.tencent.com/document/product/554/19276#vpn-.E7.BD.91.E5.85.B3)| 通过公网加密通道连接本地数据中心和 VPC。 | <li>网络质量依赖于公网。</li><li>网络传输基于 IKE 协议的预共享密钥加密。</li> |
|[专线接入](https://cloud.tencent.com/document/product/216)|通过使用物理专线连接 VPC 和本地数据中心|<li>网络延时有可靠保证。</li><li>独占网络链路，安全性高。</li><li>支持在网关上配置网络地址转换服务，可解决地址冲突问题。</li>|
|[云联网](https://cloud.tencent.com/document/product/877)|通过腾讯云内网连接 VPC 和本地数据中心。<br>多个数据中心、VPC 间互通。|<li>配置简单、路由自动下发。</li><li>一次加入，可与多个 VPC、数据中心互通，支持路由开启和关闭。</li><li>同地域实例互通免费。</li>|

