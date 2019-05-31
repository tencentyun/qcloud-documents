您好，VPN 网关和对端网关建立后，即可建立 VPN 通道，用于私有网络和外部 IDC 之间的加密通信。当前 VPN 通道支持 IPsec 加密协议，可满足绝大多数 VPN 连接的需求。

VPN 通道在运营商公网中运行，公网的网络阻塞、抖动会对 VPN 网络质量有影响，因此也无法提供 SLA 服务协议保 障。如果业务对延时、抖动敏感，建议通过专线接入私有网络，更多内容可以查看专线接入服务。

腾讯云上的 VPN 通道在实现 IPsec 中使用 IKE（Internet Key Exchange，因特网密钥交换）协议来建立会话。IKE 具有一套自我保护机制，可以在不安全的网络上安全地认证身份、分发密钥、建立 IPSec 会话。

VPN 通道的建立包括以下配置信息：
- 基本信息
- SPD（Security Policy Database）策略
- IKE配置（选填）
- IPsec配置（选填）

VPN 通道的详细信息请参考：[VPN 通道](https://cloud.tencent.com/document/product/215/4956#vpn.E9.80.9A.E9.81.93) 
