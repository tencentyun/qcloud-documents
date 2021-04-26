### 如何确保 VPC 中云服务器的安全？
VPC 本身是一个逻辑隔离的网络环境，可以通过设置安全组和网络 ACL 来进行流量控制：
- 安全组提供 CVM 实例级别的网络流量控制。没有显式允许进出实例的流量将自动被拒绝。
更多信息，请参见 [安全组文档](https://cloud.tencent.com/document/product/213/12452)。
- 网络访问控制列表（ACL）提供子网级别的网络流量控制。更多信息，请参见 [网络 ACL 文档](https://cloud.tencent.com/document/product/215/5132)。
