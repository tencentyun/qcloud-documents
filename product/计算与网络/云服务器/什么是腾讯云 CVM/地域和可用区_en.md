Tencent Cloud CVM's entrusted data centers are located in different regions around the world, which are all made up of region and availability zone.

Each region is an independent geographical location. Within each region, there are multiple mutually isolated locations referred to as availability zones. Each region is entirely independent. Each availability zone is independent. However, availability zones in the same region can be connected via private network links with low latency.

Tencent Cloud supports distribution of cloud resources in different locations by users. Users are advised to consider placing resources in different availability zones when designing system to shield "service unavailable" status caused by single point of failure.


<table class="table-striped">
	<tbody>
		<tr>
			<th>&nbsp;</th>
			<th>Region</th>
			<th>Availability Zone</th>
		</tr>
		<tr>
			<td rowspan="7">Within Chinese territory</td>
			<td rowspan="3">South China region (Guangzhou)</td>
			<td>Guangzhou Zone I (Sold out)</td>
		</tr>
		<tr>
			<td>Guangzhou Zone II</td>
		</tr>
		<tr>
			<td>Guangzhou Zone III</td>
		</tr>
		<tr>
			<td>South China region (Shenzhen Finance)</td>
			<td>Shenzhen Finance Zone I<span style="background-color: rgb(249, 249, 249);"> (only financial institutions and enterprises can initiate tickets for application)</span></td>
		</tr>
		<tr>
			<td>East China region (Shanghai)</td>
			<td>Shanghai Zone I</td>
		</tr>
		<tr>
			<td>East China region (Shanghai Finance)</td>
			<td>Shanghai Finance Zone I (only financial institutions and enterprises can initiate tickets for application)</td>
		</tr>
		<tr>
			<td>North China (Beijing)</td>
			<td>Beijing Zone I</td>
		</tr>
		<tr>
			<td rowspan="3">Outside China</td>
			<td>Southeast Asia region (Hong Kong)</td>
			<td>Hong Kong Zone I</td>
		</tr>
		<tr>
			<td>South East Asia region (Singapore)</td>
			<td>Singapore Zone I</td>
		</tr>
		<tr>
			<td>North America region (Toronto)</td>
			<td>Toronto Zone I</td>
		</tr>
	</tbody>
</table>



## Region
Different regions of Tencent Cloud are completely isolated to ensure maximal stability and fault tolerance among those regions. Currently, South China, East China, and North China are covered domestically, and Hong Kong and Singapore nodes for South East Asia and Toronto node for North America are also available. We will gradually increase region supply for coverage of more nodes. Users are advised to choose the region closest to their clients in order to reduce access latency and improve download speed.

Region attribute is differentiated for all behaviors such as enabling and viewing instances by users. If image of the instance that the users need to enable does not exist in the region, then the image needs to be copied to current region. For more information, please see [Copy image] (/doc/product/213/4943).

- Even located in different availability zones, cloud resources in the same region are connected via private network, and can be accessed directly using [Private IP](/doc/product/213/5225).
- Cloud services of different regions <font color="red">cannot communicate via private network by default</font>.
 - CVMs cannot access other CVMs, Cloud Database or Cloud Memcached across regions by default.
 - When binding Cloud Load Balance to the server, only CVM in the current region can be chosen;
