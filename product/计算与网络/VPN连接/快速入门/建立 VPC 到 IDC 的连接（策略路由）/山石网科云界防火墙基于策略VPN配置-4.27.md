# 山石网科云界防火墙配置

使用IPsec VPN建立腾讯云VPC到用户IDC的连接时，在配置完腾讯云VPN网关后，您还需要在用户IDC本地站点的网关设备中进行VPN配置。本文以山石防火墙为例介绍如何在本地站点中加载VPN配置。

## 前提条件

请确保您已经在腾讯云VPC内创建VPN，并完成VPN通道配置。

>?此处为VPN1.0版本和VPN2.0版本，如果是VPN3.0版本则认为使用的是SPD策略。

## 数据准备

本文IPsec VPN配置数据举例如下：

<table>
<th colspan="3">配置项</th>
<th>示例值</th>
<tr>
<td rowspan="4">网络配置 </td>
<td rowspan="2">VPC信息 </td>
<td>VPC CIDR</td>
<td>10.1.1.0/24 </td>
</tr>
<tr>
<td>VPN 网关公网IP</td>
<td>159.75.41.242</td>
</tr>
<tr>
<td rowspan="2">IDC信息 </td>
<td>内网CIDR</td>
<td>172.16.0.0/16</td>
</tr>
<tr>
<td>网关公网IP</td>
<td>120.235.225.76</td>
</tr>
<tr>
<td rowspan="16">IPsec连接配置 </td>
<td rowspan="10">IKE配置 </td>
<td>版本</td>
<td>IKEV1 </td>
</tr>
<tr>
<td>身份认证方法</td>
<td>预共享密钥</td>
</tr>
<tr>
<td >PSK </td>
<td>12345</td>
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
<td rowspan="6">IPsec配置</td>
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
<td>IPsec sa Lifetime</td>
<td>3600s</td>
</tr>
</table>



## 操作步骤

1. 登录Hillstone防火墙Web界面，选择【网络】>【VPN】>【IPsec VPN】>【P1提议】，在【P1提议】界面，单击【新建】。
   ![](https://main.qcloudimg.com/raw/43808461f76bad5bb62fc6fa2d0e0805.png)

2. 在弹出的【阶段1提议配置】界面，根据腾讯云VPN连接的IKE协议信息配置IDC的IKE协议，并单击【确定】。
   ![](https://main.qcloudimg.com/raw/d76cfbb601e20dee37e51589487e1de7.png)

3. 选择【P2提议】页签，单击【新建】。
   ![](https://main.qcloudimg.com/raw/daf718603d7d8c929947fd5685cc0af9.png)
4. 在弹出的【阶段2提议配置】界面，根据腾讯云VPN连接的IPsec协议信息配置IDC的IPsec协议，并单击【确定】。
   ![](https://main.qcloudimg.com/raw/b2ef1a3f67a0b65e95095acb6c7d16b9.png)
5. 选择【VPN 对端列表】页签，单击【新建】。
    ![](https://main.qcloudimg.com/raw/7f975818c5806ded17ba7f47caabb3be.png)
6. 在弹出的【VPN 对端配置】界面，配置VPN对端的相关参数，并单击【确定】。
     ![](https://main.qcloudimg.com/raw/cfdafd4be3186d6ce121cf6dbd6fb24f.png)
   + 名称：自定义填写VPN对端名称，例如TO-CLOUDVPN
   + 对端IP地址：填写腾讯云VPN网关的公网IP地址
   + 本端IP：填写IDC本端的公网IP地址
   + 对端IP：填写IDC对端VPN网关的公网IP地址
   + 提议1：选择步骤1创建的P1提议
   + 预共享密钥：填写与腾讯云VPN通道基本配置中一致的预共享密钥，例如本例的123456

7. 选择【IKE VPN列表】页签，单击【新建】。
    ![](https://main.qcloudimg.com/raw/b63869267dba74a334336e5a0d64c4cf.png)
8. 在弹出的【IKE VPN 配置】界面，进行IKE VPN的基本配置和高级配置，完成后单击【确定】。
   + 基本配置
	   ![](https://main.qcloudimg.com/raw/b6f8fde27c90ee3d509095dc7ac2838e.png)
      + 对端选项：选择步骤6创建的VPN对端
      + P2提议：选择步骤3创建的P2提议
      + 代理ID：选择【自动】
   + 高级配置：将【自动连接】勾选设置为【启用】
       ![](https://main.qcloudimg.com/raw/fe6e12ed82e45827dcd757d75df3f0cb.png)

9. 选择【策略】>【策略】，单击【新建】，按照如下参数指导配置策略，完成后单击【确定】。
    ![](https://main.qcloudimg.com/raw/af8d1ce488f022c87c5ae691b0c1edd6.png)
  +  源信息：
	 + 安全域：选择【trust】
	 + 地址：填写【IDC本端网段及掩码】，例如172.16.0.0/16
 + 目的信息：
	+ 安全域：选择【VPNHub】
	+ 地址：填写【腾讯云VPN后端子网网段及掩码】，例如10.1.1.0/24
 + 服务：选择【any】
 + 动作：选择【安全连接】，【隧道】选择步骤6创建的VPN对端，例如TO-CLOUDVPN，勾选【双向VPN策略】