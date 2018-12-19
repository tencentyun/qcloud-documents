An elastic network interface （ENI）is a virtual network interface, you can bind the CVM with the ENI to gain access. ENI offerS great assistance in the configuration and management of a network, as well as building highly reliable network solutions.

ENIs use a private network, with a private area and subnet properties; they can only bind CVMs within the same availability zone. A CVM can bind multiple ENIs, the specific number of bindings will be based on CVM specifications.

## Basic info

The ENI mainly has the following associated information:

1. Primary ENI and secondary ENI: When the CVM of the private network is created, the ENI created by the linkage is the main ENI. The ENI that the user created will be used as the secondary ENI; you cannot bind/unbind the main ENI, but can do so with the secondary one.

2. Main private network IP: ENI's primary IP; when an ENI is created. it is either randomly assigned by the system or created by the user. For a primary ENI, the primary private IP can be modified. But for a secondary ENI, the primary private IP cannot be modifed.

3. Secondary private IP: a secondary network IP that is bound, in addition to the main IP, to the ENI. It is automatically configured by the user when creating or editing an ENI, and supports binding/unbinding.

4. Elastic public network IP: binds with private IPs on the ENI one at a time.

5. Security groups: ENIs can be bound to one or more security groups.

6. MAC Address: Each ENI has a globally unique MAC address.

## Restrictions on use

According to CPU and memory configurations, the number of ENIs and IPs per ENI that a CVM can bind vary greatly. Please see below:

| CVM Configuration | ENIs | IPs per ENI |
| ------------------- | :---- | :------ |
| CPU: 1 core  memory: 1G    | 2     | 2       |
| CPU: 1 core  memory: >1G   | 2     | 6       |
| CPU: 2 cores             | 2     | 10      |
| CPU: 4 cores  memory: < 16G | 4     | 10      |
| CPU: 4 cores  memory: > 16G | 4     | 20      |
| CPU: 8~12 cores          | 6     | 20      |
| CPU: >12 cores           | 8     | 30      |


## Operation Guide
### Check ENIs

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Click the CVM instance ID to access the CVM details page.

3) Click the ENI tab to view information about the elastic network adapter bound to the CVM.

### Create ENIs

A primary ENI will be created automatically when you create a CVM. The primary ENI cannot be bound and unbound. 

To create a new ENI, please do the followings:

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Find the desired CVM via the ID

3) In the operation column, select "More - ENI - Bind ENI"

4) Select "New ENI" in the pop-up window

5) Enter data of the ENI and click "OK"

## Bind elastic public IPs

Method 1:

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Click the CVM instance ID to access the CVM details page.

3) Click the "ENI - Bind an ENI".
4) In the pop-up list, select ENIs in the same VPC and the **same availability zone**

5) Click "Confirm" to complete

Method 2:

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Find the desired CVM via the ID

3) In the operation column, select "More - Elastic Network Cards-Bind Elastic Network Cards"

4) In the pop-up list, select elastic network card in the same VPC and the **same availability zone**

5) Click "Confirm" to complete

Tip 1: A CVM can only be bound with ENIs in the same VPC and availability zone

Tip 2: There're upper limits for bound ENIs. Please check the Usage Restriction section for details

### Unbind ENIs

Method 1:

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Click the CVM instance ID to access the CVM details page.

3) Click the ENI tab and select the desired ENI

4) Click "Unbind" to complete

Method 2:

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Find the desired CVM via the ID

3) In the operation column, select "More - Elastic Network Cards-Unbind Elastic Network Cards"

4) Click "Confirm" to complete

### Assign private IP (Tencent Cloud console)

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Click the CVM [Instance ID] to access the CVM details page.

3) Click the [Elastic Network Card tab] to view the bound IP and elastic public network IP of the elastic host network card.

4) Click the [Assign Private IP] button and a "Assign Private IP" window will pop up.

5) You can select either to "Auto Assign" or "Fill in Manually" for the private IP.

6) You can click the [Add] button to assign multiple IP addresses to the elastic network card in the "Assign Private IP" window.

7) Click the [Finish] button to use the console to assign private IPs.

Note: The private IP needs to be configured on the CVM before taking effect.
## Assign private IP (CVM system)
There are two ways to configure private IPs on the CVM. Here, centos 7.2 is used as an example to demonstrate the configuration process.

