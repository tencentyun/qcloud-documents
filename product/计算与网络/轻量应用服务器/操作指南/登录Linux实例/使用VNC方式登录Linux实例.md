## 操作场景
VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接实例的方式。在没有安装或者无法使用远程登录客户端，以及通过其他方式均无法登录的情况下，用户可以通过 VNC 登录连接到实例，观察实例状态，并进行基本的管理操作。

## 使用限制
- VNC 暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- VNC 登录实例时，需要使用主流浏览器，例如 Chrome，Firefox，IE 10及以上版本等。
- VNC 登录为独享终端，即同一时间只有一个用户可以使用 VNC 登录。

## 前提条件
已获取远程登录 Linux 实例需要使用实例的管理员帐号和对应的密码。

<dx-alert infotype="notice" title="">
在使用 VNC 方式登录 Linux 实例之前，如果您未设置需要登录的用户名的密码，请先完成设置密码操作，具体方法请参考 [重置密码](https://cloud.tencent.com/document/product/1207/44575)。
</dx-alert>


## 操作步骤
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 在服务器列表中找到需登录的实例，进入实例详情页。
3. 选择**远程登录**，单击 “VNC登录”栏中的**登录**。如下图所示：
![](https://main.qcloudimg.com/raw/461aa630721c5ede4c49bb29d477e2e2.png)
4. 在弹出的对话框中，在 “login” 后输入用户名，按 **Enter**。
5. 在 “Password” 后输入密码，按 **Enter**。
输入的密码默认不显示，如下图所示：
![](https://main.qcloudimg.com/raw/6469e226220c9160839b2809e16325f2.png)
登录完成后，命令提示符左侧将显示当前登录实例的信息。
>?您可通过单击界面左上角的**发送远程命令**，选择直接发送下拉列表中的命令。
