弹性公网 IP 为您提供更加规范和全面 3.0 版本的 API 接口文档，统一的参数风格和公共错误码，统一的 SDK/CLI 版本与 API 文档严格一致，给您带来简单快捷的使用体验。支持全地域就近接入让您更快连接腾讯云产品。

欢迎使用弹性公网 IP （Elastic IP）。

弹性公网 IP （Elastic IP，EIP），简称弹性 IP 地址或弹性 IP。它是专为动态云计算设计的静态 IP 地址，是某地域下一个固定不变的公网 IP 地址。借助弹性公网 IP 地址，您可以快速将地址重新映射到账户中的另一个云服务器实例或 NAT 网关实例，从而屏蔽实例故障。

弹性公网 IP，是可以独立购买和持有的公网 IP 地址资源。用户可以使用弹性公网 IP 的 API，并参照相应的示例，对弹性公网 IP进行相关操作：如创建、绑定、查询、解绑等，如下表所示：
<table>
<thead>
<tr>
<th>接口名称</th>
<th>接口功能</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/16699" target="_blank">AllocateAddresses</a></td>
<td>创建弹性公网 IP</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/16700" target="_blank">AssociateAddress</a></td>
<td>绑定弹性公网 IP</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/16701" target="_blank">DescribeAddressQuota</a></td>
<td>查询弹性公网 IP 配额</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/16702" target="_blank">DescribeAddresses</a></td>
<td>查询弹性公网 IP 列表</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/43278" target="_blank">DescribeSecurityGroupReferences</a></td>
<td>查询安全组被引用信息</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/36271" target="_blank">DescribeTaskResult</a></td>
<td>查询异步任务执行结果</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/16703" target="_blank">DisassociateAddress</a></td>
<td>解绑定弹性公网 IP</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/16704" target="_blank">ModifyAddressAttribute</a></td>
<td>修改弹性公网 IP 属性</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/19214" target="_blank">ModifyAddressesBandwidth</a></td>
<td>调整弹性公网 IP 带宽</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/16705" target="_blank">ReleaseAddresses</a></td>
<td>释放弹性公网 IP</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/16706" target="_blank">TransformAddress</a></td>
<td>普通IP转弹性IP</td>
</tr>
</tbody>
</table>

更多信息，请参见 [弹性公网 IP 相关接口概览](https://cloud.tencent.com/document/product/215/15755#.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91IP.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3)。

请确保在使用这些接口前，已充分了解了 [弹性公网 IP - 产品概述](https://cloud.tencent.com/document/product/1199/41646)。