** Method 1 **

1) Log onto the CVM as an administrator.

2) Execute command

`ip addr add [ip/mask] dev [ifname]` 

Example: the CVM's network card eth0 needs to add subnet 192.168.0.0/24 IP 192.168.0.5, then just execute the command

 `ip addr add 192.168.0.5/24 dev eth0`

3) Private IP configuration complete.

Note: This way the configuration of the private network IP is only written on the CVM system memory; after the CVM is restarted, the private network IP will be invalid, and will need to be reconfigured.

** Method 2 **

1) Log onto the CVM as an administrator.

2) Execute below command

`cd /etc/sysconfig/network-scripts/`

`ls`

3) On the list, find the network card name; using Tencent Cloud centos 7.2 CVM as an example, you need to bind the network card's private IP with the name "ifcfg-eth0"; then you can execute the command "vim" to open the network card configuration file.

`vim ifcfg-eth0`

The original system configuration file is:

`DEVICE='eth0'`

`MM_CONTROLLED='yes'`

`ONBOOT='yes'`

`IPADDR='192.168.0.3'`

`NETMASK='255.255.255.0'`

`GATEWAY='192.168.0.1'`

Modified to:

`DEVICE='eth0'`

`MM_CONTROLLED='yes'`

`ONBOOT='yes'`

`IPADDR0='192.168.0.3'`

`IPADDR1='192.168.0.5'`

`NETMASK='255.255.255.0'`

`GATEWAY='192.168.0.1'`

Save the configuration file after modifying and exit vim.

4) Restart network card

`systemctl restart network`

Check whether the eth0 card has joined the IP address

`ip addr`

5) Complete private network IP binding.

Note: The private network IP configured in this way will still take effect after the CVM restarts. However, if you make a custom mirror for this CVM, the other private IPs created by this image will need to be updated.

### Release private IP

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Click the CVM [Instance ID] to access the CVM details page.

3) Click the [Elastic Network Card tab] to view the bound IP and elastic public network IP of the elastic host network card.

4) Click the [Release] button on the bar next to the private IP.

5) Click [OK] to complete the action.

Note 1: The elastic network card's primary IP does not support release, only the secondary IP supports release.

Note 2: After the private IP is unbound, it will automatically disassociate from the elastic public network IP.

### Bind EIP

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Click the CVM [Instance ID] to access the CVM details page.

3) Click the [Elastic Network Card tab] to view the private IP that is already bound to the cloud host's elastic network card.

4) Click the [Bind] button on the already bound elastic public network IP list, on the same line where the private IP is.

5) In the pop-up window, select to bind an IP from the [Existing Elastic IPs] list or [Create New Elastic IP].

6) Click the [OK] button, to complete binding with elastic IP.

### Unbind EIP

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Click the CVM [Instance ID] to access the CVM details page.

3) Click the [Elastic Network Card tab] to view the bound IP and elastic public network IP of the elastic host network card.

4) Click the [Unbind] button on the already bound elastic public network IP list, on the same line where the private IP is.

5) Click the [OK] button, to complete unbinding with elastic public IP.

### Change primary private IP

1) Open [CVM console](https://console.cloud.tencent.com/cvm).

2) Click the CVM [Instance ID] to access the CVM details page.

3) Click the [Elastic Network Card tab] to view the main private IP of the cloud host elastic network card.

4) Click the [Modify Main IP] button that is in the list next to the main private IP.

5) In the pop-up window, enter the new main network IP, and click [OK] to complete the modification.

### Change subnet of ENI

1) Open [Private network VPC console](https://console.cloud.tencent.com/vpc).

2) Click [Elastic Network Card] in the left column to enter the Elastic Network Card List page.

3) Click the elastic network card's [Instance ID] to enter the Elastic Network Card Details page.

4) On the Basic Information page of the Elastic Network Card Details page, click the [Replace] button for the subnet.

5) In the pop-up window, select the subnet to be replaced and specify the new primary IP.

6) Click the [Save] button to complete the subnet replacement of the elastic network card.

> Note:
> 
1. You can only change subnet of the primary network card
2. Before changing the subnet of an elastic network card, unbind all secondary IPs.
3. When modifying the subnet of an elastic network card, you can only change it to other subnets under the availability zone.

