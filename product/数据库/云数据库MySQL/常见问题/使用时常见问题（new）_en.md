## 1. Restrictions on file upload with phpMyAdmin
Cloud database supports importing and exporting SQL data files with phpMyAdmin. The uploaded files to be imported must be SQL files or compressed SQL files (tar, bz2, zip), and cannot be larger than 2 MB.

## 2. How to get informed of insufficient disk space?
The monitoring center monitors the disk space of cloud databases. When over 90% of the cloud database space is occupied, text message and e-mail alarms are triggered. You simply need to configure the alarm recipient in Cloud Monitoring, who will receive the alarms in case of insufficient disk space. For more information on how to configure alarm recipient, please see [Alarm](https://cloud.tencent.com/document/product/236/8457).

## 3. What needs to be done before using a cloud database?
The following two questions need to be considered before you use a cloud database:
1. Is DB suitable for your application? For example, for the scenarios with a small data volume, large traffic and key-value storage, it is recommended to use [Cloud Memcached](https://cloud.tencent.com/product/cmem), a memory-level persistent storage service.
2. Does your database have a reasonable design? For example, for a table with obvious access hot spots or large data volume, you need to consider splitting it into multiple tables. 

## 4. How long is the binlog of a cloud database retained?
MySQL binlog takes up a large amount of storage space, thus the cloud database only retains the binlog for the last five days. In addition, if the data volume of binlog grows so fast that the server disk storage is not enough to store the binlog for five days, you can delete binlog manually to free the storage space.

## 5. Troubleshooting and solutions for cloud database connection failures
In case of a connection failure when using cloud database, check the IP, port, user and password of your cloud database instance first, then log in to the cloud database using the command line on your application machine:
```
mysql -h IP -P [port number] -u root -p [cloud database password]
```
The following lists the common problems and solutions:
```
ERROR 1045(28000):Access denied for user...
```
The message `Access denied for user 'xxx'@'x.x.x.x'(using password:YES)` indicates the password is incorrect. Please verify whether the cloud database password you entered is correct. If this error persists after you enter the correct password, [submit a ticket](https://console.cloud.tencent.com/workorder) for technical support. 
```
ERROR 1040(00000):Too many connections
```
The message `ERROR 1040(00000):Too many connections` indicates the number of connections to the cloud database instance has exceeded the limit.
Check the program and decrease the number of connections to the database as appropriate. If this error persists after you decrease the number of connections, [submit a ticket](https://console.cloud.tencent.com/workorder) for technical support. 
```
ERROR 2003 (HY000): Can't connect to MySQL server...
```
The message `ERROR 2003 (HY000): Can't connect to MySQL server on 'x.x.x.x' (111)` indicates the connection to the cloud database IP failed. Check whether the cloud database IP and port information you entered is correct. If this error persists after you enter the correct information, [submit a ticket](https://console.cloud.tencent.com/workorder) for technical support.

## 6. What business scenarios are cloud database suitable for?
Cloud database can be used wherever MySQL is applicable. Compared to building MySQL by yourself, using cloud database can achieve a higher ease of operation and reliability.
Cloud database is completely compatible with MySQL protocol, while providing master-slave hot backup and scheduled cold backup services. In addition, it supports seamless upgrade of instances to minimize the investment in deployment, monitoring, capacity expansion, and failure recovery, allowing developers to focus on product development and operation.

## 7. What is the difference between occupied space and used space of a cloud database?
The actually used space of cloud database users and log data (such as binlog) are calculated separately. The occupied space displayed in the cloud database console equals the used space.

## 8. Is there a buffer when the cloud database is executing a task?
**Description:**
If multiple SQL statements are input in the cloud database for execution in a short period of time, does the cloud database execute them individually or crash? What is the limit on the number of concurrent connections?
**Answer:**
Whether the concurrently executed statements can cause the crash of MySQL instance provided by cloud database depends on system resources and the SQL statements. This is same with conventional MySQL instances installed by yourself. 
When the number of connections reaches the limit (max_connections), this instance is unable to provide services normally. This is generally caused by the following reasons:
- Too many null connections caused by bugs in the business application;
- The volume of accesses from the front end is far beyond the processing capacity of the instance;
- A connection which is executed for too long occupies the MySQL resources exclusively, resulting in a large number of blocked access requests.

## 9. What is the limit on the data volume for a cloud database?

See <a href="https://cloud.tencent.com/document/product/236/7259#1-.E6.95.B0.E6.8D.AE.E9.87.8F.E9.99.90.E5.88.B61" target="_blank">Limits on the data volume of cloud databases</a>.

## 10. What are the considerations for using a cloud database?
See <a href="https://cloud.tencent.com/document/product/236/7259#7-.E6.93.8D.E4.BD.9C.E9.99.90.E5.88.B67" target="_blank">Operation limits on cloud databases</a>.

## 11. How to log in to a cloud database?
Developers can control and manage MySQL instances through IP/Port without logging in to the server. You can log in to the cloud database through a command line or the cloud database console. For more information, please see <a href="https://cloud.tencent.com/document/product/236/3130" target="_blank">Access MySQL Database</a>.

## 12. Can users modify the configuration of an MySQL instance?
The configurations of MySQL instances are managed centrally by the cloud database. Users can modify some of the parameters. For more information, please see the question [How to modify the configuration parameters of a cloud database](#change_parameter_21).

## 13. How does the cloud database manage MySQL?
Developers do not need to take care of the daily maintenance and adjustment of MySQL, which are carried out by the OPS system of cloud database. In case of an exception with MySQL, the OPS system can identify and notify it to the OPS personnel immediately. Developers do not need to make any changes.

## 14. What is the version of MySQL running in the cloud database?
The MySQL versions used in cloud database are 5.5.45 and 5.6.28.

## 15. Is there a physical machine behind the cloud database?
There is a physical machine behind the cloud database.

## 16. Can the cloud database conduct database sharding and table splitting?
As the standards for database sharding and table splitting are related to business logics, the cloud database does not conduct database sharding and table splitting for businesses.

## 17. Can the default character set encoding of a cloud database be modified?
Yes.
For more information on the default character set and how to modify it, please see <a href=https://cloud.tencent.com/document/product/236/7259#6-.E5.AD.97.E7.AC.A6.E9.9B.86.E8.AF.B4.E6.98.8E6"" target="_blank">Use limits on cloud databases</a>.

## 18. How to view the slow log of a cloud database?
You can obtain the slow log using the data export tool of cloud database. For more information, please see <a href="https://cloud.tencent.com/document/product/236/7274" target="_blank">Downloading Backup Files</a>.

## 19. How can developers back up data?
Cloud database instances are fully backed up every day. Developers can also back up data using the quick multi-thread import/export tool provided by the cloud database (For more information, please see [Manual Backup and Recovery of Cloud Database](https://cloud.tencent.com/document/product/236/7275)), or using the mysqldump tool.

## 20. How to apply for the enabling/disabling of the slave read-only permission for a cloud database instance?
To enable/disable slave read-only instances, submit a ticket for application based on the template.

## 21.<span id="change_parameter_21"></span> How to modify the configuration parameters of a cloud database?

Developers can modify configuration parameters of a cloud database using command line or phpMyAdmin console:

1. Using command line
Click "Go to Console" to go to the [Overview](https://console.cloud.tencent.com/) page:
![Overview](//mc.qcloudimg.com/static/img/e3b4a1474b5d47ded82b5f2c3b534caf/image.png)
In the "Cloud Products in Use" drop-down menu, click "Cloud Database" to go to [MySQL-Instance List](https://console.cloud.tencent.com/cdb):
![Management](//mc.qcloudimg.com/static/img/ca4c7858bcf89a2d0fe97fdcd4754e42/image.png)
Click the parameter setting in the management list. The common variables under var\_name are as follows:
<table class="t">
<tbody><tr>
<th>  Variable
</th><th>  Description
</th></tr>
<tr>
<td> character_set_server
</td><td> Default character set of the server
</td></tr>
<tr>
<td> connect_timeout
</td><td> Connection timeout threshold
</td></tr>
<tr>
<td> long_query_time
</td><td> A query that is executed for a time longer than this value is considered a slow query
</td></tr>
<tr>
<td> max_allowed_packet
</td><td> Maximum packet length
</td></tr>
<tr>
<td> max_connections
</td><td> Maximum number of connections
</td></tr>
<tr>
<td> sql_mode
</td><td> Current server SQL mode
</td></tr>
<tr>
<td> table_open_cache
</td><td> Number of tables opened by all threads. Increasing this value will increase the number of file descriptors that mysqld is requested to open
</td></tr>
<tr>
<td> wait_timeout
</td><td> Timeout threshold of non-interactive connection
</td></tr></tbody></table>
2. Via phpMyAdmin console
Log in to the cloud database through phpMyAdmin, and click "Variables" on the top menu. Click the "Edit" button next to the variable to be modified in the variable list, modify it, and then click "Save".
![](//mc.qcloudimg.com/static/img/dbe6b04b221424dc11fedd1507e03f09/image.png)
For more information, please see [Modifiable Configurations for Cloud Database](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/cdb_user_modify_var.xls).

## 22. Is there a limit on the number of connections to a cloud database?
See <a href="https://cloud.tencent.com/document/product/236/7259#2-.E8.BF.9E.E6.8E.A5.E6.95.B0.E9.99.90.E5.88.B62" target="_blank">Limit on the number of connections to a cloud database</a>.

## 23. How long is the binlog of cloud database retained?
See <a href="https://cloud.tencent.com/document/product/236/7269#5-.E4.BA.91.E6.95.B0.E6.8D.AE.E5.BA.93.E7.9A.84binlog.E4.BF.9D.E5.AD.98.E6.97.B6.E9.97.B4.E8.AF.B4.E6.98.8E5" target="_blank">binlog storage duration of cloud database</a>.

## 24. How long must a query run to be considered a slow query in cloud database?
The default slow query time threshold (long\_query\_time) of cloud database is 10 seconds. You can modify it in parameter configuration in the same way as configuring parameters using command line. For more information, please see [MySQL Database](https://cloud.tencent.com/document/product/236).
Click "Go to Console" to go to the [Overview](https://console.cloud.tencent.com/) page:

![Overview](//mc.qcloudimg.com/static/img/33ad26ed6b2fde8caad10566c7e21206/image.png)
In the "Cloud Products in Use" drop-down menu, click "Cloud Database" to go to [MySQL-Instance List](https://console.cloud.tencent.com/cdb):

![Management](//mc.qcloudimg.com/static/img/0513c3baad993254f80fbd0be0825f96/image.png)

Click the parameter setting in the management list to modify the following variable:
<table>
<tbody><tr>
<th>  Variable
</th><th>  Description
</th></tr>
<tr>
<td> long_query_time
</td><td> A query that is executed for a time longer than this value is considered a slow query
</td></tr>
</tr></tbody></table>

## 25. Why do unreadable codes appear in the Chinese data in the cloud database?
Before storing data to the cloud database, the developer should go to [Cloud Database Console](https://console.cloud.tencent.com/cdb) and enter the "Management View" page to view the default character set of this instance. When writing the program, set character\_set\_client, character\_set\_results, and character\_set\_connection to the same character sets for the cloud database instance. Otherwise, unreadable codes will appear if the data to be stored contains Chinese characters.
For example: The default character set of the cloud database instance is utf8. When writing a program to connect the database, you need to execute the following statements before storing the Chinese data to the cloud database.
```
SET NAMES 'utf8';
```

## 26. How to export database data?
1. To export cold backup data, download the data in "Backup Management" in the console.
2. To export real-time data, you can purchase read-only instances, and get the data through the read-only instance mysqldump.

