## 操作场景
WebShell 为腾讯云推荐的登录方式，您可以直接使用腾讯云 WebShell 工具一键登录 Linux 实例。其优点如下：
- 支持复制、粘贴。
- 支持鼠标滚屏。
- 支持中文输入法。

>? 创建 Linux 操作系统的轻量应用服务器时，该服务器默认绑定1个密钥。此密钥对应的用户名为 `lighthouse`，具备 root 权限。
> 当您使用 WebShell 工具登录 Linux 实例时，系统默认使用此密钥（对应的用户名为 `lighthouse`）进行登录。
>

## 适用本地操作系统
Window，Linux 或者 Mac OS

## 前提条件

在登录前，请确认实例的防火墙已放行22端口（创建实例时默认已开通22端口）。

## 操作步骤

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 在服务器列表中找到对应的实例，并根据实际的操作习惯选择不同的方式进行登录。
 - 在服务器列表中的实例卡片上，单击**登录**。
![](https://main.qcloudimg.com/raw/ad83b4066ea56c22ca1593a6ab808ff0.png)
 - 单击实例卡片进入服务器详情页，单击“远程登录”中的**登录**。
![](https://main.qcloudimg.com/raw/c87f1ecca7eb821f0f74b9c718025e00.png)
 - 使用 [应用镜像](https://cloud.tencent.com/document/product/1207/44361#appOS) 创建的实例，可在实例详情页选择**应用管理**，单击“应用内软件信息”中的**登录**。
![](https://main.qcloudimg.com/raw/c18295d4ac3b40aee2b6b9f2bb11217c.png)
成功登录后，您可参考 [最佳实践](https://cloud.tencent.com/document/product/1207/45116) 及 [第三方教程](https://cloud.tencent.com/document/product/1207/58793)，进行搭建中小型网站、Web 应用、博客、论坛、小程序/小游戏、电商、云盘/图床、云端开发测试和学习环境等轻量级、低负载且访问量适中的应用。

## 相关操作
### 关闭或开启 WebShell 一键登录
>?服务器创建成功后，默认开启 WebShell 一键登录功能，您可参考以下步骤进行关闭或再次开启 WebShell 一键登录功能。
>
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 在服务器列表中找到对应的实例，进入服务器详情页。
3. 在“远程登录”的“一键登录”中，按需选择**开启**或**关闭** WebShell 一键登录：
 - **关闭**：当无需使用一键登录时，可选择关闭此功能。
>!
>- 关闭一键登录后，并不会影响您使用本地 SSH 客户端远程登录实例，您也可以选择再次开启一键登录功能。
>- 关闭一键登录操作并不会在实例操作系统中同步删除系统默认密钥的公钥（默认保存在操作系统的 lighthouse 用户下）。您可以自行删除公钥，但删除将会导致再次开启一键登录功能无效。
>
 - **开启**：开启一键登录后，您可以基于系统默认密钥实现浏览器 WebShell 一键登录实例。
>!请确认系统默认私钥的公钥（默认保存在操作系统的 lighthouse 用户下）未被删除，否则开启后仍无法正常一键登录。
>
 
