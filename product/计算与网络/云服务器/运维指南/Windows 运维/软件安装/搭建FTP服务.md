
本文档介绍在 Windows 云服务器上搭建 FTP 服务的操作。此处使用 FileZilla 为例介绍，您也可以通过获取服务市场镜像，免除了您安装配置的各种工作，具体详情请参见 [云市场](https://market.cloud.tencent.com/list?cid=64) 

## 软件下载
 - FileZilla 是一个快速可靠的、跨平台的 FTP 、 FTPS 和 SFTP 软件。具有图形用户界面（GUI） 和很多特性。易于使用，支持多种协议，本例使用 FileZilla 进行配置演示和操作测试。
 - 进入官网下载 FileZilla，中文版官方下载地址： 
 `https://www.filezilla.cn/download`

## 安装配置
1. 下载 FileZilla Server 后启动安装程序，阅读许可协议，单击【我同意】进入下一步安装；选择安装内容，默认标准安装即可，单击【下一步】。
![](https://main.qcloudimg.com/raw/8d17fe17de20eb21f7cc8bc58d821037.png)

2.  <span id="step2"></span>选择安装路径、选择 FileZilla Server 启动方式以及管理端口。
3 种 FileZilla Server 安装启动方式：
  - 作为服务安装，随 Windows 系统启动。
  - 作为服务安装，手动启动。
  - 不作为服务安装，随 Windows 系统启动。

 一般情况选择默认，管理端口选择未被占用的端口即可。如下图所示：
 ![](https://main.qcloudimg.com/raw/c97294110f187db619e50097bb614f0e.png)
3. 安装完成后，启动 FileZilla Server 。出现配置 IP 、管理端口对话框。如下图所示：
  - 服务器地址：输入 127.0.0.1
  - 端口：填写 [步骤2](#step2) 设置的管理端口（本例为 14147 ）
![](https://main.qcloudimg.com/raw/05393c6c6519c9d052dc87f6ff09af4c.png)
填写完成后，单击【确定】。
4. 用户配置。单击工具栏左上角用户按钮小图标，单击【添加】新增用户；在弹出的对话框中输入用户名（本例测试用户名为 tencent-qcloud ），单击【确定】。
![](https://main.qcloudimg.com/raw/3f766e03c8b7bbd6e4a2679e2186d523.png)
5. 密码设置。勾选“密码”，为新增的用户设置密码后，单击【确定】。
![](https://main.qcloudimg.com/raw/4d0b34e03796e5e1aca0c9ac97d60c14.png)
6. 弹出提示框告知添加用户目录，单击【确定】进入设置界面。单击【添加】新增用户目录。
![](https://main.qcloudimg.com/raw/e5b0accf2129a6f54278487a6aa2a8ba.png)
7. 选择 FTP 资源目录。本例使用已新建的 Tencent-Qcloud 目录，单击【确定】。在该目录下放置文件`欢迎使用腾讯云服务器.txt`以便后续测试。
![](//mc.qcloudimg.com/static/img/abfe5bdfd1011f723b4e5d75e4b3de36/image.jpg)
8. 用户授权。选中右侧“用户”框中用户，选择中间目录名称及对应权限，单击【确定】。
![](https://main.qcloudimg.com/raw/fe1b57c00ef8e91461a814d94bec2238.png)
至此，FileZilla FTP 服务已经搭建好。

## 使用测试
通过 FileZilla Client 客户端工具，连接至云服务器上搭建的 FTP 服务器。输入该云服务器公网 IP 、FTP 用户、密码，单击【快速连接】，即可看到服务器分享给该用户的目录，并且可以看到之前放在该目录里面的文件“欢迎使用腾讯云服务器.txt ”。
![](https://main.qcloudimg.com/raw/ff94910a171be385bf8aaa7059f9c560.jpg)

FileZilla 服务器此刻可监控到客户端的连接。

![](https://main.qcloudimg.com/raw/7856575e8d7a57e1c72ad5a867ac46b8.jpg)
