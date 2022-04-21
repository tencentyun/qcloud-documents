VPN 网关是 VPN 连接服务的功能实例，因此在使用 VPN 连接实现外部网络到腾讯云 VPC 的网络的安全访问之前，您必须先创建一个 IPsec VPN 网关，本文指导您如何在控制台创建 VPN 网关。

## 前提条件
如需创建 VPC 类型的 VPN 网关，请提前创建好同地域的 VPC 网络，详情请参考 [创建私有网络](https://cloud.tencent.com/document/product/215/36515)。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 网关**，进入管理页。
3. 在 VPN 网关管理页面，单击 **+新建**。
4. 在弹出的**新建 VPN 网关**对话框中，配置如下网关参数。
>?
>- 200Mbps、500Mbps和1000Mbps带宽目前仅华北地区（北京）、华东地区（上海）、华南地区（广州）、西南地区（成都）、港澳台地区（香港）、华东地区（南京）和华北地区（北京金融）等可用区开放，如需请 <a href="https://console.cloud.tencent.com/workorder/category">提交工单</a>。
>- 200Mbps、500Mbps和1000Mbps带宽仅支持新建网关，存量网关暂不支持。
>- 如果 VPN 网关使用200Mbps、500Mbps和1000Mbps规格的带宽，VPN 通道加密协议建议使用 AES128+MD5。
>
![](https://qcloudimg.tencent-cloud.cn/raw/5930468229109601b94a48aea14018cf.png)
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
<td>可用区</td>
<td>选择当前网关所在的可用区。</td>
</tr>
<tr>
<td>协议类型</td>
<td>支持 IPSec 和 SSL 两种协议类型。</td>
</tr>
<tr>
<td>关联网络</td>
<td>此处表示您将创建云联网类型 VPN 还是私有网络类型的 VPN，通常我们也称为 CCN 型 VPN 网关、VPC 型 VPN 网关。<ul><li>如果您需要通过 VPN 连接实现与多 VPC 网络，或其他专线网络的互通，您可以勾选<b>云联网</b>。
<dx-alert infotype="notice" title="">
暂不支持 CCN 类型 VPN 网关创建时直接关联云联网实例。请在完成 VPN 网关创建后，在详情页关联云联网实例。如您创建是策略型的 VPN 通道，您还需在 VPN 网关的 IDC 网段中启用发布至云联网的路由。
</dx-alert>
</li><li>如果您需要通过 VPN 连接实现与单 VPC 网络的互通，您可以勾选<b>私有网络</b>。</li></ul></td>
</tr>
<tr>
<td>所属网络</td>
<td>仅当关联网络为<b>私有网络</b>时，此处需要选择 VPN 网关将要关联的具体私有网络。</td>
</tr>
<tr>
<td>带宽上限</td>
<td> 请根据业务实际情况，合理设置 VPN 网关带宽上限。
</td>
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
5. 完成网关参数设置后，单击<b>创建</b>启动 VPN 网关的创建，此时<b>状态</b>为<b>创建中</b>，等待约1～2分钟，创建成功的 VPN 网关状态为<b>运行中</b>，系统为 VPN 网关分配一个公网 IP。
<img src="https://qcloudimg.tencent-cloud.cn/raw/cf34595cf180cf84c867de80898c2d8f.png">

