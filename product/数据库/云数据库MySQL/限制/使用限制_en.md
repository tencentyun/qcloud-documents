## Service Limits

### 1. Limits on Data Volume

Due to limited resources, CDB for MySQL imposes restrictions on data volume of all types of MySQL instances to isolate users from getting affected by others. We will now discuss the technical impacts caused by large data volume when using single instance or single table in CDB for MySQL:

**Table with large data volume**: When a table contains too much data, the cost for MySQL to manage the table resources (data, indexes, etc.) will change, which will affect the efficiency when handling the table. For example, when a transaction table (innodb) contains more than 5 G of data, the latency for update operations will increase significantly, affecting the response time for transactions. In this case, we will need to solve this problem by migrating sub-tables.

**Instance with large data volume**: The default storage engine for cloud database is Innodb. When the cache buffer is able to cache all data and index pages in the instance, the MySQL instance will support large amount of concurrent accesses. If the instance contains too much data, the cache buffer will swap data in/out frequently, in which case bottleneck data of MySQL will soon go over to IO, which will reduce throughput. For example, a cloud database instance supports 8,000 accesses per second. When data volume is twice the amount of the cache buffer, it will only support 700 accesses per second instead.

### 2. Limits on Connection Number 

The limit for number of connections for CDB for MySQL equals to the MySQL system variable max_connections. Any new CDB for MySQL instance connections beyond this limit cannot be established.

The default value is 3,000 for large-size cloud databases, 800 for other specifications. Users may adjust the max_connections value according to their own needs.

However, more connections mean more system resources will be occupied. The service performance of the system will be affected if the number of connections goes beyond the actual capacity of the system.

Refer to the MySQL official manual for more information on max_connections. 

### 3. Limits on the Version of the MySQL Client Connecting to the Cloud Database

We recommend that you use the MySQL client and library provided by the CVM system to connect to the cloud database instance.

### 4. About Slow Query

1. Developers using Linux cloud databases can obtain slow query logs with the cloud database export tool. For details, see Cloud Database Data Export.

2. For now, developers using Windows cloud databases cannot acquire slow query logs directly. Please submit a ticket and contact us to obtain slow query log files if necessary. 

### 5. binlog Storage Time of Cloud Database

MySQL binlog will use up large amount of storage, thus the cloud database will only save the binlog for the recent 3 days. In addition, if the data volume of binlog grows too fast and server disk storage is not enough to store the binlog for 3 days, you can delete binlog manually to release storage. 

### 6. Character Set

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

### 7. Operation Restriction

(1) Do not modify information or privilege of existing accounts for the MySQL instance, for this may cause some of the cluster services to become unavailable.

(2) It is recommended to use Innodb engine in a unified manner when creating libraries and tables. This will help instances support more concurrent accesses.

(3) Do not modify or stop master-slave relations, for this may cause the hot backup feature to become unavailable.

### 8. Limits on Database Table Names
Please note that Chinese table names are not supported when creating tables

## Notes

### 1. Database Account Permission
CDB for MySQL will not provide super user permission for users. You need super user permission to modify parameters via "Parameter Configuration" function or by submitting a ticket in the console. Some of the parameters are not subject to modification.

### 2. Database Engine
We recommend InnoDB storage engines to ensure performance and security. MyISAM engine is not supported for CDB for MySQL 5.6 or above.

### 3. Network Selection
For the comparison between the VPC and basic network, please refer to [VPC product documentation](/doc/product/215#2.-.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B8.8E.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C)
As VPC and basic network cannot communicate, instances in each network shall be accessed separately.




