Drupal is an open source content management framework written in PHP language, which consists of content management system and PHP development framework. It can be used to build dynamic websites that offer multiple features and services, and provides support to web projects for a variety of applications from personal blogs to large communities.
This tutorial shows how to set up a Drupal e-commerce website on Tencent Cloud CVM. Supported software environment is: CentOS7.2 | Drupal7.56 | PHP5.4.16.

### Logging in to CVM Instance
For more information on purchase and access of CVM, please see [Quick Start for Linux CVM](https://cloud.tencent.com/document/product/213/2936).

### Installing MariaDB Service
1. By default, MariaDB database is supported on CentOS7 or above, so MariaDB database is used. Use `yum` to install MariaDB service in the CVM instance.
```
yum install mariadb-server mariadb -y
```
2. Start MariaDB service.
```
systemctl start mariadb
```
3. Create a database for Drupal. (drupal is used as the database name in this project)
```
mysqladmin -u root -p create drupal
```
"drupal" is the database name used in the Drupal service.
3. Create a user for the database.
```
mysql -u root -p
```
Authorize a user, and close the database after the authorization is successful.
```
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON drupal.* TO 'username'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
exit
```
"username" and "password" are the database username and the database password used in the Drupal service, respectively.

### Installing Apache Service
1. Use `yum` to install Apache in the CVM instance.
```
yum install httpd -y
```
2. Start Apache service.
```
service httpd start
```
3. Test Apache.
>**Note:**
In this step, you must configure the source as **all** and the port protocol as **TCP:80** inbound rule for your CVM in the security group. For more information on how to configure the security group, please see [Security Group](https://cloud.tencent.com/document/product/213/5221).

Enter `http://115.xxx.xxx.xxx/` in your local browser (`115.xxx.xxx.xxx` is the public IP of your CVM). The appearance of the following screen indicates Apahce has started successfully.
![](//mc.qcloudimg.com/static/img/3cde70e76a386b81f96ea9919280269d/image.png)

### Installing PHP 
1. Use `yum` to install PHP and its extension in the CVM instance.
```
yum install php php-dom php-dg php-mysql php-pdo -y
```
2. Create an info.php file in the `/var/www/html` directory of CVM to check whether the PHP is installed successfully. See the following sample code.
```
<?php phpinfo(); ?>
```
3. Restart Apache service.
```
service httpd restart
```
4. Enter `http://115.xxx.xxx.xxx/info.php` in your local browser (`115.xxx.xxx.xxx` is the public IP of your CVM). The appearance of the following screen indicates PHP has been installed successfully.
![](//mc.qcloudimg.com/static/img/0bc6667d122fe85d505fbe50b507b60a/image.png)

### Installing Drupal Service
1. Download the Drupal setup package.
```
wget http://ftp.drupal.org/files/projects/drupal-7.56.zip
```
2. Decompress the package to the root directory of the website.
```
unzip drupal-7.56.zip 
mv drupal-7.56/* /var/www/html/
```
3. Download the translation kit.
```
cd /var/www/html/
wget -P profiles/standard/translations http://ftp.drupal.org/files/translations/7.x/drupal/drupal-7.56.zh-hans.po
```
4. Modify the owner and group of `sites`.
```
chown -R apache:apache /var/www/html/sites
```
5. Restart Apache service.
```
service httpd restart
```
6. Enter `http://115.xxx.xxx.xxx/` in your local browser (`115.xxx.xxx.xxx` is the public IP of your CVM), to go to the installation interface of Drupal, select the version and then click "Save and continue".
![](//mc.qcloudimg.com/static/img/73f38550392e4fa6c496ed2afd0263a9/image.png)
7. Select the language, and click "Save and continue".
![](//mc.qcloudimg.com/static/img/9ab7121915a685816504a80d347be29c/image.png)
8. Set up the database, and enter the database information you configured in the section "**Install MariaDB Service**".
![](//mc.qcloudimg.com/static/img/a4d53a2d9421be3d223862585cf1c61e/image.png)
9. Enter the site information.
 ![](//mc.qcloudimg.com/static/img/c124ba56012c3a3bd8023a65cdb87b52/image.png)
10. Complete the process of Drupal installation.
![](//mc.qcloudimg.com/static/img/ed4795e8c6cb3183c56aeb8e18ef5d4a/image.png)
11. You can access `http://115.xxx.xxx.xxx/` (`115.xxx.xxx.xxx` is the public IP of your CVM) to customize the website.
![](//mc.qcloudimg.com/static/img/1c27ddd5419452fb92b8348d03586101/image.png)