- Cloud resources of different regions can perform Internet access via [Public IP](/doc/product/213/5224); Cloud Services in VPC can also communicate via [Peer connection](/doc/product/215/5000) provided by Tencent Cloud using Tencent Cloud high-speed con- [Cloud Load Balance](https://www.qcloud.com/doc/product/214) does not support cross-region data forwarding.
- The name of regional availability zone is the most straightforward representation of the coverage range of the data center. To make the name of regional availability zone easier for clients to understand, the "coverage range + city where the data center- The above private network interconnection refers to the interconnection of resources under the same account. Private networks for resources under different accounts are completely isolated.

**Special instructions for Hong Kong region:**
- The following cloud services are temporarily unavailable: Cloud Memcached, elastic web engine, Cloud Object Storage, Cloud Block Storage, one-click opening of server and domain binding with separated regions and servers.
- When you need to log in to CVMs in Hong Kong region, login via jump server is recommended for better operation and maintenance experience.

**Special instructions for North America region:**
- The following cloud services are temporarily unavailable: Cloud Memcached, elastic web engine, Cloud Object Storage, mobile acceleration, Cloud Automated Testing, one-click opening of server and domain binding with separated regions and servers.
- Due to the considerable latency between North America and China, when you need to log in to CVMs in North America region, login via jump server is recommended for better operation and maintenance experience.

**Special instructions for Shanghai Finance Zone:**
Compliance zone customized according to regulatory requirements of finance industry characterized by high level of safety and isolation; currently provide CVM, finance database, Redis storage, face recognition and other services. Verified clients in finance industry can apply for using the zone with initiating tickets. For details, see [Introduction of finance zone](http://www.qcloud.com/doc/product/304/%E9%87%91%E8%9E%8D%E4%BA%91%E7%AE%80%E4%BB%8B).

## Availability zone
Availability zones (Zone) refer to Tencent Cloud's physical data centers whose power and network are independent from each other within the same region. They are designed to ensure that the failures within an availability zones can be isolated (except for large-scale disaster or major power failure) without spreading to and affecting other zones so that users' businesses can provide continuous online services. By starting an instance in an independent availability zone, users can protect their applications from being affected by the failures occurring in a single location.

When starting an instance, users can choose any availability zone within the specified region. If a user needs to ensure the high reliability of application systems so that the services are still available even when a failure occurs in an instance, the user can use across-zone deployment scheme (e.g. [Cloud Load Balance](https://www.qcloud.com/doc/product/214), [Elastic IP](/doc/product/213/5733), etc.) to allow the instance in another availability zone to handle the relevant requests in replace of the failed instance.

### Migrate an instance to another availability zone

For an instance that is already started, its availability zone cannot be changed, but its user can migrate it to another availability zone by other means. The migration process involves creating a custom image from the original instance, using the custom image to start an instance in a new availability zone and updating the configuration of the new instance. 

1. Create a custom image for current instance. For more information, see [Create Custom Image](/doc/product/213/4942).2. If the network environment of the current instance is [Virtual Private Cloud] (/doc/product/213/5227) and the private IP address needs to be retained after the migration, users can first delete the subnet in the current availability zone and then create a subnet in the new availability zone with the same IP address range as that of the original subnet. Please note that a subnet can be deleted only when it contains no available instance. Thus, all the instances in the current subnet should be migrated to the new subnet.3. Create a new instance in the new availability zone using the custom image you have just created. User can choose the same type and configuration as those of the original instance, or choose new ones. For more information, see [Purchase and Start an Instance] (/doc/product/213/4855).4. If an elastic IP address is associated with the original instance, then dissociate it from the old instance and associate it with the new instance. For more information, see [Elastic IP] (/doc/product/213/5733).
5. (Optional) If the type of original instance is [Charge by Quantity](https://www.qcloud.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9), then you can choose to destroy the original instance. For more information, see [Destroy an Instance] (/doc/product/213/4930). If the type of the original instance is [Annual or Monthly Plan], (https://www.qcloud.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88)you can choose to wait until it expires and reclaim it.
## How to select region and availability zone
When purchasing Cloud Services, it is recommended to choose the region that is closest to your customers to minimize the access latency and improve download speed.

## Locations of resources
Specify which resources of Tencent Cloud are global, which resources are regional and not specific to any availability zone and which resources are based on availability zones.

<table>
<tr><th>Resource</th><th>Resource ID format<br><资源缩写>-8-digit number and character</th><th>Type</th><th>Description</th></tr>
<tbody>
<tr>
  <td>User account ID</td>
  <td>Not limited</td>
  <td>Globally Unique</td>
  <td>Users can access Tencent Cloud resources globally with the same account ID.</td>
</tr>
<tr>
<td> <a href="/doc/product/213/5223">SSH key</a> </td>
  <td>skey-xxxxxxxx</td>
  <td>Available in all regions</td>
  <td>Users can use SSH key to bind to any CVM in any region under their account.</td>
</tr>
<tr>
<td> <a href="/doc/product/213/4939">CVM instance</a> </td>
  <td>ins-xxxxxxxx</td>
  <td>Only available in a single availability zone of a single region</td>
  <td>Users can only create CVM instance under specified availability zones</td>
</tr>
<tr>
<td> <a href="/doc/product/213/4941">Custom Image</a> </td>
  <td>img-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>Users can create custom Image for instances which can be used in different availability zones of the same region Please copy custom image to other regions using the copy image function to use it in those regions.</td>
</tr>
<tr>
<td> <a href="/doc/product/213/5733">Elastic IP</a> </td>
  <td>eip-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>Elastic IP address is created under a certain region, and can only be associated with instance in the same region </td>
</tr>
<tr>
<td> <a href="/doc/product/213/5221">Security Group</a> </td>
  <td>sg-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>Security Group is created under a certain region, and can only be associated with instance in the same region. Tencent Cloud automatically creates 3 default Security Groups for users.</td>
</tr>
<tr>
<td> <a href="https://www.qcloud.com/doc/product/362">(Elastic) Cloud Block Storage</a> </td>
  <td>disk-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>Elastic Cloud Block Storage can be created independently under a certain region and mounted to instances in the same region. </td>
</tr>
<tr>
<td> <a href="https://www.qcloud.com/doc/product/362/2455">Snapshot</a> </td>
  <td>snap-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>After creating snapshot for a specific Cloud Block Storage, users can use this snapshot in the region for other operations (such as creating Cloud Block Storage)</td>
</tr>
<tr>
<td> <a href="/doc/product/214/524">Cloud Load Balance</a> </td>
  <td>clb-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>Cloud Load Balance can bind to CVMs in different availability zones in a single region for forwarding traffic.</td>
</tr>
<tr>
<td> <a href="/doc/product/215/535">Virtual Private Cloud (VPC)</a> </td>
  <td>vpc-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>VPC is created under a certain region. Resources belonging to the same VPC can be created under different availability zones</td>
</tr>
<tr>
<td> <a href="/doc/product/215/4927">Subnet</a> </td>
  <td>subnet-xxxxxxxx</td>
  <td>Only available in a single availability zone of a single region</td>
  <td>Users cannot create a subnet across availability zones.</td>
</tr>
<tr>
<td> <a href="/doc/product/215/4954">Routing table</a> </td>
  <td>rtb-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>When creating a routing table, users need to designate a specific VPC, and therefore location attribute of the VPC should be followed.</td>
</tr>
</tbody></table>

