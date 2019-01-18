The TencentDB Service for Transmission (DTS) supports data migration feature and provides continuous data replication feature from self-built MySQL database to TencentDB, allowing users to carry out hot data migration without interrupting their services. Data migration is supported for local IDCs with public IP/Port or Tencent Cloud direct connection access, or MySQL databases in Tencent Cloud CVMs. **MySQL5.7 does not support data transfer service for now, and you can import the data by downloading cold backup file.**

## 1. Preparation
### 1.1 Note
- DTS data migration task includes two steps: cold backup data export and incremental data synchronization. **Cold backup data export and migrated data comparison process have certain effect on the load of the source database**, thus it is recommended to perform database migration during off-peak hours or in the standby database.

- **Only certain database table migration tasks restart target TencentDB instance at the beginning of incremental synchronization and after migration task is completed. The source database is not affected.**

- **Super permission for the source instance is required**

### 1.2 Super Permission for Source Instance
For accounts that are used for migration, it is recommended to acquire super permission for the source instance. There are mainly the following scenarios where super permission is required:
-  Before data migration is completed, DTS will check data consistency which requires super permission to change the "session" parameter and "binlog_format".
-  **If, during binlog synchronization, a user creates an Event in the source instance and an account that is not used for DTS data migration is specified as DEFINER for this event, an error will occur if super permission is unavailable.**

### 1.3 Database Supported for Migration
- Data migration from self-built CVM MySQL databases in basic network and VPC network to TencentDB instances.

- Data migration from MySQL databases with public network IP/Port to TencentDB instances.

- Data migration from MySQL databases with access to Tencent Cloud via VPN or direct connection to TencentDB instances.

### 1.4 Check the Following Items in Advance
1. Check if any database table with the same name as the target TencentDB instance exists, to avoid conflict;
2. Check database version. Cloud migration is supported for MySQL 5.1/5.5/5.6. As MySQL 5.1 is no longer supported by Tencent Cloud TencentDB, it is recommended that you update MySQL 5.1 to MySQL 5.5 first, then migrate data to TencentDB for MySQL 5.5. Of course, you can also use DTS data migration tool to directly migrate data from local MySQL 5.1 to Tencent Cloud TencentDB for MySQL 5.5.
3. Check the capacity of target TencentDB instance, which must be larger than that of the source instance;
4. Create a migration account in the source MySQL database (this is not required if you already have an authorized account for data migration);
		
			GRANT ALL PRIVILEGES ON *. * TO "migration account" @ "%" IDENTIFIED BY "migration password";

			FLUSH PRIVILEGES;	
  
5. Confirm source database MySQL variables
	  Use `SHOW GLOBAL VARIABLES LIKE 'XXX'`; 
	
	  Check MySQL global variables to confirm whether migration can be performed under the current status:
		
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

	a.  Change the source database MySQL configuration file `my.cnf`, and restart:
	
		        log-bin=[custom binlog file name]
	
	b. Modify configuration dynamically:
         
                set global server_id = 99;
                
                set global binlog_format=ROW;
               
                set global binlog_row_image=FULL;
                
                set global innodb_stats_on_metadata = 0;
	

## 2. Steps

### 2.1 Create DTS Data Migration Service
Log into the console, go to Data Migration page and click "New Task".
![][img-creat0]
Select your desired region and quantity.
![][img-creat1]
After purchasing DTS instance, click "Modify Configuration" to enter the task creation process
![][img-creat2]


### 2.2 Modify Configuration
Click "Modify Configuration", enter task name and information of the source database and target TencentDB for MySQL instance. Details:

#### Task Configuration

* Name of task: Specify a name for the task.
* Execution schedule: Specify a start time for your migration task.

##### Source Database Information
* Source database type: Four types of source databases are supported for now: MySQL with public IP, self-built MySQL on CVM, MySQL with access to Tencent Cloud via direct connection, and MySQL with access via VPN.
###### MySQL with public IP: MySQL databases accessible via public IP.
Required information:
* Address of the MySQL host
* Port of MySQL
* Account of MySQL
* Password of MySQL
		
![][img-init1]
		
###### Self-built MySQL on CVM: CVM-based self-built MySQL databases in basic network and VPCs are both supported. You need to specify the CVM instance ID and the network environment to use the self-built MySQL.
Required information:
* Region: Now, data migration is only supported when the CVM-based self-built MySQL and target TencentDB are in the same region. If CVM and TencentDB are located in different regions, you need to choose "MySQL with Public IP" to perform migration using CVM public network.
* CVM network: Basic network and VPC are supported.
* VPC: If you select VPC, you need to select the VPC and subnet where the instance belongs to.
* CVM instance ID
* Port of MySQL
* Account of MySQL
* Password of MySQL
			
