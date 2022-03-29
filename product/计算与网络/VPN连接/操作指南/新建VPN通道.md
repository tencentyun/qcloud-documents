VPN 通道是 VPN 连接中用来传输数据包的公网加密通道，腾讯云上的 VPN 通道在实现 IPsec 时，使用 IKE（Internet Key Exchange，因特网密钥交换）协议来建立会话。IKE 具有一套自我保护机制，可以在不安全的网络上安全地认证身份、分发密钥、建立 IPSec 会话。本文介绍如何在[ 私有网络控制台 ](https://console.cloud.tencent.com/vpc/vpnConn?rid=25)创建 VPN 通道。

VPN 通道的建立包括以下配置信息：
+ [基本信息](#buzhou4)
+ [SPD（Security Policy Database）策略](#buzhou6)
+ [IKE 配置（选填）](#buzhou7)
+ [IPsec 配置（选填）](#buzhou8)

## 前提条件
+ 已完成 VPN 网关和对端网关的配置。
+ 本端和对端网段不能重叠。
+ 对端 IDC 必须配置静态的公网 IP。




## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 通道**，进入管理页。
3. 在 **VPN 通道**管理页面，单击**新建**。
4. 在弹出的新建对话框中，配置 VPN 通道基本信息。[](id:buzhou4)
![](https://qcloudimg.tencent-cloud.cn/raw/2a8cf9d6e7436d438ee906ef825a7148.png)
<table>
<tr>
<th>参数名称</th>
<th>说明</th>
</tr>
<tr>
<td>通道名称</td>
<td>自定义通道名称，字符长度为60个。</td>
</tr>
<tr>
<td>地域</td>
<td>此处地域与本端 VPN 网关所在地域一样。</td>
</tr>
<tr>
<td>VPN 网关类型</td>
<td>VPN 网关类型有私有网络型 VPN 和云联网型 VPN。</td>
</tr>
<tr>
<td>私有网络</td>
<td>仅当 <b>VPN 网关类型</b>为<b>私有网络</b>时，需要在此处选择 VPN 网关所属的私有网络。云联网类型无此参数。</td>
</tr>
<tr>
<td>VPN 网关</td>
<td>在列表中选择 VPN 网关。</td>
</tr>
<tr>
<td>对端网关</td>
<td>选择已创建的对端信息，如果没有，可选择新建。</td>
</tr>
<tr>
<td>对端网关 IP</td>
<td>对端网关的公网 IP 地址。</td>
</tr>
<tr>
<td>开启 DPD 检测</td>
<td>DPD 检测开启/关闭开关，用于检测对端是否存活，默认开启。</br>本端主动向对端发送 DPD 请求报文，若在指定超时时间内未收到对端的回应报文，则认为对端离线，进行超时后对应操作。</td>
</tr>
<tr>
<td>DPD 超时时间</td>
<td>DPD 探测总体超时时间。默认30秒，取值范围30秒~60秒。</td>
</tr>
<tr>
<td>DPD 超时操作</td>
<td><ul><li>断开：清除当前 SA，且当前 VPN 通道断开</li><li>重试：重新与对端建立连接</li></ul></td>
</tr>
<tr>
<td>预共享密钥</td>
<td>用于本端和对端网关之间的身份认证，本端和对端须使用相同的预共享密钥。</td>
</tr>
<tr>
<td>协商类型</td>
<td><ul><li>流量协商：创建通道完成之后，当本端有流量进入时，开始与对端协商。</li><li>主动协商：通道创建后主动向对端发起协商。</li><li>被动协商：等待对端发起协商。</li></ul></td>
</tr>
<tr>
<td>开启健康检查</td>
<td>健康检查的开启/关闭开关，用于检测链路健康状态，默认不开启。
<dx-alert infotype="explain" title="">
健康检查参数配置完成后，您还需要在 [步骤6](#buzhou6) 中配置健康检查的 SPD 策略，这样健康检查功能才会生效。健康检查操作指导可参考 [配置健康检查](https://cloud.tencent.com/document/product/554/70209)。
</dx-alert>
</td>
</tr>
<tr>
<td>健康检查本端地址</td>
<td>仅当开启健康检查功能时，需要设置此参数，需填写 VPC 外的可用 IP 地址。</td>
</tr>
<tr>
<td>健康检查对端地址</td>
<td>仅当开启健康检查功能时，需要设置此参数，需填写 IDC 内可用 IP 地址，不可为169.254.0.0/16，224.0.0.0-239.255.255.255，以及0.0.0.0地址。</td>
</tr>
<tr>
<td>标签</td>
<td>用于标识网络资源，便于资源管理，非必选参数，请根据实际情况进行设置。</td>
</tr>
</table>
5. 单击**下一步**，进入**通信模式**配置界面。[](id:buzhou6)[](id:cfg_vpn_spd)
 - 目的路由模式
  本通信通过路由策略指定 VPN 网关所属网络可以和 IDC 中哪些网段通信，创建通道完成后需在 VPN 网关的路由表中配置对应路由策略，详情请参见[配置 VPN 网关路由](https://cloud.tencent.com/document/product/554/52860) 。
 - 配置 SPD 策略。
>?
>+ SPD（Security Policy Database）策略由一系列 SPD 规则组成，用于指定 VPC 或云联网内哪些网段可以和 IDC 内哪些网段通信。每条 SPD 规则包括一个本端网段 CIDR，和至少一个对端网段 CIDR。一个本端网段 CIDR 和一个对端网段 CIDR 构成一组匹配关系。一个 SPD 规则下可以有多组匹配关系。
>+ 同一 VPN 网关下所有通道内的规则，匹配关系不能重叠，即一组的匹配关系中，本端网段和对端网段不能同时重叠。
>
**示例：**
如下图所示，某 VPN 网关下已经存在以下 SPD 规则：
![](https://main.qcloudimg.com/raw/6e585587b4bb23e22558a3d84cc50ba6.png)
 - SPD 规则1本端网段 10.0.0.0/24，对端网段为 192.168.0.0/24、192.168.1.0/24，有两组匹配关系。
 - SPD 规则2本端网段 10.0.1.0/24，对端网段为 192.168.2.0/24，有一组匹配关系。
 - SPD 规则3本端网段 10.0.2.0/24，对端网段为 192.168.2.0/24，有一组匹配关系。
 他们的匹配关系分别是：
 - 10.0.0.0/24-----192.168.0.0/24
 - 10.0.0.0/24-----192.168.1.0/24
 - 10.0.1.0/24-----192.168.2.0/24
 - 10.0.2.0/24-----192.168.2.0/24
这四组匹配关系相互不能重叠，即他们的本端网段和对端网段不能同时重叠。
 - 如果新增一个10.0.0.0/24-----192.168.1.0/24匹配关系，则会因为和已有匹配关系重叠，而无法添加 SPD 规则。
 - 如果新增一个10.0.1.0/24-----192.168.1.0/24匹配关系，和已有的3个匹配关系均不重叠，则可以加入 SPD 规则。
![](https://main.qcloudimg.com/raw/641121e50364a1a40b4b3643a20703c1.png)
6. [](id:buzhou7)单击**下一步**，进入**IKE 配置（选填）**界面，如不需要高级配置，可直接单击**下一步**。
 ![](https://main.qcloudimg.com/raw/cb7acde379a0aafb5d4b28dfe759c683.png)
<table>
<tr>
<th width="20%">配置项</th>
<th>说明</th>
</tr>
<tr>
<td>版本</td>
<td>IKE V1、IKE V2</td>
</tr>
<tr>
<td>身份认证方法</td>
<td>默认预共享密钥</td>
</tr>
<tr>
<td>加密算法</td>
<td>加密算法支持 AES-128、AES-192、AES-256、3DES、DES、SM4</td>
</tr>
<tr>
<td>认证算法</td>
<td>身份认证算法，支持 MD5、SHA1、SHA256、AES-383、SHA512、SM3</td>
</tr>
<tr>
<td>协商模式</td>
<td>支持 main（主模式）和 aggressive（野蛮模式）<br/>二者的不同之处在于，aggressive 模式可以用更少的包发送更多信息，可以快速建立连接，但是是以清晰的方式发送安全网关的身份。使用 aggressive 模式时，配置参数如 Diffie-Hellman 和 PFS 不能进行协商，要求两端拥有兼容的配置</td>
</tr>
<tr>
<td>本端标识</td>
<td>支持 IP Address 和 FQDN（全称域名），默认 IP Address</td>
</tr>
<tr>
<td>对端标识</td>
<td>支持 IP Address 和 FQDN ，默认 IP Address</td>
</tr>
<tr>
<td>DH group</td>
<td>指定 IKE 交换密钥时使用的 DH 组，密钥交换的安全性随着 DH 组的扩大而增加，但交换的时间也增加了<br/>DH1：采用 768-bit 模指数（Modular Exponential，MODP ）算法的 DH 组<br/> DH2：采用 1024-bit MODP 算法的 DH 组<br/> DH5：采用 1536-bit MODP 算法的 DH 组<br/>DH14：采用 2048-bit MODP 算法，不支持动态 VPN 实现此选项<br/>DH24：带 256 位的素数阶子群的 2048-bit MODP 算法 DH 组</td>
</tr>
<tr>
<td>IKE SA Lifetime</td>
<td>单位：秒<br/>设置 IKE 安全提议的 SA 生存周期，在设定的生存周期超时前，会提前协商另一个 SA 来替换旧的 SA。在新的 SA 还没有协商完之前，依然使用旧的 SA；在新的 SA 建立后，将立即使用新的 SA，而旧的 SA 在生存周期超时后，被自动清除</td>
</tr>
</table>
7. [](id:buzhou8) 进入**IPsec配置（选填）**界面，如果不需要高级配置，可直接单击**完成**。
<table>
<tr>
<th width="22%">配置项</th>
<th>说明</th>
</tr>
<tr>
<td>加密算法</td>
<td>加密算法支持 AES-128、AES-192、AES-256、3DES、DES、SM4</td>
</tr>
<tr>
<td>认证算法</td>
<td>身份认证算法，支持 MD5、SHA1、SHA256、SHA384、SHA512、SM3</td>
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
<td>支持 disable、DH-GROUP1、DH-GROUP2、DH-GROUP5、DH-GROUP14 和 DH-GROUP24</td>
</tr>
<tr>
<td>IPsec SA lifetime(s)</td>
<td>单位：s</td>
</tr>
<tr>
<td>IPsec SA lifetime(KB)</td>
<td>单位：KB</td>
</tr>
</table>
8. 创建成功后，返回 VPN 通道列表页，单击**更多**，选择**下载配置文件**并完成下载。
9. 其他操作：
     1. 单击**重置**会清空已有通道配置，重置操作会中断现有 VPN 通道数据传输并重新建立连接，请提前做好网络变更准备。
     2. 单击**更多** > **日志**，可查看通道日志。
     3. 单击**更多** > **删除**，可删除通道，未联通的通道可执行删除操作。
     4. 单击**更多** > **下载配置文件**，可下载通道配置文件，该文件用于加载到对端的 VPN 设备上。
     5. 单击**更多** > **编辑标签**，可对标签进行修改。
![](https://qcloudimg.tencent-cloud.cn/raw/93a87a2204f0a7270cf8e71f72275d97.png)
	 
