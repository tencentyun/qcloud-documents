## Introduction
NAT Gateway is a gateway with the ability to translate private and public IP addresses within a VPC, providing a way for cloud resources that exist in a VPC without a public IP to access the Internet (active access from the Internet to a VPC not supported). Typical application scenarios of Tencent Cloud's VPC include:
- **Public network access with large bandwidth and high availability.** Tencent Cloud's NAT gateway can easily accommodate the demand for public network access that requires large bandwidth, massive use of public IPs, and a high number of services to be deployed.
- **Secure public network access.** The NAT gateway of Tencent Cloud VPC provides secure IP translation. If you want to hide the public IP of the CVM in the VPC to avoid exposing its network deployment while still being able to access the public network, you can use Tencent Cloud NAT gateway.

## Network Topology
As shown below, NAT gateway is a gateway that resides on the boundary between the Internet and the VPC, and connects to the router on the VPC. In a topology like this, when resources like CVM within the VPC send outgoing data packets via the NAT gateway, the data will firstly move through the router and make routing selection based on the route rules. After that, the NAT gateway will use the bound elastic IP address as the source IP address to send the traffic to the Internet:
![](//mccdn.qcloud.com/static/img/4772b9bc1e78436104f89f943f06ac97/image.png)

## The Difference between NAT Gateway and Public Network Gateway
Both NAT gateway and public network gateway are used for the CVM in the VPC to access the Internet, but there exist some differences between the two:

| Attribute | NAT Gateway | Public Network Gateway |
|---------|---------|---------|
|Availability	| Master/slave hot backup, automatic hot switching |	Switch the failed gateway manually |
| Public network bandwidth	| Maximum is 5Gbps	| Depend on the network bandwidth of CVM |
| Public IP	| Bind a maximum of 10 EIPs |	An EIP or an ordinary public IP |
| Rate limit of public network	| N/A |	Depend on the rate limit of CVM |
| Maximum number of connections	| 10,000,000 |	500,000
| Private IP	| Private IP of VPC user is not occupied |	Occupy the subnet private IP |
| Security group |	Binding of security group is not supported. You can bind the security group to the NAT gateway backend CVM	| Support |
| Network ACL |	Binding of network ACL is not supported. You can bind the network ACL to the subnet where the NAT gateway backend CVM resides in	| Binding of network ACL is not supported. You can bind the network ACL to the subnet to which the public network gateway belongs |
| Charges	| Mainland China:<br>Small-sized (a maximum of 1,000,000 connections): RMB 0.5/hour<br>Medium-sized (a maximum of 3,000,000 connections): RMB 1.5/hour<br>Large-sized (a maximum of 10,000,000 connections): RMB 5/hour | Depend on the size of CVM used as a public network gateway. Take Mainland China as an example:<br>1-core 2GB: RMB 0.44/hour<br>4-core 8GB: RMB 1.76/hour<br>12-core 24GB: RMB 5.28/hour

The comparisons listed above show that Tencent Cloud's NAT gateway has three advantages:
- Large capacity: supports a maximum of 10,000,000 concurrent connections, 5Gbps bandwidth and 10 elastic IPs to meet the demand of users with a large business scale.
- Highly available master/slave hot backup: automatic switch to the slave when one server suffers a failure, providing automatic disaster recovery, and 99.99% service availability, superior to the manual switch mode of a public network gateway.
- Cost effectiveness: three configuration types, high, medium and low, are available for users to choose from as needed, offering flexibility in billing and high cost effectiveness.

## Configuration types
NAT gateway supports binding up to 10 elastic IPs, and a maximum of 5Gbps traffic surge and 10,000,000 concurrent connections.

- Small (max. 1,000,000 connections)
- Medium (max. 3,000,000 connections) 
- Large (max. 10,000,000 connections)

Available values for maximum public network outbound bandwidth of NAT gateway (unit: Mbps) include 10, 20, 50, 100, 200, 500, 1000, 2000, and 5000.

## How to Use NAT Gateway and Elastic Public IP

NAT gateway and elastic public IP are the two ways for the CVM to access the Internet. You can use either one of them or both of them to design your public network access architecture.

### Method 1: Use NAT gateway only
The CVM is not bound to an elastic public IP; all traffic from accessing the Internet is forwarded through the NAT gateway. With this method, the traffic from the CVM accessing the Internet will be forwarded to the NAT gateway through the private network. That means this traffic will not be subject to the public bandwidth limit specified when the CVM was purchased, nor will the traffic generated at the NAT gateway occupy the public bandwidth egress of the CVM.

### Method 2: Use elastic public IP only
The CVM is only bound to an elastic public IP, and the NAT gateway will not be used. With this method, all traffic from the CVM accessing the Internet will go out from the elastic public IP. That means this traffic will not be subject to the public bandwidth limit specified when the CVM was purchased. The cost resulting from accessing the public network will be charged based on the network billing mode of the CVM.

### Method 3: Use both the NAT gateway and the elastic public IP
The CVM is bound to an elastic public IP; meanwhile all traffic from the subnet route accessing the Internet is directed to the NAT gateway. With this method, all traffic from the CVM actively accessing the Internet **can only be forwarded to the NAT gateway through the private network**, and the returning packets will be returned to the CVM through the NAT gateway as well. This traffic will not be subject to the public bandwidth limit specified when the CVM was purchased, nor will the traffic generated at the NAT gateway occupy the public bandwidth egress of the CVM. If the traffic from the Internet actively accesses the elastic public IP of the CVM, the returning packets of the CVM will be uniformly returned through the elastic public IP. This way, the resulting outbound traffic of the public network will be subject to the public bandwidth limit specified when the CVM was purchased. The cost resulting from accessing the public network will be charged based on the network billing mode of the CVM.

> Note: For users with a Bandwidth Package for bandwidth sharing, the outbound traffic generated at the NAT gateway will be billed as per the Bandwidth Package (the RMB 0.8/GB network traffic fee will not be charged separately). It's recommended that you set a limit on the outbound bandwidth of the NAT gateway, so as to avoid any high Bandwidth Package charge due to excessively high amount of such bandwidth.


## Key Features
The following are some key features of NAT gateway:
- SNAT: source network address translation for cloud service resources within the VPC to access the Internet.
- High performance: NAT gateway supports forwarding up to 5Gbps of data to a single instance;
- High availability: NAT gateway provides master/slave hot backup, by which the failed one will be automatically switched to the slave without affecting your use of services.

## Usage Constraints
The following should be noted about the usage of the NAT gateway:
- Deleting the NAT gateway will disassociate its elastic IP address, but will not release this address from the user account.
- Although the NAT gateway cannot be associated with security groups, security groups can be used for the instances within the private subnet in order to control the traffic that goes in and out of these instances.
- You cannot use the network ACL to control the traffic that goes in and out of the NAT gateway, but you can use it to control the traffic of the associated subnet that goes in and out of the NAT gateway.
- You cannot use VPC Peering Connection, VPN Connection or Direct Connect to route the traffic to the NAT gateway. The NAT gateway cannot be used for these resources that are connected to the other end. For example, the moving of all the traffic from VPC 1 to the Internet can be enabled by the NAT gateway. Now, as a peering connection has been established between VPC 1 and VPC 2, all the resources within VPC 2 can access all the resources within VPC 1, but no resources within VPC 2 can access the Internet through the NAT gateway.
- Supported protocols for the NAT gateway include TCP, UDP and ICMP, while ESP and AH for the GRE tunnel and IPSec cannot be used for the NAT gateway. This is a result of the characteristics of the NAT gateway itself, and has nothing to do with the service provider. Luckily, TCP is a dominant type of application in the Internet world, and, together with UDP, accounting for 99% of all Internet applications.
- For the restrictions on the supported resources for the NAT gateway, refer to [Usage Constraints of Other VPC Products](https://www.qcloud.com/doc/product/215/537).

| Resources | Limit | 
|---------|---------|
| Number of NAT gateways per VPC | 3 | 
| Number of elastic IPs per NAT gateway | 10 |
| Maximum forwarding capacity per NAT gateway | 5Gbps |

## Billing Method
Charges for a NAT gateway device include two parts: Gateway rental fee (by hour) and the fee for traffic generated during the access to the Internet. The cost for the traffic can be charged as per the "Bill by Traffic" method for CVM network charges. The billing mode for the NAT gateway itself is as follows:

| Type | Mainland China | Hong Kong |Singapore| North America |
|---------|---------|---------|---------|
| Small | RMB 0.5/h | RMB 0.75/h | RMB 0.75/h | RMB 0.8/h |
| Medium | RMB 1.5/h| RMB 2.25/h | RMB 2.25/h | RMB 2.4/h |
| Large | RMB 5/h | RMB 7.5/h | RMB 7.5/h | RMB 8/h |

 >Note:
 For users with a Bandwidth Package for bandwidth sharing, the outbound traffic generated at the NAT gateway will be billed as per the Bandwidth Package (the RMB 0.8/GB network traffic fee will not be charged separately). It's recommended that you set a limit on the outbound bandwidth of the NAT gateway, so as to avoid any high Bandwidth Package charge due to excessively high amount of such bandwidth. Click to view the [Bandwidth Package billing details](https://www.qcloud.com/doc/product/213/%E8%B4%AD%E4%B9%B0%E7%BD%91%E7%BB%9C%E5%B8%A6%E5%AE%BD#.E5.B8.A6.E5.AE.BD.E5.8C.85.E8.AE.A1.E8.B4.B9)
 - Arrear logic: be consistent with the Bill by Traffic method for CVM. [Click to obtain the VPC Price Overview](https://www.qcloud.com/doc/product/215/3079)
 - As the NAT gateway features master/slave hot backup, the system will send a 5KB check packet to the master and slave servers of the NAT gateway every three seconds. This will result in a traffic of 0.2747GB each day, incurring a daily charge of RMB 0.2197, RMB 0.2747 and RMB　0.1373 for Mainland China, Hong Kong and North America, respectively.


## Expiry Reminder
- When you have insufficient balance in your account: Starting from the moment your account balance becomes 0, you can use the NAT gateway for a further period of **2** hours with the usage being further billed.
- If your account balance is still not topped up to greater than 0 after those two hours, the NAT gateway service will be automatically suspended and the billing stopped.
- The NAT gateway will remain unavailable until your account balance is topped up to an amount greater than 0 within 24 hours after the suspense of the service. When your account balance has been topped up to an amount greater than 0, the gateway will become available and the billing will start over again.
- When your account balance has remained below 0 for 24 hours after the suspense of NAT gateway service, the NAT gateway will be reclaimed immediately.
- The Tencent Cloud account creator and all the collaborators will be notified of the reclaim via email and SMS.

## Operation Instructions
If you want to allow the resources within the subnet of a VPC to access the Internet through a NAT gateway, you need not only to create the NAT gateway, but also to configure the routing rules in the routing table with which the subnet that needs route forwarding is associated.

### Quick Start
You need to complete the following two steps to allow accessing the Internet through a NAT gateway:
#### Step 1: Create a NAT gateway
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/), select "Virtual Private Cloud" tab, and select "NAT Gateway".
2) Click the "New" button at the upper left corner, and enter or specify the following parameters in the pop-up box:
- Gateway name
- Gateway type (It can be changed after creation)
- VPC of NAT gateway services
- Assign an elastic IP to NAT gateway. You can choose the existing elastic IP, or purchase another elastic IP and assign it

3) After selection, click "OK" to complete the creation of NAT gateway.
After the creation of a NAT gateway, you need to configure the routing rules in the Routing Tables page in the Virtual Private Cloud console to direct the subnet traffic to the NAT gateway.
> Note: The rental fee will be frozen for 1 hour during the creation of NAT Gateway.

