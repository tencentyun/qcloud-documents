### 1. How to connect to MySQL if CVM and cloud database are deployed in the same region?
When the CVM and cloud database are deployed in the same region, you can access MySQL via private network. For more information on the connection method, please see [Access MySQL Database](https://cloud.tencent.com/document/product/236/3130).

### 2. How to connect to MySQL if CVM and cloud database are deployed in different regions?
When the CVM and cloud database are deployed in different regions, you can access MySQL via public network. For more information on the connection method, please see [Public Network Access](https://cloud.tencent.com/document/product/236/9038).

### 3. Why does the PING test for the connectivity between the CDB and CVM under the same account in the same region (Shanghai Zone 1) fail?
By default, Ping command is not allowed for CDB. You can use telnet to test the connectivity.

### 4. How to access CDB for MySQL via public network?
For more information on public network access, please see [Public Network Access](https://cloud.tencent.com/document/product/236/9038).

### 5. How to access CDB for MySQL via private network?
For more information on private network access, please see [Assess MySQL Database](https://cloud.tencent.com/document/product/236/3130).

### 6. Troubleshooting and solutions for cloud database connection failures
When you fail to connect and log in to a cloud database, test the connectivity of network port of the cloud database using telnet command, and then log in to the cloud database on your CVM using command lines (The default account of cloud database is root, and the password is same as the one set in the initialization steps described above):
```
mysql -h [cloud database IP] -P[port of cloud database] -uroot -p[cloud database password]
```
The following are common errors and solutions:
1. When the message "ERROR 1045(28000):Access denied for user..." appears, verify whether the cloud database account and password you entered are correct. If you forget the password, please see [Preset Password](https://cloud.tencent.com/document/product/236/10305). If the error persists after you enter the correct information again, check whether restrictions are imposed on the IPs accessing your instance by going to "[MySQL Console](https://console.cloud.tencent.com/)" -> "Instance" -> "Account Management".
2. The message "ERROR 1040(00000):Too many connections" indicates that the number of current connections to the cloud database instance exceeds the limit. The common reasons and solutions are as follows:
(1) Too many sleep threads: It is recommended to decrease the values of wait_timeout and interactive_timeout in console. 
(2) Retention of slow logs: The parameter long_query_time defaults to 10s. It is recommended to modify it to 1-2s and observe slow logs.
(3) There are few sleep threads and no slow log is retained: It is recommended to increase the max_connections parameter value in console.
3. When the message "ERROR 2003 (HY000): Can't connect to MySQL server..." appears, verify whether the cloud database IP and port information you entered are correct. If the error persists after you enter the correct information again, check the security group policies of the instance in console to verify whether the CVM has the permission to access the CDB. For more information, please see [Operation Guide for Cloud Database Security Group](https://cloud.tencent.com/document/product/236/10636).
