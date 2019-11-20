>?当前页面接口为旧版 API，未来可能停止维护。私有网络 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [私有网络 API 3.0](https://cloud.tencent.com/document/api/215/15755)。
## 1. VPC 相关接口

| 接口功能            | Action ID                                | 功能描述                    |
| --------------- | ---------------------------------------- | ----------------------- |
| 创建私有网络          | [CreateVpc](http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BA%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C) | 创建私有网络，规划好您的网段。         |
| 删除私有网络          | [DeleteVpc](http://cloud.tencent.com/doc/api/245/%E5%88%A0%E9%99%A4%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C) | 删除某个私有网络。               |
| 修改私有网络名称        | [ModifyVpcAttribute](http://cloud.tencent.com/doc/api/245/%E4%BF%AE%E6%94%B9%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%90%8D%E7%A7%B0) | 修改指定 vpc 的名称。             |
| 查询私有网络列表        | [DescribeVpcEx](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8) | 批量查询 vpc 信息，支持分页查询、模糊匹配等。 |
| 绑定私有网络内主机与 VIP   | [AssociateVip](http://cloud.tencent.com/doc/api/245/%E7%BB%91%E5%AE%9A%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%86%85%E4%B8%BB%E6%9C%BA%E4%B8%8EVIP) | 给 vpc 内云服务器绑定一个 VIP。       |
| 创建私有网络和基础网络设备互通 | [AttachClassicLinkVpc](https://cloud.tencent.com/doc/api/245/2098) | 创建私有网络和基础网络设备互通。        |
| 删除私有网络和基础网络设备互通 | [DetachClassicLinkVpc](https://cloud.tencent.com/doc/api/245/2097) | 删除私有网络和基础网络设备互通。        |
| 查询私有网络和基础网络设备互通 | [DescribeVpcClassicLink](https://cloud.tencent.com/document/api/215/2112) | 查询私有网络和基础网络设备互通。        |

## 2. 子网相关接口
| 接口功能   | Action ID                                | 功能描述                                  |
| ------ | ---------------------------------------- | ------------------------------------- |
| 创建子网   | [CreateSubnet](http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BA%E5%AD%90%E7%BD%91) | 创建子网，并指定可用区。                          |
| 删除子网   | [DeleteSubnet](http://cloud.tencent.com/doc/api/245/%E5%88%A0%E9%99%A4%E5%AD%90%E7%BD%91) | 删除指定子网。                               |
| 修改子网名称 | [ModifySubnetAttribute](https://cloud.tencent.com/document/api/215/1313) | 修改指定子网名称。                             |
| 查询子网列表 | [DescribeSubnetEx](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8) | 批量查询子网信息，支持分页查询、模糊匹配等。                |
| 查询子网详情 | [DescribeSubnet](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E8%AF%A6%E6%83%85) | 根据用户输入信息，如 subnetId、子网名称等，查询对应子网的详细信息。 |


## 3. 路由表相关接口
| 接口功能       | Action ID                                | 功能描述                                     |
| ---------- | ---------------------------------------- | ---------------------------------------- |
| 创建路由表      | [CreateRouteTable](http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BA%E8%B7%AF%E7%94%B1%E8%A1%A8) | 创建一个路由表。                                 |
| 删除路由表      | [DeleteRouteTable](http://cloud.tencent.com/doc/api/245/%E5%88%A0%E9%99%A4%E8%B7%AF%E7%94%B1%E8%A1%A8) | 删除指定路由表，删除后该路由表内路由策略都失效。                 |
| 修改路由表      | [ModifyRouteTableAttribute](http://cloud.tencent.com/doc/api/245/%E4%BF%AE%E6%94%B9%E8%B7%AF%E7%94%B1%E8%A1%A8) | 修改指定路由表名称。                               |
| 查询路由表      | [DescribeRouteTable](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8) | 根据用户输入信息，如 routeTableId、路由表名称等，查询对应路由表的详细信息。 |
| 修改子网关联的路由表 | [AssociateRouteTable](https://cloud.tencent.com/document/api/215/1416) | 修改子网关联的路由表。                              |
| 添加路由策略     | [CreateRoute](http://cloud.tencent.com/doc/api/245/5688) | 新增路由策略。                                  |
| 删除路由策略     | [DeleteRoute](http://cloud.tencent.com/doc/api/245/5689) | 删除路由策略。                                  |


## 4. 网络 ACL 相关接口
| 接口功能       | Action ID                                | 功能描述          |
| ---------- | ---------------------------------------- | ------------- |
| 创建 VPC 网络 ACL | [CreateNetworkAcl](http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BAVPC%E7%BD%91%E7%BB%9CACL) | 创建安全防火墙。      |
| 删除网络 ACL    | [DeleteNetworkAcl](http://cloud.tencent.com/doc/api/245/%E5%88%A0%E9%99%A4%E7%BD%91%E7%BB%9CACL) | 删除指定安全防火墙。    |
| 修改网络 ACL 名称  | [ModifyNetworkAcl](http://cloud.tencent.com/doc/api/245/%E4%BF%AE%E6%94%B9%E7%BD%91%E7%BB%9CACL%E5%90%8D%E7%A7%B0) | 修改安全防火墙名称。    |
| 查询网络 ACL 列表  | [DescribeNetworkAcl](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%BD%91%E7%BB%9CACL%E5%88%97%E8%A1%A8) | 查询 vpc 安全防火墙列表。 |
| 设置网络 ACL 规则  | [ModifyNetworkAclEntry](http://cloud.tencent.com/doc/api/245/%E8%AE%BE%E7%BD%AE%E7%BD%91%E7%BB%9CACL%E8%A7%84%E5%88%99) | 设置安全防火墙网络规则。  |
| 网络 ACL 绑定子网  | [CreateSubnetAclRule](http://cloud.tencent.com/doc/api/245/%E7%BD%91%E7%BB%9CACL%E7%BB%91%E5%AE%9A%E5%AD%90%E7%BD%91) | 安全防火墙绑定子网。    |
| 网络 ACL 解绑子网  | [DeteleSubnetAclRule](http://cloud.tencent.com/doc/api/245/%E7%BD%91%E7%BB%9CACL%E8%A7%A3%E7%BB%91%E5%AD%90%E7%BD%91) | 安全防火墙和子网解绑。   |


## 5. VPN 相关接口
| 接口功能      | Action ID                                | 功能描述                             |
| --------- | ---------------------------------------- | -------------------------------- |
| 查询 VPN 网关价格 | [InquiryVpnPrice](http://cloud.tencent.com/doc/api/245/5104) | 查询 VPN 网关价格。                       |
| 购买 VPN 网关   | [CreateVpn](http://cloud.tencent.com/doc/api/245/5106) | 购买 VPN 网关。                         |
| 修改 VPN 网关属性 | [ModifyVpnGw](http://cloud.tencent.com/doc/api/245/5107) | 修改指定 VPN 网关信息，例如名称。                |
| 查询 VPN 网关列表 | [DescribeVpnGw](http://cloud.tencent.com/doc/api/245/5108) | 根据用户信息，如 VPN 网关 ID，名称，查询对应 VPN 网关的信息。 |
| 续费 VPN 网关   | [RenewVpn](http://cloud.tencent.com/doc/api/245/5109) | 续费 VPN 网关。                         |

## 6. 对端网关相关接口
| 接口功能           | Action ID                                | 功能描述                           |
| -------------- | ---------------------------------------- | ------------------------------ |
| 创建对端网关         | [AddUserGw](http://cloud.tencent.com/doc/api/245/5116) | 创建要连接的对端网关。                    |
| 删除对端网关         | [DeleteUserGw](http://cloud.tencent.com/doc/api/245/5117) | 删除指定对端网关。                      |
| 修改对端网关名称       | [ModifyUserGw](http://cloud.tencent.com/doc/api/245/5118) | 修改对端网关名称。                      |
| 查询对端网关列表       | [DescribeUserGw](http://cloud.tencent.com/doc/api/245/5119) | 根据用户信息，如对端网关 ID，名称，查询对应对端网关的信息。 |
| 获取可支持的对端网关厂商信息 | [DescribeUserGwVendor](http://cloud.tencent.com/doc/api/245/5120) | 查询腾讯云 VPN 网关可支持的对端网关厂商信息。        |


## 7. VPN 通道相关接口
| 接口功能         | Action ID                                | 功能描述                       |
| ------------ | ---------------------------------------- | -------------------------- |
| 创建 VPN 通道      | [AddVpnConnEx](http://cloud.tencent.com/doc/api/245/5110) | 创建 VPN 加密通道，将 vpc 接入其他网络资源。    |
| 删除 VPN 通道      | [DeleteVpnConn](http://cloud.tencent.com/doc/api/245/5111) | 删除指定 VPN 通道。                 |
| 修改 VPN 通道      | [ModifyVpnConnEx](http://cloud.tencent.com/doc/api/245/5112) | 修改指定 VPN 通道的信息，如名称。          |
| 查询 VPN 通道列表    | [DescribeVpnConn](http://cloud.tencent.com/doc/api/245/5113) | 根据用户信息，如通道 ID，名称，查询对应通道的信息。 |
| 下载 VPN 通道配置    | [GetVpnConnConfig](http://cloud.tencent.com/doc/api/245/5114) | 下载 VPN 通道配置，对通道配置做调整。        |
| 获取 VPN 通道的监控数据 | [DescribeVpnConnMonitor](http://cloud.tencent.com/doc/api/245/5115) | 获取 VPN 通道的监控数据。              |

## 8. SSL VPN 相关接口
| 接口功能      | Action ID                                | 功能描述       |
| --------- | ---------------------------------------- | ---------- |
| 查询 sslVPN  | [DescribeSSLVpn](https://cloud.tencent.com/doc/api/245/5121) | 查询 sslVPN。  |
| 查询 sslVPN 域 | [DescribeSSLVpnDomain](https://cloud.tencent.com/doc/api/245/5122) | 查询 sslVPN域。 |
| 设置 sslVPN 域 | [SetSSLVpnDomain](https://cloud.tencent.com/doc/api/245/5123) | 设置 sslVPN域。 |

## 9. 对等连接
| 接口功能        | Action ID                                | 功能描述         |
| ----------- | ---------------------------------------- | ------------ |
| 创建同地域对等连接   | [CreateVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2107) | 创建同地域对等连接。   |
| 删除同地域对等连接   | [DeleteVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2104) | 删除同地域对等连接。   |
| 修改同地域对等连接属性 | [ModifyVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2103) | 修改同地域对等连接属性。 |
| 接受同地域对等连接   | [AcceptVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2106) | 接受同地域对等连接。   |
| 驳回同地域对等连接   | [RejectVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2105) | 驳回同地域对等连接。   |
| 启用同地域过期对等连接 | [EnableVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2102) | 启用同地域过期对等连接。 |
| 创建跨地域对等连接   | [CreateVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4803) | 创建跨地域对等连接。   |
| 删除跨地域对等连接   | [DeleteVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4804) | 删除跨地域对等连接。   |
| 修改跨地域对等连接属性 | [ModifyVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4805) | 修改跨地域对等连接属性。 |
| 接受跨地域对等连接   | [AcceptVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4806) | 接受跨地域对等连接。   |
| 驳回跨地域对等连接   | [RejectVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4807) | 驳回跨地域对等连接。   |
| 启用跨地域过期对等连接 | [EnableVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4808) | 启用跨地域过期对等连接。 |
| 查询对等连接      | [DescribeVpcPeeringConnections](https://cloud.tencent.com/doc/api/245/2101) | 查询对等连接。      |

## 10. 专线网关相关接口
| 接口功能             | Action ID                                | 功能描述              |
| ---------------- | ---------------------------------------- | ----------------- |
| 创建专线网关           | [CreateDirectConnectGateway](https://cloud.tencent.com/doc/api/245/4824) | 创建专线网关。           |
| 修改专线网关属性         | [ModifyDirectConnectGateway](https://cloud.tencent.com/doc/api/245/4826) | 修改专线网关属性。         |
| 删除专线网关           | [DeleteDirectConnectGateway](https://cloud.tencent.com/doc/api/245/4825) | 删除专线网关。           |
| 查询专线网关           | [DescribeDirectConnectGateway](https://cloud.tencent.com/doc/api/245/4827) | 查询专线网关。           |
| 添加专线网关本端 IP 转换     | [CreateLocalIPTranslationNatRule](https://cloud.tencent.com/doc/api/245/5185) | 添加专线网关本端 IP 转换。     |
| 删除专线网关本端 IP 转换     | [DeleteLocalIPTranslationNatRule](https://cloud.tencent.com/doc/api/245/5186) | 删除专线网关本端 IP 转换。     |
| 修改专线网关本端 IP 转换     | [ModifyLocalIPTranslationNatRule](https://cloud.tencent.com/doc/api/245/5187) | 修改专线网关本端 IP 转换。     |
| 查询专线网关本端 IP 转换     | [DescribeLocalIPTranslationNatRule](https://cloud.tencent.com/doc/api/245/5188) | 查询专线网关本端 IP 转换。     |
| 添加专线网关本端源 IP 端口转换  | [CreateLocalSourceIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5190) | 添加专线网关本端源 IP 端口转换。  |
| 删除专线网关本端源 IP 端口转换  | [DeleteLocalSourceIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5191) | 删除专线网关本端源 IP 端口转换。  |
| 修改专线网关本端源 IP 端口转换  | [ModifyLocalSourceIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5192) | 修改专线网关本端源 IP 端口转换。  |
| 查询专线网关本端源 IP 端口转换  | [DescribeLocalSourceIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5193) | 查询专线网关本端源 IP 端口转换。  |
| 添加专线网关本端目的 IP 端口转换 | [CreateLocalDestinationIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5195) | 添加专线网关本端目的 IP 端口转换。 |
| 删除专线网关本端目的 IP 端口转换 | [DeleteLocalDestinationIPPortTranslationNatRule](https://cloud.tencent.com/document/product/215/5196) | 删除专线网关本端目的 IP 端口转换。 |
| 修改专线网关本端目的IP端口转换 | [ModifyLocalDestinationIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5197) | 修改专线网关本端目的 IP 端口转换。 |
| 查询专线网关本端目的 IP 端口转换 | [DescribeLocalDestinationIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5198) | 查询专线网关本端目的 IP 端口转换。 |
| 添加专线网关对端 IP 转换     | [CreatePeerIPTranslationNatRule](https://cloud.tencent.com/document/api/215/5201) | 添加专线网关对端 IP 转换。     |
| 删除专线网关对端 IP 转换     | [DeletePeerIPTranslationNatRule](https://cloud.tencent.com/document/api/215/5202) | 删除专线网关对端 IP 转换。     |
| 修改专线网关对端 IP 转换     | [ModifyPeerIPTranslationNatRule](https://cloud.tencent.com/document/api/215/5203) | 修改专线网关对端 IP 转换。     |
| 查询专线网关对端 IP 转换     | [DescribePeerIPTranslationNatRule](https://cloud.tencent.com/document/api/215/5204) | 查询专线网关对端 IP 转换。     |
| 添加本端 IP 转换 ACL 策略   | [CreateLocalIPTranslationAclRule](https://cloud.tencent.com/doc/api/245/5205) | 添加本端 IP 转换  ACL 策略。   |
| 删除本端 IP 转换  ACL 策略   | [DeleteLocalIPTranslationAclRule](https://cloud.tencent.com/doc/api/245/5206) | 删除本端IP转换 acl策略。   |
| 修改本端 IP 转换  ACL 策略   | [ModifyLocalIPTranslationAclRule](https://cloud.tencent.com/doc/api/245/5207) | 修改本端 IP 转换  ACL 策略。   |
| 查询本端 IP 转换  ACL 策略   | [DescribeLocalIPTranslationAclRule](https://cloud.tencent.com/doc/api/245/5208) | 查询本端 IP 转换  ACL 策略。   |
| 添加本端 IP 端口转换  ACL 策略 | [CreateLocalSourceIPPortTranslationAclRule](https://cloud.tencent.com/doc/api/245/5211) | 添加本端 IP 端口转换  ACL 策略。 |
| 删除本端 IP 端口转换  ACL 策略 | [DeleteLocalSourceIPPortTranslationAclRule](https://cloud.tencent.com/doc/api/245/5212) | 删除本端 IP 端口转换  ACL 策略。 |
| 修改本端 IP 端口转换  ACL 策略 | [ModifyLocalSourceIPPortTranslationAclRule](https://cloud.tencent.com/doc/api/245/5213) | 修改本端 IP 端口转换 ACL 策略。 |
| 查询本端 IP 端口转换 ACL 策略 | [DescribeLocalSourceIPPortTranslationAclRule](https://cloud.tencent.com/doc/api/245/5214) | 查询本端 IP 端口转换  ACL 策略。 |

## 11. NAT 网关相关接口
| 接口功能        | Action ID                                | 功能描述         |
| ----------- | ---------------------------------------- | ------------ |
| 创建 NAT 网关     | [CreateNatGateway](https://cloud.tencent.com/doc/api/245/4094) | 创建 NAT 网关。     |
| 查询 NAT 网关创建状态 | [QueryNatGatewayProductionStatus](https://cloud.tencent.com/doc/api/245/4089) | 查询 NAT 网关创建状态。 |
| 删除 NAT 网关     | [DeleteNatGateway](https://cloud.tencent.com/doc/api/245/4087) | 删除 NAT 网关。     |
| 修改 NAT 网关     | [ModifyNatGateway](https://cloud.tencent.com/doc/api/245/4086) | 修改 NAT 网关。     |
| 查询 NAT 网关     | [DescribeNatGateway](https://cloud.tencent.com/doc/api/245/4088) | 查询 NAT 网关。     |
| NAT 网关绑定 EIP  | [EipBindNatGateway](https://cloud.tencent.com/doc/api/245/4093) | NAT 网关绑定 EIP。  |
| NAT 网关解绑 EIP  | [EipUnBindNatGateway](https://cloud.tencent.com/doc/api/245/4092) | NAT 网关解绑 EIP。  |
| 升级 NAT 网关规格   | [UpgradeNatGateway](https://cloud.tencent.com/doc/api/245/4090) | 升级 NAT 网关规格。   |

## 12. 弹性网卡相关接口
| 接口功能       | Action ID                                | 功能描述        |
| ---------- | ---------------------------------------- | ----------- |
| 创建弹性网卡     | [CreateNetworkInterface](https://cloud.tencent.com/doc/api/245/4811) | 创建弹性网卡。     |
| 删除弹性网卡     | [DeleteNetworkInterface](https://cloud.tencent.com/doc/api/245/4813) | 删除弹性网卡。     |
| 查询弹性网卡信息   | [DescribeNetworkInterfaces](https://cloud.tencent.com/doc/api/245/4814) | 查询弹性网卡信息。   |
| 弹性网卡申请内网 IP | [AssignPrivateIpAddresses](https://cloud.tencent.com/doc/api/245/4817) | 弹性网卡申请内网 IP。 |
| 弹性网卡退还内网 IP | [UnassignPrivateIpAddresses](https://cloud.tencent.com/doc/api/245/4819) | 弹性网卡退还内网 IP。 |
| 弹性网卡绑定云服务器 | [AttachNetworkInterface](https://cloud.tencent.com/doc/api/245/4820) | 弹性网卡绑定云服务器。 |
| 弹性网卡解绑云服务器 | [DetachNetworkInterface](https://cloud.tencent.com/document/product/215/4822) | 弹性网卡解绑云服务器。 |
| 弹性网卡迁移     | [MigrateNetworkInterface](https://cloud.tencent.com/doc/api/245/5384) | 弹性网卡迁移。     |
| 内网 IP 迁移     | [MigratePrivateIpAddress](https://cloud.tencent.com/doc/api/245/5385) | 内网 IP 迁移。     |

## 13. 流日志相关接口
| 接口功能    | Action ID                                | 功能描述       |
| ------- | ---------------------------------------- | ---------- |
| 创建流日志   | [CreateFlowLog](https://cloud.tencent.com/document/api/215/14038)           | 创建流日志。     |
| 删除流日志   | [DeleteFlowLog](https://cloud.tencent.com/document/api/215/14040)           | 删除流日志。     |
| 查询流日志信息 | [DescribeFlowLog](https://cloud.tencent.com/document/api/215/14041)       | 查询流日志实例信息。 |
| 查询流日志列表 | [DescribeFlowLogs](https://cloud.tencent.com/document/api/215/14042)      | 查询流日志列表信息。 |
| 修改流日志属性 | [ModifyFlowLogAttribute](https://cloud.tencent.com/document/api/215/14039) | 修改流日志属性。   |
