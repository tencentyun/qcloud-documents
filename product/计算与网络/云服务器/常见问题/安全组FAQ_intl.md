## About the usage of security groups
### 1. When a security group is not selected correctly, what network problems will there be that interfere with the creation of CVM instances by using the security group? How to resolve them?
**Problems**
- The attempt to remotely connect to a Linux instance (SSH) or perform remote desktop connection to a Windows instance may fail.
- The attempt to remotely ping the public IP and private IP for the CVM under this security group may fail.
- The attempt to perform HTTP access to the Web services exposed by the CVM instance under this security group may fail.
- The CVM instance under this security group may not be able to access Internet services.

**Solutions**
- In case any of the above problems happens, you can go to "Security Group Management" in the CVM console and reset the rule for the security group, for example, to "only bind all-pass security groups by default".
- For how to set up security group rules, please see [Security Group Guidelines](https://cloud.tencent.com/doc/product/213/5221).

### 2. In what order does the security group policy go into effect?
From top to bottom. The policy matching is in a top-to-bottom order when the traffic goes through the security group, and the policy goes into effect once the matching is successful.

### 3. What do security group direction and policy mean?
The security group policy works in the directions of outbound and inbound. The former is to filter the outbound traffic of the CVM, and the latter is to filter the inbound traffic of the CVM.
The policy is two-fold: **Allow** and **Reject** traffic.

### 4. Why is an IP able to access the CVM without being allowed by the Security Group?
- The CVM may be bound to multiple security groups and that particular IP may be allowed in other security groups.
- That particular IP serves for an approved Tencent Cloud public service.

### 5. How to determine the priority for multiple bound security groups?
A lower number indicates a higher priority.

### 6. How to adjust the priority for security groups?
Go to "CVM Console" -> "Details Page" -> "Security Group" -> "Bound Security Groups" -> "Modify".

### 7. Even though all the CVMs have been returned, the security groups still cannot be deleted, why?
Check the Recycle Bin for any CVM. The deletion won't be successful when there is bound CVM(s) in the Recycle Bin.

### 8. By using security groups, does it mean iptables cannot be used?
No, security groups and iptables can be used simultaneously. Your traffic will be filtered twice in the following directions:
- Outbound: processes on your CVM instance -> iptables -> security groups.
- Inbound: security groups -> iptables -> processes on your CVM instance.


## About security group cloning

### 1. When a security group is being cloned across different projects and regions, will the CVMs managed by the security group be copied over?
No, cloning a security group across different regions will only clone the entry and exit rules of the original security group. The CVM needs to be associated separately.
### 2. Can a security group be cloned across different users?
Not for now.
### 3. Is there any Cloud API support for cloning a security group across different projects and regions?
Currently MC support is provided to offer ease to customers who use the console, whereas no direct Cloud API support is available at the moment. You can use the original Cloud APIs for security group rules on batch import/export to indirectly clone a security group across different projects and regions.
### 4. Can the name of the security group to be cloned be the same as that of a security group in the target area?
The name should be different from that of any existing security group in the target area.
