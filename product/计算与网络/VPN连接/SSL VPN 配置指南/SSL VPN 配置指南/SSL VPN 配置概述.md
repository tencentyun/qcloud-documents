## 前提条件
- 本地设备和腾讯云侧 VPC 内私有网段不能相同，避免出现 IP 冲突。 
- 客户端已连接公网。

## 配置流程
![](https://qcloudimg.tencent-cloud.cn/raw/fac8844eac5f6e1f5e17df513d753229.png)
1. [创建 SSL VPN 网关](https://cloud.tencent.com/document/product/554/63716)。
    创建 SSL 协议类型的 VPN 网关，启用 SSL-VPN功能。
2. [创建 SSL 服务端](https://cloud.tencent.com/document/product/554/63717)。
   在 SSL 服务端中指定要连接的腾讯云侧网段和客户端网段。
3. [创建客户端证书](https://iwiki.woa.com/pages/viewpage.action?pageId=1059338353)。
  用户使用证书和密钥与VPN网关建连，用户侧验证服务端证书，服务端验证用户端证书，校验通过后，服务端从客户端IP地址池中分配一个IP给用户，该IP用于和VPC内VM通信时使用。
4. [配置 VPC 内路由(缺少链接)]()。
  在 VPC 内配置流量从 IDC 到腾讯云 VPC 内的路由转发策略，目的地址为客户端网段，下一跳为 SSL VPN 网关。
5. 配置 IDC 客户端。
  在腾讯云侧 VPN 客户端管理页面下载客户端证书，并完成配置。
  目前客户端操作系统支持Windows、MAC、Linux (主流版本）。
6. 激活 SSL VPN。 
  腾讯云侧和用户 IDC 侧配置完成后，使用 Ping 验证 SSL VPN 连接的连通性。
