## 操作场景

WooCommerce 是当前最受欢迎的电商独立站建站工具，具备开源、免费、使用简单且功能强大等特点，您可通过该镜像快速搭建基于 WordPress 的电商独立站。该镜像已预装 WordPress（包含WooCommerce插件）、Nginx、MariaDB、PHP 软件。


## 操作步骤

### 使用 WooCommerce 应用镜像创建实例
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，在“服务器”页面单击新建。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
其中，“镜像”选择为**应用镜像** > **WooCommerce 6.5.1**，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
<dx-alert infotype="explain" title="">
- 若您想使用已创建的实例搭建直播间，则可使用 WooCommerce 应用镜像 [重装系统](https://cloud.tencent.com/document/product/1207/44576)。
- 本文以使用应用镜像 WooCommerce 6.5.1 版本为例，镜像可能会进行版本升级与更新，请您以购买页实际版本为准。
</dx-alert>


### 登录网站后台管理页面
1. 在实例详情页面，选择**应用管理**页签，进入应用管理详情页。
2. [](id:Step2)在“应用内软件信息”中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin-bottom:-3px 0px">，复制获取管理员帐号及密码的命令。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/49964533bf999981244387c28bc214f0.png)
3. 在“应用内软件信息”中，单击**登录**，或页面右上角的**登录**。
4. [](id:Step4)在弹出的登录窗口中，粘贴在 [步骤2](#Step2) 中获取的命令，并按 **Enter**。
即可获取管理员帐号（admin）和对应的密码（wordpress_password）。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/24a91d82cb71b14dff4db24ed0be8aa0.png)
5. 记录管理员帐号和密码，关闭登录窗口，并返回该实例的应用管理详情页。
6. 在“应用内软件信息”中，单击“管理员登录地址”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1c2f4974706c282cf4edc71d0cba24f3.png)
7. 在新打开的浏览器窗口中，输入 [步骤4](#Step4) 记录的账号和密码，单击**登录**。
8. 选择左侧导航中的 **WooCommerce** > **Home**，进入如下图所示页面，您即可开始配置自己的独立电商站。
![](https://qcloudimg.tencent-cloud.cn/raw/c3f958d021128402006e770d6c646252.png)
您可参考 [WooCommerce](https://woocommerce.com/documentation/plugins/woocommerce/getting-started/) 文档，了解更多关于  WooCommerce 的入门信息。


## 相关操作

### 域名与 DNS 解析设置
您可以给自己的 WooCommerce 网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 WooCommerce 实例安装 SSL 证书并开启 HTTPS 访问。
