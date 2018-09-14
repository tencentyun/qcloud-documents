
### What is DTS?
TencentDB Service for Transmission (DTS) provides database data transfer service integrated with data migration, data synchronization and data subscription features, helping you achieve database migration without downtime. It also allows you to use a real-time synchronization channel to easily build a highly available database architecture which supports remote disaster recovery.

### How to use Tencent Cloud DTS?
You can use Tencent Cloud DTS to migrate all your data to the Tencent Cloud-based database at a time, or you can perform continuous data replication. Tencent Cloud DTS captures changes to the source database, and applies them to the destination database in a transaction-consistent manner. For information on how to perform continuous data replication, please see [Data Subscription](https://cloud.tencent.com/document/product/571/8774).

### Can DTS support data migration between TencentDB instances under two different Tencent Cloud accounts?
Yes. For the migration between TencentDB instances cross Tencent Cloud accounts, log in to the DTS with the Tencent Cloud account to which the destination TencentDB instance belongs. And for the source instance type, select the self-built database with public IP.

### Which sources and destinations does Tencent Cloud DTS support?
Tencent Cloud DTS supports MySQL with public IP, MySQL built on CVM, MySQL with Direct Connect, MySQL with VPN access, source database for TencentDB for MySQL, and destination database for TencentDB for MySQL.

### Can the progress of database migration tasks be monitored?
Yes. You can see the progress of the migration tasks on the Tencent Cloud DTS console management page.

### When I use the Tencent Cloud DTS for data migration, will the data of source database be deleted after migration?
No. When DTS performs data migration, it actually copies the data of the source database, without any effect on it.

### Does Tencent Cloud DTS support timed automatic migration?
Yes. After you create Tencent Cloud DTS, you can select the option of timed execution when modifying the configuration, and select the time for timed migration.

### What version of CRS is applicable to migration?
Source instances of version 3.2 or above are not supported for migration.

### What version of MySQL is applicable to migration?
MySQL 5.1/5.5/5.6 is supported for the migration of data to the cloud. Since MySQL 5.1 is no longer supported by Tencent Cloud TencentDB, we recommended that you update MySQL 5.1 to MySQL 5.5 before migrating data to TencentDB for MySQL 5.5. You can also use the DTS data migration tool to directly migrate data from local MySQL 5.1 to Tencent Cloud TencentDB for MySQL 5.5.

### How to check the cause for connectivity failure?
Click **Click to View Details** to view the solution.

### Why is the destination instance unavailable?
The destination instance cannot be used when:
1. The destination instance is not initialized.
2. The destination instance is locked by other tasks.
3. The destination instance has data.
4. The size of data used by the source instance is greater than the capacity of destination instance.

### Why does a warning occur when I verify a task?
You can click **View Details** on the right of the warning item to view the cause and solution.
 
### What causes the error during migration that results in the failure of the migration task?
1. Failed to bgsave the source instance during the migration process.
2. During the migration process, the volume of data written into the source instance is too large and exceeds the configured sync BUFFER, which causes the sync connection to reconnect. The migration task will continue to retry the connection and generate RDB.
 

