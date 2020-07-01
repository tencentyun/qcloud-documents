## 1. 如何确保在 VPC 中运行的云主机的安全？
VPC本身是一个逻辑隔离的网络环境，另外安全组和网络ACL可以用来进行流量控制：
- **安全组**可用于指定允许进出各个 云主机的进站和出站网络流量。没有显式允许进出实例的流量将自动被拒绝。
- **网络访问控制列表 (ACL)** 也可允许或拒绝进出各个子网的网络流量。

## 2. VPC 中的安全组和网络 ACL 有什么区别？
[点击查看安全组和网络ACL的区别详情](https://cloud.tencent.com/doc/product/215/5132#.E5.AE.89.E5.85.A8.E7.BB.84.E4.B8.8E.E7.BD.91.E7.BB.9Cacl.E7.9A.84.E5.8C.BA.E5.88.AB)。

## 3. 云主机TCP 25 端口出方向被封禁？
无法使用TCP 25 端口连接外部地址。例如，运行Telnet smtp.***.com 25，该命令执行失败。

**原因**：为了提升腾讯云IP地址发邮件的质量，将默认限制云主机TCP 25 端口连接外部地址 。

**解封方法**：请提[工单申请](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM)。
> 注意：如果您发起解封申请，腾讯云将默认您已确认并承诺：保证TCP 25 端口仅用来连接第三方的SMTP服务器，并从第三方的SMTP服务器向外发邮件。如发现您使用申请的IP直接通过SMTP发送邮件，腾讯云有权永久性封禁TCP 25端口，并不再提供解封服务。
