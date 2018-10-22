#VPC安全
####如何确保VPC中云主机的安全？
VPC 本身是一个逻辑隔离的网络环境，可以通过设置安全组和网络 ACL 来进行流量控制：

- 安全组提供CVM实例级别的网络流量控制。没有显式允许进出实例的流量将自动被拒绝。更多信息可参考[安全组文档](https://cloud.tencent.com/document/product/213/12452)。
- 网络访问控制列表 (ACL) 提供子网级别的网络流量控制，更多信息可参考[网络ACL文档](https://cloud.tencent.com/document/product/215/5132)。