SSL VPN 网关是 VPC 建立 SSL VPN 连接的出口网关 ，主要用于腾讯云 VPC 和客户移动端建立安全可靠的加密网络通信。

## 前提条件
已创建 VPC，详情请参考 [创建私有网络](https://cloud.tencent.com/document/product/215/36515)。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 网关**，进入管理页。
3. 在 VPN 网关管理页面，单击**+新建**。
4. 在弹出的**新建 VPN 网关**对话框中，配置如下网关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/24e073cdbc0df83e5bc4388695cd4507.png)
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
<td>可用区</td>
<td>选择当前网关所在的可用区。</td>
</tr>
<tr>
<td>协议类型</td>
<td>支持 IPSec 和 SSL 两种协议类型。</td>
</tr>
<tr>
<td>带宽上限</td>
<td>请根据业务实际情况，合理设置 VPN 网关带宽上限。 </td>
</tr>
<tr>
<td>关联网络</td>
<td><ul><li>此处表示您将创建云联网类型 VPN 还是私有网络类型的 VPN，通常我们也称为 CCN 型 VPN 网关、VPC 型 VPN 网关。如果您需要通过 VPN 连接实现与多 VPC 网络，或其他专线网络的互通，您可以勾选<b>云联网</b>。</li>
<dx-alert infotype="notice" title="">
暂不支持 CCN 类型 VPN 网关创建时直接关联云联网实例。请在完成 VPN 网关创建后，在详情页关联云联网实例。如您创建是策略型的 VPN 通道，您还需在 VPN 网关的 IDC 网段中启用发布至云联网的路由。
</dx-alert>
<li>如果您需要通过 VPN 连接实现与单 VPC 网络的互通，您可以勾选<b>私有网络</b>。</li></ul></td>
</tr>
<tr>
<td>所属网络</td>
<td>仅当关联网络为私有网络时，此处需要选择 VPN 网关将要关联的具体私有网络。
云联网实例需要创建网关后在详情页进行绑定，详情请参见 <a href="https://cloud.tencent.com/document/product/554/71642">绑定云联网实例</a>。</td>
</tr>
<tr>
<td>SSL 连接数</td>
<td>“协议类型”选择 “SSL” 需要配置该项，SSL 连接所支持的数量与网关相关，具体请参见 <a href="https://cloud.tencent.com/document/product/554/18982">使用限制</a>。</td>
</tr>
<tr>
<td>标签</td>
<td>标签是对 VPN 网关资源的标识，目的是为了方便更快速的查询和管理 VPN 网关资源，非必选配置，您可按需定义。</td>
</tr>
<tr>
<td>计费方式</td>
<td>SSL VPN目前仅支持按流量计费。</td>
</tr>
</table>
5. 完成网关参数设置后，单击<b>创建</b>。
