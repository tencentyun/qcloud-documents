
## Introduction
VPC peering connection is a cross-VPC network interconnection service for office data synchronization that allows VPC IPs to route traffic between peer VPCs as if they belong to the same network. You can achieve VPC interconnection between the same or different users for the same or different regions. Traffic interconnection between VPCs can be achieved through setting up routing policies on the two sides. Peering connections do not depend on a single piece of hardware, so there is no single point of failure or bandwidth bottleneck.

> Note: Click to view [Cross-region Connection Service Agreement](https://www.qcloud.com/document/product/215/7682). If you have violated any of the provisions of the agreement, Tencent Cloud may at any time restrict, suspend or terminate services to you under the agreement as appropriate, and retain the right to pursue related liability.

## Interconnectivity of Peering Connection Is Not Transitive
Peering connection allows interconnections between VPCs, but this interconnection is not transitive. As shown in the following figure, peering connection is established between VPC 1 and VPC 2, as is done between VPC 1 and VPC 3. However, due to the non-transitive nature of peering connection, VPC 2 and VPC 3 cannot readily interconnect.
![](//mccdn.qcloud.com/static/img/9127397dcb1df231bfd8d32bcd628223/image.png)
> Note: Even if a peering connection is established, communication cannot be achieved if routes for sending and returning packets are not configured at both ends.


## Regional Peering Connection and Cross-region Peering Connection (i.e., cross-region interconnection)
VPC supports both regional and cross-region peering connections (i.e., cross-region interconnection). Since the physical distance between the two ends of the peering connection as well as the underlying architecture is different for these two connections, there are also some differences on function and billing, which is summarized below:

| Comparison Item | Regional Peering Connection | Cross-region Peering Connection |
|---------|---------|---------|
| Underlying architecture | Local private network within a single region based on Tencent Cloud | Cross-region internal MPLS network based on Tencent Cloud |
| Bandwidth | No bandwidth limit | Maximum 1 GB, bandwidth upper limit can be set |
| Billing Rule | 	Free of charge | 	Daily rate is applicable depending on the regions where both sides of the peering connection are located and the actually used network bandwidth. For details, please refer to [Price Overview](https://www.qcloud.com/doc/product/215/%E4%BB%B7%E6%A0%BC%E6%80%BB%E8%A7%88) |	
| Availability | Above 99.95%, no single point of failure | 	Above 99.95%, no single point of failure |	
| Cross-account connection | Support | Support |	
| Access Permission | CVMs on both ends of a peering connection can access all resources of its peer including peer CVM, database, cloud load balancer and so on | CVMs on both ends of a peering connection can access all resources of its peer including peer CVM, database, cloud load balancer and so on |	
| Function Limits | VPC network segments on both sides of a peering connection must not overlap; multiple peering connections will not affect one another | VPC network segments on both sides of a peering connection must not overlap; <br><font color="red">When multiple peer VPCs are connected to one VPC, multiple peer VPC network segments must not overlap</font> |	

Regional peering connection is used primarily to connect applications located in different VPCs within the same region.
The typical applications for cross-region peering connection (cross-region interconnection) are: **Cross-region disaster recovery**, cross-region connection of VPCs within different regions, rapid deployment of Disaster Recovery at Two Locations and Three Centers, high bandwidth and reliability, and catering to needs of network disaster recovery of financial network.

## Workflow for Establishing and Deleting
### Workflow for Establishing a Peering Connection
![](//mccdn.qcloud.com/static/img/9527bab04ca5213bdd72dbec99c9e9ef/image.png)

### Workflow for Deleting a Peering Connection
![](//mccdn.qcloud.com/static/img/0e0ae950ebface4e307cd510de2b885e/image.png)

## Service Limits
When using peering connection, you have to note the following:
- To achieve true communication between both ends of a peering connection, you must configure a routing rules targeting the peer on related routing tables of the originating and receiving ends.
- Costs for cross-region peering connection are paid by the requester of such connection.
- If the other party does not accept a peering connection request, the request will automatically expire after 7 days.
- Please do not accept peering connection requests from unknown accounts because they may pose risks to your network.
- The VPC CIDR on both ends of a peering connection cannot overlap, otherwise an error will occur at the time of creation.
- For a cross-region peering connection, the CIDRs of multiple peer networks of one VPC cannot overlap, otherwise an error will occur.
- Any party of a peering connection can interrupt the peering connection at any time. The communication between the two VPCs is terminated immediately after the interruption.
- There is no bandwidth limit for regional peering connection, and a bandwidth limit must be set for across-region peering connections.


| Resource | Restriction | Description |
|---------|---------|---------|
| Bandwidth limit for cross-region peering connection | 1 GB | If you need a larger bandwidth, please initiate the request by submitting a ticket. There is no limit for the bandwidth of regional peering connections. |
| Number of peering connections supported by each VPC |10 |　|

> Note: For peering connection services in other region, please submit a ticket for the request.

For additional VPC service restrictions, refer to [Additional VPC Service Restrictions](https://www.qcloud.com/document/product/215/537).

## Billing Model
### Billing Method Description
1) Regional peering connection is available for free.
2) Cross-region peering connection (i.e., cross-region interconnection): 
- Post-payment by the peering connection initiator on a daily basis.
- Calculated as the peak bandwidth of the day multiplied by the applicable tiered price.
- Peak bandwidth of the day is calculated as this: bandwidth is captured once every 5 minutes, and the maximum one out of both inbound and outbound bandwidth of that day is taken as the peak bandwidth.
For details, please refer to the following table:


<table>
        <tbody>
				<tr>
            <th style="width: 10%;" rowspan="2">Function</th>
            <th style="width: 25%;" rowspan="2">Billing Method</th>
						<th style="width: 25%;" rowspan="2">Configuration</th>
            <th style="width: 40%;" colspan="4">Price</th>
        </tr>
				
				 <tr>
            <th>Beijing <br>Shanghai <br>Shanghai Finance <br>Guangzhou <br>Shenzhen Finance</th>
						<th>Hong Kong</th>
						<th>Singapore</th>
            <th>Toronto</th>
        </tr>
				<tr>
        <td>Regional Peering Connection</td>
				<td colspan="6" >　　　　　　　　　　　　　　　　　　　　　Free</td>
				<tr>
				<tr>
            <td rowspan="5">Cross-region Peering Connection</td>
						<td rowspan="5">Peak bandwidth of the day<br><br>Daily rate (CNY/Mbps/Day) <br><br>Peak bandwidth is calculated using the average bandwidth per 5 mins<br></td>
						<td>(0, 20] Mbps</td>
						<td>20</td>
						<td>-</td>
						<td>-</td>
						<td>-</td>
        </tr>
				
				<tr>
				<td>(20,100] Mbps</td>
						<td>12</td>
						<td>-</td>
						<td>-</td>
						<td>-</td>
				</tr>
				
				<tr>
				<td>(100, 500] Mbps</td>
				<td colspan="4" rowspan="4">　　　　　　　Please consult with the business department<br>
				</tr>
				
				<tr>
				<td>(500, 2000] Mbps</td>
				</tr>
				
			 <tr>
				<td >Above 2000 Mbps</td>
				</tr>
					<tr>
</tbody></table>

> Contact business department to consult more about prices.

For more information regarding the prices of VPC services, refer to [VPC Price Overview](https://www.qcloud.com/doc/product/215/3079).

> Note: In order for you to view the cost, the billing system describes peering connections as:  bill for cross-region interconnection (mainland) and bill for peering connection of which both ends are in mainland China


**Example:**
If the peering connection initiator is in Shanghai, the receiver is in Guangzhou, outbound peak bandwidth of the day is 20 Mbps, inbound peak bandwidth is 30 Mbps, then the cost of the day is: 30 * 12 = 360 CNY, which shall be paid by the initiator.

### Free cross-region interconnection bandwidth campaign **(Key customers are entitled to its benefits by default, but it is closed to common customers)**
Benefits for VIP customers and common customers during the campaign are as follows:

**VIP customers** (The benefits are entitled to all VIP customer and those becoming a VIP customer)
- Extra free bandwidth of 100Mbps is offered for each peering connection in Mainland China (automatically assigned by the system).

**Common customer** (The campaign is closed)
- Extra free bandwidth of 10 Mbps is offered for each peering connection in Mainland China.

> Note:
- It takes effect on the day the bandwidth remission is approved upon review. The extra amount is applicable to the tiered price. This is valid until Dec. 31, 2017. You can view the remission details in the peering connection creation pop-up or in the details page.


- If you consume more than 100,000 CNY in Tencent Cloud within a month, you can apply to become a VIP customer, entitled to the supreme service and related benefits, [Apply Now >>](https://www.qcloud.com/service/vip. Html)

## Operating Instructions

### Quick Start
Cross-region connection and Cross-account communication of VPC are both advanced features of peering connection, and you can take the following steps to implement cross-account and cross-region interconnection over peering connection.

- There are two steps to implement communication over peering connection:
  Step 1: Creating a peering connection.
  Step 2: Setting routing tables on both ends.
	
- There are three steps to implement cross-account communication over peering connection:
  Step 1: Creating a peering connection.
  Step 2: Accepting request for peering connection.
  Step 3: Setting routing tables on both ends.

Example:
Network segment 1: VPC1 subnet A `192.168.1.0/24` in **Guangzhou**.
Network segment 2:   VPC2 subnet B `10.0.1.0/24` in **Beijing**.
The following steps are required to achieve interconnection between segment 1 and segment 2 via peering connection:
![](//mc.qcloudimg.com/static/img/4817a68077ccf82022ea167476871c41/3.jpg)
#### Step 1: Creating a peering connection
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/), and click "Virtual Private Cloud" in the navigation bar.
2) Select the "Peering Connection" tab in the VPC console, and select **Region: Guangzhou**, VPC `VPC1` above the list, and then click "New" to create a peering connection.
3) Enter a name (e.g., `PeerConn`), select the peer **Region: Beijing**, "Peer account type" and Peer network `VPC2`.

- If the peer account type is "My Account", select the peer network from the drop-down list.
- If the peer account type is "Other accounts", enter the account ID and VPC ID of the peer account.

4) Select the maximum bandwidth

- For a regional peering connection, there is no restriction on bandwidth, **No modification**.
- For a cross-region peering connection, you can select a maximum bandwidth. If you need a higher cross-region bandwidth, please initiate a request by submitting a ticket.

5) A peering connection between the VPCs under the same account takes effect immediately after its creation;
   4) If you want to create a peering connection to a VPC under another account, the connection takes effect only after the peer accepts the connection request.
> Note: Any fees charged for a cross-region peering connection are paid by the initiator of the connection.

#### (Optional) Step 2: Accepting request for peering connection
If VPC2 belongs to other user, you need to notify the user to accept your request for peering connection.
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/). Click "Virtual Private Cloud" in the navigation bar to select the "Peering Connection" in the VPC console.
2) Select the corresponding *Region: Beijing* above the list, locate the peering connection to be accepted in the peering connection list: `PeerConn`, and click "Accept".
3) This complete the creation of the peering connection
> Note: After the peering connection is created, you need to add the route that points to the peering connection in the VPCs of both sides to allow local VPC and the peer VPC to interconnect with each other, which otherwise cannot be realized.

