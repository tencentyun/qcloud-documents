弹性公网 IP（EIP） API 已全面升级至3.0版本，基于2.0版本接口访问时延较高和使用复杂的考虑，原弹性公网 IP  API2.0 接口服务将不再提供技术支持，并于北京时间2023年1月1日起下线。如果您的业务还在使用弹性公网 IP API2.0 相关接口，建议尽快将服务升级至 API3.0 接口，以免对您的业务造成影响，详情请参见 [API 3.0 文档](https://cloud.tencent.com/document/product/215/15755#.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91IP.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3)。

请您参照如下对比，找到您需要升级的新接口，完成升级：
<table>
<tr>
<th>API 2.0</th>
<th>API 3.0</th>
</tr>
<tr>
<td>CreateEip</td>
<td><a href="https://cloud.tencent.com/document/api/215/16699">AllocateAddresses</a></td>
</tr>
<tr>
<td>DeleteEip</td>
<td><a href="https://cloud.tencent.com/document/api/215/16705">ReleaseAddresses</a></td>
</tr>
<tr>
<td>DescribeEip</td>
<td><a href="https://cloud.tencent.com/document/api/215/16702">DescribeAddresses</a></td>
</tr>
<tr>
<td>DescribeEipQuota</td>
<td><a href="https://cloud.tencent.com/document/api/215/16701">DescribeAddressQuota</a></td>
</tr>
<tr>
<td>EipBindInstance</td>
<td><a href="https://cloud.tencent.com/document/api/215/16700">AssociateAddress</a></td>
</tr>
<tr>
<td>EipUnBindInstance</td>
<td><a href="https://cloud.tencent.com/document/api/215/16703">DisassociateAddress</a></td>
</tr>
<tr>
<td>TransformWanIpToEip</td>
<td><a href="https://cloud.tencent.com/document/api/215/16706">TransformAddress</a></td>
</tr>
</table>
