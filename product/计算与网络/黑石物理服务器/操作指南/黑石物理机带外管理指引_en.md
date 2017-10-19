Out-of-band network is a dedicated management network that is independent of the data network. Even in case of a data network failure or device crash, you can still connect to the out-of-band network via SSL VPN and remotely manage and maintain faulty devices. Operating and maintaining CPMs via out-of-band network is known as "Out-of-Band Management".

# __Log in to Out-of-band SSL VPN__


## Preparation

The following are needed for establishing a VPN connection:


- Tencent Cloud VPN Client
- VPN gateway IP as well as VPN username and password

Details are described below.

## Installing Tencent Cloud VPN Client

Log in to Tencent Cloud CPM console, select any of the CPMs and open the details page to locate the "Out-of-Band Management" tab.
Download correct VPN client from out-of-band management page.

![](https://mc.qcloudimg.com/static/img/e08bb2d98c97ebb61c06fdc1e7638106/001.png)


Requirement for operating system in which VPN client is installed:


- Windows operating systems: Windows XP, Windows Server 2003, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10 Enterprise
- Mac operating systems: MacOS 10.9, MacOS 10.10, MacOS 10.11, MacOS 10.12

When the download is complete, install the VPN Client

## Obtaining the VPN Gateway IP as well as VPN Username and Password
Locate the VPN gateway, user name, password and domain in the "Out-of-Band Management" tab.

![](https://mc.qcloudimg.com/static/img/0d426a9f7d8f62a457f4b95a5f9eec5d/002.png)



## How to Use VPN Client in Windows Operating System
Open VPN client, enter VPN gateway IP, user name, password and domain.

![](https://mc.qcloudimg.com/static/img/a7b820a30427d720504de3c9e069ade9/003.png)
Click "Connect" to establish a VPN connection.

![](https://mc.qcloudimg.com/static/img/2dd765f8c114421bc0c67333f33c5a7f/004.png)

## How to Use VPN Client in MAC Operating System
Open VPN client for MAC, and click "Add" button to add a new VPN connection.

![](https://mc.qcloudimg.com/static/img/ce60d1d393853355c111f67802292249/005.png)


Confirm and click "Next".


![](https://mc.qcloudimg.com/static/img/a129b19a14a0596bc940bc3c2c17e952/006.png)

Enter related VPN gateway IP, username, password, and click "Finish".


![](https://mc.qcloudimg.com/static/img/c2b10dd164933e92f8f6972fe9737c13/007.png)

Enter corresponding "Domain".

![](https://mc.qcloudimg.com/static/img/68566234130f01caf1a2b38b4cbd4139/008.png)
Click "Connect" to complete the process.

![](https://mc.qcloudimg.com/static/img/97bb61f78e5299aa452dae8589400dad/009.png)
 __Note__: 


- All the CPMs in the same availability zone under a Tencent Cloud account use the same out-of-band SSL VPN gateway.
- For each customer's SSL VPN, the upper limit for the speed of both sending and receiving messages is 5 Mbps, and the maximum number of concurrent connections is 10.


# Logging in to Out-of-band System of CPM
The followings are required for logging in to the out-of-band system of CPM.


- Create an SSL VPN connection
- Out-of-band login IP, username, password for the CPM
- Log in via browser using out-of-band IP of CPM.

After VPN connection is established, locate the out-of-band login IP, user name, password for the CPM in the "Out-of-Band Management" tab on CPM details page.

![](https://mc.qcloudimg.com/static/img/c6884c0c00b8515d306a82bb2c071277/010.png)
Log in to the out-of-band system of CPM with out-of-band login IP, username and password.

![](https://mc.qcloudimg.com/static/img/d9a6ae97e4f90735de5caa4a582c1fc5/011.png)
 __Note__: Each CPM has a different out-of-band login IP, username and password.

# KVM Console
Remote KVM is a dedicated CPM management tool that allows you to operate a remote CPM in the same way as you do a local computer.
But this is done in the Java applet running in the browser. In case of security issues of browser and Java version, please follow the steps below:

### Installing Browser and JRE
You're recommended to use Firefox, install the correct Java version (JRE7u80 is recommended) and make correct Java security settings. Please verify whether you are using a 32-bit or 64-bit Firefox browser and install the correct version of JRE. After installing the JRE, restart the browser.
[Download Firefox](http://www.firefox.com.cn/download/)
[Download JRE7u80](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html)

## Setting JAVA Security Level
Locate [JRE] in the "Start" menu.
Open the Java control panel and set all of the out-of-band IPs under your account in the "Exception Sites" list.

![](https://mc.qcloudimg.com/static/img/4678086a40776453153066fb7aa72881/012.png)

## Logging in to KVM Console
The following shows how to log in to a remote KVM by taking Inspur server as an example. Locate "Remote Control" options and download the JNLP file

![](https://mc.qcloudimg.com/static/img/a35a3e1ba9bea017eb478fd0fae9a287/013.png)
When JRE has been installed, run the JNLP file. When receiving a security warning, select "Accept Risk" and click "Run".

![](https://mc.qcloudimg.com/static/img/9f1a11106f7aceb452a8717664890c07/014.png)
Open the KVM console to log in to the server.

![](https://mc.qcloudimg.com/static/img/0edf6dd157370d0f8469b02545663300/015.png)
Note: The way of logging in to remote KVM varies with different server manufactures. Please locate the options related to "Remote Control" on the out-of-band page and log in to remote KVM as instructed by the page.
