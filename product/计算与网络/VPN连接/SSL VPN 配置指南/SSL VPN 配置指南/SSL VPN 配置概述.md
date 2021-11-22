>?SSL VPN 内测中，如需体验，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)。
>

## 前提条件
- 本地设备和腾讯云侧 VPC 内私有网段不能相同，避免出现 IP 冲突。 
- 客户端已连接公网。

## 配置流程
![](https://qcloudimg.tencent-cloud.cn/raw/aa83c71919f5f685999a1a5690ab90c2.png)
1. [创建 SSL VPN 网关](https://cloud.tencent.com/document/product/554/63716)。
创建 SSL 协议类型的 VPN 网关。
2. [创建 SSL 服务端](https://cloud.tencent.com/document/product/554/63717)。
在 SSL 服务端中指定要连接的腾讯云侧网段和客户端网段。
3. [创建 SSL 客户端](https://cloud.tencent.com/document/product/554/63718)。
用户使用证书和密钥与 VPN 网关建连，用户侧验证服务端证书，服务端验证用户端证书，校验通过后，服务端从客户端 IP 地址池中分配一个 IP 给用户，该 IP 用于和 VPC 内 CVM 通信时使用。
4. [配置 VPC 内路由](https://cloud.tencent.com/document/product/554/52860)。
在 VPC 内配置流量从用户移动端到腾讯云 VPC 内的路由转发策略，目的地址为客户端网段，下一跳类型为 VPN 网关，下一跳为 SSL VPN 网关。
5. 配置用户移动端。
在用户移动端完成 SSL 证书配置。
6. 测试连通性。 
 腾讯云侧和用户移动端配置完成后，使用 Ping 验证 SSL VPN 连接的连通性。
