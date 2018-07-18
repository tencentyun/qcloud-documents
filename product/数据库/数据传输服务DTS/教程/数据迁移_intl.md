TencentDB Service for Transmission (DTS) provides data migration and continuous data replication from self-built MySQL databases to TencentDB, allowing users to migrate hot data without interrupting their services. Data migration is supported for local IDCs with public IP/Port or access to Tencent Cloud via direct connect, or MySQL databases in Tencent Cloud CVMs.** MySQL 5.7 does not support DTS, and you can import your data by downloading cold backup files.**



## 1. Preparation
### 1.1 Note
- A DTS data migration task involves two steps: cold backup data export and incremental data synchronization. **Cold backup data export and migrated data comparison have certain effect on the load of the source database**, so it is recommended to perform database migration during off-peak hours or in the standby database.

- **Only certain database table migration tasks restart target TencentDB instance at the beginning of incremental synchronization and after migration task is completed. The source database is not affected.**

- **Super permission for the source instance is required**

### 1.2 Super permission for source instance
For accounts to be used for migration, it is recommended to acquire the Super permission for the source instance. The Super permission is required in the following scenarios:
-  Before data migration is completed, DTS will check data consistency, which requires the Super permission to change the "session" parameter and "binlog_format".
-  **If, during binlog synchronization, a user creates an Event in the source instance and an account that is not used for DTS data migration is specified as DEFINER for this event, an error will occur if the Super permission is unavailable.**

### 1.3 Databases supported for migration
- Data migration from self-built CVM MySQL databases in basic and VPC networks to TencentDB instances.

- Data migration from MySQL databases with public network IP/Port to TencentDB instances.

- Data migration from MySQL databases with access to Tencent Cloud via VPN or direct connect to TencentDB instances.

### 1.4 Check the following in advance
1. Check if any database table with the same name as the target TencentDB instance exists, to avoid conflict.
2. Check database version. Cloud migration is supported for MySQL 5.1/5.5/5.6. As MySQL 5.1 is no longer supported by Tencent Cloud TencentDB, it is recommended that you update MySQL 5.1 to MySQL 5.5 first, then migrate data to TencentDB for MySQL 5.5. You can also use the DTS data migration tool to directly migrate data from local MySQL 5.1 to Tencent Cloud TencentDB for MySQL 5.5.
3. Check the capacity of the destination TencentDB instance, which must be larger than that of the source instance;
4. Create a migration account in the source MySQL database (this is not required if you already have an authorized account for data migration).
		
			GRANT ALL PRIVILEGES ON *. * TO "migration account" @ "%" IDENTIFIED BY "migration password";

			FLUSH PRIVILEGES;	
  
5. Confirm source database MySQL variables
	  Use `SHOW GLOBAL VARIABLES LIKE 'XXX'`; 
	  
	  to check MySQL global variables, so as to confirm whether migration can be performed under the current status:
		
            server_id > 1
            
            log_bin = ON;
            
            binlog_format = ROW/MIXED
            
            binlog_row_image = FULL
            
            innodb_stats_on_metadata = 0
            
            It is recommended that wait_timeout is higher than or equal to 3,600 seconds, and it must be lower than 7,200 seconds.
            
            The same time length is configured for interactive_timeout and wait_timeout.
            
            If the source instance is slave, confirm the following parameters in the source instance:
            
            log_slave_updates = 1           
		
6. Change variable value:

	a. Change the source database MySQL configuration file `my.cnf`, and restart:
	
		        log-bin=[custom binlog file name]
		        
	B. Modify configuration dynamically:
         
                set global server_id = 99;
                
                set global binlog_format=ROW;
               
                set global binlog_row_image=FULL;
                
                set global innodb_stats_on_metadata = 0;
		

## 2. Steps

