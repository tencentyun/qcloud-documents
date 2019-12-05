
本文档介绍在 Windows 云服务器上搭建 FTP 服务的操作。此处使用 FileZilla 为例介绍，您也可以通过获取服务市场镜像，免除了您安装配置的各种工作，具体详情请参见 [云市场](http://market.qcloud.com/?categoryId=64&page=1&orderby=2) 。

## 软件下载
 - FileZilla 是一个快速可靠的、跨平台的 FTP 、 FTPS 和 SFTP 软件。具有图形用户界面( GUI ) 和很多特性。易于使用，支持多种协议，本例使用 FileZilla 进行配置演示和操作测试。
 - 进入官网下载 FileZilla Server，官方下载地址： `https://sourceforge.net/projects/filezilla/files/FileZilla%20Server/`
 - 进入官网下载 FileZilla Client，官方下载地址： `https://sourceforge.net/projects/filezilla/files/FileZilla_Client/`

## 安装配置
 1. 下载 FileZilla Server 后启动安装程序，阅读许可协议，单击【I Agree】进入下一步安装；选择安装内容，默认安装标准即可，单击【Next】（其中 Source Code 是源代码，不需要勾选）。
![](//mc.qcloudimg.com/static/img/1575622f1b1366c8bcff8d71c777b561/image.jpg)

 2. 选择安装路径、选择 FileZilla Server 启动方式以及管理端口。
3 种 FileZilla Server 安装启动方式：
  - 作为服务安装，随 Windows 系统启动；
  - 作为服务安装，手动启动；
  - 不作为服务安装，随 Windows 系统启动。
  
 一般情况选择第一种，管理端口选择未被占用的端口即可。
 ![](//mc.qcloudimg.com/static/img/7091c25ad8381f3702dfc37b3d9d56fd/image.jpg)

 3. 配置控制台启动方式。
 3 种控制台启动方式：
  - 所有用户适用，自动启动；
  - 仅对当前用户适用，自动启动；
  - 手动启动。
  
	一般情况选择第一种，单击【Install】开始安装。
 ![](//mc.qcloudimg.com/static/img/129d6460bae48c8e59fe770ac5f08430/image.jpg)

 4. 安装完成后，启动 FileZilla Server 。出现配置 IP 、管理端口对话框，输入本地 IP （即 127.0.0.1）、第 2 步配置的管理端口（本例为 14147 ），单击【OK】。
 ![](//mc.qcloudimg.com/static/img/3953153a08d6fb1eda1fa087e8f19264/image.jpg)

 5. 用户配置。单击工具栏左上角 user 按钮小图标，单击【Add】按钮新增用户；在弹出的对话框中输入用户名（本例测试用户名为 tencent-qcloud ），单击【OK】。
 ![](//mc.qcloudimg.com/static/img/2a000f0e725f8d830a29e1ed18392ec0/image.png)

 6. 密码设置。勾选 “password” ，为新增的用户设置密码后，单击【OK】按钮。
 ![](//mc.qcloudimg.com/static/img/2635b4a5c6dc8d1debcb593b5307fe79/image.jpg)

 7. 弹出提示框告知添加用户目录，单击【确定】进入设置界面。单击【Add】新增用户目录。
 ![](//mc.qcloudimg.com/static/img/10e37b8b35a6a81381e2a398ae4d9764/image.jpg)

 8. 选择 FTP 资源目录。本例使用已新建的 Tencent-Qcloud 目录，单击【确定】。
 ![](//mc.qcloudimg.com/static/img/abfe5bdfd1011f723b4e5d75e4b3de36/image.jpg)
（可在该目录下放置文件`欢迎使用腾讯云服务器.txt`以便后续测试 ）。

 9. 用户授权。选中右侧“ User ”框中用户，选择中间目录名称及对应权限，单击【OK】。（请删除 Shared Folders 下面的 New directory 项，否则可能报错)。
![](//mc.qcloudimg.com/static/img/ada463488ce9abfd65d086db08aa35ce/image.jpg)

至此，FileZilla FTP 服务已经搭建好。

## 使用测试
通过 FileZilla Client 客户端工具，连接至云服务器上搭建的 FTP 服务器。输入 FTP 服务器公网 IP 、账号、密码，单击【快速连接】，即可看到服务器分享给该用户的目录，并且可以看到之前放在该目录里面的文件“欢迎使用腾讯云服务器.txt ”。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](//mc.qcloudimg.com/static/img/5e7fdbc24a8d5ca0690af8b09bf5a2e0/image.png)

 FileZilla 服务器此刻可监控到客户端的连接。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](//mc.qcloudimg.com/static/img/ff304d1fe6056e920c6637896f6aae3a/image.jpg)
