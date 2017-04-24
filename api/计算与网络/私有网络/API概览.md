## 1. VPC相关接口

| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 创建私有网络 | [CreateVpc](http://www.qcloud.com/doc/api/245/%E5%88%9B%E5%BB%BA%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C) | 创建私有网络，规划好您的网段。 |
| 删除私有网络 | [DeleteVpc](http://www.qcloud.com/doc/api/245/%E5%88%A0%E9%99%A4%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C) | 删除某个私有网络。 |
| 修改私有网络名称 | [ModifyVpcAttribute](http://www.qcloud.com/doc/api/245/%E4%BF%AE%E6%94%B9%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%90%8D%E7%A7%B0) | 修改指定vpc的名称。 |
| 查询私有网络列表 | [DescribeVpcEx](http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8) | 批量查询vpc信息，支持分页查询、模糊匹配等。|
| 绑定私有网络内主机与VIP | [AssociateVip](http://www.qcloud.com/doc/api/245/%E7%BB%91%E5%AE%9A%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%86%85%E4%B8%BB%E6%9C%BA%E4%B8%8EVIP) | 给vpc内云主机绑定一个VIP。 |
| 创建私有网络和基础网络设备互通 | [AttachClassicLinkVpc](https://www.qcloud.com/doc/api/245/2098) | 创建私有网络和基础网络设备互通。 |
| 删除私有网络和基础网络设备互通 | [DetachClassicLinkVpc](https://www.qcloud.com/doc/api/245/2097) | 删除私有网络和基础网络设备互通。 |
| 查询私有网络和基础网络设备互通 | [DescribeVpcClassicLink](https://www.qcloud.com/doc/api/245/2097) | 查询私有网络和基础网络设备互通。 |

## 2. 子网相关接口
| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 创建子网 | [CreateSubnet](http://www.qcloud.com/doc/api/245/%E5%88%9B%E5%BB%BA%E5%AD%90%E7%BD%91) |  创建子网，并指定可用区。 |
| 删除子网 | [DeleteSubnet](http://www.qcloud.com/doc/api/245/%E5%88%A0%E9%99%A4%E5%AD%90%E7%BD%91) | 删除指定子网。 |
| 修改子网名称 | [ModifySubnetAttribute](http://www.qcloud.com/document/product/215/1313) | 修改指定子网名称。 |
| 查询子网列表 | [DescribeSubnetEx](http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8) | 批量查询子网信息，支持分页查询、模糊匹配等。|
| 查询子网详情 | [DescribeSubnet](http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E8%AF%A6%E6%83%85) | 根据用户输入信息，如subnetId、子网名称等，查询对应子网的详细信息。|


## 3. 路由表相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 创建路由表 | [CreateRouteTable](http://www.qcloud.com/doc/api/245/%E5%88%9B%E5%BB%BA%E8%B7%AF%E7%94%B1%E8%A1%A8) | 创建一个路由表。 |
| 删除路由表 | [DeleteRouteTable](http://www.qcloud.com/doc/api/245/%E5%88%A0%E9%99%A4%E8%B7%AF%E7%94%B1%E8%A1%A8) | 删除指定路由表，删除后该路由表内路由策略都失效。 |
| 修改路由表 | [ModifyRouteTableAttribute](http://www.qcloud.com/doc/api/245/%E4%BF%AE%E6%94%B9%E8%B7%AF%E7%94%B1%E8%A1%A8) | 修改指定路由表名称。 |
| 查询路由表 | [DescribeRouteTable](http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8) | 根据用户输入信息，如routeTableId、路由表名称等，查询对应路由表的详细信息。|
| 修改子网关联的路由表 | [AssociateRouteTable](https://www.qcloud.com/document/api/215/1416) | 修改子网关联的路由表。 |
| 添加路由策略 | [CreateRoute](http://www.qcloud.com/doc/api/245/5688) | 新增路由策略。 |
| 删除路由策略 | [DeleteRoute](http://www.qcloud.com/doc/api/245/5689) | 删除路由策略。 |


## 4. 网络ACL相关接口
| 接口功能 | Action ID | 功能描述 |
|---------|---------|---------|
| 创建VPC网络ACL | [CreateNetworkAcl](http://www.qcloud.com/doc/api/245/%E5%88%9B%E5%BB%BAVPC%E7%BD%91%E7%BB%9CACL) | 创建安全防火墙。 |
| 删除网络ACL | [DeleteNetworkAcl](http://www.qcloud.com/doc/api/245/%E5%88%A0%E9%99%A4%E7%BD%91%E7%BB%9CACL) | 删除指定安全防火墙。 |
| 修改网络ACL名称 | [ModifyNetworkAcl](http://www.qcloud.com/doc/api/245/%E4%BF%AE%E6%94%B9%E7%BD%91%E7%BB%9CACL%E5%90%8D%E7%A7%B0) | 修改安全防火墙名称。 |
| 查询网络ACL列表 | [DescribeNetworkAcl](http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%BD%91%E7%BB%9CACL%E5%88%97%E8%A1%A8) | 查询vpc安全防火墙列表。 |
| 设置网络ACL规则 | [ModifyNetworkAclEntry](http://www.qcloud.com/doc/api/245/%E8%AE%BE%E7%BD%AE%E7%BD%91%E7%BB%9CACL%E8%A7%84%E5%88%99) | 设置安全防火墙网络规则。 |
| 网络ACL绑定子网 | [CreateSubnetAclRule](http://www.qcloud.com/doc/api/245/%E7%BD%91%E7%BB%9CACL%E7%BB%91%E5%AE%9A%E5%AD%90%E7%BD%91) | 安全防火墙绑定子网。 |
| 网络ACL解绑子网 | [DeteleSubnetAclRule](http://www.qcloud.com/doc/api/245/%E7%BD%91%E7%BB%9CACL%E8%A7%A3%E7%BB%91%E5%AD%90%E7%BD%91) | 安全防火墙和子网解绑。 |


## 5. VPN相关接口
| 接口功能 | Action ID |  功能描述 |
|---------|---------|---------|
| 查询VPN网关价格 | [InquiryVpnPrice](http://www.qcloud.com/doc/api/245/5104) | 查询VPN网关价格。 |
| 购买VPN网关 | [CreateVpn](http://www.qcloud.com/doc/api/245/5106) | 购买vpn网关。 |
| 修改VPN网关属性 | [ModifyVpnGw](http://www.qcloud.com/doc/api/245/5107) | 修改指定vpn网关信息，例如名称。|
| 查询VPN网关列表 | [DescribeVpnGw](http://www.qcloud.com/doc/api/245/5108) | 根据用户信息，如vpn网关ID，名称，查询对应vpn网关的信息。|
| 续费VPN网关 | [RenewVpn](http://www.qcloud.com/doc/api/245/5109) | 续费vpn网关。 |

## 6. 对端网关相关接口
| 接口功能 | Action ID |  功能描述 |
|---------|---------|---------|
| 创建对端网关 | [AddUserGw](http://www.qcloud.com/doc/api/245/5116) | 创建要连接的对端网关。 |
| 删除对端网关 | [DeleteUserGw](http://www.qcloud.com/doc/api/245/5117) | 删除指定对端网关。 |
| 修改对端网关名称 | [ModifyUserGw](http://www.qcloud.com/doc/api/245/5118) | 修改对端网关名称。 |
| 查询对端网关列表 | [DescribeUserGw](http://www.qcloud.com/doc/api/245/5119) | 根据用户信息，如对端网关ID，名称，查询对应对端网关的信息。|
| 获取可支持的对端网关厂商信息 | [DescribeUserGwVendor](http://www.qcloud.com/doc/api/245/5120) | 查询腾讯云vpn网关可支持的对端网关厂商信息。 |


## 7. VPN通道相关接口
| 接口功能 | Action ID |  功能描述 |
|---------|---------|---------|
| 创建VPN通道 | [AddVpnConnEx](http://www.qcloud.com/doc/api/245/5110) | 创建vpn加密通道，将vpc接入其他网络资源。 |
| 删除VPN通道 | [DeleteVpnConn](http://www.qcloud.com/doc/api/245/5111) | 删除指定vpn通道。|
| 修改VPN通道 | [ModifyVpnConnEx](http://www.qcloud.com/doc/api/245/5112) | 修改指定vpn通道的信息，如名称。 |
| 查询VPN通道列表 | [DescribeVpnConn](http://www.qcloud.com/doc/api/245/5113) | 根据用户信息，如通道ID，名称，查询对应通道的信息。|
| 下载VPN通道配置 | [GetVpnConnConfig](http://www.qcloud.com/doc/api/245/5114) | 下载vpn通道配置，对通道配置做调整。 |
| 获取VPN通道的监控数据 | [DescribeVpnConnMonitor](http://www.qcloud.com/doc/api/245/5115) |  获取VPN通道的监控数据。 |

## 8. SSL VPN相关接口
| 接口功能 | Action ID |  功能描述 |
|---------|---------|---------|
| 查询sslVPN | [DescribeSSLVpn](https://www.qcloud.com/doc/api/245/5121) | 查询sslVPN。 |
| 查询sslVPN域 | [DescribeSSLVpnDomain](https://www.qcloud.com/doc/api/245/5122) | 查询sslVPN域。 |
| 设置sslVPN域 | [SetSSLVpnDomain](https://www.qcloud.com/doc/api/245/5123) | 设置sslVPN域。 |

## 9. 对等连接
| 接口功能 | Action ID |  功能描述 |
|---------|---------|---------|
| 创建同地域对等连接 | [CreateVpcPeeringConnection](https://www.qcloud.com/doc/api/245/2107) | 创建同地域对等连接。 |
| 删除同地域对等连接 | [DeleteVpcPeeringConnection](https://www.qcloud.com/doc/api/245/2104) | 删除同地域对等连接。 |
| 修改同地域对等连接属性 | [ModifyVpcPeeringConnection](https://www.qcloud.com/doc/api/245/2103) | 修改同地域对等连接属性。 |
| 接受同地域对等连接 | [AcceptVpcPeeringConnection](https://www.qcloud.com/doc/api/245/2106) | 接受同地域对等连接。 |
| 驳回同地域对等连接 | [RejectVpcPeeringConnection](https://www.qcloud.com/doc/api/245/2105) | 驳回同地域对等连接。 |
| 启用同地域过期对等连接 | [EnableVpcPeeringConnection](https://www.qcloud.com/doc/api/245/2102) | 启用同地域过期对等连接。 |
| 创建跨地域对等连接 | [CreateVpcPeeringConnectionEx](https://www.qcloud.com/doc/api/245/4803) | 创建跨地域对等连接。 |
| 删除跨地域对等连接 | [DeleteVpcPeeringConnectionEx](https://www.qcloud.com/doc/api/245/4804) | 删除跨地域对等连接。 |
| 修改跨地域对等连接属性 | [ModifyVpcPeeringConnectionEx](https://www.qcloud.com/doc/api/245/4805) | 修改跨地域对等连接属性。 |
| 接受跨地域对等连接 | [AcceptVpcPeeringConnectionEx](https://www.qcloud.com/doc/api/245/4806) | 接受跨地域对等连接。 |
| 驳回跨地域对等连接 | [RejectVpcPeeringConnectionEx](https://www.qcloud.com/doc/api/245/4807) | 驳回跨地域对等连接。 |
| 启用跨地域过期对等连接 | [EnableVpcPeeringConnectionEx](https://www.qcloud.com/doc/api/245/4808) | 启用跨地域过期对等连接。 |
| 查询对等连接 | [DescribeVpcPeeringConnections](https://www.qcloud.com/doc/api/245/2101) | 查询对等连接。 |

## 10. 专线网关相关接口
| 接口功能 | Action ID |  功能描述 |
|---------|---------|---------|
| 创建专线网关 | [CreateDirectConnectGateway](https://www.qcloud.com/doc/api/245/4824) | 创建专线网关。 |
| 修改专线网关属性 | [ModifyDirectConnectGateway](https://www.qcloud.com/doc/api/245/4825) | 修改专线网关属性。|
| 删除专线网关 | [DeleteDirectConnectGateway](https://www.qcloud.com/doc/api/245/4826) | 删除专线网关。 |
| 查询专线网关 | [DescribeDirectConnectGateway](https://www.qcloud.com/doc/api/245/4827) | 查询专线网关。 |
| 添加专线网关本端IP转换 | [CreateLocalIPTranslationNatRule](https://www.qcloud.com/doc/api/245/5185) | 添加专线网关本端IP转换。 |
| 删除专线网关本端IP转换 | [DeleteLocalIPTranslationNatRule](https://www.qcloud.com/doc/api/245/5186) | 删除专线网关本端IP转换。 |
| 修改专线网关本端IP转换 | [ModifyLocalIPTranslationNatRule](https://www.qcloud.com/doc/api/245/5187) | 修改专线网关本端IP转换。 |
| 查询专线网关本端IP转换 | [DescribeLocalIPTranslationNatRule](https://www.qcloud.com/doc/api/245/5188) | 查询专线网关本端IP转换。 |
| 添加专线网关本端源IP端口转换 | [CreateLocalSourceIPPortTranslationNatRule](https://www.qcloud.com/document/api/215/5190) | 添加专线网关本端源IP端口转换。 |
| 删除专线网关本端源IP端口转换 | [DeleteLocalSourceIPPortTranslationNatRule](https://www.qcloud.com/document/api/215/5191) | 删除专线网关本端源IP端口转换。 |
| 修改专线网关本端源IP端口转换 | [ModifyLocalSourceIPPortTranslationNatRule](https://www.qcloud.com/document/api/215/5192) | 修改专线网关本端源IP端口转换。 |
| 查询专线网关本端源IP端口转换 | [DescribeLocalSourceIPPortTranslationNatRule](https://www.qcloud.com/document/api/215/5193) | 查询专线网关本端源IP端口转换。 |
| 添加专线网关本端目的IP端口转换 | [CreateLocalDestinationIPPortTranslationNatRule](https://www.qcloud.com/document/api/215/5195) | 添加专线网关本端目的IP端口转换。 |
| 删除专线网关本端目的IP端口转换 | [DeleteLocalDestinationIPPortTranslationNatRule](https://www.qcloud.com/document/product/215/5196) | 删除专线网关本端目的IP端口转换。 |
| 修改专线网关本端目的IP端口转换 | [ModifyLocalDestinationIPPortTranslationNatRule](https://www.qcloud.com/document/api/215/5197) | 修改专线网关本端目的IP端口转换。 |
| 查询专线网关本端目的IP端口转换 | [DescribeLocalDestinationIPPortTranslationNatRule](https://www.qcloud.com/document/api/215/5198) | 查询专线网关本端目的IP端口转换。 |
| 添加专线网关对端IP转换 | [CreatePeerIPTranslationNatRule](https://www.qcloud.com/doc/api/245/5190) | 添加专线网关对端IP转换。 |
| 删除专线网关对端IP转换 | [DeletePeerIPTranslationNatRule](https://www.qcloud.com/doc/api/245/5191) | 删除专线网关对端IP转换。 |
| 修改专线网关对端IP转换 | [ModifyPeerIPTranslationNatRule](https://www.qcloud.com/doc/api/245/5192) | 修改专线网关对端IP转换。 |
| 查询专线网关对端IP转换 | [DescribePeerIPTranslationNatRule](https://www.qcloud.com/doc/api/245/5193) | 查询专线网关对端IP转换。 |
| 添加本端IP转换 acl策略 | [CreateLocalIPTranslationAclRule](https://www.qcloud.com/doc/api/245/5205) | 添加本端IP转换 acl策略。 |
| 删除本端IP转换 acl策略 | [DeleteLocalIPTranslationAclRule](https://www.qcloud.com/doc/api/245/5206) | 删除本端IP转换 acl策略。 |
| 修改本端IP转换 acl策略 | [ModifyLocalIPTranslationAclRule](https://www.qcloud.com/doc/api/245/5207) | 修改本端IP转换 acl策略。 |
| 查询本端IP转换 acl策略 | [DescribeLocalIPTranslationAclRule](https://www.qcloud.com/doc/api/245/5208) | 查询本端IP转换 acl策略。 |
| 添加本端IP端口转换 acl策略 | [CreateLocalSourceIPPortTranslationAclRule](https://www.qcloud.com/doc/api/245/5211) | 添加本端IP端口转换 acl策略。 |
| 删除本端IP端口转换 acl策略 | [DeleteLocalSourceIPPortTranslationAclRule](https://www.qcloud.com/doc/api/245/5212) | 删除本端IP端口转换 acl策略。 |
| 修改本端IP端口转换 acl策略 | [ModifyLocalSourceIPPortTranslationAclRule](https://www.qcloud.com/doc/api/245/5213) | 修改本端IP端口转换 acl策略。 |
| 查询本端IP端口转换 acl策略 | [DescribeLocalSourceIPPortTranslationAclRule](https://www.qcloud.com/doc/api/245/5214) | 查询本端IP端口转换 acl策略。 |

## 11. NAT网关相关接口
| 接口功能 | Action ID |  功能描述 |
|---------|---------|---------|
| 创建NAT网关 | [CreateNatGateway](https://www.qcloud.com/doc/api/245/4094) |  创建NAT网关。 |
| 查询NAT网关创建状态 | [QueryNatGatewayProductionStatus](https://www.qcloud.com/doc/api/245/4089) |  查询NAT网关创建状态。 |
| 删除NAT网关 | [DeleteNatGateway](https://www.qcloud.com/doc/api/245/4087) | 删除NAT网关。 |
| 修改NAT网关 | [ModifyNatGateway](https://www.qcloud.com/doc/api/245/4086) | 修改NAT网关。 |
| 查询NAT网关 | [DescribeNatGateway](https://www.qcloud.com/doc/api/245/4088) | 查询NAT网关。 |
| NAT网关绑定EIP | [EipBindNatGateway](https://www.qcloud.com/doc/api/245/4093) | NAT网关绑定EIP。 |
| NAT网关解绑EIP | [EipUnBindNatGateway](https://www.qcloud.com/doc/api/245/4092) | NAT网关解绑EIP。 |
| 升级NAT网关规格 | [UpgradeNatGateway](https://www.qcloud.com/doc/api/245/4090) | 升级NAT网关规格。 |

## 12. 弹性网卡相关接口
| 接口功能 | Action ID |  功能描述 |
|---------|---------|---------|
| 创建弹性网卡 | [CreateNetworkInterface](https://www.qcloud.com/doc/api/245/4811) |  创建弹性网卡。 |
| 删除弹性网卡 | [DeleteNetworkInterface](https://www.qcloud.com/doc/api/245/4813) |  删除弹性网卡。 |
| 查询弹性网卡信息 | [DescribeNetworkInterfaces](https://www.qcloud.com/doc/api/245/4814) | 查询弹性网卡信息。 |
| 弹性网卡申请内网Ip | [AssignPrivateIpAddresses](https://www.qcloud.com/doc/api/245/4817) | 弹性网卡申请内网Ip。 |
| 弹性网卡退还内网Ip | [UnassignPrivateIpAddresses](https://www.qcloud.com/doc/api/245/4819) | 弹性网卡退还内网Ip。 |
| 弹性网卡绑定云主机 | [AttachNetworkInterface](https://www.qcloud.com/doc/api/245/4820) | 弹性网卡绑定云主机。 |
| 弹性网卡解绑云主机 | [DetachNetworkInterface](https://www.qcloud.com/document/product/215/4822) | 弹性网卡解绑云主机。 |
| 弹性网卡迁移 | [MigrateNetworkInterface](https://www.qcloud.com/doc/api/245/5384) | 弹性网卡迁移。 |
| 内网IP迁移 | [MigratePrivateIpAddress](https://www.qcloud.com/doc/api/245/5385) | 内网IP迁移。 |

