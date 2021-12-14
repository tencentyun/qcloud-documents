您不仅可以通过 SD-WAN 控制台配置 WAN 口，还可以通过本地 Web 控制台进行配置。本文将介绍如何登录本地 Web 控制台配置 WAN 口和 LAN 口。


## 步骤1：安装 Edge 设备
1. 收到 Edge 设备后，请检查配件是否完整，配件详情请参见 [硬件特性说明](https://cloud.tencent.com/document/product/1277/47251)。
2. 将 WAN 口 和 Modem 相连，LAN 口和本地客户端相连。

## 步骤2：配置本地客户端
配置 Edge 设备前，需要访问 Web 配置的本地客户端开启 DHCP。


### Windows 客户端
为 Windows 客户端配置动态 IP，以 Windows 为例操作步骤如下：
1. 在 Windows 桌面右下角，右键单击网络连接图标，然后单击**打开“网络和 Internet”设置**。
2. 在设置页面，单击**更改适配器选项**。
3. 右键单击所有连接的网络，然后单击**属性**。
4. 双击**Internet 协议版本4（TCP/IPv4）**选项。
![](https://main.qcloudimg.com/raw/6f05aca988fb44f24d9e9d1e2cb8ce6a.png)
5. 在“Internet 协议版本4（TCP/IPv4）属性”弹窗中，选择“自动获得 IP 地址”和“自动获得 DNS 服务器地址”。
6. 设置完成后，单击**确定**。


### Mac 客户端
为 Mac 客户端配置动态 IP，操作步骤如下：
1. 在 Mac 桌面单击**系统偏好设置**图标，然后在互联网和无线选项中，单击**网络**。
2. 在“网络”弹窗中，单击所有连接的网络，并单击**高级**。
3. 在“以太网”设置界面，单击**TCP/IP**页签。
4. 在“配置 IPv4”选项中，选择**使用 DHCP**。
![](https://main.qcloudimg.com/raw/c041c2ed4b383d4aa0033657260b0643.png)
5. 设置完成后，单击**好**。


## 步骤3：配置 Edge 设备
1. 启动 Edge 设备。
2. 在本地 PC 端浏览器访问本地 Web 控制台，即`192.168.2.1`或使用域名方式访问`edge.cloud.tencent.com`，初次访问本地 Web 控制台时，需要设置登录密码。
>?请妥善保管您的登录密码，则需登录 [SD-WAN 接入服务控制台](https://console.cloud.tencent.com/sas/edge) 重新配置。具体操作请参见 [配置 WLAN](https://cloud.tencent.com/document/product/1277/47272)。
>
![](https://main.qcloudimg.com/raw/9c9bd9852c51a58a0b7d2e157d142f3c.png)
3. 滚动鼠标至 Edge 设备详情页面底部，单击**修改配置**。
4. 在修改配置页面进行以下配置：
   1. 在 WAN1 接口页签的 “WAN 配置”对话框中，选择 WAN1 接口接入互联网的方式为 “Internet” 或者“专线”，然后单击**下一步**。
>?Internet 指通过互联网实现网络通信，即 VPN 原理，专线指通过专线实现网络通信。
>
   2. 在 WAN1 接口页签的 “WAN 配置”对话框中，配置接入互联网的类型。
      - 若选择互联方式为 “Internet” ，按照以下说明配置接入互联网类型：
<table>
<thead>
<tr>
<th>字段</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>DHCP 自动获取</td>
<td>通过 DHCP 协议动态获取 IP 地址。</td>
</tr>
<tr>
<td>静态</td>
<td>通过为 WAN 口静态指定 IP 地址，进而进行网络互访。选择此种连接类型后还需编辑 WAN 口的 IP 地址、子网掩码和 Edge 设备的网关 IP 地址。</td>
</tr>
<tr>
<td>PPPOE</td>
<td>适用于 Edge 设备 WAN 口，需通过运营商拨号方式进行网络互访的场景，选择此种连接类型后需要您输入运营商提供的 PPPoE 账号和密码。</td>
</tr>
<tr>
<td>SNAT 转发</td>
<td>开启 SNAT 转发后，由本地局域网向广域网发送的数据默认都经过 NAT 转发。</td>
</tr>
</tbody></table> 
      - 若选择互联方式为“专线”，按照以下说明配置接入互联网类型：
<table>
<thead>
<tr>
<th>字段</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>DHCP 自动获取</td>
<td>通过 DHCP 协议动态获取 IP 地址。</td>
</tr>
<tr>
<td>SSID 广播</td>
<td>绑定对应腾讯云专线，绑定专线时需配置 “VLAN ID”、“对端 IP”和“本端 IP”。</td>
</tr>
</tbody></table>   
   3. 单击【WAN2 接口】页签， 并配置 WAN2 接口接入互联方式和接入互联类型，单击**下一步**。
>? 
>- 若 WAN1 接口的互联方式为 “Internet”，则 WAN2 接口的互联方式默认为 “专线”。
>- 若 WAN1 接口的互联方式为 “专线”，则 WAN2 接口的互联方式默认为 “Internet”。
>

## 步骤4：配置 WLAN
在 “WLAN 配置”页面，配置接入网络的方式 ，单击**完成**。
![](https://main.qcloudimg.com/raw/94098c27c90714335c0e1e1ccc674ca0.png)

|字段	|含义|
|----|---|
|Wi-Fi	|选择是否开启 Wi-Fi，若选择开启还需配置 Wi-Fi 名称和密钥。|
|SSID 广播| 选择展示或隐藏 Edge 设备名称。|
|频段	|Edge-100 仅支持 2.4G，Edge-1000 支持 2.4G 和 5G。|
|安全认证|	选择是否加密访问，若选择 AWP-PSK 或 WAP-PSK2 加密方式，还需配置安全密钥。|
|DHCP 地址池	|仅支持 192、172、10 开头的三大私有网段。|
