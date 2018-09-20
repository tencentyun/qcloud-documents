Security group serves as a stateful virtual firewall with filtering function for setting network access control for one or more cloud databases. It is an important network security isolation tool provided by Tencent Cloud. A security group is a logical group. You can associate the VPC-based cloud database instances with the same network security isolation requirements in the same region with the same security group. Basic network-based cloud databases are not supported now. The databases share the security group list with the CVMs. Matching is performed based on the rules in the security group. **If you want to use the security group feature, submit a ticket to active Use Whitelist.**
## Policies ##
Security group policies are divided into "allowing" and "denying" traffic. You can use the security group policies to filter the inbound traffic of an instance.
## Templates ##
You can create a custom security group, or create a security group from a template. You can control the inbound and outbound packets of CVMs by configuring security group rules. Three templates are available in the system:<br>

- Port 22 allowed on Linux: Only TCP port 22 for SSH login is exposed to the public network, and all the private network ports are allowed. This template is unavailable for databases.
- Port 3389 allowed on Windows: Only TCP port 3389 for MSTSC login is exposed to the public network, and all the private network ports are allowed. This template is unavailable for databases.
- All ports opened to the Internet: Allow all IPs to access databases. This involves a certain security risk.
## Rules ##
Security group rules are used to control the inbound and outbound traffic of instances associated with the security group (filtered based on the rules from top to bottom). By default, a new security group rejects all traffic (All Drop). You can modify security group rules at any time, and the new rules take effect immediately. Each security group rule involves the following items:<br>

- Protocol port: Only **ALL** is supported for the database protocol port. If you specify a port, this rule does not take effect for the database.
- Authorization type: Access based on address ranges (CIDR/IP).
- Source (inbound rules) or destination (outbound rules): choose one from the following options:
	- Specify a single IP in CIDR notation.
	- Specify an IP address range in CIDR notation, such as 203.0.113.0/24.
- Policy: Allow or Reject.
## Priority ##
You can set security group priority in the instance console, and the smaller the number, the higher the priority. If an instance is associated with multiple security groups, the priority is used as a basis for evaluating the overall security rules for this instance.<br>
In addition, if the last policy of multiple security groups associated with an instance is "ALL Traffic Denied", the last policy of all the security groups, except the security group with the lowest priority, will fail.
## Limits ##
| Feature | Max count |
|---------|---------|
| Number of security groups | 50/region |
| Access policy | 100 (Inbound/Outbound) |
| Number of security groups associated with an instance | No limit |
| Number of instances associated with a security group | No limit |
> Note:
> No outbound traffic is generated for databases, so outbound rules do not take effect for databases.
## Operation Instructions ##
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and go to the CVM management page. Click **Security Groups** in the left navigation tree to enter the security group management page.
![](https://main.qcloudimg.com/raw/2f610d991434e8b8fd88a8a62e2b35be.png)
![](https://main.qcloudimg.com/raw/83abfd58095f5cadaf6d37952c26be0d.png)
2. Click **New**, select **Template** or **Custom**, and then enter the security group name. Select the Project, enter Remarks (optional), and then click **OK** and configure the inbound rules for the security group.
![](https://main.qcloudimg.com/raw/e3771c3361e5be17d57b3d43b1075c41.png)
![](https://main.qcloudimg.com/raw/6d743de438da3351bb8c88aa27e66695.png)
![](https://main.qcloudimg.com/raw/f42d369504fdc331caa17be888f9d5d4.png)
3. In the security group list, select **Manage Instances**, click **Cloud Database**, and click **Add Instances** to associate databases with the security group.
![](https://main.qcloudimg.com/raw/bfeb92ddfb8b8b2e1705d209f30242bc.png)
![](https://main.qcloudimg.com/raw/14fee1c0e3c5c039f95dc2dbff137044.png)
![](https://main.qcloudimg.com/raw/2cda9e2a0bdc31a2d6071f3d926573ae.png)
For more information, see [Common Security Group Operations](https://cloud.tencent.com/document/product/213/12450).

