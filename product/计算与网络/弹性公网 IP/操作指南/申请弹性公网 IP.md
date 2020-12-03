弹性公网 IP（EIP）是可以独立购买和持有的公网 IP 地址资源，您可根据如下操作申请 EIP。

## 费用说明
申请 EIP 后，不同类型账户的费用说明如下：
<table>
<thead>
<tr>
<th>账户类型</th>
<th align="center">计费模式</th>
<th>计费说明</th>
</tr>
</thead>
<tbody><tr>
<td>传统账户类型</td>
<td align="center">-</td>
<td>EIP 仅收取 <a href="https://cloud.tencent.com/document/product/1199/41692#ip" target="_blank">IP 资源费用</a>。</td>
</tr>
<tr>
<td rowspan="4">标准账户类型</td>
<td align="center"><a href="https://cloud.tencent.com/document/product/1199/41692#1" target="_blank">按流量</a></td>
<td>EIP 仅收取 <a href="https://cloud.tencent.com/document/product/1199/41692#ip" target="_blank"> IP 资源费用</a>。</td>
</tr>
 <tr>
<td align="center"><a href="https://cloud.tencent.com/document/product/1199/41692#3" target="_blank">包月带宽</a></td>
<td>EIP 不收取 IP 资源费用，仅收取 <a href="https://cloud.tencent.com/document/product/1199/41692#net" target="_blank">公网网络费用</a>。</td>
</tr> 
<tr>
<td align="center"><a href="https://cloud.tencent.com/document/product/1199/41692#2" target="_blank">按小时带宽</a></td>
<td>EIP 不收取 IP 资源费用，仅收取 <a href="https://cloud.tencent.com/document/product/1199/41692#net" target="_blank">公网网络费用</a>。</td>
</tr>
<tr>
<td align="center"><a href="https://cloud.tencent.com/document/product/1199/41692#4" target="_blank">共享带宽包</a></td>
<td>EIP 不收取 IP 资源费用，仅收取 <a href="https://cloud.tencent.com/document/product/1199/41692#net" target="_blank">公网网络费用</a>。</td>
</tr>
</tbody></table>

