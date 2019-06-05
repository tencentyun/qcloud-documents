## 操作场景

本指南将介绍通过腾讯云云服务器 CVM（以下简称 CVM）上安装的 WordPress 镜像来启动并运行一个网站。您将了解如何配置并启动 CVM 云服务器实例、如何获取 WordPress 用户名和密码，以及如何登录 WordPress 管理页面。

>! 本指南主要针对基本的 WordPress 网站搭建，适用于个人使用或学习，建议对可扩展性需求要求不高的业务级网站使用本教程。如果您比较熟悉命令行操作，并且对业务网站有较高的扩展性需求，请参考 [手动搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/8044)。

## 操作步骤

### 配置并购买云服务器

1. 单击 [购买云服务器](https://buy.cloud.tencent.com/cvm)，进入购买页面。
2. 选择【自定义配置】，根据页面提示选择地域与机型，单击【下一步：选择镜像】。
3. 在“2.选择镜像”页面，单击【镜像市场】，并选择【从镜像市场选择】。如下图所示：
![](https://main.qcloudimg.com/raw/9ba27bcd697702022e6341e10ff0c2bb.png)
4. 在弹出的【选择镜像】对话框中，选择【建站系统】> 【WordPress博客平台】，单击【免费使用】。如下图所示：
![](https://main.qcloudimg.com/raw/3e0965a65bcdc83501d46fc45c4add35.png)
5. 按照页面提示，逐步操作。
关于自定义配置的其他步骤、包括地域、可用区、存储带宽等的选择，您可以参考 [自定义配置Linux云服务器](https://cloud.tencent.com/document/product/213/10517) 或者 [自定义配置Windows云服务器](https://cloud.tencent.com/document/product/213/10516)。

### 启动云服务器实例

>? 云服务器实例状态处于运行中时，即可测试 WordPress 网站。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在云服务器实例的**主 IP 地址**下，复制云服务器实例的**公网 IP**。例如，需启动实例的公网 IP 为119.29.135.128，则只需复制该实例的公网 IP 即可。如下图所示：
![](https://main.qcloudimg.com/raw/83b1a4cb7d0b72aae5542a41d213e21f.png)
3. 将**公网 IP** 粘贴到您本地浏览器的地址栏中访问，即可看到【获取权限】引导页面。 如下图所示：
<img src="//mc.qcloudimg.com/static/img/f7ea8180f0c49be0f422e88140bbafee/image.png" style="width: 65%;">

### 启动 WordPress 网站

1. 在引导页面中，单击【获取权限】，下载该镜像的相关信息文档到本地。
>! 该文档包含 WordPress 网站的相关重要信息，请注意保存。
2. 打开文档，获取 WordPress 网站的管理员登录账号和密码。如下图所示：
<img src="//mc.qcloudimg.com/static/img/bcc8d0f0c96c58050171cf4faf61d940/image.png" style="width: 60%;">
3. 刷新引导页面，出现 WordPress 的欢迎页面，即表示 WordPress 网站启动成功。
4. 登录管理页面，自定义网站。
 1. 在欢迎页面右下角的【功能】下，单击【登录】。如下图所示：
<img src="//mc.qcloudimg.com/static/img/076e034cc8dcd206c627d8b924aab0bf/image.png" style="width: 88%;">
 2. 输入管理员账号和密码，单击【登录】。
![账号密码登录wp](//mc.qcloudimg.com/static/img/48f8740a24c0602616a5935ab6b6ae64/image.png)
即可根据实际需要对其进行管理、自定义和配置。
