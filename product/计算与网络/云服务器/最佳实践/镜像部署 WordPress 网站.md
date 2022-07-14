## 操作场景

本文档介绍如何在腾讯云云服务器（以下简称 CVM）上安装 WordPress 镜像来启动并运行一个网站。您将了解如何配置并启动 CVM 实例，如何获取 WordPress 用户名和密码，以及如何登录 WordPress 管理页面。

## 技能要求
腾讯云市场中提供了 WordPress 镜像，如果您不熟悉 Linux 命令的使用，建议您通过镜像部署 WordPress 个人站点。如果您对 Linux 的使用比较熟悉，并且对业务网站有较高的扩展性需求，您也可以 [手动搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/8044)。


## 操作步骤

### 步骤1：创建云服务器时使用 WordPress 镜像

<dx-alert infotype="notice" title="">
如果您想使用已购买的云服务器部署 WordPress，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您 [手动搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/8044) 或者使用其他地域云服务器进行搭建。
</dx-alert>

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的**新建**。
2. 根据页面提示选择机型，并在 “镜像” 中单击**镜像市场**，选择**从镜像市场选择**。如下图所示：
<dx-alert infotype="notice" title="">
部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有**镜像市场**，请选择其他支持镜像市场的地域。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/f65014010e9d40e71b945a189ed574f2.png">
3. 在弹出的“镜像市场”对话框中，选择**建站系统**，输入 **wordpress** 并单击 <img src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px">。
4. 按需选择镜像，本文以选择 **Wordpress 建站系统** 为例，单击**免费使用**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c0c39a1f915315b1572fdd2d3e3f6a65.png)
更多关于此镜像信息，请参见 <a href="https://market.cloud.tencent.com/products/1794">WordPress博客平台（Wordpress 建站系统 CentOS7.6 | LAMP）</a>。
5. 在实例关联的安全组需添加放通80端口的入站规则，详情请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。
存储介质、带宽等其他配置请根据实际需求选择，最终选择购买完成 WordPress 建站系统。


### 步骤2：安装 WordPress 网站
<dx-alert infotype="explain" title="">
不同的 WordPress 镜像，安装配置 WordPress 的操作步骤略有不同。具体操作请参见腾讯云市场提供的对应 WordPress 镜像商品详情页。
</dx-alert>

1. 在实例的管理页面，找到运行中的云服务器实例，并复制该云服务器实例的**公网 IP**。例如，需启动实例的公网 IP 为193.112.145.136，则只需复制该实例的公网 IP 即可。如下图所示：
![](https://main.qcloudimg.com/raw/3f015e2decf3a89e0fa03a5bf32e13a4.png)
2. 在本地浏览器中访问**公网 IP**，开始安装 WordPress 网站。
  1. 选择 Wordpress 语言后，单击 **Continue**。 
  2. 在页面中按需输入 WordPress 站点标题、管理员用户名、管理员密码及电子邮件。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fdf0c8fa2cc7cc70e9f4ffdbcc2a6f49.png)
  3. 单击**安装WordPress**，在页面中查看到安装成功提示即表示已完成安装。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2a8a31a4ad60aa71228fcc4c5c2982c5.png)
3. 单击**登录**。
4. 输入已设置的用户及密码后，单击登录。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/99f0e29b4b15a7cf96a9ba76091e216b.png)
5. 选择**升级WordPress数据库**，并单击**继续**。
出现如下页面，表明已成功安装 WordPress 网站。即可根据实际需要对其进行管理、自定义和配置。
![](https://qcloudimg.tencent-cloud.cn/raw/3416ee4cb8e41fae393b948f1472f536.png)


## 后续操作
为了提高安全性，通过腾讯云市场提供的 WordPress 镜像搭建 WordPress 个人站点后，建议您登录 WordPress 管理页面，将 WordPress 升级至最新版本。


## 常见问题
如果您在搭建 WordPress 的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
