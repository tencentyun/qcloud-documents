TencentDB Service for Transmission (DTS) provides the capability to migrate data between MySQL, Redis, and PostgreSQL databases. Read on for more information.
>At present, the data migration capability is only available for MySQL and Redis databases, and will be made available for MongoDB, MariaDB, and other databases. Available soon!

##  MySQL Database Migration
DTS provides continuous data replication from self-built MySQL databases to TencentDBs, allowing users to migrate hot data without interrupting their services. Data migration is supported for local IDCs with public IP/Port or access to Tencent Cloud via direct connection, or MySQL databases in Tencent Cloud CVMs. **MySQL 5.7 does not support DTS, and you can import your data by downloading cold backup files. In addition, DTS is not supported for instances with associated disaster recovery instances. If needed, submit a ticket for data migration.** (An incremental migration may last for a maximum of 15 days. Make sure to click the Complete Migration button after master/slave synchronization is accomplished, or the resource may be reclaimed.)
For more information, please see [Operation Guide-MySQL Data Migration](/document/product/571/13728).

## Redis Migration
The online migration tool does not support migration between Master/Slave, Cluster, and new-generation CRS instances.
For more information, please see [Operation Guide-Redis Data Migration](/document/product/571/13748).
### Notes on Migration
1. You can only migrate instances to Tencent CRS master/slave edition.
2. To ensure efficient migration, cross-region migration is not supported for self-built CVM instances .
3. Migration of self-built CRS 3.2 instances is not allowed by the RDB protocol.
4. For the migration of public network instances, make sure the source instance service is accessible in public network environments.
5. Only migrate instances that are running normally. Instances with an uninitialized password or another task going on cannot be migrated.
6. The destination instance must be an empty instance without any data. Instances in migration will be locked, so no data can be written into them.
7. When the migration succeeds, you can disconnect from the source instance and switch the connection to the destination instance after the data is verified at the business side.

## PostgreSQL Database Migration
DTS supports data migration and provides continuous data replication from self-built MySQL databases to TencentDB, allowing users to migrate hot data without interrupting their services. Data migration is supported for local IDCs with public IP/Port or access to Tencent Cloud via direct connection, or MySQL databases in Tencent Cloud CVMs. Data migration is only supported for 9.3.x and 9.5.x PostgreSQL databases. Incremental synchronization is not supported for the 9.3.x versions, and is supported for the 9.5.x versions only if an online sync plug-in is available.
For more information, please see [Operation Guide-PostgreSQL Data Migration](/document/product/571/16309).
 
 

