## 操作场景
Discuz! Q 是全球成熟度最高、覆盖率最大的社区论坛软件系统之一。腾讯云轻量应用服务器提供 Discuz! Q 应用镜像，其中已集成宝塔 Linux 面板、MySQL、Nginx 和 PHP 软件，您可以使用它构建移动端社区。
>?
>- Discuz! Q 应用镜像底层基于 CentOS 7.6 64位操作系统。
>- 轻量应用服务器实例创建完成后，将会自动下载并安装最新版的 Discuz! Q 软件。您无需进行 Discuz! Q 初始化等安装操作，可参考文档步骤，获取管理员帐号及密码并进行登录。

## 说明事项
- CentOS 系统在安装了宝塔面板后，会默认开启操作系统防火墙（可通过命令行 `systemctl status firewalld.service` 查看）。若您需访问指定端口（例如8080端口），则需通过配置轻量应用服务器网络防火墙及操作系统防火墙放通指定端口。具体操作请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577) 及 [配置操作系统防火墙](#updatePort)。
- 为提高宝塔面板安全性，建议将面板默认的8888端口修改为其他端口，您可以登录面板后进行修改。修改后需在轻量应用服务器网络防火墙中放通对应端口，详情请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577) 。

## 操作步骤
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。
2. 单击【新建】，进入轻量应用服务器购买页面。如下图所示：
![](https://main.qcloudimg.com/raw/06f26e8e88c53d5cd5cb6f772364b7e7.png)
	- **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
	- **镜像**：选择 “Discuz! Q v1.0” 应用镜像。
	- **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、峰值带宽、每月流量），选择一种实例套餐。
	- **实例名称**：自定义实例名称，若不填则默认使用“镜像名称+四位随机字符”。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
	- **购买时长**：默认1个月。
	- **购买数量**：默认1台。
3. 单击【立即购买】，并根据页面提示提交订单完成支付，返回轻量应用服务器控制台。
4. 待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。
您可以在此页面查看 Discuz! Q 应用的各项配置信息。
5. 选择【应用管理】页签，进入应用管理详情页。
6. [](id:Step6)在“应用内软件信息”栏中，单击<img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png">，复制获取 Discuz! Q 的管理员帐户密码的命令。
7. 在“应用内软件信息”栏中，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/f98e022191f1fcb49698fa2db2f519ff.png)
8. [](id:Step8)在弹出的登录窗口中，粘贴 [步骤6](#Step6) 复制的管理员密码，按 **Enter**。
如下图所示即可获取 Discuz! Q 管理员账号（admin）和对应的密码，请妥善保管并记录。
![](https://main.qcloudimg.com/raw/b0e81edfcb7da408504343dc98622556.png)
9. 关闭登录窗口，并返回该实例的应用管理详情页。
10. 在“应用内软件信息”栏中，单击 Discuz! Q 的【后台访问地址】。如下图所示：
![](https://main.qcloudimg.com/raw/bd7302b9dd9f100dbab7a2d87aa41345.png)
11. 在新打开的浏览器窗口中，输入 [步骤8](#Step8) 记录的账号和密码，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/01192dbc6dd0522e873c5c93241f17af.png)
即可根据实际需要，对 Discuz! Q 进行管理、自定义和配置。

## 相关操作
### 修改管理员账号密码
您可参考以下步骤，修改 Discuz! Q 管理员账号（admin）的密码：
1. 在“应用内软件信息”栏中，单击 Discuz! Q 的【前台访问地址】。
2. 在新打开的浏览器窗口中，选择底部菜单栏中的<img src="https://main.qcloudimg.com/raw/30f96457f5daeed05440989ab41e9405.png" style="margin:-3px 0">。
3. 进入 Discuz! Q 登录页面，输入 [步骤8](#Step8) 记录的账号和密码，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/1be6cea0343be72db7bc5f663c9852c8.png)
4. 成功登录后，选择底部菜单栏中的<img src="https://main.qcloudimg.com/raw/30f96457f5daeed05440989ab41e9405.png" style="margin:-3px 0">，进入个人信息页面。
5. 在个人信息页面中，选择【我的资料】并单击密码所在行右侧的【修改>】。如下图所示：
![](https://main.qcloudimg.com/raw/e0ba02f7810264e29f5d9900b2332f98.png)
6. 在修改密码界面设置新密码后单击【提交】即可完成密码修改。


### 查看其他配置信息
在 Discuz! Q 实例的应用管理详情页，您除了可以查看 Discuz! Q 的配置信息，还可以查看其他配置信息。例如宝塔Linux面板登录信息、 MySQL 数据库管理员密码、实例中各个软件的安装路径等。如下图所示：
![](https://main.qcloudimg.com/raw/46dfb1a9fdbbc8191e697744b8a04103.png)

### 配置操作系统防火墙[](id:updatePort)
Discuz! Q 应用镜像集成了宝塔 Linux 面板，可通过宝塔面板直接放通操作系统防火墙端口。步骤如下：
1.  登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。
2.  在“服务器”页面，选择实例进入实例详情页面。
3.  在“应用那软件信息”中获取宝塔 Linux 面板相关信息，配置并登录宝塔 Linux 面板。
4.  在宝塔 Linux 面板中，选择左侧【安全】。
5. 在“系统安全”页面的“防火墙”中，填写需放行端口号及说明。如下图所示：
![](https://main.qcloudimg.com/raw/866b18637a5587cd09b0919e16aa5f0d.png)
6. 单击【放行】即可放通对应端口。

### 域名与 DNS 解析设置
您可以给自己的 Discuz! Q 论坛设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
您可通过以下方式，为您的实例安装 SSL 证书：
- 方式1：Discuz! Q 实例创建完成后，使用实例中内置的宝塔 Linux 面板安装 SSL 证书。详情可参考宝塔 Linux 面板官方文档。
- 方式2：可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 Discuz! Q 实例安装 SSL 证书并开启 HTTPS 访问。
