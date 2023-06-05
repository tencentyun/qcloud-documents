尊敬的腾讯云用户，您好！
为了确保您使用 VPN 服务的健康、稳定、高质量、高安全运行，腾讯云将于2023年05月19日00:00 ~ 06:00起对 VPN API 接口实现全量化支持 CAM 鉴权。

### 优势
- VPN API 接口全量化支持 CAM 鉴权后，您的 VPN 业务更加安全可控。
- VPN API 接口全量化期间，您当前的通信不受影响。

### 影响
如果子账户需要访问对应的接口，需要为子账户授权，具体请参见 [通过策略生成器创建自定义策略](https://cloud.tencent.com/document/product/598/37739)。
本次新增 CAM 鉴权接口如下：

| 接口名称                                | 接口功能                                       |
| --------------------------------------- | ---------------------------------------------- |
| [CreateVpnGatewaySslClient](https://cloud.tencent.com/document/api/215/70290)               | 创建 SSL-VPN-CLIENT                            |
| [CreateVpnGatewaySslServer](https://cloud.tencent.com/document/api/215/70289)               | 创建 SSL-VPN Server 端                        |
| [DeleteVpnGatewaySslClient](https://cloud.tencent.com/document/api/215/70288)               | 删除 SSL-VPN-CLIENT                            |
| [DeleteVpnGatewaySslServer](https://cloud.tencent.com/document/api/215/70287)               | 删除 SSL-VPN-SERVER                            |
| [DescribeCustomerGatewayVendors](https://cloud.tencent.com/document/api/215/17517)          | 查询可支持的对端网关厂商信息                 |
| [DescribeVpnGatewaySslClients](https://cloud.tencent.com/document/api/215/70286)            | 查询 SSL-VPN-CLIENT 列表                      |
| [DescribeVpnGatewaySslServers](https://cloud.tencent.com/document/api/215/70285)            | 查询 SSL-VPN SERVER 列表                      |
| [DisableVpnGatewaySslClientCert](https://cloud.tencent.com/document/api/215/70284)          | 禁用 SSL-VPN-CLIENT 证书                       |
| [DownloadVpnGatewaySslClientCert](https://cloud.tencent.com/document/api/215/70283)         | 下载 SSL-VPN-CLIENT 客户端证书                 |
| [GenerateVpnConnectionDefaultHealthCheckIp](https://cloud.tencent.com/document/api/215/90654) | 获取一对 VPN 通道健康检查地址                |

感谢您一如既往的支持！
此致！
腾讯云团队
