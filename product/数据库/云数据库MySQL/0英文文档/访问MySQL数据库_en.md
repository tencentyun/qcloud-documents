You can connect to a MySQL database by the following ways:
- Private network access: Use a CVM in the same availability zone to access the private IP assigned automatically to the database. This method has a low delay by using high-speed private network. (Note: The CVM and the database need to be in the same basic network, or belong to the same VPC. For more information on VPC, please see <a href="https://cloud.tencent.com/document/product/215/535" target="_blank">VPC Overview</a>.
- Public network access: Log in to phpMyAdmin page to operate the database via the login page of Tencent Cloud console with a public network account.

**Note:** For public network access, the database instance's public IP needs to be enabled, thus exposing your database service to attacks or intrusions on the public network. Therefore, it is recommended to log in to the database using private network.
# Private Network Access
1. Log in to an CVM that is accessible from network and resides in the same availability zone as the database instance.
For more information on how to log in to CVM, please see <a href="https://cloud.tencent.com/document/product/213/2783" target="_blank">Getting Started with Windows CVM</a> or <a href="https://cloud.tencent.com/document/product/213/2973" target="_blank">Getting Started with Linux CVM</a>. "Accessible from network" means that the CVM and the MySQL database instance are in the same basic network, or belong to the same VPC.
1. Select the recommended connection method based on CVM's operating system.
**-Login from Windows system**
(1) Download a standard SQL. It is recommend to download MySQL Workbench, which is the commonly used SQL under Windows. Open https://dev.mysql.com/downloads/workbench/ in the CVM, and download the appropriate installer based on your system.
![](//mc.qcloudimg.com/static/img/4d7e6c56f02aad86f232e5cdd8c0bb17/image.png)
(2) When "Login", "Sign Up" and "No, thanks, just start my download." appear on the screen, select "No, thanks, just start my download." to start a quick download.
	![](//mc.qcloudimg.com/static/img/7169ce063b1b41c58c48089bc2a61441/image.png)
(3) Install MySQL Workbench on this CVM. Microsoft .NET Framework 4.5 and Visual C ++ Redistributable for Visual Studio 2015 are required for the installation. Before installing MySQL Workbench, you can click "Download Prerequisites" in the MySQL Workbench installation wizard to install the two software.
	![](//mc.qcloudimg.com/static/img/bcf08cec72e8ea9c490cb30ae79f0da4/image.png)
	(4) Open the MySQL Workbench, select "Database" -> "Connect to Database", enter the MySQL database instance's private IP, user name, and password, and then click "OK" to log in.
 - Hostname: Enter the private IP. You can view the private IP of the target database instance on the MySQL database instance details page in the console. In this example, it is 10.66.238.24.
 - Port: Default to port 3306.
 - Username: Default to "root".
 - Password: Enter the password you set when you initialize the database instance.
	![](//mc.qcloudimg.com/static/img/feb4b95b1038532330e876a605016b87/image.png)
(5) When you have logged in to the MySQL database, the following page appears, where you can view the modes and objects of the database, create tables, and perform such operations as data insertion and query.
	![](//mc.qcloudimg.com/static/img/abd8efce579343d25f534143c19c132e/image.png)
	
**-Login from Linux system**
(1) In this example, the CVM is run on a CentOS 7.2 64-bit system. You can use Yum, the package manager built in CentOS, to download and install the MySQL from the Tencent Cloud image sources. 
	The command is as follows:
	```yum install mysql```
	The command is executed as shown in the figure below:
	![](//mc.qcloudimg.com/static/img/eee76fa95379b8a25fc076b66b4ca28c/image.png)
(2) Log in to MySQL using the MySQL command line tool. The command is as follows:
```mysql -h hostname -u username -p```
Replace "hostname" with the private IP of the target MySQL database instance, and replace "username" with the default user name "root", and then enter its password when prompted with "Enter password:".
	In this case, the hostname is 10.66.238.24.
![](//mc.qcloudimg.com/static/img/d1da9f59f0fff77ad2a8ff18e0b11e7c/image.png)
(3) Under the prompt "MySQL>", you can send an SQL statement to the MySQL server for execution. For specific command lines, please visit: https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html
In the following example, the statement is "show databases;":
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

# Public Network Access
**Note:** For public network access, the database instance's public IP needs to be enabled, thus exposing your database service to attacks or intrusions on the public network. 
Please select the login method based on the operating system of the public network-based CVM.
**- Login from Windows system**
1. In the [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Products" -> "Relational Database" -> "MySQL" -> "Instance List", select the target instance with a status of "running", and then click "Log In".
![](//mc.qcloudimg.com/static/img/248ca91c3b13e3f249c752f43019ed1a/image.png)
1. In the login page of the data management console, enter "root" as the account, and enter the password you set for the account "root" in the initialization steps described above, and then click "Log In".
![](//mc.qcloudimg.com/static/img/b5538d93dc27d99af6fed9f0e5c9b798/image.png)
1. In the data management page, you can view the instance's status and basic information. Click "Back to PMA" to access the database.
![](//mc.qcloudimg.com/static/img/ceab808b44adf5feba818e70a079b83e/image.png)
1. When you have connected to the MySQL database successfully via phpMyAdmin, you can view the modes and objects of the database, create tables, and perform such operations as data insertion and query.
![](//mc.qcloudimg.com/static/img/c8f60117f5aec772663d3c7890c96b1e/image.png)

**-Login from Linux system**
1. In the Tencent cloud console, select "Cloud Products" -> "Relational Database" -> "MySQL" -> "Instance List", and click the target instance ID to go to the instance details page.
![](//mc.qcloudimg.com/static/img/018350e48f1d535d105c3c6340d36b2d/image.png)
1. In the instance details page, click "Enable" next to the pubic IP to set the password for the account for public network access cdb_outerroot, and then click "OK".
![](//mc.qcloudimg.com/static/img/730e65a8b10f429a80ea15456b9a7193/image.png)
![](//mc.qcloudimg.com/static/img/48a8489d3c0341ef87627fdc108f93e7/image.png)
1. The enabled public IP is displayed in the instance details page, and will be used in the subsequent steps.
![](//mc.qcloudimg.com/static/img/3d1176c8958f8ffc0e1f2594fc7f3141/image.png)
1. In this example, the CVM is run on a CentOS 7.2 64-bit system. You can use Yum, the package manager built in CentOS, to download and install the MySQL.
	The command is as follows:
	```yum install mysql```
1. Log in to MySQL using the MySQL command line tool. 
The command is as follows:
```mysql -h hostname -P port -u username -p```
Replace "hostname" with the public IP of the target MySQL database instance, replace "port" with the public network port, replace "username" with the default user name for public network access "cdb_outerroot", and then enter its password when prompted with "Enter password:".
In this case, the hostname is 59281c4e4b511.gz.cdb.myqcloud.com, and the public network port is 15311.
![](//mc.qcloudimg.com/static/img/48df6390ccf7669d04403cd84b8b6fad/image.png)
1. Under the prompt "MySQL>", you can send an SQL statement to the MySQL server for execution. For specific command lines, please visit: https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html
In the following example, the statement is "show databases;".
![](//mc.qcloudimg.com/static/img/76b4346a84f7388ae263dc6c09220fc0/image.png)

