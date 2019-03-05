## Security Group Overview
Security group is a stateful packet filtering virtual firewall, which is used to set up single or multiple CVM network access controls; and is an important means by which Tencent Cloud provides network security isolation.

- A security group is a logical grouping that adds instances of CVMs with the same network security isolation requirements, in the same geographic location, to the same security group. You can securely filter incoming and outgoing traffic to a CVM through security group policies.
-  You can securely filter incoming and outgoing traffic to an instance (**basic network CVM** or **elastic network card**) through security group policies.
- You can modify the rules for a security group at any time
- The security group priority that you configured in the console; the lower the number, the higher the priority

Tencent Cloud in adds three default security groups in each region; namely: the default security group to release all ports, Linux security group release 22 port (to allow SSH remote login for Linux servers), Windows security group release 3389 port (allowing mstsc to log onto a Windows server remotely) You can bind the default security groups as needed.

## Security group rules
The security group rule controls inbound traffic to CVM instances associated with a security group, and outbound traffic that is allowed to leave the CVM instance (filtering rules are from top to bottom). By default, the new security group will 'All Drop' (reject) all traffic.
For each rule of a security group, you can specify the following:

● Protocol type: such as TCP, UDP, or ICMP.
●	Port: Port range of source or target.
●	Authorization type: address segment (CIDR/IP) access, or security group access (security group ID);
●	Source (inbound rule) or target (outbound rule) of one of the following options:
　○	Use CIDR notation to specify a single IP address.
　○	Use CIDR notation to specify a range of IP addresses (for example, 203.0.113.0/24).
　○	Reference the security group ID. You can reference one of the following security group IDs:
　　■  The current security group. (Indicates that CVMs associated with a security group can/cannot be visited)
　　■	Another security group ID in the same zone.

> Note: The security group ID is referenced as a high-level feature that you can choose to use without adding a rule from the referenced security group to the current security group; where the security group ID represents the private network IP of the associated CVM instance address.

●  Policy: Allow or Deny.
> Referencing the security group ID and setting the policy to 'Allow' means that the CVM associated with the source security group ID can access the CVM associated with the security group; or the CVM associated with the security group can access the CVM associated with the target security group.

## Security group priority
The security group priority that you configured in the CVM instance console; the lower the number, the higher the priority. When a cloud host binds to multiple security groups, the priority is used as the basis for our assessment of the overall security rules for that instance.
In addition, if the last policy of the multiple security groups to which the cloud host is bound is [Deny ALL Traffic], the last policy [Deny ALL Traffic] of the other security groups will be invalid except for the lowest priority security group.

## Restrictions for security groups

- The security group applies to CVM instances under any [network environment](/doc/product/213/5227).
　　
- Each user can set up to 50 security groups per project per region.
　　
- A maximum of 100 access policies can be configured for the inbound and outbound directions of a security group.
　　
- A CVM can join multiple security groups; a security group can associate multiple CVMs at the same time, with an unlimited number.

- For CVMs in the **basic network**, bound security groups **CANNOT filter** packets to and from CDB and elastic cache (Redis和Memcached) of Tencent Cloud. To filter these packets, please use iptables.

> Note: The number of CVM instances in a security group is unlimited, but should not be excessive.
> If you have a large number of CVM instances that need to be visited, you can assign them to multiple security groups and grant them mutual access to each other by using the rule set of the security group ID.

| Function description | Amount | 
|---------|---------|
| Security group | 50/region |
| Access policy | 100/inbound direction, 100/outbound direction |
| Number of bound security groups of in instance | Unlimited |
| Number of instances in a security group | Unlimited |

## The difference between security groups and network ACLs

| Security group | Network ACL | 
|---------|---------|
| Instance-level operations (first defense layer) | Subnet-level operations (second defense layer) |
"
| Supports rules that 'Allow' or 'Deny' | Supports rules that 'Allow' or 'Deny' |
| Stateful: The return data stream is automatically allowed and is not affected by any rules | Stateless: The return data stream must be explicitly allowed by the rule |

1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

## Create security group

1) Open [CVM console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click [Security Group].

3) Click the [New] button.

4) Enter the name of the security group (for example: my-security-group) and provide a description.

## Delete security group

1) Open [CVM console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click [Security Group].

3) Click the [Delete] button next to the security group entry in the list.

4) In the Delete Security Group dialog box, click [OK]. If the current security group has a CVM associated with it, you need to remove the security group before you can delete it.

## Clone security group

1) Open [CVM console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click [Security Group].

3) Click the [Clone] button next to the security group entry in the list.

4) In the Clone Security Group dialog box, select the target region and target item, and click [OK]. If the new security group is associated with a CVM, please re-administer the cloud host within the security group.

## Add a rule to the security group

1) Open [CVM console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click [Security Group].

3) Select the security group that needs to be updated and click the security group ID. The details pane displays detailed information about the security group and makes tabs available that allow you to use inbound and outbound rules.

4) On the Inbound/Outbound Rules tab, click [Edit]. From the tab, select the option for the Inbound/Outbound rule, and fill in the required information. For example, select HTTP or HTTPS, and specify the source/destination as 0.0.0.0/0. When finished, click [Save].

5) You can also allow/deny communication between instances associated with different security groups. On the Inbound/Outbound Rules tab, select [All Traffic] from the list of rule protocols; for Source/Target, select [Security Group ID]; this will provide you with a list of security groups. Select the security group from the list, and then click Save. This means that communication is allowed/denied between CVMs that are associated with this security group and the CVMs that are associated with the selected security groups.

## Configure the CVM instance associated with the security group

1) Open [CVM console](https://console.cloud.tencent.com/cvm/).

2) Click [Cloud Host] in the navigation pane.

3) On the right side of the instance where the security group needs to be configured, click [Configure Security Group].

4) In the Configure Security Group dialog box, select one or more security groups from the list and click [OK].

or
1) Open [CVM console](https://console.cloud.tencent.com/cvm/).

2) Click [Security Group] in the navigation pane.

3) Select the security group to be associated and click the [Manage Cloud Host] button in the action bar.

4) In the Add/Remove Cloud Hosts pop-up, add or remove the cloud hosts that need to be associated with the security group and click [OK].
![](//mccdn.qcloud.com/img568cc2f621ea8.png)

## Import and export security group rules

1) Open [CVM console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click [Security Group].

3) Select the security group that needs to be updated and click the security group ID. The details pane displays detailed information about the security group and makes tabs available that allow you to use inbound and outbound rules.

4) On the Inbound/Outbound Rules tab, click [Edit]. From the tab, select the option for the Inbound/Outbound rule, and click the [Import Rules] button. If you already have a rule, it is recommended that you export the existing rule first, because the rule import will overwrite any original rules; if the original rule is blank, you can export the template, edit the template file, and then import the file.


## Security Group Cloud API
Security Group Developer Tool, you can use the cloud API to complete security group operations, and manage configurations between security groups and CVM instances; click [here](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88#6.-安全组相关接口).


