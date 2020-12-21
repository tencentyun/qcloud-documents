腾讯云 DNSPod 解析是国际领先的域名解析平台，65个境内云集群节点，12个境外云集群节点，单机解析可达千万次/秒，为超过650万的域名提供域名解析，日处理 DNS 请求超210亿次，每月成功防御 DNS 攻击超过2000次。

集群内多节点不仅可以提供用户解析请求的就近访问，而且兼备完善的异地灾备机制。同时集群内解析可以达到秒级同步，在 Web 上修改记录，可以瞬间（最快1秒、最慢5秒）将记录同步至所有后端 DNS 集群，实现在 DNSPod 秒级生效（递归 DNS 受 TTL 设置的控制，所以终端用户的实际生效时间取决于域名解析记录里设置的 TTL）。

使用不同套餐版本的解析分别为不同集群，每种集群对应的 DNS 地址是不同的：
<table>
<thead>
<tr>
<th width="20%">解析套餐版本</th>
<th>DNS 地址</th>
<th>备注</th>
</tr>
</thead>
<tbody><tr>
<td>免费 DNS 地址</td>
<td>DNS 解析 DNSPod 为每个用户随机分配了2个组合 DNS 地址，若需要查询您专属的 DNS 地址，请您 <a href="https://cloud.tencent.com/document/product/302/5518#.E6.9F.A5.E7.9C.8B-dns-.E6.9C.8D.E5.8A.A1.E5.99.A8">查看 DNS 服务器</a>。</td>
<td>对应10个节点</td>
</tr>
<tr>
<td>个人专业版套餐</td>
<td>ns3.dnsv2.com/ns4.dnsv2.com</td>
<td>对应12个节点</td>
</tr>
<tr>
<td>企业基础版套餐</td>
<td>ns3.dnsv3.com/ns4.dnsv3.com</td>
<td>对应14个节点</td>
</tr>
<tr>
<td>企业标准版套餐</td>
<td>ns3.dnsv4.com/ns4.dnsv4.com</td>
<td>对应18个节点</td>
</tr>
<tr>
<td>企业旗舰版套餐</td>
<td>ns3.dnsv5.com/ns4.dnsv5.com</td>
<td>对应22个节点</td>
</tr>
</tbody></table>
