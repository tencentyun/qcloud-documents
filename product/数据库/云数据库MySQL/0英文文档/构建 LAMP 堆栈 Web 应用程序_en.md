LAMP, short for Linux+Apache+Mysql/MariaDB+Perl/PHP/Python, is a group of open source software used to build dynamic websites or servers. Each component of LAMP is independent from but increasingly compatible with each other, so they are used in combination to form a powerful Web application platform.
This tutorial guides you through the following procedure: Start a Tencent Cloud CDB database instance, and configure an LAMP application through Tencent Cloud CVM to connect to the high availability environment of the Tencent Cloud CDB database instance.
The database can be separated from the environment life cycle after you run the Tencent Cloud database instance. This allows you to connect multiple servers to the same database, and to simplify the OPS for database, eliminating your need to worry about the database installation, deployment, version update, and troubleshooting.
>**Note:**
The cloud database instance and CVM instance used in this tutorial reside in the same region. If they are in different regions, see [Access from Public Network](https://cloud.tencent.com/document/product/236/3130#.E5.A4.96.E7.BD.91.E8.AE.BF.E9.97.AE).

### Initializing Cloud Database Instance
For more information on how to purchase and initialize cloud databases, please see [Purchase and Renewal](https://cloud.tencent.com/document/product/236/5160) and [Initialize MySQL Database](https://cloud.tencent.com/document/product/236/3128).

### Logging in to CVM Instance
For more information on purchase and access of CVM, please see [Quick Start for Linux CVM](https://cloud.tencent.com/document/product/213/2936). CentOS is used in this tutorial.

### Installing MySQL Client
1. Use `yum` to install MySQL client in CVM instance:
```
yum install mysql -y
```
![](//mc.qcloudimg.com/static/img/8b952d6d7d767413a6558e82df092d44/image.png)
2. After the installation is completed, connect to the Tencent Cloud database instance:
```
mysql -h hostname -u username -p
```
![](//mc.qcloudimg.com/static/img/297856a53959582220b9bba6f06ce9f6/image.png)
"hostname" is the private IP of the database instance, and "username" is the user name of your database.
3. After the connection is successful, you can close the database to go to the next step.
```
quit;
```

### Installing Apache Service
1. Use `yum` to install Apache in the CVM instance:
```
yum install httpd -y
```
![](//mc.qcloudimg.com/static/img/dc142f813e8e8474a5994e2e841828f2/image.png)
2. Start Apache service:
```
service httpd start
```
3. Test Apache:
>**Note:**
In this step, you must configure the source as **all** and the port protocol as **TCP:80** inbound rule for your CVM in the security group. For more information on how to configure the security group, please see [Security Group](https://cloud.tencent.com/document/product/213/5221).

Enter `http://115.xxx.xxx.xxx/` in your local browser (`115.xxx.xxx.xxx` is the public IP of your CVM). The appearance of the following screen indicates Apahce has started successfully.
![](//mc.qcloudimg.com/static/img/3cde70e76a386b81f96ea9919280269d/image.png)

### Installing PHP 
1. Use `yum` to install PHP in CVM instance:
```
yum install php -y
```
![](//mc.qcloudimg.com/static/img/61a0864ddbb70e65c63ad5093e8165d4/image.png)

### Creating a Project to Test LAMP Environment
1. Create an info.php file in the `/var/www/html` directory of CVM. See the following sample code:
```
<?php phpinfo(); ?>
```
2. Restart Apache service.
```
service httpd restart
```
3. Enter `http://0.0.0.0/info.php` in your local browser (`0.0.0.0` is the public IP of your CVM). The appearance of the following screen indicates LAMP has been deployed successfully.
![](//mc.qcloudimg.com/static/img/0bc6667d122fe85d505fbe50b507b60a/image.png)

