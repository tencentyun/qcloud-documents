This document introduces the PHP configuration of Windows CVM. For more information, please see [Installation of PHP versions above 5.3](#jump) and [Installation of PHP 5.3 and earlier](#jump1) as needed.
## Prerequisites
To configure PHP in Windows CVMs, you need to add and install IIS role. For more information, please see [Installing and Configuring IIS](/doc/product/213/2755).


## Installation of PHP Versions above 5.3
<span id="jump">  </span>
For PHP versions above 5.3, the installer mode has been canceled, and the installation is only performed through zip file or debug pack. The following example shows the zip installation in Windows Server 2012 R2 environment.

### Downloading File

 1. Download the PHP zip installer from the CVM (download URL: http://windows.php.net/download/).
>Note:
> You must select Non Thread Safe (NTS) x86 package when running under IIS. If you have to select x64 package for PHP in Windows Server 32bit (x64), you cannot select IIS. In this case, you can use Apache as an alternative option.

	Select the installer as shown below:
  ![](//mc.qcloudimg.com/static/img/d02eb264ae4d5fbaaf8fd01a08433c61/image.png)
  ![](//mc.qcloudimg.com/static/img/f719e6893f1addd0b260d0c740e4e0ba/image.png)
  ![](//mc.qcloudimg.com/static/img/24ca3df57de6195ad45adabad1c5dc13/image.png)

 2. The installation of PHP versions above 5.3 is dependent on Visual C++ Redistributable Update. Download and install VC Update Installer according to the name of downloaded PHP installer by referring to the relations as shown in the following table:

| PHP Installer Name | Download Link for Visual C++ Redistributable Installer|
|---------|---------|---------|
| php-x.x.x-nts-Win32-VC14-x86.zip | [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/zh-cn/download/details.aspx?id=48145) |
| php-x.x.x-nts-Win32-VC11-x86.zip | [Visual C++ Redistributable for Visual Studio 2012 Update 4](https://www.microsoft.com/zh-cn/download/details.aspx?id=30679) |
| php-x.x.x-nts-Win32-VC9-x86.zip | [Microsoft Visual C++ 2008 SP1 Redistributable Package (x86)](https://www.microsoft.com/zh-cn/download/details.aspx?id=5582) |

  If the downloaded PHP installer is as shown below:
![](//mccdn.qcloud.com/static/img/974ac7192d8f10236fcc27bfd54b8aed/image.png)

then download the installer for VS 2015 version based on the relation indicated in the first row, and download and install the following two `.exe` files:
![](//mc.qcloudimg.com/static/img/7128c0b621f2534cecddd23b6f3efdb9/image.png)


### Installation and configuration
 1. Unzip the PHP zip installer (in this case, extract to `C:\PHP`), copy `php.ini-production` and rename it to `php.ini`, as shown below:
![](//mc.qcloudimg.com/static/img/1be9b1771a93852aff909b08159a5b79/image.png)

 2. Click **Server Manager** -> **IIS**; On the local IIS, right-click and select **IIS Manager**:
![](//mc.qcloudimg.com/static/img/f0387eeb456b7d60e8a5b601cbd3c6b0/image.png)

	Click on the host name (IP) on the left to go to the home page, and then double-click **Handler Mappings**:
![](//mc.qcloudimg.com/static/img/898aa0d2f61c467d333601b75c57704c/image.png)

	Click **Add Module Mappings** on the right, enter the following information in the pop-up box, and click **OK** to save:
![](//mc.qcloudimg.com/static/img/6f0fd95475a7c00a5779592d15a7753e/image.png)

	>**Note:**
	> If you are unable to select `php-cgi.exe` as the executable file, please change the filename extension of the selected file to .exe:![](//mc.qcloudimg.com/static/img/d749a9fe4c77f6ea7b55afd8fd37e808/image.png)

 3. Click the server IP on the left to go to the home page and double-click **Default Documents**:
![](//mc.qcloudimg.com/static/img/b5861a95bf6aafd8f4bcaf1c12e9f9be/image.png)

	Click **Add** on the right to add a default document named `index.php`:
![](//mc.qcloudimg.com/static/img/6b2543227fec95d1b9bed5f4260a86bb/image.png)

 4. Click the server IP on the left to go to the home page and double-click **FastCGI Settings**:
![](//mc.qcloudimg.com/static/img/aa23422c038b1024354f01ed0cb3ab73/image.png)

	Click **Edit** on the right, and select `php.ini` path in **Monitor the Changes Made to File**:
![](//mc.qcloudimg.com/static/img/b4f1ec7d39519dc7d2e89d52ed8a1a87/image.png)
![](//mc.qcloudimg.com/static/img/a2acbed50587552c6ef7ed796b82eb36/image.png)

 5. Create a PHP file `index.php` under `C:\inetpub\wwwroot` and write the following:
```
<?php
phpinfo();
?>
```

 6. Visit `http://localhost/index.php` in the browser on CVM and check whether the environment has been configured successfully. The appearance of the following page indicates that the configuration has been completed successfully:
![](//mc.qcloudimg.com/static/img/46eec848975e77e770569eb5d8849d37/image.png)



## Installation of PHP 5.3 and earlier versions
<span id="jump1">  </span>
>Note:
> PHP 5.3 and earlier versions are no longer available on the official download address http://windows.php.net/download/. To use these versions, download them locally and upload them to the CVM or search on the CVM network. For more information on uploading files, please see [here](https://cloud.tencent.com/document/product/213/2761).

 1. Open PHP installer in the CVM.

 2. Select **IIS FastCGI** in **Web Server Setup**, as shown below:
![](//mc.qcloudimg.com/static/img/ef2f5959779cd733934d11ecbcb4a7f5/image.png)

 3. Complete the installation of PHP under the guidance of installation interface.

 4. Create a PHP file `hello.php` under `C:/inetpub/wwwroot`, as shown below:
![](//mc.qcloudimg.com/static/img/31d992849b04c1bc76c0d4ca61ab8a4b/image.png)

	The following content is written to the `hello.php` file:

	```
	<?php
	echo "<title>Test Page</title>";
	echo "hello world";
	?>
	```

 5. Access the public network IP of Windows CVM via browser to check whether the environment configuration has been completed successfully. The appearance of the following page indicates that the configuration has been completed successfully:
![](//mc.qcloudimg.com/static/img/89cebc1127f5c76790c2a9bf3be9fd1f/image.png)



