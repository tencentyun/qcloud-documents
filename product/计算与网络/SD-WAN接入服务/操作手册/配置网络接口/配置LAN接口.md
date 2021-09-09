LAN（Local Area Network）即局域网端口，Edge 设备通过 LAN 口连接本地客户端或交换机，进而实现本地网络与腾讯云通信。本文将为您介绍如何在控制台配置 SD-WAN 接入服务 LAN 口。

## 操作步骤
1. 登录 [SD-WAN 接入服务控制台](https://console.cloud.tencent.com/sas/edge)。
2. 在 Edge 设备页面的实例列表中，单击目标实例 ID。
3. 在实例详情页面的左侧导航栏，选择**设备配置** > **接口配置**。
4. 在**接口配置**页面，选择物理接口 LAN1，并在页面右上角开启**高级模式**。
![](https://main.qcloudimg.com/raw/f4b3a700124d25d6e2fb21fc20360ce0.png)
5. 在**基本信息**区域，单击**修改**。
 ![](https://main.qcloudimg.com/raw/a944c19908dbc8c6b5da4f0778d615d8.png)
6. 在**编辑接口**弹窗中，填写接口名称和 MTU 信息。
   - **名称**：LAN 接口的名称。
   - **MTU**：最大运输单元，默认为 1500 字节，范围为 [512,1500]。
![](https://main.qcloudimg.com/raw/c86157783e9181062e02512888e4018c.png)
7. 在**已关联逻辑接口**区域的逻辑接口卡片右上角，单击<img src="https://main.qcloudimg.com/raw/463afbc4198fb885dbb914309ec143f8.png" style="margin:0;" />，并选择**编辑**。
![](https://main.qcloudimg.com/raw/8000e45063474c45917bb5d1e874eddc.png)
8. 在**编辑接口**弹窗中，填写以下信息，单击**确定**。
  ![](https://main.qcloudimg.com/raw/82435abfd9519e80ecfd260d4040e449.png)
>!系统创建的默认逻辑接口不允许更改 DHCP 字段。
<table>
<tr>
<th>字段名称</th>
<th>字段说明</th>
</tr>
<tr>
<td>名称</td>
<td>逻辑接口的名称。</td>
</tr>
<tr>
<td>VLAN ID</td>
<td>物理接口 VLAN ID，默认为1，范围为 [1,4096]。</td>
</tr>
<tr>
<td>IP 地址</td>
<td>逻辑接口上的 IP 地址，且必须与 DHCP 同一网段。</td>
</tr>
<tr>
<td>关联物理接口</td>
<td>至少勾选一个 LAN 口，一个 LAN 口最多可以关联5个逻辑接口。</td>
</tr>
<tr>
<td>DHCP</td>
<td>通过 DHCP 协议动态获取 IP 地址。</td>
</tr>
<tr>
<td>DHCP 地址池</td>
<td>仅支持192、172、10开头的三大私有网段。</td>
</tr>
</table>
9. （可选）若当前 LAN 需关联多个逻辑接口，请按以下操作关联：
>?一个 LAN 口最多可以关联5个逻辑接口。
>
   1. 在**接口配置**页面，单击目标 LAN 口，并在页面上方，单击**逻辑接口**页签。
   2. 在**逻辑接口**页面，单击**新建**。
   ![](https://main.qcloudimg.com/raw/4cf610226422790fa6967d3993868bbf.png)
   3. 在**新建接口**弹窗中，配置以下信息，单击**确定**。
![](https://main.qcloudimg.com/raw/b123d756d83d104707a7e5c7977a5834.png)
<table>
<tr>
<th>字段名称</th>
<th>字段说明</th>
</tr>
<tr>
<td>名称</td>
<td>逻辑接口的名称。</td>
</tr>
<tr>
<td>VLAN ID</td>
<td>物理接口 VLAN ID，默认为1，范围为 [1,4096]。</td>
</tr>
<tr>
<td>IP 地址</td>
<td>逻辑接口上的 IP 地址，且必须与 DHCP 同一网段。</td>
</tr>
<tr>
<td>关联物理接口</td>
<td>至少勾选一个 LAN 口，一个 LAN 口最多可以关联5个逻辑接口。</td>
</tr>
<tr>
<td>DHCP</td>
<td>通过 DHCP 协议动态获取 IP 地址。</td>
</tr>
</table>	
10. （可选）重复步骤8-步骤9，配置其他 LAN 接口。


