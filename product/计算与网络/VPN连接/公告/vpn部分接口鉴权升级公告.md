北京时间2021年7月29日零点后，VPN 部分接口的鉴权功能进行升级优化。升级后，子用户调用该接口需要向主账号申请授权，否则调用失败，申请操作请参见[ 为子账号配置策略授权](#cam)。

## 升级的接口列表
<table>
<tr >
<th colspan=2>接口名称</th><th>接口功能</th></tr>
<tr>
<td rowspan=6>读接口</td>
<td><a href="https://cloud.tencent.com/document/api/215/57676">DescribeVpnGatewayRoutes</a></td>
<td>查询 VPN 网关路由</td></tr>
<tr>
<td>DescribeVpnGatewayCcnRoutes</a></td>
<td>查询 VPN 网关云联网路由</td></tr>
<tr><td><a href="">DescribeVpnConnectionLogs</a></td><td>查询VPN连接日志
</td>
</tr>

<tr>
<td><a href="https://cloud.tencent.com/document/api/215/17515">DescribeVpnConnections</a></td>
<td>查询 VPN 通道列表
</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/17516">DescribeCustomerGateways</a></td>
<td>查询对端网关
</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/17513">DownloadCustomerGatewayConfiguration</a></td><td>下载 VPN 通道配置
</td>
</tr>
<tr>
<td rowspan= 4>写接口</td>
<td><a href="https://cloud.tencent.com/document/api/215/57677">DeleteVpnGatewayRoutes</a></td>
<td>删除 VPN 网关路由
</td>
</tr>
<tr><td><a href="https://cloud.tencent.com/document/api/215/57675">ModifyVpnGatewayRoutes</a></td>
<td>修改 VPN 路由状态
</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/57678">CreateVpnGatewayRoutes</a></td><td>创建 VPN 网关路由
</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/215/43497">ModifyVpnGatewayCcnRoutes</a></td><td>修改 VPN 网关云联网路由
</td>
</tr>

</table>

## 为子账号配置策略授权[](id:cam)
当子用户调用以上升级后的接口失败时，您需通过以下操作为子用户完成策略授权。
1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)。
2. 在左侧导航栏，单击【策略】。
3. 在“策略管理”页面，单击右侧的【全部策略】。
4. 在策略列表中，找到需授权的策略，单击右侧“操作”列的【关联用户/组】。
5. [](id:step4)在弹出的“关联用户/用户组”对话框中，单击左侧列表的目标用户项，将其添加至右侧的“已选择”列表中，单击【确定】。
![](https://main.qcloudimg.com/raw/a10c35e5a71ef2792b1f338441017a8a.png)
6. （可选）若需关联用户组，则在“关联用户/用户组”对话框，单击【切换成用户组】＞【用户组】，重复<a href="#step4"> 步骤5</a>。
   ![](https://main.qcloudimg.com/raw/eb74742271b5d4cfed844e6e1914dbea.png)


