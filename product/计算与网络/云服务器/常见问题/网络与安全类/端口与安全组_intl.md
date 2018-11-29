## Port

### What ports need to be opened to Internet before instance login?

You need to open the corresponding port for the security group bound with the instance. For the detailed procedures, please see [Configuration in Typical Scenarios](https://cloud.tencent.com/document/product/213/12448).

### Which are common CVM ports?

Please see [Common Server Ports](https://cloud.tencent.com/document/product/213/12451).

### Why do you need to open the port? How to open a port?

You need to open the port in the security group before using services corresponding to the port. Example:

If you want to access web pages using port 8080, the port must be opened to Internet in the security group.

Open a port to Internet
1. Log in to the security group console, and click the security group bound with the instance to enter the details page
![](https://main.qcloudimg.com/raw/c448e60ad071de9abc1824aaa616f614.png)
2. Select "Inbound/Outbound Rules" and click **Add Rule**
![](https://main.qcloudimg.com/raw/6b69628e3a0ce6daa06071a6eaaaad55.png)
3. You can refer to the following template to enter your IP address (range) and port to be opened, and then select "Allow" to open the port
![](https://main.qcloudimg.com/raw/0477ac68f7ea684128f84fe0851a6514.png)

For detailed operation guide, please click [Common Security Group Operations](https://cloud.tencent.com/document/product/213/12450)

### Why cannot the service be used after the port is modified?

After modifying the service port, you also need to open the corresponding port in the corresponding security group. Otherwise, the service cannot be used.

### Which ports are not supported by Tencent Cloud?

There are security risks with the following ports. For security reasons, ISPs block them and make them inaccessible. It is recommended that you replace the port. Do not use the following ports for listening:

| Protocol | Unsupported Ports                                                   |
| ---- | ------------------------------------------------------------ |
| TCP  | 42 135 137 138 139 445 593 1025 1434 1068 3127 3128 3129 3130 4444 5554 9996 |
| UDP  | 1026 1027 1434 1068 5554 9996 1028 1433 135 ~ 139            |

### Why cannot I use the TCP 25 port to connect to an external address and how to lift the ban?

To improve the performance for sending emails from Tencent Cloud IP address, connection of CVM TCP port 25 to an external address is restricted by default. You can log in to the [console](https://console.cloud.tencent.com) and move your mouse cursor to **Account** of the top navigation, and you can see the entry of **Unblocking Port 25**.

Each user can unblock 5 instances in each region by default.

For more information, please see [Why is the outbound direction of CVM TCP port 25 blocked?](https://cloud.tencent.com/document/product/215/12390) 

## Security Group

### Why is there a default Reject rule in the security group?

The security group rules are filtered and take effect from top to bottom. After the Allow rules are enabled, other rules will be rejected by default. If all the ports are opened, the last Reject rule does not take effect. For security reasons, we provide this default setting.

### How to create a security group?

Please see the **Create Security Group** section of [Common Security Group Operations](https://cloud.tencent.com/document/product/213/12450).

### How to configure a security group?

Please see [Common Security Group Operations](https://cloud.tencent.com/document/product/213/12450).

### How are security groups associated with CVM instances?

Please see the **Configure Security Groups Associated with CVM Instances** section of [Common Security Group Operations](https://cloud.tencent.com/document/product/213/12450).

### If I bind an incorrect security group with an instance, what is the effect on the instance? How to solve the problem?

**Potential problems**

- You may fail to remotely connect to a Linux instance (SSH) or remotely log in to desktop Windows instance.
- You may fail to remotely ping the public IP and private IP for the CVM instance under this security group.
- You may fail to perform HTTP access to the Web services exposed by the CVM instance under this security group.
- The CVM instance under this security group may be unable to access Internet services.

**Solutions**

- In case any of the above problems happens, you can go to "Security Group Management" in the CVM console and reset the rule for the security group, for example, to "only bind all-pass security groups by default".
- For specific settings for security group rules, please see [Introduction to Security Group](https://cloud.tencent.com/document/product/213/12452).

### What do security group direction and policy mean?

The security group policy works in the directions of outbound and inbound. The former is to filter the outbound traffic of the CVM, and the latter is to filter the inbound traffic of the CVM.
The policy is two-fold: **Allow** and **Reject** traffic.

### In what order does the security group policy go into effect?

From top to bottom. The policy matching is in a top-to-bottom order when the traffic goes through the security group, and the policy goes into effect once the matching is successful.

### Why is an IP able to access the CVM without being allowed by the Security Group?

It may be caused by the following reasons:

- The CVM may be bound to multiple security groups and that specific IP may be allowed in other security groups.
- That specific IP serves for an approved Tencent Cloud public service.

### By using security groups, does it mean iptables cannot be used?

No. Security groups and iptables can be used simultaneously. Your traffic will be filtered twice in the following directions:

- Outbound: Processes on your CVM instance -> iptables -> Security groups.
- Inbound: Security groups -> iptables -> Processes on your CVM instance.

### Even though all the CVMs have been returned, the security groups still cannot be deleted, why?

Check if there is a CVM in the recycle bin. The security group bound to the CVM in recycle bin cannot be deleted.

### Can the name of the security group to be cloned be the same as that of a security group in the target area?

No. The name should be different from that of any existing security group in the target area.

### Can a security group be cloned across different users?

Not for now.

### Is there any Cloud API support for cloning a security group across different projects and regions?

MC support is provided to offer ease to customers who use the console, whereas no direct Cloud API support is available at the moment. You can use the original Cloud APIs for security group rules on batch import/export to indirectly clone a security group across different projects and regions.

### When a security group is being cloned across different projects and regions, will the CVMs managed by the security group be copied over?

No, cloning a security group across different regions will only clone the entry and exit rules of the original security group. The CVM needs to be associated separately.

