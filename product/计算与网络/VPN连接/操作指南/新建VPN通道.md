VPN 通道是 VPN 连接中用来传输数据包的公网加密通道，腾讯云上的 VPN 通道在实现 IPsec 时，使用 IKE（Internet Key Exchange，因特网密钥交换）协议来建立会话。IKE 具有一套自我保护机制，可以在不安全的网络上安全地认证身份、分发密钥、建立 IPSec 会话。本文介绍如何通过“控制台”创建 VPN 通道。您还可以通过 API、SDK 管理您的 VPN 通道，详情参见 [API 文档](https://cloud.tencent.com/document/product/554/19005)。

VPN 通道的建立包括以下配置信息：
+ [基本信息](#buzhou4)
+ [通道模式](#buzhou6)
+ [IKE 配置（选填）](#buzhou7)
+ [IPsec 配置（选填）](#buzhou8)

## 背景信息
 - 目的路由
本通信通过路由策略指定 VPN 网关所属网络可以和 IDC 中哪些网段通信，创建通道完成后需在 VPN 网关的路由表中配置对应路由策略，详情请参见 [配置 VPN 网关路由](https://cloud.tencent.com/document/product/554/52860) 。
 - SPD 策略。[](id:ipsecvpnspd)
>?
>+ SPD（Security Policy Database）策略由一系列 SPD 规则组成，用于指定 VPC 或云联网内哪些网段可以和 IDC 内哪些网段通信。每条 SPD 规则包括一个本端网段 CIDR，和至少一个对端网段 CIDR。一个本端网段 CIDR 和一个对端网段 CIDR 构成一组匹配关系。一个 SPD 规则下可以有多组**匹配关系**。
>+ 腾讯云 VPN 网关会按照**匹配关系**依次和对端网关设备进行协商，您需要确保您的对端网关设备支持按照匹配关系进行协商，例如在 StrongSwan 配置中使用 also 关键字。
>+ 同一 VPN 网关下所有 SPD 规则形成匹配关系的数量最多为**200**个，否则建议您使用**路由型 VPN 连接**。
>+ 同一 VPN 网关下所有通道内的规则，匹配关系不能重叠，即一组的匹配关系中，本端网段和对端网段不能同时重叠。
>+ 在腾讯云配置的 **SPD 策略建议与对端网关设备配置的 SPD 策略对称**，即在腾讯云配置 SPD 策略中本端网段为`10.11.12.0/24`，对端网段为`192.168.1.0/24`；对端网关设备配置 SPD 策略中本端网段为`192.168.1.0/24`，对端网段为`10.11.12.0/24`。
>- 配置 SPD 策略后，VPN 网关会自动下发路由，无需在 VPN 网关添加路由。
>
**示例：**
如下图所示，某 VPN 网关下已经存在以下 SPD 规则：
![](https://main.qcloudimg.com/raw/6e585587b4bb23e22558a3d84cc50ba6.png)
 - SPD 规则1本端网段`10.0.0.0/24`，对端网段为`192.168.0.0/24`、`192.168.1.0/24`，有两组匹配关系。
 - SPD 规则2本端网段`10.0.1.0/24`，对端网段为`192.168.2.0/24`，有一组匹配关系。
 - SPD 规则3本端网段`10.0.2.0/24`，对端网段为`192.168.2.0/24`，有一组匹配关系。
 他们的匹配关系分别是：
 - `10.0.0.0/24`-----`192.168.0.0/24`
 - `10.0.0.0/24`-----`192.168.1.0/24`
 - `10.0.1.0/24`-----`192.168.2.0/24`
 - `10.0.2.0/24`-----`192.168.2.0/24`
这四组匹配关系相互不能重叠，即他们的本端网段和对端网段不能同时重叠。
 - 如果新增一个`10.0.0.0/24`-----`192.168.1.0/24`匹配关系，则会因为和已有匹配关系重叠，而无法添加 SPD 规则。
 - 如果新增一个`10.0.1.0/24`-----`192.168.1.0/24`匹配关系，和已有的3个匹配关系均不重叠，则可以加入 SPD 规则。

## 前提条件
+ 已[ 创建 VPN 网关 ](https://cloud.tencent.com/document/product/554/71816)和[ 对端网关](https://cloud.tencent.com/document/product/554/52865)。
+ 请确保您已创建的 VPN 通道没有超出配额，调整配额请参考[ 使用限制](https://cloud.tencent.com/document/product/554/18982)。


## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧导航栏中 **VPN 连接** > **VPN 通道**，进入管理页。
3. 在 **VPN 通道**管理页面，单击**新建**。
4. 在**新建VPN 通道**对话框中，配置 VPN 通道基本信息。[](id:buzhou4)
  1. **基本信息配置**
本步骤主要配置通道名称、所属网络、关联 VPN 网关、对完网关、共享密钥、协商类型、通信模式等基本配置。
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
<td>您要创建的 VPN 通道关联的 VPN 网关所在的地域。</td>
</tr>
<tr>
<td>VPN 网关类型</td>
<td>VPN 网关类型有私有网络型 VPN 和云联网型 VPN。关于两种 VPN 网关类型的详细说明请参考<a href="https://cloud.tencent.com/document/product/554/18980#ipsec-vpn"> IPsec VPN</a>。</td>
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
<td>协议类型</td>
<td>默认为 	IKE/IPsec。</td>
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
<td>通信模式</td>
<td>支持目的路由和 SPD 策略两种类型，推荐使用<b>目的路由</b>。
在使用 SPD 策略模式前，您可先了解 <a href="#ipsecvpnspd">SPD 策略原则</a>。</td>
</tr>
</table>
  2. **高级配置**
本步骤主要配置 DPD 检测、健康检查、IKE 和 IPSec 等。
**DPD 检测配置**
<table>
<tr>
<th>参数名称</th>
<th>说明</th>
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
<td><ul><li>断开：清除当前 SA，且当前 VPN 通道断开。</li><li>重试：重新与对端建立连接。</li></ul></td>
</tr>
</table>
<b>健康检测配置</b>
<table>
<tr>
<th>参数名称</th>
<th>说明</th>
</tr>
<tr>
<td>开启健康检查</td>
<td>健康检查用于主备通道的场景，具体请参考 <a href="https://cloud.tencent.com/document/product/554/60005">IDC 与单个腾讯云 VPC 实现主备容灾</a>。如果您不涉及，无需开启此开关（默认不开启），否则请开启本开关，并完成下面的健康检查本端及对端地址的配置，详情请参见  <a href="https://cloud.tencent.com/document/product/554/70209">配置健康检查</a>。
<dx-alert infotype="explain" title="">
一旦您开启健康检查并创建通道完成，系统立即开始通过 NQA 检测 VPN 通道健康状况，如果 VPN 通道未联通或您配置的对端地址不响应 NQA 探测，则系统会在多次探测失败后判定为不健康，并临时中断业务流量，直到 VPN 通道恢复健康。
</dx-alert>
</td>
</tr>
<tr>
<td>健康检查本端地址</td>
<td>仅当开启健康检查功能时，需要设置此参数。您可以使用系统为您分配的 IP 地址或者指定。
<dx-alert infotype="explain" title="">
指定地址不能与 VPC 或 CCN 以及 IDC 通信私网地址或网段冲突，也不能与健康检查对端地址冲突。不能使用多播、广播及本地环回地址。
</dx-alert>
</td>
</tr>
<tr>
<td>健康检查对端地址</td>
<td>仅当开启健康检查功能时，需要设置此参数。您可以使用系统为您分配的 IP 地址或者指定。
<dx-alert infotype="explain" title="">
指定地址不能与 VPC 或 CCN 以及 IDC 通信私网地址或网段冲突，也不能与健康检查本端地址冲突。不能使用多播、广播及本地环回地址。
</dx-alert>
</td>
</tr>
</table>
<b>IKE 配置</b>
<table>
<tr>
<th width="20%">配置项</th>
<th>说明</th>
</tr>
<tr>
<td>版本</td>
<td>IKE V1、IKE V2。</td>
</tr>
<tr>
<td>身份认证方法</td>
<td>默认预共享密钥。</td>
</tr>
<tr>
<td>加密算法</td>
<td>加密算法支持 AES-128、AES-192、AES-256、3DES、DES、SM4，推荐使用 AES-128。</td>
</tr>
<tr>
<td>认证算法</td>
<td>身份认证算法，支持 MD5、SHA1、SHA256、AES-383、SHA512、SM3，推荐使用 MD5。</td>
</tr>
<tr>
<td>协商模式</td>
<td>支持 main（主模式）和 aggressive（野蛮模式）。<br/>二者的不同之处在于，aggressive 模式可以用更少的包发送更多信息，可以快速建立连接，但是是以清晰的方式发送安全网关的身份。使用 aggressive 模式时，配置参数如 Diffie-Hellman 和 PFS 不能进行协商，要求两端拥有兼容的配置。</td>
</tr>
<tr>
<td>本端标识</td>
<td>支持 IP Address 和 FQDN（全称域名），默认 IP Address。</td>
</tr>
<tr>
<td>远端标识</td>
<td>支持 IP Address 和 FQDN ，默认 IP Address。</td>
</tr>
<tr>
<td>DH group</td>
<td>指定 IKE 交换密钥时使用的 DH 组，密钥交换的安全性随着 DH 组的扩大而增加，但交换的时间也增加了。<br/>DH1：采用 768-bit 模指数（Modular Exponential，MODP ）算法的 DH 组。<br/> DH2：采用 1024-bit MODP 算法的 DH 组。<br/> DH5：采用 1536-bit MODP 算法的 DH 组。<br/>DH14：采用 2048-bit MODP 算法，不支持动态 VPN 实现此选项。<br/>DH24：带 256 位的素数阶子群的 2048-bit MODP 算法 DH 组。</td>
</tr>
<tr>
<td>IKE SA Lifetime</td>
<td>单位：s。<br/>设置 IKE 安全提议的 SA 生存周期，在设定的生存周期超时前，会提前协商另一个 SA 来替换旧的 SA。在新的 SA 还没有协商完之前，依然使用旧的 SA；在新的 SA 建立后，将立即使用新的 SA，而旧的 SA 在生存周期超时后，被自动清除。</td>
</tr>
</table>
<b>IPSec 信息配置</b>
<table>
<tr>
<th width="22%">配置项</th>
<th>说明</th>
</tr>
<tr>
<td>加密算法</td>
<td>加密算法支持 AES-128、AES-192、AES-256、3DES、DES、SM4。</td>
</tr>
<tr>
<td>认证算法</td>
<td>身份认证算法，支持 MD5、SHA1、SHA256、SHA384、SHA512、SM3。</td>
</tr>
<tr>
<td>报文封装模式</td>
<td>Tunnel。</td>
</tr>
<tr>
<td>安全协议</td>
<td>ESP。</td>
</tr>
<tr>
<td>PFS</td>
<td>支持 disable、DH-GROUP1、DH-GROUP2、DH-GROUP5、DH-GROUP14 和 DH-GROUP24。</td>
</tr>
<tr>
<td>IPsec SA lifetime(s)</td>
<td>单位：s。</td>
</tr>
<tr>
<td>IPsec SA lifetime(KB)</td>
<td>单位：KB。</td>
</tr>
</table>
5. 如不需要高级配置，可直接单击**创建**。