#### Step 2: Configure the routing table associated with the subnet
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.qcloud.com/vpc/vpc?rid=8). Select "Routing Tables".
2) In the routing table list, click the routing table ID with which the subnet that needs to access the Internet is associated to enter its details page, and click "Edit" button in the "Routing Rules".
3) Click "New line", fill in the "Destination" field, select "NAT Gateway" in "Next hop type", and select the created NAT gateway ID
4) Click "OK". After the above configuration is made, the traffic generated when the CVM in the subnet associated with the routing table accesses the Internet will be directed to the NAT gateway.

### Modify NAT gateway configuration
After the creation of a NAT gateway, you can modify its attributes.
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.qcloud.com/vpc/vpc?rid=8). Select "NAT Gateway".
2) In the NAT gateway list page, click the NAT gateway ID to be modified to enter its details page, where you can make modifications to the following attributes:
- Change the custom name of NAT gateway
- Change the NAT gateway specifications. Specification changes take effect immediately (the network connection will not be broken)

### Manage the elastic IPs bound to the NAT gateway
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.qcloud.com/vpc/vpc?rid=8), and select "NAT Gateway".
2) In the NAT gateway list page, click the NAT gateway ID to enter its details page.
3) In the associated elastic IP list, you can select "Add" to add an elastic IP, or "Unbind" to unbind an elastic IP.

