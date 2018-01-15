## Introduction
Public network gateway is a CVM on which the forwarding feature is enabled. CVMs without public IPs can access the Internet through a public network gateway in a different subnet. The public network gateway host will carry out source address translation for public network traffic. The IP of traffic by all other hosts accessing the public network is translated to the IP address of public network gateway host after passing through the public network gateway, as shown below:
![](//mccdn.qcloud.com/static/img/a0453fe63b0a2b1100c339b877242387/image.png)



## Difference Between Public Network Gateways and CVMs with Public IPs
Public network gateways have had the public network traffic route forwarding function enabled in image, while CVMs with public IPs do not have traffic forwarding function by default. Windows public image CVMs cannot be used as public network gateways, because the traffic forwarding function is not enabled in Windows image.

## Usage Constraints
- Public network gateway currently supports a maximum egress bandwidth of 100 Mbps. If you need a larger egress bandwidth, you can purchase more public network gateways to form a public network egress cluster. With the same destination route configured in routing tables, the self-adaptive load balancing for forwarding traffic can be achieved between public network gateways. (Note: The cloud load balancer does not support health checks currently. Public network gateway failures may lead to loss of traffic).
- A gateway subnet and an ordinary subnet cannot be associated with the same routing table. A separate gateway routing table needs to be created to be associated with the gateway subnet.
- Public network gateways support NAT connections, and users need to log in to the CVM to configure this. Direct Connect gateways and VPN gateways do not support NAT connections currently.

## Billing
As a public network gateway is essentially a CVM instance, the billing method is the same as the CVM billing. For details, please refer to [here](https://cloud.tencent.com/doc/product/213/2179).

## Expiry Reminder
The expiry reminder mode is consistent with the CVM. For details, please refer to [here](https://cloud.tencent.com/doc/product/213/2181).

## Operating Instructions
If a CVM without a public IP in a VPC needs to access the public network through a public network gateway, the following steps should be completed:

a) Create a gateway subnet;
b) Purchase a public network gateway; 
c) Create a routing table of gateway subnet;
d) Configure the routing table of ordinary subnet;

### Creating a gateway subnet
The public network gateway can only forward the route forwarding request of the subnet to which it does not belong, so the public network gateway cannot be in the same subnet with the CVM which needs to access the public network through the public network gateway. Therefore, it is necessary to set up a separate gateway subnet first.

1)	Click "Subnet" in the left navigation bar of [VPC Console](https://console.cloud.tencent.com/vpc).
2)	Select a region and a VPC in the top drop-down boxes.
3)	Click "New", and fill in a subnet name (such as public network gateway subnet), CIDR, availability zone and associated routing table (A random routing table can be associated with at this time).
4)	Click "Create", and then the newly created subnet will display in the subnet list.

### Purchasing a public network gateway
Like the CVMs, public network gateways are also purchased in the [Tencent Cloud CVM Purchase Page](https://buy.cloud.tencent.com/cvm).

1) Log in to [Tencent Cloud CVM Purchase Page](https://buy.cloud.tencent.com/cvm), and select "VPC" in the Network Type on the "3. Select Storage and Network" page.
2) Select a VPC and the gateway subnet created in the previous step.
3) Check "Used as a public network gateway". The public network gateway is created upon the completion of the purchase.
 ![](https://mc.qcloudimg.com/static/img/2e85182a198309bcc3c13f6f3d16302c/vpc1.jpg)

### Creating a routing table of gateway subnet
A gateway subnet and an ordinary subnet cannot be associated with the same routing table. A separate gateway routing table needs to be created to be associated with the gateway subnet created in association with this routing table. The default Local policy can be retained as a routing policy. For related operations, refer to [Creating Custom Routing Table](https://cloud.tencent.com/document/product/215/4954) and [Modifying Routing Table Associated with a Subnet](https://cloud.tencent.com/document/product/215/4954).

### Configuring the routing table of ordinary subnet
Configure the routing table of the ordinary subnet, and direct the route to the public network gateway CVM, so that the CVM without a public IP in the ordinary subnet can access the public network through the route forwarding capability of public network gateway.

1)	Click the "Routing Table" in the left navigation bar of [VPC Console](https://console.cloud.tencent.com/vpc), and select the routing table associated with the ordinary subnet that needs to access the public network (users can find the routing table associated with the ordinary subnet in the [Subnet list page](https://console.cloud.tencent.com/vpc/subnet).
2)	Click the ID of the routing table associated with the ordinary subnet to enter the routing table details page.
3)	Click the "Edit" button and configure the default route to take the public network gateway CVM, so that the CVM in the ordinary subnet can access the public network through the route forwarding capability of public network gateway.
 ![](https://mc.qcloudimg.com/static/img/d70946d2101e9f38593f103193814450/vpc2.jpg)

## API Overview
The public network gateway is essentially a CVM instance. Users can view related APIs in [Overview of CVM APIs](https://cloud.tencent.com/doc/api/229/569), or use VPC, subnet, routing table and other APIs to complete the configuration of public network gateways. For more information, refer to [Overview of All VPC APIs](https://intl.cloud.tencent.com/document/product/215/909).

