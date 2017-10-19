The CVM instance described below also refers to dedicated CVM.

Tencent Cloud provides two types of network environments: basic network and Virtual Private Cloud (VPC).

All of the user's cloud resources are managed centrally by Tencent Cloud over basic network, which features an ease of use and configuration to help users manage CVMs quickly and easily. All basic network instances in the same region under an account can communicate with each other via [private network service](/doc/product/213/5225). Basic network is able to meet the needs of most users, and is the most straightforward way to get started with Tencent Cloud.

With Tencent Cloud VPC, you can customize a logically isolated virtual network within the cloud and put cloud service resources (such as instances) into the isolated zone. Even in the same region, different VPCs cannot communicate with each other by default. VPC is very similar to traditional networks run by IDCs, except that its infrastructure can be scaled up quickly on the cloud. You can customize network topology and private IPs, and configure [Routing Table](https://cloud.tencent.com/doc/product/215/4954), gateway and security settings; connect VPC to your local IDC via [Direct connect](https://cloud.tencent.com/doc/product/215/4976) to scale up computing resources quickly; and plan on how the VPC communicates with Internet. A variety of control methods (including [Security Group](/doc/product/213/5221) and [Network ACL](https://cloud.tencent.com/doc/product/215/5132)) can be used to protect VPC resources. For more information, please see [VPC product documentation](https://cloud.tencent.com/doc/product/215). VPC allows users to build complex network architecture and is suitable for users who are familiar with network management.

## Basic Network and VPC
![](//mccdn.qcloud.com/static/img/f1c113751199560fb87bc002b4bf0207/image.png)


The differences between VPC and basic network are shown below:

| Feature    | VPC                                     | Basic Network                         |
| ----- | ---------------------------------------- | ---------------------------- |
| Tenant association | Logically isolated network based on GRE encapsulation                           | Tenants are associated with each other                         |
| Customized network | Support                                       | Not supported                          |
| Customized routing | Support                                       | Not supported                          |
| Customized IP | Support                                       | Not supported                          |
| Interconnection rule  | Cross-region and cross-account interconnection is supported                             | Interconnection is only allowed for the same tenant in the same region                     |
| Security control  | [Security Group](/doc/product/213/5221) and [Network ACL](https://cloud.tencent.com/doc/product/215/5132) | [Security Group](/doc/product/213/5221) |

## How You Benefit from VPC

By putting instances into VPC, you can:

- Assign **customized** static private IP that is kept unchanged to an instance.
- Assign multiple IPs to an instance (available soon).
- Control inbound and outbound traffic for an instance.
- Add an extra access control layer to an instance using network Access Control List (ACL).

## Resource Sharing and Access Between Basic Network and VPC

Some of the cloud resources and features on Tencent Cloud support both basic network and VPC, and can be shared or accessed between the two different networks.

| Resource                              | Description                                       |
| ------------------------------- | ---------------------------------------- |
| [Image](/doc/product/213/4940)     | You can use image to start a CVM instance in any network environment                    |
| [Elastic IP](/doc/product/213/5733)  | EIP can be bound to any CVM instance in any network environment                 |
| Instance                              | Instances in basic network and those in VPC communicate with each other via [Internet IP](/doc/product/213/5224) or [Classiclink](https://cloud.tencent.com/doc/product/215/5002).
| [SSH Key](/doc/product/213/6092) | SSH key can be loaded to a CVM instance in any network environment                |
| [Security Group](/doc/product/213/5221)    | Security Group can be bound to a CVM instance in any network environment                    |

> Note: [Load Balancer](https://cloud.tencent.com/doc/product/214) cannot be shared between basic network and VPC. This means that a Load Balancer cannot be bound to both VPC instance and basic network instance, even if a connection has been set up between the instances via Classiclink.

## Migrate Instances from Basic Network to VPC
1) [Create a custom image](/doc/product/213/4942) for the CVM instance in basic network.
2) (Optional) [Create a snapshot](/doc/product/362/5755) for the CVM instance data disk in basic network.
3) [Create a VPC and subnet](https://cloud.tencent.com/doc/product/215/4927#.E5.88.9B.E5.BB.BA.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E3.80.81.E5.88.9D.E5.A7.8B.E5.8C.96.E5.AD.90.E7.BD.91.E5.92.8C.E8.B7.AF.E7.94.B1.E8.A1.A8).
4) [Purchase and start the CVM Instance](/doc/product/213/4855) in the VPC.
