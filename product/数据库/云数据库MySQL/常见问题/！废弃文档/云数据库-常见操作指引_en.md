## 1. How to back up data

Cloud database instances are fully backed up every day. Developers can download backup data in the console via public network or private network, or back up database manually in phpMyAdmin.

## 2. How to view the slow query logs of cloud database

You can export and view the slow query logs in the Cloud Database console.

The default slow query time (long_query_time) of cloud database is 10 seconds. Users can modify it by running the command as follows:

<pre> set global long_query_time = 1
</pre>

For details, please refer to [MySQL official manual](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_long_query_time). 


## 3. How to authorize other users to work with the cloud database

root users can authorize other users using the grant command of mysql, but cannot do so using "grant all" command.

Currently, "shutdown" and "file" permissions are not available to root users, so you cannot create users with all permissions through root. Please refer to the following commands for authorization:

<pre>grant SELECT,INSERT, UPDATE, DELETE, CREATE, DROP, ALTER on *.* to 'myuser'@'%' identified 
by 'mypasswd';</pre>
 
## 4. How to access the cloud database through a public network

The access to cloud database through public networks in domestic regions has been made possible, while it is not supported in Hong Kong and North American regions currently.

If you need to access the cloud database through a public network, you can achieve this by building a MySQL Proxy on a CVM with a public IP.

For details, please refer to [MySQL Proxy official manual](http://dev.mysql.com/downloads/mysql-proxy/).

The steps for building a MySQL Proxy are as follows:

1) Download mysql-proxy installer to the CVM

wget [http://cdn.mysql.com/Downloads/MySQL-Proxy/mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz](http://cdn.mysql.com/Downloads/MySQL-Proxy/mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz)

2) Unzip the installer

tar -xzf mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz 

3) View the extracted directory

Under the ls mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit, there are bin, lib, libexec and other directories:  Directories bin and libexec contain programs such as mysql proxy, and directory lib has dependency libraries, such as glibc and pcre.  Please keep the relationship between the relative paths of directories bin, lib, and libexec lest you cannot find the dependency libraries.

4) Enter the directory where mysql proxy locates and run it

cd mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit/bin 
./mysql-proxy --proxy-backend-addresses=10.**.**.17:3306 --proxy-address=:4040 

Parameter description:

--proxy-backend-addresses=10.**.**.17:3306 indicates the IP and port of a cloud database. The 10.**.**.17:3306 should be replaced with the IP and port of your cloud database.
--proxy-address=:4040 indicates the proxy listening address and port. The default value is ":4040", which represents all the IPs of the 4040 port. 

You can also append the command with the following parameters:

--daemon, which allows the proxy to run in the backend
--keepalive, which tries to restart the proxy when the proxy crashes
After running the command, you'll see the following message indicating that the proxy has been built successfully:
2014-09-01 11:56:38:  (critical) plugin proxy 0.8.4 started 
Please feel free to contact us if the proxy is not started successfully.
The listening port of the proxy is 4040. Next we will test whether the proxy can be forwarded smoothly.

5) Access the mysql proxy on the CVM through a public network.

Run (assuming that the public network IP is 182.*.*.2) mysql -h 182.*.*.2 -P 4040 -u root -p on a public network machine, enter your cloud database password as prompted to see whether you can log in to the cloud database.  If the login fails, check:

a. whether the IP and the port in step 4) are correct.

b. whether the public network machine can ping the public network IP of the CVM

c. whether the CVM successfully starts mysql proxy.


## 5. How to modify the default character set encoding of the cloud database

The default character set encoding format of cloud databases is the same with MySQL databases: latin1 (ISO-8859-1 encoding format).

Developers can modify the database character set on the Server side in the console of the cloud database. Currently, four types of character sets including latin1, gbk, utf8 and utf8mb4 are supported.

You may configure the default character set encoding setting for cloud databases, but it is recommended that you specify the encoding for tables explicitly when creating the tables, and specify the encoding for connections when establishing the connections.

This will improve the portability of your applications.

For resources related to MySQL character sets, please refer to [MySQL official manual](https://dev.mysql.com/doc/refman/5.7/en/charset.html).

The character set can be modified through the CDB Console.

## 6. How does the cloud database count the number of accesses

The number of accesses to the cloud database is calculated based on the MySQL status variable Queries.

## 7. How is read and write separation achieved in the cloud database

Read and write separation can be achieved by purchasing read-only instances.


