## 操作场景
本文档介绍通过在腾讯云云服务器（以下简称 CVM）上安装 Discuz! 镜像来启动并运行一个论坛网站。您将了解如何配置并启动 CVM 云服务器实例，如何获取 Discuz! 用户名和密码，以及如何登录 Discuz! 管理页面。


## 技能要求
腾讯云市场中提供了 Discuz! 镜像，如果您不熟悉 Linux 命令的使用，建议您通过镜像部署 Discuz! 论坛。如果您对 Linux 的使用比较熟悉，并且对业务网站有较高的扩展性需求，您也可以 [手动搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/8043)。


## 操作步骤

### 步骤1：创建云服务器使用 Discuz! 镜像



<dx-alert infotype="notice" title="">
如果您想使用已购买的云服务器部署 Discuz!，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您 [手动搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/8043) 或者使用其他地域云服务器进行搭建。
</dx-alert>


1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的**新建**。
2. 根据页面提示选择机型，并在 “镜像” 中单击**镜像市场**，选择**从镜像市场选择**。如下图所示：
<dx-alert infotype="notice" title="">
 部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有**镜像市场**，请选择其他支持镜像市场的地域。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/3c558a8a9b03162bafe4700dce1591f5.png"/>
3. 在弹出的**镜像市场**对话框中，选择**建站系统** >  **Discuz! X3.2论坛系统**，单击**免费使用**。
<dx-alert infotype="explain" title="">
单击镜像名可查看镜像详情。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/32d0a64b6fb0aba038dcc2602291bab9.png" style="width: 88%"></img>
4. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的创建。

### 步骤2：安装并启动 Discuz! 论坛
1. 在实例的管理页面，找到运行中的云服务器实例，并复制该云服务器实例的**公网 IP**。如下图所示：
例如，需启动实例的公网 IP 为193.112.145.136，则只需复制该实例的公网 IP 即可。
![](https://main.qcloudimg.com/raw/3f015e2decf3a89e0fa03a5bf32e13a4.png)
2. 在本地浏览器中访问**公网 IP**，进入Discuz！安装页面。如下图所示：
![](https://main.qcloudimg.com/raw/268160dd3f095f9fad788f332b7b877b.png)
3. 单击**我同意**。
4. 在检查安装环境页面，确认当前状态正常，单击**下一步**。如下图所示：
![安装2](https://main.qcloudimg.com/raw/824c95544d61b9971a7f17911fcee721.png)
5. 在设置运行环境页面，选择全新安装，单击**下一步**。如下图所示：
![安装3](https://main.qcloudimg.com/raw/b314e56fc96eb23520ecb06064196988.png)
6. 在创建数据库页面，根据页面提示和实际需求，填写相关信息。如下图所示：
<dx-alert infotype="notice" title="">
- 请记录或保存本页面的数据库信息及管理员信息。
- 数据库信息建议保持镜像的默认设置，如需修改或管理数据库信息，以及了解更多相关镜像的详细信息，请前往 [云市场](https://market.cloud.tencent.com/categories/1076?tagName=Discuz)。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/450c91a57148fa5fa8027c729a3e43bd.png"/>
7. 单击**下一步**，开始安装。
8. 安装完成后，单击**您的论坛已完成安装，点此访问**，即可访问论坛。如下图所示：
![安装5](//mc.qcloudimg.com/static/img/41dab1ec86120a565bdd790238f271da/image.png)


## 常见问题
如果您在搭建 Discuz! 论坛的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。

