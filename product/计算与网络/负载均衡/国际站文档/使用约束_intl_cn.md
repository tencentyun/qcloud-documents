腾讯云负载均衡使用时有一些通用限制，不同类型的负载均衡实例也有该类型特定的使用限制。有关负载均衡类型的更多内容，请参考 [产品定位](https://cloud.tencent.com/document/product/214/8847)。
<table>
<tbody>
<tr><th></th><th>资源</th><th>默认限制</th></tr>
<tr>
  <td  rowspan="4">负载均衡实例</td>
  <td>一个账号可创建的公网 CLB 实例数量</td><td>100</td>
</tr>
<tr>
  <td>一个账号可创建的内网 CLB 实例数量</td><td>100</td>
</tr>
<tr>
  <td>一个 CLB 实例可添加的监听器数量</td><td>50</td>
</tr>
<tr>
  <td>CLB 实例监听可选择的端口</td><td>端口为1 - 65535的整数</td>
</tr>

<tr>
  <td  rowspan="3">应用型负载均衡</td>
  <td>一个应用型 CLB 实例中，HTTP/HTTPS 监听可配置的域名和 URL 转发规则数量</td><td>50</td>
</tr>
<tr>
  <td>一个应用型 CLB 实例的转发规则可绑定的服务器数量</td><td>100</td>
</tr>
<tr>
  <td>一个应用型 CLB 实例的前端端口可对应的后端端口数量</td><td>多个端口</td>
</tr>

<tr>
  <td rowspan="2">传统型负载均衡</td>
  <td>一个传统型 CLB 实例的监听器可绑定的服务器数量</td><td>100</td>
</tr>  
<tr>
  <td>一个传统型 CLB 实例的前端端口可对应的后端端口数量</td><td>1个端口</td>
</tr>
</tbody>
</table>

若 CLB 关联的云服务器 CVM 由于欠费被隔离（如进入回收站，或按量计费被清退的云服务器），CLB **不会** 解除与该云服务器的绑定关系。
