WAN（Wide Area Network）口为广域网端口，Edge 设备通过该端口，将您 LAN 口所连接的本地网络连接至腾讯云 SD-WAN 局域网中，您便可通过腾讯云 SD-WAN 局域网与其他分支机构互通。本文为您介绍如何在控制台配置 WAN 口。

## 操作步骤
1. 登录 [SD-WAN 接入服务控制台](https://console.cloud.tencent.com/sas/edge)，并在实例列表中，单击目标实例 ID。
2. 在实例详情页的左侧导航栏，选择**设备配置** > **接口配置**。
3. 在**接口配置**页面，选择物理接口 WAN1， 并在“基本信息”区域，单击**修改**。
![](https://main.qcloudimg.com/raw/ce8448a1369120d3cda49f0fe98f3b84.png)
4. 在**编辑接口**对话框中，配置以下信息，并单击**确定**。[](id:step4)
![](https://main.qcloudimg.com/raw/f2b072cb9edca6b71542a021403434fc.png)
<table>
<thead>
<tr>
<th>字段名称</th>
<th>字段说明</th>
</tr>
</thead>
<tbody><tr>
<td>名称</td>
<td>该 WAN 接口的名称。</td>
</tr>
<tr>
<td>接入方式</td>
<td>具有 Internet、专线和冗余三种方式。<ul><li>Internet：通过 VPN 隧道通信。</li><li>专线：通过专线通信，若选择<b>专线-静态</b>路由模式时，可以选择绑定对应腾讯云专线，绑定专线时需配置 VLAN ID、对端 IP 和本端 IP。</li><li>冗余：为已配置好的接口做备份。选择“冗余”后，还需选择具体备份的设备和接口，适用于双设备热备的场景。</li></ul> </td>
</tr>
<tr>
<td>连接类型</td>
<td>具有 DHCP、静态和 PPPOE 三种类型。<ul><li>DHCP：WAN 口将通过 DHCP 协议动态获取 IP 地址，进而进行网络访问。</li><li>静态：通过为 WAN 口静态指定 IP 地址，进而进行网络互访。选择此种连接类型后，还需编辑 WAN 口的 IP 地址和 Edge 设备的网关 IP 地址。</li><li>PPPOE：适用于 Edge 设备 WAN 口需通过运营商拨号方式进行网络互访的场景，选择此种连接类型后，需要您输入运营商提供的 PPPOE 账号和密码。</li></ul> </td>
</tr>
<tr>
<td>NAT</td>
<td>开启后，可以将腾讯云 SD-WAN 局域网的内网地址转换成公网地址。 </td>
</tr>
<tr>
<td>MTU</td>
<td>最大运输单元，默认为1500字节，范围为：[512,1500]。 </td>
</tr>
</tbody></table>
5. （可选）重复 [步骤4](#step4)，配置其他 WAN 接口。
