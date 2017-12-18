## 1. What does VPC (Virtual Private Cloud) consist of?
Tencent Cloud VPC consists of various services which should appear very similar to customers who own a VPC:
**1)  Software Defined Network**: You can customize your VPC network segment, subnet segment and routing policy:
- **Virtual Private Cloud (VPC)** is a logically separated virtual network in Tencent Cloud. Define the IP space of the VPC from selected range.
- **Subnet** is a segment within the IP range of the VPC, where you can place groups of isolated resources.
- ** Router** consists of a series of routing policies, which are used to define the traffic direction of each subnet within the VPC.


**2)  Internet Connection**: There are three types of flexible, high-performance Internet connection methods:
- **NAT Gateway** is a highly available Network Address Translation (NAT) service, which helps resources in private subnets access the Internet.
- **Elastic IP** (EIP) is an independent public IP address you can apply for, which is used for public network access. You can dynamically bind/unbind this IP to or from instances (such as CVMs and NAT gateways) and use it to avoid instance failures.
- **Public Network Gateway** is a type of CVM which is able to forward the traffic between Internet and VPCs. A CVM can access the Internet via public network gateway if it needs to do so, but does not have a public IP.

**3)  Deploy Hybrid Cloud** Connect your data center and your VPC.
- **VPN Connection** is a method you can use to connect your IDC and VPC through public network encrypted tunnel. It consists of three components: VPN gateway, peering gateway and VPN tunnel.
- **Direct Connection** provides a fast approach to connect Tencent Cloud with local data centers. You can simply use one physical direct connection line to access Tencent Cloud computing resources in multiple regions in one go. It consists of three components: physical direct connection, direct connection tunnel and direct connection gateway:

**4) Resource Interconnection between Clouds** is used to communicate with resources from other VPCs and basic networks.
- **Peering Connection**: This service is used to connect two VPCs. You can use it to connect the traffic between two VPCs of different accounts or regions, after which the resources (such as CVMs and cloud databases) from the two ends will be able to access each other
- **Basic Network Interconnection**: This service is used to associate CVMs in the basic network with specified VPCs, thus allowing the CVMs and VPCs in the basic network to communicate with each other

**5)  Security Control**
- **Security Group**: is a stateful packet filtering virtual firewall, which is used to control the outbound/inbound traffic of a single or multiple CVMs (accuracy up to protocol and port dimensions).
- **Network Access Control List (ACL)** is an optional stateless packet filtering virtual firewall (of subnet level), which is used to control the inbound/outbound data traffic that goes through the subnet (accuracy up to protocol and port dimensions).



