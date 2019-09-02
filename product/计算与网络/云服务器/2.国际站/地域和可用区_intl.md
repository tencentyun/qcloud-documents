Tencent Cloud CVM's entrusted data centers are located in different regions around the world, which are all made up of region and availability zone.

Each region is an independent geographical location. Within each region, there are multiple mutually isolated locations referred to as availability zones. Each region is entirely independent. Each availability zone is independent. However, availability zones in the same region can be connected via private network links with low latency.

Tencent Cloud supports distribution of cloud resources in different locations by users. Users are advised to consider placing resources in different availability zones when designing system to shield "service unavailable" status caused by single point of failure.
## Region
Regions are completely isolated with each other, so as to ensure high stability and fault tolerance. Tencent Cloud now have 3 regions in Mainland China and provides nodes in Hong Kong, Singapore and Toronto. You are recommended to choose nearest region to reduce access latency and improve download speed.

Region attribute is differentiated for all behaviors such as enabling and viewing instances by users. If image of the instance that the users need to enable does not exist in the region, then the image needs to be copied to current region. For more information, please see [Copy Image](/doc/product/213/4943).

- Resources in different availability zones of the same region are connected via private network, and can be accessed directly using [Private IP](/doc/product/213/5225).
- Cloud services of different regions <font color="red">cannot communicate via private network by default</font>.
- CVMs cannot access other CVMs, Cloud Database or Cloud Memcached across regions by default.
- When binding Cloud Load Balance to the server, only CVMs in the current region can be chosen;
- Cloud resources on different regions can communicate via [Public IP](/doc/product/213/5224). Cloud Services on VPC can access Internet via [peering connection](/doc/product/215/5000) service. 
- [Cloud Load Balance](https://cloud.tencent.com/doc/product/214) does not support cross-region data forwarding.
- Regions are named by Coverage + City, and availability zones are named by city + serial number.  
- Only resources under the same account can communicate via private network. 

**Notes for Hong Kong region:**

- The following cloud services are temporarily unavailable: Cloud Memcached, elastic web engine, Cloud Object Storage, Cloud Block Storage, one-click opening of server and domain binding with separated regions and servers.
- When you need to log in to CVMs in Hong Kong region, log in via jump server is recommended for better operation and maintenance experience.

**Notes for North America region:**

- The following cloud services are temporarily unavailable: Cloud Memcached, elastic web engine, Cloud Object Storage, mobile acceleration, Cloud Automated Testing, one-click opening of server and domain binding with separated regions and servers.
- Due to the considerable latency between North America and China, when you need to log in to CVMs in North America region, login via jump server is recommended for better operation and maintenance experience.


## Availability Zone
Availability zones (Zone) refer to Tencent Cloud's physical data centers whose power and network are independent from each other within the same region. They are designed to ensure that the failures within an availability zones can be isolated (except for large-scale disaster or major power failure) without spreading to and affecting other zones so that users' businesses can provide continuous online services. By starting an instance in an independent availability zone, users can protect their applications from being affected by the failures occurring in a single location.

When starting an instance, users can choose any availability zone within the specified region. If a user needs to ensure the high reliability of application systems so that the services are still available even when a failure occurs in an instance, the user can use cross-zone deployment scheme (e.g. [Cloud Load Balance](https://cloud.tencent.com/doc/product/214), [Elastic IP](/doc/product/213/5733), etc.) to allow the instance in another availability zone to handle the relevant requests in replace of the failed instance.

### Migrating an instance to another availability zone

Once an instance is started, its availability zone cannot be changed. However you can migrate it to another availability zone. 

1. Create a custom image for the instance (see [Create Custom Image](/doc/product/213/4942)).
2. If the instance is using [Virtual Private Cloud](/doc/product/213/5227) and you want to keep the private IP address after the migration, you can first delete the subnet in the current availability zone and then create a subnet in the new availability zone with the same IP address range as that of the original subnet. Please note that a subnet can be deleted only when it contains no available instances. Thus, all the instances in the current subnet should be migrated to the new subnet.
3. Create a new instance in the new availability zone using the custom image you have just created. User can choose the same type and configuration as those of the original instance, or choose new ones.(see [Purchase and Start an Instance](/doc/product/213/4855)).
4. If an elastic IP address is associated with the original instance, then dissociate it from the old instance and associate it with the new instance (see [Elastic IP](/doc/product/213/5733)).
5. (Optional) For [postpaid](https://cloud.tencent.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9) instances, you can terminate them manually (see [Terminate an Instance](/doc/product/213/4930)). [Prepaid](https://cloud.tencent.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88) instances will be reclaimed automatically after expiration.

## How do I select the region and availability zone?
While purchasing Tencent Cloud services, it is recommended to choose the region that is closest to your customers to minimize the access latency and improve download speed.

## Resource Availability
Specify which resources of Tencent Cloud are global, which resources are regional and not specific to any availability zone and which resources are based on availability zones.

<table>
<tr><th>Resource</th><th>Resource ID Format</th><th>Availability</th><th>Description</th></tr>
<tbody>
<tr>
  <td>User ID</td>
  <td>Not limited</td>
  <td>Cross-region</td>
  <td>Each Tencent Cloud user account is unique and applicable to all resources under the account.</td>
</tr>
<tr>
<td> <a href="/document/product/416/7594">SSH key</a> </td>
  <td>skey-xxxxxxxx</td>
  <td>Cross-region</td>
  <td>You can bind an SSH key pair to any CVM in any region under your account.</td>
</tr>
<tr>
<td> <a href="/doc/product/213/4939">CVM instance</a> </td>
  <td>ins-xxxxxxxx</td>
  <td>One zone only</td>
  <td>A CVM instance is created under a specified availability zone</td>
</tr>
<tr>
<td> <a href="/doc/product/213/4941">Custom Image</a> </td>
  <td>img-xxxxxxxx</td>
  <td>Cross-zone</td>
  <td>A custom image can be used in different availability zones of the same region. You can copy an image to another region.</td>
</tr>
<tr>
<td> <a href="/doc/product/213/5733">Elastic IP</a> </td>
  <td>eip-xxxxxxxx</td>
  <td>Cross-zone</td>
  <td>An EIP is created under a specified region, and can only be associated with instance in the same region.</td>
</tr>
<tr>
<td> <a href="/doc/product/213/5221">Security Group</a> </td>
  <td>sg-xxxxxxxx</td>
  <td>Cross-zone</td>
  <td>A security Group is created under a specified region, and can only be associated with instance in the same region.</td>
</tr>
<tr>
<td> <a href="https://cloud.tencent.com/doc/product/362">(Elastic) Cloud Disk</a> </td>
  <td>disk-xxxxxxxx</td>
  <td>Cross-zone</td>
  <td>Elastic cloud disks can be created independently under a certain region and mounted to instances in the same region. </td>

<td> <a href="https://cloud.tencent.com/doc/product/362/2455">
</tr>
<tr>
<td> <a href="/doc/product/214/524">Cloud Load Balance</a> </td>
  <td>clb-xxxxxxxx</td>
  <td>Cross-zone</td>
  <td>Cloud Load Balance can bind to CVMs in different availability zones in a single region for forwarding traffic.</td>
</tr>
<tr>
<td> <a href="/doc/product/215/535">Virtual Private Cloud (VPC)</a> </td>
  <td>vpc-xxxxxxxx</td>
  <td>Cross-zone</td>
  <td>VPC is created under a certain region. Resources belonging to the same VPC can be created under different availability zones</td>
</tr>
<tr>
<td> <a href="/doc/product/215/4927">Subnet</a> </td>
  <td>subnet-xxxxxxxx</td>
  <td>One zone only</td>
  <td>Users cannot create a subnet across availability zones.</td>
</tr>
<tr>
<td> <a href="/doc/product/215/4954">Routing table</a> </td>
  <td>rtb-xxxxxxxx</td>
  <td>Cross-zone</td>
  <td>When creating a routing table, users need to designate a specific VPC, and therefore location attribute of the VPC should be followed.</td>
</tr>
</tbody></table>

