Security group is an instance-level firewall provided by Tencent Cloud, which is used to control inbound/outbound traffic of CVMs.

 1. Log in to the [CVM console](https://console.cloud.tencent.com/cvm/index), and click **Security Group** in the left navigation pane.
 2. Click the **New** button, enter the security group name (e.g. my-security-group), select **Template** or **Custom**, and then click **OK** after confirming inbound and outbound rules.
 3. Click the **Add an Instance** button on the right of the security group list, and select the CVM to be associated with the security group to complete the process. 

**Or**

You can also enter the CVM list page to view or modify the security group associated with the CVM. On the **CVM** list page, select the CVM for which you want to modify the security group, then click **More** -> **Configure Security Group** on the right side, and select a security group to associate.
(For example, to allow your local computer (IP: 186.23.55.90) to send HTTP requests to the CVM, you can create a rule as shown in the figure below.)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](//mc.qcloudimg.com/static/img/5a7f41e7a6e4fb76f33565fb9a860bf7/image.png)