## 2. How to start using VPC?
You can start using VPC either from the Tencent Cloud Console, or by using cloud APIs.
- [**Console** Quick Guide](https://cloud.tencent.com/document/product/215/8119)
- [**API** Quick Guide](https://cloud.tencent.com/doc/api/245/5157)

## 3. Is the VPC able to communicate with basic network/public network/other VPCs (of different accounts and regions)/my data center?
Yes. The following table lists your demands and their corresponding features:

| User Demand | Corresponding VPC Feature | 
|---------|---------|
| Communication between VPC and CVM within the basic network |  [Basic Network Interconnection](https://cloud.tencent.com/doc/product/215/5002)|
| Access public network | Elastic IP / NAT Gateway](https://cloud.tencent.com/doc/product/215/4975)(High performance)/ Public Network Gateway |
| Other VPCs | [Peering Connection](https://cloud.tencent.com/doc/product/215/5000)(Cross-region and cross-account are supported) |
| My data center | [VPN Connection ](https://cloud.tencent.com/doc/product/215/4956)/ Direct Connect |


## 4. How many VPCs, subnets, routing tables, public network gateways, NAT gateways, peering connections, VPN gateways, VPN tunnels, network ACLs can I create, respectively?
[View Detailed Resource Quota in the VPC](https://cloud.tencent.com/doc/product/215/537), please submit a ticket to apply for a higher quota if needed.

## 5. What's the difference between basic network and VPC?
VPC is able to achieve all functions that can be provided by the basic network, without additional fee.
VPC is able to satisfy more demands for network customization. [Please Refer to Details about Differences between Basic Network and VPC](https://cloud.tencent.com/doc/product/215/535#.E9.80.89.E6.8B.A9.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C-or-.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C.EF.BC.9F).


## 6. I have a VPC. How do I configure it to allow only some of the CVMs in it to access the public network through the gateway?
Place the CVMs that need to access the public network into a certain subnet, then configure routing policy on the routing table which is bound to this subnet and direct data packets to access via the gateway if their destination is the public network. Detailed procedure is shown below:
1) **[Create Subnet](https://cloud.tencent.com/doc/product/215/4927#.E6.96.B0.E5.A2.9E.E5.AD.90.E7.BD.91)** and place the CVMs that need to access the public network into this subnet: purchase CVMs from the [Subnet Console](https://console.cloud.tencent.com/vpc/subnet) / choose this subnet from the Purchased Network Configuration section of the [CVM Introduction Page](https://cloud.tencent.com/product/cvm.html).
2) **Purchase the corresponding gateway equipment**. There are two types of gateway equipments in Tencent Cloud VPC that can access the public network: [NAT Gateway](https://cloud.tencent.com/doc/product/215/4975) and [Public Network Gateway](https://cloud.tencent.com/doc/product/215/4972). [Click to View Their Differences](https://cloud.tencent.com/doc/product/215/4975#nat.E7.BD.91.E5.85.B3.E5.92.8C.E5.85.AC.E7.BD.91.E7.BD.91.E5.85.B3.E7.9A.84.E5.8C.BA.E5.88.AB). You may purchase the corresponding gateway equipment according to your business needs. Instruction on how to allow [CVMs without Public IPs to Access the Public Network via Public Network Gateway](https://cloud.tencent.com/doc/product/215/4972#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97) / instruction on how to [Use NAT Gateway to Access the Internet](https://cloud.tencent.com/doc/product/215/4975#.E4.BD.BF.E7.94.A8-nat-.E7.BD.91.E5.85.B3.E8.AE.BF.E9.97.AE-internet).

## 7. I have a VPC, can I create CVMs in different availability zones and how do I do that? Such as creating CVMs in both Guangzhou Zone 2 and Guangzhou Zone 3.
Yes. There are two preconditions:
1) You can only create CVMs within availability zones of the region to which the VPC belongs. For example, if your CVM belongs to the region Guangzhou, you can create CVMs in Guangzhou Zone 2 and Zone 3, but you cannot create CVMs in Guangzhou Zone 2 and Beijing Zone 1 at the same time, in this VPC. [Click to View Detailed Distribution of Regions and Availability Zones](https://cloud.tencent.com/doc/product/215/4927#.E5.8F.AF.E7.94.A8.E5.8C.BA.EF.BC.88zone.EF.BC.89)
2) You must create a subnet in the availability zone before you can create CVMs in this availability zone.

The detailed procedure regarding how to create CVMs in different availability zones is shown below:
1) [Create Subnets](https://cloud.tencent.com/doc/product/215/4927#.E6.96.B0.E5.A2.9E.E5.AD.90.E7.BD.91) in **different** availability zones under this VPC.
2) Create CVM. Purchase CVMs from the [Subnet Console](https://console.cloud.tencent.com/vpc/subnet) / choose subnets of **different availability zones** from the Purchased Network Configuration section of the [CVM Introduction Page](https://cloud.tencent.com/product/cvm.html).

## 8. Can I modify the private IP of cloud virtual machine (CVM)/private cloud load balancer (LB)/cloud database (CDB)?
You can modify the primary private IP of the CVM's primary NIC. You cannot modify the primary private IP of secondary NIC. [Click to View Instructions](https://cloud.tencent.com/doc/product/215/6508#4.-.E5.A6.82.E4.BD.95.E4.BF.AE.E6.94.B9.E4.BA.91.E4.B8.BB.E6.9C.BA.E5.86.85.E7.BD.91ip.EF.BC.9F).
You cannot modify private IP of private cloud load balancer (LB) or cloud database (CDB).
