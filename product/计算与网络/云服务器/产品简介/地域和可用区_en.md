Tencent Cloud CVM's hosted data centers are located in different locations around the world, which are all made up of region and availability zone.

Each region is a separate geographic area and has multiple isolated locations known as availability zones. Each area is completely independent, and each availability zone is isolated. However, the availability zones in a region are connected through low-latency private network linkages.

Tencent Cloud allows users to assign cloud resources in different locations. Users are advised to place resources in different availability zones when designing system to block "service unavailable" status caused by single point of failure.


<table class="table-striped">
	<tbody>
		<tr>
			<th>&nbsp;</th>
			<th>Region</th>
			<th>Availability Zone</th>
		</tr>
		<tr>
			<td rowspan="16">Mainland China</td>
			<td rowspan="4">South China (Guangzhou)<br>ap-guangzhou</td>
			<td>Guangzhou Zone 1 (Sold out)<br>ap-guangzhou-1</td>
		</tr>	
		<tr>
			<td>Guangzhou Zone 2<br>ap-guangzhou-2</td>
		</tr>
		<tr>
			<td>Guangzhou Zone 3<br>ap-guangzhou-3</td>
		</tr>
		<tr>
			<td>Guangzhou Zone 4<br>ap-guangzhou-4</td>
		</tr>
		<tr>
			<td rowspan="2">South China (Shenzhen Finance)<br>ap-shenzhen-fsi
</td>
			<td>Shenzhen Finance Zone 1 <span style="background-color: rgb(249, 249, 249);">(only available to financial institutions and enterprises)<br>ap-shenzhen-fsi-1</span></td>
			</tr>
			<tr>
			<td>Shenzhen Finance Zone 2 <span style="background-color: rgb(249, 249, 249);">(only available to financial institutions and enterprises)<br>ap-shenzhen-fsi-2</span></td>
			<tr>
		
		<tr>
			<td rowspan="2">East China (Shanghai)<br>ap-shanghai</td>
			<td>Shanghai Zone 1<br>ap-shanghai-1</td>
		</tr>
			<tr>
			<td>Shanghai Zone 2<br>ap-shanghai-2</td>
		   </tr>
		
			
		</tr>
		<tr>
			<td rowspan="2">East China (Shanghai Finance)<br>ap-shanghai-fsi</td>
			<td>Shanghai Finance Zone 1 (only available to financial institutions and enterprises)<br>ap-shanghai-fsi-1</td>
		</tr>
		<tr>
			<td>Shanghai Finance Zone 1 (only available to financial institutions and enterprises)<br>ap-shanghai-fsi-2</td>
		   </tr>
		<tr>
			<td rowspan="3">North China (Beijing)<br>ap-beijing</td>
			<td>Beijing Zone 1<br>ap-beijing-1</td>
		</tr>
			<tr>
			<td>Beijing Zone 2<br>ap-beijing-2</td>
		   </tr>
		   <tr>
			<td>Beijing Zone 3<br>ap-beijing-3</td>
		   </tr>
		</tr>
		<tr>
			<td rowspan="2">Southwest (Chengdu)<br>ap-chengdu</td>
			<td>Chengdu Zone 1<br>ap-chengdu-1</td>
		</tr>
			<tr>
			<td>Chengdu Zone 2<br>ap-chengdu-2</td>
		   </tr>
		</tr>
		<tr>
			<td rowspan="6">Overseas</td>
			<td>Southeast Asia (Hong Kong)<br>ap-hongkong</td>
			<td>Hong Kong Zone 1 (Hong Kong node serves users in Southeast Asia)<br>ap-hongkong-1</td>
		</tr>
		<tr>
			<td>Southeast Asia (Singapore)<br>ap-singapore</td>
			<td>Singapore Zone 1 (Singapore node serves users in Southeast Asia)<br>ap-singapore-1</td>
		</tr>
		<tr>
			<td>Asia Pacific (Seoul)<br>ap-seoul</td>
			<td>Seoul Zone 1 (Seoul node serves users in Northeast Asia)<br>ap-seoul-1</td>
		</tr>
		<tr>
			<td>North America (Toronto)<br>na-toronto</td>
			<td>Toronto Zone 1 (Toronto Zone node serves users in North American)<br>na-toronto-1</td>
		</tr>
		<tr>
			<td>Western U.S. (Silicon Valley)<br>na-siliconvalley</td>
			<td>Silicon Valley Zone 1 (Silicon Valley node serves users in Western U.S.)<br>na-siliconvalley-1</td>
		</tr>
		<tr>
			<td>Europe (Frankfurt)<br>eu-frankfurt</td>
			<td>Frankfurt Zone 1 (Frankfurt node serves users in Europe)<br>eu-frankfurt-1</td>
		</tr>
	</tbody>
