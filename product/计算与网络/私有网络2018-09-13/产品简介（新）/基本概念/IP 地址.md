腾讯云有两类 IP 地址，公网 IP 地址和内网 IP 地址。如果您不主动做解绑、更换操作，公网 IP 和内网 IP 都不会改变。

## 公网 IP 地址
公网 IP 地址是 Internet 上的非保留地址，有公网 IP 地址的云服务器可以和 Internet 上的其他计算机互相访问。
腾讯云公网 IP 地址有两类，普通公网 IP 和弹性公网 IP，二者都可以为云服务器提供访问公网和被公网访问的能力。
<table>
<thead>
<tr>
<th colspan="2" width="16%">对比项</th>
<th>普通公网 IP</th>
<th>弹性公网 IP</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">访问公网/被公网访问能力</td>
<td colspan="2">二者作为公网 IP，访问公网和被公网访问的能力没有差别。</td>
</tr>
<tr>
<td colspan="2">获取方式</td>
<td>只能在云服务器购买时分配，如购买时未分配，则无法获得。</td>
<td><li>在控制台 <a href="https://cloud.tencent.com/document/product/213/16586#.E7.94.B3.E8.AF.B7.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip" target="_blank">申请弹性公网 IP </a> 获得。</li><li><a href="https://cloud.tencent.com/document/product/213/16586#.E5.85.AC.E7.BD.91-ip-.E8.BD.AC.E5.BC.B9.E6.80.A7-ip" target="_blank">普通公网 IP 转换为弹性公网 IP</a>。</li></td>
</tr>
<tr>
<td colspan="2">特点</td>
<td>与云服务器生命周期一致，云服务器释放后，普通公网 IP 也会释放。</td>
<td><li>独立享有的 IP 资源，可随时与云服务器、NAT 网关等绑定、解绑。</li><li>不再需要时可以释放。</li></td>
</tr>
<tr>
<td colspan="2" >IP 费用</td>
<td>普通公网 IP 可免费使用。</td>
<td><li>绑定：有绑定资源（如云服务器、NAT 网关）时，不收取 <a href="https://cloud.tencent.com/document/product/213/17156" target="_blank">资源占用费</a>。</li>
<li>未绑定：收取资源占用费。</li>
<li>释放：不再收取任何费用。</li>
</td>
</tr>
<tr>
<td colspan="2" rowspan="2">配额</td>
<td>IP 数无固定配额，与可购云服务器配额一致。</td>
<td>每个账户每个地域（Region）可申请：20个。</td>
</tr>
<tr>
<td colspan="2">单台云服务器绑定公网 IP 数配额请参见 <a href="https://cloud.tencent.com/document/product/213/5733#.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E7.BB.91.E5.AE.9A.E5.85.AC.E7.BD.91-ip-.E9.99.90.E5.88.B6" target="_blank">配额说明</a>。
</td>
</tr>
<tr>
<td rowspan="4" >操作</td>
<td>转换 IP</td>
<td>可转换，详情请参见 <a href="https://cloud.tencent.com/document/product/213/16586#.E5.85.AC.E7.BD.91-ip-.E8.BD.AC.E5.BC.B9.E6.80.A7-ip" target="_blank"> 普通公网 IP 转换为弹性公网 IP</a>。<br>普通公网 IP 转换为弹性公网 IP 后，仅 IP 属性改变，IP 地址不变。</td>
<td>弹性公网 IP 不可转换为普通公网 IP。</td>
</tr>
<tr>
<td>更换 IP</td>
<td>可以直接更换普通公网 IP，
详情请参见 <a href="https://cloud.tencent.com/document/product/213/16642" target="_blank"> 更换公网 IP 地址</a>。</td>
<td>不可以直接更换弹性公网 IP，您可以解绑并释放后，申请新的弹性公网 IP 并绑定。</td>
</tr>
<tr>
<td>释放 IP</td>
<td>如果您不再需要该公网IP，可在 <a href="https://console.cloud.tencent.com/cvm" target="_blank">云服务器控制台 </a>的操作栏下，选择【更多】>【IP/网卡】>【退还公网 IP】进行退还。</td>
<td>可以在弹性公网 IP 控制台释放，详情请参见 <a href="https://cloud.tencent.com/document/product/213/16586#.E9.87.8A.E6.94.BE.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip" target="_blank"> 释放弹性公网 IP</a>。</td>
</tr>
<tr>
<td>找回 IP</td>
<td colspan="2">您可以找回您使用过、且未被其它用户使用的普通公网 IP/弹性公网 IP，详情请参见 <a href="https://cloud.tencent.com/document/product/213/34376" target="_blank"> 找回公网 IP 地址</a>。</td>
</tr>
</tbody></table>

## 内网 IP 地址
内网 IP 地址是腾讯云内网服务的实现形式，无法通过 Internet 访问。每个云服务器实例都具有分配内网 IP 的默认网络接口（即 eth0 ），内网 IP 地址可由系统自动分配，在私有网络环境下，内网 IP 地址也可由用户自定义。

### 属性
- 内网服务具有用户属性，不同用户间相互隔离，即默认无法经由内网访问另一个用户的云服务。
- 内网服务具有地域属性，不同地域间相互隔离，即默认无法经由内网访问同账户下不同地域的云服务。

### 适用场景
内网 IP 可以用于负载均衡与云服务器实例之间内网互访、云服务器实例与其他云服务（如 TencentDB）之间内网互访。

### 相关操作
- 获取实例的内网 IP 地址和设置 DNS，请参见 [获取内网 IP 地址和设置 DNS](https://cloud.tencent.com/document/product/213/17941)。
- 修改私有网络中云服务器实例的内网 IP，请参见 [修改内网 IP 地址](https://cloud.tencent.com/document/product/213/16561)。