#### Step 3: Configuring routing tables on both sides for the peering connection
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/). Click "Virtual Private Cloud" in the navigation bar and select the "Subnet" tab in VPC console.
2) Click the ID of the associated routing table (routing table A) with the specified subnet (subnet A) on local end of the peering connection, to enter the details page of the routing table.
3) Click to edit the routing policy. For the destination, enter the peer CIDR (`10.0.1.0/24`); for next hop type, select "peering connections"; and for next hop, select the created peering connection (PeerConn).
4) Save the routing table.
**The configuration of the peer routing table is the same as above.**
> Note:
1) You must configure routes on both ends before you can communicate via the peering connection.
2) For communication between two VPCs on both ends and conducted by multiple network segments, you only need to **increase the corresponding routing tables** instead of creating multiple peering connections.

After the routing table configuration is completed, communication can be performed between different network segments of the two VPCs.

### Viewing Routing Policy Related to Peering Connection
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/). Click "Virtual Private Cloud" in the navigation bar to select the "Peering Connection" in the VPC console.
2) Select the region and VPC above the list.
3) Click the ID of the specified peering connection to enter its details page. You can view in the related routing policy that the next hop is the destination IP address range, the associated subnet, and the related routing table of the peering connection.
> Note: If you have established a peering connection but cannot communicate via it, please use this step to check whether the configuration of routing tables on *both ends* are correct.

