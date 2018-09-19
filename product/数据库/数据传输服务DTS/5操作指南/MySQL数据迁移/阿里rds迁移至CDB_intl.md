This document describes how to migrate data from Alibaba Cloud Database (RDS) to Tencent Cloud's TencentDB using the data migration tool DTS provided by Tencent Cloud.

## Environment Requirements
Alibaba Cloud CVM MySQL 5.6 or earlier version.
Tencent Cloud TencentDB MySQL 5.6 instance.

## Procedure

### Obtain the basic information and AccessKey of source database 
 1. Log in to the [RDS Management console][1] and select the destination instance.
 2. You can obtain necessary information on the basic information page of the destination instance, as shown below:
![](https://main.qcloudimg.com/raw/e55af45a5c36a99097418808cc542389.png)
>**Note:**
> Public network addresses provided by Alibaba Cloud need to be converted to IP addresses. Here is an address for [querying IP/server address][2].
 3. Hover the cursor over the profile photo in the upper right corner and choose **accesskeys** in the drop-down box. You can obtain the AccessKey in the page.
	![](https://main.qcloudimg.com/raw/2d67bd05558d5762c322d0c33d344332.png)
	
### Create DTS tasks of Tencent Cloud TencentDB
1. Log in to the console, go to the Data Migration page and click **New Task**.
![](https://mc.qcloudimg.com/static/img/2ad6200dc53556f2c03f45e7a1af8320/image.png)
2. On the page you are redirected to, complete task configuration, source database configuration, and destination database configuration. Details:

![](https://main.qcloudimg.com/raw/27cb0363ec0324605161a4de595c8002.png)
#### Task configuration
* Task name: Specify a name for the task.
* Execution schedule: Specify a start time for your migration task.
![](https://mc.qcloudimg.com/static/img/6d45bf22f31923704b6055f3f94f1781/image.png)
##### Source database information
Select the connection type as needed. Enter the connection information of the corresponding source database.
![](https://main.qcloudimg.com/raw/b099d7a519f80fcdb450e8476a17d314.png)
>**Note:**
> You need to activate a IP whitelist for external mapping by TencentDB in Alibaba Cloud. Otherwise, the connectivity test fails.
>For example:
>1. For the mapping of Tencent Cloud's MySQL with public IP, you need to add the corresponding public IP to Alibaba Cloud's whitelist.
>2. For "direct connect" or "VPN" database configured in DTS configuration, an IP for external mapping will appear after the task is generated. You must add the IP to Alibaba Cloud's whitelist.

##### Destination database information
Select TencentDB instance for the destination instance type and enter the link information of the destination database.
![](https://main.qcloudimg.com/raw/28b1998fd0b7e512be01c281490703bb.png)
### Select the database to migrate
Select the database to be migrated, and then create and check migration task information.
![](https://main.qcloudimg.com/raw/ed8274a0b47d81ecf1466adea1fac10c.png)
#### Data consistency test
Select a data test type. (Choose from whole test or no test.) 
![](https://main.qcloudimg.com/raw/efa134922b1097f832f0c1e41fafaef3.png)
>**Note:**
>The test ratio fields are required for certain test items.

#### Verify migration task information
 After a migration task is created, verify the task information. Click **Next Step: Verification Task** to verify it. You cannot start the task until all the verification items pass. Click **Start** to complete the process.
![](https://main.qcloudimg.com/raw/f0d5e8a304edd34bebe4d21d9ff4746d.png)
There are three statuses for task verification:

 - Pass: This means verification is fully passed.
 - Warning: This means that the verification fails. Database operation may be affected during or after data migration, but the migration task can still be executed.
 - Failed: This means that the verification fails, and the migration task cannot be executed. If the verification fails, check and modify the migration task information according to the error entries and then retry the verification.

### Start migration
Once the verification passes, you can click **Start Migration** to start the migration right away. Note that if you have set a specified time for a migration task, the task will be queued and executed at the specified time. Otherwise, it will be executed immediately.
When the migration is started, you can see the corresponding migration progress information under the migration task. Required migration steps and the current stage will be displayed if you move your cursor over the exclamation mark following the steps.
 
> **Note:**
> Due to system design limitations, multiple migration tasks submitted or queued at the same time will be performed serially based on the queuing time.

### Cancel migration
To cancel an in-progress migration task, click the **Cancel** button.
![](https://main.qcloudimg.com/raw/d57e495a06627c9d10274c3e3ea9beba.png)

### Complete migration
When the migration is 100% complete, click the **Finish** button on the right to complete the migration.
![](https://main.qcloudimg.com/raw/30dbf7018d72cee1daef076323dd5377.png)

>**Note:**
> While the migration is in a status of **Unfinished**, the migration task will continue, so will the database data synchronization.














[1]:    https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Frdsnew.console.aliyun.com%2F%3Fspm%3Da2c4g.11186623.2.5.cdjgiR
[2]:   http://ip.chinaz.com
[3]:   https://console.cloud.tencent.com/dtsnew

