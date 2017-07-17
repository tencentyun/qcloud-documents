# __服务器带外管理__

  带外网是独立于数据网络之外的专用管理网络， 即使在数据网络发生故障或者设备宕机的情况下，您仍然可通过SSL VPN 连接带外网络，并远程管理和维护故障设备。通过带外网运维服务器，即叫作【带外管理】

## __1.登录带外SSL VPN__
 __准备工作__ 
需要准备以下内容，才可以建立VPN连接：
__服务器带外管理__

- 腾讯云VPN客户端
- VPN网关地址和VPN的用户名、密码


以下将介绍如何获取上述内容。
 __安装腾讯云VPN客户端__ 
腾讯云VPN客户端下载地址
安装VPN客户端的系统要求：


- 主流 Window /Mac操作系统
- VPN客户端版本 1.0.0

下载完成后，请安装VPN客户端
 __获取VPN网关地址及VPN用户名、密码__ 
登录腾讯云黑石服务器控制台。
选中任意一台服务器并打开详情页，找到【带外管理】标签。
在【带外管理】标签内找到VPN网关、用户名、密码和域。

![](https://mc.qcloudimg.com/static/img/6c3c5b30915dcf9eb0041c07068e1bd0/01.png)

打开VPN客户端，将刚刚找到的VPN网关IP、用户名、密码和域，设置在VPN客户端。


![](https://mc.qcloudimg.com/static/img/a7b820a30427d720504de3c9e069ade9/02.png)
点击【连接】，即可成功建立了VPN连接

![](https://mc.qcloudimg.com/static/img/2dd765f8c114421bc0c67333f33c5a7f/03.png)
注意: 腾讯云账号下同地域的所有黑石服务器，共用一个带外SSL VPN网关及用户名、密码。

## __2.登录服务器带外系统__

需要准备以下内容，才能登录服务器带外系统。


- 建立SSL VPN连接
- 服务器带外登录IP、用户名、密码
- 通过服务器带外IP浏览器登录

建立VPN连接后，在服务器详情页的【带外管理】标签,找到服务器带外登录IP、用户名、密码。

![](https://mc.qcloudimg.com/static/img/c6884c0c00b8515d306a82bb2c071277/04.png)
使用带外登录IP、用户名、密码，登录服务器带外系统。

![](https://mc.qcloudimg.com/static/img/d9a6ae97e4f90735de5caa4a582c1fc5/05.png)
 __注意__ : 每台服务器的带外登录IP、用户名、密码都不同。


## __3.KVM控制台__
远程KVM是一种服务器的专用管理工具，它允许您像操作本地计算机一样操作远端的服务器。
但它是在浏览器中运行的java applet完成。如遇到浏览器及java版本安全问题，请按以下步骤操作：
 __安装浏览器和JRE__ 
推荐使用firefox,并且正确安装java版本及java安全设置。请确认您使用的firefox浏览器是32位还是64位，并安装相应版本的JRE程序。安装JRE完毕后，请重启浏览器。
 __设置JAVA安全级别__ 
在windows系统【开始菜单】中找到[JRE]程序
打开java控制面板，请将您账号内的所有带外IP都设置在【例外站点】列表。
![](https://mc.qcloudimg.com/static/img/4678086a40776453153066fb7aa72881/06.png)

 __登录KVM控制台__ 
以浪潮服务器为例演示如何登录远程KVM。请找到远程控制选项，下载JNLP文件
![](https://mc.qcloudimg.com/static/img/a35a3e1ba9bea017eb478fd0fae9a287/07.png)

请在安装了JRE的前提下，运行JNLP文件，如遇到安全警告请选择【接受风险】并点击【运行】

![](https://mc.qcloudimg.com/static/img/9f1a11106f7aceb452a8717664890c07/08.png)
打开KVM控制台后，即可登录该服务器。

![](https://mc.qcloudimg.com/static/img/0edf6dd157370d0f8469b02545663300/09.png)
注意：不同服务器厂商登录远程KVM的方式不同，请在带外页面找到与【远程控制】相关的选项，并按页面指引操作以登录远程KVM。
## __4.安装OS__
由于华为服务器的带外安装iso流程与其他厂家的服务器不同，华为服务器的安装流程请参考第5章节。
打开—Media—Virtual Media Wizard, 把需要安装的本地ISO镜像加载并连接

![](https://mc.qcloudimg.com/static/img/24189d647a0fc747c1433958bee32642/10.png)

打开软键盘

![](https://mc.qcloudimg.com/static/img/cfeb0fe0382a84025a6bfaa6e4bb2c58/11.png)
重启机器

![](https://mc.qcloudimg.com/static/img/408dad9bebe6e3f43695a57b50d0f640/12.png)
点击F11进入boot menu，通过Virtual CD-ROM启动

![](https://mc.qcloudimg.com/static/img/c7a5ea7a9a588a3e73a8461a32ad7563/13.png)


![](https://mc.qcloudimg.com/static/img/66b6653802cb27812d1111774ce908e2/14.png)

进入安装界面，重装系统

![](https://mc.qcloudimg.com/static/img/4d4f690684aaadffe1d49d93b79b2be8/15.png)


![](https://mc.qcloudimg.com/static/img/f99020b50f443505b8447ddc074cd82b/16.png)

## __5.华为服务器安装OS__

在带外控制台以此点击：配置—系统启动项—光驱，来实现设置好启动项为：光驱。

![](https://mc.qcloudimg.com/static/img/5105731f9785458d62e33f4f37e9287c/17.png)
打开kvm：建议使用共享模式打开，在kvm上点击重启后，关闭KVM

![](https://mc.qcloudimg.com/static/img/0f59d2ca43562134b8332998cfca11d4/18.png)
由于sharelink的问题，重启后，有10-15秒的时间，kvm没法点击；
等kvm的选项可以点击时，点击打开kvm，并挂载ISO

![](https://mc.qcloudimg.com/static/img/4c148e334bc7e1ff65f65528db78de01/19.png)
等待机器重启，进入安装页面

![](https://mc.qcloudimg.com/static/img/db43b427cc34e9b3e44a991d02f02a40/20.png)

