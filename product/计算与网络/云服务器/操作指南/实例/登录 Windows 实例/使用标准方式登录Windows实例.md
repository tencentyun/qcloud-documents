## 操作场景
WebRDP 作为腾讯云推荐登录您 Windows 云服务器的标准登录方式，本文介绍如何通过该方式登录 Windows 实例。

## 适用本地操作系统
Windows，Linux 和 Mac OS 都可以使用 WebRDP 方式登录云服务器。

## 前提条件[](id:Prerequisites)

- 已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买公网 IP，且该实例已在关联安全组中开通来源为 WebRDP 代理 IP 的远程登录端口（默认为3389）。WebRDP 代理 IP 网段如下：
	- 81.69.102.0/24
	- 106.55.203.0/24
	- 101.33.121.0/24
	- 101.32.250.0/24

## 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择需要登录的 Windows 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/52dc409778da5f8c6ae87bc1907a7cf4.png)
3. 在弹出的“登录Windows实例”窗口中，选择“标准登录方式”中的【立即登录】。如下图所示：
![](https://main.qcloudimg.com/raw/cc68bf46b47c5c314671b639287baef8.png)
4. 在新建页面的“登录Windows实例”窗口中，根据实际情况填写登录信息。如下图所示：
![](https://main.qcloudimg.com/raw/43a0df38e10d76e0cca1a86b68f79d97.png)
 - **端口**：默认为3389，可请按需填写。
 - **用户名**：Windows 实例用户名默认为 `Administrator`，可请按需填写。
 - **登录密码**：填写已从 [前提条件](#Prerequisites) 步骤中获取的登录密码。
5. 单击【登录】即可登录 Windows 实例。登录成功则出现类似如下图所示界面：
>?本文以登录操作系统为 Windows Server 2016 数据中心版64位中文版的云服务器为例，其他版本 Windows 系统界面可能与下图有一定区别。
>
![](https://main.qcloudimg.com/raw/a68deed91b8d73db1e6b2f931c6689c1.png)
