## 1. Creating VPC and Initial Subnet
A VPC may contain multiple subnets. You need to create a VPC and subnets at the same time to add cloud service resources to the subnets of VPC.

You can create a VPC in the console, and need to create initial subnets at the same time, so as to add cloud service resources to the VPC.

Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar, select the region in which you want to create the VPC in the VPC console, and click "New" to create a VPC.
![](//mccdn.qcloud.com/img567f9faf86cdc.png)

To create a VPC, you need to specify the CIDR network segment of VPC and subnet, and determine the availability zone of the subnet. When creating VPC, you're recommended to reserve enough IP resources for VPC and subnets to avoid insufficient network resources caused by business expansion.

**About CIDR** 

CIDR achieves the division of network with independent network space address blocks specified by users using the combination of IPs and masks. Take "10.1.0.0/16" as an example. The string to the left of the slash is the IP of the network block, and the one to the right is the mask of network block. You can resize the network block by setting the mask. The IPs contained in the network block = 2 ^ (32-mask), so the "10.1.0.0/16" network block contains a maximum of 65,536 IP addresses.  

VPC masks ranging from /28 to/16 are supported. In other words, your VPC space contains a minimum of 16 and a maximum of 65,536 IP addresses. 

VPC supports private IPs within three network segments: "10.a.0.0/8" (a is between 0 and 255), "172.b.0.0/16" (b is between 16 and 31), and "192.168.0.0/16". CIDR of VPC can be the above three net work segments, or a part of a network segment. 

## 2. Adding Subnet
Subnet is a logical subdivision of VPC. You need to create VPC first, and then divide the VPC into subnets.

Log in to [CVM Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar, then select "Subnets" tab in the VPC console, and click "New" to create a subnet.

![](//mccdn.qcloud.com/img567fa0e851555.png)

- A VPC may contain multiple subnets. The network block of each subnet is a VPC subset, and CIDR network blocks cannot overlap between subnets.
- Subnet has the availability zone attribute. CVMs within the same subnet must belong to the availability zone of the subnet.
- Each subnet is associated with a routing table. You can specify the network routing for subnet by setting a routing table.
