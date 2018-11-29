## Application Scenarios
For the isolation deployment of multi-layer Web applications, the users not only want to ensure that the Web access layer can access the Internet and respond to massive requests, but also need to protect the security of database server through network isolation.
Then, you can create different subnets within a VPC and put the entire Web layer in a subnet. Moreover, you can communicate with the Internet through configuring elastic IP/gateway CVM/NAT gateway. By configuring the cloud load balance service, the access traffic will be automatically assigned to multiple Web access layer CVM. The logical layer is put in another subnet, only communicating with the Web layer and the data layer. The data layer is put in a third subnet, only communicating with the logical layer.
![](https://mc.qcloudimg.com/static/img/b127c404a42371721b7cc4c08b8ce7e0/image.png)

## Solutions:
**VPC**: CIDR(10.0.0.0/16), and create three subnets within the VPC.
**Web layer subnet**: CIDR(10.0.0.0/24), the CVM deployed Web layer application will be put separately in the subnet, which can communicate with the Internet in response to user's requests. At the same time, you can use cloud load balance service when faced with massive requests.
**Logical layer subnet**: CIDR(10.0.0.1/24), the CVM deployed the logical layer application will be put separately in the subnet to ensure that the logical layer application cannot be accessed via public network.
**Data layer subnet**: CIDR (10.0.0.2/24), a data subnet is assigned separately to ensure data security, in which the database products are deployed. This subnet only allows the traffic access of logical layer subnet.
**Network ACL**: control the traffic between subnets through network ACL, the rules are as follows:

- **Network ACL A**: bind logic layer subnet. The goal is to ensure that the logic layer application can be accessed via Web layer subnet and database layer subnet instead of public network.

Inbound rules:

| Protocol Type | Port | Source IP | Policy | Note |
|---------|---------|---------|---------|---------|
| All traffic | ALL | 10.0.0.0/24 | Allow | Allow Web layer access |

Outbound rules:

| Protocol Type | Port | Destination IP | Policy | Note |
|---------|---------|---------|---------|---------|
| All traffic | ALL | 10.0.0.0/24 | Allow | Allow response to Web layer access |
| All traffic | ALL | 10.0.0.2/24 | Allow | Allow database layer subnet access |


- **Network ACL B**: bind database layer subnet. The goal is to ensure that the database layer subnet can only be accessed via logical layer subnet.

Inbound rules:

| Protocol Type | Port | Source IP | Policy | Note |
|---------|---------|---------|---------|---------|
| All traffic | ALL | 10.0.0.1/24 | Allow | Allow logical layer subnet access |
Outbound rules:

| Protocol Type | Port | Destination IP | Policy | Note |
|---------|---------|---------|---------|---------|
| All traffic | ALL | 10.0.0.1/24 | Allow | Allow to return the request from logical layer |


## Steps
To deploy multi-layer Web applications, you need to complete the following steps:
Step 1: Create a private network. [Click here to view details](https://cloud.tencent.com/document/product/215/4927#.E5.88.9B.E5.BB.BA.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E3.80.81.E5.88.9D.E5.A7.8B.E5.8C.96.E5.AD.90.E7.BD.91.E5.92.8C.E8.B7.AF.E7.94.B1.E8.A1.A8).
Step 2: Create a Web layer subnet, [add CVM](https://cloud.tencent.com/document/product/215/4927#.E5.90.91.E5.AD.90.E7.BD.91.E4.B8.AD.E6.B7.BB.E5.8A.A0.E4.BA.91.E4.B8.BB.E6.9C.BA), and deploy the cloud load balance service. For details, please check [Cloud Load Balance Instance](https://cloud.tencent.com/document/product/214/6574#.E8.B4.AD.E4.B9.B0.E5.B9.B6.E5.88.9B.E5.BB.BA.E8.B4.9F.E8.BD.BD.E5.9D.87.E8.A1.A1.E5.AE.9E.E4.BE.8B).
Step 3: Create a logical layer subnet, and [add CVM](https://cloud.tencent.com/document/product/215/4927#.E5.90.91.E5.AD.90.E7.BD.91.E4.B8.AD.E6.B7.BB.E5.8A.A0.E4.BA.91.E4.B8.BB.E6.9C.BA).
Step 4: Create a data layer subnet, add a cloud database. Click here to view [Purchase Cloud Database](https://cloud.tencent.com/document/product/236/3128).
Step 5: Configure the network ACLs for the three subnets. The rules are shown in the table above. [Click here to view details](https://cloud.tencent.com/document/product/215/8119).

