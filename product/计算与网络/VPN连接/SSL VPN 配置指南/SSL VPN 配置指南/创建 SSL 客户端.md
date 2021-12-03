SSL VPN 网关和 SSL 服务端创建完成后，您还需要在腾讯云侧创建 SSL 客户端证书。SSL 客户端证书记录了腾讯云分配给用户的 SSL 证书信息，即用于服务端和客户移动端进行双向认证的 SSL 证书。您可以下载该证书至移动端，并通过 OpenVPN 与腾讯云进行通信。


## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 客户端**，进入管理页面。
3. 在 SSL 客户端管理页面，单击**+新建**。
4. 在弹出的**新建 SSL 客户端**对话框中，配置如下参数。
![](https://qcloudimg.tencent-cloud.cn/raw/c19d9edf6ba9ff1ec64089f2602771ce.png)
<table>
<tr>
<th width="12%">参数名称</th>
<th>参数说明</th>
</tr>
<tr>
<td>名称</td>
<td>填写 SSL 服务端名称，不超过60个字符。</td>
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
5. 完成 SSL 客户端参数设置后，单击**创建**启动 SSL 客户务端创建，当**证书状态**为**可用**表示创建完成。
![](https://qcloudimg.tencent-cloud.cn/raw/5173738b6a23084597c1f017fcc52c4e.png)


