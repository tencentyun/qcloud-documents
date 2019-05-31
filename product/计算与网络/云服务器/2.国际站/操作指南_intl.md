You can create, view, update and delete security groups and security group rules or perform other operations on them in the CVM console.

## Common Operations

### Creating a security group

1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
2. Click **New** button.
3. Enter the security group name (e.g. my-security-group) and the description.
4. Click **OK** to finish the creation.

### Adding rules to security group

1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
2. Select the security group to be updated, and then click **Security Group ID**. The Details pane will list the details of the security group as well as the tab for using inbound and outbound rules.
3. On the Inbound/Outbound Rules tab, click **Edit**. Select the options for the inbound/outbound rules from the tab, enter the required information, and then click **Save**.

### Configuring a security group to associate with CVM instances

1. Open [Console - CVM](https://console.cloud.tencent.com/cvm/).
2. In the Operation column next to the instance for which you want to configure a security group, click **More** and then click **Configure Security Group**.
3. In the Configure Security Group dialog box, select one or more security groups from the list and click **OK**.

**Or**

1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
2. Select the security group to be associated with CVMs, and then click **Add Instances** or **Remove Instances** button in the Operation column.
3. In the Add/Remove CVMs popup box, add or delete the CVMs to be associated with this security group, and click **OK**.
   ![]()

### Importing/exporting security group rules

1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
2. Select the security group to be updated, click **Security Group ID**. The Details pane will list the details of the security group as well as the tab for using inbound and outbound rules.
3. Select the options for inbound/outbound rules from the tab, and then click **Import Rules** button. If you already have the rules, it is recommended to export existing rules first. Importing the new rules will overwrite the existing rules. If the original rules are empty, you can export the template, edit the template file, and then import the file.

### Cloning a security group

1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
2. Click the **Clone** button for the security group to be cloned in the list.
3. In the Clone Security Group dialog box, select the destination region and project, and then click **OK**. If the new security group needs to be associated with a CVM, reconfigure the security group.

### Deleting a security group

1. Open [Console - Security Group](https://console.cloud.tencent.com/cvm/securitygroup).
2. Click the **Delete** button for the security group to be deleted in the list.
3. In the Delete Security Group dialog box, click **OK**. If the current security group is associated with a CVM, disassociate the security group from the CVM before deleting it.

## Typical Scenario Configuration

### Remotely logging in to Linux instances via SSH

To log in to a Linux instance via SSH remotely, add the following inbound rule to the security group associated with the instance:

| Source    | Protocol Port | Policy |
| --------- | ------------- | ------ |
| 0.0.0.0/0 | TCP:22        | Allow  |

> **Note:** You can set **IP address range** or **security group** for the Source.

### Logging in to Windows instances via MSTSC

To log in to a Windows instance via MSTSC, add the following inbound rule to the security group associated with the instance:

| Source    | Protocol Port | Policy |
| --------- | ------------- | ------ |
| 0.0.0.0/0 | TCP:3389      | Allow  |

> **Note:** You can set **IP address range** or **security group** for the Source.

### Pinging a CVM instance in public network

To test the communication status of a CVM instance using Ping program, add the following inbound rule to the security group associated with the instance:

| Source    | Protocol Port | Policy |
| --------- | ------------- | ------ |
| 0.0.0.0/0 | ICMP          | Allow  |

> **Note:** You can set **IP address range** or **security group** for the Source.

### Using CVM instance as Web servers

If you create an instance as a Web server, you need to install the Web server program on the instance, and add the following inbound rule to the security group associated with the instance:

> **Note:** You need to start the Web server program first, and check whether the port is set to 80.

| Source    | Protocol Port | Policy |
| --------- | ------------- | ------ |
| 0.0.0.0/0 | TCP:80        | Allow  |

### Uploading or downloading files with FTP

To upload/download files to/from a CVM instance with FTP, add the following inbound rule to the security group associated with the instance:

> **Note:** You need to install the FTP server program on the instance, and then check whether the port 20/21 works properly.

| Source    | Protocol Port | Policy |
| --------- | ------------- | ------ |
| 0.0.0.0/0 | TCP:20,21     | Allow  |