![][img-init2]
	
###### MySQL via direct connection: You can migrate data to Tencent Cloud using DTS data migration for local IDC self-built MySQL that accesses Tencent Cloud through [Direct Connect (DC)][1] service. Required information:
* Direct connection gateway: The direct connection gateway used by the database server to access Tencent Cloud. [About Direct Connection Gateway][2]
* VPC: The VPC where the direct connection gateway belongs to.
* Address of MySQL host: The address of MySQL host in the IDC. DTS data migration accesses the host by mapping with the IP through direct connection gateway.
* Port of MySQL
* Account of MySQL
* Password of MySQL
	
![][img-init3]
		
###### MySQL with access via VPN: You can migrate data to Tencent Cloud using DTS data migration for local IDC self-built MySQL that accesses Tencent Cloud through [VPN Connection][3] or self-built VPN service in CVM.
Required information:
* Region: For now, VPN services are only supported if they are in the same region.
* VPN type: [Cloud VPN Service][3] or self-built VPN on CVM.
* VPN gateway: This information is only required for [Cloud VPN Service][3]. [About VPN][4]
* VPC: The VPC where VPN service belongs to.
* Address of MySQL host: The address of MySQL host in the IDC. DTS data migration accesses the host by mapping with the IP through direct connection gateway.
* Port of MySQL
* Account of MySQL
* Password of MySQL
		
![][img-init4]

### 2.3 Select the Database to Migrate
 Select the database to migrate (you can choose to migrate the entire database on only certain tables), create migration task and check task information.

>**Note:**
> 1. The character_set_server and lower_case_table_names configuration items are migrated only when the whole instance is migrated.
> 2. If character set configuration of migrated tables for the source instance is different from that of the target instance, the character set configuration of source instance is retained.

![][img-init6]
![][img-init5]

**Data migration**: Export data in the selected database and import it into TencentDB for MySQL.
**Incremental synchronization**: After performing data export and import, configure TencentDB for MySQL as the slave database for source database to achieve incremental synchronization between master and slave.
**Overwrite root account**: Since root account is used for security verification for cloud database, subsequent TencentDB operations will be affected if root account does not exist in the source database. Therefore, if the entire instance is migrated, you should specify whether to overwrite the target database root account with the source database root account. Choose "Yes" if you want to use root account of the source database or if root account is not configured for target database. Choose "No" if you want to retain the root account of target database.

### 2.4 Verify Migration Task Information
 When migration task is created, you need to verify the migration task information and start the task only if all verification items pass. There are three statuses for task verification:

 - Pass: This means verification is fully passed.
 - Warning: This means that the verification did not pass. Database operation may be affected during or after data migration, but the migration task can still be executed.
 - Failed: This means that the verification did not pass, and the migration task cannot be executed. If verification fails, check and modify the migration task information according to the error entries and then retry the verification. To view the cause of failure, refer to "Verification Failure Description".

### 2.5 Start Migration
If verification passes, you can click "Start Migration" to start data migration right away. Note: if you set a specified time for the migration task, it will be queued and executed at the specified time. Otherwise, the migration task will be executed immediately.
When the migration is started, you can see the corresponding migration progress information under the migration task. Required migration steps and the current stage will be displayed if you move your cursor over the exclamation mark following the steps.
![][img-init7]
> **Note:**
> Due to system design limitations, multiple migration tasks submitted or queued at the same time will be performed serially based on the queuing time.

### 2.6 Incremental Synchronization
When creating a migration task, the incremental synchronization option is selected by default. When data migration is completed, the target TencentDB for MySQL will be set as the slave database for the source database, and new data of the source database during migration will be synchronized to the target TencentDB for MySQL via master/slave synchronization. In this case, any changes made to the source database will be synchronized to the target TencentDB for MySQL.
After migration, you can click the "Stop" button to terminate the synchronization relationship between source and target databases, then switch service to the target TencentDB for MySQL instance to complete the migration process.
> **Note:**
> Before terminating synchronization, do not write data into the target database instance as this may cause data inconsistency between source and target databases which will cause data comparison to fail, resulting in a failed migration.


### 2.7 Stop Migration
During migration, if you need to terminate the process, click the "Terminate" button.
![][img-init8]

>**Note:**
1. Restarting the task may cause verification or task to fail. You may need to manually clear all conflicting databases or tables in the target database to start the migration task again.
2. When migrating a single table, it is necessary to ensure that tables relied on by foreign keys of all tables are also migrated.

	1]:	https://cloud.tencent.com/product/dc
	2]:	https://cloud.tencent.com/document/product/216/549
	3]:	https://cloud.tencent.com/product/vpn
	3]:	https://cloud.tencent.com/product/vpn
	4]:	https://cloud.tencent.com/document/product/215/4956

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
