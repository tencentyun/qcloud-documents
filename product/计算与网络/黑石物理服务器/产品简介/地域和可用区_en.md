Region and the Availability Zone are used to describe the locations of the Tencent Cloud data centers. You can purchase a Cloud Physical Machine (CPM) in a specified region and availability zone.

Region is an independent geographical location. Within a region, there are multiple mutually isolated data centers referred to as availability zone.</br>
Different regions are completely independent to ensure maximal fault tolerance and stability. Each availability zone is also independent. However, availability zones in the same region can be connected via private network links with low latency.

You can purchase CPM in different locations and you are recommended to deploy your business in different availability zones to avoid unavailability of service caused by single point of failure.

The followings are the regions and availability zones where data centers are open for the sale of *CPM* or under construction.

<table class="table-striped">
	<tbody>
		<tr>
			<th>&nbsp;</th>
			<th>Region</th>
			<th>Availability Zone</th>
		</tr>
		<tr>
			<td rowspan="7">China</td>
			<td rowspan="3">North China (Beijing)</td>
			<td>Beijing Zone 1</td>
			<tr><td>Beijing Zone 2 (Coming soon)</td></tr>
		</tr>
		<tr>
			
		</tr>
		<tr>
			
		</tr>
		
		<tr>
			<td>East China (Shanghai)</td>
			<td>Shanghai Zone 1</td>
		</tr>
		<tr>
			<td>South China (Guangzhou)</td>
			<td>Guangzhou Zone 1 (Coming soon)</td>
		</tr>
			
	</tbody>
</table>



## Region
Different regions of Tencent Cloud are completely isolated to ensure maximal stability and fault tolerance among those regions. Currently, North China and East China are covered domestically. We will gradually increase available nodes to cover more regions. You are recommended to choose the region that is closest to your customer to minimize access latency and improve download speed.

- CPMs of different regions <font color="red">cannot communicate via private network by default</font>, but you can request for activation of interconnection over private network.
- You can only select CPMs in the same region when binding BM load balancer to CPMs.
- The "interconnection over private network" mentioned above refers to the interconnection among resources within the same Tencent Cloud account. The private networks for the resources under difference accounts are completely isolated from each other.

## Availability Zone
Availability zones refer to Tencent Cloud physical data centers in a certain region whose power and network equipment are independent from each other. They are designed to ensure that the failures within availability zones can be isolated (except for large-scale disaster or major power failure) without spreading to and affecting other zones so that your businesses can provide continuous online services. By starting an instance in multiple independent availability zones, you can protect your application from being affected by the failures occurring in a single location.

When purchasing a CPM, you can choose any availability zone within the specified region. If you need to design an architecture with high reliability to ensure the availability of services when a failure occurs in a CPM or cluster, you can use cross-zone deployment scheme.




