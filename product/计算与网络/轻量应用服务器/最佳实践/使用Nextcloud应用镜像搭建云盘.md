## 操作场景
Nextcloud 是一款开源免费的云存储网盘软件，其客户端覆盖 Windows、Mac、Android、iOS、Linux 等各种平台，提供网页端以及  WebDAV 接口，您可跨设备跨平台访问您的云盘。同时，Nextcloud 提供多种应用安装，包括但不限于 Markdown 在线编辑、OnlyOffice、思维导图、日历等，您可自行选择安装应用以丰富个人网盘的功能。

Nextcloud 19.0 腾讯云插件版镜像基于 CentOS 7.6 64位操作系统，已预置 Nginx、MariaDB、PHP 软件。同时还集成了腾讯云对象存储（COS）插件，插件使用方法请参见 [腾讯云开源应用插件中心](https://openapp.qq.com/docs/Nextcloud/cos.html)。您可参考本文，使用该镜像快速便捷地搭建一套属于自己或团队共享的云同步网盘，实现跨平台跨设备文件同步、共享、版本控制、团队协作等能力。


## 操作步骤
### 使用 Nextcloud 镜像创建实例
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，在“服务器”页面单击【新建】。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
其中，“镜像”选择为【应用镜像】>【Nextcloud 19.0 腾讯云插件版】，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。

### 安装 Nextcloud
1. 在“服务器”页面中，选择并进入实例详情页。
2. 在实例详情页中，选择【应用管理】页签，进入应用管理详情页。
3. 在“应用内软件信息”栏中获取“首页地址”，并使用浏览器访问，进入 Nextcloud 页面。
4. 在 Nextcloud 页面中，单击【安装完成】。等待片刻即可成功安装 Nextcloud。如下图所示：
![](https://main.qcloudimg.com/raw/9c4a87e7ab935ff5cb3ae392e3bba4be.png)

### 使用 Nextcloud
1. 在实例详情页中，选择【应用管理】页签，进入应用管理详情页。您可以在此页面查看 Nextcloud 应用的各项配置信息。
2. [](id:Step2)在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px">，复制获取 Nextcloud 管理员密码的命令。如下图所示：
![](https://main.qcloudimg.com/raw/d4db12317869c9dc61f795de3a52a0b6.png)
3. 在“应用内软件信息”栏中，单击【登录】。
4. 在弹出的登录窗口中，粘贴并执行 [步骤2](#Step2) 获取的命令，按 **Enter**。
5. [](id:Step5)记录返回结果中的 Nextcloud 管理员名与密码（即 “nextcloud_username” 和 “nextcloud_password” 值）。如下图所示：
![](https://main.qcloudimg.com/raw/894a91340f457a5a2ebd9cc0044f30e7.png)
7. 使用浏览器访问“应用内软件信息”中的“首页地址”，输入 [步骤5](#Step5) 获取的用户名与密码，并单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/2705040ce2e1cd3416ac716f5b7d0a70.png)
登录成功后，即可开始使用共享云同步网盘。

## 相关操作
### 域名与 DNS 解析设置
您可以给自己的 Nextcloud 网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 Nextcloud 实例安装 SSL 证书并开启 HTTPS 访问。
>!Nextcloud 实例无需修改 `/usr/local/lighthouse/softwares/nginx/conf/nginx.conf` 配置文件，仅需修改 `/usr/local/lighthouse/softwares/nginx/conf/include/nextcloud.conf` 配置文件即可。
>
请查阅以下 SSL 相关配置内容，参考注释并按照实际环境进行修改，并添加至 `nextcloud.conf` 文件：
```
server {
    listen 80;
    listen [::]:80;
    server_name cloud.tencent.com; #填写您的证书绑定的域名，例如：cloud.tencent.com
    return 301 https://$server_name:443$request_uri;
}

server {
      listen 443 ssl;
      listen [::]:443 ssl;
      server_name cloud.tencent.com; #填写您的证书绑定的域名，例如：cloud.tencent.com
      ssl_certificate 1_cloud.tencent.com_bundle.crt; #填写您的证书文件名称，例如：1_cloud.tencent.com_bundle.crt
      ssl_certificate_key 2_cloud.tencent.com.key; #填写您的私钥文件名称，例如：2_cloud.tencent.com.key
      ····
}			
```
添加完成后，效果如下图所示：
![](https://main.qcloudimg.com/raw/b6236cb22189a6f3789c304faa3fa6af.png)
