## 前提条件
在配置 VPN 路由策略前，请确保已完成 VPN 网关、对端网关及 VPN 通道的配置。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左导航栏中 **VPN 连接** > **VPN 网关**。
3. 在 **VPN 网关**页面，选择地域和私有网络，单击 VPN 网关实例 ID 进入详情页。
4. 在**实例详情**页面，单击**路由表**页签。
   ![](https://main.qcloudimg.com/raw/d261071d65c453ecf21d3980d1b3a8cd.png)
5. 单击**新增路由**，并配置路由策略。
![](https://main.qcloudimg.com/raw/288637983594aa439f67c2ee00a7a12a.png)
>?
>- VPN 网关路由表新增路由时，列表默认显示 VPN 网关下所有 VPN 通道（即 VPN 网关下所有 SPD 策略型和路由型 VPN 通道）。
>- SPD 策略型通道无需添加路由，仅路由型通道根据您的通信需要添加对应的路由。
>
<table>
<tr>
<th>配置项</th>
<th>说明</th>
</tr>
<tr>
<td>目的端</td>
<td>填写要访问的对端网络的网段。</td>
</tr>
<tr>
<td>下一跳类型</td>
<td>支持<b> VPN 通道</b>和<b>云联网</b>类型。
<dx-alert infotype="explain" title="">
如果是 CCN 型 VPN 网关，且 VPN 网关已关联至云联网实例时，则下一跳到<b>云联网</b>的路由策略系统将自动学习到并展示在路由条目中，请勿手动配置重复路由。
</dx-alert>
</td>
</tr>
<tr>
<td>下一跳</td>
<td>选择具体的下一跳实例 ID。<ul><li>如果<b>下一跳类型</b>为<b> VPN 通道</b>，则选择已创建的 VPN 通道。</li><li>如果<b>下一跳类型</b>为<b>云联网</b>，则系统自动展示该 VPN 网关关联的云联网实例。</li></ul></td>
</tr>
<tr>
<td>权重</td>
<td>选择通道的权重值：<ul><li>0：优先级高。</li><li>100：优先级低。</li></ul>
<dx-alert infotype="explain" title="">
主备通道场景请为主通道选择高优先级，备通道选择低优先级，其他情况请选默认值即可。
</dx-alert>
</td>
</tr>
<tr>
<td>新增一行</td>
<td>可添加多条路由策略。</td>
</tr>
<tr>
<td>删除</td>
<td>可删除路由策略，最后一条不允许删除。</td>
</tr>
</table>
6. 完成路由策略的配置后，单击**确定**。
7. 其他可执行操作。
  1. 启动、或禁用路由策略。
>!
>- 禁用路由策略：单击某条处于启用状态的路由策略右侧的图标<img src="https://qcloudimg.tencent-cloud.cn/raw/2913784b020055bf99f4d06f94a015c0.png" width="5%">可禁用该条路由策略。路由条目禁用可能导致业务中断，请谨慎评估后再操作。
>- 启用路由策略：单击某条处于禁用状态的路由策略右侧的图标<img src="https://qcloudimg.tencent-cloud.cn/raw/d60e0509787d8060bb522b925dd7bbd6.png" width="5%">，可启用该条路由策略。
>
 ![](https://main.qcloudimg.com/raw/1d2b107d0c80bb1a0a291b6e68f7455f.png)
  2. 已禁用的路由策略支持删除。
>!路由策略删除可能存在的业务影响，请谨慎评估后再操作。
>
 ![](https://main.qcloudimg.com/raw/dfb2085c28e54597fd1d399091cd9826.png)


