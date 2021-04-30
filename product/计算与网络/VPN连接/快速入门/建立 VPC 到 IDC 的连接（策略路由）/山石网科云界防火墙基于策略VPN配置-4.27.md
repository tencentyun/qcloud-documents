使用 IPsec VPN 建立腾讯云 VPC 到用户 IDC 的连接时，在配置完腾讯云 VPN 网关后，您还需要在用户 IDC 本地站点的网关设备中进行 VPN 配置。本文以山石防火墙为例介绍如何在本地站点中进行 VPN 配置。
>?本文仅支持 IKEv1 协议的配置。

## 前提条件
请确保您已经在腾讯云 VPC 内创建 VPN，并完成 VPN 通道配置。

## 数据准备
本文 IPsec VPN 配置数据举例如下：
<table>
<th colspan="3">配置项</th>
<th>示例值</th>
<tr>
<td rowspan="4">网络配置 </td>
<td rowspan="2">VPC 信息 </td>
<td>子网 CIDR</td>
<td>10.1.1.0/24 </td>
</tr>
<tr>
<td>VPN 网关公网 IP</td>
<td>159.75.41.242</td>
</tr>
<tr>
<td rowspan="2">IDC 信息 </td>
<td>内网 CIDR</td>
<td>172.16.0.0/16</td>
</tr>
<tr>
<td>网关公网 IP</td>
<td>120.235.225.76</td>
</tr>
<tr>
<td rowspan="16">IPsec 连接配置 </td>
<td rowspan="9">IKE 配置 </td>
<td>版本</td>
<td>IKEV1 </td>
</tr>
<tr>
<td>身份认证方法</td>
<td>预共享密钥，例如123456</td>
</tr>
<tr>
<td>加密算法</td>
<td>DES</td>
</tr>
<tr>
<td>认证算法</td>
<td>MD5</td>
</tr>
<tr>
<td>协商模式</td>
<td>main</td>
</tr>
<tr>
<td>本端标识</td>
<td>IP Address：120.235.225.76</td>
</tr>
<tr>
<td>远端标识</td>
<td>IP Address：159.75.41.242</td>
</tr>
<tr>
<td>DH group</td>
<td>DH2</td>
</tr>
<tr>
<td>IKE SA Lifetime</td>
<td>86400</td>
</tr>
<tr>
<td rowspan="7">IPsec 配置</td>
<td>加密算法</td>
<td>AES-128</td>
</tr>
<tr>
<td>认证算法</td>
<td>MD5</td>
</tr>
<tr>
<td>报文封装模式</td>
<td>Tunnel</td>
</tr>
<tr>
<td>安全协议</td>
<td>ESP</td>
</tr>
<tr>
<td>PFS</td>
<td>disable</td>
</tr>
<tr>
<td>IPsec SA 生存周期（s）</td>
<td>3600s</td>
</tr>
<tr>
<td>IPsec SA 生存周期（KB）</td>
<td>1843200KB</td>
</tr>
</table>

## 操作步骤
1. 登录 Hillstone 防火墙 Web 界面，选择【网络】>【VPN】>【IPsec VPN】>【P1提议】，在【P1提议】界面，单击【新建】。
   ![](https://main.qcloudimg.com/raw/43808461f76bad5bb62fc6fa2d0e0805.png)
2. [](id:step2)在弹出的【阶段1提议配置】界面，根据腾讯云 VPN 连接的 IKE 协议信息配置 IDC 的 IKE 协议，并单击【确定】。
   ![](https://main.qcloudimg.com/raw/d76cfbb601e20dee37e51589487e1de7.png)
3. 选择【P2提议】页签，单击【新建】。
   ![](https://main.qcloudimg.com/raw/daf718603d7d8c929947fd5685cc0af9.png)
4. [](id:step4)在弹出的【阶段2提议配置】界面，根据腾讯云 VPN 连接的 IPsec 协议信息配置 IDC 的 IPsec 协议，并单击【确定】。
   ![](https://main.qcloudimg.com/raw/b2ef1a3f67a0b65e95095acb6c7d16b9.png)
5. 选择【VPN 对端列表】页签，单击【新建】。
    ![](https://main.qcloudimg.com/raw/7f975818c5806ded17ba7f47caabb3be.png)
6. [](id:step6)在弹出的【VPN 对端配置】界面，配置 VPN 对端的相关参数，并单击【确定】。
     ![](https://main.qcloudimg.com/raw/cfdafd4be3186d6ce121cf6dbd6fb24f.png)
   + 名称：自定义填写 VPN 对端名称，例如 TO-CLOUDVPN
   + 对端 IP 地址：填写腾讯云 VPN 网关的公网 IP 地址
   + 本端 IP：填写 IDC 本端的公网 IP 地址
   + 对端 IP：填写 IDC 对端 VPN 网关的公网 IP 地址
   + 提议1：选择[ 步骤2 ](#step2)创建的P1提议
   + 预共享密钥：填写与腾讯云 VPN 通道基本配置中一致的预共享密钥，例如本例的123456
7. 选择【IKE VPN列表】页签，单击【新建】。
    ![](https://main.qcloudimg.com/raw/b63869267dba74a334336e5a0d64c4cf.png)
8. 在弹出的【IKE VPN 配置】界面，进行 IKE VPN 的基本配置和高级配置，完成后单击【确定】。
   + 基本配置
	   ![](https://main.qcloudimg.com/raw/b6f8fde27c90ee3d509095dc7ac2838e.png)
      + 对端选项：选择[ 步骤6 ](#step6)创建的 VPN 对端
      + P2提议：选择[ 步骤4 ](#step4)创建的P2提议
      + 代理 ID：选择【自动】
   + 高级配置：将【自动连接】勾选设置为【启用】
       ![](https://main.qcloudimg.com/raw/fe6e12ed82e45827dcd757d75df3f0cb.png)
9. 选择【网络】>【安全域】，单击【新建】 配置安全域。
     ![](https://main.qcloudimg.com/raw/4858ab1e86ec84b22b42e641294db926.png)
10. 在弹出的【安全域配置】界面，配置如下参数，完成后，单击【确定】。
    + 安全域名称：自定义名称，设备默认预设多个安全域，其中包含【VPNhub】
    + 虚拟路由器：默认选择【trust-vr】
	![](https://main.qcloudimg.com/raw/bb0999aaf4a33e4186fadec2d4bdd8c5.png)
11. 选择【策略】>【策略】，单击【新建】，按照如下参数指导配置策略，完成后单击【确定】。
    ![](https://main.qcloudimg.com/raw/af8d1ce488f022c87c5ae691b0c1edd6.png)
  +  源信息：
	 + 安全域：选择【trust】
	 + 地址：填写【IDC 本端网段及掩码】，例如172.16.0.0/16
 + 目的信息：
	 + 安全域：选择【VPNHub】
	 + 地址：填写【腾讯云 VPN 后端子网网段及掩码】，例如10.1.1.0/24
 + 服务：选择【any】
 + 动作：选择【安全连接】，【隧道】选择[ 步骤6 ](#step6)创建的 VPN 对端，例如 TO-CLOUDVPN，勾选【双向 VPN 策略】
