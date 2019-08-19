## 操作场景

Discuz! 是全球成熟度最高、覆盖率最大的论坛网站软件系统之一，被200多万网站用户使用。本教程介绍在 LAMP（Linux + Apache + MariaDB + PHP）环境下搭建 Discuz! 论坛网站的步骤，以 Discuz! X3.2 为例。
具体操作方法如下：
![流程图2](https://main.qcloudimg.com/raw/f26817fd2a6719ccb43cbe744b0af2ed.png)

>? 本文主要介绍自主安装 LAMP 环境并搭建 Discuz! 论坛的方法，推荐具备相关论坛搭建经验和一定的命令操作基础的用户使用。如果您第一次搭建 Discuz! 论坛且不熟悉 Linux 命令，您可以参考 [使用镜像搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/9753)。
>

## 相关简介
以下是本教程中，将会使用的服务或工具：
- **云服务器**：本教程使用腾讯云云服务器（Cloud Virtual Machine，CVM）创建云服务器实例，用来完成 Discuz! 搭建工作。
- **域名注册**：如果想要使用易记的域名访问您的 Discuz! 站点，可以使用腾讯云域名注册服务来购买域名。
- **网站备案**：对于域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云 [网站备案](https://cloud.tencent.com/product/ba) 产品为您的域名备案。
- **云解析**：配置域名解析后，用户可通过域名访问您的网站，不需要使用复杂的 IP 地址才可访问您的网站。您可以通过腾讯云的 [云解析](https://cloud.tencent.com/product/cns) 服务来解析域名。


## 前提条件

已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤

### 创建云服务器
>! 此步骤针对全新购买云服务器。如果您已购买云服务器实例，可以通过重装系统选择 Discuz! 建站系统。
> 本教程中以操作系统版本为 CentOS 7.5 的云服务器实例为例。
> 
1. 在实例的管理页面，单击【新建】，创建实例。
具体操作请参考 [快速入门 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 云服务器创建成功后，返回至 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，查看和获取实例的以下信息。如下图所示：
![实例1](https://main.qcloudimg.com/raw/96a5f8e2eca54d4ea3ec56cb439b025a.png)
 - 云服务器实例用户名和密码
 - 云服务器实例公网 IP

### 搭建 LAMP 环境 

对于 CentOS 系统，腾讯云提供与 CentOS 官方同步的软件安装源，包含的软件均为当前最稳定的版本，可直接通过 Yum 快速安装。

#### 运行 PuTTY 连接 Linux 云服务器
1. [下载 PuTTY ](https://www.putty.org/) 到您的电脑，并解压该文件。
2. 双击 “putty.exe”，弹出 “PuTTY Configuration” 对话框。
3. 选择 “Session”，在 “Host Name (or IP address)” 输入框中输入欲访问的主机名或 IP。例如 “server1” 或 “192.168.2.XX”。
>? 本教程输入的是云服务器实例的公网 IP，其他配置保持默认。
>
4. 在 “Saved Sessions” 输入栏中命名会话，单击 “Save” ，即可保存会话配置。如下图所示：
![putty1](//mc.qcloudimg.com/static/img/85df3247daae4982003a91ad1ad6f89e/image.png)
5. 配置完成后，单击【Open】。
6. 在弹出的确认证书提示对话框中，单击【是】。如下图所示：
![putty2](//mc.qcloudimg.com/static/img/b7883110e977fb0d94310379a152c5d3/image.png)
7. 在 “PuTTY” 运行界面，依次输入云服务器实例的用户名和密码，即可连接到云服务器，进行后续操作。如下图所示：
![putty3](//mc.qcloudimg.com/static/img/b632cf3e122832193a77afe04c93fbc1/image.png)

<span id="InstallNecessarySoftware"></span>
#### 安装必要软件
1. 执行以下命令，安装必要软件（Apache、MariaDB、PHP）：
```
yum install httpd php php-fpm php-mysql mariadb mariadb-server -y
```
安装完成，PuTTY 窗口会提示 “Complete!”。您可以上滑滚动条查看当前安装包版本。
本教程中安装包版本分别如下：
 - Apache：2.4.15
 - MariaDB：5.5.60
 - PHP：5.4.16
2. 执行以下命令，启动服务。
```
systemctl start httpd
systemctl start mariadb
systemctl start php-fpm
```
3. <span id="step3"></span>执行以下命令，设定 root 帐户密码及基础配置，使 root 用户可以访问数据库。
>!
>- 针对首次登录 MariaDB 前执行以下命令进入用户密码及基础设置。
>- 首次输入 root 帐户密码后按下回车键（设置 root 密码时界面默认不显示），并再次输入确认。通过界面上的提示完成基础配置。
> 
```
mysql_secure_installation
```
4. 执行以下命令，登录 MariaDB，并输入 [步骤3](#step3) 设置的密码，按 “**Enter**”。
```
mysql -u root -p
``` 
若输入刚设定的密码可以登录到 MariaDB 中，则说明配置正确。如下图所示：
![](https://main.qcloudimg.com/raw/e22b91cc30bf4155436ab398ee44502a.png)

5. 执行以下命令，退出 MariaDB 数据库。
```
exit
```

#### 验证环境配置

为确认和保证环境搭建成功，您可以通过以下操作来验证：
1. 执行以下命令，在 Apache 的默认根目录 `/var/www/html` 中创建 `test.php` 测试文件。
```
vim /var/www/html/test.php
```
2. 按 “**i**” 切换至编辑模式，写入如下内容：
```
<?php
echo "<title>Test Page</title>";
phpinfo()
?>
```
3. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
4. 在浏览器中，访问该`test.php`文件，查看环境配置是否成功。
```
http://云服务器的公网 IP/test.php 
```
出现以下页面，则说明 LAMP 环境配置成功。
![](https://main.qcloudimg.com/raw/f511b15ac3016d710c2b1f833e69448d.png)


<span id="ConfigureDomain"></span>
### 配置域名（可选）

您可以给自己的 Discuz! 论坛网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建论坛仅用于学习，那么可使用 IP 直接安装临时使用，但不推荐这样操作。
如果您使用 IP 直接安装，请跳过此步骤，直接 [安装 Discuz!](#InstallDiscuz)。
如果您已有域名或者想要通过域名来访问您的论坛，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，一般审核时间为20天左右。
3. 通过腾讯云 [云解析](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

<span id="InstallDiscuz"></span>
### 下载和安装 Discuz!  

#### 下载 Discuz! 
执行以下命令，下载安装包。
```
wget http://download.comsenz.com/DiscuzX/3.2/Discuz_X3.2_SC_UTF8.zip
```

#### 安装准备工作
1. 执行以下命令，解压安装包。
```
unzip Discuz_X3.2_SC_UTF8.zip
```
2. 执行以下命令，将解压后的 “upload” 文件夹下的所有文件复制到 `/var/www/html/`。
```
cp -r upload/* /var/www/html/
```
3. 执行以下命令，将写权限赋予给其他用户。
```
chmod -R 777 /var/www/html
```

#### 安装 Discuz!
1. 在 Web 浏览器地址栏中，输入 [配置域名](#ConfigureDomain) 中已配置好的域名或 Discuz! 站点的 IP 地址（即云服务器实例的公网 IP 地址），即可看到 Discuz! 安装界面。如下图所示：
![安装1](//mc.qcloudimg.com/static/img/ad97b179b5b4977d86ca09a78ef05a7d/image.png)
2. 单击【我同意】，进入检查安装环境页面。如下图所示：
![安装2](//mc.qcloudimg.com/static/img/c5a521673ed6f1a3528ba67ca5886ee4/image.png)
3. 确认当前状态正常，单击 【下一步】，进入设置运行环境页面。如下图所示：
![安装3](//mc.qcloudimg.com/static/img/11a44bd86bfdfcd1fe3dcce6e8f200e6/image.png)
4. 选择全新安装，单击【下一步】，进入创建数据库页面。如下图所示：
![安装4改](//mc.qcloudimg.com/static/img/5d5184cfb34f98d791c243273b910065/image.png)
5. 根据页面提示，填写信息，为 Discuz! 创建一个数据库。
>!  
>- 请使用 [安装必要软件](#InstallNecessarySoftware) 设置的 root 帐号和密码连接数据库，并设置好系统信箱、管理员帐号、密码和 Email。
>- 请记住自己的管理员用户和密码。
>
6. 单击【下一步】，开始安装。
6. 安装完成后，单击【您的论坛已完成安装，点此访问】，即可访问论坛。如下图所示：
![安装5](//mc.qcloudimg.com/static/img/41dab1ec86120a565bdd790238f271da/image.png)
 
