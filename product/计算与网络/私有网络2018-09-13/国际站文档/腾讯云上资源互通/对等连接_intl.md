## Overview
VPC peering connection is a cross-VPC network interconnection service for office data synchronization that allows VPC IPs to route traffic between peer VPCs as if they belong to the same network. The interconnection between VPCs of the same or different users in the same or different regions can be achieved. You can also achieve traffic interconnection between different VPCs by configuring routing policies on both ends. Peering connections do not depend on a single piece of hardware, so no single point of failure or bandwidth bottleneck exists.
Cross-region interconnections include: VPC cross-region interconnections (the cross-region peering connections) and basic network cross-region interconnections (you need to submit a [Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=168&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC) to apply for it).

> Note: Click to view [Cross-region Connection Service Agreement](https://cloud.tencent.com/document/product/215/7682). If any infringement of this agreement is identified, Tencent Cloud may at any time restrict, suspend or terminate services to you under the agreement as appropriate, and retain the right to pursue related liability.

## Interconnectivity of Peering Connection is Not Transitive
Peering connection allows interconnections between VPCs, but this interconnection is not transitive. As shown below, peering connection is established between VPC 1 and VPC 2, as is done between VPC 1 and VPC 3. However, due to the non-transitivity of peering connection, the traffic interconnection between VPC 2 and VPC 3 cannot be achieved.

![](https://mc.qcloudimg.com/static/img/abb5acd1e173508dc37afbd01c0d8492/VPC-Peer+Connection%281%29.png)
> Note: Even if a peering connection is established, communication cannot be achieved if routes for sending and returning packets are not configured on both ends.


## Intra-region Peering Connections and VPC Cross-region Peering Connections (the VPC Cross-region Interconnections)
VPC supports both intra-region and cross-region peering connections (the cross-region interconnection). As both types of connections are different in physical distance and underlying architecture, they are also different in function and billing method, as shown below:


## Intra-region Peering Connections and VPC Cross-region Peering Connections (the VPC Cross-region Interconnections)
VPC supports both intra-region and cross-region peering connections (the cross-region interconnection). As both types of connections are different in physical distance and underlying architecture, they are also different in function and billing method, as shown below:


| Comparison Item | Intra-region Peering Connection | Cross-region Peering Connection |
|---------|---------|---------|
| Underlying architecture | Local private network within a single region based on Tencent Cloud | Cross-region internal MPLS network based on Tencent Cloud |
| Bandwidth | Interconnection with public cloud supports up to 5 Gbps<br>Interconnection with BM supports up to 1 Gbps | For a maximum of 1 Gbps, the upper limit of bandwidth supports the following configurations (in Mbps):<br>10, 20, 50, 100, 200, 500 and 1,000 |
| Billing Rule | 	Free of charge | 	Daily billing based on the regions where both ends of the peering connection are located and the actually network bandwidth used. For more information, please see [Price Overview](https://cloud.tencent.com/doc/product/215/%E4%BB%B7%E6%A0%BC%E6%80%BB%E8%A7%88) |	
| Availability | Above 99.95%, with no single point of failure | 	Above 99.95%, with no single point of failure |	
| Cross-account connection | Support | Support |	
| Access Permission | CVMs on both ends of a peering connection can access all resources of each other including CVMs, databases, load balancers | CVMs on both ends of a peering connection can access all resources of each other including CVMs, databases, load balancers |	
| Function Limits | VPC IP address ranges to which both ends of a peering connection belong must not overlap; multiple peering connections will not affect one another | VPC IP address ranges to which both ends of a peering connection belong must not overlap; <br><font color="red">if multiple peer VPCs are connected to the same VPC, the IP address ranges that these peer VPCs belong to must not overlap</font> |	

Intra-region peering connection is used primarily to connect applications located in different VPCs within the same region.
The typical application for cross-region peering connection (cross-region interconnection) is **Cross-region disaster recovery**. VPCs within different regions are connected by means of cross-region connection to rapidly deploy a 2-region-3-DC solution for disaster recovery, thus meeting the needs of financial-level network disaster recovery with high bandwidth and reliability.

## Gateway Traffic Control for Peering Connections
Gateway traffic control for peering connections provides the "monitoring" and "controlling" capabilities at **IP-gateway** granularity. Refined gateway traffic visualization enables network OPS personnel to get a clear picture of the traffic in the gateway. The speed restricting capability at IP-gateway granularity helps block exceptional traffic.
For example, in the early morning of one day, the gateway traffic of a company surges. With intelligent gateway traffic control, the OPS personnel can trace data to find which IPs cause this traffic surge according to the time when the traffic surge occurs, so as to rapidly locate its source. In addition, the gateway traffic control provides bandwidth control based on IP-gateway granularity, which can restrict the bandwidth from an IP to the gateway and block exceptional traffic to guarantee key businesses.

The advantages of gateway traffic control are as follows:
- Featured with the capability for accurate gateway troubleshooting, it can minimize the network failure time. It can also analyze the source IP and its key metrics by combining real-time traffic query and TOP N ranking features, to rapidly locate the exceptional traffic.
- With "monitoring" and "controlling" capabilities based on IP-gateway granularity and by using the minute-level network traffic query, it can find the exceptional traffic that maliciously occupies the bandwidth in real time, and set bandwidth limits at IP-gateway granularity, so as to guarantee the stable operation of core businesses.
- It has full-time and full-traffic gateway traffic analysis capability, to help reduce cloud network cost. It controls the cost through qos, thus restricting the bandwidth of non-key businesses to reduce cost in case of limited network budget.


## Workflows

### Workflow for Establishing a Peering Connection
![](https://main.qcloudimg.com/raw/8ccdab3137bbcd16e982130f360ea875.png)

### Workflow for Deleting a Peering Connection
![](https://main.qcloudimg.com/raw/512bd95bc024e945986b3a659df6ef9a.png)

## Service Limits
Please note the following when you use peering connection:
- To enable real communication between both ends of a peering connection, you must configure routing rules in routing tables of both the sending and receiving ends.
- Costs for cross-region peering connection are paid by the requester of such connection.
- If the other party does not accept a peering connection request, the request will automatically expire after 7 days.
- Please do not accept peering connection requests from unknown accounts because they may pose risks to your network.
- The VPC CIDR on both ends of a peering connection cannot overlap, otherwise an error will occur at the time of creation.
- For a cross-region peering connection, the CIDRs of multiple peer networks of one VPC cannot overlap, otherwise an error will occur.
- The peering connection can be interrupted on either end at any time. The communication between two VPCs is terminated immediately upon the interruption.
- There is no bandwidth limit for intra-region peering connection, and a bandwidth limit must be set for across-region peering connections.


| Resource | Limit | Description |
|---------|---------|---------|
| Bandwidth limit for cross-region peering connection | 1 Gbps | If you need a larger bandwidth, submit a ticket. No limit on bandwidth is set for an intra-region peering connection. |

| Number of peering connections supported by each VPC |10 |  | |


> Note: To request for the peering connection in other regions, submit a ticket.

For additional service limits of VPC, please see [Service Limits](https://cloud.tencent.com/document/product/215/537).

## Billing Method
### Billing Method Description
1) Intra-region peering connection is available for free.
2) Cross-region peering connections (the VPC cross-region interconnections) & basic network cross-region interconnections:
- Postpaid on a daily basis. Payment is borne on the peering connection initiator.
- Calculated as the peak bandwidth of the day multiplied by the applicable tiered price.
- Peak bandwidth of the current day is calculated as this: bandwidth is captured once every 5 minutes, and the maximum one out of both inbound and outbound bandwidth of that day is taken as the peak bandwidth.
For more information, please see the following table:



<table class="cvmMonth">
        <tbody>
				<tr>
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
        <td>Intra-region Peering Connection</td>
				<td colspan="9" >                     Free</td>
				<tr>
				<tr>
            <td rowspan="5">Cross-region Peering Connection</td>
						<td rowspan="5">Peak bandwidth of the day Bill by days (USD/Mbps/day) Peak bandwidth is calculated as the average bandwidth every 5 minutes<br></td>
						<td>(0 , 20] Mbps</td>
						<td colspan="1" rowspan="1" align="center">3.19</td>
                         <td colspan="6" rowspan="1" align="center">15</td>

        </tr>
				
				<tr>
				<td>(20 ,100] Mbps</td>

					<td colspan="1" rowspan="1" align="center">1.98</td>
                         <td colspan="6" rowspan="1" align="center">12</td>

				</tr>
				
				<tr>
				<td>(100 , 500] Mbps</td>

			 <td colspan="1" rowspan="1" align="center">1.48</td>
                         <td colspan="6" rowspan="1" align="center">9</td>

				</tr>
				
				<tr>
				<td>(500 , 2000] Mbps</td>

				<td colspan="1" rowspan="1" align="center">1.19</td>
                         <td colspan="6" rowspan="1" align="center">6</td>

				</tr>
				
			 <tr>
				<td >> 2,000 Mbps</td>

					<td colspan="1" rowspan="1" align="center">0.82</td>
                        <td colspan="6" rowspan="1" align="center">5</td>
				</tr>

</tbody></table>

> Contact business department to inquire more about the prices.


For more information about the prices of VPC services, please see [VPC Price Overview](https://intl.cloud.tencent.com/doc/product/215/3079).


>Note:
1. In order for you to view the cost, the billing system describes peering connections as:  bill for cross-region interconnection (mainland) and bill for peering connection of which both ends are in Mainland China
2. Basic network cross-region interconnection is **not supported in the following regions**: Shanghai Finance, Shenzhen Finance and Silicon Valley.



### Free cross-region interconnection bandwidth campaign **(Key customers are entitled to its benefits by default, but it is no longer available to common customers)**
Benefits for VIP customers and common customers during the campaign are as follows:

**VIP customers** (The benefits are entitled to all VIP customers)
- Extra free bandwidth of 100Mbps is offered for each peering connection in Mainland China (automatically assigned by the system).

**Common customers** (The campaign is closed)
- An extra bandwidth of 10 Mbps is offered free of charge for each peering connection in Mainland China.

> Note:
- It takes effect on the day the bandwidth remission is approved upon review. The bandwidth beyond the free quota is billed based on tiered prices. This is valid until December 31, 2017. You can view the remission details in the pop-up window for the creation of peering connection or in the details page.


- **This benefit is not applicable for basic network cross-region interconnection.**


## Operation Instructions

### Quick Start
Cross-region connection and cross-account communication of VPC are both advanced features of peering connection, so you can take the following steps to implement cross-account and cross-region interconnections over peering connection.

- There are two steps to implement communication over peering connection:
  Step 1: Create a peering connection.
  Step 2: Set routing tables on both ends.
	
- There are three steps to implement cross-account communication over peering connection:
  Step 1: Create a peering connection.
  Step 2: Accept request for peering connection.
  Step 3: Set routing tables on both ends.

Example:
IP address range 1: The subnet A `192.168.1.0/24` of VPC1 in **Guangzhou**.
IP address range 2: The subnet B `10.0.1.0/24` of VPC2 in **Beijing**.
The following steps are required to achieve interconnection between IP address range 1 and IP address range 2 via peering connection:

![](https://mc.qcloudimg.com/static/img/d79a35cb5fa2701e147dd1d52f316ea1/VPC-Peer+Connection%284%29.png)

#### Step 1: Create Peering Connection
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and click "Virtual Private Cloud" in the navigation bar.
2) Select the "Peering Connection" tab in the VPC console, and select the region "**Guangzhou**" and the VPC `VPC1` above the list, and then click "New" to create a peering connection.
3) Enter a name (such as `PeerConn`), select **Beijing** in "Peer Region", the "Peer account type" and `VPC2` in "Peer network".

- If the type of the peer account is "My Account", select it directly from the drop-down list.
- If the type of the peer account is "Other Accounts", enter the account ID and VPC ID of the peer account.

4) Select the maximum bandwidth

- For a intra-region peering connection, there is no restriction on bandwidth. **No modification** to this.
- A maximum bandwidth can be selected for a cross-region peering connection. Submit a ticket to request for a larger cross-region bandwidth.

5) A peering connection between the VPCs under the same account takes effect immediately upon its creation.
   4) When you create a peering connection to a VPC under another account, the connection takes effect only after the peer accepts the connection request.
> Note: Any fees charged for a cross-region peering connection are paid by the initiator of the connection.

#### (Optional) Step 2: Accept Request for Peering Connection
If VPC2 belongs to other user, you need to notify the user to accept your request for peering connection.
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to select the "Peering Connection" in the VPC console.
2) Select the region **Beijing** above the list, find the peering connection to be accepted in the peering connection list: `PeerConn`, and click "Accept".
3) The creation of peering connection is completed.
> Note: When the peering connection is created, the interconnection between VPCs of both ends is not allowed until the route that is directed to the peering connection is added in "both" VPCs.

