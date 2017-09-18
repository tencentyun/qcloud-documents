## 1. Data Volume Limit

Due to limited resources, Tencent has imposed limits on data volume of all types of MySQL instances on the business aspect. We will now discuss the technical impacts caused by large data volume when using single instance or single table in cloud database:

**Table with large data volume**: When a table contains too much data, the cost for MySQL to manage the table resources (data, indexes, etc.) will change, which will affect the efficiency when handling the table. For example, when a transaction table (innodb) contains more than 5 G of data, the latency for update operations will increase significantly, affecting the response time for transactions. In this case, we will need to solve this problem by migrating sub-tables.

**Instance with large data volume**: The default storage engine for cloud database is Innodb. When the cache buffer is able to cache all data and index pages in the instance, the MySQL instance will support large amount of concurrent accesses. If the instance contains too much data, the cache buffer will swap data in/out frequently, in which case bottleneck data of MySQL will soon go over to IO, which will reduce throughput. For example, a cloud database instance supports 8,000 accesses per second. When data volume is twice the amount of the cache buffer, it will only support 700 accesses per second instead.

## 2. Limit on Number of Connections

The limit for number of connections for cloud database equals to the MySQL system variable max_connections. Any new cloud database instance connections beyond this limit cannot be established.

The default value is 3,000 for large-size cloud databases, 800 for other specifications. Users may adjust the max_connections value according to their own needs.

However, more connections means more system resources will be occupied. The service performance of the system will be affected if the number of connections goes beyond the actual capacity of the system.

Refer to the MySQL official manual for more information on max_connections. 

## 3. Limit on the Version of the MySQL Client Connecting to the Cloud Database

We recommend that you use the MySQL client and library provided by the CVM system to connect to the cloud database instance.

## 4. About Slow Query

1. Developers using Linux cloud databases can obtain slow query logs with the cloud database export tool. For details, see Cloud Database Data Export.

2. Currently, developers using Windows cloud databases cannot acquire slow query logs directly. Please submit a ticket and contact us to obtain slow query log files if necessary. 


## 5. binlog Storage Time of Cloud Database

MySQL binlog will use up large amount of storage, thus the cloud database will only save the binlog for the recent 3 days. In addition, if the data volume of binlog grows too fast and server disk storage is not enough to store the binlog for 3 days, you can delete binlog manually to release storage. 

## 6. Character Set

The default character set encoding format of cloud databases is the same with MySQL databases: latin1 (ISO-8859-1 encoding format).

You may configure the default character set encoding setting for cloud databases, but it is recommended that you specify the encoding for tables explicitly when creating the tables, and specify the encoding for connections when establishing the connections.

This will improve the portability of your applications.

Refer to the MySQL official manual for relevant resources about MySQL character set. 

Here are the steps for changing cloud database character set:

(1) Execute the following command to change the default character set encoding for cloud database instance:
```
SET @@global.character_set_client = utf8;
SET @@global.character_set_results = utf8;
SET @@global.character_set_connection = utf8;
SET @@global.character_set_server = utf8;
```

The @@global.character_set_server will be automatically synchronized to local file for persistence in approximately 10 minutes (the other 3 variables will not). The configured value will be retained upon migration or reboot.

(2) Execute the following command to change the character set encoding for the current connection:
```
SET @@session.character_set_client = utf8;
SET @@session.character_set_results = utf8;
SET @@session.character_set_connection = utf8;
```

Or
```
SET names utf8;
```

(3) For php programs, you can configure the character set encoding for the currently connection by using the following function:
```
bool mysqli::set_charset(string charset);
```
Or
```
bool mysqli_set_charset(mysqli link, string charset);
```

For details, refer to the MySQL official manual. 

(4) For java programs, you can configure the character set encoding for the currently connection by using the following:
```
jdbc:mysql://localhost:3306/dbname?useUnicode=true&characterEncoding=UTF-8
```

For details, refer to the MySQL official manual. 

## 7. Operation Restriction

(1) Do not modify information or privilege of existing accounts for the MySQL instance, for this may cause some of the cluster services to become unavailable.

(2) It is recommended to use Innodb engine in a unified manner when creating libraries and tables. This will help instances support more concurrent accesses.

(3) Do not modify or stop master-slave relations, for this may cause the hot backup feature to become unavailable.

## 8. Limits on High-performance Version

### 8.1 InnoDB Storage Format

For InnoDB storage engine, high-performance cloud databases use DYNAMIC format by default. Users are advised not to modify this format in order to avoid affecting normal usage. 

### 8.2 Maximum Number of Concurrent Transactions Supported

Cloud databases support a maximum of 1,000 concurrent transactions. 

### 8.3 Maximum In-row Record Length Supported by InnoDB

The maximum in-row record length supported by high-performance InnoDB is 1,982 bytes. The following error will occur if this limit is exceeded:
```
ERROR 1118 (42000): Row size too large. The maximum row size for the used table type, not counting BLOBs, is 1982. You have to change some columns to TEXT or BLOBs
```

Users are advised to keep the storage length of in-row records as short as possible. For example, try to declare the length of varchar fields as 256 or above (in which case the fields will be stored outside rows), or use text/blob as replacement. 
