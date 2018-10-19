带外网是独立于数据网络之外的专用管理网络， 即使在数据网络发生故障或者设备宕机的情况下，您仍然可通过SSL VPN 连接带外网络，并远程管理和维护故障设备。通过带外网运维服务器，即叫作【带外管理】

# __登录带外SSL VPN__


## 准备工作

需要准备以下内容，才可以建立VPN连接：


- 腾讯云VPN客户端
- VPN网关地址和VPN的用户名、密码

以下将介绍如何获取上述内容。

## 安装腾讯云VPN客户端

登录腾讯云黑石服务器控制台，选中任意一台服务器并打开详情页，找到【带外管理】标签。
在带外管理页面分别下载相应的VPN客户端。

![](https://mc.qcloudimg.com/static/img/e08bb2d98c97ebb61c06fdc1e7638106/001.png)


安装VPN客户端的操作系统要求：


- Windows操作系统：Windows XP，Windows Server 2003，Windows Vista，Windows 7，Windows 8，Windows 8.1，Windows 10 Enterprise
- Mac操作系统：MacOS 10.9，MacOS 10.10，MacOS 10.11，MacOS 10.12

下载完成后，请安装VPN客户端

## 获取VPN网关地址及VPN用户名、密码
在【带外管理】标签内找到VPN网关IP、用户名、密码和域。

![](https://mc.qcloudimg.com/static/img/0d426a9f7d8f62a457f4b95a5f9eec5d/002.png)



## Windows操作系统的VPN客户端使用指南
打开VPN客户端，输入VPN网关IP、用户名、密码和域。

![](https://mc.qcloudimg.com/static/img/a7b820a30427d720504de3c9e069ade9/003.png)
单击【连接】，即可成功建立了VPN连接

![](https://mc.qcloudimg.com/static/img/2dd765f8c114421bc0c67333f33c5a7f/004.png)

## MAC操作系统的VPN客户端使用指南
打开mac版的VPN客户端，单击添加按钮，添加新的VPN连接。

![](https://mc.qcloudimg.com/static/img/ce60d1d393853355c111f67802292249/005.png)


确认并单击【next】


![](https://mc.qcloudimg.com/static/img/a129b19a14a0596bc940bc3c2c17e952/006.png)

输入相应的VPN网关IP、用户名、密码，并单击【Finish】。


![](https://mc.qcloudimg.com/static/img/c2b10dd164933e92f8f6972fe9737c13/007.png)

输入相应的域【Domain】。

![](https://mc.qcloudimg.com/static/img/68566234130f01caf1a2b38b4cbd4139/008.png)
单击【connect】即可

![](https://mc.qcloudimg.com/static/img/97bb61f78e5299aa452dae8589400dad/009.png)
 __注意__ : 


- 腾讯云账号下同可用区的所有黑石服务器，使用的带外SSL VPN网关相同。
- 每个客户的带外SSL VPN，发送报文速率上限5Mbps，接收报文速率上限5Mbps，最大并发连接数10。


# 登录服务器带外系统
需要准备以下内容，才能登录服务器带外系统。


- 建立SSL VPN连接
- 服务器带外登录IP、用户名、密码
- 通过服务器带外IP浏览器登录

建立VPN连接后，在服务器详情页的【带外管理】标签,找到服务器带外登录IP、用户名、密码。

![](https://mc.qcloudimg.com/static/img/c6884c0c00b8515d306a82bb2c071277/010.png)
使用带外登录IP、用户名、密码，登录服务器带外系统。

![](https://mc.qcloudimg.com/static/img/d9a6ae97e4f90735de5caa4a582c1fc5/011.png)
 __注意__ : 每台服务器的带外登录IP、用户名、密码都不同。

# KVM控制台
远程KVM是一种服务器的专用管理工具，它允许您像操作本地计算机一样操作远端的服务器。
但它是在浏览器中运行的java applet完成。如遇到浏览器及java版本安全问题，请按以下步骤操作：

## 安装浏览器和JRE
推荐使用firefox,并且正确安装java版本(推荐使用JRE7u80版本)及java安全设置。请确认您使用的firefox浏览器是32位还是64位，并安装相应版本的JRE程序。安装JRE完毕后，请重启浏览器。
[Firefox下载](http://www.firefox.com.cn/download/)
[JRE7u80下载](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html)

## 设置JAVA安全级别
在windows系统【开始菜单】中找到[JRE]程序
打开java控制面板，请将您账号内的所有带外IP都设置在【例外站点】列表。

![](https://mc.qcloudimg.com/static/img/4678086a40776453153066fb7aa72881/012.png)

## 登录KVM控制台
以浪潮服务器为例演示如何登录远程KVM。请找到远程控制选项，下载JNLP文件

![](https://mc.qcloudimg.com/static/img/a35a3e1ba9bea017eb478fd0fae9a287/013.png)
请在安装了JRE的前提下，运行JNLP文件，如遇到安全警告请选择【接受风险】并单击【运行】

![](https://mc.qcloudimg.com/static/img/9f1a11106f7aceb452a8717664890c07/014.png)
打开KVM控制台后，即可登录该服务器。

![](https://mc.qcloudimg.com/static/img/0edf6dd157370d0f8469b02545663300/015.png)
注意：不同服务器厂商登录远程KVM的方式不同，请在带外页面找到与【远程控制】相关的选项，并按页面指引操作以登录远程KVM。