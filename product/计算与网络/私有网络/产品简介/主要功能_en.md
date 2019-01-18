
The Virtual Private Cloud is a customizable logically isolated network space. In a VPC, you can customize network segmentation, IP address and routing policy, and deploy [Cloud Virtual Machine](https://cloud.tencent.com/doc/product/213/495), [Cloud Load Balance](https://cloud.tencent.com/doc/product/214/524), [Cloud Database](https://cloud.tencent.com/doc/product/236) and other cloud service resources. The VPC on Tencent Cloud provides easy access to the Internet and a variety of connection methods to connect to your data center, allowing you to quickly deploy the hybrid cloud. Also, Tencent Cloud VPC [Peering Connection](https://cloud.tencent.com/doc/product/215/5000) and [Classiclink](https://cloud.tencent.com/doc/product/215/5002) can enable you to easily connect private network resources, helping you achieve "one server covering the globe" and disaster recovery at "two regions, three centers". In addition, the [Network ACL](https://cloud.tencent.com/doc/product/215/5132) and [Security Group](https://cloud.tencent.com/document/product/213/5221) on Tencent Cloud VPC help you ensure the network security in a multi-dimensional and all-round manner.
![](https://mc.qcloudimg.com/static/img/fd060d334b0fa4c2f27b0804782946e8/image.png)
## Customizing the Network
You can customize VPC network segment, subnet network segment, and routing policy through the console or API. You can also further divide your network into multiple subnets and deploy applications and services across subnets. In addition, you can flexibly manage the network forwarding traffic of resources in VPC, public network, and hybrid cloud by setting a reasonable routing policy.

## Flexible and High-performance Internet Access
Tencent Cloud VPC provides you with flexible and high-performance Internet connection methods, including elastic IP, NAT gateway and public network gateway.

| Function | Description |
|---------|---------|
| [**Elastic IP (EIP)**](https://cloud.tencent.com/document/product/213/5733) | Elastic IP (EIP) is a public IP address that can be applied for independently. It supports dynamic binding and unbinding to instances (such as CVMs and NAT gateways). Typical application scenarios include:<br>**`Retaining an IP`**. Domain licensing is required between domestic IPs and DNS.<br>** `Shielding off instance failures`**. For example, a DNS name is mapped to an IP address through the dynamic DNS mapping. It may take up to 24 hours to propagate this mapping to the entire Internet, while elastic IP enables the drift of an IP from one CVM to another. In case of a CVM failure, all you need to do is start another instance and remap it, thus shielding off the instance failure. |
| **[NAT Gateway](https://cloud.tencent.com/doc/product/215/4975)** | NAT gateway is a way for VPC to access the Internet, which is able to translate private and public IP addresses within a VPC when the private and public networks are isolated. Typical application scenarios include:   <br>**`Public network access with large bandwidth and high availability`.**  NAT gateway supports a maximum of 10,000,000 concurrent connections, 5Gbps bandwidth and 10 elastic IPs, and provides master/slave hot backup, automatic disaster recovery, and 99.99% service availability. It applies to public network access application scenarios that need large bandwidth, massive use of public network IPs, and a large number of services to be deployed.<br>**   `Secure public network access`**The NAT gateway of Tencent Cloud VPC provides secure IP translation. If you want to hide the public IP of the CVM in the VPC to avoid exposing its network deployment while still being able to access the public network, you can use Tencent Cloud NAT gateway. | 
| **[Public Network Gateway](https://cloud.tencent.com/doc/product/215/4972)** | Public network gateway is a type of CVM which is able to forward the traffic between the Internet and VPCs. A CVM without a public IP can access the Internet via public network gateway. |


## Stable and Reliable User Data Center Connection
If you want to build your enterprise's hybrid cloud deployment, namely, to connect your cloud computing resources and local data centers, you can use public network VPN/Direct Connect.
- **[VPN Connection](https://cloud.tencent.com/doc/product/215/4956)** is a method to connect your IDC and Tencent Cloud VPC through public network encrypted tunnels. You can create VPN gateways of your VPC, peer gateways for your IDC and VPN tunnels supporting IPsec encryption protocols on the console to realize the secure communication between VPC and your local data center, thus completing the hybrid cloud deployment quickly.
- **[Direct Connect](https://cloud.tencent.com/doc/product/215/4976)** is a service used to connect your data center and Tencent Cloud computing resources located in multiple regions through physical Direct Connect, which can help you build a flexible and reliable hybrid cloud network connection. Direct Connect supports master/slave hot backup, SLA service assurance and interconnection across regions at home and abroad, which can fully meet high-quality network interconnection requirements of fields such as finance.

## Flexible Resource Interconnection on Tencent Cloud
The interconnection between resources in a VPC and other cloud resources can be achieved through peering connection and Classiclink.
- **[Peering Connection](https://intl.cloud.tencent.com/document/product/215/5000)** is a service that connects two VPCs and makes them combined into one VPC in a sense. It can help you achieve "one server covering the globe" and disaster recovery deployment at "two regions, three centers" easily.
- **[Classiclink](https://cloud.tencent.com/doc/product/215/5002)** is a service that associates CVMs in the basic network with specified VPCs to allow them to communicate with each other, thus achieving the smooth connection of private network resources.

## Multi-dimensional and Comprehensive Security Protection
The resource access control for port and instance dimensions can be achieved through network ACLs and security groups, which can help you improve the security of CVMs.
- **[Access Control List (ACL)](https://cloud.tencent.com/doc/product/215/5132)** is a stateless optional layer of security at the subnet level which can be used as a firewall to control the traffic in and out of subnets (accuracy up to protocol and port dimensions).
- **[Security Group](https://cloud.tencent.com/document/product/213/5221)** is an instance-level virtual firewall with packet filtering function, which is used to set network access control for one or more instances. You can add CVM instances with the same network security isolation requirements in the same region to the same security group, to securely filter the outbound and inbound traffic of the CVM through the network policy.








