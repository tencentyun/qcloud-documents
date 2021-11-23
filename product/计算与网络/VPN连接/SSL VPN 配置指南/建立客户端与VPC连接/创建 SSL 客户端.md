SSL VPN 网关和 SSL 服务端创建完成后，您还需要在腾讯云侧创建 SSL 客户端。SSL 客户端记录了腾讯云分配给用户的 SSL 证书信息，即用于服务端和用户侧移动端进行双向认证的 SSL 证书。您可以下载该证书至移动端，并通过 OpenVPN 与腾讯云进行通信。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 客户端**，进入管理页面。
3. 在 SSL 客户端管理页面，单击**+新建**。
4. 在弹出的 **SSL 客户端**对话框中，配置如下参数。
![](https://qcloudimg.tencent-cloud.cn/raw/cc42b0c61eb77ec1e284df85a36304f6.png)
<table>
<tr>
<th width="12%">参数名称</th>
<th>参数说明</th>
</tr>
<tr>
<td>名称</td>
<td>填写 SSL 客户端名称，不超过60个字符。</td>
</tr>
<tr>
<td>地域</td>
<td>展示 SSL 服务端所在地域。</td>
</tr>
<tr>
<td>SSL 服务端</td>
<td>选择创建好的 SSL 服务端。</td>
</tr>
</table>
5. 完成 SSL 客户端参数设置后，单击**确定**，当**证书状态**为**可用**表示创建完成。
![](https://qcloudimg.tencent-cloud.cn/raw/a1377b94b539a8ecd9a4f13b5bea2415.png)


