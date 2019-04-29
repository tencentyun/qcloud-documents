The CVM instance described below also refers to dedicated CVM.

Elastic network interface (ENI) is a virtual network API. You can bind an ENI to a CVM and connect it to the network. ENI is very useful when you configure management networks and establish highly reliable network solutions.

ENI has VPC, availability zone and subnet attributes. You can only bind it to CVMs under the same availability zone. Each CVM may have multiple ENIs bound to it. The allowed number depends on the specifications of the CVM.

## Basic Information

The ENI has the following relevant information:

1. Primary ENI or secondary ENI: The ENI that was created when creating the CVM within the VPC is the primary ENI. The ENIs created by the user will be secondary ENIs. You can bind/unbind secondary ENIs but cannot do so with the primary one.

2. Primary private IP: The primary private IP of the ENI is assigned by the system, or specified by the user when the ENI was created. You can modify the primary private IP of the primary ENI, but not that of secondary ENI.

3. Secondary private IP: Secondary private IPs that are bound to the ENI, other than the primary IP, are configured by users when they create or modify the ENI. You can bind/unbind these IPs.

4. EIP: Bound with private IPs of the ENI in a one-to-one correspondence manner.

5. Security group: Each ENI may bind one or multiple security groups.

6. MAC address: Each ENI has a unique global MAC address.

## Usage Restrictions

The number of ENIs that may bind to a CVM and the number of private IPs that can bind to each ENI will greatly vary according to CPU and RAM configuration. Please see below:

| CVM Configuration               | Number of ENIs | Number of IPs for Each ENI |
| ------------------- | :---- | :------ |
| CPU:  Single core   RAM:  1G    | 2     | 2       |
| CPU:  Single core   RAM:  >1G   | 2     | 6       |
| CPU:  Dual core             | 2     | 10      |
| CPU:  4-core   RAM:  < 16G | 4     | 10      |
| CPU:  4-core   RAM:  > 16G | 4     | 20      |
| CPU:  8 to 12 cores          | 6     | 20      |
| CPU:  >12-core           | 8     | 30      |

### Checking ENI

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click the CVM instance ID to access the CVM details page.

3) Click the ENI tab to view information about the ENI bound to the CVM.

## Assigning Private IP (Tencent Cloud Console)

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click the CVM "instance ID" to enter the CVM details page.

3) Click "IP Management" tab to view the private IPs and EIPs that are already bound to the ENI in CVM.

4) Click "Assign Private IP" button to open the "Assign Private IP" window.

5) You can choose to "Auto Assign" or "Manually Enter" private IP.

6) You can click the "Add" button to assign multiple IPs for the ENI in the "Assign Private IP" window.

7) Click "OK" button to complete the assigning process.

Note: You need to configure the private IPs in the CVM as well before they can take effect.

## Assigning Private IP (In the CVM System)

There are two ways to configure private IPs in CVMs. The example below is based on centos 7.2.

**Method 1**

1) Log in to the CVM as an administrator.

2) Execute command

`ip addr add [ip/mask] dev [ifname]` 

Example: If you wish to add the IP "192.168.0.5" within subnet 192.168.0.0/24 for the ENI "eth0" of the CVM, execute the command

 `ip addr add 192.168.0.5/24 dev eth0`

3) The private IP is configured.

Note: Private IPs configured in this way are only written in the system memory of the CVM, they will be in valid if the CVM restarts, in which case you will need to configure again.

**Method 2**

1) Log in to the CVM as an administrator.

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

Check whether the IP has been added into ENI "eth0"

`ip addr`

5) The private IP binding process is finished.

Note: Private IPs configured in this way will still be in effect after the CVM restarts. However, if you create a custom image of this CVM and use the image to create other CVMs, you will need to manually update private IP configurations for those CVMs.

### Releasing Private IP

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click the CVM "instance ID" to enter the CVM details page.

3) Click "IP Management" tab to view the private IPs and EIPs that are already bound to the ENI in CVM.

4) Click "Release" button from the action bar of the private IP line.

5) Click "OK" to complete the operation.

Note 1: You can only release secondary IPs of ENIs, but not the primary one.

Note 2: Once the private IP is unbound, the EIP will be automatically disassociated.

## Binding EIP

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click the CVM "instance ID" to enter the CVM details page.

3) Click "IP Management" tab to view the private IPs that are already bound to the ENI in CVM.

4) Click "Bind" button in the "Bound EIPs" column of the line to which the private IP belongs.

5) In the pop-up window, select to bind an IP from the "Existing EIPs" list or "Create EIP".

6) Click "OK" to complete the binding process.

## Unbinding EIP

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click the CVM "instance ID" to enter the CVM details page.

3) Click "IP Management" tab to view the private IPs and EIPs that are already bound to the ENI in CVM.

4) Click "Unbind" button in the "Bound EIPs" column of the line to which the private IP belongs.

5) Click "OK" to complete the unbinding process.

### Modifying the Primary Private IP

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click the CVM "instance ID" to enter the CVM details page.

3) Click "IP Management" tab to view the private IPs of the ENI in CVM.

4) Click "Modify Main IP" button in the action bar for the line of the primary private IP.

5) Enter the new primary private IP in the pop-up window and click "OK" to modify.

### Modifying the Subnet of ENI

1) Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).

2) Click "ENI" in the left panel to enter ENI List page.

3) Click the "Instance ID" of the ENI to enter ENI Details page.

4) In the basic information page of the ENI Details page, click "Replace" button for the subnet.

5) In the pop-up window, select the subnet to be replaced and specify the new primary IP.

6) Click "Save" to finish the subnet replacement process.

Note 1: You can only modify the subnet of the primary ENI.

Note 2: You must unbind all secondary IPs before you can modify the subnet of ENI.

Note 3: When modifying the subnet of ENI, you can only choose another subnet under the same availability zone.

## Creating, binding and unbinding ENI

Currently, ENI cannot be created, bound or unbound in the console. This feature will become available soon.
