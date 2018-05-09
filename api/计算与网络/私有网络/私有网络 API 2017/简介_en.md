VPC (Virtual Private Cloud) can help you build an independent network space at Tencent Cloud which allows you to customize network segmentation, IP address, routing policy, etc. You can also establish a VPN tunnel through public network/Direct Connect to achieve the interconnection between private network and your other cloud resources and deploy hybrid cloud flexibly. 
Users can perform such operations as creating VPC and creating subnet with the APIs described in this document. For information on supported operations, please refer to <a href="https://cloud.tencent.com/doc/api/245/909" title="API Overview">API Overview</a>. 
Before using these APIs, please make sure that you have a thorough understanding of <a href="https://cloud.tencent.com/doc/product/215/535" title="VPC Product Overview">VPC Product Overview</a> and <a href="https://cloud.tencent.com/doc/product/215/1178" title="Operation Instruction">Operation Instruction</a>. 

## 1. Product Objects
| Product Object | Full Name  | Description |
|---------|---------|---------|---------|
| VPC  | Virtual Private Cloud | Virtual Private Cloud |
| subnet | Subnet | Subnet |
| routeTable | RouteTable | Routing table |
| networkAcl | NetworkAcl | Network ACL |
| VPN | Virtual Private Network | IPsec VPN gateway |
| SSL VPN | SSL Virtual Private Network | SSL O&M Management VPN |
| vpcPeeringConnection | VpcPeeringConnection | Peering connection, i.e. traffic between VPCs.  |
| directConnectGateway | DirectConnectGateway | Direct Connect gateway. This used to establish a link between VPC and user's IDC based on interconnection among ISP private lines to build hybrid cloud.  |
| NATGateway | NatGateway | NAT gateway, through which VPC accesses the Internet.  |
| classicLink | ClassicLink | Link between VPC and basic network |
| networkInterface | NetworkInterface | Elastic network interface |

## 2. Service Limits
For details, refer to <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Service Limits">VPC Service Limits</a>. If you need more resources, you can contact customer service personnel. We will provide you with individualized configuration after an evaluation.
