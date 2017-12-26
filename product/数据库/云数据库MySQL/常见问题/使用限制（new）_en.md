## 1. Limits on data volume

For the reason of limited resources, Tencent imposes limits on the data volume for various MySQL instances. The following describes how an instance or table with a large data volume affect the performance of cloud database:
- **Table with a large data volume**: When a table contains too much data, the cost of MySQL for managing the table resources (data, indexes, etc.) changes, which will affect the efficiency of table processing.
- **Instance with a large data volume**: The default storage engine for cloud database is Innodb. When the cache buffer of Innodb is able to cache all the data and index pages in the instance, the MySQL instance supports a large number of concurrent access requests. If the instance contains too much data, the cache buffer will swap data in/out frequently. In this case, the bottleneck of MySQL shifts to IO soon, leading to the decline of access throughput. For example, for a cloud database instance supporting 8,000 access requests per second, when data volume is twice larger than the cache buffer, the instance can only process 700 access requests per second.

## 2. Limit on number of connections
The maximum number of connections to cloud database is specified with the MySQL system variable max_connections. When the number of connections to a cloud database instance reaches max_connections, no more connection can be established. 
The maximum number of connections to cloud database defaults to 1/5 of the instance memory size, ranging from 10240 to 800. For example, if the instance memory size is 8000 MB, the maximum number of connections defaults to 8000/5=1600. You may modify the max_connections value as needed.
You can set max_connections to 10000 at most in the cloud database console. If you need more connections, submit a ticket for application, and Tencent Cloud will approve or reject your application based on your instance memory size.
However, the more connections, the more system resources are consumed. If the number of connections exceeds the actual load capacity of the system, the service quality of system will be inevitably affected.
For more information on max_connections, please see [Official MySQL Manual](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_max_connections). 

## 3. Limit on the version of MySQL connecting to cloud database

We recommend using the MySQL and library supplied with the CVM system to connect to the cloud database instances.

## 4. Operation limits

4.1. Do not modify the information and permissions of existing accounts for the MySQL instance to prevent some of the cluster services from becoming unavailable.
4.2. It is recommended to use Innodb engine for the creation of both libraries and tables to allow the instance to perform better in case of a high access volume.
4.3. Do not modify or stop master-slave relation to avoid the failure of hot backup.

## 5. About slow log
5.1 Developers using Linux cloud databases can obtain slow logs with the cloud database export tool. For more information, please see <a href="https://cloud.tencent.com/document/product/236/8464" target="_blank">Migrating Data Offline</a>.
5.2 Developers using Windows cloud databases cannot acquire slow logs directly. If necessary, submit a ticket to contact us for the slow logs. 

## 6. Binlog storage duration of cloud database
MySQL binlog takes up a large amount of storage space, thus the cloud database only retains the binlog for the last three days. In addition, if the data volume of binlog grows so fast that the server disk storage is not enough to store the binlog for three days, you can delete binlog manually to free the storage space. 

## 7. Character set

The default character set encoding format of cloud databases is the same with MySQL databases: latin1 (ISO-8859-1 encoding format).
Although cloud database supports the default character set encoding, we recommend that you explicitly specify the encoding for table when creating a table and specify the encoding for connection when the connection is established.
This will improve the portability of your applications.
For more information on the resources of MySQL character set, please see the official MySQL manual. 
The steps for changing cloud database character set are as follows:

1. Execute the following statements to change the default character set encoding for cloud database instance:
```
SET @@global.character_set_client = utf8;
SET @@global.character_set_results = utf8;
SET @@global.character_set_connection = utf8;
SET @@global.character_set_server = utf8;
```
The @@global.character_set_server will be automatically synchronized to local file for persistence in about 10 minutes (the other 3 variables will not). The configured values remain unchanged upon migration or reboot.

2. Execute the following statements to change the character set encoding for the current connection:
```
SET @@session.character_set_client = utf8;
SET @@session.character_set_results = utf8;
SET @@session.character_set_connection = utf8;
```
Or
```
SET names utf8;
```

3. For php programs, you can configure the character set encoding for the current connection by using the following function:
```
bool mysqli::set_charset(string charset);
```
Or
```
bool mysqli_set_charset(mysqli link, string charset);
```
For more information, please see [official MySQL manual](https://dev.mysql.com/doc/connectors/en/apis-php-mysqli.set-charset.html). 

4. For java programs, you can configure the character set encoding for the current connection as shown in the figure below:
```
jdbc:mysql://localhost:3306/dbname?useUnicode=true&characterEncoding=UTF-8
```
For more information, please see [official MySQL manual](https://dev.mysql.com/doc/connectors/en/connector-j-reference-configuration-properties.html). 