### 2.1 Create DTS data migration service
Log in to the console, go to the Data Migration page and click **New Task**.
![](https://mc.qcloudimg.com/static/img/2ad6200dc53556f2c03f45e7a1af8320/image.png)

### 2.2 Enter configuration
On the page you are redirected to, complete task configuration, source database configuration, and destination database configuration. Details:
![](https://mc.qcloudimg.com/static/img/513a6893e79862359ee52fd6d2d97c5b/image.png)

#### Task configuration
	
* Task name: Specify a name for the task.
* Execution schedule: Specify a start time for your migration task.
![](https://mc.qcloudimg.com/static/img/6d45bf22f31923704b6055f3f94f1781/image.png)

##### Source database information
* Source database type: MySQL with public IP, Self-built MySQL on CVM, MySQL with access to Tencent Cloud via direct connect and MySQL with access via VPN are supported.
###### MySQL with public IP: MySQL databases that can be accessed via public IP.
Required information:
* CVM address of MySQL
* Port of MySQL
* Account of MySQL
* Password of MySQL
		
![](https://mc.qcloudimg.com/static/img/d7ea867e99cf6dcaeea777f1f8a498e2/image.png)
		
###### Self-built MySQL on CVM: CVM-based self-built MySQL databases in both basic networks and VPCs. You need to specify the ID of the CVM instance and the network environment where it is located.
Required information:
* Region: Data migration is only supported when the CVM-based self-built MySQL and the destination TencentDB are in the same region. If the CVM and TencentDB are located in different regions, you need to choose **MySQL with Public IP** and perform migration using CVM public network.
* CVM network: Both basic networks and VPCs are supported.
* VPC: If you select a VPC, you need to select the VPC and subnet to which the instance belongs.
* CVM instance ID
* Port of MySQL
* Account of MySQL
* Password of MySQL
			
![](https://mc.qcloudimg.com/static/img/1f7d1837b9c18ae22835460215c48daf/image.png)
	
###### MySQL connected via Direct Connect: You can migrate data to Tencent Cloud using DTS for local IDC self-built MySQL databases connected to Tencent Cloud through the [Direct Connect (DC)][1] service. Required information:
* Direct Connect Gateway: The direct connect gateway used by the database server to connect to Tencent Cloud. [About Direct Connect Gateway][2]
* VPC: The VPC where the direct connect gateway belongs to.
* CVM address of MySQL: The CVM address of MySQL in the IDC. DTS accesses the CVM by mapping with the IP through the direct connect gateway.
* Port of MySQL
* Account of MySQL
* Password of MySQL
	
![](https://mc.qcloudimg.com/static/img/4d6317bb20e5551f9a5ff58218ae9c18/image.png)
		
###### MySQL with access via VPN: You can migrate data to Tencent Cloud using DTS for local IDC self-built MySQL databases connected to Tencent Cloud through [VPN Connection][3] or a self-built VPN service in CVM.
Required information:
* Region: VPN services are only supported if they are in the same region.
* VPN type: [Cloud VPN Service][3] or self-built VPN on CVM.
* VPN gateway: This information is only required for [Cloud VPN Service][3]. [About VPN][4]
* VPC: The VPC where the VPN service belongs.
* CVM address of MySQL: The CVM address of MySQL in the IDC. DTS accesses the CVM by mapping with the IP through the direct connect gateway.
* Port of MySQL
* Account of MySQL
* Password of MySQL
		
![](https://mc.qcloudimg.com/static/img/dd72353254680fb09b2d004c50d33c01/image.png)

### 2.3 Select the database to migrate
 Select the database to migrate (you can choose to migrate the entire database or only certain tables), create migration task and check task information.

>**Note:**
> 1. The character_set_server and lower_case_table_names configuration items are migrated only when the whole instance is migrated.
> 2. If the character set configuration of migrated tables for the source instance is different from that of the destination instance, the character set configuration of the source instance is retained.
		
![](https://mc.qcloudimg.com/static/img/4c944c5a4b9871eb971c22a4344933a5/image.png)

**Data migration**: Export data from the selected database and import it to TencentDB for MySQL.
**Incremental synchronization**: After performing data export and import, configure TencentDB for MySQL as the slave database for source database to achieve incremental synchronization between master and slave.
**Overwrite root account**: Since the root account is used for security verification for cloud databases, subsequent TencentDB operations will be affected if no root account exists in the source database. Therefore, if the entire instance is migrated, you should specify whether to overwrite the destination database root account with the source database root account. Choose **Yes** if you want to use the root account of the source database or if no root account is configured for the destination database. Choose **No** if you want to retain the root account for the destination database.

### 2.4 Data consistency test
Select a data test type. (Choose from whole test, partial test, or no test.) 
![](https://mc.qcloudimg.com/static/img/6c49e44bbc5c289f218892290ea396e7/image.png)

>**Note:**
>The test ratio fields are required for certain test items.

### 2.5 Verify migration task information
 After a migration task is created, verify the task information. Click **Next Step: Verification Task** to verify it. You cannot start the task until all the verification items pass. Click **Start** to complete the process.
![](https://mc.qcloudimg.com/static/img/f71f17469f53e1d7a32d4c836ce7ef4d/image.png)
There are 3 statuses for task verification:

 - Pass: This means verification is fully passed.
 - Warning: This means that the verification fails. Database operation may be affected during or after data migration, but the migration task can still be executed.
 - Failed: This means that the verification fails, and the migration task cannot be executed. If the verification fails, check and modify the migration task information according to the error entries and then retry the verification. To view the cause of failure, please see "Verification Failure Description".

### 2.6 Start migration
Once the verification passes, you can click **Start Migration** to start the migration right away. Note that if you have set a specified time for a migration task, the task will be queued and executed at the specified time. Otherwise, it will be executed immediately.
When the migration is started, you can see the corresponding migration progress information under the migration task. Required migration steps and the current stage will be displayed if you move your cursor over the exclamation mark following the steps.
> **Note:**
> Due to system design limitations, multiple migration tasks submitted or queued at the same time will be performed serially based on the queuing time.

### 2.7 Incremental Synchronization
When creating a migration task, the incremental synchronization option is selected by default. When data migration is completed, the target TencentDB for MySQL will be set as the slave database for the source database, and new data of the source database during migration will be synced to the destination TencentDB for MySQL via master/slave synchronization. In this case, any changes made to the source database will be synced to the destination TencentDB for MySQL.
After migration, click the **Stop** button to terminate the synchronization relationship between source and destination databases, then switch the service to the destination the TencentDB for MySQL instance to complete migration.
> **Note:**
> Before terminating synchronization, do not write data into the destination database instance as this may cause data inconsistency between the source and destination databases, which will cause data comparison to fail, resulting in a failed migration.


### 2.8 Stop migration
To cancel an in-progress migration task, click the **Cancel** button.
![](https://mc.qcloudimg.com/static/img/2c7a3c1534676cf9753010e986681938/image.png)

>**Note:**
1. Restarting the task may cause the verification or task to fail. You may need to manually clear all conflicting databases or tables in the destination database to start the migration task again.
2. When migrating a single table, make sure that tables relied on by foreign keys of all tables are migrated.

### 2.9 Complete migration
When the migration is 100% complete, click the **Finish** button on the right to complete the migration.
![](https://mc.qcloudimg.com/static/img/1fff643dd6dd18a8c678e7ae1462d317/image.png)

>**Note:**
> While the migration is in a status of **Unfinished**, the migration task will continue, so will the database data synchronization.





[1]:	https://cloud.tencent.com/product/dc
[2]:	https://cloud.tencent.com/document/product/216/549
[3]:	https://cloud.tencent.com/product/vpn
[3]:	https://cloud.tencent.com/product/vpn
[4]:	https://cloud.tencent.com/document/product/215/4956

[img-creat0]: //mc.qcloudimg.com/static/img/d782322e94fc253a41f95e642f794b32/create0.png
[img-creat1]: //mc.qcloudimg.com/static/img/123cd23d3449cd5497502d8572f4b0a0/creat1.png
[img-creat2]: //mc.qcloudimg.com/static/img/8b75f2ad6610107c0856ea5e335c5923/create3.png
[img-init1]:  //mc.qcloudimg.com/static/img/cb72f72cf07d6b72c516d17d8ae8a114/init1.png
[img-init2]:  //mc.qcloudimg.com/static/img/3085341d195ecd9c0b5e130d86634e5e/init2.png
[img-init3]:  //mc.qcloudimg.com/static/img/5662f6a28286a2bb7ec3d1506206b5c7/init3.png
[img-init4]:  //mc.qcloudimg.com/static/img/2973c030e020d1a6e18ea882c062c741/init4.png
[img-init5]:  //mc.qcloudimg.com/static/img/f4f7f8156acd6899bcc534aa3913fa18/init5.png
[img-init6]:  //mc.qcloudimg.com/static/img/2402e535c9e893ba899ccf756e0c204c/init6.png
[img-init7]:  //mc.qcloudimg.com/static/img/d745dd9b585ca0a62cc30cabb1f31a3c/init7.png
[img-init8]:  //mc.qcloudimg.com/static/img/21effe29a213a3d3315ee776b8eed362/init8.png

