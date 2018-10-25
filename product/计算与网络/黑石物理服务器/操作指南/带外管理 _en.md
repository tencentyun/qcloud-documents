
Out-of-band network is a dedicated management network that is independent of the data network. Even in case of a data network failure or device crash, you can still connect to the out-of-band network via SSL VPN and remotely manage and maintain faulty devices. Operating and maintaining CPMs via out-of-band network is known as "Out-of-Band Management".


## Logging in to SSL VPN
### Preparations
The following are needed for establishing a VPN connection:
<li>Tencent Cloud VPN Client</li>
<li>VPN gateway IP as well as VPN username and password</li>


Next, we'll guide you through the process step by step.

### Installing Tencent Cloud VPN Client
Tencent Cloud VPN Client [Download URL](http://vpnclient-10040239.file.myqcloud.com/iNodeSetup7.2%20%28E0407%29.rar "")

System requirements for installing VPN Client:

<li>Main-stream Windows operating system</li>

<li>VPN Client version	1.0.0</li>

<li>When the download is complete, install the VPN Client</li>

### Obtaining the VPN gateway IP as well as VPN username and password

Log in to Tencent Cloud [Cloud Physical Machine Console](https://console.cloud.tencent.com/cpm)

Select any of the CPMs and open the details page to locate the "Out-of-Band Management" tab.  
Locate the VPN gateway, user name, password and domain in the "Out-of-Band Management" tab.
![](http:////mc.qcloudimg.com/static/img/81dc7ec19eaab7aabc61e0dab38f2e2b/image.png)

Open VPN client, and set the VPN gateway IP, user name, password and domain you just found on the VPN Client.  
![](http:///mc.qcloudimg.com/static/img/9a423d872f235b0aef545952363084ab/image.png)

Click "Connect" to establish a VPN connection.  
![](http:////mc.qcloudimg.com/static/img/a37d604c4324595effbf6146d8e69540/image.png)

*Note: All CPMs under your Tencent Cloud account share one VPN gateway, username and password*

## Logging in to CPM from out-of-band network

The following are needed for logging in to a CPM from out-of-band network:
<li>Create an SSL VPN connection</li>
<li>Out-of-band login IP, username, password for the CPM</li>
### Logging in with out-of-band IP of CPM
After establishing a VPN connection, please follow the steps below to log in to the CPM.

Locate the out-of-band login IP, user name, password for the CPM in the "Out-of-Band Management" tab on CPM details page.
![](http://mc.qcloudimg.com/static/img/9136a3f9e9a65deb72e0f3393d609254/image.png)

Log in to the CPM with out-of-band login IP, username and password.
![](http://mc.qcloudimg.com/static/img/5f3e839f35ed59f93f501f6018c406cd/image.png)


*Note: Each CPM has a different out-of-band login IP, username and password*

## Remote KVM
Remote KVM is a dedicated CPM management tool that allows you to operate a remote CPM in the same way as you do a local computer.  
But this is done in the Java applet running in the browser. In case of security issues of browser and Java version, please follow the steps below:

### Install browser and JRE
You're recommended to use Firefox, install the correct Java version and make correct Java security settings. Please verify whether you are using a 32-bit or 64-bit Firefox browser and install the correct version of JRE. After installing the JRE, restart the browser.

[FireFox](http://www.firefox.com.cn/download/)  
[JRE](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html)

### Setting JAVA security level
If you are using a Windows system, please locate [JRE] in the "Start" menu 
Open the Java control panel and set all of the out-of-band IPs under your account in the "Exception Sites" list.
![](http://mc.qcloudimg.com/static/img/4678086a40776453153066fb7aa72881/image.png)

### Logging in to Remote Terminal
The following shows how to log in to a remote terminal by taking Inspur server as an example. Select "Remote Terminal" and download the JNLP file
![](http://mc.qcloudimg.com/static/img/a0f8ea92860599ee84cef64d5424c4fb/image.png)

When JRE has been installed, run the JNLP file. When receiving a security warning, select "Accept Risk" and click "Run".
![](http://mc.qcloudimg.com/static/img/bb488ef0b23136416157cadac511cf9b/image.png)

Open the KVM console to log in to the server.
![](http://mc.qcloudimg.com/static/img/621d8581d874366d0cb4576cab579a9f/image.png)
* The way of logging in to remote terminal varies with different server manufactures. Please locate the options related to "Remote Terminal" on the out-of-band page and log in to remote terminal as instructed by the page*





