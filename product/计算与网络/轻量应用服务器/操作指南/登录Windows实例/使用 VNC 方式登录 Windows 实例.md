
## 操作场景
VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接实例的方式。在没有安装或者无法使用远程桌面连接工具，以及通过其他方式均无法登录的情况下，用户可以通过 VNC 登录到实例，观察实例状态，并进行基本的管理操作。

## 使用限制

- VNC 暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- VNC 登录实例时，需要使用主流浏览器，例如 Chrome，Firefox，IE 10及以上版本等。
- VNC 登录为独享终端，即同一时间只有一个用户可以使用 VNC 登录。

## 前提条件

已获取远程登录 Windows 实例需要使用实例的管理员帐号（Administrator）和对应的密码。 
- 如在创建实例时设置登录密码，则请使用该密码登录。如忘记密码，则请 [重置密码](https://cloud.tencent.com/document/product/1207/44575) 。
- 如在创建实例时选择系统随机生成密码，则请往 [站内信](https://console.cloud.tencent.com/message) 获取初始密码。
 
## 操作步骤

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 在服务器列表中找到对应的实例，并根据实际的操作习惯选择不同的方式进行登录。
 - 在服务器列表中的实例卡片上，单击【登录】。
![](https://main.qcloudimg.com/raw/fac5bd2895a3717cd2d516ba57fcaf5e.png)
 - 进入服务器详情页，选择【概要】页签，单击“远程登录”中的【登录】。
![](https://main.qcloudimg.com/raw/53dc1f62ce0b358cc20b2bcf3c44ac23.png)
成功登录后，您可参考 [最佳实践](https://cloud.tencent.com/document/product/1207/45116) 及 [第三方教程](https://cloud.tencent.com/document/product/1207/58793)，进行搭建中小型网站、Web 应用、博客、论坛、小程序/小游戏、电商、云盘/图床、云端开发测试和学习环境等轻量级、低负载且访问量适中的应用。


