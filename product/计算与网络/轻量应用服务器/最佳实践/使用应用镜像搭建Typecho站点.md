## 操作场景
Typecho 是开源的博客建站平台，具有轻量、高效、稳定等特点，操作界面简洁友好。该镜像基于 CentOS 7.6 64 位操作系统，并已预置 Nginx、PHP、MariaDB 软件。您可以使用它快速搭建博客、企业官网、电商、论坛等各类网站。

## 操作步骤
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，并单击【新建】。
2. 在轻量应用服务器购买页面，参考以下信息购买实例：
	- **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
	- **镜像**：选择 “Typecho 1.1.0” 应用镜像。
	- **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、峰值带宽、每月流量），选择一种实例套餐。
	- **实例名称**：自定义实例名称，若不填则默认使用所选镜像名称。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
	- **购买时长**：默认1个月。
	- **购买数量**：默认1台。
3. 单击【立即购买】，并根据页面提示提交订单完成支付。
4. 返回轻量应用服务器控制台，待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。
您可以在此页面查看 Typecho 应用的各项配置信息。
5. 选择【应用管理】页签，进入应用管理详情页。
6. [](id:Step6)在“应用内软件信息”栏中，单击<img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px">，复制获取 Typecho 管理员帐号及密码的命令。
7. 在“应用内软件信息”栏中，单击【登录】。如下图所示：
<dx-alert infotype="explain" title="">
在应用管理详情页中，除了可以查看 Typecho 的配置信息，还可以查看其他配置信息。例如首页地址、 Nginx 主配置文件保存路径、 MariaDB 数据库管理员密码、实例中各个软件的安装路径等。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/6a1e42a54eb6999ad2522d023f838761.png"/>
8. [](id:Step8)在弹出的登录窗口中，粘贴在 [步骤6](#Step6) 中获取的命令，并按 **Enter**。
即可获取 Typecho 管理员帐号（admin ）和对应的密码。
9. 在“应用内软件信息”栏中，单击 Typecho 的【管理员登录地址】。如下图所示：
![](https://main.qcloudimg.com/raw/a6e715e38b41b628317b7ac5649325f0.png)
10. 在新打开的浏览器窗口中，输入 [步骤8](#Step8) 记录的帐号和密码，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/b6b9a13700780ee4b4039a3166260795.png)
成功登录后，您可根据实际需要对 Typecho 进行管理、自定义和配置。

## 相关操作
### 域名与 DNS 解析设置
您可以给自己的 Typecho 网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 Typecho 实例安装 SSL 证书并开启 HTTPS 访问。
