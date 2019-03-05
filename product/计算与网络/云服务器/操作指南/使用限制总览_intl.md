## Account Limits for Purchasing CVM Instances

- You need to sign up for a Tencent Cloud account. For more information, please see [Sign up for Tencent Cloud](https://cloud.tencent.com/document/product/378/9603) for registration instructions.
- You need to go through identity verification. For more information on how to verify your identity, please see [Identity Verification Guide](https://cloud.tencent.com/document/product/378/3629).
- When you create a postpaid CVM, the system will freeze the CVM fee for one hour. Make sure that the account has sufficient balance to pay for the order.

## Use Limits for CVM Instances

- Virtualized software cannot be installed or re-virtualized (such as installing VMware or Hyper-V).
- You cannot use sound card applications or external hardware devices (such as ISO files, USB disks, external disks and U-keys).
- The public gateway is available only in Linux systems.

## Purchase Limits for CVM Instances

- For each user in each availability zone, the monthly quota for newly purchased prepaid CVM instances (not net increase) is 150.

- For each user in each availability zone, the **total quota** for postpaid CVM instances is 30.

- For more information, please see [Purchase Limits for CVM Instances](https://cloud.tencent.com/document/product/213/2664).


## Image Limits

- Public image and service marketplace image: none.
- Custom image: Each region supports a maximum of 10 custom images.
- Shared image: Each custom image can be shared to a maximum of 50 Tencent Cloud users, and can only be shared to the accounts in the same region as the source account.
- For more information, please see [Image Type Limits](https://cloud.tencent.com/document/product/213/4941).

## ENI Limits

- The number of ENIs bound to a CVM is quite different from that of private IPs bound to an ENI depending on the CPU and memory configurations. These allowed numbers are shown in the following table:

| CVM Configuration | Max. Number of ENIs | Max. Number of IPs Bound to Each ENI |
| ------------------- | :---- | :------ |
| CPU: 1-core   Memory: 1 GB    | 2     | 2       |
| CPU: 1-core   Memory: > 1 GB   | 2     | 6       |
| CPU: 2-core             |  2     | 10      |
| CPU: 4-core   Memory: < 16 GB | 4     | 10      |
| CPU: 4-core   Memory: > 16 GB | 4     | 20      |
| CPU: 8- to 12-core          | 6     | 20      |
| CPU: >12-core           |  8     | 30      |


## Bandwidth Limits

-  Upper Limit of the Outbound Bandwidth (Downstream Bandwidth):
<table border="3">
    <tr>
       <th rowspan="2"><b>Network Billing Method</b></th> 
       <th colspan="2" ><b>CVM</b></th>
       <th rowspan="2"><b>Available range of the upper limit of bandwidth (Mbps)</b></th>	
   </tr>
    <tr>
       <th><b>CVM Billing Method</b></th> 
       <th><b>CVM Configuration</b></th> 
    </tr>
	<tr>
	      <td rowspan="4">Bill-by-Traffic</td> 
        <td >Postpaid CVM</td> 
        <td >ALL</td> 
				<td>0-100</td>    
   </tr>
	  <tr>
        <td rowspan="3">Prepaid CVM</td> 
        <td>Cores ≤ 8</td> 
				<td>0-200</td>        
   </tr>
	  <tr>
        <td>8 < Cores < 24</td> 
        <td>0-400</td> 
   </tr> 
	 <tr>
        <td>Cores ≥ 24</td> 
        <td>0-400 or no speed limit</td> 
   </tr>
	 <tr>
		    <td rowspan="3">Bill-by-Bandwidth</td> 
        <td >Postpaid CVM</td> 
        <td >ALL</td> 
				<td>0-100</td>      
   </tr>
	 <tr>
		    <td rowspan="2">Prepaid CVM</td> 
        <td >Guangzhou Zone 1<br>Guangzhou Zone 2<br>Shanghai Zone 1<br>Hong Kong Zone 1<br>Toronto Zone 1</td> 
				<td>0-200</td>      
   </tr>
	 <tr>
        <td>Other availability zones</td> 
        <td>0-1,000</td> 
   </tr>
    <tr>
		    <td>Shared bandwidth</td> 
        <td colspan="2">ALL</td> 
        <td>0-200 or no speed limit</td>    
    </tr>
</table>

-  Upper Limit of the Inbound Bandwidth (Upstream Bandwidth):

	- If the fixed bandwidth purchased by users is larger than 10 Mbps, Tencent Cloud assigns the public network inbound bandwidth that is equal to the purchased bandwidth.
	- If the fixed bandwidth purchased by users is less than 10 Mbps, Tencent Cloud assigns 10 Mbps public network inbound bandwidth.

## Disk Limits

| Limits on | Description | 
| --- |  --- |
| Relevant CBS APIs | If an API's name contains "Elastic cloud disk", it means this API can only operate on elastic cloud disks (for example, mounting elastic cloud disks). If the name doesn't contain "Elastic cloud disk", it can operate on all cloud storage (for example, modifying cloud disk attributes). |
| Elastic cloud disk capability | Since November, 2017, all prepaid data disks that are purchased along with CVM are elastic cloud disks. You can unmount them from your CVM and get them remounted. This capability is available in all [Availability Zones](https://cloud.tencent.com/doc/api/229/1286). |
| Regions where SSD Cloud Storage is commercially available | SSD Cloud Storage is commercially available in Guangzhou, Shanghai, Beijing, Singapore, Silicon Valley, and Finance Zone. |
| Cloud disk performance | The I/O performance described in the product documentation. For example, a 1 TB SSD cloud disk can deliver up to 24,000 random IOPS. This means the 24,000 IOPS is achievable for both read and write operations. The I/O performances of 4 KB/8 KB can both reach this number, while the IO of 16 KB cannot reach 24,000 IOPS because its throughput has already reached the limit of 260 MB/s. |
| Maximum number of elastic cloud disks under a single account | 500 at most |
| Maximum number of elastic cloud disks that can be mounted to a single CVM | 10 at most |
| Maximum number of elastic cloud disks allowed for batch operations in a single API request (including operations such as purchasing, mounting, and unmounting) | 10 at most |
| Maximum capacity for an HDD cloud disk (data disk) | 10 GB ~ 16000 GB | |
| Number of snapshots in a single region | Up to (number of cloud disks in the current region\*7) |
| Mounting elastic cloud storage to CVM | The CVM and the elastic cloud storage must be in the same availability zone. |
| Elastic cloud disk billing method | Elastic cloud disks only support prepaid billing. Postpaid billing is not supported. |
| Snapshot rollback | Snapshot data can only be rolled back to the cloud disk from which the snapshot was created. |
| Allowed disk type for creating elastic cloud disks using snapshots | You can only use data disk snapshots to create new elastic cloud disks. |
| Allowed disk size for creating elastic cloud disks using snapshots | The size of the created elastic cloud disk must be bigger or equal to the size of the cloud disk from which the snapshot was created. |
| Retrieving overdue elastic cloud disks | Elastic cloud disks are billed on a prepaid basis. If the associated CVM or elastic cloud disk is overdue, the association will be canceled and the product will be moved into the recycle bin. Auto-renewal policy is enabled by default when mounting elastic cloud disks. This makes sure that you do not experience any interruption in business only because you forget to renew the product. |

## Security Group Limits

- Security groups are region and project-specific. CVMs can only be associated with the security groups in the same region and project.
- Security groups apply to any CVM instances in network environment.
- Each user can set a maximum of 50 security groups for each project in each region.
- A maximum of 100 inbound/outbound access policies can be set for a security group.
- A CVM can be associated with multiple security groups, and a security group can be associated with multiple CVMs. No number limit is imposed.
- Security groups bound with CVMs in **basic network** **cannot filter** data packets sent from (or to) relational database (CDB) and cloud cache service (Redis and Memcached) of Tencent Cloud. If necessary, you can use iptables to filter traffic of such instances.
- The quota limits are as follows:

| Feature | Count | 
|---------|---------|
| Security group | 50/Region |
| Access policy | 100 (Inbound/Outbound) |
| Number of security groups associated with an instance | No limit |
| Number of instances associated with a security group | No limit |

## VPC Limits

| Resource | Limit | 
|---------|---------|
| Number of VPCs in a region |  5	 | 
| Number of subnets per VPC |  10 | 
| Number of basic network CVMs that can be associated with each VPC |  100 |
| Number of routing tables per VPC |  10	 | 
| Number of routing policies per routing table |  50	 | 
| Number of peering connections supported by each VPC |  10 | 
| Number of NAT gateways per VPC |  3 | 
| Number of EIPs per NAT gateway |  10  |
| Maximum forwarding capacity per NAT gateway | 5Gbps|
| Number of VPN gateways per VPC |  10	 | 
| Number of peer gateways in a region |  20 | 
| Number of VPN tunnels per peer gateway |  10 | 
| Number of VPN tunnels that can be created in a VPN gateway |  20	 | 
| Number of SPDs per VPN tunnel |  10 | 
| Number of peer IP address ranges per SPD |  50 | 
| Number of network ACLs per VPC |  50|
| Number of rules per network ACL | Inbound: 20, outbound: 20. |
| Number of associated network ACLs per subnet |  1 |
| Number of associated subnets per network ACL | Unlimited |

## Direct Connect Limits
| Resource | Limit | Description |
|------|-----|-----|
| Physical Direct Connect/User | 10 |  |
| Direct Connect tunnel/Physical Direct Connect | 10  |
| Direct Connect gateway (NAT supported)/VPC | 1  |
| Direct Connect gateway (NAT not supported)/VPC | 1  |
| Local IP translation/Direct Connect gateway | 100 | You can apply for higher quota. |
| Peer IP translation/Direct Connect gateway | 100 | You can apply for higher quota. |
| Number of IPs for local source IP port translation/Direct Connect gateway | 20 | You can apply for higher quota. |
| Local destination IP port translation/Direct Connect gateway | 100 | You can apply for higher quota. |

