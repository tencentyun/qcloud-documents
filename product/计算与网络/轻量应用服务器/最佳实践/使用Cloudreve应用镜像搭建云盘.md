## 操作场景
Cloudreve 是一款开源的网盘软件，支持服务器本机及腾讯云对象存储 COS 等多种存储方式，提供离线下载、拖拽上传、在线预览等功能，能够帮助您快速搭建个人使用或多人共享的云盘系统。该镜像基于 CentOS 8.2 64位操作系统，已集成宝塔 Linux 面板，并已预置 Nginx、Aria2、MariaDB 软件。

本文介绍如何使用 Cloudreve 应用镜像搭建 Cloudreve 云盘，实现文件上传、分享及离线下载功能。同时，还介绍了如何通过镜像中已集成的宝塔 Linux 面板，轻松管理您的轻量云服务器。

## 说明事项
- CentOS 系统在安装了宝塔面板后，会默认开启操作系统防火墙（可通过命令行 `systemctl status firewalld.service` 查看）。若您需访问指定端口（例如8080端口），则需通过配置轻量应用服务器网络防火墙及操作系统防火墙放通指定端口。具体操作请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577) 及 [配置操作系统防火墙](#updatePort)。
- 为提高宝塔面板安全性，建议将面板默认的8888端口修改为其他端口，您可以登录面板后进行修改。修改后需在轻量应用服务器网络防火墙中放通对应端口，详情请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577) 。


## 操作步骤

