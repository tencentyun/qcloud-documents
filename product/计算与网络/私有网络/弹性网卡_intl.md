ENI is a virtual network interface. You can bind an ENI to a CVM for connection to network. It is very useful for configuring management networks and establishing highly reliable network solutions.

An ENI is VPC, availability zone and subnet-specific, and can only be bound to a CVM that resides in the same availability zone as it. A CVM can be bound with multiple ENIs. The maximum number of ENIs allowed to be bound to a CVM depends on the CVM's specification.

## Basic Information

The following information is associated with an ENI:

1. Primary ENI or secondary ENI: The ENI created with the creation of CVM within VPC is the primary ENI, and those created by users are secondary ENIs. The primary ENI does not support binding and unbinding, while secondary ENIs support.

2. Primary private IP: The primary private IP of an ENI is assigned by the system or specified by user when the ENI is created. The primary private IP of primary ENI can be modified, but that of secondary ENI cannot.

3. Secondary private IP: The secondary private IP bound to an ENI in addition to the primary IP. It is configured by user during the creation or editing of ENI, and supports binding and unbinding.

4. EIP: Bound with private IPs of an ENI in a one-to-one manner.

5. Security group: An ENI can be bound with one or more security groups.

6. MAC address: Each ENI has a unique global MAC address.


## Use Limits

The maximum number of ENIs that can be bound to a CVM and that of private IPs that can be bound to each ENI vary greatly with CPU and memory configurations. The limits are shown in the following table. For more information, please see [Use Limits on Other VPC Products](https://cloud.tencent.com/doc/product/215/537).

| CVM Configuration | Max. Number of ENIs | Max. Number of IPs Bound to Each ENI |
| ------------------- | :---- | :------ |
| CPU: 1-core   Memory: 1 GB | 2 | 2 |
| CPU: 1-core   Memory: >1 GB | 2 | 6 |
| CPU: 2-core | 2 | 10 |
| CPU: 4-core   Memory: < 16G | 4     | 10      |
| CPU: 4-core  Memory: >16 GB | 4 | 20 |
| CPU: 8-12 core | 6 | 20 |
| CPU: >12-core | 8 | 30 |

## Billing Method
Free of charge. For more information about the prices of VPC services, please see [VPC Price Overview](https://cloud.tencent.com/doc/product/215/3079).

## Operation Instructions


### View the ENI information

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left sidebar to go to the ENI list page.

3) Click the **Instance ID** of an ENI to go to its details page to view its information.

### Create an ENI

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left sidebar to go to the ENI list page.

3) Click **Create** in the upper left corner, and then select the VPC and subnet of the ENI in the pop-up window.

4) Select the private IP assigned to the ENI. It can be generated automatically or specified manually.

5) Click **OK** to complete the creation.

### Bind and configure an ENI (important)

**Step 1: Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).**

**Step 2: Click **ENI** in the left sidebar to go to the ENI list page.**

**Step 3: Locate the line of the ENI, and click **Bind to CVM** in the operation column (only CVMs in the same availability zone as the ENI are supported).**

**Step 4: Select the CVM to bind to and click **OK** to complete the binding.**



**Step 5: Configure the bound ENI in the CVM (important)**
>Note: After being bound on the console, the ENI needs to be configured in the CVM before it can be used normally. The following is the operation procedure for centos 7.2:

a. Log in to the CVM as an administrator, and execute the following command:


`cd /etc/sysconfig/network-scripts/`


b. Create the configuration file ifcfg-eth1 for the new ENI:

Enter the command:

`cp ifcfg-eth0 ifcfg-eth1`


Enter the command to modify the configuration file:

`vim ifcfg-eth1`

Modify the configuration file as follows:


`DEVICE='eth1'`

`NM_CONTROLLED='yes'`

`ONBOOT='yes'`

`IPADDR='192.168.1.62'  #Enter the actual address of the ENI`

`NETMASK='255.255.255.192'  #Enter the actual subnet mask`

`GATEWAY='192.168.1.1'  #Enter the actual gateway`


Save the modified configuration file and exit (enter "wq!" in the last line of vim and press Enter).


**Step 6: Disable rp_filter check**


Disable reverse path filtering in etc/sysctl.conf.

> Note: Reverse path filter means that when receiving an IP packet from an IP, the system checks whether the source IP is valid and discards the IP packet if the source IP is invalid. For example, an IP packet from IP B is received on ENI A. If ENI A is not the ENI intended for sending data to IP B, this IP packet is discarded. Because the route uses the primary ENI by default, after the reverse path filtering is enabled, the Ping test of the IP on the secondary ENI will fail.

Open the configuration file:

`vim /etc/sysctl.conf`

Modify

`net.ipv4.conf.default.rp_filter = 1`

to:

`net.ipv4.conf.default.rp_filter = 0`
`net.ipv4.conf.all.rp_filter = 0`
`net.ipv4.conf.eth0.rp_filter = 0`
`net.ipv4.conf.eth1.rp_filter = 0`

**Step 7: Restart network service**

