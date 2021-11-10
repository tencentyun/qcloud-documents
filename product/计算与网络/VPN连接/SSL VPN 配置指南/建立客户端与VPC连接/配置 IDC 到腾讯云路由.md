SSL VPN 网关、SSL 服务端、SSL 客户端配置完成，需要配置客户侧 IDC 流量到达腾讯云 VPC 内的路由转发策略。

## 前提条件
- 已[ 创建 SSL VPN 网关](https://cloud.tencent.com/document/product/554/63605)。 
- 已[ 创建 SSL 服务端](https://cloud.tencent.com/document/product/554/63606)。 

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击**路由表**，进入管理页面。
3. 在 路由表管理页面，单击**+新建**。
4. 在弹出的 **SSL 客户端**对话框中，配置如下参数。
![](https://qcloudimg.tencent-cloud.cn/raw/ce1ed932b7a10555bc567468459b9f28.png)
<table>
<tr>
<th width="12%">参数名称</th>
<th>参数说明</th>
</tr>
<tr>
<td>目标服务器</td>
<td>填写客户端网段。</td>
</tr>
<tr>
<td>下一跳类型</td>
<td> 选择 VPN 网关。</td>
</tr>
<tr>
<td>下一跳</td>
<td>下一跳选择创建好的具体 VPN 网关实例。</td>
</tr>
</table>
5. 完成参数设置后，单击**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/3965d6cc0aaa41af96f3161020780798.png)
