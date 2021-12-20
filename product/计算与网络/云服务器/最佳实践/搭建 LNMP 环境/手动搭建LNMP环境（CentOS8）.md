## 操作场景
LNMP 环境是指在 Linux 系统下，由 Nginx + MySQL/MariaDB + PHP 组成的网站服务器架构。本文档介绍如何在腾讯云云服务器（CVM）上手动搭建 LNMP 环境。

进行手动搭建 LNMP 环境，您需要熟悉 Linux 命令，并对所安装软件的使用及版本兼容性比较了解。

<dx-alert infotype="notice" title="">
腾讯云建议您可以通过云市场的镜像环境部署 LNMP 环境，手动搭建 LNMP 环境可能需要较长的时间。具体步骤可参考 [镜像部署 LNMP 环境](https://cloud.tencent.com/document/product/213/38053)。

</dx-alert>



## 示例软件版本
本文搭建的 LNMP 环境软件组成版本及说明如下：
Linux：Linux 操作系统，本文以 CentOS 8.0 为例。
Nginx：Web 服务器，本文以 Nginx 1.18.0 为例。
MySQL：数据库，本文以 MySQL 8.0.21 为例。
PHP：脚本语言，本文以 PHP 7.4.11 为例。

## 前提条件
已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。

## 操作步骤
### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)

### 步骤2：安装及配置 Nginx
1. 执行以下命令，安装 Nginx。
<dx-alert infotype="explain" title="">
本文以安装 Nginx 1.18.0 为例，您可通过 [Nginx 官方安装包](http://nginx.org/packages/centos/8/x86_64/RPMS/?spm=a2c4g.11186623.2.31.557423bfYPMd6u) 获取适用于 CentOS 8的更多版本。
</dx-alert>
```
dnf -y install http://nginx.org/packages/centos/8/x86_64/RPMS/nginx-1.18.0-1.el8.ngx.x86_64.rpm
```
2. 执行以下命令，查看 Nginx 版本。
```
nginx -v
```
返回类似如下结果，则表明已成功安装。
```
nginx version: nginx/1.18.0
```
3. 执行以下命令，查看 Nginx 配置文件路径。
```
cat /etc/nginx/nginx.conf
```
可查看 include 配置项的 `/etc/nginx/conf.d/*.conf` 即为 Nginx 配置文件的默认路径。
4. 依次执行以下命令，在配置文件默认路径下进行备份。
```
cd /etc/nginx/conf.d
```
```
cp default.conf default.conf.bak
```
5. 执行以下命令，打开 default.conf 文件。
```
vim default.conf
```
6. 按 **i** 切换至编辑模式，编辑 default.conf 文件。
  1. 在 location 的 index 项中添加 index.php。如下图所示：
![](https://main.qcloudimg.com/raw/32df0b8ba82278cd96cf86152738677e.png)
  2. 删除 location ~  \\.php$ 大括号前的 `#`，并修改以下配置项：
    - 修改 root 项为您的网站根目录，即 location 中的 root 项，本文以 `/usr/share/nginx/html;` 为例。
    - 修改 fastcgi_pass 项为 `unix:/run/php-fpm/www.sock;`，Nginx 通过 UNIX 套接字与 PHP-FPM 建立联系，该配置与 `/etc/php-fpm.d/www.conf` 文件内的 listen 配置一致。
    - 将 fastcgi_param  SCRIPT_FILENAME 后的 `/scripts$fastcgi_script_name;` 替换为 `$document_root$fastcgi_script_name;`。
    修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/2e4bff09d70399881bfbf995390a58d3.png) 
7. 按 **Esc**，输入 **:wq**，保存文件并返回。
8. 依次执行以下命令，启动 Nginx 并设置为开机自启动。
```
systemctl start nginx
```
```
systemctl enable nginx
```

### 步骤3：安装及配置 MySQL
1. 执行以下命令，安装 MySQL。
```
dnf -y install @mysql
```
2. 执行以下命令，查看 MySQL 版本。
```
mysql -V
```
返回类似如下结果，则表明已安装成功。
```
mysql  Ver 8.0.21 for Linux on x86_64 (Source distribution)
```
3. 依次执行以下命令，启动 MySQL 并设置为开机自启动。
```
systemctl enable --now mysqld
```
```
systemctl status mysqld
```
4. 执行以下命令，执行 MySQL 安全性操作并设置密码。
```
mysql_secure_installation
```
按照以下步骤，执行对应操作：
  1. 输入 `y` 并按 **Enter** 开始相关配置。
  2. 选择密码验证策略强度，建议选择高强度的密码验证策略。输入 `2` 并按 **Enter**。
    - 0：表示低。
    - 1：表示中。
    - 2：表示高。
  3. 设置 MySQL 密码并按 **Enter** ，输入密码默认不显示。
  4. 再次输入密码并按 **Enter**，输入 `y` 确认设置该密码。
  5. 输入 `y` 并按 **Enter**，移除匿名用户。
  6. 设置是否禁止远程连接 MySQL：
    - 禁止远程连接：输入 `y` 并按 **Enter**。
    - 允许远程连接：输入 `n` 并按 **Enter**。
  7. 输入 `y` 并按 **Enter**，删除 test 库及对 test 库的访问权限。
  8. 输入 `y` 并按 **Enter**，重新加载授权表。

### 步骤4：安装及配置 PHP
1. 依次执行以下命令，添加并更新 epel 源。
```
dnf -y install epel-release
```
```
dnf update epel-release
```
2. 依次执行以下命令，删除缓存的无用软件包并更新软件源。
```
dnf clean all
```
```
dnf makecache
```
3. 执行以下命令，安装 remi 源。
<dx-alert infotype="explain" title="">
安装 PHP 7.4.11 需安装 remi 源，请对应您实际安装的 PHP 版本执行此命令。
</dx-alert>
```
dnf -y install https://rpms.remirepo.net/enterprise/remi-release-8.rpm
```
4. 执行以下命令，启动 PHP 7.4 模块。
```
dnf module install php:remi-7.4
```
5. 执行以下命令，安装所需 PHP 对应模块。
```
dnf install php php-curl php-dom php-exif php-fileinfo php-fpm php-gd php-hash php-json php-mbstring php-mysqli php-openssl php-pcre php-xml libsodium
```
6. 执行以下命令，查看 PHP 版本。
```
php -v
```
返回类似如下结果，则表明已安装成功。
```
PHP 7.4.11 (cli) (built: Sep 29 2020 10:17:06) ( NTS )
Copyright (c) The PHP Group
Zend Engine v3.4.0, Copyright (c) Zend Technologies
    with Zend OPcache v7.4.11, Copyright (c), by Zend Technologies
```
7. 执行以下命令，打开 www.conf 文件。
```
vi /etc/php-fpm.d/www.conf
```
8. 按 **i** 切换至编辑模式，编辑 www.conf 文件。
9. 将 user = apache 及 group = apache 修改为 user = nginx 及 group = nginx。如下图所示：
![](https://main.qcloudimg.com/raw/ceb9c202ebe56c9bd9265e86c0ad2333.png)
10. 按 **Esc**，输入 **:wq**，保存文件并返回。
11. 依次执行以下命令，启动 PHP-FPM 并设置为开机自启动。
```
systemctl start php-fpm
```
```
systemctl enable php-fpm
```

### 验证环境配置
1. 执行以下命令，创建测试文件。
<dx-alert infotype="explain" title="">
`/usr/share/nginx/html` 为您在 Nginx 中已配置的网站根目录，本文以该目录为例。
</dx-alert>
```
echo "<?php phpinfo(); ?>" >> /usr/share/nginx/html/index.php
```
2. 在本地浏览器中访问如下地址，查看环境配置是否成功。如何获取实例公网 IP，请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。
```
http://云服务器实例的公网 IP/index.php
```
显示结果如下，则说明环境配置成功。
![](https://main.qcloudimg.com/raw/182c0f73df20d66216a9b73d571b2093.png)

## 相关操作
在完成了 LNMP 环境搭建之后，您可在此基础上进行 [手动搭建 Wordpress 个人站点](https://cloud.tencent.com/document/product/213/8044) 实践，了解并掌握更多关于云服务器的相关功能。

## 常见问题

如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：

- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。

