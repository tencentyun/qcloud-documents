## 操作场景
本文档以 FileZilla 为例介绍在 Windows 云服务器上搭建 FTP 服务的操作。您也可以通过获取服务市场镜像，免除了您安装配置的各种工作，具体详情请参见 [云市场](https://market.cloud.tencent.com/list?cid=64)。

## 软件下载
 FileZilla 是一个快速可靠的、跨平台的 FTP 、 FTPS 和 SFTP 软件。具有图形用户界面（GUI） 和很多特性。易于使用，支持多种协议。
 FileZilla 中文版官方下载地址：[点此获取](https://www.filezilla.cn/download)

## 操作步骤

1. 登录云服务器。
2. 下载并运行 FileZilla Server 安装程序。
3. 阅读许可协议，单击【我接受】。
4. 选择安装的类型（保持默认即可），单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/8d17fe17de20eb21f7cc8bc58d821037.png)
5. 选择安装位置，单击【下一步】。
6. <span id="step2">选择 FileZilla Server 的启动模式，设置 FileZilla Server的端口，单击【下一步】。如下图所示：</span>
一般情况下，选择默认的启动模式，管理端口选择未被占用的端口即可。
 ![](https://main.qcloudimg.com/raw/c97294110f187db619e50097bb614f0e.png)
7. 单击【安装】，启动 FileZilla Server。
8. 在打开的 “连接到服务器” 窗口中，填写以下信息，单击【确定】，连接 FileZilla 服务器。如下图所示：
![](https://main.qcloudimg.com/raw/05393c6c6519c9d052dc87f6ff09af4c.png)
 - 服务器地址：输入127.0.0.1
 - 端口：填写 [步骤6](#step2) 设置的管理端口。例如 14147。
9. 在 FileZilla Server 窗口中，单击 <img src="https://main.qcloudimg.com/raw/6eaffea83cd46f08300a27dcdf1c62a1.png" style="margin: 0;">，打开用户窗口。
10. 在打开的 “用户” 窗口中，单击【添加】，弹出 “添加用户账户” 对话框。如下图所示：
![](https://main.qcloudimg.com/raw/2ed9ccaeee7a4a4b3278f50d5c8b30ff.png)
11.  在弹出的 “添加用户账户” 对话框中，输入用户名，单击【确定】。
例如，输入 tencent-qcloud 用户名。
12.  在 “用户” 窗口中，勾选【密码】，为新增的用户设置密码，并单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/4d0b34e03796e5e1aca0c9ac97d60c14.png)
13.  在弹出的提示框中，单击【确定】。
14.  在 “Shared folders” 设置界面，单击【添加】，新增用户目录。如下图所示：
![](https://main.qcloudimg.com/raw/e5b0accf2129a6f54278487a6aa2a8ba.png)
15.  选择 FTP 的资源目录，单击【确定】。如下图所示：
例如，选择 Tencent-Qcloud 目录作为 FTP 的资源目录，并在该目录下放置`欢迎使用腾讯云服务器.txt`文件，便于 [检验 FTP 服务](#checkFTPService)。
![](//mc.qcloudimg.com/static/img/abfe5bdfd1011f723b4e5d75e4b3de36/image.jpg)
16.  在 “共享文件夹” 栏中，设置用户对 FTP 的资源目录的操作权限。如下图所示：
![](https://main.qcloudimg.com/raw/fe1b57c00ef8e91461a814d94bec2238.png)
17.  单击【确定】，完成 FileZilla FTP 服务的搭建。

<sapn id="checkFTPService"></span>
## 检验 FTP 服务

1. 在本地 PC 中，安装并打开 FileZilla 客户端。
2. 在打开的 FileZilla 客户端中，输入云服务器公网 IP 、FTP 用户、密码，并单击【快速连接】，即可看到 FileZilla 服务器分享给该用户的目录，还可以看到之前放在该目录里面的文件“欢迎使用腾讯云服务器.txt ”。如下图所示：
![](https://main.qcloudimg.com/raw/ff94910a171be385bf8aaa7059f9c560.jpg)
3. 切换至 FileZilla 服务器，即可监控到 FileZilla 客户端的连接。如下图所示：
![](https://main.qcloudimg.com/raw/7856575e8d7a57e1c72ad5a867ac46b8.jpg)



