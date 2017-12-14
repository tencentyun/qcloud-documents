## 1. Overview

Video Sharing page is a vehicle for LVB App sharing that can be opened in WeChat, QQ and other mobile Apps in a form of webpage, allowing users to watch videos, communicate with each other via IM, facilitate the spread of Apps and improve the exposure.

This document shows how to deploy the source code on a self-built Apache server, designed to guide engineers with little experience in static webpage deployment through the webpage code debugging.

## 2. How to Achieve Sharing

- App constructs the sharing URL with required parameters. For example:
<table class="t" style="text-align: center; width:750px">
<tbody>
<tr><td>
`http://imgcache.qq.com/open/qcloud/video/share/xiaozhibo.html?sdkappid=1400012345&acctype=8888&userid=test1234&type=0`
</td></tr>
</tbody></table>
- When a user opens the sharing URL, the sharing page fetches data from Mini LVB's livedemo server based on the URL parameters, including video playback URL, VJ data, IM room information, and then presents the video playback and IM messaging features.

## 3.Directory Structure of Demo
- sdk:  ## IM SDK code
- js:   js code of demo
- img:  Image file
- css:  Style file

## 4. Deploy the Sharing Page
The source code provides a series of static files for deployment to the static file servers, such as Nginx, Apache, Nodejs, etc.

### 3.1 Prepare the environment

- Operating system: Windows 7 64-bit
- Web server: Apache 2.4 64-bit
- Demo can also be run with other Web server, such as Nginx
- Server has a public IP and domain name. In this example, the domain name is `www.xiaozhibo.com`.

Welcome to Tencent Cloud's one-stop solution. It covers a range of solutions such as CVM and DNS, eliminating your efforts in a variety of configurations. For more information, please see

[https://cloud.tencent.com/product/cvm](https://cloud.tencent.com/product/cvm)


### 3.2 Install Apache

Download 64-bit Apache from:
http://www.apachehaus.com/cgi-bin/download.plx?dli=StmURFWaNJzTEx2KWVkRwAlVOpkVFVFdSxGZPVWQ

Check other versions from:
http://www.apachehaus.com/cgi-bin/download.plx

Decompress the downloaded zip file to a local directory, for example, D:\Program Files\directory.

Edit Apache configuration file:

```
D:\Program Files\Apache24\conf\httpd.conf
```

Locate Define SRVROOT, change the value to its right to the current Apache installation directory, as shown below:

```
Define SRVROOT "D:/Program Files/Apache24"
```

Then locate Listene 80. If port 80 is occupied (check this using netstat-a command under cmd), change it to another port, for example, port 8080, as shown below:

```
Listen 8080
```

After the modifications, save httpd.conf file.

Next, configure and install Apache service, which is a precondition for starting Apache:
Open the CMD window, and then enter:

```
"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
```
This command means installing Apache service and naming it as apache (you can change it to another name). And then press Enter.

When the installation is completed successfully, the result is shown as below:

```
C:\Users\peakerdong>"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
[Fri May 20 13:39:16.474314 2016] [mpm_winnt:error] [pid 14884:tid 144] AH00433: apache: Service 
is already installed.
```

An error message following "Errors reported here must be corrected before the service can be started" indicates the failure of installation. In this case, you need to fix the error first. If there is no such error message, the installation is successful.

Under the installation directory, locate D: \ Program Files\Apache24\bin\ApacheMonitor.exe, and then double click the file to run it. Double click the icon that appears at the bottom-right corner to open a window as shown below:
![](//mccdn.qcloud.com/static/img/02ef4d509e5579661953a9cc3dc4ee59/image.png)

Click "start" on the left to start Apache service.

Open the browser and enter `http://localhost`
If the port you set is 8080, then the access URL is `http://localhost: 8080/`
The appearance of the following page indicates Apahce has started successfully.
![](//mccdn.qcloud.com/static/img/1a051fa9cbedf08e55a979f732e824ef/image.png)

If the server has a public IP and domain name, you can use the domain name for access, for example:
`http://www.xiaozhibo.com/`

### 3.3 Run Demo

Copy the file under the share directory of the Demo to the running directory of Apache Web:

```
D:\Program Files\Apache24\htdocs
```

Then the URL for accessing the sharing page is

`http://www.xiaozhibo.com/share/xiaozhibo.html`

Note: This URL has not included required parameters.

Required parameters need to be appended to the above URL by Mini LVB App to construct the complete sharing URL as shown below:

`http://www.xiaozhibo.com/share/xiaozhibo.html?sdkappid=1400012894&acctype=6672&userid=test1234&type=0&ts=1479299174`

When a user opens the sharing URL, the sharing page fetches data from Mini LVB's livedemo server based on the URL parameters, including video playback URL, VJ data, IM room information, and then presents the video playback and IM messaging features.

## 3.4 References for server configuration

- [Setup of Apache Server and General Configurations of Static Websites](https://my.oschina.net/wdos/blog/71512)

- [Configuration of Nginx Static Server](http://www.cnblogs.com/h9527/p/5530298.html)





