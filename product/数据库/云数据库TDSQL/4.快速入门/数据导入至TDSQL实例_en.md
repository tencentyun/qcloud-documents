You can use Tencent Cloud Database migration tool to migrate business data to CDB for MariaDB (TDSQL). The migration tool migrates data from different types of source databases within the same region to MariaDB (TDSQL). The supported source databases are:
1. Source database from MySQL instance self-built by the Cloud Service in the basic network of Tencent Cloud ([VPC Network](http://cloud.tencent.com/doc/product/215/%E4%BA%A7%E5%93%81%E6%A6%82%E8%BF%B0) to be supported);
2. Source database from CDB for MySQL instance of Tencent Cloud;
3. Source database from another CDB for MySQL (TDSQL) instance;

**To migrate data, follow steps below:**
### 1.1. Go to Migration Tool page
![](//mccdn.qcloud.com/img56835f031e53b.png)

### 1.2. Create a migration task
![](//mccdn.qcloud.com/img56835f3f5fe77.png)
Click to create a migration task, and enter the task name, source database and information on target MariaDB (TDSQL).

![](//mccdn.qcloud.com/img56835f611f583.png)
Select the database to migrate, and then create and check the migration task information.

![](//mccdn.qcloud.com/img56835f91aec32.png)
**Data migration**: Export the data in the selected database and import it into MariaDB (TDSQL).
**Incremental synchronization**: After performing data export and import, set MariaDB (TDSQL) as the slave database of the source database to realize the incremental synchronization of the master and slave.

### 1.3. Verify migration task information
After the creation of a migration task, you need to verify the migration task information. Only after all verification items have passed can the migration task be started. There are three statuses for task verification:
- Pass: indicates that the verification is fully passed.
- Warning: indicates that the verification does not pass. That means, during or after the migration, normal operation of database may be affected, but the implementation of the migration task will not be affected.
- Failed: indicates that the verification does not pass, and the migration cannot be implemented. If the verification fails, check and modify the migration task information according to the error items, and then retry the verification. For reasons of failure, please see "Verification Failure Description".

![](//mccdn.qcloud.com/img56837a4d5ead6.png)

### 1.4. Start the migration
If the verification is passed, you can start the migration task. If you set a specified time for the migration task, the migration task will be queued and executed at the specified time. Otherwise, the migration task will be executed immediately.
After the migration is started, you can see the corresponding migration progress information under the migration task.
![](//mccdn.qcloud.com/img56837a6d2a476.png)
<span style="background-color:#FFFF00">Note: Due to system design constraints, multiple migration tasks submitted or queued at a time will be performed serially based on the queuing time.</span>

### 1.5. Perform incremental synchronization
If you select incremental synchronization option when creating a migration task, upon the completion of data migration, target MariaDB (TDSQL) will be set as the slave database of the source database, and the new data of the source database during the migration will be synchronized to the target MariaDB (TDSQL) via master/slave synchronization. At this point, the modifications in the source database will be synchronized to the target MariaDB (TDSQL). Therefore, you can switch your business to the target MariaDB (TDSQL), and then click "Finish" to complete the migration.
After click to complete migration, the synchronization of master/slave is broken.

### 1.6. Terminate the migration
During the migration process, if you need to terminate the migration, click "Terminate" button to terminate.
![](//mccdn.qcloud.com/img56837a93c69e0.png)
<span style="background-color:#FFFF00">Note: The reboot may cause the failure of verification or task. You may need to manually clear the data in the target database to reboot the migration task.</span>

## 2. Migration Using Third-Party Tools
If your source database is not in Tencent Cloud or any VPC network environment, you can use a third-party tool to export and upload the data from the source database to Tencent Cloud CVM, and then import it into MariaDB (TDSQL).
Common import and export tools are: mysqldump, mydumper, MySQL GUI Tools, etc.

