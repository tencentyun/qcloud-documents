ENI is a virtual network interface. You can bind an ENI to a CVM and connect it to the network. ENI is very useful when configuring management networks and establishing highly reliable network solutions.

ENI has VPC, availability zone and subnet attributes. You can only bind it to CVMs under the same availability zone. Each CVM may have multiple ENIs bound to it. The allowed number of ENIs depends on the specifications of the host.

## Basic Information

An ENI has the following major relevant information:

1. Primary ENI or secondary ENI: The ENI that was created when creating the CVM within the VPC is the primary ENI. And ENIs created by the user will be secondary ENIs. You can bind/unbind secondary ENIs but not the primary one.

2. Primary private IP: The primary private IP of the ENI is assigned by the system, or specified by the user when the ENI was created. You can modify the primary private IP of the primary ENI, but not the ones for secondary ENIs.

3. Secondary private IP: Secondary private IPs that are bound to the ENI, other than the primary IP, are configured by the user when he/she creates of modifies the ENI. You can bind/unbind these IPs.

4. Elastic public IP: Bound with private IPs of the ENI in a one-to-one correspondence manner.

5. Security group: Each ENI may bind one or multiple security groups.

6. MAC address: Each ENI has a unique global MAC address.


## Usage Constraints

The number of ENIs that may bind to a CVM, and the number of private IPs that can bind to each ENI will greatly vary according to CPU and RAM configuration. These allowed numbers are shown in the following table. Also, refer to [Usage Limits of Other VPC Products](https://cloud.tencent.com/doc/product/215/537).

| CVM Configuration               | Number of ENIs | Number of IPs for Each ENI |
| ------------------- | :---- | :------ |
| CPU:  Single core   RAM:  1 G    | 2     | 2       |
| CPU:  Single core   RAM:  >1 G   | 2     | 6       |
| CPU:  Dual core             | 2     | 10      |
| CPU:  4-core   RAM:  < 16 G | 4     | 10      |
| CPU:  4-core   RAM:  > 16 G | 4     | 20      |
| CPU:  8 to 12 cores          | 6     | 20      |
| CPU:  >12-core           | 8     | 30      |

## Billing Method
Free. For more information regarding the prices of VPC services, refer to [VPC Price Overview](https://cloud.tencent.com/doc/product/215/3079).

## Instructions

### Viewing ENI

1) Go to [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left panel to open the ENI list.

3) Click the **Instance ID** of an ENI to open its detail page and view its information.

### Creating ENI

1) Go to [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left panel to open the ENI list.

3) Click **New** in the top-left corner and choose the parameters of the ENI in the pop-up window.

4) Click **OK** to complete.

### Binding with a CVM

1) Go to [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left panel to go to the page with a list of ENIs.

3) Find your target ENI and click **Bind CVM** in the action bar.

4) Select the CVM to be bound and click **OK** to complete.

### Unbinding with a CVM

1) Go to [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left panel to go to the page with a list of ENIs.

3) Find the line of the ENI and click **Unbind CVM** in the action bar.

4) Click **OK** to complete.

Note: Once you unbind an ENI, information such as its associated private IPs, elastic public IPs, security groups will be retained.

### Deleting an ENI

1) Open the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left panel to go to the page with a list of ENIs.

3) Find the line of the ENI and click **Delete** in the action bar.

4) Click **OK** to complete the deletion process.

Note 1: Once the ENI is deleted, its private IPs, elastic public IPs and security groups will be disassociated.

Note 2: You can only delete ENIs that are not currently associated with CVMs.

Note 3: The primary ENI will be deleted as the CVM is deleted.

### Assigning Private IP (Tencent Cloud Console)

1) Open the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left panel to go to the page with a list of ENIs.

3) Click the **Instance ID** of the ENI to go to its detail page and view its information.

4) Click **IP Management** tab to view the private IPs and elastic public IPs that are already bound to the ENI.

5) Click **Assign Private IP** button to open the **Assign Private IP** window.

6) You can choose to "Auto Assign" or "Manually Enter" private IP.

7) You can click the **Add** button to assign multiple IPs for the ENI in the "Assign Private IP" window.

8) Click "OK" button to complete the assigning process.

Note: You need to configure the private IPs in the CVM as well before they can take effect.

### Assigning Private IP (In the CVM System)

There are two ways to configure private IPs in CVMs. The example below is based on centos 7.2.

