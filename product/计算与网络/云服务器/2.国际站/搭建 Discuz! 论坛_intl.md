Discuz!, with more than 2 million website users, is one of the world's most mature forum website software systems with the widest coverage. This tutorial takes Discuz! X3.2 as an example to show how to build a Discuz! forum website in LAMP (Linux + Apache + MySQL + PHP) environment.

Here, we provide two ways to build the Discuz! forum, and you can choose the appropriate one based on your needs:
- Use a Discuz! image for quick installation
This is recommended for users who build a Discuz! forum for the first time and are less familiar with relevant command operations.
- Self-install the LAMP environment and build a forum
This is recommended for users who are experienced in building forums and know how to work with relevant commands.

> Linux: Linux system
Apache: One of the widely used Web server software for parsing Web applications
MySQL: A database management system
PHP: A program used to generate Web pages from a Web server

## Installation via Image 
The following services/tools are used in this tutorial:
**CVM**: In this tutorial, we are going to create a CVM using the Tencent Cloud's Cloud Virtual Machine (CVM) to build a Discuz! Forum.
**Domain name registration**: To access your Discuz! forum with an easy-to-remember domain name, you can use Tencent Cloud's domain name registration service to purchase a domain name.
**ICP licensing**: Required for websites whose domain names are directed to Chinese servers. A website cannot be launched until an ICP license is obtained for its domain name. You can complete ICP licensing via Tencent Cloud.
**Tencent Cloud DNS**: You need to configure domain name resolution to allow users to access your website with a domain name instead of an IP address. You can resolve domain names through Tencent Cloud DNS service.
 
