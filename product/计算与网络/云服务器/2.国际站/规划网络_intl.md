Tencent Cloud Virtual Private Cloud (VPC) is a user-defined logically isolated network space on the Tencent Cloud, in which users can customize IP address range, IP address and routing policies. Therefore, you are recommended to use VPC.

To help you use Tencent Cloud VPC, Tencent Cloud provides the following suggestions on network planning:

### Determining the Number of VPCs
- Existing features:
	
	- VPC is region related. By default, cloud service products in different regions cannot communicate with each other over private network. For cross-region communication, you need to establish a [Peering Connection](https://cloud.tencent.com/document/product/215/5000).
	- By default, VPCs in the same region cannot communicate with each other over private network. For cross-VPC communication, you need to establish a [Peering Connection](https://cloud.tencent.com/document/product/215/5000).
	- By default, availability zones in the same VPC are interconnected with each other via private network.


- Suggestions:

	- If you need to deploy the system in multiple regions for your business, multiple VPCs are required. You can build a VPC close to the region of your customers to reduce access latency and improve access speed.

	- If you have deployed multiple businesses in the current region, and want to achieve network isolation among different businesses, you can build a VPC for each of your businesses in the current region.
	- If you have no requirement for multi-region deployment and network isolation among businesses, you can use only one VPC.

### Determining Subnet Division
- Existing features:
	- Subnet is an IP address block within a VPC, and all cloud resources in a VPC must be deployed in subnets.
	- In the same VPC, subnet IP address ranges must not overlap.
	- Tencent Cloud VPC supports private IPs within three IP address ranges: "10.a.0.0/8" (a is between 0 and 255), "172.b.0.0/16" (b is between 16 and 31), and "192.168.0.0/16".
	- When a VPC has been created, the IP address range cannot be modified.
- Suggestions:
	- If only VPC subnet division is required, and communication between VPC and basic network/IDC is not involved, you can choose one of the above IP address ranges to create a new subnet.
	- If VPC needs to communication with basic network, establish a VPC with the IP address range of 10.[0~47].0.0/16 and its subsets as required.
	- If VPN needs to be established, local IP address range (VPC's IP address range) and peer IP address range (your IDC IP address range) cannot overlap. Therefore, avoid using peer IP address range when you create a subnet.
	- During subnet division, the number of available IPs in the IP address range should also be taken into account.
	- Finally, it is recommended that subnets can be divided according to the service modules within the same VPC business. For example, subnet A is used for WEB layer, subnet B is used for logic layer, and subnet C is used for DB layer. This helps facilitate access control and filtering using network ACL.

### Determining Route Policies

- Existing features:
	A routing table consists of a series of routing policies that are used to control the outbound traffic direction of subnets within the VPC.
	- Each subnet must be associated with one routing table only.
	- Each routing table can be associated to multiple subnets.
	- When a VPC is created, the system automatically generates a default routing table, which indicates that VPCs are interconnected with each other via private network.
- Suggestions:
	- If you do not need to control the traffic direction of subnets, and VPCs are interconnected with each other via private network by default, you can directly use the default routing table without the need to configure a custom routing policy.
	- If you need to control the traffic direction of subnets, please see the detailed description of [Routing Table](https://cloud.tencent.com/document/product/215/4954) on the official website.


For more information on VPC, please see [VPC](https://cloud.tencent.com/document/product/215).