#### Step 3: Configure Routing tables on Both Ends for Peering Connection
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar and select the "Subnet" tab in VPC console.
2) Click the ID of the routing table (routing table A) associated to the specified subnet (subnet A) on the local end of the peering connection, to go to the details page of the routing table.
3) Click to edit the routing policy. Enter the peer CIDR (`10.0.1.0/24`) for "Destination", select "Peering connections" for "Next hop type", and select the created peering connection (PeerConn) for "Next hop".
4) Save the routing table.
**Use the same configuration for the peer routing table.**
>Note:
1) You must configure routes on both ends before you can communicate via the peering connection.
2) For communication between multiple IP address ranges of two VPCs on both ends, you only need to **increase the corresponding routing tables** instead of creating multiple peering connections.

After the routing table is configured, the communication can be achieved between different IP address ranges of two VPCs.

### Viewing Routing Policy Related to Peering Connection
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to select the "Peering Connection" in the VPC console.
2) Select the region and VPC above the list.
3) Click the ID of the specified peering connection to go to its details page. You can see in the related routing policy that the next hop is the destination IP address range, the associated subnet, and the related routing table of the peering connection.
> Note: If you have established a peering connection but cannot communicate via it, check whether the configurations of the routing tables on **both ends** are correct by taking this step.

