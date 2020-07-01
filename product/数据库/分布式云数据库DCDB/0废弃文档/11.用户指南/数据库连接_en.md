## 1. Connection Address
CDB for TDSQL provides private network access address, which is in fact the access gateway cluster address of CDB for TDSQL, rather than the node address from a database node group.
Access gateway cluster is completely transparent to users, and all SQLs are forwarded to the database node group by access gateway cluster. You can check the private network address from the Instance List page or Instance Details page in the management console, as shown below:
![](//mccdn.qcloud.com/img568a2d51e4f1e.png)
Only CVMs within Tencent Cloud private network can access private network addresses. VPC support is required to access from public network.

## 2. Network Type
CDB for TDSQL supports two network environment types: basic network and VPC.
-     Basic network: Cloud services in the basic network are not isolated from each other. You can only use the security groups or whitelists of cloud services to prevent unauthorized access.
-     VPC: Virtual Private Cloud is a network space which can be customized by the user. You can deploy cloud service resources such as CVMs, load balancers, databases and NoSQL fast storage across different availability zones inside the VPC. You can allocate IP address ranges, create routing strategies and specify IPs for cloud resources in the VPC at your own will. You can configure public network gateway for your VPC to access the Internet. You can also configure public network or direct connection to establish hybrid cloud. Different networks in VPC are logically isolated from each other. 
