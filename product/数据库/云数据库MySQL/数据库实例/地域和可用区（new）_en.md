Tencent Cloud's database hosting data centers are distributed in different locations worldwide, which are divided into regions and availability zones.
Each region is an separate geographic area and has multiple isolated locations known as availability zones. The name of a region or an availability zone defines the coverage of the data center within the region or availability zone. To make it easy for customers to understand the name of a region or an availability zone, region is named in the structure of "coverage range + city where the data center is located" (where "coverage range" represents the coverage capability of the data center and "city where the data center is located" indicates the city where the data center is located or near to), and availability zone is named in the structure of "city + No.". Each availability zone is isolated, but the availability zones in a region are connected through low-latency private network links.
Tencent Cloud allows you to distribute your cloud resources in multiple locations. You are advised to consider placing resources in different availability zones when you design the system, to avoid Service Unavailable caused by single point of failure.
Region and Availability Zones:
<table class="table-striped">
	<tbody>
		<tr>
			<th>&nbsp;</th>
			<th>Region</th>
			<th>Availability Zone</th>
		</tr>
		<tr>
			<td rowspan="13">Mainland China</td>
			<td rowspan="3">South China (Guangzhou) <br> ap-guangzhou</td>
			<td>Guangzhou Zone 1 (Sold out) <br> ap-guangzhou-1</td>
		</tr>
		<tr>
			<td>Guangzhou Zone 2 <br> ap-guangzhou-2</td>
		</tr>
		<tr>
			<td>Guangzhou Zone 3 <br> ap-guangzhou-3</td>
		</tr>
		<tr>
			<td rowspan="2">South China (Shenzhen Finance) <br> ap-shenzhen-fsi
</td>
			<td>Shenzhen Finance Zone 1 (only financial institutions and enterprises can submit tickets for application) <br> ap-shenzhen-fsi-1</td>
			</tr>
			<tr>
			<td>Shenzhen Finance Zone 2 (only financial institutions and enterprises can submit tickets for application) <br> ap-shenzhen-fsi-2</td>
			<tr>
		
		<tr>
			<td rowspan="2">East China (Shanghai) <br> ap-shanghai</td>
			<td>Shanghai Zone 1 <br> ap-shanghai-1</td>
		</tr>
			<tr>
			<td>Shanghai Zone 2 <br> ap-shanghai-2</td>
		   </tr>
		
			
		</tr>
		<tr>
			<td rowspan="2">East China (Shanghai Finance) <br> ap-shanghai-fsi</td>
			<td>Shanghai Finance Zone 1 (only financial institutions and enterprises can submit tickets for application) <br> ap-shanghai-fsi-1</td>
		</tr>
		<tr>
			<td>Shanghai Finance Zone 1 (only financial institutions and enterprises can submit tickets for application) <br> ap-shanghai-fsi-2</td>
		   </tr>
		<tr>
			<td rowspan="2">North China (Beijing) <br> ap-beijing</td>
			<td>Beijing Zone 1 <br> ap-beijing-1</td>
		</tr>
			<tr>
			<td>Beijing Zone 2 <br> ap-beijing-2</td>
		   </tr>
		</tr>
		
		<tr>
			<td rowspan="1">Southwest (Chengdu) <br> ap-chengdu</td>
			<td>Chengdu Zone 1 <br> ap-chengdu-1</td>
		</tr>
		
		<tr>
			<td rowspan="4">Overseas</td>
			<td>Southeast Asia (Hong Kong) <br> ap-hongkong</td>
			<td>Hong Kong Zone 1 (Hong Kong node is available in Southeast Asia) <br> ap-hongkong-1</td>
		</tr>
		<tr>
			<td>Southeast Asia (Singapore) <br> ap-singapore</td>
			<td>Singapore Zone 1 (Singapore node is available in Southeast Asia)<br> ap-singapore-1</td>
		</tr>
		<tr>
			<td>North America (Toronto) <br> na-toronto</td>
			<td>Toronto Zone 1 (Toronto Zone node is available in North American) <br> na-toronto-1</td>
		</tr>
		<tr>
			<td>Western U.S. (Silicon Valley) <br> na-siliconvalley</td>
			<td>Silicon Valley Zone 1 (Silicon Valley node is available in Western U.S.)<br> na-siliconvalley-1</td>
		</tr>
	</tbody>
