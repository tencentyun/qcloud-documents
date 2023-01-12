## 操作场景

WooCommerce 是当前很受欢迎的电商独立站建站工具，具备开源、免费、使用简单且功能强大等特点，您可通过该镜像快速搭建基于 WordPress 的电商独立站。该镜像已预装 WordPress（包含 WooCommerce 插件）、Nginx、MariaDB、PHP 软件。


您可参考以下视频或文档，使用轻量应用服务器快速搭建电商独立站。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/3645-62993?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>


## 操作步骤

### 使用 WooCommerce 应用镜像创建实例
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在 **服务器** 页面单击 **新建**。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
 - **镜像**：选择为应用模板 > 电商场景 > WooCommerce 应用模板，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
<dx-alert infotype="explain" title="">
- 应用模板即应用镜像。
- 查看镜像说明详情请参见 [基本概念](https://cloud.tencent.com/document/product/1207/79254)。
</dx-alert>
<dx-alert infotype="explain" title="">
- 若您想使用已创建的实例搭建直播间，则可使用 WooCommerce 应用镜像 [重装系统](https://cloud.tencent.com/document/product/1207/44576)。
- 本文以使用应用镜像 WooCommerce 6.8.2 版本为例，镜像可能会进行版本升级与更新，请您以购买页实际版本为准。
</dx-alert>

### 登录网站后台管理页面[](id:login)
1. 在实例详情页面，选择**应用管理**页签，进入应用管理详情页。
2. [](id:Step2)在“应用内软件信息”中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin-bottom:-3px 0px">，复制获取管理员帐号及密码的命令。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0474aed37f4bbb4f760a1d1ab6aafeeb.png)
3. 在“应用内软件信息”中，单击**登录**，或页面右上角的**登录**。
4. [](id:Step4)在弹出的登录窗口中，粘贴在 [步骤2](#Step2) 中获取的命令，并按 **Enter**。
即可获取管理员帐号（admin）和对应的密码（wordpress_password）。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/24a91d82cb71b14dff4db24ed0be8aa0.png)
5. 记录管理员帐号和密码，关闭登录窗口，并返回该实例的应用管理详情页。
6. 在“应用内软件信息”中，单击“管理员登录地址”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8df37cd14409531f4678f597e2223b09.png)
7. 在新打开的浏览器窗口中，输入 [步骤4](#Step4) 记录的账号和密码，单击**登录**。
8. 选择左侧导航中的 **WooCommerce** > **Home**，进入如下图所示页面，您即可开始配置自己的电商独立站。
![](https://qcloudimg.tencent-cloud.cn/raw/c3f958d021128402006e770d6c646252.png)
您可参考 [WooCommerce](https://woocommerce.com/documentation/plugins/woocommerce/getting-started/) 文档，了解更多关于  WooCommerce 的入门信息。



### 快速运营 WooCommerce 独立站
您可参考以下步骤，进行 WooCommerce 独立站基本配置，快速开始进行产品销售。


#### 配置独立站详细信息
1. 在后台管理页面中，选择左侧导航栏中的 **WooCommerce**。
2. 在设置向导页面中，按需依次填写或选择信息、行业、产品信息、业务详情及主题。步骤如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/aa73bc1f096468ee347d6b3e2b2be43c.png)
其中，在设置主题步骤中，您可选择 WooCommerce 应用镜像已安装的 Kadence 或 Astra 主题，也可选择其他安装其他心仪的主题。


#### 设置 WordPress 地址 URL
请参考以下步骤，设置 WordPress 地址 URL。若您未配置 WordPress 地址 URL，否则可能发生页面无法正常跳转、收到邮件链接无法点击等问题。
1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**设置**，进入“常规选项”页面。
2. 找到 “WordPress地址（URL）”并填写。建议填写店铺的域名，若暂未拥有域名，可先填写实例的 IP 地址，格式如下：
```shell
http://实例公网 IP/
```
<dx-alert infotype="explain" title="">
您可登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，获取实例公网 IP。
</dx-alert>
3. 单击页面底部的**保存更改**，配置即可生效。


#### 添加产品
WooCommerce 提供了使用模板添加、手动添加、导入 CSV 表格文件以及独立站迁移四种添加产品的方式。本文以使用模板添加为例进行产品添加，具体步骤如下：

1. 在后台管理页面中，选择左侧导航栏中的 **WooCommerce**。
2. 单击“添加要销售的产品”中的**添加产品**，进入“添加我的产品”页面。
3. 选择**从模板入手**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9a73bf43d862d2db8c842ee618f5bc9b.png)
3. 在弹出的“从模板入手”窗口中，选择“实体产品”后，单击**确定**。
4. 在“编辑产品”页面中，按需设置产品名称、产品描述、产品类型、产品价格、产品图片及产品标签等产品信息。
5. 设置完成后单击**发布**，即可上架产品。


#### 设置付款方式
1. 在后台管理页面中，选择左侧导航栏中的 **WooCommerce**。
2. 单击“添加收款方式”中的**查看选项**，进入“设置付款方式”页面。
3. 根据实际需求选择在线或线下付款，并按照页面提示完成设置。


#### 设置税率
1. 在后台管理页面中，选择左侧导航栏中的 **WooCommerce**。
2. 单击“添加税率”中的**是的，请**，进入“设置税率”页面，根据实际需求并按照页面提示启用及设置税率工具。



#### 添加销售渠道
1. 在后台管理页面中，选择左侧导航栏中的 **WooCommerce**。
3. 单击“提升销售额”中的**添加销售渠道**，根据实际需求，并按照页面提示选择推荐的营销扩展程序。


#### 个性化我的商店
1. 在后台管理页面中，选择左侧导航栏中的 **WooCommerce**。
3. 单击“让您的商店脱颖而出”中的**个性化**，进入“个性化我的商店”页面。
3. 您可一个客户主页，并且能够上传独立站 Logo 和公告信息。若暂时无此方面需求，则请单击**跳过**。


#### 访客设置
1. 在后台管理页面中，选择左侧导航栏中的 **WooCommerce** > **设置**。
2. 在“设置”页面中，选择**帐户和隐私**页签，并按需设置“访客结账”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/055a64f8476e015ef203ba533979b736.png)
3. 拉至页面底部，单击**保存更改**即生效。


## 相关操作

### 设置语言[](id:setLan)
您可根据以下步骤，分别设置站点语言、后台语言及 WooCommerce 插件语言。

<dx-tabs>
::: 设置站点语言
通过该步骤设置，您的网站后台页面及访客页面都将显示为设定的语言。

1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**设置**，进入“常规选项”页面。
3. 找到“站点语言”，并按需选择页面语言。本文以选择“简体中文”为例，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ad82471b3fa89b3c788d0db21ab5fcac.png)
4. 拉至页面底部，单击**保存更改**即生效。
<dx-alert infotype="explain" title="">
此时，您的网站后台页面及访客页面都将显示为“简体中文”。若您的网站面向境外，则请将站点语言设置为英语后，参考 [设置后台语言](#backstage) 将后台页面设置为中文。
</dx-alert>

:::
::: 设置后台语言[](id:backstage)


通过该步骤设置，您可指定登录者使用的后台语言。

1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**用户**，进入所有用户列表页面。
3. 选择您需设置用户名下的**编辑**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d1d724edba875dd458b1c0c1e56ba1cd.png)
4. 在用户个人资料页面，找到“语言”，设置该用户登录后台管理页面时使用的语言。
本文以“简体中文”为例，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/71b0a0b40c5c5493c0f0b47320d32e25.png)
5. 拉至页面底部，单击**更新个人资料**即生效。

