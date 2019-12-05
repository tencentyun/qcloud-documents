## 操作场景

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装或者无法使用远程登录客户端，以及通过其他方式均无法登录的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。

## 使用限制

- VNC 登录的云服务器暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- VNC 登录云服务器时，需要使用主流浏览器，例如 Chrome，Firefox，IE 10及以上版本等。
- VNC 登录为独享终端，即同一时间只有一个用户可以使用 VNC 登录。

## 适用本地操作系统

Windows，Linux 和 Mac OS

## 前提条件

已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
- Windows 实例的管理员帐号统一为 **Administrator**。
- 如果您在购买实例时选择**自动生成密码**，则可登录 [腾讯云控制台](https://console.cloud.tencent.com/)，单击右上角的 <img src="https://main.qcloudimg.com/raw/60e7d0de182a973d69fb82b69d01f52a.png" style="margin: 0;"></img>，进入“【腾讯云】请查收您新购买的云服务器”页面，查看初始密码。
- 如果您在购买实例时选择**自定义密码**，则登录密码为您在购买云服务器实例时指定的密码。
- 如果您忘记登录云服务器的密码，请参考 [重置实例密码](https://cloud.tencent.com/document/product/213/16566) 进行重置。


## 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 。
2. 在实例列表中，选择需要登录的 Windows 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/96689027b98d8fc6bfb00036de7a87f8.png)
3. 在弹出的 “登录Windows实例” 窗口中，选择【其他方式（VNC）】，单击【立即登录】。如下图所示：
![](https://main.qcloudimg.com/raw/bdfe5b286e7e0c388adfbc12d15cfad6.png)
4. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 **Ctrl-Alt-Delete** 进入系统登录界面。如下图所示：
![](https://main.qcloudimg.com/raw/2dec43fa6ddb5e442da59c75f7a34b0f.png)