</table>



## Region
Different regions of Tencent Cloud are completely isolated to ensure maximal stability and fault tolerance among these regions. South China, East China, and North China are covered domestically. Hong Kong and Singapore nodes for South East Asia, Toronto node for North America, and Silicon Valley node for Western America are also available. We will gradually increase available nodes to cover more regions. You're recommended to choose the region closest to your customers to minimize access latency and improve download speed.

Actions such as enabling and viewing instances vary in different regions. If image of the instance that you need to enable does not exist in the region, the image needs to be copied to current region. For more information, please see [Copy Image](https://cloud.tencent.com/document/product/213/4943).

- Even located in different availability zones, cloud resources in the same region are interconnected via private network, and can be accessed directly via [Private IP](https://cloud.tencent.com/document/product/213/5225).
- Cloud products of different regions <font color="red">cannot communicate via private network by default</font>.
 - CVMs cannot access other CVMs, Cloud Database or Cloud Memcached across regions by default.
 - When binding load balance service to a CVM, you can only bind it to a CVM in the same region.
- Cloud resources of different regions can access Internet via [Public IP](https://cloud.tencent.com/document/product/213/5224). Cloud services in the VPC can also communicate with each other using [Peering Connection](https://cloud.tencent.com/document/product/215/5000) provided by Tencent Cloud through Tencent Cloud high-speed connected network, to realize connection that is more stable and faster than Internet access.
- [Cloud Load Balancer](https://cloud.tencent.com/document/product/214) does not support cross-region traffic forwarding.
- The name of a region or an availability zone defines the coverage of the data center within the region or availability zone. To make it easy for customers to understand the name of a region or an availability zone, region is named in the structure of "coverage range + city where the data center is located" (where "coverage range" represents the coverage capability of the data center and "city where the data center is located" indicates the city where the data center is located or near to), and availability zone is named in the structure of "city + No.".
- The "interconnection via private network" mentioned above refers to the interconnection among resources under the same account. Private resource networks of different accounts are completely isolated from each other.


**Notes About Shenzhen/Shanghai Finance Zone:**
Compliance zone customized according to regulatory requirements of finance industry features high level of security and isolation. Currently available services are CVM, finance database, Redis storage, face recognition, etc. Verified clients in finance industry can apply for the zone by submitting tickets. For more information, please see [About Finance Zone](https://cloud.tencent.com/document/product/304/2766).

## Availability Zone
Availability zones refer to Tencent Cloud physical data centers in the same region with independent power and network resources. They are designed to ensure that the failures within an availability zone can be isolated (except for large-scale disaster or major power failure) without spreading to and affecting other zones, so as to ensure users' business stability. By starting an instance in an independent availability zone, users can protect their applications from being affected by the failures occurring in a single location.

When enabling an instance, users can choose any availability zone within the specified region. If a user needs to ensure the high reliability of application systems so that the services are still available even when a failure occurs in an instance, the user can use cross-zone deployment scheme (e.g. [Cloud Load Balancer](https://cloud.tencent.com/document/product/214), [Elastic IP](https://cloud.tencent.com/document/product/213/5733), etc.) to allow the instance in another availability zone to handle the relevant requests in place of the failed instance.

### Migrate an Instance to Another Availability Zone

For an instance that is already started, its availability zone cannot be changed, but its user can migrate it to another availability zone by other means. The migration process involves creating a custom image from the original instance, using the custom image to start an instance in a new availability zone and updating the configuration of the new instance.

1. Create a custom image for the current instance. For more information, please see [Create Custom Image](https://cloud.tencent.com/document/product/213/4942).
2. If the network environment of the current instance is [Virtual Private Cloud](https://cloud.tencent.com/document/product/213/5227) and the private IP address needs to be retained after the migration, users can first delete the subnet in the current availability zone and then create a subnet in the new availability zone with the same IP address range as that of the original subnet. Please note that a subnet can be deleted only when it contains no available instance. Thus, all the instances in the current subnet should be migrated to the new subnet.
3. Create a new instance in the new availability zone using the custom image you have just created. You can choose the same type and configuration as those of the original instance, or choose new ones. For more information, please see [Purchase and Launch Instance](https://cloud.tencent.com/document/product/213/4855).
4. If an EIP address is associated with the original instance, dissociate it from the old instance and associate it with the new instance. For more information, please see [Elastic IP](https://cloud.tencent.com/document/product/213/5733).
5. (Optional) If the original instance is billed on a [Postpaid](https://cloud.tencent.com/document/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B92) basis, then you can choose to terminate the original instance. For more information, please see [Terminate Instance](https://cloud.tencent.com/document/product/213/4930). If the original instance is billed on a [Prepaid](https://cloud.tencent.com/document/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.881) basis, you can choose to wait until it expires and reclaim it.

## How to Select Region and Availability Zone
When purchasing Cloud Services, it is recommended to choose the region that is closest to your customers to minimize the access latency and improve download speed.

## Locations of Resources
Specify which resources of Tencent Cloud are global, which resources are regional and not specific to any availability zone and which resources are based on availability zones.

<table>
<tr><th>Resource</th><th>Resource ID<br></th><th>Type</th><th>Description</th></tr>
<tbody>
<tr>
  <td>User account ID</td>
  <td>No limit</td>
  <td>Globally unique</td>
  <td>Users can access Tencent Cloud resources globally with the same account ID.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/416/7594">SSH Key</a> </td>
  <td>skey-xxxxxxxx</td>
  <td>Available in all regions</td>
  <td>Users can use SSH key to bind any CVM in any region under their account.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/213/4939">CVM instance</a> </td>
  <td>ins-xxxxxxxx</td>
  <td>Only available in a single availability zone of a single region</td>
  <td>Users can only create CVM instances under specified availability zones</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/213/4941">Custom image</a> </td>
  <td>img-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>Users can create a custom image for instances, which can be used in different availability zones of the same region. Copy the custom image to other regions using the "Copy Image" feature to use it in those regions.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/213/5733">EIP</a> </td>
  <td>eip-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>Elastic IP address is created under a certain region, and can only be associated with instance in the same region.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/213/5221">Security Group</a> </td>
  <td>sg-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>Security Group is created under a certain region, and can only be associated with instances in the same region. Tencent Cloud automatically creates three default security groups for users.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/362">(Elastic) Cloud Block Storage</a> </td>
  <td>disk-xxxxxxxx</td>
  <td>Available in a single availability zone of a single region</td>
  <td>Elastic Cloud Block Storage can be created independently under an availability zone of a certain region and mounted to instances in the same availability zone.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/362/2455">Snapshot</a> </td>
  <td>snap-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>After creating snapshot for a specific Cloud Block Storage, users can use this snapshot in the region for other operations (such as creating Cloud Block Storage)</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/214/524">Cloud load balancer</a> </td>
  <td>clb-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>Cloud load balancer can be bound with CVMs in different availability zones in a single region for traffic forwarding.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/215/535">VPC</a> </td>
  <td>vpc-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>VPC is created under a certain region. Resources belonging to the same VPC can be created under different availability zones.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/215/4927">Subnet</a> </td>
  <td>subnet-xxxxxxxx</td>
  <td>Only available in a single availability zone of a single region</td>
  <td>Users cannot create a subnet across availability zones.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/document/product/215/4954">Routing table</a> </td>
  <td>rtb-xxxxxxxx</td>
  <td>Available in multiple availability zones of a single region</td>
  <td>When creating a routing table, users need to specify a specific VPC. Thus, the location attribute of the VPC should be followed.</td>
</tr>
</tbody></table>



