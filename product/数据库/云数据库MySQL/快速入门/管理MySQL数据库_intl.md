CDB for MySQL management entry enables viewing and modification of database instance details, instance monitoring, parameter configuration, account management, database operations, backup management, as well as download of database operation logs, rollback and upgrade, etc.
1. Instance details. You can view and operate on various information of databases, as shown in the figure below. The public network address is disabled by default, and you need to enable it manually.
![](//mc.qcloudimg.com/static/img/e9ef43b4ac67c30b3200c73b3bd9bf18/image.png)
2. Instance monitoring. You can monitor multiple key indicators running in the current database from the following six dimensions: access, load, query cache, table, Innodb and MyISAM.
The monitoring data items for access include statistics for sql operations such as numbers of slow queries, full table scans, queries, updates, deletions, insertions, and overwrites, total number of requests, number of current connections and connection usage and other server service indicators. With these data, you can get an overall sense of operations currently performed on the database in real time.
The monitoring data items for load include real disk capacity, total disk capacity, volume rate, and sent and received data volume. These data can reflect some indicators such as database space increase, and can be used as the basis for database upgrade.
The monitoring data items for query cache include cache hit rate and cache usage. This indicator reflects the cache efficiency of database. When there is a low cache hit rate, you need to analyze the SQL operations on the service.
The table monitoring contains two indicators: number of temporary tables and number of table lock waits. If there are too many temporary tables, there might be a large number of data table connection operations. In this case, the query efficiency will be severely affected, and you need to optimize the query then.
InnoDB monitoring and MyISAM monitoring are used to monitor the running indicators of these two storage engines respectively, so that the administrators can better understand the running status of the actual table (the above two storage engines may be used).
3. Parameter configuration. You can configure the modifiable parameters in the database and view the modification history, as shown in the figure below:
![](//mc.qcloudimg.com/static/img/a0396cb2820ac3866b7c34f463e8d385/image.png)
4. Account management. You can modify the password of the default root account in the system, as shown in the figure below:
![ ](//mc.qcloudimg.com/static/img/664905c652dbd3ffbe1a1a0ca5622622/image.png)

5. Database operations. You can import sql files into a specified database, as shown in the figure below:
![](//mc.qcloudimg.com/static/img/e8ca6659238a6c00d8db6fa2e5fad1cb/image.png)
6. Backup management. You can download binlog and cold backup, as shown in the figure below:
![](//mc.qcloudimg.com/static/img/9de5e511c57a7d2c8bdfc9c6812e9433/image.png)
7. Operation log. You can download slow query and rollback logs.
8. Upgrade and rollback. Database expansion can be done through upgrading. With cold backup and binlog, you can roll the database back to a specified time.
