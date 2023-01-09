## 操作场景
本文介绍如何使用标准登录方式（WebRDP）登录 Windows 实例。 

<dx-alert infotype="explain" title="">
该方式不区分本地机器操作系统，支持通过控制台直接登录 Windows 实例。
</dx-alert>


## 前提条件[](id:preconditions)
已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
- 如已设置登录密码，则请使用该密码登录。如忘记密码，则请 [重置实例密码](https://cloud.tencent.com/document/product/1207/44575)。
- 如在创建实例时选择系统随机生成密码，则请往 [站内信](https://console.cloud.tencent.com/message) 获取初始密码。


## 操作步骤
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 在服务器列表中找到对应的实例，并根据实际的操作习惯选择不同的方式进行登录。
 - 在服务器列表中的实例卡片上，单击**登录**。
![](https://qcloudimg.tencent-cloud.cn/raw/861cc6329d3f3ec63e00035d8c261074.png)
 - 单击实例卡片进入服务器详情页，单击“远程登录”中“WebRDP登录”下的**登录**，或页面右上角的**登录**。
![](https://qcloudimg.tencent-cloud.cn/raw/f76f7194cea0c460411e4ca9419da61a.png)
 - 使用 [应用镜像](https://cloud.tencent.com/document/product/1207/79254#appOS) 创建的 Windows 实例，可在实例详情页选择“应用管理”，单击页面右上角的**登录**。
![](https://qcloudimg.tencent-cloud.cn/raw/4d378ad53d556881185ebbcae7bc8268.png)
3. 在打开的“标准登录 | Windows 实例”窗口中，根据实际情况填写登录信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/59662e3028fa633e7d1ce2effa354b82.png)
 - **端口**：默认为3389，请按需填写。
 - **用户名**：Windows 实例用户名默认为 Administrator，请按需填写。
 - **密码**：填写已从 [前提条件](#preconditions) 步骤中获取的登录密码。
4. 单击登录，即可登录 Windows 实例。
本文以登录操作系统为 Windows Server 2019 数据中心版64位中文版的轻量应用服务器为例，登录成功则出现如下图所示界面：
![](https://qcloudimg.tencent-cloud.cn/raw/60522f6b8a24ecfce350fff866527235.png)

## 相关操作
- 成功登录后，您可参考 [最佳实践](https://cloud.tencent.com/document/product/1207/45116) 及 [第三方教程](https://cloud.tencent.com/document/product/1207/58793)，进行搭建中小型网站、Web 应用、博客、论坛、小程序/小游戏、电商、云盘/图床、云端开发测试和学习环境等轻量级、低负载且访问量适中的应用。
- 如登录过程中遇到问题，您可使用自助检测工具。如需进一步了解自助检测工具，请参见 [使用实例自助检测](https://cloud.tencent.com/document/product/1207/74704)。
