# Use CDB to improve the system database's load capacity

The database with excellent performance and scalability can help you quickly improve the load capacity of the original system. With the same size of the database, if CDB is reasonably used, it can help you improve the concurrency of the database to support more visits per second.

## 1. Select a Proper Database Configuration
#### 1.1 Select a database version
In Tencent Cloud, CDB for MySQL currently provides Version 5.5, 5.6 and 5.7 for your selection, which are fully compatible with native MySQL. We strongly recommend you to select Version 5.6 or above, because they are equipped with more stable database kernels, have optimized and improved the design of Version 5.5 and below to improve the performance of the entire system, and provide a number of attractive new features. We will take MySQL Version 5.7 as example to introduce the new features of those new versions.

MySQL Version 5.7 is the latest version currently available from CDB, and is featured with well recognized high performance, good reliability and usability. Some of its optimization and new features are as follows:

##### MySQL Version 5.7 natively supports JSON
In MySQL Version 5.7, a new data type has been added to store data in the JSON format in MySQL tables. The JSON data type natively supported by MySQL Version 5.7 has main advantages as follows:
• Document verification - Only the data segment in line with JSON rules can be written into JSON-type columns, which means that those columns are featured with the JSON syntax verification function.

• Efficient access - It is important to note that when a JSON document is stored in a JSON-type column, the data will not be stored as the plain text. In fact, the data will be stored in the optimized binary format so that it can be accessed by its object members and array elements more quickly.

• Performance - An index can be created among data in JSON-type columns so as to improve query performance. Such index can be achieved through "function index" created on virtual columns.

• Convenience - The inline syntax attached to JSON-type columns can be naturally integrated into document queries in SQL statements. For example, (features.feature is a JSON field):

> SELECT feature->"$.properties.STREET" AS property_street FROM features WHERE id = 121254;

With the help of MySQL Version 5.7, you can seamlessly integrate the best relational example with the best document example in one tool, that is, to use the most proper example out of relational examples and document examples in different applications and use cases, which greatly expands the range of applications for MySQL users.

##### Sys Schema
MySQL SYS Schema is a database schema with a set of objects (views, stored procedures, storage methods, tables and triggers) that were implemented to give easy, readable, DBA and Developer-friendly access to the wealth of monitoring data implemented primarily within Performance Schema, but also with various INFORMATION_SCHEMA tables as well.

MySQL SYS Schema is included MySQL Version 5.7 by default and provides a summary view to answer frequently asked questions as follows:

• "Who takes up all of my data resources provided by database?" 
	
• "Which CVM Server visits the database server most frequently?"

• "Where has the memory on my instances gone?"

##### InnoDB-related improvements
* Online operation of InnoDB (Online DDL): First of all, you can dynamically adjust your Buffer Pool size making it adapt to the change of your needs without restarting MySQL. Secondly, InnoDB can automatically empty InnoDB's UNDO logs and tablespaces on line, thus eliminating one of the common reasons to generate big shared tablespace files (ibdata1). Finally, MySQL Version 5.7 supports the functions of renaming the index and changing the varchar size, both of which are required to recreate the index or table in previous versions.
* InnoDB's native partitioning: In MySQL Version 5.7, InnoDB includes the native support for partitioning. The native partitioning of InnoDB can reduce both the load and memory of up to 90%.
* InnoDB's cache preheating: For now, when MySQL restarts, InnoDB will automatically retain 25% of the hottest data in your cache pool. You do not need to pre-load or preheat your data cache or suffer from any possible performance loss caused by restarting MySQL.

