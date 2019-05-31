## 1. Basic Concepts
Network Access Control List (ACL) is an optional security layer at the subnet level and can be used as a firewall to control the incoming and outgoing traffic of subnets. You can configure a network ACL on subnet to add an additional security layer for your VPC. Its rules are similar to those of security group. In addition, network ACL can restrict the network traffic and improve the network performance.

- Network ACL has separate inbound and outbound rules. Each rule can be configured to allow or reject data traffic.
- Each new network ACL is disabled (reject all data traffic) initially until you add a rule.
- Network ACL is stateless, and its response to allow inbound traffic varies with the rules for outbound traffic - and vice versa.
- Network ACL does not affect the mutual access between CVM instances in the associated subnets.

### 2. Network ACL Rules
You need to add or delete ACL rules in the network ACL. When you add or delete rules in a network ACL, the changes are automatically applied to the subnets associated with the network ACL.

A network ACL rule consists of the following four elements:
- Protocol type
- Port or port range
- IP of source traffic or destination traffic (CIDR range)
- Allow or reject


Tencent Cloud evaluates the data packet and determines whether to allow the packet to flow in/out of the subnets based on the ACL inbound/outbound rules associated with the subnet. The network ACL rules in the list shall be applied in an order from top (the first rule) to bottom (the last rule). In case of any conflict among the rules, the rule that is higher in the list will be applied by default.

For example, you need to allow all source IPs to access all ports on the CVM, and only reject the HTTP access of the machine with a source IP of 192.168.200.11/24 to port 80. You can configure it as follows:

| Protocol Type | Port | Source IP | Policy | 
|---------|---------|---------|
| HTTP |80 | 192.168.200.11/24 | Reject |
| ALL |ALL | 0.0.0.0/0 | Allow |


## 3. Ephemeral Port Range
Since network ACL is stateless, it may fail to respond to the access request when no outbound rule is set, even if some inbound access is allowed. In this case, the client initiating the request will select an ephemeral port range. The range varies with different operating systems at the client side.
- Many Linux kernels use ports 32768-61000.
- Windows Server 2003 uses ports 1025-5000.
- Windows Server 2008 uses ports 49152-65535.

Therefore, if a Windows XP client on the Internet sends a request for access to the Web server in your VPC, your network ACL must have outbound rules to enable the traffic destined for ports 1025-5000.

## 4. Comparison Between Security Group and Network ACL

| Security Group | Network ACL | 
|---------|---------|
| Operations at the CVM instance level (the primary defense layer) | Operations at the subnet level (the secondary defense layer) | 
| Allow and Reject rules are supported | Allow and Reject rules are supported | 
| Stateful: Returned traffic is automatically allowed without subjecting to any rules | Stateless: Returned traffic must be explicitly allowed by rules | 
| Operations are only applied to CVM instance if security group is specified when the instance is activated or the security group is associated with the instance later | Operations are automatically applied to all CVM instances in the associated subnet (a backup defense layer to be used when a security group is bound to the CVM instances) | 

