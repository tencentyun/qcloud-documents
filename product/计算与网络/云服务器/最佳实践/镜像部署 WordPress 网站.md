## 操作场景

本文档介绍如何在腾讯云云服务器（以下简称 CVM）上安装 WordPress 镜像来启动并运行一个网站。您将了解如何配置并启动 CVM 实例，如何获取 WordPress 用户名和密码，以及如何登录 WordPress 管理页面。

## 技能要求
腾讯云市场中提供了 WordPress 镜像，如果您不熟悉 Linux 命令的使用，建议您通过镜像部署 WordPress 个人站点。如果您对 Linux 的使用比较熟悉，并且对业务网站有较高的扩展性需求，您也可以 [手动搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/8044)。


## 操作步骤

### 步骤1：创建云服务器时使用 WordPress 镜像

>! 如果您想使用已购买的云服务器部署 WordPress，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您 [手动搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/8044) 或者使用其他地域云服务器进行搭建。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 根据页面提示选择机型，并在 “镜像” 中单击【镜像市场】，选择【从镜像市场选择】。如下图所示：
>! 部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有【镜像市场】，请选择其他支持镜像市场的地域。
>
![](https://main.qcloudimg.com/raw/f65014010e9d40e71b945a189ed574f2.png)
3. 在弹出的【镜像市场】对话框中，选择【建站系统】> 【WordPress博客平台】，单击【免费使用】。如下图所示：
<img src="https://main.qcloudimg.com/raw/6a3645a1e4c5d3a51e6d917eca2a28ec.png" style="width: 88%;"></img>
更多关于此镜像信息，请参见 [WordPress博客平台（CentOS 6.8 64位）](https://market.cloud.tencent.com/products/63)。
4. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 WordPress 建站系统的购买。

### 步骤2：访问获取权限的引导页面
>? 不同的 WordPress 镜像，安装配置 WordPress 的操作步骤略有不同。具体操作请参见腾讯云市场提供的对应 WordPress 镜像商品详情页。
>

1. 在实例的管理页面，找到运行中的云服务器实例，并复制该云服务器实例的**公网 IP**。例如，需启动实例的公网 IP 为193.112.145.136，则只需复制该实例的公网 IP 即可。如下图所示：
![](https://main.qcloudimg.com/raw/3f015e2decf3a89e0fa03a5bf32e13a4.png)
2. 在本地浏览器中访问**公网 IP**，打开【获取权限】引导页面。 如下图所示：
<img src="//mc.qcloudimg.com/static/img/f7ea8180f0c49be0f422e88140bbafee/image.png" style="width: 65%;">

### 步骤3：启动 WordPress 网站
1. 在引导页面中，单击【获取权限】，下载该镜像的相关信息文档到本地。
>! 该文档包含 WordPress 网站的相关重要信息，请注意保存。
2. 打开文档，获取 WordPress 网站的管理员登录账号和密码。如下图所示：
![](https://main.qcloudimg.com/raw/d342c51de533967d41624431c9445033.png)
3. 刷新引导页面，出现 WordPress 的欢迎页面，即表示 WordPress 网站启动成功。
4. 登录管理页面，自定义网站。
 1. 在欢迎页面右下角的【功能】下，单击【登录】。如下图所示：
<img src="//mc.qcloudimg.com/static/img/076e034cc8dcd206c627d8b924aab0bf/image.png" style="width: 88%;">
 2. 输入管理员账号和密码，单击【登录】。
![账号密码登录wp](//mc.qcloudimg.com/static/img/48f8740a24c0602616a5935ab6b6ae64/image.png)
即可根据实际需要对其进行管理、自定义和配置。

## 后续操作
为了提高安全性，通过腾讯云市场提供的 WordPress 镜像搭建 WordPress 个人站点后，建议您登录 WordPress 管理页面，将 WordPress 升级至最新版本。


## 常见问题
如果您在搭建 WordPress 的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
