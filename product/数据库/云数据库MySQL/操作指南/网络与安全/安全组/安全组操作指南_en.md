This document describes how to create, delete, clone and configure a security group, and how to add, import and export security group rules.
>**Note:**
Now, cloud database security group only supports the network control of private network access and public network access in VPC, and does not support the network control of basic network. At present, only CDB for MySQL supports security group.

### Creating a security group

1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and then click "CVM" in the **Cloud Products in Use** section to go to the CVM management page. Click "Security Groups" in the left navigation tree to enter the security group management page.
![](//mc.qcloudimg.com/static/img/605d8758a359487291240d791ce4e90f/image.png)
![](//mc.qcloudimg.com/static/img/d6c8d4e12d497e3f55a4d5fbbae84e84/image.png)
2. Click "New" button, and select "Template" or "Custom", then enter the security group **name**, such as my-security-group. Select the **Project**, fill in **Remarks** (optional), and then click "OK".
![](//mc.qcloudimg.com/static/img/9dc27b43803588b7abb92ec1699ac89c/image.png)
![](//mc.qcloudimg.com/static/img/b1ca53ce95a6a908effec0cb71a81e57/image.png)

### Configuring security groups for a cloud database
[Security Group](https://cloud.tencent.com/doc/product/213/500) is an instance-level firewall provided by Tencent Cloud that is used to control inbound/outbound traffic of cloud databases. You can bind a security group to an instance when purchasing the instance, or bind a security group in the console after purchasing an instance.
>**Note:**
Now, security group is only available for **VPC-based cloud databases**.

Go to [Cloud Database Console](https://console.cloud.tencent.com/cdb), select the instance for which you want to configure a security group from the instance list, and then click "Manage". Select the "Security Group" tab, click "Configure Security Group", and then select the security group to associate with the instance. 
![](//mc.qcloudimg.com/static/img/2331e6b96fa1af3c9754cac0f8fe3854/image.png)

### Deleting a security group

1. Open the [Security Groups](https://console.cloud.tencent.com/cvm/securitygroup) page on the CVM console, and then click the "Delete" button next to the security group to be deleted in the list.
![](//mc.qcloudimg.com/static/img/43f705a8efd4426f18e547e6046b2149/image.png)
2. In the deletion confirmation dialog box, click "OK". If the security group is associated with a CVM, you need to remove the association before deleting the security group.

### Cloning a security group

1. Open the [Security Groups](https://console.cloud.tencent.com/cvm/securitygroup) page on the CVM console, and click the "Clone" button next to the security group to be cloned in the list.
![](//mc.qcloudimg.com/static/img/88ca3f6b17c21a2bd9d78f9e30a6c1b7/image.png)
2. In the "Clone Security Group" dialog box, select the destination region and project, then click "OK". If the new security group needs to be associated with CVMs, associate it with the desired CVMs.

### Adding rules to security group

1. Open the [Security Groups](https://console.cloud.tencent.com/cvm/securitygroup) page on the CVM console, and select the security group you want to update, then click the security group ID to show the details page, on which you can see the inbound/outbound rule tabs.
![](//mc.qcloudimg.com/static/img/20ad1010d14dde2696e3594339203929/image.png)
2. Click "Add Rules" on the inbound/outbound rule tab, select the options for the inbound/outbound rules, and fill in the required information. For example, specify 0.0.0.0/0 for source/destination, "ALL" for protocol port, and "Allow" for the policy, and then click "Finish". You can click "New Line" to add more rules.
>**Note:**
>Each security group rule involves the following items:
>- Protocol port: Only **ALL** is supported for the cloud database protocol port. If you specify a port, this rule does not take effect for the cloud database.
>- Authorization type: Access based on address ranges (CIDR/IP).
>- Source (inbound rules) or destination (outbound rules): choose one of the following options:
>    - Specify a single IP in CIDR notation.
>    - Specify an IP address range in CIDR notation, such as 203.0.113.0/24.
>- Policy: Allow or Deny.
</blockquote>
![The specified port for the security group is ALL](//mc.qcloudimg.com/static/img/8c5fa48b305592762e1e86acb30376b6/image.png)

### Importing/exporting security group rules

1. Open the [Security Groups](https://console.cloud.tencent.com/cvm/securitygroup) page on the CVM console, and select the security group you want to update, then click the security group ID to show the details page, on which you can see the inbound/outbound rule tabs.
![](//mc.qcloudimg.com/static/img/20ad1010d14dde2696e3594339203929/image.png)
2. On the tab, select the options for the inbound/outbound rules, and click the "Import Rule" button. If a rule already exists in the security group, export the existing rule first, otherwise it will be overwritten by the imported rule. If no rule exists, you can export and edit the rule template, and then import the modified template file.
![](//mc.qcloudimg.com/static/img/c338b1cd919986000468371e83a43655/image.png)
	