### 使用 Cloudreve 镜像创建实例
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，在“服务器”页面单击【新建】。
2. 在轻量应用服务器购买页面，选择所需配置完成轻量应用服务器购买。
其中，“镜像”选择为【应用镜像】>【Cloudreve 3.3.1】，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。
>?
>- 若实例所在地域为中国内地，则建议选择更适合搭建云盘的存储型套餐。详情请参见 [基础套餐](https://cloud.tencent.com/document/product/1207/44368#basis)。
>- 本文以使用应用镜像 Cloudreve 3.3.1 为例，镜像可能会进行版本升级与更新，请您以购买页实际版本为准。
>

### 使用 Cloudreve

#### 登录 Cloudreve 页面
1. 在实例详情页中，选择【应用管理】页签，进入应用管理详情页。您可以在此页面查看 Cloudreve 应用的各项配置信息。
2. [](id:Step2)在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px">，复制获取 Cloudreve 管理员密码的命令。如下图所示：
![](https://main.qcloudimg.com/raw/88232ca1358b79f4b512c8d55ba14fb9.png)
3. 在“应用内软件信息”栏中，单击【登录】。
4. 在弹出的登录窗口中，粘贴并执行 [步骤2](#Step2) 获取的命令，按 **Enter**。
5. [](id:Step5)记录返回结果中的 Cloudreve 管理员名与密码（即 “cloudreve_username” 和 “cloudreve_password” 值）。如下图所示：
![](https://main.qcloudimg.com/raw/34b600733c567907d203f2db974726fe.png)
6. 使用浏览器访问“应用内软件信息”中的“首页地址”，输入 [步骤5](#Step5) 获取的用户名与密码，并单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/1da6c4e5cc65e2beaff5e7624f10bb6a.png)

#### 上传文件至 Cloudreve
在 Cloudreve 页面中，您可直接将本地文件拖拽至指定区域，或单击右键选择上传文件/目录，进行文件上传。如下图所示：
<img src="https://main.qcloudimg.com/raw/b08872d6ebfc8eb34b7198845202c781.png" width="90%"/>

#### 分享文件
 Cloudreve 支持将文件或文件夹的下载链接分享给您的好友，还可针对该下载链接设置密码保护或过期时间。步骤如下：
1. 在 Cloudreve 页面中，右键单击需分享的文件，并在弹出菜单中选择【创建分享链接】。
2. 在弹出的“创建分享链接”窗口中，按需进行设置，并单击【创建分享链接】。如下图所示：
![](https://main.qcloudimg.com/raw/a88cfaa84e953695d5e674e4a90a84df.png)
3. 获取链接后，只需访问 `首页地址+分享链接` 即可下载该文件。
例如，首页地址为 `http://xxx.xxx.xxx`，分享链接为 `/s/jRfM`，则访问 `http://xxx.xxx.xxx/s/jRfM` 即可下载该文件。

#### 离线下载
Cloudreve 应用镜像中已预置 Aria2，无需重复下载安装。Cloudreve 支持 Aria2 驱动的离线下载功能。在使用该功能前，您需了解 Aria2 配置与 Cloudreve 接入设置。步骤如下：
1. 在 Cloudreve 页面中，选择右上角的用户头像，并在弹出菜单中单击【管理面板】。
2. 进入”Cloudreve 仪表盘“ 页面，选择左侧导航栏中的【参数设置】>【离线下载】。可查看相关参数设置如下图所示：
您可参考 [离线下载](https://docs.cloudreve.org/use/aria2)，按需修改相关参数设置。
<img src="https://main.qcloudimg.com/raw/5eaab79ca7797a5b64cb8a3a3b7af3dd.png" width="70%">



创建离线下载步骤如下：
1. 在 Cloudreve 页面中，选择左侧导航栏中的【离线下载】。
2. 进入“离线下载”页面，选择页面右下角的【+】。
3. 在弹出的“新建离线下载任务”窗口中，根据指引创建下载任务即可。如下图所示：
![](https://main.qcloudimg.com/raw/0ec3a87d6e8e3faaacd05463bfcb2b19.png)

#### 后台管理
1. 在 Cloudreve 页面中，选择右上角的用户头像，并在弹出菜单中单击【管理面板】。
2. 进入”Cloudreve 仪表盘“页面，您可进行用户组权限、存储策略等参数设置。
 - 可根据用户所属的用户组类型设置其权限，例如容量上限、下载速度、创建分享、下载分享及 WebDAV 等。
 - 可更改默认存储策略，各类型存储策略对比请参见 [对比 - Cloudreve](https://docs.cloudreve.org/use/policy/compare)。

## 相关操作

### 登录宝塔 Linux 面板 
Cloudreve 应用镜像已集成宝塔 Linux 面板，您可利用宝塔面板可轻松管理轻量应用服务器、提升运维效率及实时监控实例运行情况。
>?宝塔 Linux 面板默认端口为8888，请确保您已在实例防火墙中放通8888端口。详情请参见 [添加防火墙规则](https://cloud.tencent.com/document/product/1207/44577#.E6.B7.BB.E5.8A.A0.E9.98.B2.E7.81.AB.E5.A2.99.E8.A7.84.E5.88.99)。
>
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，选择实例进入详情页。
2. 在实例详情页中，选择【应用管理】页签，进入应用管理详情页。
3. [](id:step3)在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px">，复制获取宝塔 Linux 面板管理员密码的命令。 如下图所示：
![](https://main.qcloudimg.com/raw/557c5f45fdacb6300d9161b78c71c812.png)
4. 在“应用内软件信息”栏中，单击【登录】。
5. 在弹出的登录窗口中，粘贴并执行 [步骤3](#step3) 获取的命令，按 **Enter**。
6. [](id:step6)记录返回结果中的宝塔 Linux 面板管理员名与密码（即 “username” 和 “password” 值）。如下图所示：
![](https://main.qcloudimg.com/raw/74ef86c0cb12db2850b012cb6fa73ffe.png)
6. 使用浏览器访问“应用内软件信息”中的“面板首页地址”，输入 [步骤6](#step6) 获取的用户名与密码，并单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/60f0f6af7d4e2d085b142593349903fb.png)

### 使用宝塔 Linux 面板管理 Mariadb 数据库
在宝塔 Linux 面板中，选择左侧导航栏中的【数据库】，进入“数据库管理”页面。如下图所示：
在此页面中，您可进行一键修改数据库密码、一键备份及更改 IP 权限等操作。
![](https://main.qcloudimg.com/raw/937f11d9c357bcfa9ab86e18132d9088.png)


### 配置操作系统防火墙[](id:updatePort)
可通过宝塔面板直接放通操作系统防火墙端口。步骤如下：
1. 在宝塔 Linux 面板中，选择左侧【安全】。
2. 在“系统安全”页面的“防火墙”中，填写需放行端口号及说明。如下图所示：
![](https://main.qcloudimg.com/raw/866b18637a5587cd09b0919e16aa5f0d.png)
3. 单击【放行】即可放通对应端口。


### 域名与 DNS 解析设置
您可以给自己的 Cloudreve 网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问

可通过宝塔 Linux 面板安装 SSL 证书，开启 HTTPS 访问。步骤如下：
1. 在宝塔 Linux 面板中，选择左侧导航栏中的【面板设置】。
2. 在“面板设置”页面中，开启“面板SSL”开关，并在弹出的“面板SSL”窗口中进行确认即可。如下图所示：
![](https://main.qcloudimg.com/raw/73a3149a77a5f1fcdd96dfa26a1a37a2.png)
>?安装 SSL 证书后的 [常见问题](https://www.bt.cn/bbs/forum.php?mod=viewthread&tid=4689) 及解决办法前往宝塔官方页面查找，您也可以参考腾讯云 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/54869) 文档开启 HTTPS 访问。
