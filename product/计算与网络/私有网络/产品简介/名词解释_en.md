## VPC and Subnet

### Region
A [region](https://cloud.tencent.com/doc/product/215/4927#.E5.9C.B0.E5.9F.9F.EF.BC.88region.EF.BC.89) refers to a geographical location where Tencent Cloud data center is hosted. There are multiple availability zones in a region. For example, the region of a hosted data center is Beijing, and its availability zone is Beijing Zone 1. The cloud service products in the same region can communicate with each other through private network, but those in different regions cannot. Thus, it is recommended to choose the region that is closest to your customers to minimize the access latency and improve download speed. Click here to view the region selection guide.

### Zone
A [zone](https://cloud.tencent.com/doc/product/215/4927#.E5.8F.AF.E7.94.A8.E5.8C.BA.EF.BC.88zone.EF.BC.89) refer to a physical area (generally a physical data center) with an independent power supply and network in a single region (like Guangzhou), such as Guangzhou Zone 1. In this way, failure isolation can be achieved between different zones (except for large-scale disaster failure). For example, if you have deployed the same service in Zone 1 and Zone 2, the power failure in Zone 1 will not affect Zone 2, thus providing you with stable and highly available services. Click here to view the region selection guide.

### Virtual Private Cloud
Tencent Cloud Virtual Private Cloud can help you build an independent network space on Tencent Cloud, similar to the traditional network you run in the data center. The service resources hosted in Tencent Cloud VPC include: [Cloud Virtual Machine](https://cloud.tencent.com/doc/product/213/495), [Cloud Load Balance](https://cloud.tencent.com/doc/product/214/524), [Cloud Database](https://cloud.tencent.com/document/product/236) and other resources of Cloud Services on your Tencent Cloud. You don't need to consider the purchase and O&M of network devices, but focus on the customization of network segmentation, IP address, routing policy, etc. using software. You can access the Internet easily via [Elastic IP](https://cloud.tencent.com/doc/product/213/1941), [NAT Gateway](https://cloud.tencent.com/doc/product/215/4975) and [Public Network Gateway](https://cloud.tencent.com/doc/product/215/4972), and connect VPC with your data centers via [VPN](https://cloud.tencent.com/doc/product/215/4956)[/Direct Connect](https://cloud.tencent.com/doc/product/215/4976). Also, Tencent Cloud VPC [Peering Connection](https://cloud.tencent.com/doc/product/215/5000) can help you achieve "one server covering the globe" and disaster recovery at "two regions, three centers". In addition, the [Security Group](https://cloud.tencent.com/doc/product/213/500) and [Network ACL](https://cloud.tencent.com/doc/product/215/5132) on Tencent Cloud VPC can satisfy your network security requirement in a multi-dimensional and all-round manner.

### Basic Network
The basic network is the resource pool of public network for all users on Tencent Cloud. The private IP addresses of CVM in the resource pool are assigned by Tencent Cloud. It is easy to configure and convenient to use, suitable for scenarios that have high usability requirements and need to get started with the CVM quickly. By contrast, the VPC is more suitable for customers with network management capabilities and demands. [Click here to view the difference between VPC and basic network](https://cloud.tencent.com/document/product/215/535#choose-vpc-or-basic-network.3F3).

### Subnet
A [subnet](https://cloud.tencent.com/doc/product/215/4927) is a flexible division of VPC network segments that allows you to deploy applications and services across different subnets and host multi-layer Web applications safely and flexibly on Tencent Cloud VPC.

### CIDR
CIDR achieves the overall division of network with independent network space address blocks specified by you using the combination of IPs and masks. Take "10.1.0.0/16" as an example. The string to the left of the slash is the IP of the network block, and the string to the right is the mask of network block. You can resize the network block by setting the length of mask. The IPs contained in the network block = 2 ^ (32-mask length), so the "10.1.0.0/16" network block contains a maximum of 65,536 IP addresses. [Click here to view CIDR details](https://cloud.tencent.com/doc/product/215/4927#cidr).

### Private IP
A private IP is an IP address assigned to an instance in Tencent Cloud VPC or basic network, which cannot be accessed via the Internet. But you can use it for communication between instances in VPC or basic network.

### Public IP
A public IP address can be accessed via the Internet and you can use it for communication between your instances and the Internet or between other Tencent Cloud resources (such as CDBs) with common terminal nodes.

## Routing
### 	Routing Table
A [routing table](https://cloud.tencent.com/doc/product/215/4954) consists of a series of routing policies, which are used to define the traffic direction of each subnet within the VPC. A subnet can be associated with only one routing table, but a routing table can be associated with multiple subnets in the same VPC.

### 	Routing Policies
[Routing policies](https://cloud.tencent.com/doc/product/215/V1.0%E8%B7%AF%E7%94%B1%E8%A1%A8?viewType=preview#5.-.E8.B7.AF.E7.94.B1.E8.A7.84.E5.88.99) are used to specify the routing of network traffic, each of which contains three parameters:
- **Destination**: The description of destination network segments. The destination cannot be the IP segment of the VPC in which the routing table locates;
- **Next hop type**: The next hop type for VPC supports "public network gateway", "VPN gateway", "Direct Connect gateway" etc. You need to create such a gateway, otherwise you cannot pull the next hop type;
- **Next hop**: Specify the next hop gateway to which the subnet traffic associated with the routing table is directed.
   Click here to view routing policy setting details.

## Internet Access
### 	Elastic IP
A [elastic IP](https://cloud.tencent.com/doc/product/213/1941) is a public IP address that can be applied for independently. It supports dynamic binding and unbinding. You can bind or unbind it to the CVM (or NAT gateway instance) in the account to:
- **Retain an IP**. Domain name licensing is required between domestic IPs and DNS.
- **Shield off instance failures**. For example, a DNS name is mapped to an IP address through the dynamic DNS mapping. It may take up to 24 hours to propagate this mapping to the entire Internet, while elastic IP enables the drift of an IP from one CVM to another. In case of a CVM failure, all you need to do is start another instance and remap it, thus responding rapidly to the instance failure.


###  	Public Network Gateway
A [public network gateway](https://cloud.tencent.com/doc/product/215/4972) is a type of CVM which is able to forward the traffic between the Internet and VPCs. A CVM without a public IP can access the Internet via public network gateway.

### 	NAT (Network Address Translation) Gateway
[NAT gateway](https://cloud.tencent.com/doc/product/215/4975) can translate private and public IP addresses within a VPC when the private and public networks are isolated, allowing VPC to access the Internet. NAT gateway supports a maximum of 5Gbps traffic surge and 10,000,000 concurrent connections. As a highly available gateway, NAT gateway also provides master/slave hot backup, by which the failed one will be automatically switched to the slave without affecting your use of services.


## Connecting Your Data Centers
### 	User IDC
User Internet Data Center (IDC) is a full set of IT infrastructure deployed outside Tencent Cloud.
### IPsec 
IPsec is a protocol suite that secures Internet Protocol (IP) communication by authenticating and encrypting each IP packet of traffic.
### IPsec VPN
[IPsec VPN](https://cloud.tencent.com/doc/product/215/4956) is a method to connect your IDC and VPC through public network encrypted tunnel. Tencent Cloud VPC IPsec VPN connection consists of the following components:
- **VPN gateway**: An IPsec VPN gateway in the VPC, which can be used with peer gateway (your IPsec VPN service gateway for IDC). VPN gateway is mainly used to establish a secure and reliable encrypted network communication between VPC and your IDC.
- **Peer gateway**: An IPsec VPN service gateway of your IDC data center that mapped in VPC, which needs to be used with VPN gateway. A VPN gateway can establish encrypted VPN network tunnels with multiple peer gateways.
- **VPN tunnel**: An encrypted public network IPsec VPN tunnel. After the VPN gateway and the peer gateway are established, the VPN tunnel used for encrypted communication between VPC and your IDC can be established.


### 	Direct Connect
[Direct Connect](https://cloud.tencent.com/doc/product/215/4976) provides a fast approach to connect Tencent Cloud with local data centers. You can have access to Tencent Cloud computing resources in multiple regions in one go using a physical direct connection line, to achieve a flexible and reliable hybrid cloud deployment. Direct Connect supports the connection method of dual-line hot backup without SPOF to meet high network interconnection requirements of fields such as finance. It consists of three components: 
- **Physical Direct Connect**: The physical line to connect Tencent Cloud with local data centers. A physical line can be used to establish Direct Connect tunnel with Direct Connect gateways in multiple regions.
- **Direct Connect tunnel**: The network link segmentation of the physical Direct Connect. You can create the Direct Connect tunnels connected to different Direct Connect gateways to achieve the interconnection between local data centers and multiple VPCs.
- **Direct Connect gateway**: The Direct Connect traffic entry for VPC, by which you can connect multiple Direct Connect tunnels with different local data centers.


## Resource Interconnection on Tencent Cloud
### Peering Connection 
[Peering connection](https://cloud.tencent.com/doc/product/215/5000) is the connection established by different VPCs that can be used to connect the traffic between VPCs of different accounts or regions. You can use it to connect the IP traffic between VPCs that establish peering connections, after which the resources (such as CVMs and cloud databases) from the two ends will be able to access each other.

### Classiclink
[Classiclink](https://cloud.tencent.com/doc/product/215/5002) refers to the interconnection of cloud services between Tencent Cloud VPC and basic network. The basic network Cloud Virtual Machine (CVM) interconnected with VPC can actively access such computing resources as CVM, Cloud Database within VPC via private network. The CVM in the VPC can also actively access the basic network CVM via private network.

## Security
### 	Network ACL
[Access Control List (ACL)](https://cloud.tencent.com/doc/product/215/5132) is a stateless optional layer of security at the subnet level which can be used as a firewall to control the traffic in and out of subnets (accuracy up to protocol and port dimensions). In addition, the network ACL can restrict the network traffic and improve the network performance.

### 	Security Group
[Security group](https://cloud.tencent.com/doc/product/213/500) a virtual firewall with stateful packet filtering feature, which is used to set network access control for one or more CVM(s). You can add CVM instances with the same network security isolation requirements in the same region to the same security group, to securely filter the inbound and outbound traffic of the CVM through the network policies of the security group.





