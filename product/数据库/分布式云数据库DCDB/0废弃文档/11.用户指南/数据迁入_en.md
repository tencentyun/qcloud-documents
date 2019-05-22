## 1. Import Through Tencent Cloud Migration Tool
You can use Tencent Cloud Database migration tool to migrate business data to CDB for TDSQL. The migration tool migrates data from different types of source databases within the same region to TDSQL. The supported source databases are:
1. Source databases from MySQL instances built by cloud services within Tencent Cloud basic network ([VPC Network](http://cloud.tencent.com/doc/product/215/%E4%BA%A7%E5%93%81%E6%A6%82%E8%BF%B0) will become supported soon);
2. Source databases from CDB for MySQL instances in Tencent Cloud;
3. Source databases from another CDB for TDSQL instance;

**Steps for data migration:**
### (1) Go to Migration Tool Page
![](//mccdn.qcloud.com/img56835f031e53b.png)

### (2) Create a Migration Task
![](//mccdn.qcloud.com/img56835f3f5fe77.png)
Click **Create Migration Task**, enter task name, source database and target TDSQL information.

![](//mccdn.qcloud.com/img56835f611f583.png)
Select the database to be migrated, create and check migration task information.

![](//mccdn.qcloud.com/img56835f91aec32.png)
**Data migration**: Export the data in the selected database and import it into TDSQL.
**Incremental synchronization**: After data export and import, set TDSQL as the slave database of the source database to realize master-slave incremental synchronization.

### (3) Verify Migration Task Information
When migration task is created, you need to verify the migration task information and start the task only if all verification items pass. There are three statuses for task verification:
- Pass: This means verification is fully passed.
- Warning: This means that the verification did not pass. Database operation may be affected during or after data migration, but the migration task can still be executed.
- Failed: This means that the verification did not pass, and the migration task cannot be executed. If verification fails, check and modify the migration task information according to the error entries and then retry the verification. To view the cause of failure, refer to: "Verification Failure Description".

![](//mccdn.qcloud.com/img56837a4d5ead6.png)

### (4) Start Migration
If verification passes, you can start the migration task. If you set a specified time for the migration task, it will be queued and executed at the specified time. Otherwise, the migration task will be executed immediately.
When the migration is started, you can see the corresponding migration progress information under the migration task.
![](//mccdn.qcloud.com/img56837a6d2a476.png)
Note: Due to system design limitations, multiple migration tasks submitted or queued at the same time will be performed serially based on the queuing time.

### (5) Incremental Synchronization
If you selected Incremental Synchronization option when creating a migration task, the target TDSQL will be set as the slave database of the source database upon completion, and new data of the source database during the migration process will be synchronized to the target TDSQL via master-slave synchronization. At this point, any changes to the source database will be synchronized to the target TDSQL. Therefore, you can switch your business to the target TDSQL and click **Finish** to complete the migration process.
By doing so, the master-slave synchronization relationship will be cancelled.

### (6) Terminate Migration
During migration, if you need to terminate the process, click the **Terminate** button.
![](//mccdn.qcloud.com/img56837a93c69e0.png)
Note: Restarting the task may cause verification or task to fail. You may need to manually clear all data in the target database to start the migration task again.

## 2. Migration by Third-Party Tools
If your source database is not in Tencent Cloud or any VPC network environment, you can use a third-party tool to export and upload data from the source database to Tencent Cloud CVM, and then import it into TDSQL.
Common import and export tools include mysqldump, mydumper, MySQL GUI Tools, etc.

