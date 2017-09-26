## 1. File Upload Restriction When Using phpMyAdmin

Currently, cloud databases can import/export sql data files through phpMyAdmin. When importing the files to be uploaded, the files must be sql files or compressed (tar, bz2, zip) sql files, and the size of the files must not exceed 2 M.

## 2. How to Get Informed about Insufficient Disk Space

The monitoring center monitors the disk space of the cloud database. When over 90% of the cloud database space is occupied, text message and e-mail alarms will be triggered. You simply need to configure the corresponding alarm recipient in cloud monitoring, and the recipient will receive these alarms in case of insufficient disk space.

## 3. Preparations before Using Cloud Database

Consider the following:

(1) Is DB suitable for your application? For example, "Cloud Memcached", a memory-level persistent storage service, needs to be considered under scenarios with small data volume, large traffic and key-value storage.
(2) Is your database design reasonable? For example, you need to consider splitting tables with obvious access hot spots or large data volume into multiple tables. 

## 4. How Long is the binlog of the Cloud Database Stored?

MySQL binlog will use up large amount of storage, thus the cloud database will only save the binlog for the recent 3 days. In addition, if the data volume of binlog grows too fast and server disk storage is not enough to store the binlog for 3 days, you can delete binlog manually to release storage.

## 5. Diagnosing and Solving Cloud Database Connection Failures

In case of connection failure when using cloud database, check the IP, port, user and password of your cloud database instance first, then log in to the cloud database using the command line on your application machine:

<pre>mysql -h IP -P [port number] -u root -p [cloud database password]
</pre>

Different types of errors and their solutions are shown below:

**(1) ERROR 1045(28000):Access denied for user...**

The message "Access denied for user 'xxx'@'x.x.x.x' (using password:YES)" indicates the password is incorrect.

Please check that the cloud database password you entered is correct. If this error is still shown when the correct information is entered, please [Submit a Ticket](https://console.qcloud.com/workorder) for technical support. 


**(2) ERROR 1040(00000):Too many connections**
The message "ERROR 1040(00000):Too many connections" indicates that the current number of connections to the cloud database instance has exceeded the limit.

Please check the program and properly reduce the number of connections for the database. If this error is still shown after you have reduced the number of connections, please [Submit a Ticket](https://console.qcloud.com/workorder) for technical support. 

**(3) ERROR 2003 (HY000): Can't connect to MySQL server...**

The message "ERROR 2003 (HY000): Can't connect to MySQL server on 'x.x.x.x' (111)" indicates that the connection to cloud database address has failed. Please check whether the cloud database IP and port information you entered is correct. If this error is still shown after the correct information is entered, please [Submit a Ticket](https://console.qcloud.com/workorder) for technical support.

## 6. Business Scenarios that are Suitable for Cloud Database

Cloud databases can be used where MySQL is applicable. Compared to building MySQL on your own, cloud databases are more convenient and reliable to use.

Cloud database is completely compatible with MySQL protocol while providing master-slave hot backup and timed cold backup services. In addition, it supports seamless upgrading of instances so as to reduce investment in deployment, monitoring, expansion, failure recovery, etc. for developers as much as possible, allowing the developers to fully concentrate on product development and operation.

## 7. Difference between Occupied Space and Used Space for Cloud Database

Currently, the actual space used by the user and log data (such as binlog) are calculated separately. The occupied space that is displayed in the cloud database console equals to the used space.

## 8. Is There a Buffer When the Cloud Database is Performing Tasks?

Question Description:

If N SQL statements are sent to the cloud database for execution within a short period, will the cloud database execute them one by one or crash? If it would crash, what is the limit on the number of concurrent connections?

Answer:

MySQL instances provided by cloud database are the same as those you installed on your own. Whether the concurrently executed statements will crash the database depends on system resource and the SQL statements themselves.

If the number of connections max_connections reached its limit, basically this instance will be unable to provide services normally. This is generally caused by the following reasons:

(1) Too many null connections caused by bugs in the business application;

(2) The number of accesses from the front end is far beyond the processing capacity of the instance;

(3) A certain connection executed exclusive resources that take up MySQL for a long time, which caused large amounts of access requests to be blocked.
