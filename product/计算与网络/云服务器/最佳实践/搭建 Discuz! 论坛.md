## 操作场景

Discuz! 是全球成熟度最高、覆盖率最大的论坛网站软件系统之一，被200多万网站用户使用。您可通过 Discuz! 搭建论坛，本文档介绍在腾讯云云服务器上搭建 Discuz! 论坛及其所需的 LAMP（Linux + Apache + MariaDB + PHP）环境。


进行手动搭建 Discuz! 论坛，您需要熟悉 Linux 命令，例如 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件的使用及版本兼容性比较了解。
>!腾讯云建议您可以通过云市场的镜像环境部署 Discuz! 论坛，手动搭建过程可能需要较长时间。具体步骤可参考 [镜像部署 Discuz! 论坛](https://cloud.tencent.com/document/product/213/9753)。
>

## 示例软件版本
本文搭建的 Discuz! 论坛软件组成版本及说明如下：
- Linux：Linux 操作系统，本文以 CentOS 7.6 为例。
- Apache：Web 服务器，本文以 Apache 2.4.15 为例。
- MariaDB：数据库，本文以 MariaDB 5.5.60 为例。
- PHP：脚本语言，本文以 PHP 5.4.16 为例。
- Discuz!：论坛网站软件，本文以 Discuz! X3.4 为例。


## 操作步骤
### 步骤1：登录云服务器
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)



### 步骤2：搭建 LAMP 环境 

对于 CentOS 系统，腾讯云提供与 CentOS 官方同步的软件安装源，包含的软件均为当前最稳定的版本，可直接通过 Yum 快速安装。

<span id="InstallNecessarySoftware"></span>
#### 安装配置必要软件
1. 执行以下命令，安装必要软件（Apache、MariaDB、PHP、Git）：
```
yum install httpd php php-fpm php-mysql mariadb mariadb-server git -y
```
2. 依次执行以下命令，启动服务。
```
systemctl start httpd
```
```
systemctl start mariadb
```
```
systemctl start php-fpm
```
3. <span id="step3"></span>执行以下命令，设定 root 帐户密码及基础配置，使 root 用户可以访问数据库。
>!
>- 针对首次登录 MariaDB 前执行以下命令进入用户密码及基础设置。
>- 首次提示输入 root 密码后按 **Enter** 直接进入 root 密码设置步骤，设置 root 密码时界面默认不显示，并再次输入确认。通过界面上的提示完成基础配置。
> 
```
mysql_secure_installation
```
4. 执行以下命令，登录 MariaDB，并输入 [步骤3](#step3) 设置的密码，按 “**Enter**”。
```
mysql -u root -p
``` 
若输入刚设定的密码可以登录到 MariaDB 中，则说明配置正确。如下图所示：
![](https://main.qcloudimg.com/raw/18c54971e141db38c3f483161fefe251.png)

5. 执行以下命令，退出 MariaDB 数据库。
```
\q
```

#### 验证环境配置

为确认和保证环境搭建成功，您可以通过以下操作来验证：
1. 执行以下命令，在 Apache 的默认根目录 `/var/www/html` 中创建 `test.php` 测试文件。
```
vim /var/www/html/test.php
```
2. 按 **i** 切换至编辑模式，写入如下内容：
```
<?php
echo "<title>Test Page</title>";
phpinfo()
?>
```
3. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 在浏览器中，访问该`test.php`文件，查看环境配置是否成功。
```
http://云服务器的公网 IP/test.php 
```
出现以下页面，则说明 LAMP 环境配置成功。
![](https://main.qcloudimg.com/raw/f511b15ac3016d710c2b1f833e69448d.png)



<span id="InstallDiscuz"></span>
### 步骤3：安装和配置 Discuz!  

#### 下载 Discuz! 
执行以下命令，下载安装包。
```
git clone https://gitee.com/ComsenzDiscuz/DiscuzX.git
```

#### 安装准备工作
1. 执行以下命令，进入下载好的安装目录。
```
cd DiscuzX
```
2. 执行以下命令，将 “upload” 文件夹下的所有文件复制到 `/var/www/html/`。
```
cp -r upload/* /var/www/html/
```
3. 执行以下命令，将写权限赋予给其他用户。
```
chmod -R 777 /var/www/html
```

#### 安装 Discuz!
1. 在 Web 浏览器地址栏中，输入 Discuz! 站点的 IP 地址（即云服务器实例的公网 IP 地址）或通过 [相关操作](#ConfigureDomain) 获取的可用域名，即可看到 Discuz! 安装界面。如下图所示：
![](https://main.qcloudimg.com/raw/aeb31eb70f45bef295250b359a750b84.png)
2. 单击【我同意】，进入检查安装环境页面。如下图所示：
![](https://main.qcloudimg.com/raw/470f6dd4dd2551da8c543070d100707b.png)
3. 确认当前状态正常，单击 【下一步】，进入设置运行环境页面。如下图所示：
![](https://main.qcloudimg.com/raw/fbcf579c70121a6622fc0adb54a84bf0.png)
4. 选择全新安装，单击【下一步】，进入创建数据库页面。如下图所示：
![](https://main.qcloudimg.com/raw/83fe2d6b18f88ad9096e71f8abcb898b.png)
5. 根据页面提示，填写信息，为 Discuz! 创建一个数据库。
>!  
>- 请使用 [安装必要软件](#InstallNecessarySoftware) 设置的 root 帐号和密码连接数据库，并设置好系统信箱、管理员帐号、密码和 Email。
>- 请记住自己的管理员用户和密码。
>
6. 单击【下一步】，开始安装。
6. 安装完成后，单击【您的论坛已完成安装，点此访问】，即可访问论坛。如下图所示：
![](https://main.qcloudimg.com/raw/56ac7c82a4041a84b1861234e8eda802.png)

<span id="ConfigureDomain"></span>
## 相关操作
您可以给自己的 Discuz! 论坛网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建论坛仅用于学习，那么可使用 IP 直接安装临时使用，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的论坛，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。
 


