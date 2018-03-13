实例元数据是有关您运行的云主机实例的数据，可以用来配置或管理正在运行的实例。
>注：虽然只能从实例云主机自身内部访问实例元数据，但数据并未进行加密保护。可访问实例的人员均可查看其元数据。因此，您应当采取适当的预防措施来保护敏感数据（例如使用永久加密密钥）。

腾讯云现在提供如下meta-data信息：

| 数据 | 描述 | 引入版本 |
|---------|---------|---------|
| instance-id | 云主机唯一 ID | 1.0 |
| uuid | 云主机唯一 ID | 1.0 |
| local-ipv4 | 内网 IP | 1.0 |
| public-ipv4 | 公网 IP | 1.0 |
| mac | eth0 设备 mac 地址 | 1.0 |
| placement/region | 地域信息 | 1.1 |
| placement/zone | 可用区信息 | 1.1 |
| network/network/macs/**mac**/mac | 本机网络接口设备地址 | 1.2 |
| network/network/macs/**mac**/primary-local-ipv4 | 本机网络接口主内网 IP 地址 | 1.2 |
| network/network/macs/**mac**/public-ipv4s | 本机网络接口公网 IP 地址 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/gateway | 本机网络接口网关地址 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/local-ipv4 | 本机网络接口内网 IP 地址 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/public-ipv4 | 本机网络接口公网 IP 地址 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/public-ipv4-mode | 本机网络接口公网网络模式 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/subnet-mask | 本机网络接口子网掩码 | 1.2 |

> 以上表格中粗体 **mac** 和 **local-ipv4** 字段分别表示本机指定网络接口的设备地址和内网 IP 地址。
