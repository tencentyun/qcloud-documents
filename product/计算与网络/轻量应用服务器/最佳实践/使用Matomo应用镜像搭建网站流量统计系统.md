## 操作场景

Matomo 是一款开源的网站数据统计软件，可以用于跟踪、分析您的网站的流量，同时充分保障数据安全性、隐私性。该镜像基于 CentOS 7.6 64位操作系统，已预置 Nginx、MariaDB、PHP 软件。本文介绍如何使用 Matomo 快速搭建您的网站流量统计系统。


## 操作步骤

### 使用 Matomo 应用镜像创建实例
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在 **服务器** 页面单击 **新建**。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
 - **镜像**：选择为应用模板 > 网站场景 > Matomo 应用模板，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
<dx-alert infotype="explain" title="">
- 应用模板即应用镜像。
- 查看镜像说明详情请参见 [基本概念](https://cloud.tencent.com/document/product/1207/79254)。
</dx-alert>
<dx-alert infotype="explain" title="">
- 若您想使用已创建的实例搭建直播间，则可使用 Matomo 应用镜像 [重装系统](https://cloud.tencent.com/document/product/1207/44576)。
- 本文以使用应用镜像 Matomo 4.9.1 版本为例，镜像可能会进行版本升级与更新，请您以购买页实际版本为准。
</dx-alert>

### 获取 MariaDB 管理员信息[](id:mariadb)
1. 在实例详情页面，选择**应用管理**页签，进入应用管理详情页。
2. 在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px;">，复制获取 MariaDB 管理员密码的命令。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8dc5603d321b06fc9ff615dac03faed4.png)
3. 在“应用内软件信息”栏中，单击**登录**，或页面右上角的**登录**，以登录实例。
4. 在弹出的登录窗口中，粘贴上一步骤中已获取的命令，并按 **Enter**。
即可获取 MariaDB 管理员帐号和对应的密码，请妥善保存。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e943364da463b4ed211311016f9c2e5d.png)



### Matomo 初始化设置
1. 在实例详情页面，选择**应用管理**页签，进入应用管理详情页。
2. 在“应用内软件信息”中，单击“访问地址”，进入 Matomo 初始化设置页面。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8d82e7133cce3adb3f52979ebb2ecf65.png)
3. 在 Matomo 欢迎页面中，单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a5bf66778d086d6decc45a5edba1b791.png)
4. 在“系统检查”步骤中，您可查看、下载系统检查信息，确认无误后，下拉至页面底部并单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/af1a7684d877a7075f19e054747a8cd3.png)
<dx-alert infotype="explain" title="">
 - “强制 SSL 连接”检查项提示信息可忽略，若后续您有需求，可参考 [开启 HTTPS 访问](#httpsConfig) 进行配置。
- “ fpm-fcgi” 及 “nginx/1.20.2” 推荐项提示信息可忽略。
除以上提示信息外，若您的实例有其他检查项未通过，则需自行排查。
</dx-alert>
5. 在“数据库设置”步骤中，输入 [获取 MariaDB 管理员信息](#mariadb) 步骤已获取的 MariaDB 管理员帐号及密码，并输入自定义数据库名称（本文以 matomo 为例）后，单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/90a5a4515639deb83ab68c557994b781.png)
6. 在“建立数据表中”步骤中，查看数据库及表已创建成功，单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/04a8691f9b6f237cf271b70bd277da6b.png)
7. [](id:Step7)在“超级用户”步骤中，自定义 Matomo 超级用户名、密码及电子邮箱（本文超级用户名以 admin 为例），其他参数可按需设置，并单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e274ed7b79112a9e6510d98c4146687a.png)
8. 在“设置网站”步骤中，填写需跟踪的网站信息、时区等信息，并单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/827dc1bf3a19736e2860c3e1ea2fab7a.png)
9. 在 “JavaScript 跟踪代码” 步骤中，查看信息，并单击**下一步**。
10. 进入完成安装页面，单击**继续使用 MATOMO**。



### 使用 Matomo 进行站点统计
1. 在 Matomo 登录页面，输入 [步骤7](#Step7) 设置的超级用户名及密码，单击**登录**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9493fd13213181a0bd8bee8444425712.png)
2. 登录成功后，可查看跟踪代码信息。请复制如下图所示中的跟踪代码：
<img src="https://qcloudimg.tencent-cloud.cn/raw/15a7dd0851ff0a032baf458c135f067b.png" width="80%"/>
3. 将已获取的跟踪代码粘贴至网站的相关版块。本文以跟踪 WordPress 网站为例，您可通过以下两种方式编辑跟踪代码。
<dx-tabs>
::: 登录实例编辑代码
 1. 参考 [使用 WebShell 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录 Matomo 实例。
 2. 执行以下命令，编辑 WordPress 主题 header.php 文件。其中，`<主题名称>` 需替换为您实际使用的主题名称。
```text
sudo vi /usr/local/lighthouse/softwares/wordpress/wp-content/themes/<主题名称>/header.php
```
3. 按 **i** 进入编辑模式，在 `</header><!-- #site-header -->` 上方，输入已获取的跟踪代码内容。编辑完成后如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c6509fec7fb154924ac7e8f80ba6edb2.png)
4. 按 **Esc**，输入 **:wq** 保存编辑并退出编辑器。
:::
::: 登录博客后台管理页面编辑代码
1. 登录 WordPress 后台管理页面，选择左侧导航栏中的**外观** > **主题编辑器**。
2. 在“编辑主题”页面，选择 **主题页眉 header.php** 文件，并在 `</header><!-- #site-header -->` 上方输入已获取的跟踪代码内容。编辑完成后如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ad20aa5957a67ac3d880e0d96f2375c1.png)
3. 单击**更新文件**保存编辑。


:::
</dx-tabs>
4. 返回 Matomo 页面，选择页面上方的**所有网站**，即可查看到已统计到的数据信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9dac0fc06f89a64da00988908da0058c.png)
您可单击网站名，在详情页面查看访问客户端访问时间、地点、访问页面记录、终端操作系统和浏览器等信息。若您需添加新的站点，请单击页面中的**增加一个新网站**后，重复参考本步骤进行设置。





## 相关操作


### 域名与 DNS 解析设置
您可以给自己的 Matomo 网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。
5. 参考 [使用 WebShell 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录 Matomo 实例。
6. 执行以下命令，编辑配置文件。
```text
sudo vi /usr/local/lighthouse/softwares/matomo/config/config.ini.php
```
7. 按 **i** 进入编辑模式，将 `trusted_hosts[]="实例 IP 地址"` 中的 IP 地址替换为已解析的域名。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bdf9b10ae68e26c81c70c318d0faaf68.png) 
8. 按 **Esc** 输入 **:wq** 保存编辑并退出编辑器。
至此，您可使用域名访问您的 Matomo 网站。


### 开启 HTTPS 访问[](id:httpsConfig)
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 Matomo 实例安装 SSL 证书并开启 HTTPS 访问。您也可参考 [Nginx 官方 HTTPS 配置介绍](https://nginx.org/en/docs/http/configuring_https_servers.html)，以了解更多配置信息。