### Viewing **Monitoring** Data of Network Traffic over Cross-region Peering Connection (Cross-region Interconnection)
No upper limit is set on the network traffic for intra-region peering connection.
Monitoring of network traffic is only supported for cross-region peering connections.
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to select the "Peering Connection" in the VPC console.
2) Select the region and VPC above the list.
3) Click the Monitoring icon of the specified peering connection to view the **inbound/outbound bandwidth, number of inbound/outbound packets and packet loss**.

### Configuring Traffic Control for Cross-region Peering Connection (Cross-region Interconnection)
Network traffic over intra-region peering connection is free of charge. No traffic control is applicable. Maximum bandwidth is 5 Gbps.
Traffic control is supported for cross-region peering connection.
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar to select the "Peering Connection" in the VPC console.
2) Click the ID of corresponding peering connection in the list page to go to its details page.
3) In the basic information section, click "Change Bandwidth". Select the corresponding bandwidth, and save it to take effect.


### Enabling Traffic Control Details for Peering Connection
After it is enabled, you can view the metrics of IP traffic flowing through a peering connection over the past 7 days, and also set the outbound bandwidth for an IP to flow to a specific peering connection.

1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "Peering Connection".
2) In the peering connection list, click an ID to go to the peering connection details page.
3) Click the "Monitor" tab, and enable the switch of "Traffic Control Details for Peering Connection" on the upper right corner.
After the Traffic Control Details for Peering Connection is enabled, it takes 5 to 6 days to collect and publish data. During this period, you can view the monitoring details table at the lower part of the monitoring chart.

