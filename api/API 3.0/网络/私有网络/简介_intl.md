Thank you for using Tencent Cloud VPC.
VPC (Virtual Private Cloud) can help you build an independent network space at Tencent Cloud, which allows you to customize IP address ranges, IP address, routing policies, etc. You can also establish a VPN tunnel through Internet/Direct Connect to interconnect VPC with your other cloud resources and deploy hybrid cloud flexibly.
You can perform such operations as creating a VPC and creating a subnet with the APIs described in this document. For information on supported operations, please see <a href="https://cloud.tencent.com/doc/api/215/15755" title="API Overview">API Overview</a>.
Before using these APIs, please make sure that you have a thorough understanding of <a href="https://cloud.tencent.com/doc/product/215/535" title="API Product Description">VPC Product Description</a> and <a href="https://cloud.tencent.com/doc/product/215/1178" title="Operation Guide">Operation Guide</a>.

## Product Objects

| Product Object | Full Name | Description |
|---------|---------|---------|---------|
| VPC  | Virtual Private Cloud | VPC |
| subnet | Subnet |Subnet |
| routeTable | RouteTable |Route table |
| networkAcl | NetworkAcl |Network ACL |
| VPN | Virtual Private Network | IPsec VPN gateway |
| SSL VPN | SSL Virtual Private Network | SSL OPS Management VPN |
| vpcPeeringConnection | VpcPeeringConnection | Peering connection, i.e. traffic between VPCs. |
| directConnectGateway | DirectConnectGateway | Direct Connect gateway. This is used to establish a link between a VPC and your IDC based on interconnection among ISP Direct Connects to build hybrid cloud. |
| NATGateway | NatGateway | NAT gateway, through which a VPC accesses the Internet. |
| classicLink | ClassicLink | A link between a VPC and a basic network |
| networkInterface |NetworkInterface | ENI |


## Getting Started

Take the following steps to quickly create a VPC:

1. Create a VPC and its subnets
You can use the API [Create VPC](https://cloud.tencent.com/doc/api/215/15774) to create a VPC and its subnets. After creation, the system creates a default route table and directs the subnets to the default route table.

2. Purchase VPC servers
After the subnets are created, you can use the API [Create Instance](https://cloud.tencent.com/doc/api/213/15730) to purchase VPC CVMs. These CVMs may come with no public IPs, and we can use the public gateway as a unified egress.

3. (Optional) Purchase a NAT gateway
If the CVMs purchased come with no public IPs, you can use the API "Create NAT Gateway" to purchase a NAT gateway which can be used as an egress for external access by the CVMs in the VPC.

4. (Optional) Modify the route table
In the subnet that needs to access the Internet, you can modify the route table policy by using the API [Modify Route Table](https://cloud.tencent.com/doc/api/215/16724), and create a routing policy to direct the next hop of the destination IP address range that requires external access to the public gateway.

## Use Limits
For more information, please see <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC Use Limits">VPC Use Limits</a>. To request more resources, contact customer service. We will provide you with individualized configuration after an evaluation.