### View NAT gateway monitoring information
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.qcloud.com/vpc/vpc?rid=8), and select "NAT Gateway".
2) In the NAT gateway list page, click the "Monitor" button in a NAT gateway entry to view its monitoring information.
(Alternatively) In the NAT gateway list page, click the ID of a NAT gateway to enter its details page, and then click "Monitoring" tab to view its monitoring information.

### Setting the Alarm
1)	Log in to [Tencent Cloud Console](https://console.qcloud.com/), click "Cloud Products" - "Monitor & Management" - ["Cloud Monitoring"](https://console.qcloud .com/monitor/overview) in the top navigation bar, and then select "My Alarms" - ["Alarm Policy"](https://console.qcloud.com/monitor/policylist) in the left navigation bar, and click Add Alarm Policy.
2) Fill in the Alarm Policy Name, select "NAT Gateway" in Policy Type, and then add the Condition of alarm trigger.
3)	**Associate alarm objects**: select the alarm receiver group. You can view the set alarm policy in the policy list after you click "Complete".
4)	**View the alarm information**: when the alarm is triggered, you will receive SMS/email/internal message or other notices, and you can also find the information in the left navigation "My Alarms" - "Alarm List". For more information about alarms, refer to [Creating Alarms](https://www.qcloud.com/doc/product/248/1073).

### Delete NAT gateway
NAT Gateway can be deleted when it is not needed. The routing table and routing rules containing the NAT gateway will be deleted with the NAT gateway. Upon the deletion, the request forwarded over Internet will be interrupted immediately. Please provide for the network interruption in advance.
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.qcloud.com/vpc/vpc?rid=8), and select "NAT Gateway".
2) Select the NAT gateway to be deleted, click "Delete" button. After you confirm the deletion action, the NAT gateway will be deleted.

