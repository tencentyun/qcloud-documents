## 应用场景
多层 Web 应用的隔离部署，适用于既希望保证 Web 接入层能访问 Internet、响应海量请求的同时，又需要通过网络隔离保障数据库服务器的安全的场景。
您可以在私有网络内创建不同子网，将整个 Web 层放在一个子网，通过配置弹性 IP / 网关云服务器 / NAT 网关与 Internet 通信，使用负载均衡服务将访问流量自动分配到多个 Web 接入层云服务器上；逻辑层单独放在一个子网，只能和 Web 层及数据层通信；数据层放在另外一个子网，只和逻辑层通信，来实现隔离部署。
![](https://mc.qcloudimg.com/static/img/b127c404a42371721b7cc4c08b8ce7e0/image.png)

## 解决方案
- **私有网络**
CIDR(10.0.0.0/16)，并在私有网络内创建三个子网。
- **Web 层子网**
CIDR(10.0.0.0/24)，将部署了 Web 层应用的云服务器单独放于该子网，该子网可与 Internet 通信以响应用户请求。同时，面对海量请求时，您可以使用负载均衡服务。
- **逻辑层子网**
CIDR(10.0.1.0/24)，逻辑层应用所在云服务器单独放于一个子网，以保证逻辑层应用不被公网访问。
- **数据层子网**
CIDR(10.0.2.0/24)，为了保证数据的安全，单独分配一个数据子网，在这其中部署数据库产品，只允许逻辑层子网的流量访问。
<span id="guize"></span>
- **网络 ACL**
通过网络 ACL 进行子网间的流量控制。配置规则如 “网络 ACL A” 和 “网络 ACL B” 所述。
- **网络 ACL A**
绑定逻辑层子网，目标：保证逻辑层应用不被公网访问，能被 Web 层子网和数据库层子网访问，配置规则如下：
 - 入规则：
 <table>
 <tbody>
 <tr>
 <th>协议类型</th>
 <th>端口</th>
 <th>源 IP</th>
 <th>策略</th>
 <th>备注</th>
 </tr>
 <tr>
 <td>All traffic</td>
 <td>ALL</td>
 <td>	10.0.0.0/24</td>
 <td>允许</td>
 <td>允许 Web 层访问</td>
 </tr>
 </tbody>
 </table>
 - 出规则：
 <table>
 <tbody>
 <tr>
 <th>协议类型</th>
 <th>端口</th>
 <th>目的 IP</th>
 <th>策略</th>
 <th>备注</th>
 </tr>
 <tr>
 <td>All traffic</td>
 <td>ALL</td>
 <td>	10.0.0.0/24</td>
 <td>允许</td>
 <td>允许响应 Web 层访问</td>
 </tr>
  <tr>
 <td>All traffic</td>
 <td>ALL</td>
 <td>	10.0.0.0/24</td>
 <td>允许</td>
 <td>允许访问数据库层子网</td>
 </tr>
 </tbody>
 </table>
 

- **网络 ACL B**
 绑定数据库层子网，目标：保证数据库层子网只能被逻辑层子网访问，规则如下：
 - 入规则：
 <table>
 <tbody>
 <tr>
 <th>协议类型</th>
 <th>端口</th>
 <th>源 IP</th>
 <th>策略</th>
 <th>备注</th>
 </tr>
 <tr>
 <td>All traffic</td>
 <td>ALL</td>
 <td>	10.0.1.0/24</td>
 <td>允许</td>
 <td>允许逻辑层访问</td>
 </tr>
 </tbody>
 </table>
 - 出规则：
 <table>
 <tbody>
 <tr>
 <th>协议类型</th>
 <th>端口</th>
 <th>目的 IP</th>
 <th>策略</th>
 <th>备注</th>
 </tr>
 <tr>
 <td>All traffic</td>
 <td>ALL</td>
 <td>	10.0.1.0/24</td>
 <td>允许</td>
 <td>允许返回逻辑层的请求</td>
 </tr>
 </tbody>
 </table>
 
## 操作步骤
为部署多层 Web 应用，您需要完成以下步骤：
1. 创建私有网络，详情请参见 [创建私有网络、初始化子网和路由表](https://cloud.tencent.com/document/product/215/4927#.E5.88.9B.E5.BB.BA.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E3.80.81.E5.88.9D.E5.A7.8B.E5.8C.96.E5.AD.90.E7.BD.91.E5.92.8C.E8.B7.AF.E7.94.B1.E8.A1.A8)。
2. 创建 Web 层子网， [添加云服务器](https://cloud.tencent.com/document/product/215/4927#.E5.90.91.E5.AD.90.E7.BD.91.E4.B8.AD.E6.B7.BB.E5.8A.A0.E4.BA.91.E4.B8.BB.E6.9C.BA)，部署负载均衡服务，详情请参见 [部署负载均衡实例](https://cloud.tencent.com/document/product/214/6574#.E8.B4.AD.E4.B9.B0.E5.B9.B6.E5.88.9B.E5.BB.BA.E8.B4.9F.E8.BD.BD.E5.9D.87.E8.A1.A1.E5.AE.9E.E4.BE.8B)。
3. 创建逻辑层子网，[添加云服务器](https://cloud.tencent.com/document/product/215/4927#.E5.90.91.E5.AD.90.E7.BD.91.E4.B8.AD.E6.B7.BB.E5.8A.A0.E4.BA.91.E4.B8.BB.E6.9C.BA)。
4. 创建数据层子网，添加云数据库，详情请参见 [购买云数据库](https://cloud.tencent.com/document/product/236/3128)。
5. 分别为三个子网配置网络 ACL，配置规则请参见上文 [网络 ACL](#guize)，操作详情请参见 [快速入门](https://cloud.tencent.com/document/product/215/8119)。
