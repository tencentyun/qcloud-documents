There are two methods to connect to MariaDB database:
- Private network access: Use a CVM that is connected to the MariaDB database instance in Tencent Cloud to access the private network address of the MariaDB database instance. (Note: The CVM and the database need to be in the subnet of a VPC. For more information on VPC, see <a href="https://cloud.tencent.com/document/product/215/535" target="_blank">VPC Overview</a>.)
- Public network access: For Windows or Linux CVM with public network, install the database client to access the public network address of MariaDB database instance within Tencent Cloud.

**Security note:** The public network address of database instance must be enabled for public network access, which makes your database services expose on the public network, and thus causes database intrusions or attacks. Therefore, it is recommended to access a database using the private network mode.

An account is required for both private network and public network access.
## Create an Account
1. On the [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Products" -> "Relational Database" -> "TDSQL(MariaDB)" -> "Instance List", click the ID of running MariaDB database instance to go to details page.
![](//mc.qcloudimg.com/static/img/08e24afbf51b941df4b8c4a893857b31/image.png)
2. On the **Account Management** page, click "Create an Account", and set the account permission. Here we take test123 with full permission as an example.
Create an account, set a password, and click "OK".
![](//mc.qcloudimg.com/static/img/b5673f5c88f57d4a389fc4e673416659/image.png)
Set the permission for account test123, and click "Save Configuration".
![](//mc.qcloudimg.com/static/img/38297ac6bb2bde4a085cddd53ba8dcd7/image.png)
Check whether the account permission is configured correctly, and click **Close** to complete the configuration.
![](//mc.qcloudimg.com/static/img/385bfb7ab899da5266a56242601a4c62/image.png)
For more information on creating an account, see [creating an account](https://cloud.tencent.com/document/product/237/7054).

## Access Database
There are two methods to connect to MariaDB database:
 - Private network access: Use a CVM that is connected to the MariaDB database instance in Tencent Cloud to access the private network address of the MariaDB database instance. (Note: The CVM and the database need to be in the subnet of a VPC. For more information on VPC, see <a href="https://cloud.tencent.com/document/product/215/535" target="_blank">VPC Overview</a>.)
 - Public network access: For Windows or Linux CVM with public network, install the database client to access the public network address of MariaDB database instance within Tencent Cloud.

### Private Network Access

1. Log in to a CVM that is reachable via network and in the same availability zone as the database instance. For more information on CVM login, see <a href="https://cloud.tencent.com/document/product/213/2764" target="_blank">Getting started with Windows CVM </a>or <a href="https://cloud.tencent.com/document/product/213/2936" target="_blank">Getting started with Linux</a>. "Reachable via network" means that the CVM and the MariaDB database instance are in the same basic network, or belong to the same VPC.
2. Select the recommended connection method based on CVM's operating system.
**-Login from Windows system**
1) Download and install MariadDB client. It is recommend to download sqlyog. Here is the official website: https://www.webyog.com/.
2) Open sqlyog, and enter private IP and port number of MariaDB database instance, and database account and password.
 - My SQL CVM address: enter 10.30.0.7 for this example.
 - User name: Enter the user name test123 you created earlier.
 - Password: User password corresponding to the user test123.
 - Port: Enter 3306 for this example.
![](//mc.qcloudimg.com/static/img/d4b72b365c7e31ac824851602ca5a29a/image.png)
3) After the login succeeds, the following interface shows up, on which you can view various modes and objects of the MariaDB database, and you can perform table creation, data insertion, query, and other operations.
![](//mc.qcloudimg.com/static/img/7646040af53a923f47c4973a4aac7680/image.png)

**-Login from Linux system**
(1) In this example, the CVM is run on a CentOS 7.2 64-bit system. You can use Yum, the package manager built in CentOS, to download and install the MySQL from the Tencent Cloud image sources.
The command is as follows:
`yum install mysql`
The command is executed as shown in the figure below: ![](//mc.qcloudimg.com/static/img/eee76fa95379b8a25fc076b66b4ca28c/image.png)
2) Log in to MariaDB database using the MySQL command line tool.
The command is as follows:
`mysql -h hostname -u username -p`
Replace "hostname" with the private IP of the target MariaDB database instance, and replace "username" with the user "test123" created earlier, and then enter its password when **Enter password:** is prompted.
In this case, the hostname is 10.30.0.7.
![](//mc.qcloudimg.com/static/img/f8dccff34309cfd332f600f1ceb35ff1/image.png)
3). Under the prompt "MySQL>", you can send SQL statements to a MariaDB server for execution. For specific command lines, refer to: <https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html>
We take `show databases;` as an example in the screenshot below.
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

### Public Network Access
**Security note:** The public network address of database instance is required to be enabled for public network access, which makes your database services expose on the public network, and thus causes database intrusions or attacks.
1. Obtain the public network address of database.
1) Click the ID of running MariaDB database instance to enter details page.
![](//mc.qcloudimg.com/static/img/08e24afbf51b941df4b8c4a893857b31/image.png)
2) On the **Instance Details** page, click "Enable" after the "Public network address" to enable the public network address of the database instance.
![](//mc.qcloudimg.com/static/img/e4793d117939c3f56c5f3d63b0491fe9/image.png)
3) View the public network address of this database instance.
In the screenshot below, the public domain name of database is 	tdsql-6gy3mopk.gz.cdb.myqcloud.com and port number is 114
![](//mc.qcloudimg.com/static/img/e364724c2944099a9cd9c8c8c79fd96f/image.png)

2. Log in to database
**-Login from Windows system**
1) Download and install MariadDB client. It is recommend to download sqlyog. Here is the official website: https://www.webyog.com/.
2) Open sqlyog, enter domain name and port number of a public network of MariaDB database instance, and database account and password.
 - My SQL CVM address: enter tdsql-6gy3mopk.gz.cdb.myqcloud.com for this example.
 - User name: Enter the user name test123 you created earlier.
 - Password: User password corresponding to the user test123.
 - Port: Enter 114 for this example.
![](//mc.qcloudimg.com/static/img/1924e51d3519bab0ab9705217466fec2/image.png)
3) After the login succeeds, the following interface shows up, on which you can view various modes and objects of the MariaDB database, and you can perform table creation, data insertion, query, and other operations.![](//mc.qcloudimg.com/static/img/d050b1917e7ccfea62a9ec7c8992c313/image.png)
 
**-Login from Linux system**
1) In this example, the CVM is running on a CentOS 7.2 64-bit system. You can download and install the MySQL client. The command is as follows:
`
yum intall mysql
`
2) Log in to MariaDB database using the MySQL command line tool. The command is as follows:
`
mysql -h hostname -P port -u username -p
`
Replace "hostname" with the public IP of the target MariaDB database instance, and replace "username" with the user "test123" created earlier, and then enter its password when **Enter password:** is prompted.
In this case, the hostname is tdsql-6gy3mopk.gz.cdb.myqcloud.com and port is 114.
![](//mc.qcloudimg.com/static/img/230ca6d65526050e062c3f59186d4e6c/image.png)
3) Under the prompt "MySQL>", you can send SQL statements to a MariaDB server for execution. For specific command lines, refer to: 
<https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html>
We take `show databases;` as an example in the screenshot below.
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)


