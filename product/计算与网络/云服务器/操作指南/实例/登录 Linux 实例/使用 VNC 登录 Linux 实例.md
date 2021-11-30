## 操作场景

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装或者无法使用远程登录客户端，以及通过其他方式均无法登录的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。


## 使用限制

- VNC 登录的云服务器暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- VNC 登录云服务器时，需要使用主流浏览器，例如 Chrome，Firefox，IE 10及以上版本等。
- VNC 登录为独享终端，即同一时间只有一个用户可以使用 VNC 登录。

## 前提条件
已获取登录实例的管理员帐号及密码。
- 如在创建实例时选择系统随机生成密码，则请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
- 如已设置登录密码，则请使用该密码登录。如忘记密码，则请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。


## 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择需要登录的 Linux 云服务器，单击**登录**。如下图所示：
![](https://main.qcloudimg.com/raw/e82e7f4b606fc59d26990285d7bdbaa3.png)
3. 在打开的“标准登录 | Linux 实例”窗口，单击 **VNC登录**。如下图所示：
![](https://main.qcloudimg.com/raw/600264310b8e778ffadaa164a597faae.png)
4. 在打开的窗口中，在 “login” 后输入用户名，按 **Enter**。
Linux 实例默认用户名为 `root`，Ubuntu 系统实例默认用户名为 `ubuntu`，请按需填写。
5. 在 “Password” 后输入密码，按 **Enter**。
输入的密码默认不显示，登录完成后，命令提示符左侧将显示当前登录云服务器的信息。如下图所示：
![](https://main.qcloudimg.com/raw/69bd64692fdaffc0cbbbdd0b9d307722.png)


## 后续操作


当您成功登录云服务器后，您可以在腾讯云服务器上搭建个人站点，论坛或者使用其他操作。相关操作可参考：
-  [Linux 常用操作及命令](https://cloud.tencent.com/document/product/213/2150) 
- [搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/34064)
- [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/34065)

