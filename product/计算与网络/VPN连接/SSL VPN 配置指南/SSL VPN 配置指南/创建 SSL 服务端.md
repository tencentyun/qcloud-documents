SSL VPN 网关创建完成后，需要在腾讯云侧创建 SSL 服务端，为用户侧提供 SSL 服务。


## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 服务端**，进入管理页面。
>?一个 VPN 网关仅支持关联一个 SSL 服务端，详情请参见 [使用限制](https://cloud.tencent.com/document/product/554/18982)。
>
3. 在 SSL 服务端管理页面，单击**+新建**。
4. 在弹出的 **新建 SSL 服务端**对话框中，配置如下参数。
>?在 Windows 系统下，如果您的客户端 OpenVPN 是3.4.0及以上版本，那么 SSL 服务端配置时需要配置加密和认证算法，其中认证算法仅支持 SHA1。
>
<table>
<tr>
<th width="15%">参数名称</th>
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
<td>VPN 网关</td>
<td>选择创建好的 SSL VPN 网关。</td>
</tr>
<tr>
<td>本端网段</td>
<td>客户移动端访问的云上网段。</td>
</tr>
<tr>
<td>客户端网段</td>
<td>分配给用户移动端进行通信的网段，该网段请勿与腾讯侧 VPC CIDR 冲突，同时也不能与您本地的网段冲突。</td>
</tr>
<tr>
<td>协议</td>
<td>服务端传输协议。</td>
</tr>
<tr>
<td>端口</td>
<td>填写 SSL 服务端用于数据转发的端口。</td>
</tr>
<tr>
<td>认证算法</td>
<td>目前支持 SHA1 和 MD5 两种认证算法。</td>
</tr>
<tr>
<td>加密算法</td>
<td>目前支持 AES-128-CBC、AES-192-CBC 和 AES-256-CBC 加密算法。</td>
</tr>
<tr>
<td>是否压缩</td>
<td>否。</td>
</tr>
<tr>
<td>认证方式</td>
<td><b>证书认证</b>和<b>证书认证 + 身份认证</b>两种方式，本示例以证书认证为例。<ul>
<li>证书认证：该认证方式默认 SSL 服务端可被 SSL 客户端全量访问。</li>
<li>证书认证 + 身份认证：该认证方式仅允许在控制策略中的访问策略连接，您可选择为特定用户组或全部用户配置访问策略，勾选后需要选择对应的 EIAM 应用。</li>
</ul></td>
</tr>
</table>
5. 完成网关参数设置后，单击**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/6ef993e21f3dabdfd111926098cfacbc.png)
