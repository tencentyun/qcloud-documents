### 1. How to view the parameter list for CDB for MySQL?
You can back up your MySQL data by migrating the data to local machine offline. For more information, please see [Migrate Data Offline](https://cloud.tencent.com/document/product/236/8464).

### 2. How to modify the configuration parameters of a cloud database?

Developers can modify configuration parameters of a cloud database using command line or phpMyAdmin console:

**1. Using command line**
Step 1: Log in to Tencent Cloud [Console](https://console.cloud.tencent.com/), and click "Cloud Database" in "Cloud Products" to go to the relational database page.
![](//mc.qcloudimg.com/static/img/00ff8ac563c02a5f661a1b47284f92dc/image.png)

Step 2: On the relational database page, click "Instance List" under "MySQL", and then locate the MySQL database instance for which you want to reset password in the target region (in this example, it is Guangzhou). Click the instance name or "Manage" button to go to the MySQL database management page.

![](//mc.qcloudimg.com/static/img/62b1e4ab9953e54eab6c53da62ad6436/image.png)
Step 3: On the MySQL database management page, click the parameter settings in the management list. The common variables under var\_name are as follows:
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
**2. Via phpMyAdmin console**
Log in to the cloud database through phpMyAdmin, and click "Variables" on the top menu. Click the "Edit" button next to the variable to be modified in the variable list, modify it, and then click "Save".
![](//mc.qcloudimg.com/static/img/dbe6b04b221424dc11fedd1507e03f09/image.png)
For more information, please see [Modifiable Configurations for Cloud Database](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/cdb_user_modify_var.xls).

### How to set queries for Chinese characters for CDB for MySQL?
CDB does not support Chinese characters now.

### 3. How to enable the scheduler feature for MySQL?
Go to [Cloud Database Console](https://console.cloud.tencent.com/cdb), locate the instance to be modified, click the "Manage" button to go to the database management page. Click "Parameter Settings", and then enable the event in the parameter settings of console.
![](//mc.qcloudimg.com/static/img/3843219af515499661c4335800253c6a/image.png)
   
### 4. How to increase the MySQL connection timeout threshold?
Go to [Cloud Database Console](https://console.cloud.tencent.com/cdb), locate the instance you want to update, click the "Manage" button to go to the database management page. Click "Parameter Settings", and then modify the wait_timeout parameter in the parameter settings of console.
![](https://mc.qcloudimg.com/static/img/e70e9a76b6651794552bd5253099c285/2017-09-01_094218.png)

### 5. How to modify the group_concat parameter for CDB for MySQL?
Go to [Cloud Database Console](https://console.cloud.tencent.com/cdb), locate the instance you want to update, click the "Manage" button to go to the database management page. Click "Parameter Settings", and then modify the group_concat parameter in the parameter settings of console.
![](//mc.qcloudimg.com/static/img/67cfe78563599245bd12c07d55aad191/image.png)

### 6. How to locate the SQL statement for MySQL full table scan?
The statements for full table scan is not recorded by default. You can enable the log_queries_not_using_indexes parameter in parameter settings of cloud database console. Note: Do not keep it enabled for too long.

### 7. How to modify the default character set encoding of a cloud database?
The default character set encoding format of cloud databases is the same with MySQL databases: latin1 (ISO-8859-1 encoding format). Developers can modify the database character set of the server by going to cloud database console. Four character sets are supported now: latin1, gbk, utf8 and utf8mb4. Although the cloud database supports the default character set encoding settings, we recommend that you explicitly specify the encoding for table when creating a table and specify the encoding for connection when the connection is established. This will improve the portability of your applications. For more information on the default character set and how to modify it, please see <a href=https://cloud.tencent.com/document/product/236/7259#6-.E5.AD.97.E7.AC.A6.E9.9B.86.E8.AF.B4.E6.98.8E6"" target="_blank">Use limits on cloud databases</a>. The character set can be modified on the CDB console.
