VPN 网关是 VPN 连接服务的功能实例，因此在使用 VPN 连接实现外部网络到腾讯云 VPC 的网络的安全访问之前，您必须先创建一个SSL VPN 网关，本文指导您如何在控制台创建  SSL VPN 网关。

## 前提条件
已创建 VPC，详情请参考 [创建私有网络](https://cloud.tencent.com/document/product/215/36515)。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 网关**，进入管理页。
3. 在 VPN 网关管理页面，单击**+新建**。
4. 在弹出的**新建 VPN 网关**对话框中，配置如下网关参数。
>?
> - 200MB、500MB和1000MB带宽目前仅华北地区（北京）、华东地区（上海）、华南地区（广州）、西南地区（成都）、港澳台地区（香港）、华东地区（南京）和华北地区（北京金融）等可用区开放，如需请 [提交工单](https://console.cloud.tencent.com/workorder/category)。
> - 200MB、500MB和1000MB带宽仅支持新建网关，存量网关暂不支持。
> - 如果 VPN 网关使用200MB、500MB和1000MB规格的带宽，VPN 通道加密协议建议使用 AES128+MD5。
> 
![](https://qcloudimg.tencent-cloud.cn/raw/77e1f97a3415d9b7e20caf363580a2a2.png)
<table>
<tr>
<th width="12%">参数名称</th>
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
<td>协议类型</td>
<td>选择 SSL。</td>
</tr>
<tr>
<td>SSL 连接数</td>
<td>SSL 连接数规格有5、10、20、50、100、200、500、1000，请依据实际需求选择。</td>
</tr>
<tr>
<td>关联网络</td>
<td>表示您创建私有网络类型的 VPN。</td>
</tr>
<tr>
<td>所属网络</td>
<td>选择 VPN 网关将要关联的具体私有网络。</td>
</tr>
<tr>
<td>带宽上限</td>
<td>请根据业务实际情况，合理设置 VPN 网关带宽上限。</td>
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
5. 完成网关参数设置后，单击**创建**启动 VPN 网关的创建，此时**状态**为**创建中**，等待约1～2分钟，创建成功的 VPN 网关状态为**运行中**，系统为 VPN 网关分配一个公网 IP。
![1.png](/download/attachments/1059338329/1.png?version=2&modificationDate=1632399048042&api=v2)
