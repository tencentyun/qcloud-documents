## 1. How to back up data?

Cloud database instances are fully backed up every day. Developers can download backup data in the console via public network or private network (For more information, please see <a href="https://cloud.tencent.com/document/product/236/7274" target="_blank">Downloading Backup Files</a>), or back up databases manually in phpMyAdmin console.

## 2. How to view the slow log of the cloud database?

You can export and view the slow logs in [Cloud Database Console](https://console.cloud.tencent.com/cdb).
The default slow log threshold (long\_query\_time) of cloud database is 10 seconds. You can modify it using the following command:
```
 set global long_query_time = 1
```
For more information, please see [official MySQL manual](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_long_query_time).

## 3. How to authorize other users to operate cloud databases?

Root user can authorize other users to operate cloud databases by using the grant command of mysql. Do not use "grant all" command.
"shutdown" and "file" permissions are unavailable to root users now, so a root user cannot create users with all permissions. Please refer to the following commands for authorization:
```
grant SELECT,INSERT, UPDATE, DELETE, CREATE, DROP, ALTER on *.* to 'myuser'@'%' identified 
by 'mypasswd';
```
 
## 4. How to access the cloud database from public network?

The access to cloud database from public network is supported in domestic regions, and is not supported in Hong Kong and North American regions for now.
You can access the cloud database from public network with MySQL Proxy built on a CVM with a public IP.
For more information, please see [official MySQL Proxy manual](http://dev.mysql.com/downloads/mysql-proxy/).
To build a MySQL Proxy, follow the steps below:
1. Download mysql-proxy setup package to the CVM.
```
wget http://cdn.mysql.com/Downloads/MySQL-Proxy/mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz
```

2. Decompress the setup package.
```
tar -xzf mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz 
```

3. Check the decompressed directory.
```
ls mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit
```
The directory contains bin, libexec, lib and other directories: bin and libexec directories contain MySQL Proxy and other programs; lib directory contains the libraries on which the programs are dependent, such as glibc, pcre, etc. Please keep the relative path relationship between bin, libexec and lib directories to avoid breaking the dependency links.

4. <span id="document_access_step4"></span>Go to the directory where mysql proxy locates, and run MySQL Proxy.
```
cd mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit/bin 
./mysql-proxy --proxy-backend-addresses=10.**.**.17:3306 --proxy-address=:4040 
```
Parameter description:
--proxy-backend-addresses=10.\*\*.\*\*.17:3306 indicates the IP and port of cloud database. "10.\*\*.\*\*.17:3306" needs to be replaced with the IP and port of your cloud database.
--proxy-address=:4040 indicates the  listening address and port of proxy. The default value is ":4040", which represents all the IPs of the 4040 port. 
You can also append the following parameters to the command:
--daemon: Allows the proxy to run in the backend.
--keepalive: Attempts to restart the proxy when it crashes.
After running the command, the following message appears, indicating that the proxy has been built successfully:
```
2014-09-01 11:56:38: (critical) plugin proxy 0.8.4 started 
```
Please contact us if the proxy cannot be started successfully.
The listening port of the proxy is 4040. Next we can test whether the proxy can forward requests normally.

5. Access the mysql proxy on the CVM from public network.
Run  `mysql -h 182.*.*.2 -P 4040 -u root -p` on a public network machine (assuming that the public IP is 182.\*.\*.2), enter your cloud database password as prompted to verify whether you can log in to the cloud database.
	(1) Whether the IP and port in Step [4](#document_access_step4) are correct.
	(2) Whether the public network machine can ping the public IP of the CVM.
	(3) Whether the mysql proxy can be started by CVM successfully.

## 5. How to modify the default character set encoding of cloud database?

The default character set encoding format of cloud databases is the same with MySQL databases: latin1 (ISO-8859-1 encoding format).
Developers can modify the database character set of the server by going to [Cloud Database Console](https://console.cloud.tencent.com/cdb) -> "Management" -> "Parameter Settings". Four character sets are supported now: latin1, gbk, utf8 and utf8mb4.
Although the cloud database supports the default character set encoding settings, we recommend that you explicitly specify the encoding for table when creating a table and specify the encoding for connection when the connection is established. This will improve the portability of your applications.
For more information on the resources of MySQL character sets, please see [official MySQL manual](https://dev.mysql.com/doc/refman/5.7/en/charset.html).

## 6. How does the cloud database count the number of accesses?

The number of accesses to the cloud database is calculated based on the MySQL status variable Queries.

## 7. How are read and write separated in the cloud database?

Read-write separation can be achieved by purchasing read-only instances. For more information, please see <a href="https://cloud.tencent.com/document/product/236/7270" target="_blank">Read-only Instances</a>.