>Note: This feature is under internal trial. Submit a ticket to apply for it.

### Setting Traffic Control Details for Peering Connection
After the Traffic Control Details for Peering Connection is enabled, you can set the outbound bandwidth for an IP to flow to a specific peering connection.
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "Peering Connection".
2) In the peering connection list, click an ID to go to the peering connection details page.
3) Click the "Monitor" tab, find the IP for which monitoring details need to be set, and set a limit on its outbound bandwidth.

### Viewing Traffic Control Details for Peering Connection
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to go to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then select "Peering Connection".
2) In the peering connection list, click an ID to go to the peering connection details page.
3. Click the "Monitor" tab, and then click "View Restricted IP" in the upper right of the table of traffic control details for peer connection.


### Rejecting Peering Connection
You can reject the request for the peering connection with a status of "To be Accepted". Except for the accounts you trust, you can reject any unnecessary requests.

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar and select the "Peering Connection" tab in VPC console.
2) View the peering connection to be accepted in the peering connection list, and click "Reject" button in the Operation column.
3) The peering connection is rejected and disappears.

### Deleting Peering Connection
The peering connection can be deleted on either end at any time, and becomes invalid immediately upon deletion. When the peering connection is deleted, the routing entry containing this peering connection in the routing table is also deleted.

1) Log in to [Tencent Cloud Console], and click "Virtual Private Cloud" in the navigation bar.
2) Select the "Peering Connection" tab in the VPC console to view the established peering connections in the peering connection list, and click "Delete" in the Operation column.
3) After you confirm the deletion action, the peering connection is deleted.

