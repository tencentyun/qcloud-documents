## 操作场景
本文档介绍通过在腾讯云云服务器（以下简称 CVM）上安装 Discuz! 镜像来启动并运行一个论坛网站。您将了解如何配置并启动 CVM 云服务器实例，如何获取 Discuz! 用户名和密码，以及如何登录 Discuz! 管理页面。


## 技能要求
腾讯云市场中提供了 Discuz! 镜像，如果您不熟悉 Linux 命令的使用，建议您通过镜像部署 Discuz! 论坛。如果您对 Linux 的使用比较熟悉，并且对业务网站有较高的扩展性需求，您也可以 [手动搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/8043)。



## 操作步骤

### 创建云服务器使用 Discuz! 镜像

>! 如果您想使用已购买的云服务器部署 Discuz!，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 根据页面提示选择机型，并在 “镜像” 中单击【镜像市场】，选择【从镜像市场选择】。如下图所示：
![](https://main.qcloudimg.com/raw/3c558a8a9b03162bafe4700dce1591f5.png)
3. 在弹出的【选择镜像】对话框中，选择【建站系统】>【Discuz X3.4 论坛系统】，单击【免费使用】。如下图所示：
![](https://main.qcloudimg.com/raw/f9f7252f81bbb0e50b71fa89024c9ba3.png)
更多此镜像详细信息，请参考 [镜像手册](http://www.websoft9.com/xdocs/discuz-image-guide)。
4. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 Discuz! 建站系统的购买。

### 安装并启动 Discuz! 论坛
1. 在实例的管理页面，找到运行中的云服务器实例，并复制该云服务器实例的**公网 IP**。例如，需启动实例的公网 IP 为193.112.145.136，则只需复制该实例的公网 IP 即可。如下图所示：
![](https://main.qcloudimg.com/raw/3f015e2decf3a89e0fa03a5bf32e13a4.png)
2. 在本地浏览器中访问**公网 IP**，进入Discuz！安装页面。如下图所示：
![](https://main.qcloudimg.com/raw/74cc99cb3aa75cb9f1d99b6d7feced72.png)
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


## 常见问题
如果您在搭建 Discuz! 论坛的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。

