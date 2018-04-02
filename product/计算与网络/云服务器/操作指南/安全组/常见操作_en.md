You can create, view, update, delete, or perform other management operations for security groups and security group rules on the CVM Console.
### Creating a Security Group

 1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
 2. Click **New** button.
 3. Enter the security group name (e.g. my-security-group) and the description.
 4. Click **OK** to complete.

### Adding Rules to Security Group

 1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
 2. Select the security group you want to update, and click **Security Group ID** to show the details page, on which you can see the inbound/outbound rule tabs.
 3. On the **Inbound/Outbound Rules** tab, click **Edit**, then select the options for the inbound/outbound rules, and fill in the required information, and then click **Save**.

### Configuring Security Groups Associated with CVM Instances

 1. Open [Console - CVM](https://console.cloud.tencent.com/cvm/).
 2. In the operation column on the right side of the instance for which you want to configure a security group, click **More** and then click **Configure Security Group**.
 3. In the "Configure Security Group" dialog box, select one or more security groups from the list and click **OK**.

**Or**

 1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
 2. Select the security group to be associated, and click **Add an Instance** or **Remove an Instance** button in the operation column.
 3. In the **Add/Remove a CVM** dialog box, add or delete the CVM to be associated with this security group, and click **OK**.
 ![](//mc.qcloudimg.com/static/img/064ce4c28658b8fdc2015bcb58deafdd/image.png)

### Importing/Exporting Security Group Rules
 1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
 2. Select the security group you want to update, and click **Security Group ID** to show the details page, on which you can see the inbound/outbound rule tabs.
 3. On the tab, select the options for the inbound/outbound rules, and click the **Import Rule** button. If a rule already exists in the security group, export the existing rule first, otherwise it will be overwritten by the imported rule. If no rule exists, you can export and edit the rule template, and then import the modified template file.

### Cloning a Security Group

 1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
 2. Click the **Clone** button corresponding to the security group to be cloned in the list.
 3. In the **Clone Security Group** dialog box, select the target region and project, and then click **OK**. If the new security group needs to be associated with CVMs, configure the security group again.

### Deleting a Security Group

 1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
 2. Click the **Delete** button corresponding to the security group to be deleted in the list.
 3. In the **Deletion** Confirmation" dialog box, click **OK**. If the security group is associated with a CVM, you need to remove the association before deleting the security group.

