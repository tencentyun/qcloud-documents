This document uses Windows Server 2012 R2 as an example to introduce how to build MySQL 5.5.

SQL Server database is frequently used in Windows system. You need to grand authorization for SQL Server because it is not for free. You can also purchase [CDB instances for Tencent Cloud SQLServer database](http://cloud.tencent.com/product/sqlserver.html).

## Step 1: Download MySQL installer
&nbsp;&nbsp;&nbsp;Open the browser on the CVM and enter the download URL:https://dev.mysql.com/downloads/mysql/5.5.html#downloads
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](//mc.qcloudimg.com/static/img/b1da1513321247e0daf1163f529d4cd9/image.png)

## Step 2: Install the application
 1. Run the installation program. Click **Next** and select **I accept the terms in the License Agreement**.
![](//mc.qcloudimg.com/static/img/8dd2fc106b09c3538c1dd407c02adea4/image.png)
 
 2. Select **Typical** in **Choose Setup Type**.
![](//mc.qcloudimg.com/static/img/9f45d5441da017feca7eb9bdc11260fd/image.png)

 3. Select **Launch the MySQL Instance Configuration Wizard**.
	![](//mc.qcloudimg.com/static/img/1a6b6ad499c0c00d294d6f24d5ee1645/image.png)

## Step 3: Configure MySQL


 1. Configure the type of MySQL. Here we use Detailed Configuration as an example.
  - Detailed Configuration is suitable for advanced users that need to have finer control of the CVM configurations.
  - Standard Configuration is suitable for new users that want to launch MySQL quickly without considering the CVM configurations.
 
 > **Note:**
 > Standard Configuration may be incompatible with your operating system. Detailed Configuration is recommended.

	![](//mc.qcloudimg.com/static/img/434424a84d76f9492c511f567ae2d03f/image.png)
 
 2. Configure the type of MySQL server. Here we use Developer Machine as an example.
  - Developer Machine represents a typical personal desktop workstation. When multiple desktop applications are running at the same time, the MySQL server is configured to use minimal system resources.
  - Server Machine is a type of server on which MySQL server can run with other applications such as FTP, email and Web servers. The MySQL server is configured to use a moderate portion of the system resources.
  - Dedicated MySQL Server Machine is a type of server on which only MySQL server can run. The MySQL server is configured to use all available system resources.

	![](//mc.qcloudimg.com/static/img/11b1162dd70e46882a43933f517dcaf4/image.png)

 3. Configure MySQL database. Here we use Multifunctional Database as an example.
  - Multifunctional Database uses InnoDB and MyISAM storage engines simultaneously, and allocates resources to them equally. You are recommended to select this option if you often use two storage engines simultaneously.
  - Transactional Database Only uses InnoDB and MyISAM storage engines simultaneously, and allocates most server resources to InnoDB storage engine. You are recommended to select this option if you use InnoDB frequently and use MyISAM occasionally.
  - Non-Transactional Database Only does not use InnoDB storage engine, and allocates all server resources to MyISAM storage engine. You are recommended to select this option if you do not use InnoDB.
 
 ![](//mc.qcloudimg.com/static/img/37972855d5c880e59b5310a7872491f1/image.png)

 4. Configure the InnoDB tablespace for MySQL. Choose default configuration here.
	![](//mc.qcloudimg.com/static/img/c4c8e8710e27b202a9694b2c1be0f4f6/image.png)

 5. Configure concurrent connection for MySQL. Here we use Decision Support as an example.
  - Decision Support is suitable for situations that do not require a large number of concurrent connections.
  - Online Transaction Processing is suitable when a large number of concurrent connections are required.
  - Manual Setting is suitable when you need to configure the maximum number of concurrent connections manually.
 
 ![](//mc.qcloudimg.com/static/img/ef17aa905ea5bdd50b1ad61b416be4ea/image.png)

 6. Configure the network options of MySQL. You can enable or disable TCP/IP network and configure the port number for MySQL server connection.
 > **Notes:**
 > TCP/IP network is enabled by default.
 > Port 3306 is used by default.
 
	 ![](//mc.qcloudimg.com/static/img/b864e47b1e4b0e87cd5015007f9bd8dc/image.png)

 7. Configure MySQL character set. Here we use Standard Character Set as an example.
  - Standard Character Set uses Latin1 as the default server character set.
  - Best Support For Multilingualism uses UTF8 as the server character set.
  - For Manual Selected Default Character Set/Collation, select the character set in the drop-down box as needed.
 
	![](//mc.qcloudimg.com/static/img/31c4f7f13a2b5b6aa0754cc3e4bd526e/image.png)

 8. Configure the service options of MySQL. It is recommended to select both boxes to manage MySQL using command line.
	![](//mc.qcloudimg.com/static/img/9f24e245f4b5d08e9d0658aa21cd70cd/image.png)

 9. Set the root password.
	![](//mc.qcloudimg.com/static/img/65a265bcc69d6a75f0da51387dd3aedf/image.png)

 10. Complete the configuration. Click **Execute** to complete the installation.
	![](//mc.qcloudimg.com/static/img/fd815f05c40d11c61d801a321131e3ec/image.png)

## Step 4: Login Test for MySQL

1. Click **Start** on the CVM and click the search icon. Enter ```cmd``` to open the administrator command box:
![](//mc.qcloudimg.com/static/img/c7920f20daff62d136f6ba7987fb2ac8/image.png)

2. Enter the command ```mysql -u root -p``` and press **Enter**.
 
3. Log in to MySQL using the root password you set. The picture below indicates that MySQL has been installed and configured successfully.
![](//mc.qcloudimg.com/static/img/18aef21cabf34db1bca266a8977018f4/image.png)



