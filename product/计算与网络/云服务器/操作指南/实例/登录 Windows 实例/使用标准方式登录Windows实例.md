## 操作场景
本文介绍如何使用标准登录方式（WebRDP）登录 Windows 实例。 
>?该方式不区分本地机器操作系统，支持通过控制台直接登录 Windows 实例。
>

## 前提条件[](id:Prerequisites)

- 已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
 - 如已设置登录密码，则请使用该密码登录。如忘记密码，则请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
 - 如在创建实例时选择系统随机生成密码，则请往 [站内信](https://console.cloud.tencent.com/message) 获取初始密码。
- 您的云服务器实例已购买公网 IP，且已在实例关联的安全组中放通来源为 WebRDP 代理 IP 的远程登录端口（默认为3389）。
 - 如通过快速配置购买云服务器，则默认已开通。
 - 如通过自定义配置购买云服务器，则可参考 [允许 RDP 远程连接 Windows 云服务器](https://cloud.tencent.com/document/product/213/34601#.E5.9C.BA.E6.99.AF.E4.BA.8C.EF.BC.9A.E5.85.81.E8.AE.B8-rdp-.E8.BF.9C.E7.A8.8B.E8.BF.9E.E6.8E.A5-windows-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8) 手动放通。


## 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择需要登录的 Windows 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/52dc409778da5f8c6ae87bc1907a7cf4.png)
3. 在弹出的“登录Windows实例”窗口中，选择“标准登录方式”中的【立即登录】。如下图所示：
![](https://main.qcloudimg.com/raw/cc68bf46b47c5c314671b639287baef8.png)
4. 在新建页面的“登录Windows实例”窗口中，根据实际情况填写登录信息。如下图所示：
![](https://main.qcloudimg.com/raw/43a0df38e10d76e0cca1a86b68f79d97.png)
 - **端口**：默认为3389，请按需填写。
 - **用户名**：Windows 实例用户名默认为 `Administrator`，请按需填写。
 - **登录密码**：填写已从 [前提条件](#Prerequisites) 步骤中获取的登录密码。
5. 单击【登录】即可登录 Windows 实例。
本文以登录操作系统为 Windows Server 2016 数据中心版64位中文版的云服务器为例，登录成功则出现类似如下图所示界面：
![](https://main.qcloudimg.com/raw/a68deed91b8d73db1e6b2f931c6689c1.png)
