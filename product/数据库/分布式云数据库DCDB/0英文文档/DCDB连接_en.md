Here is the specific operation flow for connecting DCDB.
## Preparations
### Create User Permission
1. In the [DCDB Console](https://console.cloud.tencent.com/dcdb), click "Manage" on the right of the instance to be operated to enter the instance details page.
![](https://mc.qcloudimg.com/static/img/d2eafea1a7b03224961c0906180e6b22/image.png)
2. Click "Account Management" on the instance details page to enter the account management page and click "Create an Account".
![](https://mc.qcloudimg.com/static/img/4e60badccaa63bf1632dbe1ed948793f/r2.png)
3. Enter the account name, CVM, password, and notes. If all information is correct, click "OK" to enter the permission setting page.
	> The CVM name is actually the network egress address. Here a match method of % is supported and it represents that all IPs are accessible.
	
	![](https://mc.qcloudimg.com/static/img/00f4abaa96562c16f0aa3a3af0e30c00/r3.png)
4. In the permission setting page, after assigning permission based on needs, click "Save Settings" to complete the permission assignment. If you need to set permission later, click "Set Later".
	> With the navigation bar on the left, we provide a graphical interface fully compatible with MySQL management, permission management can be set to the column level.

	![](https://mc.qcloudimg.com/static/img/9029ee57e3892fe92ac0c3a5ead80dbb/r4.png)

5. After creating, click "Modify Permission" to modify the user permission, click "Clone Account" to completely copy the current account permission to create a new account. Click "More" to reset the password and delete the account.
	![](https://mc.qcloudimg.com/static/img/5f87261b43fc058adbd66b486a69e571/r5.png)

### Obtaining the Public Network Address
1. Go to the instance details page, find the public network address in the Basic Information and click "Open".

	![](https://mc.qcloudimg.com/static/img/fc3d50322e3547722a8d3e29e479b2e5/r6.png)	

2. After a moment, you can get the public network address and port number.
	> DCDB provides a unique IP and port for users to access and use.

	![](https://mc.qcloudimg.com/static/img/234c21d6897515b6623055301771dd24/r7.png)

## Connection Steps
After creating user permission and obtaining public network address, DCDB can be connected through third-party tools and program drivers. For WINDOWS, examples are shown in methods of command line connection, client connection and JDBC driver connection. For LINUX, command line connection is shown as an example.

### WINDOWS Command Line Connection
1. Open the WINDOWS command line, and enter the following commands under the correct path of mysql.

		mysql -h public network address -P port number -u user name  -p
		Enter password: **********(Enter password)

- After the relevant code is entered correctly, the following information is displayed. After the database is connected successfully, you can operate within the database for the next step.

		Welcome to the MySQL monitor.  Commands end with ; or \g.

### WINDOWS Client Connection
1. Download a standard SQL client such as MySQL Workbench and SQLyog. Here we take SQLyog as an example.
2. Open SQLyog, select "File" > "New Connection", enter CVM address, port, user name and password, and click "Connect".
> My SQL CVM address: enter the public network address obtained earlier.
> User name: Enter the user name you created earlier.
> Password: Enter the password of the user created earlier.
> Port: Enter the port assigned when obtaining the public network address.

	![](//mc.qcloudimg.com/static/img/ee0a9b423103292797873f78637e960b/image.png)
3. The interface after successful connection is as shown in the figure. You can operate within the database on this page.![](//mc.qcloudimg.com/static/img/93ecf636452505760086db5972d5fc6b/image.png)

### WINDOWS JDBC Driver Connection
> DCDB supports program-driven connection. Here we take connecting DCDB with JDBC Driver for MySQL (Connector/J) of JAVA as an example.

1. First [Download](https://dev.mysql.com/downloads/connector/j/5.0.html) a JDBC jar package from the MySQL official website, and import it to the Library referenced in JAVA.
2. Call JDBC code as follows:
```
		public static final String url = "Public network address";
		public static final String name = "com.mysql.jdbc.Driver";//Call JDBC driver
		public static final String user = "User name";
		public static final String password = "Password";
		//JDBC
		Class.forName("com.mysql.jdbc.Driver"); 
				Connection conn=DriverManager.getConnection("url, user, password");
		//
		conn.close();
```
3. After the connection is successful, you can perform other operations within database for the next step.
> Note: Because it is required to flag shardkey for DCDB in the case of sharding and inserting data, these operations can not be called with JDBC.

### LINUX Command Line Connection
Take the CVM of CentOS 7.2 64-bit system on Tencent Cloud server as an example. For more information on the purchase of Tencent CVM, refer to [CVM Purchase](https://buy.cloud.tencent.com/cvm).

1. Log in to LINUX, enter the command `yum install mysql`, and download and install MySQL client in Tencent Cloud's image source with CentOS's own package management software Yum.
![](//mc.qcloudimg.com/static/img/7f6a1f7a953cc38809fa069182481a22/image.png)
2. After "complete" is shown in command line, MySQL client installation is completed. We enter the command `mysql -h public network address -P port -u username -p password` to connect DCDB. Sharding can be done for the next step. We take `show databases;` as an example in the figure below.![](//mc.qcloudimg.com/static/img/b3fba8f8ace315e5eba05fdd252bd4c0/image.png)
