## 操作场景
WordPress 是一款使用 PHP 语言开发的博客平台，您可使用通过 WordPress 搭建属于个人的博客平台。本文以 Windows Server 2012 操作系统的腾讯云云服务器为例，手动搭建 WordPress 个人站点。

>! 腾讯云建议您可以通过云市场的镜像环境部署 WordPress 个人博客，手动搭建过程可能需要较长时间。具体步骤可参考 [镜像部署 WordPress 个人站点](https://cloud.tencent.com/document/product/213/9740)。 

## 示例软件版本
WordPress 个人站点可搭建在 PHP 5.6.20及之后版本和 MySQL 5.0及之后版本中。为了提高安全性，搭建 WordPress 个人站点时，建议选择 PHP 7.3 及之后版本和 MySQL 5.6 及之后版本进行安装。

本文搭建的 WordPress 个人站点组成版本及说明如下：
- Windows：Windows 操作系统，本文以 Windows Server 2012 为例。
- IIS：Web 服务器，本文以 IIS 8.5 为例。
- MySQL：数据库，本文以 MySQL 5.6.46 为例。
- PHP：脚本语言，本文以 PHP 7.3.12 为例。
- WordPress：博客平台，本文以 WordPress 5.3 为例。


## 操作步骤

### 步骤1：登录云服务器
[使用 RDP 文件登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/5435)。
您也可以根据实际操作习惯，[使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)。

### 步骤2：搭建 WIPM 环境
参考 [手动搭建 WIPM 环境](https://cloud.tencent.com/document/product/213/39541) 进行如下操作：
1. 安装 IIS 服务。
2. 部署 PHP 5.6.20及之后版本环境。
3. 安装 MySQL 5.6 及之后版本数据库。

### 步骤3：安装和配置 WordPress
>? WordPress 可从 WordPress 官方网站下载 WordPress 最新中文版本并安装，本教程采用 WordPress 中文版本。
>

1. 下载 WordPress，并将 WordPress 安装包解压至云服务器中。
例如，将 WordPress 安装包解压至 `C:\wordpress` 目录下。
2. 单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin: 0;"> >  <img src="https://main.qcloudimg.com/raw/ca83b4e70e201fe9ff98dc1f2b207cee.png" style="margin: 0;"> >  **MySQL 5.6 Command Line Client**，打开 MySQL 命令行客户端。
3. 在 MySQL 命令行客户端中，执行以下命令，创建 WordPress 数据库。
例如，创建 “wordpress” 数据库。
```
create database wordpress;
```
4. 在 WordPress 的解压安装路径下，找到并复制 `wp-config-sample.php` 文件，并将该文件重命名为 `wp-config.php`。
5. 使用文本编辑器打开 `wp-config.php` 文件，并将相关配置信息修改为 [步骤3：安装 MySQL 数据库](https://cloud.tencent.com/document/product/213/10190) 的内容。如下图所示：
![](https://main.qcloudimg.com/raw/ed808064e32f8c6c133e74472c934c0b.png)
6. 保存 `wp-config.php` 文件。
7. 单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin: 0;">，打开服务器管理器。
8. 在服务器管理器的左侧导航栏中，选择**IIS**，并在右侧 IIS 管理窗口中右键单击**服务器**栏中的服务器名称，选择**Internet Information Sevices (IIS)管理器**。
9. 在打开的 “Internet Information Sevices (IIS)管理器” 窗口中，依次展开左侧导航栏的服务器名称，单击**网站**，进入 “网站” 管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/7b564d224b02512904d5647c1cb243de.png)
10. 删除**网站**下绑定端口为80的网站。
您也可以将网站的绑定端口修改为其他未被占用的端口号。例如修改为8080端口。
11. 在右侧的**操作**栏中，单击**添加网站**。
12. 在弹出的窗口中，填写以下信息，并单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/3204591ca44496116b156e073b37526a.png)
 - 网站名称：用户自定义，例如 wordpress。
 - 应用程序池：选择为**DefaultAppPool**。
 - 物理路径：选择为 WordPress 解压后的存放路径，例如 `C:\wordpress`。
13. 在 PHP 的解压安装路径下，打开 `php.ini` 文件，并修改以下内容。
 1. 根据 PHP 版本不同，修改相应的配置参数：
     - 针对 PHP 版本为5.X版本，找到`extension=php_mysql.dll`，删除前面的`;`。
     - 针对 PHP 版本为7.X版本，找到`extension=mysqli` ，删除前面的`;`。
 2. 找到`extension_dir = "ext"`，删除前面的`;`。
14. 保存 `php.ini` 文件。

### 步骤4：验证 WordPress 配置

1. 使用浏览器访问 `http://localhost/wp-admin/install.php`，转至 WordPress 安装页，开始配置 WordPress。
2. 根据 WordPress 安装向导提示输入以下安装信息，单击**安装 WordPress**，完成安装。
<table>
	<tr><th>所需信息</th><th>说明</th></tr>
	<tr><td>站点标题</td><td>WordPress 网站名称。</td></tr>
	<tr><td>用户名</td><td>WordPress 管理员名称。出于安全考虑，建议设置一个不同于 admin 的名称。因为与默认用户名称 admin 相比，该名称更难破解。</td></tr>
	<tr><td>密码</td><td>可以使用默认强密码或者自定义密码。请勿重复使用现有密码，并确保将密码保存在安全的位置。</td></tr>
	<tr><td>您的电子邮件</td><td>用于接收通知的电子邮件地址。</td></tr>
</table>
现在可以用登录 WordPress 博客，并开始发布博客文章了。

## 相关操作

您可以给自己的 WordPress 博客网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接安装临时使用，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的博客，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。

