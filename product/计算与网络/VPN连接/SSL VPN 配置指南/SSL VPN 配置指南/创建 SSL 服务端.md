SSL VPN 网关创建完成后，需要在腾讯云侧创建 SSL 服务端，为用户侧提供 SSL 服务。

## 前提条件
- 已[ 创建 SSL VPN 网关](https://cloud.tencent.com/document/product/554/63716) 
- 已[ 创建 VPC](https://cloud.tencent.com/document/product/215/36515) 


## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 服务端**，进入管理页面。
3. 在 VPN 网关管理页面，单击**+新建**。
4. 在弹出的 **SSL 服务端**对话框中，配置如下网关参数。
![](https://qcloudimg.tencent-cloud.cn/raw/1f05ce498eaec55ac834073bf42f464d.png)
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
<td>VPN 网关</td>
<td>选择创建好的 SSL VPN 网关。</td>
</tr>
<tr>
<td>本端网段</td>
<td>填写与客户移动端通信的腾讯云访问网段。</td>
</tr>
<tr>
<td>客户端网段</td>
<td>填写分配给用户侧进行通信的网段，该网段不可和 SSL 服务端网段重叠，且地址池掩码需小于29。</td>
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
<td>目前支持 SHA1 和  MD5 两种认证算法。</td>
</tr>
<tr>
<td>加密算法</td>
<td>目前支持 AES-128-CBC、AES-192-CBC 和 AES-256-CBC 加密算法。</td>
</tr>
<tr>
<td>是否压缩</td>
<td>否</td>
</tr>
</table>
5. 完成网关参数设置后，单击**创建**启动 SSL 服务端创建，此时**状态**为**创建中**，等待约1～2分钟，创建成功的 SSL 服务端状态为**运行中**。
![](https://qcloudimg.tencent-cloud.cn/raw/101ee26ade0ffa4822dae0237693ae04.png)
