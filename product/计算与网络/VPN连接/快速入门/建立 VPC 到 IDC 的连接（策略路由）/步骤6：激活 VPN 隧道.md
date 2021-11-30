腾讯云侧 VPN 网关、VPN 通道、对端网关和用户本地配置完成后，您可以使用 Ping 命令激活通道，即验证腾讯云侧是否和用户侧互通。

在腾讯云侧 VPC 内的云服务器中 Ping 对端网关 IP。
例如：在 TomVPC 内的子网 A 中的云服务器 ping 10.0.1.1。
 - Ping 成功，表示腾讯云侧与用户 VPN 隧道已通达。
 - Ping 失败，请检测客户侧本地配置。如需技术支持请[ 提交工单](https://console.cloud.tencent.com/workorder/category)。