Enter the following command:

`systemctl restart network`

**Step 8: Check and verify**

Enter the following command to check the IP

`ip addr`

Verify whether the secondary ENI and the IP on it are visible. Refer to the figure below:

![](https://mc.qcloudimg.com/static/img/682c0cda0fcbdbdb508785b12e102b4a/ip.png)

### Release private IP

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left sidebar to go to the ENI list page.

3) Click the **Instance ID** of an ENI to go to its details page to view its information.

4) Click **IP Management** tab to check the private IPs and EIPs already bound to the ENI.

5) Click **Release** button in the operation column for the line of the private IP.

6) Click **OK** to complete the operation.

>Note 1: The primary IP of an ENI cannot be released. Only secondary IPs can be released.

>Note 2: When the private IP is unbound, the EIP is automatically disassociated.

### Unbind from CVM

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left sidebar to go to the ENI list page.

3) Locate the line of the ENI and click **Unbind from CVM** in the operation column.

4) Click **OK** to unbind the ENI from the CVM.

>**Tips:** After the ENI is unbound, its associated private IPs, EIPs, security groups and other information are retained.

### Delete ENI

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left sidebar to go to the ENI list page.

3) Locate the line of the ENI and click **Delete** in the operation column.

4) Click **OK** to complete the deletion.

>Note 1: When the ENI is deleted, its associated private IPs, EIPs and security groups are automatically disassociated.

>Note 2: You can only delete ENIs that are not associated with CVMs.

>Note 3: The primary ENI is deleted as the CVM is deleted.

### Bind an EIP

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left sidebar to go to the ENI list page.

3) Click the **Instance ID** of an ENI to go to its details page to view its information.

4) Click **IP Management** tab to check the private IPs already bound to the ENI.

5) Click **Bind** button in the "Bound EIPs" column for the line of the private IP.

6) Select to bind an EIP from the **Existing EIPs** list or **New EIP** in the pop-up window.

7) Click **OK** to complete the binding.

### Unbind an EIP

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left sidebar to go to the ENI list page.

3) Click the **Instance ID** of an ENI to go to its details page to view its information.

4) Click **IP Management** tab to check the private IPs and EIPs already bound to the ENI.

5) Click **Unbind** button in the "Bound EIPs" column for the line of the private IP.

6) Click **OK** to complete the unbinding.

### Modify primary private IP

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left sidebar to go to the ENI list page.

3) Click the **Instance ID** of an ENI to go to its details page to view its information.

4) Click **IP Management** tab to view the primary private IPs already bound to the ENI.

5) Click **Modify Primary IP** button in the operation column for the line of the primary private IP.

6) Enter the new primary private IP in the pop-up window and click **OK**.

### Modify the subnet of ENI

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left sidebar to go to the ENI list page.

3) Click the **Instance ID** of the ENI to go to its details page.

4) In the basic information page of the details page, click **Change** button for the subnet.

5) Select the subnet to change to for the ENI and specify a new primary IP.

6) Click **Save** to finish the change of subnet.

>Note 1: You can only change the subnet of primary ENI.

>Note 2: You must unbind all secondary IPs before you can change the subnet of an ENI.

>Note 3: The subnet of an ENI can only be changed to another one under the same availability zone.

## FAQ
### In Windows system, what should be done if IP information is lost when the hot-plug ENI is restarted?
You need to manually configure the IP information for hot-plug ENI, and it may be lost when the server is restarted. You can download the following tool for configuration. (tool link: http://enipackage-1251740579.cosgz.myqcloud.com/NetCardIPSet%20%281%29.exe).

Follow the steps below:</BR>
1. Download the tool for Windows CVM.
</BR>
2. Insert the ENI and bind the IP.</BR>
3. Run the downloaded tool.



## API Overview
The APIs for ENI and their features are listed below. For more information about other VPC resources, please see [Overview of All VPC APIs](https://cloud.tencent.com/doc/api/245/909).


| Feature | Action ID | Description |
|---------|---------|---------|
| Create ENI | [CreateNetworkInterface] (https://cloud.tencent.com/doc/api/245/4811) | Create an ENI |
| Delete ENI | [DeleteNetworkInterface](https://cloud.tencent.com/doc/api/245/4813) | Delete an ENI |
| Query ENI Information | [DescribeNetworkInterfaces](https://cloud.tencent.com/doc/api/245/4814) | Query the information of an ENI |
| Assign Private IP for ENI | [AssignPrivateIpAddresses](https://cloud.tencent.com/doc/api/245/4817) | Assign a private IP for an ENI |
| Unassign Private IP for ENI | [UnassignPrivateIpAddresses](https://cloud.tencent.com/doc/api/245/4819) | Unassign a private IP for an ENI |
| Bind ENI to CVM | [AttachNetworkInterface](https://cloud.tencent.com/doc/api/245/4820) | Bind an ENI to a CVM |
| Unbind ENI from CVM | [DetachNetworkInterface](https://cloud.tencent.com/document/product/215/4822) | Unbind an ENI from a CVM |

