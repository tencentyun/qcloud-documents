## Getting Started
Host Security can be installed together with Tencent Cloud CVMs and CPMs or installed separately.
Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click **Products** -> **Security**-> **Host Security** to go to the Host Security console page to check if Host Security has been installed on your CVM.

The following shows how the Host Security console looks like:
![](https://mc.qcloudimg.com/static/img/51114266f017374b9a12addf6c39570a/image.png)

- For the server surrounded by the yellow box, no host security product is installed. You can install the product depending on the server's operating system as shown below:
  - [Windows CVM](#windows-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E7.8E.AF.E5.A2.83) 
  - [Linux CVM](#linux-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E7.8E.AF.E5.A2.83) 
- For the server surrounded by the blue box, the Basic Protection edition of Host Security is installed. You can [Activate Professional Protection](#Activating Professional Protection ) for it.
- For the server surrounded by the red box, the Professional Protection edition of Host Security is installed to provide a multi-dimensional security protection for system.

## Intrusion Detection
After Host Security is installed, such features as Trojan detection, login behavior audit and password cracking blocking are enabled automatically. You can check the intrusion detection details of a server by either of the following two ways:
- In the **Security Overview** tab on the Host Security console page, locate the server for which you want to view details in the server list, click the IP address of the server, and then click **Protection Details** to view the intrusion detection details of the server.
- In the Host Security console page, click **Intrusion Detection** in the menu on the left, and then click the feature you want to view to check the intrusion detection details of all servers for which you have activated Host Security.

For operations related to additional features, please see:
-  [Trojan Handling Operations](/document/product/296/13008)

- [Login Audit Operations](/document/product/296/13643)

## Vulnerability Detection
After Host Security is installed with Professional Protection activated, system component vulnerability detection, Web component vulnerability detection, and security baseline detection are available for you.
In the Host Security console page, click **Vulnerability Management** in the menu on the left, and then click the feature you want to view to check the vulnerability detection details of all the servers for which you have activated Professional Protection of Host Security, and fix the vulnerabilities as instructed.

## Installing Host Security
### Windows CVM  
#### Applicable versions
Supported versions:
- Windows server 2012
- Windows server 2008 R2
- Windows server 2003 (limited support)
- Windows server 2016

#### Download address
- Download address for public network:
```
https://imgcache.qq.com/qcloud/csec/yunjing/static/ydeyes_win32.exe
```
- Download address for basic network (non-VPC server):
```
http://u.yd.qcloud.com/ydeyes_win32.exe
```
- Download address for VPC & CPM:
```
http://u.yd.tencentyun.com/ydeyes_win32.exe
```

### Note about installation
Verification of installation success on Windows:
Open the task manager to check if YDService and YDLive processes have been invoked. If so, the installation is successful.
![Windows processes](https://mc.qcloudimg.com/static/img/cb809b0f1e6a61d548a24f4bd4b57a61/image.jpg)

#### FAQs
1. Firewall blocking
It is recommended to configure the firewall policy to open the access address of the Host Security backend server to Internet:
Domain name: `s.yd.qcloud.com; l.yd.qcloud.com; u.yd.qcloud.com`
Port: `5574, 8080, 80, 9080`

2. Note about DNS
If you do not need to use the default DNS, forward all resolutions of the root domains `tencentyun.co' and ` yd.qlcoud.com` to the default DNS.

### Linux CVM
#### Applicable versions
Supported versions:
- RHEL: Versions5,6 and 7(32/64 bit)
- CentOS: Versions5,6 and 7(32/64 bit)
- Ubuntu: 9.10-14.4(32/64 bit)
- Debian: Versions6,7

#### Download address
- Download address for public network: 
```
wget --no-check-certificate https://imgcache.qq.com/qcloud/csec/yunjing/static/yunjinginstall.sh && sh ./yunjinginstall.sh
```

- Download address for basic network (non-VPC server):
```
wget http://u.yd.qcloud.com/ydeyesinst_linux64.tar.gz && tar -zxvf ydeyesinst_linux64.tar.gz && sh self_cloud_install_linux64.sh
```

- Download address for VPC & CPM:
```
wget http://u.yd.tencentyun.com/ydeyesinst_linux64.tar.gz && tar -zxvf ydeyesinst_linux64.tar.gz && sh self_cloud_install_linux64.sh
```

#### Note about installation
After running the installation command, check whether YDService and YDLive processes have been invoked. If so, the installation is successful. The command is as follows:
```
ps -ef|grep YD
```

![](https://mc.qcloudimg.com/static/img/25c18ce3ed1673ca7d47425c28c3b8ef/image.png)

If the processes have not been started, run the command manually with root user to start the programs. The command is as follows:
```
/usr/local/qcloud/YunJing/YDEyes/YDService
```

#### Uninstallation

You can uninstall Host Security by either of the following two ways:
**Uninstall in console**
1. Log in to the console.
Log in to the Tencent Cloud [Console](https://console.cloud.tencent.com/).
2. Go to the Host Security page.
Go to the [Host Security](https://console.cloud.tencent.com/yunjing) management page to check if Host Security has been installed for your CVM.
3. Uninstall Host Security
In the server list, select the server for which you want to uninstall Host Security to uninstall it.
 ![](https://main.qcloudimg.com/raw/9f5f5eec8b585df854fb735df0b47a47.png)

**Uninstall in system**
1. Windows
Locate the uninstall.exe file in the following path, and double-click it to uninstall Host Security.
Path: `C:\Program Files\QCloud\YunJing\uninst.exe`
2. Linux
Enter the command `/usr/local/qcloud/YunJing/uninst.sh` to uninstall Host Security.

#### FAQs
1. Firewall blocking
It is recommended to configure the firewall policy to open the access address of the Host Security backend server to Internet:
Domain name: `s.yd.qcloud.com; l.yd.qcloud.com; u.yd.qcloud.com`
Port: `5574, 8080, 80, 9080`

2. Note about DNS
If you do not need to use the default DNS, forward all resolutions of the root domains `tencentyun.com` and ` yd.qlcoud.com` to the default DNS.

## Activating Professional Protection
You can activate Professional Protection by either of the following two ways:
-  Click **Buy Now** in the [Host Security Introduction page](https://intl.cloud.tencent.com/product/hs) on the Tencent Cloud official website to go to the login page of Tencent Cloud console. After login, you can activate Professional Protection for your CVM as needed.

- Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click **Products** -> **Security** -> **Host Security** to go to the Host Security configuration page, and then click **Activate Professional Protection** in the **Operation** column in the **Security Overview** page to activate Professional Protection for your CVM.
