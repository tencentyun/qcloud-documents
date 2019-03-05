The CVM instance described below also refers to dedicated CVM.

## Security Group Overview

Security Group is a virtual firewall that allows state-based packet filtering. As an important network security isolation tool, it is used to set network access control for one or multiple CVMs.

A security group is a logical grouping that adds CVM instances with the same network security isolation requirements, in the same geographic location, to the same security group. You can securely filter incoming and outgoing traffic to a CVM through security group policies.

While creating a CVM instance, you can associate one or multiple security groups to it. Add rules to the security group to regulate the incoming and outgoing traffic of the associated CVM instance.

You can modify the rules for a security group at any time; the new rules will take effect immediately on all the associated CVM instances. The security group priority that you configured in the console will be the evaluation basis for the instance's security rules.

Tencent Cloud in adds three default security groups in each region, namely: the default security group to release all ports, Linux security group to release 22 port (allow SSH remote login for Linux servers), Windows security group to release 3389 ports (allow mstsc remote login for Windows servers). You can bind the default security group as needed.

## Rules of Security Group
The security group rule controls inbound traffic to CVM instances associated with a security group, and outbound traffic that is allowed to leave the CVM instance (filtering rules from top to bottom). By default, the new security group will All Drop (deny) all traffic.
You can specify the following for each rule of a security group:

●	Protocol type: such as TCP, UDP, ICMP, or etc.
●	Port: Port range of source or target.
●	Authorization type: address segment (CIDR/IP) access, or security group access (security group ID);
●	Source (inbound rule) or target (outbound rule) of one of the following options:
　○	A single IP address specified by CIDR notation.
　○	A range of IP addresses specified by CIDR notation (for example, 203.0.113.0/24).
　○	Reference the security group ID. You can reference one of the following security group IDs:
　　■	The current security group. (Indicates that CVMs associated with a security group can/cannot interconnect)
　　■	Another security group ID in the same region.

> Note: The security group ID is referenced as a high-level feature. You can choose to use without adding the rule from the referenced security group to the current security group; where the security group ID represents the private network IPs of the associated CVM instances.

●	Policy: Allow or Deny.
> Referencing the security group ID and setting the policy to 'Allow' means: the CVM associated with the source security group ID can access the CVM associated with the security group; or the CVM associated with the security group can access the CVM associated with the target security group.

## Restrictions for Security Groups

- The security group applies to CVM instances under any [Network Environments](/doc/product/213/5227).

- Each user can set at most 50 security groups per project per region.

- A maximum of 100 access policies can be set for the inbound and outbound directions of a security group.

- A CVM can join unlimited number of security groups; a security group can associate unlimited number of CVMs at the same time.

> Note: The number of CVM instances in a security group is unlimited, but should not be excessive.
If you have a large number of CVM instances that need to be interconnected, you can assign them to multiple security groups and authorize them mutual access to each other by using the rule set of the security group ID.

| Feature Description       | Quantity                  |
| ---------- | ------------------- |
| Security group        | 50/region              |
| Access policy       | 100/inbound direction, 100/outbound direction |
| Number of associated security groups of a CVM | Unlimited                 |
| Number of associated CVMs within a security group | Unlimited                 |

## Comparison of Security Group and Network ACL

| Security Group                                      | Network ACL                |
| ---------------------------------------- | -------------------- |
| Operations at the CVM instance level (the primary defense layer)                     | Operations at the subnet level (the secondary defense layer)      |
| Allow and Deny rules are supported                              | Allow and Deny rules are supported          |
| Stateful: Returned traffic is automatically allowed without subjecting to any rules                | Stateless: Returned traffic must be explicitly allowed by rules   |
| Operations are only applied to CVM instance if security group is specified when the instance is activated or the security group is associated with the instance later | Operations are automatically applied to all CVM instances in the associated subnet |

## Create a Security Group

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click "Security Group".

3) Click "New" button.

4) Enter the name of the Security Group (e.g. my-security-group) in the pop-up box and provide a description.

## Delete Security Group

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click "Security Group".

3) Click "Delete" button after the security group entry in the list.

4) In the "Delete Security Group" dialog box, click "OK". If the current security group has a CVM associated with it, you can only delete the security group after you remove it.

## Clone Security Group

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click "Security Group".

3) Click the "Clone" button next to the security group entry in the list.

4) In the "Clone Security Group" dialog box, select the target region and target item, and click [OK]. If the new security group need to associate with a CVM, please re-administer the CVM server within the security group.

## Add a Rule to the Security Group

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click "Security Group".

3) Select the security group that needs to be updated and click the security group ID. The Details pane will list the details of the Security Group as well as the tab for using inbound and outbound rules.

4) On the "Inbound/Outbound Rules" tab, click "Edit". Select the options to be used for inbound and outbound rules in the tab, then enter the required information. For example, select HTTP or HTTPS, and specify the source/target as 0.0.0.0/0. When this process completes, click "Save".

5) You can also allow/deny communication between instances associated with different security groups. On the "Inbound/Outbound Rules" tab, select "All Traffic" from the list of rule protocols; for Source/Target, select "Security Group ID", and this will provide you with a list of security groups. Select the security group from the list, then click "Save". This means that communication is allowed/denied between CVMs that are associated with this security group and the CVMs that are associated with the selected security groups.

## Configure the Security Groups Associated with the CVM Instance

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2)	Click "Cloud Virtual Machine" in the navigation pane.

3)	On the right side of the instance with the security group needs to be configured, click "Configure Security Group".

4)	In the "Configure Security Group" dialog box, select one or more security groups from the list and click "OK".

Or:
1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2)	Click "Security Group" in the navigation pane.

3) Select the security group to be associated and click the "Manage CVM" button in the operation column.

4) In the "Add/Remove CVM" pop-up box, add or remove the CVMs that need to be associated with the security group and click "OK".
![](//mccdn.qcloud.com/img568cc2f621ea8.png)

## Import and Export Security Group Rules

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) In the navigation pane, click "Security Group".

3) Select the security group that needs to be updated and click the security group ID. The Details pane will list the details of the Security Group as well as the tab for using inbound and outbound rules.

4) On the "Inbound/Outbound Rules" tab, click "Edit". Select the options to be used for inbound and outbound rules in the tab, then click "Import Rules" button. Since the rule import will overwrite any original rules, it is recommended that you export the existing rule first; if the original rule is blank, you can export the template, edit the template file, and then import the file.


## Security Group Cloud API
The security group cloud API is the developer tool for security group. It is used to complete security group operations, and manage configurations between security groups and CVM instances. Click [here](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88#6.-安全组相关接口).