### Viewing monitoring data of network traffic over cross-region peering connection (cross-region interconnection)
There is no maximum network traffic for regional peering connection.
Traffic monitoring of peering connection network is only supported for cross-region peering connections.
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/). Click "Virtual Private Cloud" in the navigation bar to select the "Peering Connection" in the VPC console.
2) Select the region and VPC above the list.
3) Click on the Monitoring icon of the specified peering connection to view **inbound and outbound bandwidths, number of inbound and outbound packets and packet loss rate**.

### Configuring Traffic Control for Cross-region Peering Connection (Cross-region Interconnection)
Network traffic over regional peering connection is free; no traffic control is applicable, with maximum bandwidth of 5 Gbps.
Traffic control is supported for cross-region peering connection.
1) Log in to [Tencent Cloud Console](https://console.qcloud.com/). Click "Virtual Private Cloud" in the navigation bar to select the "Peering Connection" in the VPC console.
2) Click on the ID of corresponding peering connection in the list page to enter its details page.
3) In the basic information section, click "Change Bandwidth", select the corresponding bandwidth, and save it to take effect.

### Rejecting Peering Connection
You can reject a "To be Accepted" peering connection request. Except for the accounts you trust, you can reject any unnecessary requests.

1) Log in to [Tencent Cloud Console](https://console.qcloud.com/). Click "Virtual Private Cloud" in the navigation bar and select the **Peering Connection** tab in VPC console.
2) View the peering connection to be accepted in the peering connection list, and click "Reject" button in the Operation Column.
3) The peering connection is rejected and disappears.

### Deleting Peering Connection
Either party can delete the peering connection at any time. The peering connection becomes invalid immediately after being deleted. When the peering connection is deleted, the routing entry containing this connection in the routing table will also be deleted.

1) Log in to Tencent Cloud Console, and click "Virtual Private Cloud" in the navigation bar.
2) Select the **Peering Connections** to view the established peering connections, and click **Delete** in the Operation Column.
3) After you confirm the deletion action, the peering connection is deleted.

### Viewing Peer Account ID
When you create a cross-account peering connection/shared Direct Connect, you need to enter the peer account ID, which you can check in the following ways:
1) Log in to Tencent Cloud Console, and click account name in the right top corner.
2) View account ID in the personal information.
![](https://mc.qcloudimg.com/static/img/8ecbc060325b2fa0face6d875ac4ce41/pic1.png)

## Related APIs
You can use API operations to set and manage your peering connection. For more information on additional resources in VPC, please refer to [Overview of All VPC APIs](https://www.qcloud.com/doc/api/245/909).
 