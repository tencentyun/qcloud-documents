# 山石网科云界防火墙配置

使用IPsec VPN建立腾讯云VPC到用户IDC的连接时，在配置完腾讯云VPN网关后，您还需要在用户IDC本地站点的网关设备中进行VPN配置。本文以山石防火墙为例介绍如何在本地站点中加载VPN配置。

## 前提条件

请确保您已经在腾讯云VPC内创建VPN，并完成VPN通道配置。

>?此处为VPN3.0版本，即VPN具备路由功能，子网流量基于配置的路由策略传递至VPN通道。

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
<td>123456</td>
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
	    ![](https://main.qcloudimg.com/raw/3e0ca49f5862a537e49a5b98147d9c4c.png)
      + 对端选项：选择步骤6创建的VPN对端
      + P2提议：选择步骤3创建的P2提议
      + 代理ID：选择【手工】，并在【代理ID列表】的【本地IP/掩码】中输入本地IDC的内网网段，在【远程IP/掩码】中输入腾讯云VPC的内网网段，然后单击【添加】
   + 高级配置：将【自动连接】勾选设置为【启用】
       ![](https://main.qcloudimg.com/raw/fe6e12ed82e45827dcd757d75df3f0cb.png)

9. 选择【网络】>【安全域】，单击【新建】， 在弹出的【安全域配置】界面，输入安全与名称，并在【类型】中选择【三层安全域】，并单击【确定】。
   ![](https://main.qcloudimg.com/raw/69334e18d2af79c908d80d9e0aa0e256.png)
10. 选择【网络】>【接口】，依次单击【新建】>【隧道接口】 。
    ![](https://main.qcloudimg.com/raw/f12069e0a277ca48b8fdfdc3e5033beb.png)
11. 在弹出的【隧道接口】对话框中，配置隧道接口相关参数。
       ![](https://main.qcloudimg.com/raw/e9631e816b2aa9abe5dc207decb6fc7f.png)
       ![](https://main.qcloudimg.com/raw/f81f93f7a7f72fad805ebb2d79ae54ce.png)
   + 接口名称：输入【tunnelX】，X的取值范围为1-64，例如tunnel1
   + 安全域：选择步骤9创建的安全域
   + 隧道类型：选择【IPsec VPN】
   + VPN名称：选择步骤6创建的对端VPN名称 

12. 选择【策略】>【安全策略】，单击【新建】配置安全策略。
    ![](https://main.qcloudimg.com/raw/ade66ecbc1951e66b921ce16615299f1.png)
	![](https://main.qcloudimg.com/raw/9b1ec2a54ef7a80da950f446f31a0d3d.png)

13. 选择【网络】>【路由】，单击【新建】分别配置上行和下行路由，完成后单击【确定】。

  + 上行路由：目的地址为腾讯云VPC的网段，下一跳为步骤11新建的隧道接口，本例为tunnel1。
      ![](https://main.qcloudimg.com/raw/65ed16c3573f97395782ececd6b0c129.png)
    + 下行路由：配置防火墙下行接口路由。