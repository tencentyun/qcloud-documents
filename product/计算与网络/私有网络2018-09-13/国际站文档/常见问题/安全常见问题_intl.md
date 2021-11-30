## 1. How to ensure the security of CVMs running in a VPC?
A VPC is a network environment that is logically isolated, and security groups and network ACLs can be used for traffic control:
- **Security groups** can be used to specify the inbound and outbound network traffic that is allowed to enter or exit each CVM. Traffic which is not explicitly allowed to or from an instance is automatically denied.
- **Access Control List (ACL)** can also allow or deny the network traffic entering or exiting each subnet.

## 2. What are the differences between security groups and network ACLs in VPCs?
[Click to view the differences between security groups and network ACLs](https://cloud.tencent.com/doc/product/215/5132#.E5.AE.89.E5.85.A8.E7.BB.84.E4.B8.8E.E7.BD.91.E7.BB.9Cacl.E7.9A.84.E5.8C.BA.E5.88.AB).
