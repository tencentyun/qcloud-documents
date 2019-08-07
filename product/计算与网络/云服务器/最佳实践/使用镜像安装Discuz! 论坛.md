## 操作场景
本文档介绍通过在腾讯云云服务器（以下简称 CVM）上安装 Discuz! 镜像来启动并运行一个论坛网站。您将了解如何配置并启动 CVM 云服务器实例，如何获取 Discuz! 用户名和密码，以及如何登录 Discuz! 管理页面。

>! 本文档主要针对基本的 Discuz! 论坛搭建，适用于个人使用或学习。建议针对具有较高可扩展性需求要求不高的业务级网站使用本教程。要获取更高级的教程，请参阅 [手动搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/8043)。
>

## 前提条件

已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤

### 创建云服务器

>! 此步骤针对全新购买云服务器。如果您已购买云服务器实例，可以通过重装系统选择 Discuz! 建站系统。
>
1. 在实例的管理页面，单击【新建】。
2. 根据页面提示选择地域与机型，单击【下一步：选择镜像】。
3. 在“2.选择镜像”页面，单击【镜像市场】，并选择【从镜像市场选择】。如下图所示：
![](https://main.qcloudimg.com/raw/bc90e2119fa15094edd90ea096851efa.png)
4. 在弹出的【选择镜像】对话框中，选择【建站系统】>【Discuz X3.4 论坛系统】，单击【免费使用】。如下图所示：
![](https://main.qcloudimg.com/raw/f9f7252f81bbb0e50b71fa89024c9ba3.png)
更多此镜像详细信息，请参考 [镜像手册](http://www.websoft9.com/xdocs/discuz-image-guide)。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 Discuz! 建站系统的购买。

### 安装并启动 Discuz! 论坛
>? 云服务器实例状态处于运行中时，即可测试 Discuz! 论坛。
>
1. 在实例的管理页面，找到待启动的云服务器实例，并复制该云服务器实例的**公网 IP**。例如，需启动实例的公网 IP 为193.112.145.136，则只需复制该实例的公网 IP 即可。如下图所示：
![](https://main.qcloudimg.com/raw/fd428060759b3dbae9f2b178d865d8ae.png)
2. 将**公网 IP** 粘贴到本地浏览器的地址栏中访问，进入Discuz！安装页面。如下图所示：
![](https://main.qcloudimg.com/raw/c55ce0a0a24ef524c0bf0352b6651feb.png)
3. 单击【我同意】，进入检查安装环境页面。如下图所示：
![安装2](//mc.qcloudimg.com/static/img/c5a521673ed6f1a3528ba67ca5886ee4/image.png)
4. 确认当前状态正常，单击 【下一步】，进入设置运行环境页面。如下图所示：
![安装3](//mc.qcloudimg.com/static/img/11a44bd86bfdfcd1fe3dcce6e8f200e6/image.png)
5. 选择全新安装，单击【下一步】，进入创建数据库页面。如下图所示：
![安装4改](//mc.qcloudimg.com/static/img/5d5184cfb34f98d791c243273b910065/image.png)
6. 根据页面提示，填写信息，为 Discuz! 创建一个数据库。
>! 请使用镜像默认的 MySQL 帐号和密码（默认为 root/123456）连接数据库。并设置好系统信箱、管理员帐号、密码和 Email。
> 请记住自己的管理员帐号和密码。
>
7. 单击【下一步】，开始安装。
6. 安装完成后，单击【您的论坛已完成安装，点此访问】，即可访问论坛。如下图所示：
![安装5](//mc.qcloudimg.com/static/img/41dab1ec86120a565bdd790238f271da/image.png)


