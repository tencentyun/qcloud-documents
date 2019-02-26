## Overview
NAT gateway provides the capability to translate between private IPs and public IPs in VPC. It is an ingress/egress for public network traffic in VPC. The NAT gateway of Tencent Cloud VPC is used in the following typical scenarios:
- **Public network access with large bandwidth and high availability.** Tencent Cloud NAT gateway can meet users' demands for public network access that requires ultra-large bandwidth, massive use of public IPs, and a large number of services to be deployed.
- **Secure public network access.** The NAT gateway of Tencent Cloud VPC provides secure IP translation. If you want to hide the public IP of the CVM in the VPC to avoid exposing its network deployment while expecting to communicate with the public network, you can use Tencent Cloud NAT gateway.

## Network Topology
As shown in the figure below, the NAT gateway resides on the boundary between the Internet and the VPC, and is connected to the router on the VPC. In such a topology, when resources like CVM in the VPC send data packets outwards via the NAT gateway, the data first passes through the router and makes routing selection based on routing policies. Then, the NAT gateway sends traffic to the Internet through the bound EIP as the source IP:

![](https://mc.qcloudimg.com/static/img/32593cb6e9930b0126889b5a15eb2dc9/image.png)


## Features
- The NAT gateway supports SNAT and DNAT:
 - SNAT: Source network address translation. It allows multiple VPC CVMs to actively access the Internet through the same public IP.
 - DNAT: Destination network address translation (which is under internal trial. Submit a [Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=168&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC), if necessary). It is used to map [private IPs, protocols and ports] of the CVM in the VPC into [public IPs, protocols and ports], so that services on the CVM can be accessed from the public network.
 
- The NAT gateway supports high defense services:
BGP high defense provides ultra-large bandwidth DDoS and CC defense for Tencent Cloud users, with a capacity of up to 310 Gbps. You can bind the high defense package to the NAT gateway that requires defense for security protection.


## Difference between NAT Gateway and Public Network Gateway
Both NAT gateway and public network gateway are used for the CVM in the VPC to access the Internet. Differences between these two gateways are shown below:

| Attribute | NAT Gateway | Public Network Gateway |
|---------|---------|---------|
| Availability	| Master/slave hot backup, automatic hot switching |	Switch the failed gateway manually |
| Public network bandwidth	| Maximum is 5 Gbps	| Depend on the network bandwidth of CVM |
| Public IP	| A maximum of 10 EIPs can be bound |	One EIP or ordinary public IP |
| Rate limit of public network	| N/A |	Depend on the rate limit of CVM |
| Maximum number of connections	| 10m |	500k |
| Private IP	| Private IPs of VPC users are not occupied |	Private IPs of the subnet are occupied |
| Security group |	Binding of security group is not supported. You can bind the security group to the NAT gateway backend CVM	| Support |
| Network ACL |	Binding of network ACL is not supported. You can bind the network ACL to the subnet in which the NAT gateway backend CVM resides	| Binding of network ACL is not supported. You can bind the network ACL to the subnet to which the public network gateway belongs |
| Charges	| Mainland China:<br> Small (a maximum of 1m connections): 0.5 CNY/hr<br> Medium (a maximum of 3m connections): 1.5 CNY/hr <br>Large (a maximum of 10m connections): 5 CNY/hr | Depend on the size of CVM used as a public network gateway. Take Mainland China as an example: <br>1-core 2 GB: 0.44 CNY/hr <br>4-core 8 GB: 1.76 CNY/hr <br>12-core 24 GB: 5.28 CNY/hr |

The comparisons listed above show that Tencent Cloud NAT gateway has three advantages:
- Large capacity: It supports a maximum of 10m concurrent connections, 5 Gbps bandwidth and 10 EIPs to meet the demand of users with a large business scale.
- Highly available master/slave hot backup: Automatically switch when a single server suffers a failure to allow automatic disaster recovery and 99.99% service availability, superior to the manual switch of a public network gateway.
- Cost effectiveness: Three configuration types, high, medium and low, are available for users to choose from as needed, offering flexibility in billing and high cost effectiveness.

## Configuration Types
The NAT gateway supports binding up to 10 EIPs, and a maximum of 5 Gbps traffic surge and 10m concurrent connections, while providing three configuration types.

- Small (max. 1m connections)
- Medium (max. 3m connections) 
- Large (max. 10m connections)

Available values for maximum public network outbound bandwidth of NAT gateway (in Mbps): 10, 20, 50, 100, 200, 500, 1000, 2000, and 5000.

## How to Use NAT Gateway and EIP

NAT gateway and EIP are two ways for the CVM to access the Internet. You can use either one of them or both of them to design your public network access architecture.

### Method 1: Use NAT Gateway Only
The CVM is not bound to an EIP, and all the traffic for accessing the Internet is forwarded via the NAT gateway. In this way, the CVM traffic for accessing the Internet is forwarded to the NAT gateway via the private network. This means that the traffic is not restricted by the upper limit of public network bandwidth specified when you purchase the CVM, and the traffic generated from the NAT gateway doesn't occupy the public network bandwidth egress of the CVM.

### Method 2: Use EIP Only
CVM is only bound with EIP, instead of using NAT gateway. With this solution, all the traffic of the CVM accessing the Internet flows via the EIP and is restricted by the upper limit of public network bandwidth specified when you purchase the CVM. The fees for accessing the public network depends on the billing method of the CVM's network.

### Method 3: Use Both NAT gateway and EIP
The CVM is bound to an EIP, and the traffic of the subnet route for accessing the Internet is directed to the NAT gateway. In this way, all the traffic of the CVM for accessing the Internet is **forwarded to the NAT gateway via the private network only**, and the response packets are returned to the CVM via the NAT gateway. This means that the traffic is not restricted by the upper limit of public network bandwidth specified when you purchase the CVM, and the traffic generated from the NAT gateway does not occupy the public network bandwidth outlet of the CVM. If the traffic from the Internet accesses the EIP of the CVM, the response packets of the CVM are all returned through the EIP. In this case, the resulting outbound traffic of the public network is restricted by the upper limit of public network bandwidth specified when you purchase the CVM. The fees for accessing the public network depend on the billing method of the CVM's network.

> **Note:**
For the accounts with a bandwidth package for bandwidth sharing, the fee for the outbound traffic from NAT gateway is covered by the bandwidth package (the network traffic fee of 0.8 CNY/GB is not charged additionally). You're recommended to set a limit on the outbound bandwidth of the NAT gateway, so as to avoid a high bandwidth package fee due to the excessive use of outbound bandwidth of NAT gateway.

## Key Features
The followings are some key features of NAT gateway:
- SNAT: Source network address translation. It allows multiple VPC CVMs to actively access the Internet through the same public IP.
- DNAT: Destination network address translation. It is used to map [private IPs, protocols and ports] of the CVM in the VPC into [public IPs, protocols and ports], so that services on the CVM can be accessed from the public network.
- High performance: NAT gateway supports forwarding up to 5 Gbps of data to a single instance.
- High availability: NAT gateway provides master/slave hot backup to switch automatically when a single server suffers a failure, without affecting your use of services.
- Monitoring details display: All the key metrics for private IPs flowing to the NAT gateway are displayed, to help you implement rapid troubleshooting and exceptional traffic location. The monitoring details data can be kept for 7 days. 
- Refined gateway traffic control: The bandwidth between a private IP and the NAT gateway can be limited to guarantee key businesses.

## NAT Gateway Traffic Control
NAT gateway traffic control provides the "monitoring" and "controlling" capabilities at **IP-gateway** granularity. Refined gateway traffic visualization enables network OPS personnel to get a clear picture of the traffic in the gateway. The speed restricting capability at IP-gateway granularity helps block exceptional traffic.
For example, in the early morning of one day, the gateway traffic of a company surges. With intelligent gateway traffic control, the OPS personnel can trace data to find which IPs cause this traffic surge according to the time when the traffic surge occurs, so as to rapidly locate its source. In addition, the gateway traffic control provides bandwidth control based on IP-gateway granularity, which can restrict the bandwidth from an IP to the gateway and block exceptional traffic to guarantee key businesses.

The advantages of gateway traffic control are as follows:
- Featured with the capability for accurate gateway troubleshooting, it can minimize the network failure time. It can also analyze the source IP and its key metrics by combining real-time traffic query and TOP N ranking features, to rapidly locate the exceptional traffic.
- With "monitoring" and "controlling" capabilities based on IP-gateway granularity and by using the minute-level network traffic query, it can find the exceptional traffic that maliciously occupies the bandwidth in real time, and set bandwidth limits at IP-gateway granularity, so as to guarantee the stable operation of core businesses.
- It has full-time and full-traffic gateway traffic analysis capability, to help reduce cloud network cost. It controls the cost through qos, thus restricting the bandwidth of non-key businesses to reduce cost in case of limited network budget.


## Service Limits
When you use the NAT gateway, note the followings:
- If the NAT gateway is deleted, its EIP is disassociated from it, but not released from the account.
- Although the NAT gateway cannot be associated with security groups, they can be used for the instances in the private subnet to control the traffic that flows in and out of these instances.
- You cannot use the network ACL to control the traffic that flows in and out of the NAT gateway, but you can use it to control the traffic of the associated subnet that flows in and out of the NAT gateway.
- Users can not use VPC peering connection, VPN connection or direct connection to route traffic to the NAT gateway which cannot be used for these resources that are connected to the other end. For example, all the traffic of VPC 1 can be sent to the Internet through the NAT gateway. Since a peering connection has been established between VPC 1 and VPC 2, all the resources within VPC 2 can access all the resources within VPC 1, but no resources within VPC 2 can access the Internet through the NAT gateway.
- Supported protocols for the NAT gateway include TCP, UDP and ICMP, while ESP and AH for the GRE tunnel and IPSec cannot be used for the NAT gateway. This is a result of the characteristics of the NAT gateway itself, which has nothing to do with the service provider. Luckily, TCP is a dominant type of application in the Internet world, and, together with UDP, accounts for 99% of all Internet applications.
- For more information about the restrictions on the supported resources for the NAT gateway, please see [Service Limits of Other VPC Products](https://cloud.tencent.com/doc/product/215/537).

| Resource | Limit | 
|---------|---------|
| Number of NAT gateways per VPC | 3 | 
| Number of EIPs per NAT gateway | 10 |
| Maximum forwarding capacity per NAT gateway | 5 Gbps |

## Billing Method

Charges for a NAT gateway device include two parts: Gateway rental fee (by hour) and the fee for traffic generated during the access to the Internet. The cost for the traffic can be charged as per the "Bill by Traffic" method for CVM network charges. The billing mode for the NAT gateway itself is as follows:
 
 <table class="cvmMonth">
         <tbody><tr>
             <th style="width: 10%;" rowspan="2">Feature</th>
             <th style="width: 10%;" rowspan="2">Billing Model</th>
                         <th style="width: 30%;" rowspan="2">Configuration</th>
             <th style="width: 50%;" colspan="7">Price</th>
         </tr>
         <tr>
             <th>Beijing<br>Shanghai<br>Guangzhou</th>
                         <th>Hong Kong</th>
                                                  <th>Singapore</th>
             <th>Toronto</th> 
 	<th>Korea</th> 
 		<th>Frankfurt</th>
 			<th>Silicon Valley</th>
         </tr>
 
         <tr>
         
                 
                                 <tr>
             <td rowspan="4">NAT Gateway</td>
             <td rowspan="3">Rental fee for gateway<br>(USD/hour)</td>
             <td>Small</td>
             <td>0.089</td>
             <td>0.13</td>
                                     <td>0.13</td>
                         <td>0.14</td>
 			<td>0.13</td>
             <td>0.13</td>
             <td>0.13</td>
         </tr>
                 <tr>
             <td>Medium</td>
             <td>0.28</td>
             <td>0.39</td>
                         <td>0.39</td>
                         <td>0.42</td>
 			<td>0.39</td>
             <td>0.39</td>
 			<td>0.39</td>
         </tr>
                 <tr>
             <td>Large</td>
             <td>0.89</td>
             <td>1.3</td>
                         <td>1.3</td>
                         <td>1.4</td>
 			<td>1.3</td>
 			<td>1.3</td>
 			<td>1.3</td>
         </tr>
               
         </tr>
 
                     
                 
     </tbody></table>
 
 
 
  >Note:
  For users with a Bandwidth Package for bandwidth sharing, the outbound traffic generated at the NAT gateway will be billed as per the Bandwidth Package (the USD 0.12/GB network traffic fee will not be charged separately). It's recommended that you set a limit on the outbound bandwidth of the NAT gateway, so as to avoid any high Bandwidth Package charge due to excessively high amount of such bandwidth. Click to view the [Bandwidth Package billing details](https://cloud.tencent.com/doc/product/213/%E8%B4%AD%E4%B9%B0%E7%BD%91%E7%BB%9C%E5%B8%A6%E5%AE%BD#.E5.B8.A6.E5.AE.BD.E5.8C.85.E8.AE.A1.E8.B4.B9)
 Arrear logic: be consistent with the Bill by Traffic method for CVM. [Click to obtain the VPC Price Overview](https://cloud.tencent.com/doc/product/215/3079)

## Expiry Reminder
- In the event of insufficient balance in your account. Starting from the moment your account balance becomes 0, you can use the NAT gateway for a further period of **2** hours with the usage being further billed.
- If your account balance fails to be topped up to an amount greater than 0 after 2 hours, the NAT gateway service is automatically suspended and the billing is stopped.
- The NAT gateway remains unavailable until your account balance is topped up to an amount greater than 0 within 24 hours after the suspense of the service. When your account balance has been topped up to an amount greater than 0, the gateway becomes available and the billing starts over again.
- When your account balance has remained below 0 for 24 hours after the suspense of NAT gateway service, the NAT gateway is reclaimed immediately.
- The Tencent Cloud account creator and all the collaborators are notified of the reclaim via email and SMS.

## Operation Instructions
If you want to allow the resources within the subnet of a VPC to access the Internet through an NAT gateway, you need not only to create the NAT gateway, but also to configure the routing rules in the routing table with which the subnet that needs route forwarding is associated.

## Quick Start
You can access the Internet through an NAT gateway by following the steps below:
#### Step 1: Create NAT Gateway
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), select "Virtual Private Cloud" tab, and then select "NAT Gateway".
2. Click the "New" button at the upper left corner, and enter or specify the following parameters in the pop-up box:
 - Gateway name
 - Gateway type (which can be changed after creation)
 - VPC of NAT gateway service
 - Assign an EIP to NAT gateway. You can choose an existing EIP, or purchase and assign a new EIP.
3. After selection, click "OK" to complete the creation of NAT gateway.
4. After the creation of the NAT gateway, you need to configure the routing rules on the Routing Table page of the VPC Console to direct the subnet traffic to the NAT gateway.
>**Note:**
The rental fee will be frozen for 1 hour during the creation of NAT gateway.


#### Step 2: Configure the Routing Table Associated with the Subnet
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "Routing Table".
2. In the routing table list, click the ID of the routing table associated to the subnet that needs to access the Internet to go to the details page of the routing table, and then click "Edit" button in the "Routing Policies".
3. Click "New line", enter the "Destination" field, select "NAT Gateway" in "Next Hop Type", and select the ID of the created NAT gateway.
4. Click "OK". After the configuration, the traffic generated when the CVM in the subnet associated with the routing table accesses the Internet is directed to the NAT gateway.


### Creating Port Forwarding Rule
The port forwarding table is a configuration table on the NAT gateway, which is used to configure the DNAT feature on the NAT gateway. It map [private IPs, protocols and ports] of the CVM in the VPC into [public IPs, protocols and ports], so that services on the CVM can be accessed from the public network. (It is under internal trial. Submit a [Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=168&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC), if necessary).
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "NAT Gateway".
2. In the NAT gateway list page, click the ID of the NAT gateway to be modified to go to its details page, and select "Port Forwarding".
3. Click "New", and select the protocol, external IP port and internal IP port.

>**Note:**
The internal IP only supports the private IP of the CVM in this VPC.

![](https://mc.qcloudimg.com/static/img/ce676bb705b873413de907e94aa124d0/1.png)


### Querying Port Forwarding Rule

1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "NAT Gateway".
2. In the NAT gateway list page, click the ID of the NAT gateway to be modified to go to its details page, and select "Port Forwarding".
3. In the search box, select the protocol\IP\port, and enter related attribute values to query related port forwarding rules.



### Modifying NAT Gateway Configuration
You can modify the attributes of a created NAT gateway.
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "NAT Gateway".
2. In the NAT gateway list page, click the ID of the NAT gateway to be modified to go to its details page, where you can make modifications to the following attributes:
 - Change the custom name of NAT gateway
 - Change the NAT gateway specifications. Specification changes take effect immediately (the network connection is not broken)

### Managing EIPs bound to the NAT Gateway
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "NAT Gateway".
2. In the NAT gateway list page, click the NAT gateway ID to go to its details page.
3. In the list of associated EIPs, you can "Add" or "Unbind" an EIP.

### Viewing Monitoring Information of NAT Gateway
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "NAT Gateway".
2. In the NAT gateway list page, click the "Monitor" button in an NAT gateway entry to view its monitoring information.
(Alternatively) In the NAT gateway list page, click the ID of an NAT gateway to go to its details page, and then click "Monitoring" tab to view its monitoring information.

### Setting the Alarm
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Products" -> "Monitor & Management" -> ["Cloud Monitor"](https://console.cloud.tencent.com/monitor/overview) in the top navigation bar, and select "My Alarms" -> ["Alarm Policy"](https://console.cloud.tencent.com/monitor/policylist) in the left navigation bar, and then click "Add Alarm Policy".
2. Enter the alarm "Policy Name", select "NAT Gateway" in "Policy Type", and then add alarm triggering condition.
3. **Associate alarm objects**: Select the alarm receiver group, and when it is saved, you can view the set alarm polices in Policy List.
4. **View the alarm information**: When the alarm is triggered, you can receive a notification sent via SMS/email/internal message. You can also view it in "My Alarms" -> "Alarm List" in the left navigation bar. For more information, please see [Create Alarms](https://cloud.tencent.com/doc/product/248/1073).

### Deleting NAT Gateway
NAT Gateway can be deleted when it is not needed. The routing table and routing rules containing the NAT gateway is deleted with the NAT gateway. Upon the deletion, the request forwarded over Internet is interrupted immediately. Be prepared for the network interruption in advance.
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "NAT Gateway".
2. Select the NAT gateway to be deleted, click "Delete" button and confirm the action, and then the NAT gateway is deleted.

### Enabling Gateway Traffic Control Details
After it is enabled, you can view the metrics of IP traffic passing through an NAT gateway over the last 7 days, and also set the outbound bandwidth for an IP to flow to a specific NAT gateway.
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "NAT Gateway".
2. In the NAT gateway list page, click the NAT gateway ID to go to its details page.
3. Click the "Monitor" tab, and enable the switch of "Gateway Traffic Control Details" on the upper right corner.
After the Gateway Traffic Control Details are enabled, it takes 5 to 6 days to collect and publish data. During this period, you can view the monitoring details table at the lower part of the monitoring chart.


>**Note:**
This feature is under internal trial. Submit a ticket to apply for it.


### Setting Gateway Traffic Control Details
After Gateway Traffic Control Details is enabled, you can set the outbound bandwidth for an IP to flow to a specific NAT gateway.
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "NAT Gateway".
2. In the NAT gateway list page, click the NAT gateway ID to go to its details page.
3. Click the "Monitor" tab, find the IP for which monitoring details need to be set, and set a limit on its outbound bandwidth.

### Viewing Gateway Traffic Control Details
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "NAT Gateway".
2. In the NAT gateway list page, click the NAT gateway ID to go to its details page.
3. Click the "Monitor" tab, and then click "View Restricted IP" in the upper right of the gateway traffic control details table.

### Binding High Defense Package
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Security" -> "Dayu Distributed Defense" in the navigation bar, and select ["BGP High Defense Package"](https://console.cloud.tencent.com/dayu/bgp/list/sp/gz) on the left navigation bar.
2. Select an existing high defense package instance, click "Change Device" and select the EIP on the NAT gateway that needs to be used repeatedly.
3. Click "OK" to associate the high defense package feature to this NAT gateway.

## API Overview
You can use APIs to configure and manage your NAT gateway. For more information about other VPC resources, please see [Overview of All VPC APIs](https://cloud.tencent.com/doc/api/245/909).

| Feature | Action ID | Description |
|---------|---------|---------|
| Create NAT Gateway | [CreateNatGateway](https://cloud.tencent.com/doc/api/245/4094) | Create an NAT gateway. |
| Query NAT gateway creation status | [QueryNatGatewayProductionStatus](https://cloud.tencent.com/doc/api/245/4089) |  Query the creation status of an NAT gateway. |
| Delete NAT gateway | [DeleteNatGateway](https://cloud.tencent.com/doc/api/245/4087) | Delete an NAT gateway. |
| Modify NAT gateway | [ModifyNatGateway](https://cloud.tencent.com/doc/api/245/4086) | Modify an NAT gateway. |
| Query NAT gateway | [DescribeNatGateway](https://cloud.tencent.com/doc/api/245/4088) | Query an NAT gateway. |
| Bind EIP for NAT gateway | [EipBindNatGateway](https://cloud.tencent.com/doc/api/245/4093) | Bind an EIP for an NAT gateway. |
| Unbind EIP for NAT gateway | [EipUnBindNatGateway](https://cloud.tencent.com/doc/api/245/4092) | Unbind an EIP for an NAT gateway. |
| Upgrade NAT gateway specifications | [CreateNatGateway](https://cloud.tencent.com/doc/api/245/4090) | Upgrade the specifications of an NAT gateway. |

