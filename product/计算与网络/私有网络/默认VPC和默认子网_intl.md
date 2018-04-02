### Overview

Default VPC and default subnet features are under **beta** test. The network attribute of only some of the accounts registered after June 13, 2017 is only-vpc, and that of the rest is classic.
- The **only-vpc** accounts only support the creation of instances under VPC (such as CVM, LB), but not in [Basic Network](https://cloud.tencent.com/document/product/215/535).
- The **classic** accounts support the creation of instances in either basic network or VPC.


### Default VPC and Default Subnet
The only-vpc accounts support **default VPC** and **default subnet** features, and can create default VPC and default subnet in each region. The basic network is no longer supported in **regions launched after August 3, 2017 ** for all users, and default VPC and default subnet can be created in these new regions.
The advantages of default VPC and default subnet features are:

- You can produce a CVM and other instances without a VPC or subnet, and the system can create a default VPC and subnet, with no need to know the details of VPC and subnet features.
- You do not need to specify a VPC or subnet when you create a CVM or other instances, and the system can create an instance in the default VPC and default subnet.

### Basic Information of Default VPC

1) You can use the default VPC in the same way as you use any other non-default VPC, and can also add subnets, modify routing tables, add VPN connections, etc.
2) You can create additional VPCs. The default VPC is not counted into the VPC quota in a specific region.
3) The default VPC and the default subnet can be used in the same way as with any other VPC or subnet with no difference in functionality.
4) The default VPC and default subnet can be deleted


### Launching Instance (CVM/CDB) within Default VPC

#### 1. Without **Default VPC**
If your account does not have a default VPC in a region, when you produce an instance in the purchase page for a product like CVM, the VPC is specified as: Default-VPC (default), and the subnet is specified as: Default-Subnet (default).
1) The system creates a default VPC with /16 in the region you selected, a default subnet with /20 in the availability zone you selected, and a default routing table under this VPC.
2) Bind the default subnet to the default routing table.
3) Produce instances in the default subnet.
 
#### 2. With Default VPC but Without Default Subnet
If your account has a default VPC but not a default subnet in a region, when you produce an instance in the purchase page for a product like CVM, the subnet is specified as: Default-Subnet (default).
1) The system creates a default subnet with /20 in the available zone you selected.
2) Bind the default subnet to the default routing table under this VPC.
3) Produce instances in the default subnet.

#### 3. With Both Default VPC and Default Subnet
If your account has a default VPC and a default subnet in a region, you can select a default VPC and a default subnet as you would select a non-default VPC and subnet.






