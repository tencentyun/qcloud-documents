VPN 网关是 VPN 连接服务的功能实例，因此在使用 VPN 连接实现外部网络到腾讯云 VPC 的网络的安全访问之前，您必须先创建一个 IPsec VPN 网关，本文指导您如何在控制台创建 VPN 网关。

## 前提条件
如需创建 VPC 类型的 VPN 网关，请提前创建好同地域的 VPC 网络，详情请参考 [创建私有网络](https://cloud.tencent.com/document/product/215/36515)。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击【VPN 连接】>【VPN 网关】，进入管理页。
3. 在 VPN 网关管理页面，单击【+新建】。
4. 在弹出的【新建 VPN 网关】对话框中，配置如下网关参数。
<img src="https://main.qcloudimg.com/raw/52f055358ccea8f1679ddb49a49b2d40.png" width="50%" />
<table>
<tr>
<th>参数名称</th>
<th>参数说明</th>
</tr>
<tr>
<td>网关名称</td>
<td>填写 VPN 网关名称，不超过60个字符。</td>
</tr>
<tr>
<td>所在地域</td>
<td>展示 VPN 网关所在地域。</td>
</tr>
<tr>
<td>关联网络</td>
<td>此处表示您将创建云联网类型 VPN 还是私有网络类型的 VPN，通常我们也称为 CCN 型 VPN 网关、VPC 型 VPN 网关。<ul><li>如果您需要通过 VPN 连接实现与多 VPC 网络，或其他专线网络的互通，您可以勾选【云联网】。请注意：当前暂不支持 CCN 型 VPN 网关在创建时直接关联云联网实例，可在完成创建后，进入 VPN 网关详情基本信息页面编辑所属网络关联云联网实例。</li><li>如果您需要通过 VPN 连接实现与单 VPC 网络的互通，您可以勾选【私有网络】。</li></ul></td>
</tr>
<tr>
<td>所属网络</td>
<td>仅当关联网络为【私有网络】时，此处需要选择 VPN 网关将要关联的具体私有网络。</td>
</tr>
<tr>
<td>带宽上限</td>
<td> 请根据业务实际情况，合理设置 VPN 网关带宽上限。</td>
</tr>
<tr>
<td>标签</td>
<td>标签是对 VPN 网关资源的标识，目的是为了方便更快速的查询和管理 VPN 网关资源，非必选配置，您可按需定义。</td>
</tr>
<tr>
<td>计费方式</td>
<td>支持按流量计费和包年包月。按流量计费适用于带宽波动较大的场景；包年包月适用于带宽较稳定的场景。</td>
</tr>
</table>
5. 完成网关参数设置后，单击【创建】启动 VPN 网关的创建，此时【状态】为【创建中】，等待约1～2分钟，创建成功的 VPN 网关状态为【运行中】，系统为 VPN 网关分配一个公网 IP。
<img src="https://main.qcloudimg.com/raw/880187e214d253d4fac8fd135b838ebf.png">