## 前提条件
若需创建计费模式为共享带宽包的 EIP，请先创建共享带宽包，详情请参见 [创建 IP 带宽包](https://cloud.tencent.com/document/product/684/39942)，一个 IP 带宽包可以加入多个 EIP。

## 操作步骤
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在 EIP 管理页面，选择【地域】，单击【申请】。
3. 在弹出的“申请EIP”窗口中，请按照您的账户类型，分别进行如下操作：
> ? 若您无法确定账户类型，请参见 [账户类型区分](https://cloud.tencent.com/document/product/1199/41692#judge)。
>
 - **传统账户类型**
<table>
<thead>
<tr>
<th width="15%">参数</th>
<th width="85%">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP 地址类型</td>
<td>腾讯云支持常规 IP、加速 IP 和静态单线 IP 等多种类型的 EIP。
<ul>
<li>常规 IP：普通 BGP IP，用于平衡网络质量与成本。</li>
<li>加速 IP：采用 Anycast 加速，使公网访问更稳定、可靠、低延迟，加速 IP 需要开通 <a href="https://cloud.tencent.com/document/product/644">Anycast 公网加速</a> 才可申请，请提交  <a href="https://cloud.tencent.com/apply/p/47mdddtoc56">内测申请</a>。</li>
<li>静态单线 IP：通过单个网络运营商访问公网，成本低且便于自主调度，该功能处于内测阶段，如需体验，请提交 <a href="https://cloud.tencent.com/apply/p/6nzb3jwbsk">内测申请</a>。该功能的地域支持情况请参见 <a href="https://cloud.tencent.com/document/product/1199/41648#.E4.BD.BF.E7.94.A8.E8.A7.84.E5.88.99">使用限制</a></li>
</ul>
</td>
</tr>
<tr>
<td>数量</td>
<td>请按需选择申请的数量且确保 EIP 总数未超过产品总配额，详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6">配额限制</a>。</td>
</tr>
<tr>
<td>标签</td>
<td>如需添加标签可在此进行添加，可通过标签进行权限管理。</td>
</tr>
</tbody></table>
 - **标准账户类型**
<table>
<thead>
<tr>
<th width="15%">参数</th>
<th width="85%">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP 地址类型</td>
<td>腾讯云支持常规 IP、加速 IP 和静态单线 IP 等多种类型的 EIP。
<ul>
<li>常规 IP：普通 BGP IP，用于平衡网络质量与成本。</li>
<li>加速 IP：采用 Anycast 加速，使公网访问更稳定、可靠、低延迟，加速 IP 需要开通 <a href="https://cloud.tencent.com/document/product/644">Anycast 公网加速</a> 才可申请，请提交  <a href="https://cloud.tencent.com/apply/p/47mdddtoc56">内测申请</a>。</li>
<li>静态单线 IP：通过单个网络运营商访问公网，成本低且便于自主调度，该功能处于内测阶段，如需体验，请提交 <a href="https://cloud.tencent.com/apply/p/6nzb3jwbsk">内测申请</a>。该功能的地域支持情况请参见 <a href="https://cloud.tencent.com/document/product/1199/41648#.E4.BD.BF.E7.94.A8.E8.A7.84.E5.88.99">使用限制</a></li>
</ul>
</td>
</tr>
<tr>
<td>计费模式</td>
<td>
<ul>
<li>常规 IP 支持 <a href="https://cloud.tencent.com/document/product/1199/41692#1">按流量</a>、<a href="https://cloud.tencent.com/document/product/1199/41692#3">包月带宽</a>、<a href="https://cloud.tencent.com/document/product/1199/41692#2">按小时带宽</a> 和 <a href="https://cloud.tencent.com/document/product/1199/41692#4">共享带宽包</a> 计费模式，详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41692#net">公网网络费用</a>。
</li>
<li>加速 IP 和静态单线 IP 只支持 <a href="https://cloud.tencent.com/document/product/1199/41692#4">共享带宽包</a> 计费模式，不支持其它计费模式。加速 IP 和静态单线 IP 创建后会自动新增并添加到共享带宽包中。
</li>
</ul>
</td>
</tr>
<tr>
<td>带宽上限</td>
<td>请按需设置带宽上限，合理分配带宽资源。</td>
</tr>
<tr>
<td>包月时长</td>
<td>该选项仅适用计费模式为包月带宽的 EIP，请按需选择包月带宽的购买时长。</td>
</tr>
<tr>
<td>自动续费</td>
<td>该选项仅适用计费模式为包月带宽的 EIP，若勾选此选项，账户余额足够时，EIP 到期后将按月自动续费。</td>
</tr>
<tr>
<td>数量</td>
<td>请按需选择申请的数量且确保 EIP 总数未超过产品总配额，详情请参见 <a href="https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6">配额限制</a>。</td>
</tr>
<tr>
<td>标签</td>
<td>如需添加标签可在此进行添加，可通过标签进行权限管理。</td>
</tr>
</tbody></table>
4. 单击【确定】，完成 EIP 的申请。
5. 在列表中，即可查看已申请的 EIP，此时处于未绑定状态。
> ?建议您及时为处于未绑定状态的 EIP 绑定云资源，保障 IP 资源的合理利用，节省 IP 资源费，IP 资源费按小时计费，精确到秒级，不足一小时，按闲置时间占比收取费用。
>
 ![](https://main.qcloudimg.com/raw/9492216f61d10704015dac0cf217bd01.png)

## 后续步骤
- 若需要为 EIP 绑定云资源，请参见 [EIP 绑定云资源](https://cloud.tencent.com/document/product/1199/41702)。
