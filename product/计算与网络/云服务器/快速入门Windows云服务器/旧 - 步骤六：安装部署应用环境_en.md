This document describes the basic software installation and environment configuration in several Windows environments. You can select which features to install according to your needs. <font color="red">It is not necessary for beginners to perform all of the following steps. Please determine the purpose of the server before performing relevant configuration. </font>You can also start the CVM by acquiring images from Service Marketplace. Many of the images from Service Marketplace have been integrated with the necessary services, eliminating your efforts in installation and configuration. For details, please see [Service Market](http://market.qcloud.com/?categoryId=64&page=1&orderby=2).

The following examples use Windows Server 2008.
## 1. Installation and configuration of IIS and ASP
This example uses Windows Server 2008 as the operating environment. For configuration on Windows Server 2012, refer to [here](http://www.qcloud.com/doc/product/213/%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AEIIS%E5%8F%8APHP#1.1.-windows2012r2.E7.89.88.E6.9C.AC.E7.A4.BA.E4.BE.8B).

In the bottom bar, click "Server Manager" - "Role", then click "Add Roles" button. (At this point, you may be asked to restart the system. Please proceed as instructed by the system)
![](//mccdn.qcloud.com/static/img/d09bb74a5baa87e31c184ec6d75cb57d/image.png)


Select "Server Roles" - "Web Server (IIS)".
![](//mccdn.qcloud.com/static/img/f6975a71dcaabfa18b76b0c5b0f5a8cb/image.png)

Select "Role", then check the role services as needed.
![](//mccdn.qcloud.com/static/img/c750f9bbd9a1f2c9edfe78231d1aa758/image.png)

After selection, click "Next". After confirmation, click "Install". When the installation has been completed, verify whether the IIS has been installed successfully by accessing the public IP of Windows CVM via local browser.
![](//mccdn.qcloud.com/static/img/07a707f660f9dea79c86ed342ccb1af3/image.png)

Set the root directory for the website by clicking "Information Service Manager" - "Web Site" - "Default Web Site" - "Advanced Settings" - "Physical Path" (default is C:\inetpub\wwwroot):
![](//mccdn.qcloud.com/static/img/03df77ba147a055bcbeeac6fe86ebe2b/image.png)

Since ASP has been selected as the role service, now you can set about developing website based on ASP. Use index.asp to perform the test. Please note that the file storage directory should be located under the root directory of website:
![](//mccdn.qcloud.com/static/img/5f28c401eab2fd59719c2c43b7b7f4ca/image.png)
![](//mccdn.qcloud.com/static/img/bda072e406546f9954168c8724fcd5d1/image.png)

## 2. Set up MySQL
Generally, Windows systems use SQL Server database, but SQL Server is a paid product that needs your authorization (you can also purchase [Tencent Cloud SQL Server database CDB instance](http://www.qcloud.com/product/sqlserver.html)). This document describes the steps to set up MySQL 5.5.

Download MySQL 5.5 installer (download link: http://dev.mysql.com/downloads/mysql/), run the setup.exe, and select "Typical" as the setup type.
![](//mccdn.qcloud.com/static/img/96039d46303894a81b161e73a5e53f08/image.png)


Select "Custom", then select the server type, database type, installation path, the number of links, port, and character set:
![](//mccdn.qcloud.com/static/img/850064f6ca3f34d63dbb4e1c9bb30153/image.png)
![](//mccdn.qcloud.com/static/img/899ec4ba3dfbdec9099bd23739390130/image.png)
![](//mccdn.qcloud.com/static/img/6b42170fa5fc9a1f70d39d50ce920e8f/image.png)
![](//mccdn.qcloud.com/static/img/84f139f4d0fc825adf832efa2835409f/image.png)
![](//mccdn.qcloud.com/static/img/a2ac370045e5f495b56ddb0628b9f420/image.png)
![](//mccdn.qcloud.com/static/img/e3ad54af349fee1c95951fc667ce6dd7/image.png)
![](//mccdn.qcloud.com/static/img/79cbd16767ecc0b2fa268cc025db8f8a/image.png)


Set the running mode (it is recommended to check both boxes to use the command line to manage MySQL):
![](//mccdn.qcloud.com/static/img/7837ddb917b5c3244da877c79aae671e/image.png)

<font color="red">Set the root password: </font>
![](//mccdn.qcloud.com/static/img/3bb1f9bbc079fda2a5ca59ffe5060a27/image.png) 

Complete the configuration and proceed with installation:
![](//mccdn.qcloud.com/static/img/3325317d0c770640f887d9e4ef274266/image.png)

Log in to MySQL at the command line by typing in the root password you set:
![](//mccdn.qcloud.com/static/img/24d4cee90f961ae260e34e91c051c0cc/image.png)


## 3. Install PHP
This example shows the installation of PHP 5.3. For the installation of higher versions, please refer to [here](http://www.qcloud.com/doc/product/213/%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AEIIS%E5%8F%8APHP#2.2.-php-5.3.E4.B9.8B.E5.90.8E.E7.89.88.E6.9C.AC.E5.AE.89.E8.A3.85).

Download PHP installer (download link:  http://windows.php.net/download/). In this document, PHP 5.3 is taken as the example, for which the following installer is selected: 
![](//mccdn.qcloud.com/static/img/fbfdc56c240c227bd9e79d23ca3f6539/image.png)

After the download, install PHP. When you need to select Web service, select "IIS FastCGI", as shown below:
![](//mccdn.qcloud.com/static/img/0766466daaa805ed4936c1479c4a1128/image.png)

Click on the small hard disk within the box, select "Entire install" to install all of the extension components:
![](//mccdn.qcloud.com/static/img/a59ca63ed4c1fd8a3522aa5901fc1015/image.png)

Complete the installation as instructed by the system.

## 4. Set up FTP service using FileZilla
Download FileZilla Server (official download link: https://sourceforge.net/projects/filezilla/files/FileZilla%20Server/).

After the download, execute the setup.exe, read the license agreement, and click "I Agree" to proceed to the next step. Select the features you what to install. By default, select "Standard" as the installation type, then click "Next" ("Source Code" needs not to be checked):
![](//mccdn.qcloud.com/static/img/c778f5e5835d7361c71726fd9c267d2b/image.jpg)

Select the installation path, the startup mode of FileZilla Server and the management port.
FileZilla Server can be started in three ways: Is installed as a service and started with the Windows system; Is installed as a service and started manually; Is not installed as a service and is started with the Windows system. Generally, you can choose the first. You can simply select an unoccupied port as the management port.
![](//mccdn.qcloud.com/static/img/ada799498cf21fa303680b5fbd8b71a8/image.jpg)

Set startup mode for console.
There are three options: Is started automatically, apply to all users; Is started automatically, apply only to current user; Is started manually. Generally, you can choose the first. Click "Install" to begin the installation.
![](//mccdn.qcloud.com/static/img/c310e67a90a48fbd5dc8d2a67e4efe1b/image.jpg)

When FileZilla Server is started, a dialog box for setting IP and management port will appear, in which you need to enter the <font color="red"> local IP (127.0.0.1)</font> and the management port you set earlier (in this case, it is 14147) and then click "OK":
![](//mccdn.qcloud.com/static/img/e4b60a5950f6d5a1fd09480022d634b6/image.jpg)

Click the user icon on the toolbar, enter the user settings page; click "Add" button to add new user; In the pop-up box, enter a user name (in this case, the test user name is tencent-qcloud) and then click "OK" to proceed to the next step:
![](//mccdn.qcloud.com/static/img/2eceb6e6481c3c8ca1b0d62f4b8fbe03/image.png)

Check "Password" to set a password for the new user, then click "OK":
![](//mccdn.qcloud.com/static/img/39e8f56e2df01260aff5af866fb8b4f8/image.jpg)

You'll be prompted to add user directory, click "OK" to enter the settings page. Click "Add" to add the new user directory.
![](//mccdn.qcloud.com/static/img/46e210f97c4c57a520ab7deababcafc7/image.jpg)
![](//mccdn.qcloud.com/static/img/a728994312b6c8d0fb9ed182e5131e46/image.jpg)

Select the directory to be used as FTP resource (this example uses the newly created Tencent-Qcloud directory), and click "OK":
![](//mccdn.qcloud.com/static/img/4b0710e79c9523d2e672f4ed0b7d6ce0/image.jpg)

For each resource directory, select the user who can access the directory and set access permission for it (please delete the New directory entries under Shared Folders, or an error will occur). Now, the setup of FileZilla service has been completed.
![](//mccdn.qcloud.com/static/img/627d28cfacb6a67c1fb3a027f3f1d240/image.jpg)

Client connects to the FTP server that is set up on the CVM through local FileZilla tool. After entering the public IP, account ID and password of FTP server and clicking "Quick Connect", you can see the directory the server shares to the user, as well as the file "Welcome to Tencent CVM.txt" that was placed under the directory earlier.
![](//mccdn.qcloud.com/static/img/fd74b176677cebc2d98fb812aec4e5be/image.png)

FileZilla Server can now monitor the connection to the client:
![](//mccdn.qcloud.com/static/img/2542a78b00aaa930c92e8f8a9d88fdb1/image.jpg)
