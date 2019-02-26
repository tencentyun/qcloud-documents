TencentDB Service for Transmission (DTS) supports data migration and provides continuous data replication from self-built MySQL databases to TencentDB, allowing users to migrate hot data without interrupting their services. Data migration is supported for local IDCs with public IP/Port or access to Tencent Cloud via direct connect, or MySQL databases in Tencent Cloud CVMs.

>Note:
Data migration is only supported for 9.3.x and 9.5.x PostgreSQL databases. Incremental synchronization is not supported for the 9.3.x versions, and is supported for the 9.5.x versions only if an online [sync plug-in][1] is available. For more information on specific configuration, please see [Sync Plug-in Configuration](#.E5.90.8C.E6.AD.A5.E6.8F.92.E4.BB.B6.E9.85.8D.E7.BD.AE).

## Procedure

### Create DTS data migration service
Log in to the console, go to the Data Migration page and click **New Task**.
![](https://mc.qcloudimg.com/static/img/2ad6200dc53556f2c03f45e7a1af8320/image.png)
### Enter configuration
On the page you are redirected to, complete task configuration, source database configuration, and destination database configuration. Details:
![](https://main.qcloudimg.com/raw/19a5f00919d635d96aef413d7a63201f.png)
#### Task configuration
* Task name: Specify a name for the task.
* Execution schedule: Specify a start time for your migration task.
![](https://mc.qcloudimg.com/static/img/6d45bf22f31923704b6055f3f94f1781/image.png)
##### Source database information
* Source database type: PostgreSQL with public IP, Self-built PostgreSQL on CVM, PostgreSQL with access to Tencent Cloud via direct connect and PostgreSQL with access via VPN are supported.
###### PostgreSQL with public IP: PostgreSQL databases that can be accessed via public IP.
Required information:
* CVM address of PostgreSQL
* Port of PostgreSQL
* Account of PostgreSQL
* Password of PostgreSQL
![](https://main.qcloudimg.com/raw/b9135f84c4d8d92d947ebd093cd353f6.png)
###### Self-built PostgreSQL on CVM: CVM-based self-built PostgreSQL databases in both basic networks and VPCs. You need to specify the ID of the CVM instance and the network environment where it is located.
Required information:
* Region: Data migration is only supported when the CVM-based self-built PostgreSQL and the destination TencentDB are in the same region. If the CVM and TencentDB are located in different regions, you need to choose **PostgreSQL with Public IP** and perform migration using CVM public network.
* CVM network: Both basic networks and VPCs are supported.
* VPC: If you select a VPC, you need to select the VPC and subnet to which the instance belongs.
* CVM instance ID
* Port of PostgreSQL
* Account of PostgreSQL
* Password of PostgreSQL
![](https://main.qcloudimg.com/raw/cd7763bdc84eda652493d8ddd6e53f38.png)

###### PostgreSQL via direct connection: You can migrate data to Tencent Cloud using DTS for local IDC self-built PostgreSQL databases connected to Tencent Cloud through the [Direct Connect (DC)][2] service. Required information:
* Direct Connect Gateway: The direct connect gateway used by the database server to connect to Tencent Cloud. [About Direct Connect Gateway][3]
* VPC: The VPC where the direct connect gateway belongs to.
* CVM address of PostgreSQL: The CVM address of PostgreSQL in the IDC. DTS accesses the CVM by mapping with the IP through the direct connect gateway.
* Port of PostgreSQL
* Account of PostgreSQL
* Password of PostgreSQL
	![](https://main.qcloudimg.com/raw/2ed7d52a0c966284d74d78a662adbbe2.png)
		
###### MySQL with access via VPN: You can migrate data to Tencent Cloud using DTS for local IDC self-built PostgreSQL databases connected to Tencent Cloud through [VPN Connection][4] or a self-built VPN service in CVM.
Required information:
* Region: VPN services are only supported if they are in the same region.
* VPN type: [Cloud VPN Service][4] or self-built VPN on CVM.
* VPN gateway: This information is only required for [Cloud VPN Service][4]. [About VPN][5]
* VPC: The VPC where the VPN service belongs.
* CVM address of PostgreSQL: The CVM address of PostgreSQL in the IDC. DTS accesses the CVM by mapping with the IP through the direct connect gateway.
* Port of PostgreSQL
* Account of PostgreSQL
* Password of PostgreSQL
		
![](https://main.qcloudimg.com/raw/7599a0e9665796a1bc3d7e337606fcff.png)

### Select the database to migrate
 Select the database to migrate (you can choose to migrate the entire database or only certain tables), create migration task and check task information.
 ![](https://main.qcloudimg.com/raw/22aeb31026feb69a5478fe04bbcb2049.png)
### Verify migration task information
 After a migration task is created, verify the task information. Click **Next Step: Verification Task** to verify it. You cannot start the task until all the verification items pass. Click **Start** to complete the process.
![](https://main.qcloudimg.com/raw/5eea31c81b6fbf11ce2a800609f1cbbb.png)
There are 3 statuses for task verification:

 - Pass: This means verification is fully passed.
 - Warning: This means that the verification fails. Database operation may be affected during or after data migration, but the migration task can still be executed.
 - Failed: This means that the verification fails, and the migration task cannot be executed. If the verification fails, check and modify the migration task information according to the error entries and then retry the verification.

### Start migration
Once the verification passes, you can click **Start** to start the migration right away. Note that if you have set a specified time for a migration task, the task will be queued and executed at the specified time. Otherwise, it will be executed immediately.
When the migration is started, you can see the corresponding migration progress information under the migration task. Required migration steps and the current stage will be displayed if you move your cursor over the exclamation mark following the steps.
> **Note:**
> Due to system design limitations, multiple migration tasks submitted or queued at the same time will be performed serially based on the queuing time.

### Incremental synchronization
When creating a migration task, the incremental synchronization option is selected by default. When data migration is completed, the target TencentDB for PostgreSQL will be set as the slave database for the source database, and new data of the source database during migration will be synced to the target TencentDB for PostgreSQL via master/slave synchronization. In this case, any changes made to the source database will be synced to the destination TencentDB for PostgreSQL.
After migration, click the **Finish** button to terminate the synchronization relationship between source and destination databases to complete migration.
> **Note:**
> Before terminating synchronization, do not write data into the destination database instance as this may cause data inconsistency between the source and destination databases, which will cause data comparison to fail, resulting in a failed migration.

### Stop migration
To cancel an in-progress migration task, click the **Cancel** button.
![](https://main.qcloudimg.com/raw/48844d9bf0f005015b89c67c67ce0e68.png)

>**Note:**
1. Restarting the task may cause the verification or task to fail. You may need to manually clear all conflicting databases or tables in the destination database to start the migration task again.
2. When migrating a single table, make sure that tables relied on by foreign keys of all tables are migrated.

### Complete migration
![](https://main.qcloudimg.com/raw/4c6727dbdfcc9ced708406ca75ac97eb.png)

## Sync Plug-in Configuration
1. Download and copy [dts_decoding][1] to the lib directory in PostgreSQL installation path.
![](https://main.qcloudimg.com/raw/7958a443bc4564a95242949b2951d648.png)
2. Modify the configuration file "postgresql.conf" under the data directory.
```
wal_level >= logical
 Available  max_replication_slots >=  The number of databases to be migrated
 Available  max_wal_senders       >=  The number of databases to be migrated
 ```
![](https://main.qcloudimg.com/raw/231de9bb2bead27f73beed2a9279eeb4.png)
![](https://main.qcloudimg.com/raw/dd91f8795d5d8a06349e50b99ccb54ce.png)
3. Modify the configuration file "pg_hba.conf" under the data directory.
 replication connection needs to be configured. 
![](https://main.qcloudimg.com/raw/9ea1ec694a672b98f168a81ee7080c6a.png)
4. Restart the source instance.

>Note:
>When specified database table features are used, such as tables using rules or being associated with other tables, inserting data during incremental migration may fail, because some SQL operations are not supported by migration features. If this problem occurs, use schema migration or whole instance migration feature.














[1]:  https://main.qcloudimg.com/raw/97b6b39254c963fcafc228a9c565a2e0.zip
[2]:	https://cloud.tencent.com/product/dc
[3]:	https://cloud.tencent.com/document/product/216/549
[4]:	https://cloud.tencent.com/product/vpn
[5]:	https://cloud.tencent.com/product/vpn
[6]:	https://cloud.tencent.com/document/product/215/4956

