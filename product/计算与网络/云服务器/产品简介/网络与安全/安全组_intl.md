## Security Group Overview
Security group is a stateful virtual firewall for filtering packets and is used to set the network access controls for a single or multiple CVMs. It is a logical grouping and an important means of network security isolation.

- You can add the basic network-based CVM or ENI instances with the same network security isolation requirements in the same region to the same security group.
- You can use the security group policies to filter the inbound and outbound traffic of an instance, which can be a basic network-based CVM or an ENI instance.
- You can modify security group rules at any time, and the new rules take effect immediately.

## Security Group Template
You can create a custom security group, or create a security group from template. Three templates are available in the system:

- Open Port 22 on Linux: Only TCP port 22 for SSH login is open to Internet, and all private network ports are open. 
- Open Port 3389 on Windows: Only TCP port 3389 for MSTSC login is open to Internet, and all private network ports are open.
- Open all ports: All ports are open to Internet and private networks. This poses certain security risks.

## Security Group Rules
Security group rules are used to control the inbound and outbound traffic of instances associated with the security group (filtered based on the rules from top to bottom). By default, a new security group rejects all traffic (All Drop). Therefore, a CVM associated with a security group with no rules will reject all traffic.

Each security group rule involves the following items:

 - Type: You can select a system rule template, or create custom rules.
 - Source or destination: Traffic source (inbound rules) or destination (outbound rules). Choose one of the following options:
  - Specify a single IP in CIDR notation.
  - Specify an IP address range in CIDR notation, such as 203.0.113.0/24.
  - Reference a security group ID. You can reference one of the following security group IDs:
     - Current security group. (This indicates whether CVMs associated with the security group can be mutually accessed or not)
       - Another security group. Another security group ID of the same project in the same region.
  - Reference an IP address object or an IP address group object in the [Parameter Template](https://cloud.tencent.com/document/product/215/9882). 
 - Protocol port: Enter the protocol type and port range, or reference an IP address object or an IP address group object in the [Parameter Template](https://cloud.tencent.com/document/product/215/9882).
 - Policy: Allow or Reject.

> **Note:**
>  - Referencing security group ID is optional. The rules of the referenced security group will not be added to the current security group.
>  - If you enter the security group ID in Source/Destination when configuring security group rules, the private IPs of the CVM's primary ENI and the ENI that are associated with this security group ID are used as Source/Destination, excluding public IP.

## Security Group Priority
- Multiple security groups associated with an instance are **prioritized from the smaller number to the bigger number**.
- The rules in a security group are **prioritized from top to bottom**.

An instance associated with a security group with no rules will reject all traffic by default.

## Security Group Restrictions

- Security groups are region and project-specific. CVMs can only be associated with the security groups in the same region and project.
- Security groups apply to any CVM instances in [network environment](/doc/product/213/5227).
- Each user can set a maximum of 50 security groups for each project in each region.
- A maximum of 100 inbound/outbound access policies can be set for a security group.
- A CVM can be associated with multiple security groups, and a security group can be associated with multiple CVMs. No number limit is imposed.
- Security groups associated with CVMs in **basic networks** **cannot filter** data packets sent from (or to) CDB and cloud cache service (Redis and Memcached) of Tencent Cloud. If necessary, you can use iptables to filter traffic of such instances.

| Feature | Count |
| ------------------ | -------------------------------- |
| Security group | 50/Region |
| Access policy | 100 (Inbound/Outbound) |
| Number of security groups associated with an instance | No limit |
| Number of instances associated with a security group | No limit |

> **Note:**
> If you have a large number of instances that need to access each other, you can assign them to multiple security groups, and achieve mutual authorization and access by configuring the rules for security group IDs.

## Comparison of Security Group and Network ACL

| Security Group | Network ACL |
| ------------------------------------------------------------ | ------------------------------------ |
| Operations at the CVM instance level (the primary defense layer) | Operations at the subnet level (the secondary defense layer) |
| Allow and Reject rules are supported | Allow and Reject rules are supported |
| Stateful: Returned traffic is automatically allowed without subjecting to any rules | Stateless: Returned traffic must be explicitly allowed by rules |
| Operations are only applied to an instance if the security group is specified when the instance is launched or the security group is associated with the instance later | Operations are automatically applied to all CVM instances in the associated subnet |

## Security Group-related Cloud APIs
Security group-related cloud APIs are Developer Tools of security groups. Cloud APIs can be used to work with security groups and manage the configurations of security groups and CVM instances. For more information, please see [Security Group-related APIs](/doc/api/229/API%E6%A6%82%E8%A7%88#6.-安全组相关接口).

