> NOTE: Do not install any anti-virus software of PC type on Windows CVM. Such software may block the telnet port of the CVM, making it impossible to log in to the CVM. 

## 1. Installation and configuration of IIS
### 1.1. Example for Windows2012R2
1) Click "Start" at the bottom left corner of Windows CVM, select "Server Manager" to open the Server Manager interface.


2) Select "Add Roles and Features", then in "Before You Begin" in the "Add Roles and Features Wizard" pop-up box, click "Next". In "Installation Type", select "Role-based or Feature-based Installation", then click "Next".


3) In the left side of the window, select "Server Role" tab, check "Web Server (IIS)", click "Add Features" button in the pop-up box, and then click "Next".


4) In the "Features" tab, click "Next", and in the "Web Server Role (IIS)" tab, also click "Next".


5) In the "Role Services" tab, check the "CGI" option, then click "Next".


6) Confirm the installation and wait for the installation to be completed.


 7) When the installation has been completed, access localhost in the browser of CVM to verify whether the installation is successful. The appearance of the following page indicates that the installation has been completed successfully.
![](//mccdn.qcloud.com/static/img/dfa6725c4358e1a4214dcceb03e87028/image.png)
### 1.2. Example for Windows2008
1) Click "Server Manager" in the "Management Tool" in the "Start" menu at the bottom left corner of Windows CVM to open the Server Manager interface.


2) Click "Add Roles and Features" to add server roles. In this case, select "Web Server (IIS)", as shown below:

![](//mccdn.qcloud.com/img56b1bb12831b3.png)
![](//mccdn.qcloud.com/img56b1bcee2d9e8.png)

3) Click "Next". When selecting role services, check "CGI", as shown below:

![](//mccdn.qcloud.com/img56b1bd1b8f220.png)

4) After the settings are made, click "Install" to proceed with the installation:

![](//mccdn.qcloud.com/img56b1bd4f18f1a.png)

5) Access the public network IP of Windows CVM via browser to check whether the IIS service is running normally. The appearance of the following page indicates that IIS has been installed and configured successfully.

![](//mc.qcloudimg.com/static/img/066840d8117901d8d15fd95e0e273720/image.png)

## 2. Installation and configuration of PHP
### 2.1. Installation of PHP 5.3 and earlier versions
1) Download the PHP installer (Download from: http://windows.php.net/download/), select the installer indicated in the following figure:

![](//mccdn.qcloud.com/img56b1bdc4dbec6.png)


2) After the download, install PHP. When you need to select Web service, select "IIS FastCGI", as shown below:

![](//mccdn.qcloud.com/img56b1bdf45ec1f.png)

3) Complete the installation of PHP under the guidance of installation interface.

4) Create a PHP file hello.php under C: / inetpub / wwwroot, as shown below:
![](//mccdn.qcloud.com/img56b1be32d66ec.png)

The following content is written to the hello.php file:

```
Test Page";
echo "hello world";
?>
```

5) Access the public network IP of Windows CVM via browser to check whether the environment configuration has been completed successfully.

### 2.2. Installation of PHP versions above 5.3
For PHP versions above 5.3, the installer mode has been canceled, and the installation is only performed through zip file or debug pack. The following example shows the zip installation in Windows Server 2012R2 environment.

1) Download the PHP zip installer. Please note that you must select Non Thread Safe (NTS) x86 package when running under IIS.  (If you have to select x64 package for PHP in Windows Server 32bit (x64), you cannot select IIS. In this case, you can use Apache as an alternative option)

Select the installer as shown below:

![](//mccdn.qcloud.com/static/img/46ba4886a15ee851797ec5aa92743558/image.png)
![](//mccdn.qcloud.com/static/img/fb42955a0dbbdaf95d73469b845e4f97/image.png)
![](//mccdn.qcloud.com/static/img/8bc781ab6611058af2b3298682481447/image.png)

2) The installation of PHP versions above 5.3 depends on Visual C ++ Redistributable Update. Download and install VC Update Installer according to the name of downloaded PHP installer by referring to the relations as shown in the following table:

| PHP Installer Name | Download Link for Visual C ++ Redistributable Installer|
| --------- | --------- | --------- |
| Php-xxx-nts-Win32-VC14-x86.zip | [Visual C ++ Redistributable for Visual Studio 2015](https://www.microsoft.com/zh-cn/download/details.aspx?id=48145) |
| Php-xxx-nts-Win32-VC11-x86.zip | [Visual C ++ Redistributable for Visual Studio 2012 Update 4](https://www.microsoft.com/zh-cn/download/details.aspx?id=30679) |
| Php-xxx-nts-Win32-VC9-x86.zip | [Microsoft Visual C ++ 2008 SP1 Redistributable Package (x86)](https://www.microsoft.com/zh-cn/download/details.aspx?id=5582) |

For example, if the downloaded PHP installer is the one shown as below,
![](//mccdn.qcloud.com/static/img/974ac7192d8f10236fcc27bfd54b8aed/image.png)

then download the installer for VS2015 version based on the relation indicated in the first row, and download and install the .exe file.


3) Unzip the PHP zip installer (in this case, extract to C:\PHP), copy php.ini-production and rename it to php.ini.

4) Click "Server Manager" - "IIS"; On the local IIS, right-click and select IIS Manager.

Click on the host name (IP) on the left to go to the home page, then double-click "Handler Mappings".


Click "Add Module Mappings" button on the right, fill in the following information in the pop-up box, and click "OK" to save.

If you are unable to select php-cgi.exe as the executable file, please change the file name extension of the selected file to .exe.

5) Click on the host name (IP) on the left to return to the home page, then double-click "Default Document".

Click "Add" button on the right to add the default document with the name of index.php.

6) Click on the host name (IP) on the left to return to the home page, then double-click "FastCGI Settings".

Select the path, click the "Edit" button on the right, then in the "Monitor the Changes Made to File", select the php.ini path.


7) Create a PHP file index.php under C:\inetpub\wwwroot, to which the following content is written:

```
<?php

phpinfo ();

?>
```

Save, visit http: //localhost/index.php within from the CVM to verify whether PHP has been installed successfully:
![](//mccdn.qcloud.com/static/img/2c71d31eeb12d5b6434d1e3df36a213f/image.png)