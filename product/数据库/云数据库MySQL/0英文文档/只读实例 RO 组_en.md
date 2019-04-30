## Overview
[Tencent Cloud's CDB for MySQL](https://cloud.tencent.com/product/cdb-overview) supports users to create a read-only RO group composed by one read-only instance or multiple read-only instances, which is applicable to users' read-write separation and "One Master, Multi-Slave" application scenarios, thus significantly improving the read load capacity of the users' database.
>**Note:**
> - Before any read-only instance was created, master instances in the cloud database should be created. Please refer to the procedure of how to create a master instance in the cloud database described in the [Purchase and Renewal](/doc/product/236/5160) of Tencent Cloud's CDB for MySQL.
> - Before Tencent Cloud's CBD for MySQL was used, the database needs to be initialized. Please refer to the procedure of how to initialize the described in the [Initialize MySQL Database](/doc/product/236/3128) of Tencent Cloud's CDB for MySQL.

## Operation Steps
### 1. Create a read-only instance
1.1 On the page of [Relational Databases](https://console.cloud.tencent.com/cdb), select the corresponding cloud database in which a read-only instance RO group is going to be created and click "Management" to enter the Instance Management page of the cloud database.
![](//mc.qcloudimg.com/static/img/09c0db073e75d30c287de0f10ffed935/image.png)
1.2 On the management page, click "Add Read-only Instance" to enter the read-only instance management page
![](//mc.qcloudimg.com/static/img/ac1a151fe0079fac79b2901a5f9283bc/image.png)
1.3 On the read-only instance management page, click "New" to create a read-only instance.
![](//mc.qcloudimg.com/static/img/fa84be50d87cd09d0c7f25f16b31ffca/image.png)
1.4 On the pop-up purchase page, select the corresponding configuration of the read-only instance in the cloud database. After everything is checked to be correct, click [Buy Now] to purchase a read-only instance.
- Specify a RO group.

 <table>
  <tr>
    <th width="25%">Specify RO group</th>
    <th width="75%">Description</th>
  </tr>
  <tr>
    <td>No (assigned by system)</td>
    <td>If multiple instances were purchased at one time, each instance will be assigned to a separate RO group. The system will automatically make assignment with the weight method by default.</td>
  </tr>
  <tr>
    <td>Create new RO group</td>
    <td>After you create a new RO group, all of them will be assigned to this RO group if you purchase multiple instances in one time. The system will automatically make assignment with the weight method by default.</td>
  </tr>
  <tr>
    <td>Specify a RO group</td>
    <td>After you specify a RO group, all of them will be assigned to this RO group if you purchase multiple instances in one time. The weight assignment will be configured in the same way with the RO group: if the RO group is set as the automatic system assignment, then the RO group will be automatically added according to the purchased specification; if the RO group is set as the custom assignment, then the default weight is zero. <b>Since the same private network is shared within a RO group, if the VPC network is adopted, the same security group setting will be shared. If a RO group has been specified, it is not possible to customize any security group when purchasing instances.</b></td>
  </tr>
</table>

 ![](//mc.qcloudimg.com/static/img/5db6834345e4087bff22e6c0715eb033/image.png)
 
- Select instance specifications and the required disk.
![](//mc.qcloudimg.com/static/img/ab288476b0ad541d6064d7ef42209836/image.png)
If the specified RO group option is configured as **Create new RO group**, the following information of creating a new RO group should be filled in on the purchase page.
- Set a RO group name: The RO group name does not need to be unique. It can include Chinese characters, English letters, numbers, `-`, `_` and `.` with the length of no more than 60 characters.
- Elimination of instances with a delay timeout: whether to enable the elimination policy. The weight of the eliminated instance is automatically set as zero and a new instance status is added: "in the process of synchronization after service suspension". If a read-only instance was eliminated since its delay exceeds the threshold, an alarm will be issued to the concerning user.
- Delay threshold: The delay threshold is set for read-only instances. If the delay exceed the threshold, the elimination is set. This option must be set. No matter whether the elimination policy is enabled, if the delay exceeds the threshold, an alarm will be issued.
- Minimum retained instances: The minimum number of instances in the group which needs to be ensured. If the number of the existing read-only instances is less than this minimum number, the weight will not be automatically set as zero. This option must be set with a minimum of zero.
![](//mc.qcloudimg.com/static/img/06cf1b511761c3fb35fd08a504af3750/image.png)

1.5 Enter [Cloud Database Console](https://console.cloud.tencent.com/cdb) and find the created instance with the type of **Read-only instance**, which indicates that this read-only instance has been created successfully.
![](//mc.qcloudimg.com/static/img/c43acd917b990016bb418220ee5e18e3/image.png)

### 2. Configure a read-only instance RO group
On the read-only instance RO group configuration page, the basic information of a read-only instance RO group can be configured, including the name, delay timeout policy, delay threshold, minimum retained instances and read weight. The detailed operation procedure is as follows:
2.1 On the page of [Cloud Database Console](https://console.cloud.tencent.com/cdb), select the master instance in the cloud database for creating a read-only instance RO group and click "Management" to enter the Master Instance Management page of the cloud database.
![](//mc.qcloudimg.com/static/img/a4c91d09c83f1e9d6738610ba4d81933/image.png)
2.2 On the cloud database's main instance management page, click "Read-only Instance" to enter the read-only instance RO group management page. 
![](//mc.qcloudimg.com/static/img/edfc8913abe2154244edbb36d01b6fe0/image.png)
2.3 On the read-only instance RO group management page, click "Configuration" to enter the read-only instance RO group configuration page.
![](//mc.qcloudimg.com/static/img/96c1ece808557044fa9f788bf0a36d04/image.png)
2.4 On the read-only instance RO group configuration page, the read-only instance RO group can be configured in details.
![](//mc.qcloudimg.com/static/img/2857c2fd73a6750e32c10667cd0f1f76/image.png)
- Name of a RO group: The RO group name does not need to be unique. It can include Chinese characters, English letters, numbers, `-`, `_` and `.` with the length of no more than 60 characters.
- Elimination of instances with a delay timeout: whether to enable the elimination policy. The weight of the eliminated instance is automatically set as zero and a new instance status is added: in the process of synchronization after service suspension. If a read-only instance was eliminated since its delay exceeds the threshold, an alarm will be issued to the concerning user.
- Delay threshold: The delay threshold is set for read-only instances. If the delay exceeds the threshold, the elimination is set. This option must be set. No matter whether the elimination policy is enabled, if the delay exceeds the threshold, an alarm will be issued.
- Minimum retained instances: The minimum number of instances in the group which needs to be ensured. If the number of the existing read-only instances is less than this minimum number, the weight will not be automatically set as zero. This option must be set with a minimum of zero.
- Read weight assignment: The RO group supports both the system automatically assigned weight and custom weight setting. The weight input must be an integer, ranging from 0 to 100. The list of read weight values of instances which are automatically set by the system is as follows:
<table>
  <tr>
    <th>Configuration Type</th>
    <th>Database type</th>
    <th>Instance Specification</th>
    <th>Weight</th>
  </tr>
  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>1,000 MB memory</td>
		<td>1</td>
  </tr>
  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>2,000 MB memory</td>
		<td>1</td>
  </tr>
  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>4,000 MB memory</td>
		<td>2</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>8,000 MB memory</td>
		<td>2</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>12,000 MB memory</td>
		<td>4</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>16,000 MB memory</td>
		<td>4</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>24,000 MB memory</td>
		<td>8</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>32,000 MB memory</td>
		<td>8</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>48,000 MB memory</td>
		<td>10</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>64,000 MB memory</td>
		<td>12</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>96,000 MB memory</td>
		<td>14</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>128,000 MB memory</td>
		<td>16</td>
  </tr>
	  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>244,000 MB memory</td>
		<td>26</td>
  </tr>  <tr>
    <td>High IO version</td>
    <td>MySQL instance</td>
		<td>488,000 MB memory</td>
		<td>50</td>
  </tr>
</table>
- Load rebalancing:
	- If Load Rebalancing is disabled, modifying weight only takes effect for new loads, neither affecting the read-only instances accessed by the original persistent connection nor causing flash disconnection of database.
	- When Load rebalancing is enabled, flash disconnection will occur to the database to disconnect all connections, and the load of the newly added connection will be balanced according to the set weight.

> **Note:**
> - The read-only instances within the RO group can use different specifications, and the read traffic weight can be set.
> - The read-only instances within the same RO group can support different expiry dates and billing methods.

### 3. Destroy and delete a read-only instance RO group
- The manual delete function is not available to a RO group.
- The RO group will be automatically deleted after the last read-only instance in the group is completely destroyed.
- Any empty RO group is not supported to be retained.

