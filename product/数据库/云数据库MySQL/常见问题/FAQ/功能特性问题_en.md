### 1. What business scenarios are cloud database suitable for?
Cloud database can be used wherever MySQL is applicable. Compared to building MySQL by yourself, using cloud database can achieve a higher ease of operation and reliability.
Cloud database is completely compatible with MySQL protocol, while providing master-slave hot backup and scheduled cold backup services. In addition, it supports seamless upgrade of instances to minimize the investment in deployment, monitoring, capacity expansion, and failure recovery, allowing developers to focus on product development and operation.

### 2. What needs to be done before using a cloud database?
The following two questions need to be considered before you use a cloud database:
1. Is DB suitable for your application? For example, for the scenarios with a small data volume, large traffic and key-value storage, it is recommended to use [Cloud Memcached](https://cloud.tencent.com/product/cmem), a memory-level persistent storage service.
2. Does your database have a reasonable design? For example, for a table with obvious access hot spots or large data volume, you need to consider splitting it into multiple tables. 

### 3. How does the cloud database manage MySQL?
Developers do not need to take care of the daily maintenance and adjustment of MySQL, which are carried out by the OPS system of cloud database.
In case of an exception with MySQL, the OPS system can identify and notify it to the OPS personnel immediately. Developers do not need to make any changes.

### 4. Is there a physical machine behind the cloud database?
There is a physical machine behind the cloud database.

### 5. Can the cloud database conduct database sharding and table splitting?
As the standards for database sharding and table splitting are related to business logics, the cloud database does not conduct database sharding and table splitting for businesses.

What is the difference between occupied space and used space of a cloud database?
The actually used space of cloud database users and log data (such as binlog) are calculated separately. The occupied space displayed in the cloud database console equals the used space.

### 6. Is there a buffer when the cloud database is executing a task?
**Description:**
If multiple SQL statements are input in the cloud database for execution in a short period of time, does the cloud database execute them individually or crash? What is the limit on the number of concurrent connections?
**Answer:**
Whether the concurrently executed statements can cause the crash of MySQL instance provided by cloud database depends on system resources and the SQL statements. This is same with conventional MySQL instances installed by yourself.
When the number of connections reaches the limit (max_connections), this instance is unable to provide services normally. This is generally caused by the following reasons:
- Too many null connections caused by bugs in the business application;
- The volume of accesses from the front end is far beyond the processing capacity of the instance;
- A connection which is executed for too long occupies the MySQL resources exclusively, resulting in a large number of blocked access requests.

### 7. What is the limit on the data volume for a cloud database?
See <a href="https://cloud.tencent.com/document/product/236/7259#1-.E6.95.B0.E6.8D.AE.E9.87.8F.E9.99.90.E5.88.B61" target="_blank">Limits on the data volume of cloud databases</a>.

### 8. What are the considerations for using a cloud database?
See <a href="https://cloud.tencent.com/document/product/236/7259#7-.E6.93.8D.E4.BD.9C.E9.99.90.E5.88.B67" target="_blank">Operation limits on cloud databases</a>.

### 9. What is the version of MySQL running in the cloud database?
The MySQL versions used in cloud database are 5.5.45 and 5.6.28.

### 10. How to apply for the enabling/disabling of the slave read-only permission for a cloud database instance?
To enable/disable slave read-only instances, [submit a ticket for application](https://console.cloud.tencent.com/workorder/category) based on the template.

### 11. Is there a limit on the number of connections to a cloud database?
See <a href="https://cloud.tencent.com/document/product/236/7259#2-.E8.BF.9E.E6.8E.A5.E6.95.B0.E9.99.90.E5.88.B62" target="_blank">Limit on the number of connections to a cloud database</a>.

