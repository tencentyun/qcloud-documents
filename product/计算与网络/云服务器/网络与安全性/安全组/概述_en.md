## Overview
Security Group is a virtual firewall that allows state-based packet filtering. As an important network security isolation tool of Tencent Cloud, it is used to set network access control for one or multiple CVMs.

- A security group is a logical group. You can associate the basic network-based CVM or ENI instances with the same network security isolation requirements in the same region with the same security group.
- You can use the security group policies to filter the inbound and outbound traffic of an instance, which can be a basic network-based CVM or ENI instance.
- You can modify security group rules at any time, and the new rules take effect immediately.

## Security Group Template
You can create a custom security group, or create a security group from template. Three templates are available in the system:

- Port 22, 80, 443, 3389 and ICMP are open to Internet. The default Windows and Linux login ports and the common Web service ports are open to the public network. All private network ports are open.
- All ports are open: There is security risk to open all ports to public network and private network.

## Security Group Rules
Security group rules are used to control the inbound and outbound traffic of instances associated with the security group (filtered based on the rules from top to bottom). By default, a new security group denies all traffic (All Drop). The CVM associated with a security group without rules denies all traffic.

Each security group rule involves the following items:

 - Protocol type: For example, TCP, UDP or ICMP.
 - Port: Port range of the source/destination.
 - Authorization type: Access based on address ranges (CIDR/IP) or security groups (security group ID).
 - Source or destination: Traffic source (inbound rules) or destination (outbound rules). Choose one of the following options:
  - Specify a single IP in CIDR notation.
  - Specify an IP address range in CIDR notation, such as 203.0.113.0/24.
  - Reference a security group ID. You can reference one of the following security group IDs:
  	- Current security group: Indicates whether CVMs associated with the security group can be mutually accessed or not.
  	- Another security group: Another security group ID in the same region.
 - Policy: Allow or Deny.
  > **Note:**
  >  - Referencing security group ID is available for you as an advanced feature. Referencing security groups does not add rules to the current security group.
  >  - When referencing the security group ID and setting the policy to Allow: The CVM associated with source security group ID and the CVM associated with original security group can access each other.

## Security Group Priority
- The priority of multiple security groups associated with an instance: **The smaller the number, the higher the priority**.
- The priority of rules within a security group: **The higher the position, the higher the priority**.

If an instance is associated with a security group without any rules in it, the security group deny all traffic by default.

## Comparison of Security Group and Network ACL
<style> 
  table th:first-of-type { width: 20%; } 

  table th:first-of-type(3) { width: 40%; } 
 
 </style>
 
| Item | Security Group | Network ACL |
|---------|---------|---------|
| Operation level | Operations at the instance level (the primary defense layer) | Operations at the subnet level (the secondary defense layer) |
| Supported rules | Allow and Deny rules are supported | Allow and Deny rules are supported |
| State-based or not | State-based: Returned traffic is automatically allowed without subjecting to any rules | Not State-based: Returned traffic must be explicitly allowed by rules |
| Application to instances | Operations are only applied to the instance if the security group is specified when the instance is activated or the security group is associated with the instance later | Operations are automatically applied to all CVM instances in the associated subnet |