### Viewing Peer Account ID
When you create a cross-account peering connection/shared Direct Connect, you need to enter the account ID for the peer **developer**, which you can check as follows:
1) Log in to Tencent Cloud Console, and click the account name on the upper right corner.
2) View the Account ID in [Basic Info](https://console.cloud.tencent.com/developer).

![](https://mc.qcloudimg.com/static/img/8a06f2ed1e2afdfb0d1dacc590dd381a/Peering_Connection.jpg)


### Deleting Peering Connection
The peering connection can be deleted on either end at any time, and becomes invalid immediately upon deletion. When the peering connection is deleted, the routing entry containing this peering connection in the routing table is also deleted.

1) Log in to [Tencent Cloud Console], and click "Virtual Private Cloud" in the navigation bar.
2) Select the "Peering Connection" tab in the VPC console to view the established peering connections in the peering connection list, and click "Delete" in the Operation column.
3) After you confirm the deletion action, the peering connection is deleted.

### Enabling Basic Network Cross-region Interconnection
Submit a [Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=168&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC) to apply for the basic network cross-region interconnection.

### Setting Alarms for Cross-Region Interconnection
1) Log in to Tencent Cloud Console, click "Cloud Products" -> "Monitor & Management" -> "Cloud Monitor" in the top navigation bar, and select "My Alarms" -> ["Alarm Policy"](https://console.cloud.tencent.com/monitor/policylist) in the left navigation bar, and then click "Add Alarm Policy".
2) Enter the alarm "Policy Name", select "Peering Connection" or "Basic Network Cross-Region Interconnection" in Policy Type, and then add alarm triggering condition.
3) Associate alarm objects: select the alarm receiver group, and when it is saved, you can view the set alarm polices in Policy List.
4) View the alarm information: when any alarm conditions are triggered, you will receive SMS/email/internal message or other notices, and you can also find the information in the left navigation "My Alarms" -> "Alarm List".



## API Overview
You can use API operations to set and manage your peering connection. For more information on additional resources in VPC, please see [Overview of All VPC APIs](https://cloud.tencent.com/document/api/215/909).
 
 
| Feature | Action ID | Description |
|---------|---------|---------|
| Create Intra-region peering connection | [CreateVpcPeeringConnection](https://cloud.tencent.com/document/api/215/2107) | Create an intra-region peering connection. |
| Delete Intra-region peering connection | [DeleteVpcPeeringConnection](https://cloud.tencent.com/document/api/215/2104) | Delete an intra-region peering connection. |
| Modify Intra-region peering connection | [ModifyVpcPeeringConnection](https://cloud.tencent.com/document/api/215/2103) | Modify an intra-region peering connection. |
| Accept Intra-region peering connection | [AcceptVpcPeeringConnection](https://cloud.tencent.com/document/api/215/2106) | Accept an intra-region peering connection. |
| Reject Intra-region peering connection | [RejectVpcPeeringConnection](https://cloud.tencent.com/document/api/215/2105) | Reject an intra-region peering connection. |
| Enable expired Intra-region peering connection | [EnableVpcPeeringConnection](https://cloud.tencent.com/document/api/215/2102) | Enable an expired intra-region peering connection. |
| Create cross-region peering connection | [CreateVpcPeeringConnectionEx](https://cloud.tencent.com/document/api/215/4803) | Create a cross-region peering connection. |
| Delete cross-region peering connection | [DeleteVpcPeeringConnectionEx](https://cloud.tencent.com/document/api/215/4804) | Delete a cross-region peering connection. |
| Modify cross-region peering connection | [ModifyVpcPeeringConnectionEx](https://cloud.tencent.com/document/api/215/4805) | Modify a cross-region peering connection. |
| Accept cross-region peering connection | [AcceptVpcPeeringConnectionEx](https://cloud.tencent.com/document/api/215/4806) | Accept a cross-region peering connection. |
| Reject cross-region peering connection | [RejectVpcPeeringConnectionEx](https://cloud.tencent.com/document/api/215/4807) | Reject a cross-region peering connection. |
| Enable expired cross-region peering connection | [EnableVpcPeeringConnectionEx](https://cloud.tencent.com/document/api/215/4808) | Enable an expired cross-region peering connection. |
| Query peering connection | [DescribeVpcPeeringConnections](https://cloud.tencent.com/document/api/215/2101) | Query a peering connection. |