<dx-alert infotype="explain" title="">
此时，指定用户的网站后台页面语言为“简体中文”，访客页面语言为“英文”。您可参考 [设置 WooCommerce 插件语言](#wooLan)，将插件语言设置为中文。
</dx-alert>


:::
::: 设置 WooCommerce 插件语言[](id:wooLan)


通过该步骤设置，您可将 WooCommerce 插件语言设置为“简体中文”。

1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**仪表盘** > **更新**。
3. 进入 “WordPress更新”页面，拉至页面底部，单击**更新翻译**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/31de981a34bf3cc0e8f80c89c22f48e4.png)
4. 待翻译升级成功后，自动进入“更新翻译”页面，单击**转到“WordPress页面”**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ac744dc964ca43c0b5cd05a9a3616e89.png)
5. 待页面刷新后，您即可查看 WooCommerce 已切换为中文版。



:::
</dx-tabs>



### 管理 WordPress 主题

<dx-accordion>
::: 主题基本操作
系统已默认安装了可免费使用的 Kadence 和 Astra 主题，您也可以安装并使用其他的 WordPress 主题。您可通过该步骤，了解如何切换、添加、更新 WordPress 主题。

1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**外观** > **主题**。
3. 在“主题”页面中，您可进行以下操作：
 - **添加主题**：单击**添加新主题**进入“添加主题”页面后，您可按需单击**安装**，以安装新主题。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/4090a23fa9e983b16369e035845ee771.png)
  - **切换主题**：在“主题”页面，您可按需单击**启用**主题，以切换主题。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/25ea1494bfad54db3ab78465b67fcd40.png)
  - **设置主题自动更新**：在“主题”页面，单击您需设置的主题，进入主题详情页面。
