## 前提条件
本地设备和腾讯云侧 VPC 内私有网段不能相同，避免出现 IP 冲突。

## 配置流程
![](https://qcloudimg.tencent-cloud.cn/raw/cbcd93485d5f66a57c04383889e68cd1.png)
1. [创建 IPSec VPN 网关](https://cloud.tencent.com/document/product/554/52861)。
  创建 IPSec 协议类型的 VPN 网关。
2. [创建对端网关](https://cloud.tencent.com/document/product/554/52865)。
   在 SSL 服务端中指定要连接的腾讯云侧网段和客户端网段。
3. [创建 VPN 通道](https://cloud.tencent.com/document/product/554/52864)。
  用户使用证书和密钥与 VPN 网关建连，用户侧验证服务端证书，服务端验证用户端证书，校验通过后，服务端从客户端 IP 地址池中分配一个 IP 给用户，该 IP 用于和 VPC 内 CVM 通信时使用。
4. 用户本地网关配置。
  在用户侧完成网关配置。
>! 腾讯 IPSec VPN 支持业界主流的用户端网关（防火墙），具体配置请参考[ 本地网关配置](https://cloud.tencent.com/document/product/554/55321) 。
>
5. [配置 VPC 内路由](https://cloud.tencent.com/document/product/554/52860)。
  在 VPC 内配置流量从 IDC 到腾讯云 VPC 内的路由转发策略，目的地址为对端网络的网段，下一跳类型为 VPN 通道/云联网。
  - 如果**下一跳类型**为**VPN 通道**，则选择已创建的 VPN 通道。
  - 如果**下一跳类型**为**云联网**，则系统自动展示该 VPN 网关关联的云联网实例。
6. 测试连通性。 
  腾讯云侧和用户侧完成配置后，使用 Ping 验证 IPSec VPN 连接的连通性。