</table>

## Region
Different regions of Tencent Cloud are completely isolated to ensure maximal stability and fault tolerance among those regions. South China, East China, and North China are covered domestically, and Hong Kong and Singapore nodes for South East Asia and Toronto node for North America are also available. We will gradually increase available nodes to cover more regions. You're recommended to choose the region closest to your customers to minimize access latency and improve download speed. Actions such as enabling and viewing instances vary in different regions.
Notes about communication between cloud products via private network:
- Even located in different availability zones, cloud resources in the same region are connected via private network, and can be accessed directly via [Private IP][2].
- Cloud products of different regions **cannot communicate via private network by default**.
 - A CVM cannot access other CVM, Cloud Database or Cloud Memcached across regions by default.
 - When binding load balance service to a CVM, you can only bind to a CVM in the same region.
- Cloud resources of different regions can perform Internet access via [Public IP][3]. Cloud Services in VPC can also communicate via [Peering connections][4] provided by Tencent Cloud using Tencent Cloud high-speed connected network, to realize connection that is more stable and faster than Internet access.
- [Cloud Load Balance][5] does not support cross-region traffic forwarding.

The above private network interconnection refers to the interconnection among resources under the same account. Private networks for resources under different accounts are completely isolated.

**Special Notes About Hong Kong Region:**
- The following cloud services are temporarily unavailable in Southeast Asia and Hong Kong region: Cloud Memcached, Cloud Elastic Engine, Cloud Object Storage, Cloud Block Storage, One-click Start-up of Server, and Binding of Domains by Regions and Servers.
- When you need to log in to CVMs in Hong Kong, login via a jump server is recommended for better operation and maintenance experience.

**Special Notes About North America Region:**
- The following cloud services are temporarily unavailable in North America region: Cloud Block Storage, Cloud Elastic Engine, Cloud Object Storage, Mobile Acceleration, Cloud Automated Testing, One-click Start-up of Server, and Binding of Domains by Regions and Servers.
- Due to the considerable latency between North America and China, when you need to log in to CVMs in North America region, login via a jump server is recommended for a better operation and maintenance experience.

**Special Notes About Shanghai Finance Zone:**
Compliance zone customized according to regulatory requirements of finance industry features high level of security and isolation. The available services are CVM, finance database, Redis storage, face recognition, etc. Verified clients in finance industry can apply for the zone by submitting tickets. For more information, please see [About Finance Zone][6].

## Availability Zone
Availability zones (Zones) refer to Tencent Cloud physical data centers in the same region with independent power and network resources. They are designed to ensure that the failures within an availability zone can be isolated (except for large-scale disaster or major power failure) without spreading to and affecting other zones, so as to ensure users' business stability. By starting an instance in an independent availability zone, users can protect their applications from being affected by the failures occurring in a single location.
When enabling an instance, users can choose any availability zone within the specified region. If a user needs to ensure the high reliability of application systems so that the services are still available even when a failure occurs in an instance, the user can use cross-zone deployment scheme (e.g. [Cloud Load Balance][7], [Elastic IP][8], etc.) to allow the instance in another availability zone to handle the relevant requests in place of the failed instance.

## Guide on Selecting Region or Availability Zone
When you purchase Cloud services, it is recommended to choose the region that is closest to your customers to minimize the access latency and improve download speed.


[1]:	/doc/product/213/4943
[2]:	/doc/product/213/5225
[3]:	/doc/product/213/5224
[4]:	/doc/product/215/5000
[5]:	https://cloud.tencent.com/doc/product/214
[6]:	http://cloud.tencent.com/doc/product/304/%E9%87%91%E8%9E%8D%E4%BA%91%E7%AE%80%E4%BB%8B
[7]:	https://cloud.tencent.com/doc/product/214
[8]:	/doc/product/213/5733

