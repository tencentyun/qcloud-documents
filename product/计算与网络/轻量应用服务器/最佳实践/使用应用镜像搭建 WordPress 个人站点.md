## 操作场景

WordPress 是全球最流行的开源的博客和内容管理网站的建站平台，具备使用简单、功能强大、灵活可扩展的特点，提供丰富的主题插件。腾讯云轻量应用服务器提供 WordPress 应用镜像，您可以使用它快速搭建博客、企业官网、电商、论坛等各类网站。


<dx-alert infotype="explain" title="">
 本文档示例 WordPress 应用镜像底层基于 CentOS 7.6 64位操作系统。应用镜像会进行不定期更新，请以购买页面实际镜像信息为准。
</dx-alert>


## 说明事项
- CentOS 系统在安装了宝塔面板后，会默认开启操作系统防火墙（可通过命令行 `systemctl status firewalld.service` 查看）。若您需访问指定端口（例如8080端口），则需通过配置轻量应用服务器网络防火墙及操作系统防火墙放通指定端口。具体操作请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577) 及 [配置操作系统防火墙](#updatePort)。
- 为提高宝塔面板安全性，建议将面板默认的8888端口修改为其他端口，您可以登录面板后进行修改。修改后需在轻量应用服务器网络防火墙中放通对应端口，详情请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577) 。

## 操作步骤

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在 **服务器** 页面单击新建。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
  - **镜像**：选择为应用模板 > 网站场景 > WordPress 应用模板，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
<dx-alert infotype="explain" title="">
- 应用模板即应用镜像。
- 查看镜像说明详情请参见 [基本概念](https://cloud.tencent.com/document/product/1207/79254)。
</dx-alert>
 - **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
 - **可用区**：默认勾选“随机分配”，也可自行选择可用区。
 - **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、峰值带宽、每月流量），选择一种实例套餐。
 - **实例名称**：自定义实例名称，若不填则默认使用“镜像名称+四位随机字符”。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
 - **购买时长**：默认1个月。
 - **购买数量**：默认1台。
3. 单击**立即购买**，并根据页面提示提交订单完成支付。
4. 返回轻量应用服务器控制台。
5. 待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。
您可以在此页面查看 WordPress 应用的各项配置信息。
6. 选择**应用管理**页签，进入应用管理详情页。
7. [](id:step7)在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin: 0;"></img>，复制获取 WordPress 管理员帐号及密码的命令。
8. 在“应用内软件信息”栏中，单击**登录**，或页面右上角的**登录**。
![](https://qcloudimg.tencent-cloud.cn/raw/76d3579a9c94bb133c02e299f87273f5.png)
9. 在弹出的登录窗口中，粘贴在 [步骤7](#step7) 中获取的命令，并按 **Enter**。
即可获取 WordPress 管理员帐号（admin）和对应的密码。
![](https://main.qcloudimg.com/raw/2b3a5ac10481b8d63111769fb7f85f4a.png)
10. [](id:step10)复制并记录 WordPress 管理员帐号和密码。
11. 关闭登录窗口，并返回该实例的应用管理详情页。
12. 在“应用内软件信息”栏中，单击 WordPress 的**管理员登录地址**。
![](https://qcloudimg.tencent-cloud.cn/raw/8b86418ed50ad7daf31205b9ddffca51.png)
13. 在新打开的浏览器窗口中，输入 [步骤10](#step10) 记录的账号和密码，单击**登录**。
![](https://main.qcloudimg.com/raw/3fc36b90b8c5022d5a46ac6b718e30db.png)
<dx-alert infotype="explain" title="">
应用镜像 Wordpress 5.7.1 版本需进行管理邮件确认及数据库更新确认，请查阅页面信息并依次单击**此地址正确**及**升级Wordpress数据库**即可。
</dx-alert>
成功登录后，您可根据实际需要对 WordPress 进行管理、自定义和配置。



## 相关操作
### 更新 WordPress 管理员个人资料

1. 在 WordPress 管理界面的左侧导航中，选择**用户** > **所有用户**。
2. 找到 `admin` 用户，单击**编辑**。
3. 根据实际需求，设置个人资料。
例如：
 - 在“联系信息”栏中，输入您的电子邮件地址。
 - 在“账户管理”栏中，单击**设置新密码**，输入新的管理员密码。
5. 单击**更新个人资料**。

### 查看其他配置信息

在 WordPress 实例的应用管理详情页，您除了可以查看 WordPress 的配置信息，还可以查看其他配置信息。例如首页地址、 Nginx 主配置文件保存路径、 MariaDB 数据库管理员密码、实例中各个软件的安装路径等。
![](https://qcloudimg.tencent-cloud.cn/raw/362bf61b6807c72b6dd35045006aa0b4.png)


### 配置操作系统防火墙[](id:updatePort)
WordPress 应用镜像集成了宝塔 Linux 面板，可通过宝塔面板直接放通操作系统防火墙端口。步骤如下：
1.  登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。
2.  在“服务器”页面，选择实例进入实例详情页面。
3.  选择**应用管理**页签，在“应用内软件信息”中获取宝塔 Linux 面板相关信息。如下图所示：
![](https://main.qcloudimg.com/raw/7a46224ff8fd6d73098ffd552cc8e9fa.png)
3.  配置并登录宝塔 Linux 面板。
4.  在宝塔 Linux 面板中，选择左侧菜单栏中的**安全**。
5. 在“系统安全”页面的“防火墙”中，填写需放行端口号及说明。如下图所示：
![](https://main.qcloudimg.com/raw/866b18637a5587cd09b0919e16aa5f0d.png)
6. 单击**放行**即可放通对应端口。


### 设置 WordPress 地址 URL

<dx-alert infotype="notice" title="">
请参考以下步骤，设置 WordPress 地址 URL。若您未配置 WordPress 地址 URL，则发送修改管理员邮箱邮件时会出现链接无法点击的问题。
</dx-alert>


1. 选择左侧导航栏中的**设置** > **常规**，进入“常规选项”页面。
2. 找到 “WordPress地址（URL）”并填写。建议填写店铺的域名，若暂未拥有域名，可先填写实例的 IP 地址，格式如下：
```shell
http://实例公网 IP/
```
您可登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，获取实例公网 IP。
3. 单击页面底部的**保存更改**，配置即可生效。

### 配置邮件
WordPress 应用镜像 postfix 服务默认未加密。从安全性的角度考虑，建议您参考以下步骤配置加密的邮件服务。本文以使用 WordPress 插件 “WP Mail SMTP” 配置 QQ 邮箱 SMTP 服务为例：

1. 参考 [登录网站后台管理页面](#login) 步骤1 -  步骤7，登录管理页面。
2. 选择左侧导航栏中的**插件** > **安装插件**。
3. 进入“添加插件”页面后，在搜索框中输入 “WP Mail SMTP”，找到插件后单击**现在安装**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/50524db152025c536fce5dff88731b5e.png)
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





### 域名与 DNS 解析设置
您可以给自己的 WordPress 网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 WordPress 实例安装 SSL 证书并开启 HTTPS 访问。
 
  
