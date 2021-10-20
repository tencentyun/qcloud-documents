## 操作场景
Typecho 是开源的博客建站平台，具有轻量、高效、稳定等特点，操作界面简洁友好。该镜像基于 CentOS 7.6 64 位操作系统，并已预置 Nginx、PHP、MariaDB 软件。您可以使用它快速搭建博客、企业官网、电商、论坛等各类网站。

## 操作步骤
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，在“服务器”页面单击**新建**。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
其中，“镜像”选择为**应用镜像** > **Typecho 1.1.0**，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
3. 返回轻量应用服务器控制台，待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。
您可以在此页面查看 Typecho 应用的各项配置信息。
4. 选择**应用管理**页签，进入应用管理详情页。
5. [](id:Step5)在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px">，复制获取 Typecho 管理员帐号及密码的命令。
6. 在“应用内软件信息”栏中，单击**登录**。如下图所示：
<dx-alert infotype="explain" title="">
在应用管理详情页中，除了可以查看 Typecho 的配置信息，还可以查看其他配置信息。例如首页地址、 Nginx 主配置文件保存路径、 MariaDB 数据库管理员密码、实例中各个软件的安装路径等。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/6a1e42a54eb6999ad2522d023f838761.png"/>
7. [](id:Step7)在弹出的登录窗口中，粘贴在 [步骤5](#Step5) 中获取的命令，并按 **Enter**。
即可获取 Typecho 管理员帐号（admin ）和对应的密码。
8. 在“应用内软件信息”栏中，单击 Typecho 的**管理员登录地址**。如下图所示：
![](https://main.qcloudimg.com/raw/a6e715e38b41b628317b7ac5649325f0.png)
9. 在新打开的浏览器窗口中，输入 [步骤7](#Step7) 记录的帐号和密码，单击**登录**。如下图所示：
![](https://main.qcloudimg.com/raw/b6b9a13700780ee4b4039a3166260795.png)
成功登录后，您可根据实际需要对 Typecho 进行管理、自定义和配置。

## 相关操作

### 登录 MariaDB 数据库
1. 在实例的详情页中，选择**应用管理**页签。
2. [](id:Step2)在应用管理详情页的“应用内软件信息”栏中，选择 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px">，复制获取 MariaDB 管理员帐号及密码的命令。
3. 单击**登录**。如下图所示：
![](https://main.qcloudimg.com/raw/ec988d321e6cac648014f840712139f2.png)
4. [](id:Step4)在弹出的登录窗口中，执行在 [步骤2](#Step2) 中获取的命令。获取并记录 MariaDB 管理员密码。
5. 选择以下方式，登录 MariaDB 数据库。
 - 方式1（推荐）：直接执行以下命令，登录 MariaDB 数据库。
 ```
mysql -u root -h 127.0.0.1 -p
```
 - 方式2：关闭 Systemd 安全 Tmp 功能，步骤如下：
    1. 将 `/usr/lib/systemd/system/mariadb.service` 中的 `PrivateTmp` 值修改为 `false`。
    2. 依次执行以下命令，使配置生效。
   ```
	 systemctl daemon-reload
	 ```
	 ```
	 systemctl restart mariadb
	 ```
	 3. 执行以下命令，登录 MariaDB 数据库。
   ```
	 mysql -u root -p
	 ```
6. 在弹出的登录窗口中，粘贴在 [步骤4](#Step4) 中获取的 MariaDB 管理员密码（密码默认不显示），并按 **Enter**。
返回结果如下图所示，表示已成功登录 MariaDB。
![](https://main.qcloudimg.com/raw/e70612aea8d9b7cc5ac5af653b5e7aae.png)


### 域名与 DNS 解析设置
您可以给自己的 Typecho 网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 Typecho 实例安装 SSL 证书并开启 HTTPS 访问。
