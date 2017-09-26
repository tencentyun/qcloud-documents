本文档旨在介绍几种Windows环境下基本的软件安装和环境配置，您可以根据需要自行选择是否安装。<font color="red">新手用户并不是接下来的每一步都必须执行，请在确定了服务器用途后再进行相应配置。</font>您也可以通过获取服务市场的镜像来进行启动云服务器，很多服务市场镜像都集成了必要服务，免除了您安装配置的各种工作，具体详情请参见[服务市场](http://market.qcloud.com/?categoryId=64&page=1&orderby=2)。

以下均使用Windows Server 2008示例。
## 1. 安装配置IIS和ASP
本例为Windows Server 2008环境，Windows Server 2012的配置可以参考[这里](http://www.qcloud.com/doc/product/213/%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AEIIS%E5%8F%8APHP#1.1.-windows2012r2.E7.89.88.E6.9C.AC.E7.A4.BA.E4.BE.8B)。

点击底部栏【服务器管理器】-【角色】，点击【添加角色】按钮。（此时系统可能会要求重启，请按系统指示进行操作）
![](//mccdn.qcloud.com/static/img/d09bb74a5baa87e31c184ec6d75cb57d/image.png)


选择【服务器角色】-【Web服务器（IIS）】。
![](//mccdn.qcloud.com/static/img/f6975a71dcaabfa18b76b0c5b0f5a8cb/image.png)

选择功能，勾选需要的角色服务，
![](//mccdn.qcloud.com/static/img/c750f9bbd9a1f2c9edfe78231d1aa758/image.png)

选择完成后点击【下一步】，确认信息后点击【安装】按钮，等待安装结束后，通过在本地浏览器访问Windows云服务器的公网IP来验证IIS安装是否成功。
![](//mccdn.qcloud.com/static/img/07a707f660f9dea79c86ed342ccb1af3/image.png)

通过【信息服务管理器】-【网站】-【Default Web Site】-【高级设置】-【物理路径】来设置网站根目录（默认为C:\inetpub\wwwroot）：
![](//mccdn.qcloud.com/static/img/03df77ba147a055bcbeeac6fe86ebe2b/image.png)

由于角色服务已经选择了ASP，此时您即可以开始基于ASP的网站开发了。使用index.asp进行测试，注意文件存放目录必须为网站根目录下：
![](//mccdn.qcloud.com/static/img/5f28c401eab2fd59719c2c43b7b7f4ca/image.png)
![](//mccdn.qcloud.com/static/img/bda072e406546f9954168c8724fcd5d1/image.png)

## 2. 搭建MySQL
通常情况下Windows系统经常使用SQL Server数据库，但由于SQL Server属于收费产品需要您自行授权（也可购买[腾讯云SQL Server数据库CDB实例](http://www.qcloud.com/product/sqlserver.html)）。本文档主要介绍搭建MySQL 5.5的具体步骤。

下载MySQL 5.5安装包（下载地址：http://dev.mysql.com/downloads/mysql/ )，运行安装程序，选择典型安装方式（Typical）
![](//mccdn.qcloud.com/static/img/96039d46303894a81b161e73a5e53f08/image.png)


选择【自定义安装】，选择服务器类型、数据库类型、安装路径、链接数、端口、字符集：
![](//mccdn.qcloud.com/static/img/850064f6ca3f34d63dbb4e1c9bb30153/image.png)
![](//mccdn.qcloud.com/static/img/899ec4ba3dfbdec9099bd23739390130/image.png)
![](//mccdn.qcloud.com/static/img/6b42170fa5fc9a1f70d39d50ce920e8f/image.png)
![](//mccdn.qcloud.com/static/img/84f139f4d0fc825adf832efa2835409f/image.png)
![](//mccdn.qcloud.com/static/img/a2ac370045e5f495b56ddb0628b9f420/image.png)
![](//mccdn.qcloud.com/static/img/e3ad54af349fee1c95951fc667ce6dd7/image.png)
![](//mccdn.qcloud.com/static/img/79cbd16767ecc0b2fa268cc025db8f8a/image.png)


设置运行方式（建议两种都选择上以便使用命令行管理MySQL）：
![](//mccdn.qcloud.com/static/img/7837ddb917b5c3244da877c79aae671e/image.png)

<font color="red">设置root密码：</font>
![](//mccdn.qcloud.com/static/img/3bb1f9bbc079fda2a5ca59ffe5060a27/image.png) 

完成配置，进行安装：
![](//mccdn.qcloud.com/static/img/3325317d0c770640f887d9e4ef274266/image.png)

通过设置的root密码在命令行下登录MySQL：
![](//mccdn.qcloud.com/static/img/24d4cee90f961ae260e34e91c051c0cc/image.png)


## 3. 安装PHP
本例为PHP 5.3版本安装，更高版本的安装可以参考[这里](http://www.qcloud.com/doc/product/213/%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AEIIS%E5%8F%8APHP#2.2.-php-5.3.E4.B9.8B.E5.90.8E.E7.89.88.E6.9C.AC.E5.AE.89.E8.A3.85)。

下载PHP安装包（下载地址： http://windows.php.net/download/ ），本文档以5.3版本为例，选择如下图对应的安装包：
![](//mccdn.qcloud.com/static/img/fbfdc56c240c227bd9e79d23ca3f6539/image.png)

下载完成后进行安装PHP，需要选择Web服务时，选择“IIS FastCGI”，如下图所示：
![](//mccdn.qcloud.com/static/img/0766466daaa805ed4936c1479c4a1128/image.png)

点击框框标准的小硬盘，选择entire install，把扩展组件全都安装上：
![](//mccdn.qcloud.com/static/img/a59ca63ed4c1fd8a3522aa5901fc1015/image.png)

根据指引完成安装。

## 4. 使用FileZilla搭建FTP服务
下载FileZilla Server，官方下载地址：https://sourceforge.net/projects/filezilla/files/FileZilla%20Server/

下载完成后启动安装程序，阅读许可协议，点击【I Agree】进入下一步安装；选择安装内容，默认安装标准即可，点击【Next】（其中“Source Code”是源代码，不需要勾选）：
![](//mccdn.qcloud.com/static/img/c778f5e5835d7361c71726fd9c267d2b/image.jpg)

选择安装路径、选择FileZilla Server的启动方式以及管理端口。
共有3种启动方式：将FileZilla Server作为服务安装，随Windows系统启动；将FileZilla Server作为服务安装，手动启动；不将FileZilla Server作为服务安装，随Windows系统启动。一般情况选择第一种。管理端口选择未被占用的端口即可。
![](//mccdn.qcloud.com/static/img/ada799498cf21fa303680b5fbd8b71a8/image.jpg)

配置控制台启动方式。
共有3种选择：所有用户适用，自动启动；仅对当前用户适用，自动启动；手动启动。一般情况选择第一种即可。点击【Install】开始安装。
![](//mccdn.qcloud.com/static/img/c310e67a90a48fbd5dc8d2a67e4efe1b/image.jpg)

启动FileZilla Server，出现一个配置IP、管理端口的对话框，这里输入<font color="red">本地IP（即127.0.0.1）</font>，并且输入之前配置的管理端口（本例为14147），点击【OK】：
![](//mccdn.qcloud.com/static/img/e4b60a5950f6d5a1fd09480022d634b6/image.jpg)

点击工具栏上的user按钮小图标，进入用户配置界面；点击【Add】按钮新增用户；在弹出的对话框中输入用户名（本例测试用户名为tencent-qcloud），点击【OK】进入下一步：
![](//mccdn.qcloud.com/static/img/2eceb6e6481c3c8ca1b0d62f4b8fbe03/image.png)

勾选“password”，为新增的用户设置密码，点击【OK】按钮：
![](//mccdn.qcloud.com/static/img/39e8f56e2df01260aff5af866fb8b4f8/image.jpg)

出现提示告知添加用户目录，点击【确定】进入设置界面。点击【Add】新增用户目录。
![](//mccdn.qcloud.com/static/img/46e210f97c4c57a520ab7deababcafc7/image.jpg)
![](//mccdn.qcloud.com/static/img/a728994312b6c8d0fb9ed182e5131e46/image.jpg)

选择要用作FTP资源的目录（本例使用已新建的Tencent-Qcloud目录），点击【确定】：
![](//mccdn.qcloud.com/static/img/4b0710e79c9523d2e672f4ed0b7d6ce0/image.jpg)

对于每一个资源目录，选中能访问该目录的用户并配置相关的访问权限（请删除Shared Folders下面的New directory项，否则可能报错)。至此，FileZilla服务已经搭建好。
![](//mccdn.qcloud.com/static/img/627d28cfacb6a67c1fb3a027f3f1d240/image.jpg)

客户端通过本地FileZilla工具，连接至云服务器上搭建的FTP服务器。输入FTP服务器公网IP、账号、密码，点击【快速连接】，即可看到服务器分享给该用户的目录，并且可以看到之前放在该目录里面的文件“欢迎使用腾讯云服务器.txt”。
![](//mccdn.qcloud.com/static/img/fd74b176677cebc2d98fb812aec4e5be/image.png)

FileZilla服务器此刻可监控到客户端的连接：
![](//mccdn.qcloud.com/static/img/2542a78b00aaa930c92e8f8a9d88fdb1/image.jpg)