**Method 1**

1) Log in to the CVM as administrator.

2) Execute command

`ip addr add [ip/mask] dev [ifname]` 

Example: If you wish to add the IP "192.168.0.5" within subnet 192.168.0.0/24 for the ENI "eth0" of the CVM, execute the command

 `ip addr add 192.168.0.5/24 dev eth0`

3) The private IP is configured.

Note: Private IPs configured in this way are only written in the system memory of the CVM, they will disappear if the CVM restarts, in which case you will need to configure again.

**Method 2**

1) Log in to the CVM as administrator.

2) Execute the following command

`cd /etc/sysconfig/network-scripts/`

`ls`

3) Find the ENI name from the list. Take Tencent Cloud centos 7.2 CVM as an example: If you need to bind private IP for an ENI named "ifcfg-eth0", execute the vim command to open the configuration file of this ENI

`vim ifcfg-eth0`

The original system configuration file is:

`DEVICE='eth0'`

`MM_CONTROLLED='yes'`

`ONBOOT='yes'`

`IPADDR='192.168.0.3'`

`NETMASK='255.255.255.0'`

`GATEWAY='192.168.0.1'`

Change the configuration into:

`DEVICE='eth0'`

`MM_CONTROLLED='yes'`

`ONBOOT='yes'`

`IPADDR0='192.168.0.3'`

`IPADDR1='192.168.0.5'`

`NETMASK='255.255.255.0'`

`GATEWAY='192.168.0.1'`

Save the modified configuration file and exit vim.

4) Restart ENI

`systemctl restart network`

Check whether the IP address has been added into ENI "eth0"

`ip addr`

5) The private IP binding process is finished.

Note: Private IPs configured in this way will still be in effect after the CVM restarts. But if you create a custom image of this CVM and use the image to create other CVMs, you will need to manually update private IP configurations for those CVMs.

### Releasing Private IP

1) Open the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the page with a list of ENIs.

3) Click the "Instance ID" of the ENI to go to its detail page and view its information.

4) Click "IP Management" tab to view the private IPs and elastic public IPs that are already bound to the ENI.

5) Click "Release" button from the action bar of the private IP line.

6) Click "OK" to complete the operation.

Note 1: You can only release secondary IPs of ENIs, but not the primary one.

Note 2: Once the private IP is unbound, the elastic public IP will be automatically disassociated.

### Binding Elastic Public IP

1) Open the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click **ENI** in the left panel to go to the page with a list of ENIs.

3) Click the **Instance ID** of the ENI to go to its detail page and view its information.

4) Click **IP Management** tab to view the private IPs that are already bound to the ENI.

5) Click "Bind" button in the "Bound Elastic Public IP" column of the line to which the private IP belongs.

6) Select to bind an IP from the "Existing Elastic IP" list, or "Create Elastic IP", from the pop-up window.

7) Click "OK" to complete the binding process.

### Unbinding Elastic Public IP

1) Open the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the page with a list of ENIs.

3) Click the "Instance ID" of the ENI to go to its detail page and view its information.

4) Click "IP Management" tab to view the private IPs and elastic public IPs that are already bound to the ENI.

5) Click "Unbind" button in the "Bound Elastic Public IP" column of the line to which the private IP belongs.

6) Click "OK" to complete the unbinding process.

### Modifying the Primary Private IP

1) Open the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the page with a list of ENIs.

3) Click the "Instance ID" of the ENI to go to its detail page and view its information.

4) Click "IP Management" tab to view the primary private IP that is already bound to the ENI.

5) Click "Modify Main IP" button in the action bar for the line of the primary private IP.

6) Enter the new primary private IP in the pop-up window and click "OK" to modify.

### Modifying ENI's Subnet

1) Open the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to go to the page with a list of ENIs.

3) Click the "Instance ID" of the ENI to go to its detail page.

4) In the basic information page of the detail page, click "Change Subnet" button.

5) Select the subnet to change to for the ENI and specify a new primary IP.

6) Click "Save" to finish the subnet changing process.

Note 1: You can only change subnet for the primary ENI.

Note 2: You must unbind all secondary IPs before you can change subnet for the ENI.

Note 3: When changing subnet for the ENI, you can only choose another subnet under the same availability zone.

## API Overview
Refer to [Overview of All VPC APIs](https://cloud.tencent.com/doc/api/245/909) for more information about other VPC resources.