Following shows how to install a forum using an image:
![](//mc.qcloudimg.com/static/img/db454d696e269f0f29c9c63abf11db59/image.png)

### Step 1: Install a Discuz! image 
Install a Discuz! image according to the actual situation:
- Directly install an image if a Tencent Cloud CVM exists.
- Purchase a Tencent Cloud CVM.

#### Directly install an image if a Tencent Cloud CVM exists
1. Log in to the [CVM console](https://console.cloud.tencent.com/cvm), and click **Cloud Virtual Machine** on the left navigation bar to find the one used to build Discuz!.
Click **More** on the right menu and select **Reinstall the system**.
![](//mc.qcloudimg.com/static/img/5abc4a177ce635a8357b03ee7061c57e/image.png)
2. Find a Discuz! image in **Website templates** of **Service market** to reinstall the system. This tutorial uses "Discuz! X3.2 official version (CentOS 7.2 64-bit Webmin | LAMP)". You can choose an image based on your needs.
![](//mc.qcloudimg.com/static/img/f9970cfef97cb508581f3519dfd98bd2/image.png)

#### Purchase a CVM
1. Obtain a Discuz! image.
Log in to [Tencent Cloud](https://cloud.tencent.com/login?s_ur=https://console.cloud.tencent.com), enter the [Cloud Market](http://market.cloud.tencent.com/categories?q=discuz) from the top navigation bar on the home page, and enter "Discuz" in the search box to get a free Discuz! image.
![](//mc.qcloudimg.com/static/img/54021a861602cdf6560306848cdcef0f/image.png)
2. Purchase a CVM
You are required to purchase a CVM when purchasing an image. The configuration of the CVM depends on the visits to your website. For more information, please see [How to create a Linux CVM](https://cloud.tencent.com/document/product/213/2972).
![](//mc.qcloudimg.com/static/img/f62666aee21008a0dee3b16422be9bcd/image.png)
3. Create a CVM
After the purchase, you can create a new CVM on the console. Once created, the CVM is running automatically. Please wait 2-3 minutes before proceeding to step 2.
![](//mc.qcloudimg.com/static/img/8c9ac3bbd8464cc9621f95f9a775889e/image.png)
 
#### Note: The public IP of the CVM will be used in the following steps. Be sure to copy and save it.
### Step 2: Verify Discuz! image 
You need to verify the image so as to work with it properly. After the image is installed successfully, wait for about 3 minutes before using a browser to open the URL `http://CVM's public IP`. The following page appears in case of a successful access:
![](//mc.qcloudimg.com/static/img/865f57d34c75853887597c361b629eeb/image.png)
If the above page does not appear after a long time, please follow the suggestions below for troubleshooting:
- Restart the CVM and try again.
- Ping the public IP of the CVM to check whether the network connection is available.
- Reinstall the system as instructed in step 1.
- Check the CVM's [security group configuration](https://cloud.tencent.com/document/product/213/5221) to confirm whether the default HTTP port is disabled.

We have never come across a situation where the initialization page cannot be opened when the above methods are tried out.

### Step 3: (Optional) Configure a domain name
You can set a domain name for your Discuz! forum website, allowing users to access your website with an easy-to-remember domain name instead of a complicated IP address. Users who build forums for learning can only use an IP to install the software directly for temporary use, which is not recommended.
In this case, skip this step and proceed directly to step 4.
If you already have a domain name or want to access your forum via a domain name, refer to the steps below.
1. [Purchase a domain name](https://dnspod.cloud.tencent.com/?from=qcloud) via Tencent Cloud. For more information on domain name registration, please see [How to register a domain name](https://cloud.tencent.com/document/product/242/8582).
2. Obtain an [ICP license](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa).
This is required for websites whose domain names are directed to Chinese servers. A website cannot be launched until an ICP license is obtained for its domain name. You can obtain an ICP license via Tencent Cloud free of charge. It generally takes 20 days to complete audit.
3. Configure domain name resolution through Tencent Cloud [DNS](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns).
 3.1 Log in to the [DNS console](https://console.cloud.tencent.com/cns/domains), select a domain name or add an existing domain name.
 3.2 Click **Resolve** to enter the domain name's record management page.
![](//mc.qcloudimg.com/static/img/c2e3da7449cf42697a15f5c2bf9e80cf/image.png)
 3.3 Click **Add** to add a record to be resolved.
![](//mc.qcloudimg.com/static/img/4a5054890890418d83ced42db4f3a98a/image.png)

### Step 4: Install and configure Discuz! 
1. Access the domain name configured in step 3 through a browser, click Discuz! - **Install and Configure** to enter the installation page.
![](//mc.qcloudimg.com/static/img/9c158431b6de083811f5a93d545309ed/image.png)
2. Click **Agree** to go to the installation step 1: check installation environment.
![](//mc.qcloudimg.com/static/img/ad97b179b5b4977d86ca09a78ef05a7d/image.png)
3. Upon confirmation of the current status, click **Next Step** to set running environment.
![](//mc.qcloudimg.com/static/img/c5a521673ed6f1a3528ba67ca5886ee4/image.png)
4. Select clean install, and click **Next Step** to create database.
![](//mc.qcloudimg.com/static/img/11a44bd86bfdfcd1fe3dcce6e8f200e6/image.png)
5. Create a database for Discuz!, and use default MySQL account and password (root/123456) of the image to connect to the database. Set a system email as well as admin account, password and email. Click **Next Step** to start installation.
**Note**: Remember your admin account and password.
![](//mc.qcloudimg.com/static/img/5d5184cfb34f98d791c243273b910065/image.png)
6. After the installation is completed, click **Your forum has been installed successfully. Click here to access.** to access your forum.
![](//mc.qcloudimg.com/static/img/41dab1ec86120a565bdd790238f271da/image.png)
 
For more information on Discuz! Installation, please watch the video at the bottom. (For reference only. Refer to actual operations)
For more information, please see [Discuz! image installation guide](http://www.websoft9.com/xdocs/discuz-image-guide).

## Self-installation
The following services/tools are used in this tutorial:
**CVM**: In this tutorial, we are going to create a CVM using the Tencent Cloud's Cloud Virtual Machine (CVM) to build a Discuz! forum. 
**Domain name registration**: To access your Discuz! forum with an easy-to-remember domain name, you can use Tencent Cloud's domain name registration service to purchase a domain name.
**ICP licensing**: Required for websites whose domain names are directed to Chinese servers. A website cannot be launched until an ICP license is obtained for its domain name. You can complete ICP licensing via Tencent Cloud.
**Tencent Cloud DNS**: You need to configure domain name resolution to allow users to access your website with a domain name instead of an IP address. You can resolve domain names through Tencent Cloud DNS service.
**PuTTY**: One of the free tools ideal for remote login. This easy-to-operate software is used in this tutorial for forum building. [Download PuTTY ](http://xiazai.sogou.com/comm/redir?softdown=1&u=-9C432O39iS-1WMoK6o75d2rbT1v8F8PVRelGJ0KRMgmFySI7r-cdPLmpUQMiC7rMWKCgnK7gooqOgr0EiOgKJ36wBs_inYy&pcid=-3190951004095154321&filename=putty.zip&w=1907&stamp=20170524).
 
Following shows how to self-install a forum:
![](//mc.qcloudimg.com/static/img/6b60f627a0f72093c39bf0fb34b35724/image.png)
### Step 1: Create a CVM 
1. [Purchase a CVM](https://buy.cloud.tencent.com/cvm?regionId=8&projectId=8) based on your needs. For more information on how to purchase a CVM, please see [Create Linux CVMs](https://cloud.tencent.com/document/product/213/2972).
2. After the CVM is created, you can log in to the [Tencent Cloud console](https://console.cloud.tencent.com/cvm) to view or edit its status.
![](//mc.qcloudimg.com/static/img/cbd7d2717a9d162df28b4d517ab1d815/image.png)

The operating system version of the CVM in this tutorial is CentOS 6.8. Save the following information to be used in the subsequent steps:
- CVM's user name and password
- CVM's public IP

### Step 2: Build LAMP environment 
For CentOS system, Tencent Cloud provides a software installation source synced with the CentOS official version, containing the most recent and stable version of software, which can be quickly installed directly through Yum.
#### 2.1 Run PuTTY to connect to Linux CVM
1. [Download PuTTY ](http://xiazai.sogou.com/comm/redir?softdown=1&u=-9C432O39iS-1WMoK6o75d2rbT1v8F8PVRelGJ0KRMgmFySI7r-cdPLmpUQMiC7rMWKCgnK7gooqOgr0EiOgKJ36wBs_inYy&pcid=-3190951004095154321&filename=putty.zip&w=1907&stamp=20170524) to your computer, decompress the file, and then double-click "putty.exe" to open the configuration page as follows:
2. Select "Session", and enter the name or IP of the CVM to be accessed in "Host Name (or IP address)", such as "server1" or "192.168.2.10". In this tutorial, the CVM's public IP is used. Leave other configuration options unchanged.
3. Specify a name for the session in "Saved Sessions" field, and click "Save" to save the session configuration.
![putty1](//mc.qcloudimg.com/static/img/85df3247daae4982003a91ad1ad6f89e/image.png)
4. After the configuration is completed, click "Open", and a prompt window appears for certificate confirmation. Select "Yes".
![putty2](//mc.qcloudimg.com/static/img/b7883110e977fb0d94310379a152c5d3/image.png)
5. In the pop-up login interface, enter the CVM's user name and password to connect to the CVM for the subsequent operations.
![putty3](//mc.qcloudimg.com/static/img/b632cf3e122832193a77afe04c93fbc1/image.png)

#### 2.2 Install necessary software
1. After logging in to the CVM using PuTTY, you are granted the root permission by default. You can enter relevant commands in PuTTY. Enter the following command to install necessary software all at once (Apache, MySQL, PHP):
```
yum install httpd php php-fpm php-mysql mysql mysql-server -y
```
When the installation is completed, "Complete!" will show in the PuTTY window. You can use the scroll bar to view the current installer package version:
![](//mc.qcloudimg.com/static/img/4d1e4ee237bcd67ad39051f843bded53/image.png)
The versions of software in the installer package are as follows:
Apache: 2.2.15
MySQL: 5.1.73
PHP: 5.33
2. Launch the service
```
service httpd start
service mysqld start
service php-fpm start
```
3. Configure MySQL database
We need to create a database and a user to store data for the Discuz! program. The database service has been launched in the previous step, and here we need to set a root password for MySQL to allow users to access it.
```
mysqladmin -u root password "XXXXXXXX" ((the password is customizable))
```
After setting the MySQL password, verify the account password.
```
mysql -u root -p
``` 
If you can log in to the MySQL using the password you just set, the configuration is correct. Exit the MySQL:
```
exit
```
![](//mc.qcloudimg.com/static/img/5f180f866334ee46e4b7e77851c5add0/image.png)

#### 2.3 Verify environment configuration
Generally, by this point, the environment has been successfully configured. In this step, we need to verify and ensure the success of environment build.
1. Use the following command to create a test file `test.php` in the default root directory "/var/www/html" of Apache:
```
vim /var/www/html/test.php
```
2. Press "I" key or "Insert" key to switch to the edit mode and enter the following code:
```
<?php
echo "<title>Test Page</title>";
phpinfo()
?>
```
Then, press "Esc", enter ":wq", save the file and return.
3. Access the file `test.php` via a browser to check whether the environment configuration has been completed successfully:
```
http://CVM's public IP/test.php 
```
The appearance of the following page indicates the successful configuration of LAMP environment.
![](//mc.qcloudimg.com/static/img/3e2a1d07e4429d640461b64956b240cb/image.png)

### Step 3: (Optional) Configure a domain name
You can set a domain name for your Discuz! forum website, allowing users to access your website with an easy-to-remember domain name instead of a complicated IP address. Users who build forums for learning can only use an IP to install the software directly for temporary use, which is not recommended.
In this case, skip this step and proceed directly to step 4.
If you already have a domain name or want to access your forum via a domain name, refer to the steps below.
1. [Purchase a domain name](https://dnspod.cloud.tencent.com/?from=qcloud) via Tencent Cloud. For more information on domain name registration, please see [How to register a domain name](https://cloud.tencent.com/document/product/242/8582).
2. Obtain an [ICP license](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa).
This is required for websites whose domain names are directed to Chinese servers. A website cannot be launched until an ICP license is obtained for its domain name. You can obtain an ICP license via Tencent Cloud free of charge. It generally takes 20 days to complete audit.
3. Configure domain name resolution through Tencent Cloud [DNS](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns).
 3.1 Log in to the [DNS console](https://console.cloud.tencent.com/cns/domains), select a domain name or add an existing domain name.
 3.2 Click **Resolve** to enter the domain name's record management page.
![](//mc.qcloudimg.com/static/img/c2e3da7449cf42697a15f5c2bf9e80cf/image.png)
 3.3 Click **Add** to add a record to be resolved.
![](//mc.qcloudimg.com/static/img/4a5054890890418d83ced42db4f3a98a/image.png)

### Step 4: Install Discuz!  
#### 4.1 Download Discuz! 
1. If the Discuz! installer package is not built in Tencent Cloud, download it from [Discuz! official website](http://www.comsenz.com/downloads/install/discuzx).
```
wget http://download.comsenz.com/DiscuzX/3.2/Discuz_X3.2_SC_UTF8.zip
```
2. Decompress the installer package.
```
unzip Discuz_X3.2_SC_UTF8.zip
```

#### 4.2 Preparations for installation
1. Copy all files under the decompressed folder "upload" to "/var/www/html/".
```
cp -r upload/* /var/www/html/
```
2. Grant write permission to other users. After these directory files are uploaded to the server, only root users have the write permission by default.
```
chmod -R 777 /var/www/html
```

#### 4.3 Install Discuz!
Now, the forum has been completely built and can be installed in the browser.
1. By entering the domain name or IP address (CVM's public IP) of the Discuz! site configured in step 3 in the Web browser's address bar, you can see the Discuz! installation interface. Click **Agree** to go to the installation step 1: check installation environment.
![](//mc.qcloudimg.com/static/img/ad97b179b5b4977d86ca09a78ef05a7d/image.png)
2. Upon confirmation of the current status, click **Next Step** to set running environment.
![](//mc.qcloudimg.com/static/img/c5a521673ed6f1a3528ba67ca5886ee4/image.png)
3. Select clean install, and click **Next Step** to create database.
![](//mc.qcloudimg.com/static/img/11a44bd86bfdfcd1fe3dcce6e8f200e6/image.png)
4. Create a database for Discuz!, and use the root account and password set in step 2.2 to connect to the database. Set a system email as well as admin account, password and email. Click **Next Step** to start installation.
**Note**: Remember your admin account and password.
![](//mc.qcloudimg.com/static/img/5d5184cfb34f98d791c243273b910065/image.png)
5. After the installation is completed, click **Your forum has been installed successfully. Click here to access.** to access your forum.
![](//mc.qcloudimg.com/static/img/41dab1ec86120a565bdd790238f271da/image.png)
 
**Watch video**:

