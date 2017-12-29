Security group serves as a stateful virtual firewall with filtering function for setting network access control for one or more cloud databases. It is an important network security isolation tool provided by Tencent Cloud. A security group is a logical group. You can associate the **VPC-based cloud database** instances with the same network security isolation requirements in the same region with the same security group. Basic network-based cloud databases are not supported now. The cloud databases share the security group list with the CVMs. Matching is performed based on the rules in the security group and the rules not supported by the cloud databases become invalid automatically.
>**Note:**
Now, cloud database security group only supports the network control of private network access and public network access in VPC, and does not support the network control of basic network. At present, only CDB for MySQL supports security group.

## Security Group Policy
Security group policies are divided into "allowing" and "denying" traffic. You can use the security group policies to filter the inbound traffic of an instance, which can be **a private network-based cloud database** instance.

## Security Group Template
You can create a custom security group, or create a security group from template. You can control the inbound and outbound packets of CVMs by configuring security group rules. Three templates are available in the system: 
- Port 22 allowed on Linux: Only TCP port 22 for SSH login is exposed to the public network, and all the private network ports are allowed. **This template is unavailable for cloud databases**.
- Port 3389 allowed on Windows: Only TCP port 3389 for MSTSC login is exposed to the public network, and all the private network ports are allowed. **This template is unavailable for cloud databases**.
- All ports allowed: Allow all IPs to access cloud databases. This involves a certain security risk.

## Security Group Rules
Security group rules are used to control the inbound and outbound traffic of instances associated with the security group (filtered based on the rules from top to bottom). By default, a new security denies all traffic (All Drop). You can modify security group rules at any time, and the new rules take effect immediately.
Each security group rule involves the following items:
- Protocol port: Only **ALL** is supported for the cloud database protocol port. If you specify a port, this rule does not take effect for the cloud database.
- Authorization type: Access based on address ranges (CIDR/IP).
- Source (inbound rules) or destination (outbound rules): choose one of the following options:
    - Specify a single IP in CIDR notation.
    - Specify an IP address range in CIDR notation, such as 203.0.113.0/24.
- Policy: Allow or Deny.

## Security Group Priority
You can set security group priority in the instance console, and the smaller the number, the higher the priority. If an instance is associated with multiple security groups, the priority is used as a basis for evaluating the overall security rules for this instance.
In addition, if the last policy of multiple security groups associated with an instance is "ALL Traffic Denied", the last policy of all the security groups, except the security group with the lowest priority, will fail.

## Security Group Restrictions

- Security groups apply to cloud database instances in VPC [network environment](/doc/product/213/5227).
- Each user can set a maximum of 50 security groups for each project in each region.
- A maximum of 100 inbound access and 100 outbound policies can be set for a security group. **No outbound traffic is generated for cloud databases, so outbound rules do not take effect for cloud databases**.
- A cloud database can be associated with multiple security groups, and a security group can be associated with multiple cloud databases. No limit is imposes on the number.
>**Note:**
It is not recommended to associate too many instances with a security group, although no limit is imposed on the number of instances.

| Feature | Count | 
|---------|---------|
| Security group | 50/Region |
| Access policy | 100 (Inbound/Outbound) |
| Number of security groups associated with an instance | No limit |
| Number of instances associated with a security group | No limit |

