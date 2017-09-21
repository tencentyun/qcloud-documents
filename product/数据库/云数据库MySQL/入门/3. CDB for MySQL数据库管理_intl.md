CDB for MySQL management entry enables viewing and modification of database instance details, instance monitoring, parameter configuration, account management, database operations, backup management, as well as download of database operation logs, rollback and upgrade, etc.
1. Instance details. You can view and operate on various information of databases, as shown in the figure below. The public network address is disabled by default, and you need to enable it manually.
![](https://mccdn.qcloud.com/static/img/c13bba7ad631c3d1b2c5e443daa5b87a/c13bba7ad631.png)
2. Instance monitoring. You can monitor multiple key indicators running in the current database from the following six dimensions: access, load, query cache, table, Innodb and MyISAM.
The monitoring data items for access include statistics for sql operations such as numbers of slow queries, full table scans, queries, updates, deletions, insertions, and overwrites, total number of requests, number of current connections and connection usage and other server service indicators. With these data, you can get an overall sense of operations currently performed on the database in real time.
The monitoring data items for load include real disk capacity, total disk capacity, volume rate, and sent and received data volume. These data can reflect some indicators such as database space increase, and can be used as the basis for database upgrade.
The monitoring data items for query cache include cache hit rate and cache usage. This indicator reflects the cache efficiency of database. When there is a low cache hit rate, you need to analyze the SQL operations on the service.
The table monitoring contains two indicators: number of temporary tables and number of table lock waits. If there are too many temporary tables, there might be a large number of data table connection operations. In this case, the query efficiency will be severely affected, and you need to optimize the query then.
InnoDB monitoring and MyISAM monitoring are used to monitor the running indicators of these two storage engines respectively, so that the administrators can better understand the running status of the actual table (the above two storage engines may be used).
3. Parameter configuration. You can configure the modifiable parameters in the database and view the modification history, as shown in the figure below:
![](https://mccdn.qcloud.com/static/img/f6beb0e4cdec29a45840591f953b7fc5/f6beb0e4cdec.png)
4. Account management. You can modify the password of the default root account in the system, as shown in the figure below:
![](https://mccdn.qcloud.com/static/img/57b01ed76d10689467a612e899d7a075/57b01ed76d10.png)

5. Database operations. You can import sql files into a specified database, as shown in the figure below:
![](https://mccdn.qcloud.com/static/img/5cf4795c885ea7a699dcf5b94a4a725e/5cf4795c885e.png)
6. Backup management. You can download binlog and cold backup, as shown in the figure below:
![](https://mccdn.qcloud.com/static/img/7d52f26467f31898b49c7992a708d8a2/7d52f26467f3.png)
7. Operation log. You can download slow query and rollback logs.
8. Upgrade and rollback. Database expansion can be done through upgrading. With cold backup and binlog, you can roll the database back to a specified time, as shown in the figure below:
https://mccdn.qcloud.com/static/img/2cb7c8818e790b0b54d41143068f3d86/2cb7c8818e79.png
