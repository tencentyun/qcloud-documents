## What is TencentDB Service for Transmission?
TencentDB Service for Transmission (DTS) provides database data transfer service integrated with data migration, data synchronization and data subscription features, helping you achieve database migration without downtime. It also uses a real-time synchronization channel to build a highly available database architecture to allow remote disaster recovery.

DTS is designed to manage complicated data interaction activities for users, allowing them to focus on upper-level business development.


## Features
- Data Migration
Database migration is available for different database types, under different environments. Source databases that are supported for migration include self-built databases in a public network with public IP, self-built databases with access to Tencent Cloud via VPN, direct connection or other network environments, and self-built databases in CVM. Target database is TencentDB instance. Users can check the statuses of all migration tasks and carry out multi-task batch operation.
The data migration feature offered by DTS is the best choice for migrating data onto cloud. Data migration only requires several steps of configuration to help you complete complicated activities for migrating your local data onto the cloud. The migration process does not prevent your source database from providing external service, thereby minimizing the effect on your business caused by the cloud migration task.
- Data Synchronization
The data synchronization feature offered by DTS implements real-time data synchronization between two TencentDB instances and is applicable to scenarios such as remote disaster recovery. Now, data synchronization is only supported for TencentDB for MySQL instances.
- Data Subscription
DTS allows users to acquire real-time incremental update data of a cloud database and also to freely consume incremental data according to their own business demands to achieve various business scenarios, such as implementation of cache update policy, asynchronous businesses decoupling, real-time synchronization of heterogeneous data sources and real-time synchronization of data containing complicated ETL. Users may dynamically add or delete subscription object, view subscription data online and change consumption time point, etc.

