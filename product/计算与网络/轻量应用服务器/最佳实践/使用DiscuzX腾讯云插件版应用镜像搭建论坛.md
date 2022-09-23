## 操作场景
Discuz! X 是一款流行的社区论坛软件，具有性能优异、功能全面、安全稳定等特点。该镜像基于 CentOS 7.6 64位操作系统，已预置 Nginx、MariaDB、PHP 软件，同时 Discuz! X 软件中已集成腾讯云验证码、对象存储、图片内容安全、文本内容安全、云点播和短信等插件。

通过集成的插件，您可更方便的对腾讯云产品进行管理和操作。本文指导您如何在轻量应用服务器上安装和使用 Discuz! X 3.4 腾讯云插件版。

## 操作步骤

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，在“服务器”页面单击【新建】。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
其中，“镜像”选择为【应用镜像】>【Discuz! X 3.4 腾讯云插件版】，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
3. 待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。
您可以在此页面查看 Discuz! X 3.4 腾讯云插件版应用的各项配置信息。
4. 选择【应用管理】页签，进入应用管理详情页。
5. [](id:Step5)在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px">，复制获取管理员帐户密码的命令。
6. 在“应用内软件信息”栏中，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/b428fabc49a946eafc0ef6dfe798cc43.png)
7. [](id:Step7)在弹出的登录窗口中，粘贴 [步骤5](#Step5) 复制的命令，按 **Enter**。
如下图所示即可获取管理员账号（admin）和对应的密码，请妥善保管并记录。
![](https://main.qcloudimg.com/raw/b1c1b575b601aade7f224761264e046b.png)
8. 关闭登录窗口，并返回该实例的应用管理详情页。
9. 在“应用内软件信息”栏中，单击“管理员登录地址”。如下图所示：
![](https://main.qcloudimg.com/raw/642b3db57f5aff8626f6a0ba0fe56f8f.png)
10. 在新打开的浏览器窗口中，输入 [步骤7](#Step7) 记录的账号和密码，单击【提交】。如下图所示：
![](https://main.qcloudimg.com/raw/ad865820334b847cb06583f4a09a8e7f.png)
即可根据实际需要，对 Discuz! X 3.4 腾讯云插件版进行管理、自定义和配置。

## 相关操作

### 域名与 DNS 解析设置
您可以给自己的 Discuz! X 论坛设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 Discuz! X 实例安装 SSL 证书并开启 HTTPS 访问。


### 配置 URL 静态化
>?当您因业务需求在 SEO 设置中开启 URL 静态化后，还需根据以下步骤登录实例完成配置，否则可能会出现无法进入模块的问题。
>
1. 在实例详情页面的“应用内软件信息”栏中，单击“管理员登录地址”。
2. 在新打开的浏览器窗口中，输入 [步骤7](#Step7) 记录的账号和密码，单击【提交】完成登录。
3. 选择页面上方【全局】，并单击左侧的【SEO设置】。
4. 在“SEO设置”页面中，单击【查看当前的 Rewrite 规则】。如下图所示：
 ![](https://main.qcloudimg.com/raw/ca62e515bbbd9e535df6fc51c65c7d31.png)
5. [](id:Step5)在 Rewrite 规则详情页中，查看并记录 Nginx Web Server。如下图所示：
![](https://main.qcloudimg.com/raw/08524623c6a4b29a9f3b14718603630f.png)
6. 登录实例，详情请参见 [使用 WebShell 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)。
7. 执行以下命令，使用 vim 打开配置文件。
```
sudo vim /usr/local/lighthouse/softwares/nginx/conf/include/discuzx.conf
```
8. 按 **i** 进入编辑模式，将 [步骤5](#Step5) 中获取的配置，输入至 `location / {...}` 中。
9. 按 **Esc**，输入 **:wq**，保存文件并返回。
10. 执行以下命令，重启 Nginx。
```
sudo /usr/local/lighthouse/softwares/nginx/sbin/nginx -s reload
```
至此已完成配置，您可登录首页地址进行访问模块操作。

