BM NAT gateway is a high-performance gateway with the capability to translate between private IPs and public IPs in the VPC. It is an ingress/egress for public network traffic in the VPC. The NAT gateway is used in the following typical scenarios:
- Secure public network access: The NAT gateway provides secure IP translation. It is used to translate private IP to public IP in the CPM of your VPC to achieve communication between CPM and public network via the public IP.
- Public network access with large bandwidth and high availability: It applies to public network access application scenarios that need large bandwidth, high availability, and a large number of services to be deployed.

## Network Topology
The network topology of BM NAT gateway in the VPC is shown in the figure below:
![](https://mc.qcloudimg.com/static/img/9081d69c42e37dc141ac816b79b23ea5/image.png)

## Configuration Types
BM NAT gateway can be bound with 4 EIPs with each supporting up to 3 Gbps traffic, and provides three types of configurations, allowing a maximum of 12 Gbps traffic surge and 10m concurrent connections.
- Small (max. 1m connections)
- Medium (max. 3m connections)
- Large (max. 10m connections)

## Forwarding Method
The default forwarding method of BM NAT gateway is IP forwarding. To support a large number of virtual instances in Docker/KVM to access the public network through the NAT gateway and provide IP address range forwarding, the difference between the two forwarding methods is shown as follows:

| IP | <a align="center">IP Address Range</a> |
|---------|---------|
| 1,024 CPM/VM IPs in use can be bound to NAT gateways | 1,024 IP address ranges with mask of 24 can be bound to NAT gateways. The subnet with mask less than 24 (Note 1) is split by 24 (Note 2). A maximum of 260,000 IPs is supported. |
| No limit is set on the mask in the subnet CIDR which is added to the NAT gateway. | The mask in the subnet CIDR which is added to the NAT gateway must fall in the range of 16 to 24. |
| All/Part of the IPs in the subnet can be added to the NAT gateway. | All IPs must be added to the NAT gateway. |

> Note 1:
> Classless Inter-Domain Routing (CIDR) is a user-specified independent network space address block, which enables the overall division of the network by combining IP with mask. Take "10.1.0.0/16" as an example. The string to the left of the slash is the IP of the network block, and the string to the right is the mask of network block. You can resize the network block by setting the mask. The IPs contained in the network block = 2^(32-mask), so the "10.1.0.0/16" network block contains a maximum of 65,536 IP addresses.

> Note 2:
Splitting mode of IP address range: The mask in the subnet CIDR which is added to the NAT gateway must fall in the range of 16 to 24. The subnet CIDR with mask being 23 is split into 2 IP address ranges with mask being 24. The subnet CIDR with mask being 22 is split into 4 IP address ranges with mask being 24. Number of IP address ranges split = 2^(24- mask). A maximum of 1,024 IP address ranges with mask being 24 is supported for each NAT gateway.


## Key Features
The followings are the key features of BM NAT gateway:
- SNAT: Source network address translation. It allows multiple CPMs in a single VPC to actively access the Internet through the same public IP.
- High performance: NAT gateway supports forwarding up to 12 Gbps of data to a single instance.
- High availability: Cluster mode is used, where automatic switch is supported when a single server suffers a failure without affecting your use of services.
- Monitoring information display: The key metrics for the NAT gateway are displayed. The monitoring details data can be kept for 7 days.

## Service Limits
The use of BM NAT gateway is limited as follows:
- If the subnet in which the CPM under the VPC resides has been added to the NAT gateway, you can bind an EIP to this CPM. If the EIP is successfully bound, the CPM can communicates with the public network via the EIP. If you unbind the EIP from the CPM, this CPM is automatically added to the NAT gateway. 
- When the CPM is bound with an EIP, if you use part of the IPs in the subnet to add this CPM to the NAT gateway, the operation may fail.
- A subnet can be added to only one NAT gateway.
- Deleting the NAT gateway will disassociate its EIP, but will not release this EIP from the user account.
- You can choose to allow all the subnets to access the public network through NAT gateway. However, if new subnets need to access the public network through NAT gateway, they must be associated.
- You cannot use VPC peering connection to route traffic to the NAT gateway. For example, the moving of all the traffic from VPC 1 to the Internet can be enabled by the NAT gateway. Now, as a peering connection has been established between VPC 1 and VPC 2, all the resources within VPC 2 can access all the resources within VPC 1, but no resources within VPC 2 can access the Internet through the NAT gateway.
-  NAT gateway resources are limited as follows:

| Resources | Limit |
|---------|---------|
| Maximum number of NAT gateways per VPC | 10 |
| Maximum number of EIPs per NAT gateway | 4 |
| Maximum forwarding capacity per NAT gateway | 12 Gbps |
| Maximum number of IPs per NAT gateway (IP forwarding)	| 1,024 |
| Maximum number of IPs per NAT gateway (IP address range forwarding)	| 260,000 (1024*256) |

## Difference Between BM NAT gateway and BM EIP
NAT gateway and EIP are both ways for the CPM to access the Internet. You can use either one of them or both of them.

**Solution 1: Use NAT Gateway Only**
CPM is not bound with an EIP, and all the traffic for accessing the Internet is forwarded via the NAT gateway. With this solution, all the traffic of the CPM accessing the Internet is forwarded to the NAT gateway via the private network.

**Solution 2: Use EIP only**
CPM is only bound with EIP, instead of using NAT gateway. With this solution, all the traffic of the CPM accessing the Internet flows via the EIP.

**Solution 3: Use Both NAT Gateway and EIP**
CPM is bound with an EIP, and the traffic of its subnet accessing the Internet is directed to the NAT gateway. With this solution, the CPM communicates with the public network via the EIP.

