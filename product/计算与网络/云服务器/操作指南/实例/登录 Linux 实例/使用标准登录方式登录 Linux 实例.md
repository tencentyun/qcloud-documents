## 操作场景

WebShell 为腾讯云推荐的登录方式。无论您的本地系统为 Windows，Linux 或者 Mac OS，只要实例购买了公网 IP，都可以通过 WebShell 登录。本文介绍如何使用标准登录方式（WebShell）登录 Linux 实例。
WebShell 优点如下：
- 支持快捷键复制粘贴。
- 支持鼠标滚屏。
- 支持中文输入法。
- 安全性高，每次登录需要输入密码或密钥。

## 适用本地操作系统

Window，Linux 或者 Mac OS

## 鉴权方式

**密码**或**密钥**

## 前提条件

- 已获取登录实例的管理员帐号及密码（或密钥）。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买公网 IP，且该实例已开通云服务器实例的22号端口（对于通过快速配置购买的云服务器实例已默认开通）。

## 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择需要登录的 Linux 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/3106cebfdeae7762d656ffc68732e130.png)
3. 在弹出的【登录Linux实例】窗口，选择【标准登录方式】，单击【立即登录】。如下图所示：
![](https://main.qcloudimg.com/raw/75e9c0a87910d6ad7d517668f4e82459.png)
4. 在打开的 WebShell 登录页面，根据实际需求，选择【密码登录】或者【密钥登录】方式进行登录。如下图所示：
![](https://main.qcloudimg.com/raw/22e2e003bf407076596f615c4b92ff53.png)
如果登录成功，WebShell 界面会出现 Socket connection established 提示。如下图所示：
![](https://main.qcloudimg.com/raw/a810f534d55fb5609e3323efc23689d0.png)

## 后续操作

当您成功登录云服务器后，您可以在腾讯云服务器上搭建个人站点，论坛或者使用其他操作。相关操作可参考：
- [搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/34064)
- [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/34065)