For more information about optimization and new features of MySQL Version 5.7, please [View MySQL's official information](https://dev.mysql.com/doc/refman/5.7/en/mysql-nutshell.html)

#### 1.2 Select an instance specification (database memory)
At present, because CDB for MySQL does not provide a separate CPU option, the CPU will allocate the memory proportionally according to the memory specification. You can purchase an appropriate database specification based on your transaction characteristics. All of our instances have completely undergone standardized tests in order to give you a performance reference for your selection. However, it should be noted that the Sysbench standardized tests do not cover all the transaction scenarios, so we recommend you to make a stress test for the database before your transaction is operated in CDB in order to learn the CDB performance under your transaction scenario.

[View performance description of CDB for MySQL](https://cloud.tencent.com/document/product/236/8842)

The memory is one of the core indicators of the instance and its access speed is far greater than that of the disk. Generally, the more the cached data are stored in the memory, the faster the database response. If the memory is small, after the stored data exceed a certain amount, the excessive data will be stored in the disk. If a new request accesses this data again, the data will be read from the disk into the memory, consuming io of the disk, causing that the database will respond slower than normal.

**For the transaction with large read concurrency or sensitive delay, we recommend you not to choose the memory with small specification so as to ensure the performance of your database.**

#### 1.3 Select a hard disk (data storage space)
The hard disk space of the CDB database instance includes only the MySQL data directory, rather than log space, such as binlog, relaylog, undolog, errorlog and slowlog. When the amount of written data exceeds the instance hard disk space, if the instance failed to be upgraded, the instance might be triggered to be locked. Therefore, when you purchase a hard disk, we recommend you to keep a redundancy for the possible data increase in future so as to prevent the instance from being locked or frequently upgrading due to insufficient space of the hard disk.

#### 1.4 Select a proper data replication method
CDB for MySQL provides three data replication methods, namely the asynchronous, semi-synchronous and strong synchronous data replication. [Learn CDB's data replication methods](https://cloud.tencent.com/document/product/236/7913)

If your transaction is sensitive to write latency or database performance, we recommend you to choose the asynchronous data replication method.

#### 1.5 High availability of the cloud database
The master/slave M-M adopted by CDB for MySQL uses the architecture with high availability, and data synchronization between the master and slave adopts the binlog method. At the same time, the database supports the function that the instance can be restored to any time, which depends on backups and logs. Therefore, you generally do not need to set up a backup and recovery system or pay additional fees to keep your instance highly available.

#### 1.6 Scalability of the cloud database 
All of the different database versions of CDB for MySQL and different memory/drive specifications support online dynamic hot upgrade. The upgrade process will not interrupt your transaction, so you do not need to worry about any database bottlenecks caused by the increased size of your transaction.

#### 1.7 Mixed use of CVM and CDB
In general, you are required to use CVM with CDB after the purchase is successful.
[View how to access CDB with CVM](https://cloud.tencent.com/document/product/236/3130)

## 2. Take Read-only Instances as Read Extension
In the common Internet transaction, the read/write ratio of the database generally lies in between 4:1 and 10:1. In such transaction scenario, the read load of the database is much greater than the write load. When a performance bottleneck occurs, a common solution is to increase the read load.

The read-only instance of CDB for MySQL provides you with a read extension solution. [Learn how to use read-only instances](https://cloud.tencent.com/document/product/236/7270)

Read-only instances can also be used for read-only access of different transactions, for example, the master instance undertakes read/write access for online transactions, and the master instance provides read-only query for internal transactions or data analysis platforms.

## 3. Disaster Recovery Programs of the Cloud Database
CDB for MySQL provides [Disaster recovery instances](https://cloud.tencent.com/document/product/236/7272) to help you build a cross-city remote database disaster recovery with one click.

With the help of disaster recovery instances, multiple data centers in different regions can be redundant each other, so if one data center fails to provide any service due to a failure or a force majeure event, it can be quickly switched to another data center. The disaster recovery instances use the direct connect of Tencent private network to synchronize data so as to eliminate the adverse effect on transactions as much as possible due to late synchronization in the disaster scenario. When the remote service logic is ready, the disaster recovery can be switched in a few seconds.

## 4. 2-Region-3-DC Program
With the help of CDB, a 2-region-3-DC solution can be achieved through a simple configuration of a few steps:

* Purchase local CDB clusters with strong consistency, and select the multi-availability zone deployment (gray release), which provides the 1-region-2-DC capacity.
* Add remote disaster recovery nodes to the cluster, which can build a 2-region-3-DC architecture.

## 5. Use Disaster Recovery Instances to Provide Users with Nearby Access
The disaster recovery instance also has the high-availability architecture as the master/slave M-M, and provides the read-only access capability externally. Therefore, if you need to make users across different regions access to the nearby transaction scenario, you can feel free to use disaster recovery instances.

