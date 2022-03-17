SSL VPN 网关是 VPC 建立 SSL VPN 连接的出口网关 ，与 SSL 客户端（客户移动端）配合使用，主要用于腾讯云 VPC 和客户移动端建立安全可靠的加密网络通信。


## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 网关**，进入管理页。
3. 在 VPN 网关管理页面，单击**+新建**。
4. 在弹出的**新建 VPN 网关**对话框中，配置如下网关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/7dc91a84f6b4864640c52fc50a1e96fe.png)
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
<td>连接客户移动端的数量。</td>
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
<td>请根据业务实际情况，合理设置 VPN 网关带宽上限。 </td>
</tr>
</table>
5. 完成网关参数设置后，单击**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/984c75f41cc85cc8ad17dfa2e385015a.png)
