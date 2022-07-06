## 操作场景

WooCommerce 是当前很受欢迎的电商独立站建站工具，具备开源、免费、使用简单且功能强大等特点，您可通过该镜像快速搭建基于 WordPress 的电商独立站。该镜像已预装 WordPress（包含 WooCommerce 插件）、Nginx、MariaDB、PHP 软件。


## 操作步骤

### 使用 WooCommerce 应用镜像创建实例
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，在“服务器”页面单击新建。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
其中，“镜像”选择为**应用镜像** > **WooCommerce 6.5.1**，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
<dx-alert infotype="explain" title="">
- 若您想使用已创建的实例搭建直播间，则可使用 WooCommerce 应用镜像 [重装系统](https://cloud.tencent.com/document/product/1207/44576)。
- 本文以使用应用镜像 WooCommerce 6.5.1 版本为例，镜像可能会进行版本升级与更新，请您以购买页实际版本为准。
</dx-alert>


### 登录网站后台管理页面[](id:login)
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

### 切换为中文版
1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**仪表盘** > **更新**。
3. 进入 “WordPress更新”页面，拉至页面底部，单击**更新翻译**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/31de981a34bf3cc0e8f80c89c22f48e4.png)
4. 待翻译升级成功后，自动进入“更新翻译”页面，单击**转到“WordPress页面”**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ac744dc964ca43c0b5cd05a9a3616e89.png)
5. 待页面刷新后，您即可查看 WooCommerce 已切换为中文版。



### 使用 WordPress 主题
系统已默认安装了 Kadence 和 Astra 主题，您也可以安装并使用其他的 WordPress 主题。您可通过该步骤，了解如何切换、添加、更新 WordPress 主题。

1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**外观** > **主题**。
3. 在“主题”页面中，您可进行以下操作：
<dx-tabs>
::: 添加主题
单击**添加新主题**进入“添加主题”页面后，您可按需单击**安装**，以安装新主题。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4090a23fa9e983b16369e035845ee771.png)
:::
::: 切换主题
在“主题”页面，您可按需单击**启用**主题，以切换主题。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/25ea1494bfad54db3ab78465b67fcd40.png)
:::
</dx-tabs>

本文以默认安装的 Kadence 主题为例，介绍如何使用 Kadence 主题中的独立站模板，使店铺变得更美观。操作步骤如下：
1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**外观** > **主题**，进入“主题”页面后，单击 Kadence 主题。
3. 在 Kadence 主题详情页中，单击 **Kadence**。
4. 选择 **Starter Templates** 页签，并单击 **安装Kadence Starter Templates**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5b43ebf4fc3803d806162b848bf2c570.png)
5. 在页面中选择模板，本文以选择 **Outdoor Shop** 模板为例。单击模板，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ba902b5d415ecbeda9a52a5758187860.png)
6. 在模板编辑页面，按需编辑模板后，选择页面左下角 “IMPORT OPTIONS” 中的 **Single Page** 或 **Full Site**。本文以选择 **Full Site** 为例，即完整站点导入。
7. 在弹出的 “Import Starter Template” 窗口中查阅注意事项，并进行导入。
<dx-alert infotype="notice" title="">
该方式会将您的站点定制器设置、小部件、菜单覆盖。如果您正在测试不同的入门模板，建议启用 “Delete Previously Imported Posts and Images?”。
</dx-alert>
8. 导入成功后页面如下图所示，您的店铺即已使用了该模板，您可单击 **Finished! View your site** 前往店铺首页查看。
![](https://qcloudimg.tencent-cloud.cn/raw/7d158c44d2860a27dbb6301b832653f7.png)




### 域名与 DNS 解析设置
您可以给自己的 WooCommerce 网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 WooCommerce 实例安装 SSL 证书并开启 HTTPS 访问。
