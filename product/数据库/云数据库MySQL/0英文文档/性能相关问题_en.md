### 1. Why MyISAM engine can not be used?
The reasons why CDB for MySQL does not support MyISAM engine are as follows:
- MyISAM does not support the transaction.
- MyISAM uses table lock mechanism, with a concurrency performance lower than InnoDB.
- MyISAM now can be totally replaced by InnoDB. In the latest official version of CDB for MySQL, MyISAM is no longer used.

### 2. Why does CDB for MySQL crash when it is executing a task?
This is normal because it goes into a status of Lock Wait as the result of concurrent operations. 

### 3. MySQL5.5 has a specification of "High IO, 1,000 MB memory, 45 GB disk, 1,000/sec" - What does 1,000/sec refer to?
1,000/sec refers to the count of operations per second, which is the total number of addition, deletion, modification and query operations. 

### 4 Why do unreadable codes appear in the Chinese data in the cloud database?
Before storing data to the cloud database, the developer should go to [Cloud Database Console](https://console.cloud.tencent.com/cdb) and enter the "Management View" page to view the default character set of this instance. When writing the program, set `character_set_client`, `character_set_results`, and `character_set_connection` to the same character sets for the cloud database instance. Otherwise, unreadable codes will appear if the data to be stored contains Chinese characters.
For example: The default character set of the cloud database instance is utf8. When writing a program to connect the database, you need to execute the following statements before storing the Chinese data to the cloud database.
```
SET NAMES 'utf8';
```
### 5. What are the common reasons and solutions for the maximum number of connections to MySQL is reached?
- Too many sleep threads: It is recommended to decrease the values of wait_timeout and interactive_timeout in console.
- Retention of slow logs: The parameter long_query_time defaults to 10s. It is recommended to modify it to 1-2s and observe slow logs.
- There are few sleep threads and no slow log is retained: It is recommended to increase the max_connections parameter value in console.

### 6. What are the common reasons and solutions for a high utilization of CPU by MySQL?
- Retention of slow logs: Check for slow logs and full table scans in instance monitor, then conduct analysis and optimization by referring to slow logs (can be downloaded on console). If no slow log is found and there are only full table scans in the monitor, modify long_query_time to 1-2s, and then analyze slow logs after using the MySQL for a while.
- No retention of slow logs: Check the memory usage in instance monitor. The fact that it is far higher than the instance specification and the disk read/write count increases significantly indicates a bottleneck of memory. In this case, it is recommended to upgrade the memory.

### 7. How to view MySQL slow logs?
The default slow log threshold (long\_query\_time) of cloud database is 10s. In case of a performance problem, if no slow log is found, you can modify the value to 1-2s.
Log in to Tencent Cloud [Console](https://console.cloud.tencent.com/), and click "Cloud Database" in "Cloud Products" to go to the relational database page.
![Overview](//mc.qcloudimg.com/static/img/d274cc926a10f2b4741d114264f927d5/image.png)
On the relational database page, click "Instance List" under "MySQL", and then locate the MySQL database instance in the target region (in this example, it is Guangzhou). Click the "Manage" button to go to the MySQL database management page.
![Management](//mc.qcloudimg.com/static/img/8216d33e2c5063b13c92e6010a7219d9/image.png)
On the MySQL database management page, click the parameter settings in the management list. The variables to be modified are as follows:
![Parameter Settings](//mc.qcloudimg.com/static/img/a9836f3b39acfdf0f200df22e612d2bd/image.png)
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
View and export slow logs in "Operation Log".
![Operation Log](//mc.qcloudimg.com/static/img/101fd6b1360e3e77e3ba2bd5522fd8e6/image.png)