本文以默认安装的 Kadence 主题为例，在主题详情页面中，您可单击**启用自动更新**，以启用主题自动更新。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/193078c182aeceb339511d3dcb083faf.png)

:::
::: 使用主题模板

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



:::
::: 上传主题
若您具备 zip 压缩包格式的主题文件，可参考该步骤上传并使用。

1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**外观** > **主题**，进入“主题”页面后，单击**安装主题**。
3. 在“添加主题”页面中，单击**上传主题**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/188735b7ec52b3ca32d73281e6d8711b.png)
4. 在打开的上传界面中，单击**选择文件**，选择上传主题压缩包。
5. 在“主题”页面中，找到已上传的主题，单击**启用**即可使用。


:::
</dx-accordion>



### 配置邮件
WooCommerce 应用镜像考虑到安全性问题，默认未开启 postfix 服务。若您需开启邮件服务，可参考以下步骤进行配置。本文以使用 WordPress 插件 “WP Mail SMTP” 配置 QQ 邮箱 SMTP 服务为例：

1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**插件**，进入“插件”页面后，单击**安装插件**。
3. 在搜索框中输入 “WP Mail SMTP”，找到插件后单击**立即安装**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f9f52997cc77552b51f7edcd16baf302.png)
4. 安装成功后单击**启用**，并在插件配置页面单击 **Let's Get Started**。
6. 在 “Choose Your SMTP Mailer” 步骤中，选择您需配置的邮箱。本文以配置 QQ 邮箱 SMTP 为例，选择**其他 SMTP**后单击 **Save and Continue**。
7. 在 “Configure Mailer Settings” 步骤中，参考以下信息配置 SMTP 主机、加密方式、端口及认证信息后，单击 **Save and Continue**。
主要参数信息如下，其他配置请保持默认。
 - **SMTP 主机**：填写 `smtp.qq.com`。
 - **加密**：选择 “SSL”。
 - **SMTP 端口**：填写 `465`。
 - **SMTP 用户名**：填写您的邮箱地址。
 - **SMTP 密码**：填写授权码，不是 QQ 邮箱的密码。
 - **发件人名称**：可填写您的店铺名称。
 - **发件人**：可填写管理员的邮件地址。需为有效的邮件地址，否则会报错。
8. 在 “Which email features do you want to enable?” 步骤中，保持默认配置，单击 **Save and Continue**。
9. 在 “Help Improve WP Mail SMTP + Smart Recommendations” 步骤中，单击 **Skip this Step**。
10. 在 “Enter your WP Mail SMTP License Key” 步骤中，单击 **Skip this Step**。
至此，您已完成邮件基本配置。




### 设置域名与 DNS 解析
您可以给自己的 WooCommerce 网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。


### 开启 HTTPS 访问
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 WooCommerce 实例安装 SSL 证书并开启 HTTPS 访问。
