<style rel="stylesheet">
table th:nth-of-type(1){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(2){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(3){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(4){
width:200px;
}</style>
<style rel="stylesheet">
table tr:hover {
background: #efefef; 
</style>
## 简介
VPN 连接是一种通过公网加密通道连接您的对端 IDC 和私有网络的方式。如下图所示，腾讯云私有网络 VPN 连接分为以下几个组成部分：
- VPN 网关：创建的私有网络 IPsec VPN 网关
- 对端网关： IDC 端的 IPsec VPN 服务网关
- VPN 通道：加密的 IPsec VPN 通道
<div style="text-align:center">
![](//mccdn.qcloud.com/static/img/a654d376b4e4e13ae2bb65b13239cef2/image.png)

</div>
私有网络内可以建立 VPN 网关，每个 VPN 网关可以建立多个 VPN 通道，每个 VPN 通道可以打通一个本地 IDC。
>**注意:**
>在建立 VPN 连接之后，您需要在路由表中配置相关路由策略，才能真正实现通信。
 
## VPN 网关
VPN 网关是私有网络建立 VPN 连接的出口网关，与对端网关（IDC 侧的 IPsec VPN 服务网关）配合使用，主要用于腾讯云私有网络和外部 IDC 之间建立安全可靠的加密网络通信。腾讯云 VPN 网关通过软件虚拟化实现，采用双机热备策略，单台故障时自动切换，不影响业务正常运行。

VPN 网关根据带宽上限分为 5 种设置，分别为：5M、10M、20M、50M、100M。您可以随时调整 VPN 网关带宽设置，即时生效。

## 对端网关
对端网关是指 IDC 机房的 IPsec VPN 服务网关，对端网关需与腾讯云 VPN 网关配合使用，一个 VPN网关可与多个对端网关建立带有加密的 VPN 网络通道。

## VPN 通道
VPN 网关和对端网关建立后，即可建立 VPN 通道，用于私有网络和外部 IDC 之间的加密通信。当前 VPN 通道支持 IPsec 加密协议，可满足绝大多数 VPN 连接的需求。

VPN 通道在运营商公网中运行，公网的网络阻塞、抖动会对 VPN 网络质量有影响，因此也无法提供 SLA 服务协议保障。如果业务对延时、抖动敏感，建议通过专线接入私有网络，更多内容可以查看 <a href="https://cloud.tencent.com/product/dc.html" target="_blank">专线接入服务</a>。

腾讯云上的 VPN 通道在实现 IPsec 中使用 IKE（Internet Key Exchange，因特网密钥交换）协议来建立会话。IKE 具有一套自保护机制，可以在不安全的网络上安全地认证身份、分发密钥、建立 IPSec 会话。

VPN 通道的建立包括以下配置信息：
- 基本信息
- SPD（Security Policy Database）策略
- IKE 配置（选填）
- IPsec 配置（选填）

下面详细介绍基本信息、SPD 策略、IKE 配置（选填）和 IPsec 配置（选填）。

### 基本信息
协议类型：IKE/IPsec
预共享秘钥：预共享密钥是用于验证 L2TP/IPSec 连接的 Unicode 字符串，本端和对端必须使用相同的预共享密钥。

### SPD（Security Policy Database）策略
SPD（Security Policy Database）策略由一系列 SPD 规则组成，每条规则用于指定 VPC 内哪些网段可以和 IDC 中哪些网段通信。
- 每条 SPD 策略对应一个本端网段和多个对端网段，本段网段和对端网段不能重叠。
- 所有策略的集合中本端网段之间不可重叠
- 每个本端网段的多条对端网段不可重叠
- 对端网段不可与私有网络网段重叠

下面是一个正确的实例：

SPD 策略 1 本端网段 ```10.0.0.0/24```，对端网段为 ```192.168.0.0/24```、```192.168.1.0/24```。
SPD 策略 2 本端网段 ```10.0.1.0/24```，对端网段为 ```192.168.2.0/24```。
SPD 策略 3 本端网段 ```10.0.2.0/24```，对端网段为 ```192.168.2.0/24```。
<div style="text-align:center">
![](//mccdn.qcloud.com/static/img/5b32174d312e31c5b5a9162a50456de8/image.png)
 
 </div>
### IKE 配置

|配置项|说明|
|:--:|--|
|版本|IKE V1|
|身份认证方法|默认预共享秘钥|
|认证算法|身份认证算法，支持MD5 和 SHA1|
|协商模式|支持 main（主模式）和aggressive（挑战者模式）<br><br>二者的不同之处在于，aggressive 模式可以用更少的包发送更多信息，这样做的优点是快速建立连接，而代价是以清晰的方式发送安全网关的身份，使用 aggressive 模式时，配置参数如 Diffie-Hellman 和 PFS 不能进行协商，因此两端拥有兼容的配置是至关重要的|
|本端标识|支持 IP address 和 FQDN（全称域名）|
|对端标识|支持 IP address 和 FQDN|
|DH group|指定 IKE 交换密钥时使用的 DH 组，密钥交换的安全性随着 DH 组的扩大而增加，但交换的时间也增加了<br><br>Group1：采用 768-bit 模指数（Modular Exponential，MODP ）算法的 DH 组<br><br> Group2：采用 1024-bit MODP 算法的 DH 组<br><br> Group5：采用 1536-bit MODP 算法的 DH 组<br><br>Group14：采用 2048-bit MODP 算法，不支持动态 VPN 实现此选项<br><br> Group24：带 256 位的素数阶子群的 2048-bit MODP算法 DH 组，不支持组 VPN 实现此选项|
|IKE SA Lifetime|单位：秒<br><br>设置 IKE 安全提议的 SA 生存周期，在设定的生存周期超时前，会提前协商另一个 SA 来替换旧的 SA。在新的 SA 还没有协商完之前，依然使用旧的 SA；在新的 SA 建立后，将立即使用新的 SA，而旧的 SA 在生存周期超时后，被自动清除|

###  Ipsec 信息
|配置项|说明|
|:--:|--|
|加密算法|支持 3DES、AES-128、AES-192、AES-256、DES|
|认证算法|支持 MD5 和 SHA1|
|报文封装模式|Tunnel|
|安全协议|ESP|
|PFS|支持 disable、dh-group1、dh-group2、dh-group5、dh-group14和dh-group24|
|IPsec SA lifetime(s)|单位：秒|
|IPsec SA lifetime(KB)|单位：KB|

## 使用约束
### VPN 连接约束
关于 VPN 连接，您需要注意的是:
- VPN 参数配置完成后，**您需要在子网关联路由表中添加指向 VPN 网关的路由策略**，子网内云主机访问对端网段的网络请求才会通过 VPN 通道传递至对端网关。
- 在配置完路由表之后，**您需要在 VPC 内云主机 ping 对端网段中的 IP 以激活此 VPN 通道。**
- VPN 连接稳定性依赖运营商公网质量，暂时无法提供 SLA 服务协议保障。

| 资源 | 限制（个） | 
|---------|:---------:|
| 每个私有网络内 VPN 网关个数 | 10 | 
| 同一地域内对端网关个数| 20 | 
| 同一个对端网关支持的 VPN 通道数 | 1 | 
| 同一地域内 VPN 通道数 | 20 | 
| 每个 VPN 通道的 SPD 个数 | 10 | 
| 每个 SPD 支持的对端网段数 | 50 | 

### 对端网关 IP 地址约束
对端网关不支持以下 IP 地址：
- 全 0，全 255，224 开头的组播地址;
- 回环地址: ```127.x.x.x/8```;
- IP 地址中主机位为全 0 或者全 1 的地址，如:
a.以 A 类中 1~126 开头举例，1~126.0.0.0 以及1~126.255.255.255;
b.以 B 类中 128~191 开头举例，128~191.x.0.0 以及128~191.x.255.255;
c. 以 C 类中 192~223 开头举例，192~223.x.x.0 以及192~223.x.x.255;
- 内部服务地址：```169.254.x.x/16```;