## API Overview
You can use API operations to set and manage your NAT gateway. For more information about other resources in a VPC, please refer to [Overview of All VPC APIs](https://www.qcloud.com/doc/api/245/909).

| Function | Action ID |  Description |
|---------|---------|---------|
| Create NAT Gateway | [CreateNatGateway](https://www.qcloud.com/doc/api/245/4094 | Create a NAT gateway.  |
| Query NAT gateway creation progress | [QueryNatGatewayProductionStatus](https://www.qcloud.com/doc/api/245/4089) |  Query the creation progress of a NAT gateway.  |
| Delete NAT gateway | [DeleteNatGateway](https://www.qcloud.com/doc/api/245/4087) | Delete a NAT gateway.  |
| Modify NAT gateway | [ModifyNatGateway](https://www.qcloud.com/doc/api/245/4086) | Modify a NAT gateway.  |
| Query NAT gateway | [DescribeNatGateway](https://www.qcloud.com/doc/api/245/4088) |  Query a NAT gateway.  |
| Create NAT Gateway | [CreateNatGateway](https://www.qcloud.com/doc/api/245/4094 | Create a NAT gateway.  |
| Unbind EIP for NAT gateway | [EipUnBindNatGateway](https://www.qcloud.com/doc/api/245/4092) | Unbind an EIP for a NAT gateway  |
| Upgrade NAT gateway specifications | [CreateNatGateway](https://www.qcloud.com/doc/api/245/4090 | Upgrade the specifications of a NAT gateway  |



