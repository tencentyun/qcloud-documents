WordPress is a common software for building personal blog websites, which is developed using PHP language and MySQL database. You can use Tencent Cloud CVM to run WordPress and publish your personal blogs through simple operations.
Tencent Cloud Lab provides tutorials for practical operations, to help you build LNMP environment and WordPress website step by step. Click to enter the [Lab](https://cloud.tencent.com/developer/labs?utm_source=doc8044&utm_medium=qclab). For more information on how to build a WordPress website, please see [Build WordPress Personal Blog Based on CentOS](https://cloud.tencent.com/developer/labs/lab/10001).

Here, we take CentOS Linux 6.8 as an example to show how to build a WordPress personal website:
![](//mc.qcloudimg.com/static/img/6b7d99e96b495d10cd44624892c2ee46/image.png)
## Introduction
The following services/tools are used in this tutorial:

**CVM**: This tutorial uses Tencent Cloud's Cloud Virtual Machine (CVM) to build a WordPress website.
 
**Domain name registration**: To access your WordPress website with an easy-to-remember domain name, you can use Tencent Cloud's domain name registration service to purchase a domain name.
 
**ICP licensing**: Required for websites whose domain names are directed to Chinese servers. A website cannot be launched until an ICP license is obtained for its domain name. You can complete ICP licensing via Tencent Cloud.

**Tencent Cloud DNS**: You need to configure domain name resolution to allow users to access your website with a domain name instead of an IP address. You can resolve domain names through Tencent Cloud DNS service.

**PuTTY**: One of the free tools ideal for remote login. This easy-to-operate software is used in this tutorial for forum building. [Download PuTTY ](http://xiazai.sogou.com/comm/redir?softdown=1&u=-9C432O39iS-1WMoK6o75d2rbT1v8F8PVRelGJ0KRMgmFySI7r-cdPLmpUQMiC7rMWKCgnK7gooqOgr0EiOgKJ36wBs_inYy&pcid=-3190951004095154321&filename=putty.zip&w=1907&stamp=20170524).

## Step 1: Create and run a CVM
1. [Purchase a CVM](https://buy.cloud.tencent.com/cvm?regionId=8&projectId=8) based on your needs.
For more information on how to create a CVM, please see:
[Create Linux CVMs](https://cloud.tencent.com/document/product/213/2972)
2. After the CVM is created, you can log in to the [Tencent Cloud console](https://console.cloud.tencent.com/cvm) to view or edit its status.
![](//mc.qcloudimg.com/static/img/cbd7d2717a9d162df28b4d517ab1d815/image.png)

The operating system version of the CVM in this tutorial is CentOS 6.8. Save the following information to be used in the subsequent steps:
- CVM's user name and password
- CVM's public IP

## Step 2: Build LNMP environment
LNMP, an acronym for Linux, Nginx, MySQL and PHP, is one of the most common runtime environments in which Web servers can run. After the CVM is created, you can build the LNMP environment.
> Linux: CentOS 6.8
Nginx: Web server program for parsing Web applications
MySQL: A database management system
PHP: A program used to generate Web pages from a Web server

Tencent Cloud provides Yum download source. You can quickly install software through Yum in CentOS.
> Yum, Vim and PuTTY commands will be used in the building process.

### 2.1 Run PuTTY to connect to Linux CVM
1. [Download PuTTY ](http://xiazai.sogou.com/comm/redir?softdown=1&u=-9C432O39iS-1WMoK6o75d2rbT1v8F8PVRelGJ0KRMgmFySI7r-cdPLmpUQMiC7rMWKCgnK7gooqOgr0EiOgKJ36wBs_inYy&pcid=-3190951004095154321&filename=putty.zip&w=1907&stamp=20170524) to your computer, open the folder to which it is downloaded, decompress the file, and then double-click "putty.exe" to open the configuration page as follows:
2. Select "Session", and enter the name or IP of the CVM to be accessed in "Host Name (or IP address)", such as "server1" or "192.168.2.10". In this tutorial, the CVM's public IP is used. Leave other configuration options unchanged.
3. Specify a name for the session in "Saved Sessions" field, and click "Save" to save the session configuration.
![putty1](//mc.qcloudimg.com/static/img/a7f57ac399e06522be67de3cf9d264e0/image.png)
4. After the configuration is completed, click "Open", and a prompt window appears for certificate confirmation. Select "Yes".
![putty2](//mc.qcloudimg.com/static/img/b7883110e977fb0d94310379a152c5d3/image.png)
In the pop-up login interface, enter the CVM's user name and password to connect to the CVM for the subsequent operations.
![putty3](//mc.qcloudimg.com/static/img/b632cf3e122832193a77afe04c93fbc1/image.png)

### 2.2 Install necessary software using Yum
1. After logging in to the CVM, you are granted the root permission by default. With the root permission, you can install necessary software all at once (Nginx, MySQL, PHP) by using the following command:
```
yum install nginx php php-fpm php-mysql mysql-server -y
```
When the installation is completed, "Complete!" will show in the PuTTY window. You can also use the scroll bar to view the current installer package version:
![](//mc.qcloudimg.com/static/img/54fe7152ded20d5048728b5b98566eb6/image.png)
The versions of software in the installer package are as follows:
Nginx: 1.10.2
MySQL: 5.1.73
PHP: 5.33
2. Set these software to start upon startup of the CVM.
```
chkconfig nginx on
chkconfig mysqld on
chkconfig php-fpm on
```

For more information, please see [Install Software Through Yum in CentOS Environment](https://cloud.tencent.com/document/product/213/2046).

### 2.3 Software configuration
You need to configure Nginx, MySQL, PHP and other software once they are installed. The procedures are as follows:
#### 2.3.1 Configure Nginx
1. Use Vim command to open the file `default.conf`, cancel the monitoring of IPv6 address and configure Nginx to realize linkage with PHP.
```
vim /etc/nginx/conf.d/default.conf
```
2. Press "I" key or "Insert" key to switch to the edit mode, clear all contents, and copy the following code to the file `default.conf`.
<div class="code"><p></p><pre> 
server {
    listen       80;
    root   /usr/share/nginx/html;
    server_name  localhost;

    #charset koi8-r;
    #access_log  /var/log/nginx/log/host.access.log  main;

    location / {
            index index.php index.html index.htm;
    }

    #error_page  404              /404.html;

    #redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    #pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    location ~ .php$ {
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index   index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
     }

 }</pre></div>
After modification, press "Esc" and enter ":wq", save the file and then return.
3. Start Nginx.
```
service nginx start
```

4. Test whether Nginx service is working properly.
In a browser, access the public IP of CentOS CVM to check if the Nginx service is working properly.
The appearance of the following page indicates that Nginx has been installed and configured successfully:
![](//mc.qcloudimg.com/static/img/1a992f4caab3388effc70a856eaac941/image.png)
 
#### 2.3.2 Configure MySQL
1. Start the MySQL server.
```
service mysqld start
```
2. Set the password for the root user of MySQL server, in this tutorial, to "123456". This user name and password will be used in the following steps.
```
 /usr/bin/mysqladmin -u root password "123456"
```

#### 2.3.3 Configure PHP
1. Start PHP-FPM service.
```
service php-fpm start
```
2. Configure the storage path for PHP session.
Open the file `/etc/php.ini`.
```
vim /etc/php.ini
```
Enter the following command and press Enter to locate "session.save_path":
```
/session.save_path
```
Press "I" key or "Insert" key to switch to the edit mode and change the path:
```
session.save_path = "/var/lib/php/session"
```
![](//mc.qcloudimg.com/static/img/0fad1c31cd587308d8a068d767d9a9b8/image.png)
Change the groups of all files in `/var/lib/php/session` to nginx and nginx.
```
chown -R nginx:nginx /var/lib/php/session 
``` 
 
#### 2.3.4 Verify environment configuration
1. Create the file `index.php` under a Web directory using the following command:
```
vim /usr/share/nginx/html/index.php
```
2. Press "I" key or "Insert" key to switch to the edit mode and enter the following code:
```
<?php
echo "<title>Test Page</title>";
echo "Hello World!";
?>
```
Then, press "Esc", enter ":wq", save the file and return.
3. Access the file `index.php` via a browser to check whether the environment configuration has been completed successfully:
```
http://CVM's public IP/index.php 
```
The appearance of the "Hello World!" indicates the successful configuration of LNMP environment.
![](//mc.qcloudimg.com/static/img/88de64e6ff862edfeae10acb2ee787ec/image.png)

## Step 3: Install and configure WordPress
### 3.1 Download WordPress
Tencent Cloud provides Yum download source with English version of built-in WordPress installer package. You can download a Chinese version from [WordPress official website](https://cn.wordpress.org/) and install it. Chinese version of WordPress is used in this tutorial.
1. Delete the file `index.html` under the root directory of the website.
```
rm /usr/share/nginx/html/index.html
```
You will be prompted whether to delete the file. Enter "y" and press Enter.

2. Download WordPress and decompress the file to the current directory.
```
wget https://cn.wordpress.org/wordpress-4.7.4-zh_CN.tar.gz
```
```
tar zxvf wordpress-4.7.4-zh_CN.tar.gz
```

### 3.2 Configure database
Before writing a blog, you need to build a database to store data. Configure the MySQL database by following the steps below.
1. Log in to the MySQL server.
Use root user to log in to the MySQL server.
```
mysql -uroot -p
```
When prompted, enter the password (123456 set in step 2.3.2, as the password of MySQL root user) to log in.

2. Create a database for WordPress and set a user name and password as follows, which are customizable.
Create a MySQL database "wordpress" for WordPress.
```
CREATE DATABASE wordpress;
```
Create a new user "user@localhost" for the MySQL database you just created.
```
CREATE USER user@localhost;
```
Set the password "wordpresspassword" for this user.
```
SET PASSWORD FOR user@localhost=PASSWORD("wordpresspassword");
```

3. Enable full access to the database "wordpress" for the created user.
```
GRANT ALL PRIVILEGES ON wordpress.* TO user@localhost IDENTIFIED BY 'wordpresspassword';
```

4. Use the following command for all the configurations to take effect.
```
FLUSH PRIVILEGES;
```

5. After the configuration is completed, exit MySQL.
```
exit
```

### 3.3 Write database information
After configuration, you also need to write the database information into WordPress's configuration file. The WordPress installation folder contains a sample configuration file "wp-config-sample.php". In this step, copy and edit this file to adapt to different configurations. 
1. Create a configuration file
Copy the file `wp-config-sample.php` to the file `wp-config.php`, create a new configuration file using the following command, and save the original sample configuration file as a backup.
```
cd wordpress/
cp wp-config-sample.php wp-config.php
```
2. Open and edit the new configuration file.
```
vim wp-config.php
```
Press "I" key or "Insert" key to switch to the edit mode, and write the database information configured in step 3.2 into the MySQL-related section in the file:

```
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'user');

/** MySQL database password */
define('DB_PASSWORD', 'wordpresspassword');

/** MySQL hostname */
define('DB_HOST', 'localhost');
```
After modification, press "Esc" and enter ":wq", save the file and then return.

### 3.4 Install WordPress
From step 3.1 to 3.3, you have decompressed the file to the installation folder, created MySQL database and user, and customized the WordPress configuration file. Now, you are going to install WordPress.
1. Move the installation file to the document root directory on the Web server, so as to run the installation script to complete the installation.
```
mv * /usr/share/nginx/html/
```
2. By entering the IP address (CVM's public IP or followed by the path of "wordpress folder") of WordPress site in the Web browser's address bar, you can go to the WordPress installation interface and configure WordPress.
![](//mc.qcloudimg.com/static/img/6012d2bcc2f5a5a78e333e57f08545f6/image.png)
3. Enter other installation information into the WordPress installation wizard and click "Install WordPress" to complete the installation.

| Required Information | Note | 
|---------|---------|
| Site title | WordPress website name. |
| User name | WordPress admin name. For security reasons, it is recommended to set a name other than the default user name "admin", which makes it more difficult to crack. |
| Password | You can use the default strong password or a custom password. Do not reuse the existing password and ensure that the password is stored in a secure location. |
| Your email | The email address for receiving notifications. | 

Now, you can log in to your WordPress blog website and publish blogs.

## Subsequent Steps
1. You can set a domain name for your WordPress blog website, allowing users to access your website with an easy-to-remember domain name instead of a complicated IP address.
You can [purchase a domain name via Tencent Cloud](https://dnspod.cloud.tencent.com/?from=qcloud). 

2. ICP licensing is required for websites whose domain names are directed to Chinese servers. A website cannot be launched until an ICP license is obtained for its domain name. You can obtain an [ICP license](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa) on Tencent Cloud free of charge. It generally takes 20 days to complete audit.
3. You need to configure domain name resolution on Tencent Cloud [DNS](https://console.cloud.tencent.com/cns/domains) to allow users to access your website with a domain name. For more information, please see [Domain Name Resolution](https://cloud.tencent.com/document/product/302/3446).


In addition, you can also expand the service capacity horizontally and vertically on Tencent Cloud platform.
- Expand the CPU and memory specifications of a single CVM instance to enhance the processing capacity of the server. [Learn more >>](https://cloud.tencent.com/document/product/213/5730)
- Add more CVM instances, and use [Cloud Load Balance](https://cloud.tencent.com/document/product/214) to ensures a balanced distribution of loads among multiple instances.
- Use [Auto Scaling](https://cloud.tencent.com/document/product/377) to automatically scale up/down the CVM instances based on your business volume.
- Use [Cloud Object Storage](https://cloud.tencent.com/document/product/436) to store static web pages, massive images and videos.

You can also watch the following video to build WordPress on Ubuntu.
> Note: The demonstration operation interface in the video is only for reference. Please refer to the actual operation interface.

**Watch video:**

