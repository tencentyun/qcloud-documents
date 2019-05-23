## Application Scenarios
Users worry that the security of data cannot be guaranteed if the resources pool on the public cloud is shared by multiple tenants. They want to have a completely isolated network environment to deploy the cloud resources on the public cloud.
**User's core pain point**:
Users want to be completely isolated from other tenants, avoiding the risk of multi-tenant sharing.

## Solutions:
Tencent Cloud Virtual Private Cloud (VPC) is a customized network space on Tencent Cloud that is logically isolated, which is similar to the traditional network you run in the data center. The service resources hosted in Tencent Cloud VPC include Cloud Virtual Machine, Cloud Load Balance, Cloud Database and other resources of Cloud Services in your Tencent Cloud. You can fully control your VPC environment, including customizing network segmentation, IP address and routing policy, and achieve multi-layer security protections through network ACL and security group and so on. At the same time, you can also use IPsec VPN/Direct Connect to connect the VPC with your data center, and deploy hybrid cloud flexibly.

The network types of Tencent Cloud are classified as VPC and basic network:
- The **basic network** is the resource pool of public network for all users on Tencent Cloud (as shown in the left figure). All private IPs of Cloud Virtual Machine are assigned by Tencent Cloud. It is easy to configure and convenient to use, suitable for scenarios that have high usability requirements and need to get started with the CVM quickly.
- **Virtual Private Cloud** refers to a logically isolated network space built by user on Tencent Cloud (as shown in the right figure). In the VPC, users can customize network segmentation, IP address and routing policy, and deploy services such as CVM and database. Compared with the basic network, VPC is more suitable for the scenarios that have network custom configuration requirements.
![](https://mc.qcloudimg.com/static/img/906834bedb9d197b3b033f30c562fa79/VPC-Overview.png)
    　　　　　    　　　　　  Figure 1:  Comparison of basic network and VPC

## Steps
1) Create a VPC, and initialize the subnet and routing table
2) Create a subnet
3) Create a new subnet associated with routing table
4) Add CVM and database to the subnet
[Click here to view details](https://cloud.tencent.com/document/product/215/8119)

