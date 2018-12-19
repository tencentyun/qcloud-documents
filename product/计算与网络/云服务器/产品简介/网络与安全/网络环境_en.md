Tencent Cloud network environment can be divided into either basic network and private network (VPC).

Through the Tencent Cloud basic network, all of the user's resources on the cloud are managed uniformly by Tencent Cloud; relatively speaking, these configurations are simpler and more convenient to use, helping users manage their CVMs faster and easier. All basic network instances in the same geographical area are free to communicate via [Private Network Service](/doc/product/213/5225) under the user account. Most of the user's needs can be met through the basic network and implementation; this is best and most convenient if you are just beginning to understand and use Tencent Cloud.

With the Tencent Cloud Private Network (VPC), you can customize a logical isolated virtual network within the cloud and launch a CVM resource (such as an instance) into the quarantine. Even in the same area, different VPCs cannot communicate with each other by default. VPC is very similar to traditional networks that data centers run, but at the same time, can offer you faster and more extensible infrastructures on the cloud. Users can customize network topology and IP addresses within the network and configure the [Router Table](https://cloud.tencent.com/doc/product/215/4954), gateway and security settings; supports [Dedicated Connection](https://cloud.tencent.com/doc/product/215/4976) through your local data center, and rapid expansion of computing resources; freely plan how your VPC communicates with the Internet. Use a variety of control methods (including [Security Group](/doc/product/213/5221) and [Network ACL](https://cloud.tencent.com/doc/product/215/5132) to protect VPC resources. For more information, see [Private Network Product Documentation](https://cloud.tencent.com/doc/product/215). Private networks can help users build more complex network architectures, suitable for users who are familiar with network management.

## Basic network and private network
![](//mccdn.qcloud.com/static/img/f1c113751199560fb87bc002b4bf0207/image.png)

						
The functional differences between the private network and the basic network are shown in the table below:

| Function | Private Network | Basic Network |
|---------|---------|---------|
| Renter Association | Logical Isolated Network Based on GRE Encapsulation | Renter Association |
| Network customization | Yes | No |
| Router customization | Yes | No |
| Custom IP | Yes | No |
| Intercommunication Rules | Supports cross-domain, cross-account intercommunication | Interoperable among renters in the same geographical area |
| Security control | [Security group](/doc/product/213/5221) and [Network ACL](https://cloud.tencent.com/doc/product/215/5132) | [Security group](/doc/product/213/5221) |

## Advantages of VPC

By starting the instance within the VPC, you can:

- Assign an instance of **your custom** private static IP.
- Assign multiple IP addresses to your instance (coming soon).
- Controls inbound and outbound traffic for an instance.
- Add an additional access control layer to the instance using the Network Access Control List (ACL).

## Share and access resources between basic network and VPC

Some of the resources and functions on Tencent Cloud can support two kinds of network environments, and can be shared or accessed between different networks.

| Resources | Instructions |
|--|--|
| [Image](/doc/product/213/4940) | can be used to start a CVM instance in any network environment |
| [Elastic IP](/doc/product/213/5733) | Elastic IPs can be bound to any network environment on a CVM instance |
| Instances | Instances on a basic network and instances within the private network can be accessed through [Public IP](/doc/product/213/5224) or [Basic Network Interoperability](https://cloud.tencent.com/doc/product/215/5002) functions to achieve intercommunication |
| [SSH Key](/doc/product/213/6092) | SSH key supports loading a CVM instance under any network environment | 
| [Security Group](/doc/product/213/5221) | Security Groups support binding to CVM instances in any network environment |

> Note: [Cloud Load Balance](https://cloud.tencent.com/doc/product/214) cannot be shared between the underlying network and the VPC. That is, Cloud Load Balance does not support binding basic network instances and VPCs at the same time; even though the VPC and the basic network are connected through the basic network and can intercommunicate.

## Migrate instances within the basic network to VPC
1) [Create a Custom Image](/doc/product/213/4942) for the CVM instance in the basic network environment.
2) (Optional) [Create a Snapshot](/doc/product/362/5755) of the CVM instance data disk in the basic network environment.
3) [Create a VPC and Subnet](https://cloud.tencent.com/doc/product/215/4927#.E5.88.9B.E5.BB.BA.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E3.80.81.E5.88.9D.E5.A7.8B.E5.8C.96.E5.AD.90.E7.BD.91.E5.92.8C.E8.B7.AF.E7.94.B1.E8.A1.A8).
4) [Purchase and Start the CVM Instance](/doc/product/213/4855) in the VPC.
