## 1. VPC Related APIs

| Feature | Action ID | Description |
|---------|---------|---------|
| Create a VPC | [CreateVpc](http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BA%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C) | Create a VPC and plan your network segment. |
| Delete a VPC | [DeleteVpc](http://cloud.tencent.com/doc/api/245/%E5%88%A0%E9%99%A4%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C) | Delete a VPC. |
| Modify a VPC name | [ModifyVpcAttribute](http://cloud.tencent.com/doc/api/245/%E4%BF%AE%E6%94%B9%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%90%8D%E7%A7%B0) | Modify the name of a specified VPC. |
| Query VPC list | [DescribeVpcEx](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8) | Query VPC information in batches, supporting paged query, fuzzy match, etc. |
| Bind VPC CVM to VIP | [AssociateVip](http://cloud.tencent.com/doc/api/245/%E7%BB%91%E5%AE%9A%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%86%85%E4%B8%BB%E6%9C%BA%E4%B8%8EVIP) | Bind a VIP to VPC CVM. |
| Create interconnection between VPC and basic network device | [AttachClassicLinkVpc](https://cloud.tencent.com/doc/api/245/2098) | Create interconnection between VPC and basic network device. |
| Delete interconnection between VPC and basic network device | [DetachClassicLinkVpc](https://cloud.tencent.com/doc/api/245/2097) | Delete interconnection between VPC and basic network device. |
| Query interconnection between VPC and basic network device | [DescribeVpcClassicLink](https://cloud.tencent.com/document/api/215/2112) | Query interconnection between VPC and basic network device. |

## 2. Subnet Related APIs
| Feature | Action ID | Description | 
|---------|---------|---------|
| Create a subnet | [CreateSubnet](http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BA%E5%AD%90%E7%BD%91) | Create a subnet and specify its availability zone. |
| Delete a subnet | [DeleteSubnet](http://cloud.tencent.com/doc/api/245/%E5%88%A0%E9%99%A4%E5%AD%90%E7%BD%91) | Delete a subnet. |
| Modify a subnet name | [ModifySubnetAttribute](https://cloud.tencent.com/document/api/215/1313) | Modify a subnet name. |
| Query subnet list | [DescribeSubnetEx](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E5%88%97%E8%A1%A8) | Query the subnet information in batches, supporting paged query, fuzzy match, etc. |
| Query subnet details | [DescribeSubnet](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E5%AD%90%E7%BD%91%E8%AF%A6%E6%83%85) | Query subnet details based on user inputs such as subnet ID and subnet name. |


## 3. Routing Table Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Create a routing table | [CreateRouteTable](http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BA%E8%B7%AF%E7%94%B1%E8%A1%A8) | Create a routing table. |
| Delete a routing table | [DeleteRouteTable](http://cloud.tencent.com/doc/api/245/%E5%88%A0%E9%99%A4%E8%B7%AF%E7%94%B1%E8%A1%A8) | Delete a routing table, after which all the routing policies in this routing table will become invalid. |
| Modify a routing table | [ModifyRouteTableAttribute](http://cloud.tencent.com/doc/api/245/%E4%BF%AE%E6%94%B9%E8%B7%AF%E7%94%B1%E8%A1%A8) | Modify the name of a routing table. |
| Query a routing table | [DescribeRouteTable](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E8%B7%AF%E7%94%B1%E8%A1%A8) | Query routing table details based on user inputs such as routing table ID and routing table name. |
| Modify a routing table associated with a subnet | [AssociateRouteTable](https://cloud.tencent.com/document/api/215/1416) | Modify a routing table associated with a subnet. |
| Add a routing policy | [CreateRoute](http://cloud.tencent.com/doc/api/245/5688) | Add a routing policy. |
| Delete a routing policy | [DeleteRoute](http://cloud.tencent.com/doc/api/245/5689) | Delete a routing policy. |


## 4. Network ACL Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Create a VPC network ACL | [CreateNetworkAcl](http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BAVPC%E7%BD%91%E7%BB%9CACL) | Create a security firewall. |
| Delete a network ACL | [DeleteNetworkAcl](http://cloud.tencent.com/doc/api/245/%E5%88%A0%E9%99%A4%E7%BD%91%E7%BB%9CACL) | Delete a security firewall. |
| Modify the name of network ACL | [ModifyNetworkAcl](http://cloud.tencent.com/doc/api/245/%E4%BF%AE%E6%94%B9%E7%BD%91%E7%BB%9CACL%E5%90%8D%E7%A7%B0) | Modify the name of security firewall. |
| Query a network ACL list| [DescribeNetworkAcl](http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%BD%91%E7%BB%9CACL%E5%88%97%E8%A1%A8) | Query a VPC security firewall list. |
| Set network ACL rules | [ModifyNetworkAclEntry](http://cloud.tencent.com/doc/api/245/%E8%AE%BE%E7%BD%AE%E7%BD%91%E7%BB%9CACL%E8%A7%84%E5%88%99) | Set security firewall network rules. |
| Bind a subnet to a network ACL | [CreateSubnetAclRule](http://cloud.tencent.com/doc/api/245/%E7%BD%91%E7%BB%9CACL%E7%BB%91%E5%AE%9A%E5%AD%90%E7%BD%91) | Bind a subnet to a security firewall. |
| Unbind a subnet from a network ACL | [DeteleSubnetAclRule](http://cloud.tencent.com/doc/api/245/%E7%BD%91%E7%BB%9CACL%E8%A7%A3%E7%BB%91%E5%AD%90%E7%BD%91) | Unbind a subnet from a security firewall. |


## 5. VPN Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Query the price of a VPN gateway | [InquiryVpnPrice](http://cloud.tencent.com/doc/api/245/5104) | Query the price of a VPN gateway. |
| Purchase a VPN gateway | [CreateVpn](http://cloud.tencent.com/doc/api/245/5106) | Purchase a VPN gateway. |
| Modify the attributes of a VPN gateway | [ModifyVpnGw](http://cloud.tencent.com/doc/api/245/5107) | Modify the information of a VPN gateway, such as name. |
| Query the VPN gateway list | [DescribeVpnGw](http://cloud.tencent.com/doc/api/245/5108) | Query VPN gateway details based on user information such as the ID and name of the VPN gateway. |
| Renew the VPN gateway | [RenewVpn](http://cloud.tencent.com/doc/api/245/5109) | Renew the VPN gateway. |

## 6. Peer Gateway Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Create a peer gateway | [AddUserGw](http://cloud.tencent.com/doc/api/245/5116) | Create a peer gateway to connect to. |
| Delete a peer gateway | [DeleteUserGw](http://cloud.tencent.com/doc/api/245/5117) | Delete a peer gateway. |
| Modify the name of a peer gateway | [ModifyUserGw](http://cloud.tencent.com/doc/api/245/5118) | Modify the name of a peer gateway. |
| Query the peer gateway list | [DescribeUserGw](http://cloud.tencent.com/doc/api/245/5119) | Query peer gateway details based on user information such as the ID and name of the peer gateway. |
| Obtain the vendor information of supported peer gateways | [DescribeUserGwVendor](http://cloud.tencent.com/doc/api/245/5120) | Query the vendor information of peer gateways supported by Tencent Cloud VPN. |


## 7. VPN Tunnel Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Create a VPN tunnel | [AddVpnConn](http://cloud.tencent.com/doc/api/245/5110) | Create a VPN encrypted tunnel to connect the VPC to other network resources. |
| Delete a VPN tunnel | [DeleteVpnConn](http://cloud.tencent.com/doc/api/245/5111) | Delete a VPN tunnel. |
| Modify a VPN tunnel | [ModifyVpnConn](http://cloud.tencent.com/doc/api/245/5112) | Modify the information of a VPN tunnel, such as name. |
| Query the VPN tunnel list | [DescribeVpnConn](http://cloud.tencent.com/doc/api/245/5113) | Query VPN tunnel details based on user information such as the ID and name of the VPN tunnel. |
| Download VPN tunnel configuration | [GetVpnConnConfig](http://cloud.tencent.com/doc/api/245/5114) | Download VPN tunnel configuration to make adjustments to tunnel configuration. |
| Obtain the monitoring data of a VPN tunnel | [DescribeVpnConnMonitor](http://cloud.tencent.com/doc/api/245/5115) | Obtain the monitoring data of a VPN tunnel. |

## 8. SSL VPN Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Query an SSL VPN | [DescribeSSLVpn](https://cloud.tencent.com/doc/api/245/5121) | Query an SSL VPN. |
| Query an SSL VPN domain | [DescribeSSLVpnDomain](https://cloud.tencent.com/doc/api/245/5122) | Query an SSL VPN domain. |
| Set an SSL VPN domain | [SetSSLVpnDomain](https://cloud.tencent.com/doc/api/245/5123) | Set an SSL VPN domain. |

## 9. Peering Connection
| Feature | Action ID | Description |
|---------|---------|---------|
| Create intra-region peering connection | [CreateVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2107) | Create intra-region peering connection. |
| Delete intra-region peering connection | [DeleteVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2104) | Delete intra-region peering connection. |
| Modify intra-region peering connection attributes | [ModifyVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2103) | Modify intra-region peering connection attributes. |
| Accept intra-region peering connection | [AcceptVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2106) | Accept intra-region peering connection. |
| Reject intra-region peering connection | [RejectVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2105) | Reject intra-region peering connection. |
| Enable expired intra-region peering connection | [EnableVpcPeeringConnection](https://cloud.tencent.com/doc/api/245/2102) | Enable expired intra-region peering connection. |
| Create cross-region peering connection | [CreateVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4803) | Create cross-region peering connection. |
| Delete cross-region peering connection | [DeleteVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4804) | Delete cross-region peering connection. |
| Modify cross-region peering connection attributes | [ModifyVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4805) | Modify cross-region peering connection attributes. |
| Accept cross-region peering connection | [AcceptVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4806) | Accept cross-region peering connection. |
| Reject cross-region peering connection | [RejectVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4807) | Reject cross-region peering connection. |
| Enable expired cross-region peering connection | [EnableVpcPeeringConnectionEx](https://cloud.tencent.com/doc/api/245/4808) | Enable expired cross-region peering connection. |
| Query peering connection | [DescribeVpcPeeringConnections](https://cloud.tencent.com/doc/api/245/2101) | Query peering connection. |

## 10. Direct Connect Gateway Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Create a Direct Connect gateway | [CreateDirectConnectGateway](https://cloud.tencent.com/doc/api/245/4824) | Create a Direct Connect gateway. |
| Modify Direct Connect gateway attributes | [ModifyDirectConnectGateway](https://cloud.tencent.com/doc/api/245/4826) | Modify Direct Connect gateway attributes. |
| Delete a Direct Connect gateway | [DeleteDirectConnectGateway](https://cloud.tencent.com/doc/api/245/4825) | Delete a Direct Connect gateway. |
| Query a Direct Connect gateway | [DescribeDirectConnectGateway](https://cloud.tencent.com/doc/api/245/4827) | Query a Direct Connect gateway. |
| Create local IP translation for Direct Connect gateway | [CreateLocalIPTranslationNatRule](https://cloud.tencent.com/doc/api/245/5185) | Create local IP translation for Direct Connect gateway. |
| Delete local IP translation for Direct Connect gateway | [DeleteLocalIPTranslationNatRule](https://cloud.tencent.com/doc/api/245/5186) | Delete local IP translation for Direct Connect gateway. |
| Modify local IP translation for Direct Connect gateway | [ModifyLocalIPTranslationNatRule](https://cloud.tencent.com/doc/api/245/5187) | Modify local IP translation for Direct Connect gateway. |
| Query local IP translation for Direct Connect gateway | [DescribeLocalIPTranslationNatRule](https://cloud.tencent.com/doc/api/245/5188) | Query local IP translation for Direct Connect gateway. |
| Create local source IP port translation for Direct Connect gateway | [CreateLocalSourceIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5190) | Create local source IP port translation for Direct Connect gateway. |
| Delete local source IP port translation for Direct Connect gateway | [DeleteLocalSourceIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5191) | Delete local source IP port translation for Direct Connect gateway. |
| Modify local source IP port translation for Direct Connect gateway | [ModifyLocalSourceIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5192) | Modify local source IP port translation for Direct Connect gateway. |
| Query local source IP port translation for Direct Connect gateway | [DescribeLocalSourceIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5193) | Query local source IP port translation for Direct Connect gateway. |
| Create local destination IP port translation for Direct Connect gateway | [CreateLocalDestinationIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5195) | Create local destination IP port translation for Direct Connect gateway. |
| Delete local destination IP port translation for Direct Connect gateway | [DeleteLocalDestinationIPPortTranslationNatRule](https://cloud.tencent.com/document/product/215/5196) | Delete local destination IP port translation for Direct Connect gateway. |
| Modify local destination IP port translation for Direct Connect gateway | [ModifyLocalDestinationIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5197) | Modify local destination IP port translation for Direct Connect gateway. |
| Query local destination IP port translation for Direct Connect gateway | [DescribeLocalDestinationIPPortTranslationNatRule](https://cloud.tencent.com/document/api/215/5198) | Query local destination IP port translation for Direct Connect gateway. |
| Create peer IP translation for Direct Connect gateway | [CreatePeerIPTranslationNatRule](https://cloud.tencent.com/document/api/215/5201) | Create peer IP translation for Direct Connect gateway. |
| Delete peer IP translation for Direct Connect gateway | [DeletePeerIPTranslationNatRule](https://cloud.tencent.com/document/api/215/5202) | Delete peer IP translation for Direct Connect gateway. |
| Modify peer IP translation for Direct Connect gateway | [ModifyPeerIPTranslationNatRule](https://cloud.tencent.com/document/api/215/5203) | Modify peer IP translation for Direct Connect gateway. |
| Query peer IP translation for Direct Connect gateway | [DescribePeerIPTranslationNatRule](https://cloud.tencent.com/document/api/215/5204) | Query peer IP translation for Direct Connect gateway. |
| Create a local IP translation ACL rule | [CreateLocalIPTranslationAclRule](https://cloud.tencent.com/doc/api/245/5205) | Create a local IP translation ACL rule. |
| Delete a local IP translation ACL rule | [DeleteLocalIPTranslationAclRule](https://cloud.tencent.com/doc/api/245/5206) | Delete a local IP translation ACL rule. |
| Modify a local IP translation ACL rule | [ModifyLocalIPTranslationAclRule](https://cloud.tencent.com/doc/api/245/5207) | Modify a local IP translation ACL rule. |
| Query a local IP translation ACL rule | [DescribeLocalIPTranslationAclRule](https://cloud.tencent.com/doc/api/245/5208) | Query a local IP translation ACL rule. |
| Create a local IP port translation ACL rule | [CreateLocalSourceIPPortTranslationAclRule](https://cloud.tencent.com/doc/api/245/5211) | Create a local IP port translation ACL rule. |
| Delete a local IP port translation ACL rule | [DeleteLocalSourceIPPortTranslationAclRule](https://cloud.tencent.com/doc/api/245/5212) | Delete a local IP port translation ACL rule. |
| Modify a local IP port translation ACL rule | [ModifyLocalSourceIPPortTranslationAclRule](https://cloud.tencent.com/doc/api/245/5213) | Modify a local IP port translation ACL rule. |
| Query a local IP port translation ACL rule | [DescribeLocalSourceIPPortTranslationAclRule](https://cloud.tencent.com/doc/api/245/5214) | Query a local IP port translation ACL rule. |

## 11. NAT Gateway Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Create a NAT gateway | [CreateNatGateway](https://cloud.tencent.com/doc/api/245/4094) | Create a NAT gateway. |
| Query NAT gateway creation progress | [QueryNatGatewayProductionStatus](https://cloud.tencent.com/doc/api/245/4089) |  Query the creation progress of a NAT gateway. |
| Delete a NAT gateway | [DeleteNatGateway](https://cloud.tencent.com/doc/api/245/4087) | Delete a NAT gateway. |
| Modify a NAT gateway | [ModifyNatGateway](https://cloud.tencent.com/doc/api/245/4086) | Modify a NAT gateway. |
| Query a NAT gateway | [DescribeNatGateway](https://cloud.tencent.com/doc/api/245/4088) |  Query a NAT gateway. |
| Bind an EIP for a NAT gateway | [EipBindNatGateway](https://cloud.tencent.com/doc/api/245/4093) | Bind an EIP for a NAT gateway. |
| Unbind an EIP for a NAT gateway | [EipUnBindNatGateway](https://cloud.tencent.com/doc/api/245/4092) | Unbind an EIP for a NAT gateway. |
| Upgrade NAT gateway specifications | [UpgradeNatGateway](https://cloud.tencent.com/doc/api/245/4090) | Upgrade the specifications of a NAT gateway |

## 12. ENI Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Create an ENI | [CreateNetworkInterface](https://cloud.tencent.com/doc/api/245/4811) | Create an ENI. |
| Delete an ENI | [DeleteNetworkInterface](https://cloud.tencent.com/doc/api/245/4813) | Delete an ENI. |
| Query ENI information | [DescribeNetworkInterfaces](https://cloud.tencent.com/doc/api/245/4814) | Query ENI information. |
| Apply for a private IP for an ENI | [AssignPrivateIpAddresses](https://cloud.tencent.com/doc/api/245/4817) | Apply for a private IP for an ENI. |
| Return a private IP of an ENI | [UnassignPrivateIpAddresses](https://cloud.tencent.com/doc/api/245/4819) | Return a private IP of an ENI. |
| Bind an ENI to a CVM | [AttachNetworkInterface](https://cloud.tencent.com/doc/api/245/4820) | Bind an ENI to a CVM. |
| Unbind an ENI from a CVM | [DetachNetworkInterface](https://cloud.tencent.com/document/product/215/4822) | Unbind an ENI from a CVM. |
| Migrate an ENI | [MigrateNetworkInterface](https://cloud.tencent.com/doc/api/245/5384) | Migrate an ENI. |
| Migrate a private IP | [MigratePrivateIpAddress](https://cloud.tencent.com/doc/api/245/5385) | Migrate a private IP. |

## 13. FlowLog Related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| Create a FlowLog | [CreateFlowLog](流日志相关接口/创建流日志.en) |  Create a FlowLog。 |
| Delete a FlowLog | [DeleteFlowLog](流日志相关接口/删除流日志.en) |  Delete a FlowLog。 |
| Query FlowLog information | [DescribeFlowLog](流日志相关接口/查询流日志信息.en) | Query FlowLog information。 |
| Query FlowLog list | [DescribeFlowLogs](流日志相关接口/查询流日志列表.en) | Query FlowLog list。 |
| Modify a FlowLog | [ModifyFlowLogAttribute](流日志相关接口/修改流日志属性.en) | Modify a FlowLog。 |
