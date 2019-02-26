- VPN 网关和对端网关建立后，即可建立用于 VPC 和外部 IDC 之间加密通信的 VPN 通道。当前 VPN 通道支持 IPsec 加密协议，可满足绝大多数 VPN 连接的需求。
- VPN 通道在运营商公网中运行，公网的网络阻塞、抖动会影响 VPN 网络质量，因此无法提供 SLA 服务协议保障。若业务对延时、抖动敏感，建议您通过专线接入 VPC，更多详情，请参见 [专线接入服务](https://cloud.tencent.com/product/dc.html)。
- 腾讯云上的 VPN 通道在实现 IPsec 时，使用 IKE（Internet Key Exchange，因特网密钥交换）协议来建立会话。IKE 具有一套自我保护机制，可以在不安全的网络上安全地认证身份、分发密钥、建立 IPSec 会话。
- VPN 通道的建立包括以下配置信息：
 - 基本信息
 - SPD（Security Policy Database）策略
 - IKE 配置（选填）
 - IPsec 配置（选填）
 
下面将为您详细介绍基本信息、SPD 策略、IKE 配置（选填）和 IPsec 配置（选填）。
## 基本信息
- 协议类型：IKE / IPsec
- 预共享密钥：预共享密钥是用于验证 L2TP / IPSec 连接的 Unicode 字符串，本端和对端必须使用相同的预共享密钥。

## SPD（Security Policy Database）策略
- SPD（Security Policy Database）策略由一系列 SPD 规则组成，用于指定 VPC 内哪些网段可以和 IDC 内哪些网段通信。每条 SPD 规则包括一个本端网段 CIDR，和至少一个对端网段 CIDR。
使用 SPD 规则时请注意以下限制：
 - 同一 VPN 网关下所有通道内的规则，相互不能重叠。
 - 同一 VPN 网关下所有通道规则的本端网段，相互不能重叠。
 - 同一条规则的多个对端网段，相互不能重叠。
 - 每条规则的本端网段必须在 [私有网络](https://cloud.tencent.com/document/product/215/4927) 的网段内。
 - 每条规则的对端网段不能在 [私有网络](https://cloud.tencent.com/document/product/215/4927) 的网段内。
- 下面是一个正确的实例：
 - SPD策略 1 本端网段 `10.0.0.0/24`，对端网段为 `192.168.0.0/24`、`192.168.1.0/24`。
 - SPD策略 2 本端网段 `10.0.1.0/24`，对端网段为 `192.168.2.0/24`。
 - SPD策略 3 本端网段 `10.0.2.0/24`，对端网段为 `192.168.2.0/24`。
![](//mccdn.qcloud.com/static/img/5b32174d312e31c5b5a9162a50456de8/image.png)

## IKE 配置
<style> table th:first-of-type { width: 150px; } </style>

| 配置项             | 说明                                       |
| --------------- | ---------------------------------------- |
| 版本              | IKE V1                                   |
| 身份认证方法          | 默认预共享密钥                                  |
| 认证算法            | 身份认证算法，支持 MD5 和 SHA1                        |
| 协商模式            | 支持 main（主模式）和 aggressive（野蛮模式）<br/>二者的不同之处在于，aggressive 模式可以用更少的包发送更多信息，可以快速建立连接，但是是以清晰的方式发送安全网关的身份。使用 aggressive 模式时，配置参数如 Diffie-Hellman 和 PFS 不能进行协商，要求两端拥有兼容的配置 |
| 本端标识            | 支持 IP address 和 FQDN（全称域名）               |
| 对端标识            | 支持 IP address 和 FQDN                     |
| DH group        | 指定 IKE 交换密钥时使用的 DH 组，密钥交换的安全性随着 DH 组的扩大而增加，但交换的时间也增加了<br/>Group1：采用 768-bit 模指数（Modular Exponential，MODP ）算法的 DH 组<br/> Group2：采用 1024-bit MODP 算法的 DH 组<br/> Group5：采用 1536-bit MODP 算法的 DH 组<br/>Group14：采用 2048-bit MODP 算法，不支持动态 VPN 实现此选项<br/>Group24：带 256 位的素数阶子群的 2048-bit MODP算法 DH 组，不支持组 VPN 实现此选项 |
| IKE SA Lifetime | 单位：秒<br/>设置 IKE 安全提议的 SA 生存周期，在设定的生存周期超时前，会提前协商另一个 SA 来替换旧的 SA。在新的 SA 还没有协商完之前，依然使用旧的 SA；在新的 SA 建立后，将立即使用新的 SA，而旧的 SA 在生存周期超时后，被自动清除 |

##  IPsec 信息
<style> table th:first-of-type { width: 150px; } </style>

| 配置项                   | 说明                                       |
| --------------------- | ---------------------------------------- |
| 加密算法                  | 支持 3DES、AES-128、AES-192、AES-256、DES      |
| 认证算法                  | 支持 MD5 和 SHA1                            |
| 报文封装模式                | Tunnel                                   |
| 安全协议                  | ESP                                      |
| PFS                   | 支持 disable、dh-group1、dh-group2、dh-group5、dh-group14和dh-group24 |
| IPsec SA lifetime(s)  | 单位：秒                                     |
| IPsec SA lifetime(KB) | 单位：KB                                    |
