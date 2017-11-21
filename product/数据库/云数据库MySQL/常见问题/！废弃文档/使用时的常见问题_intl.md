## 1. What business scenarios are cloud databases applicable to?

Cloud databases can be used where MySQL is applicable. Compared to building MySQL on your own, cloud databases are more convenient and reliable to use.

Cloud database is completely compatible with MySQL protocol while providing master-slave hot backup and timed cold backup services. In addition, it supports seamless upgrading of instances so as to reduce investment in deployment, monitoring, expansion, failure recovery, etc. for developers as much as possible, allowing the developers to fully concentrate on product development and operation.



## 2. What preparations need to be made before a cloud database is used?

The developer needs to consider:

(1) whether DB is suitable for your application? For example, "Cloud Memcached", a memory-level persistent storage service, needs to be considered under scenarios with small data volume, large traffic and key-value storage.

(2) whether your database design is reasonable? For example, you need to consider splitting tables with obvious access hot spots or large data volume into multiple tables. 

## 3. What are the limits on data volume for cloud databases?

For details, refer to [Limits on Cloud Database Data Volume](/document/product/236/7269#1-数据量限制)

## 4. What are the considerations for using a cloud database?
For details, refer to [Limits on Operations of Cloud Database][1]

## 5. How to log in to a cloud database?

Developers can completely control and manage MySQL instances through IP/Port without logging in to the server.

You can log in to the cloud database through a command line or the cloud database console. For details, refer to: Log in to Cloud Database.

## 6. How to authorize other users to work with the cloud database?

root users can authorize other users using the grant command of mysql, but cannot do so using "grant all" command.

Currently, "shutdown" and "file" permissions are not available to root users, so you cannot create users with all permissions through root.

Please refer to the following commands for authorization:
```
grant SELECT,INSERT, UPDATE, DELETE, CREATE, DROP, ALTER on *.* to 'myuser'@'%' identified by 'mypasswd';
```

## 7. Can I modify the configuration of a MySQL instance on my own?

The configurations of MySQL instances are managed uniformly by the cloud database, and modification of some parameters is supported. For details, see question #21. How to modify the configuration parameters of the cloud database?

## 8. How does the cloud database manage MySQL?

Developers do not need to conduct daily maintenance and adjustment on MySQL, which are carried out by the O&M system of the cloud database.

When an exception arises in MySQL, the O&M system will detect it instantly and notify the O&M personnel to address it. Developers do not need to make any changes.

## 9. What is the version of MySQL running in the cloud database?

The versions of MySQL used in the cloud database are 5.5.45 and 5.6.28.

## 10. Is there a buffer when the cloud database is performing a task?

Question Description:

If N SQL statements are sent to the cloud database for execution within a short period, will the cloud database execute them one by one or crash? If it would crash, what is the limit on the number of concurrent connections?

Answer:

MySQL instances provided by cloud database are the same as those you installed on your own. Whether the concurrently executed statements will crash the database depends on system resource and the SQL statements themselves.

If the number of connections max\_connections reaches its limit, basically this instance will be unable to provide services normally. This is generally caused by the following reasons:

(1) Too many null connections caused by bugs in the business application;

(2) The number of accesses from the front end is far beyond the processing capacity of the instance;

(3) A certain connection executed exclusive resources that take up MySQL for a long time, which caused large amounts of access requests to be blocked.

## 11. Diagnosing and solving cloud database connection failures

In case of connection failure when using cloud database, check the IP, port, user and password of your cloud database instance first, then log in to the cloud database using the command line on your application machine:
```
mysql -h IP -P [port number] -u root -p [cloud database password]
```

Different types of errors and their solutions are shown below:
```
(1) ERROR 1045(28000)：Access denied for user...
```
The message "Access denied for user 'xxx'@'x.x.x.x' (using password:YES)" indicates the password is incorrect.

Please check whether the cloud database password you entered is correct. If this error is still shown after correct information is entered, please submit a ticket to contact technical support. 

```
(2) ERROR 1040(00000):Too many connections
```
The prompt "ERROR 1040(00000):Too many connections" means that the current number of connections for the cloud database instance has exceeded the limit (For details about the maximum number of connections for the cloud database instance, see here).

Please check the program and properly reduce the number of connections for the database. If this error is still shown after the number of connections is reduced, please submit a ticket to contact the technical support. 

```
(3) ERROR 2003 (HY000): Can't connect to MySQL server...
```

The message "ERROR 2003 (HY000): Can't connect to MySQL server on 'x.x.x.x' (111)" indicates that the connection to cloud database address has failed. Please check whether the cloud database IP and port information you entered is correct. If this error is still shown after the correct information is entered, please submit a ticket to contact the technical support.

## 12. Is it a physical machine behind the cloud database?

It is a physical machine behind the cloud database.

## 13. Will the cloud database conduct database sharding and table splitting for me?

As the standards for database sharding and table splitting are related to business logics, the cloud database will not conduct database sharding and table splitting for businesses.

## 14. Can the default character set encoding of the cloud database be modified?

Yes.

For details about the default character set and the modification method, refer to #6. Character Set in Cloud Database Service Limits. 

## 15. How to view the slow query log of the cloud database?

The slow query log can be obtained through the data export tool of the cloud database. For details, see Cloud Database Cold Backup Data Retrieval.

## 16. How can developers back up data by themselves?

Cloud database instances are fully backed up every day. Developers can also back up data using the multi-thread fast import/export tool provided by the cloud database (for details, see Manual Backup and Recovery of Cloud Database), or through the mysqldump tool.

## 17. How does the cloud database count the number of accesses?

The number of accesses to the cloud database is calculated based on the MySQL status variable Queries.

## 18. What's the difference between occupied space and used space for the cloud database?

Developers may find that the occupied space of the cloud database is larger than its used space. That's because binlog and other log data are included when the occupied space is calculated. The cloud database charges based on the actually used space.

## 19. How to apply for the enabling/disabling of the slave read-only permission of a cloud database instance?

If you need to enable/disable slave read-only, please submit a ticket for application according to the template.

## 20. Is there any restriction on the version of the MySQL client connecting the cloud database?

For details, refer to "#3.Limit on the Version of the MySQL Client Connecting to the Cloud Database" in "Cloud Database Service Limits".

## 21. How to modify the configuration parameters of the cloud database?

Developers can modify configuration parameters of the cloud database through a command line or phpMyAdmin:

### 1. Command line

The following variables can be dynamically modified when the syntax "set global var\_name=var\_value" is executed. Automatic synchronization to the local file will be finished in about 10 minutes. The set value will be retained for migration or reboot. The var\_name includes the following variables:
<table class="t">
<tbody><tr>
<th>  Variable
</th><th>  Description
</th></tr>
<tr>
<td> character_set_server
</td><td> The default character set for the server
</td></tr>
<tr>
<td> connect_timeout
</td><td> Connection timeout
</td></tr>
<tr>
<td> long_query_time
</td><td> A query exceeding this time is a slow query
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
</td><td> Non-interactive connection timeout
</td></tr></tbody></table>

### 2. phpMyAdmin

After logging in to the cloud database through phpMyAdmin, click "Variables" on the top menu, and click the value of the variable to be modified in the variable list below and modify it.

![][image-1]

For more information, refer to [Modifiable Configurations for Cloud Database.][2] 

## 22. Is there any restriction on the number of connections for the cloud database?
For details, refer to [Limits on Number of Connections for Cloud Database][3]

## 23. How long is the binlog of the cloud database stored?

For details, refer to [binlog Storage Time of Cloud Database][4]

## 24. How long is the slow query time for the cloud database?

The default slow query time (long\_query\_time) of the cloud database is 10 seconds. Users can modify it by running the command as follows:
```
set global long_query_time = 1;
```
For details, refer to [MySQL official manual][5]


## 25. Why are there unreadable codes in the Chinese data in the cloud database?
Before storing data into the cloud database, the develop should first view the default character set of this instance in the "Management View" page for the cloud database in the Console. When writing the program, set character\_set\_client, character\_set\_results, and character\_set\_connection to be the character set that is the same as the cloud database instance. Otherwise, if the data to be stored contains Chinese, unreadable codes will be found in the Chinese data.

For example: The default character set of the cloud database instance is utf8. When writing a program to connect the database, you need to execute the following statement before storing the Chinese data into the cloud database.
```
SET NAMES 'utf8';
```

## 26. Can the cloud database be accessed through public network addresses?

The access to cloud database through public networks in domestic regions has been made possible. For tips on usage, refer to [Public Network Access][6]

But it is not supported in Hong Kong and North American regions currently.

If you need to access the cloud database through a public network, you can achieve this by building a MySQL Proxy on a CVM with a public IP.

For details, refer to [MySQL Proxy official manual][7]

The steps for building a MySQL Proxy are as follows:

1) Download mysql-proxy installer to the CVM
 \`\`\`
wget http://cdn.mysql.com/Downloads/MySQL-Proxy/mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz
```

