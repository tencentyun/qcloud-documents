## 简介

弹性公网 IP （Elastic IP，简称 EIP），是可以独立购买和持有的、某个地域下固定不变的公网 IP 地址。借助弹性公网 IP 地址，您可以快速将地址重新映射到账户中的另一个实例或 NAT 网关实例，从而屏蔽实例故障。

弹性公网 IP 未进行释放前，您可以将其一直保留于您的账号中。相较于公网 IP 仅可跟随云服务器一起申请释放，弹性公网 IP 可以与云服务器的生命周期解耦，作为云资源单独进行操作。例如，若您需要保留某个与业务强相关的公网 IP，可以将其转为弹性公网 IP 保留在您的账号中。

## 规则与限制

<table>
	<tr><th>规则/限制</th><th>使用说明</th></tr>
	<tr><td>弹性公网 IP 使用规则</td><td>详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41648#.E4.BD.BF.E7.94.A8.E8.A7.84.E5.88.99">使用规则</a>。</td></tr>
	<tr><td>弹性公网 IP 配额限制</td><td>详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41648#eip-.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6">EIP 配额限制</a>。</td></tr>
	<tr><td>云服务器绑定公网 IP 限制</td><td>详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41648#.E7.BB.91.E5.AE.9A.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E9.99.90.E5.88.B6">绑定云服务器限制</a>。</td></tr>
</table>


## EIP 和普通公网 IP 的区别
公网 IP 地址是 Internet 上的非保留地址，有公网 IP 地址的云服务器可以和 Internet 上的其他计算机互相访问。普通公网 IP 和 EIP 均为公网 IP 地址，二者均可为云资源提供访问公网和被公网访问的能力。
- 普通公网 IP：仅能在云服务器购买时分配且无法与云服务器解绑，如购买时未分配，则无法获得。
- EIP：可以独立购买和持有的公网 IP 地址资源，可随时与云服务器、NAT 网关、弹性网卡和高可用虚拟 IP 等云资源绑定或解绑。
<dx-alert infotype="explain" title="">
当前普通公网 IP 仅支持常规 BGP IP 线路类型。
</dx-alert>
与普通公网 IP 相比， EIP 提供更灵活的管理方式，如下表所示，详情请参见 <a href="https://cloud.tencent.com/document/product/215/38109#.E5.85.AC.E7.BD.91-ipv4-.E5.9C.B0.E5.9D.80">公网 IPv4 地址</a>。
<table>
<thead>
<tr>
<th>对比项</th>
<th>普通公网 IP</th>
<th> EIP</th>
</tr>
</thead>
<tbody><tr>
<td>访问公网/被公网访问</td>
<td>&#10003; </td>
<td>&#10003; </td>
</tr>
<tr>
<td>独立购买与持有</td>
<td>×</td>
<td>&#10003; </td>
</tr>
<tr>
<td>自由绑定与解绑</td>
<td>×</td>
<td>&#10003; </td>
</tr>
<tr>
<td>实时调整带宽<sup>1</sup></td>
<td>&#10003; </td>
<td>&#10003; </td>
</tr>
<tr>
<td>IP 资源占用费</td>
<td>×</td>
<td>&#10003; </td>
</tr>
</tbody></table>
<dx-alert infotype="explain" title="">
[公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=8) 仅支持调整 EIP 的带宽，具体操作请参见 [调整网络配置](https://cloud.tencent.com/document/product/1199/41705)。普通公网 IP 的带宽调整请参见 [调整普通公网 IP 网络配置](https://cloud.tencent.com/document/product/213/15517)。
</dx-alert>
EIP 可以与云资源的生命周期解耦合，单独进行操作。例如，若您需要保留某个与业务强相关的公网 IP 地址，可以将普通公网 IP 转换为 EIP 保留在您的账号中。