2) Unzip the installer
```
tar -xzf mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz 
```

3) View the extracted directory
  
Under the ls mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit, there are bin, lib, libexec and other directories:  Directories bin and libexec contain programs such as mysql proxy, and directory lib has dependency libraries, such as glibc and pcre.  Please keep the relationship between the relative paths of directories bin, lib, and libexec lest you cannot find the dependency libraries.

4) Enter the directory where mysql proxy locates and run it
```
cd mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit/bin 
./mysql-proxy --proxy-backend-addresses=10.**.**.17:3306 --proxy-address=:4040 
```

Parameter description:
--proxy-backend-addresses=10.**.**.17:3306 indicates the IP and port of a cloud database. The 10.**.**.17:3306 should be replaced with the IP and port of your cloud database.

--proxy-address=:4040 indicates the proxy listening address and port. The default value is ":4040", which represents all the IPs of the 4040 port. 

You can also append the command with the following parameters:

--daemon, which allows the proxy to run in the backend

--keepalive, which tries to restart the proxy when the proxy crashes


After running the command, you'll see the following message indicating that the proxy has been built successfully:
```
2014-09-01 11:56:38: (critical) plugin proxy 0.8.4 started 
\`\`\`
Please feel free to contact us if the proxy is not started successfully.

The listening port of the proxy is 4040. Next we will test whether the proxy can be forwarded smoothly.

5) Access the mysql proxy on the CVM through a public network.

Run (assuming that the public network IP is 182.*.*.2) mysql -h 182.*.*.2 -P 4040 -u root -p on a public network machine, enter your cloud database password as prompted to see whether you can log in to the cloud database.  If the login fails, check:

	 a. whether the IP and the port in step 4) are correct.
	 b. whether the public network machine can ping the public network IP of the CVM
	 c. whether the CVM successfully starts mysql proxy.
	  
## 27. Restrictions on file upload by phpMyAdmin

Currently, cloud databases can import/export sql data files through phpMyAdmin. When importing the files to be uploaded, the files must be sql files or compressed (tar, bz2, zip) sql files, and the size of the files must not exceed 2 M.

## 28. How to export database data?

1. If you need to export cold backup data, you can download it in "Backup Management" in the console instance

2. If you need to export real time data, you can purchase a read-only instance, and get the data through the read-only instance mysqldump


## 29. How to get informed of the insufficient disk space?

The monitoring center monitors the disk space of the cloud database. When over 90% of the cloud database space is occupied, text message and e-mail alarms will be triggered. You simply need to configure the corresponding alarm recipient in cloud monitoring, and the recipient will receive these alarms in case of insufficient disk space.

Click here to view specific configurations.

[1]:	/document/product/236/7269#7-%E6%93%8D%E4%BD%9C%E9%99%90%E5%88%B6
[2]:	http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/cdb_user_modify_var.xls
[3]:	/document/product/236/7269#2-%E8%BF%9E%E6%8E%A5%E6%95%B0%E9%99%90%E5%88%B6
[4]:	/document/product/236/7269#5-%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84binlog%E4%BF%9D%E5%AD%98%E6%97%B6%E9%97%B4%E8%AF%B4%E6%98%8E
[5]:	http://dev.mysql.com/doc/refman/5.1/en/server-system-variables.html#sysvar_long_query_time
[6]:	/document/product/236/7264
[7]:	//dev.mysql.com/downloads/mysql-proxy/

[image-1]:	//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/faq_cdb_1.png
