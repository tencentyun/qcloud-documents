## 操作场景
LAMP 环境是指 Linux 系统下，由 Apache  + MariaDB + PHP 及其它相关辅助组件组成的网站服务器架构。本文本文档介绍如何在腾讯云云服务器（CVM）上手动搭建 LAMP 环境。

进行手动搭建 LAMP 环境，您需要熟悉 Linux 命令，例如  [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件使用的版本特性比较了解。
>!腾讯云建议您可以通过云市场的镜像部署 LAMP 环境，手动搭建 LAMP 环境可能需要较长时间。具体步骤可参考 [镜像部署 LAMP 环境](https://cloud.tencent.com/document/product/213/38364)。

## 示例软件版本
本文档搭建 LAMP 环境组成及使用版本说明如下：
- Linux：Linux 操作系统，本文以 CentOS 7.6 为例。
- Apache：Web 服务器软件，本文以 Apache 2.4.6 为例。
- MariaDB：数据库管理系统，本文以 MariaDB 10.4.8 为例。
- PHP：脚本语言，本文以 PHP 7.0.33 为例。

## 前提条件
已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。

## 操作步骤
### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)

### 步骤2：安装 Apache
1. 执行以下命令，安装 Apache。
```
yum install httpd -y
```
2. 依次执行以下命令，启动 Apache 并设置为开机自启动。
```
systemctl start httpd
```
```
systemctl enable httpd
```
3. 在本地浏览器中访问以下地址，查看 Apache 服务是否正常运行。
```
http://云服务器实例的公网 IP
```
显示如下，则说明 Apache 安装成功。
![](https://main.qcloudimg.com/raw/f9dc3992f4d6e7e94bb63330fd5cadfe.png)


### 步骤3：安装配置 MariaDB
1. 执行以下命令，查看系统中是否已安装 MariaDB。
```
rpm -qa | grep -i mariadb
```
 - 返回结果类似如下内容，则表示已存在 MariaDB。
 ![](https://main.qcloudimg.com/raw/6fa7fb51de4a61f4da08eb036b6c3e85.png)
为避免安装版本不同造成冲突，请执行下面命令移除已安装的 MariaDB。
```
yum -y remove 包名
```
 - 若返回结果为空，则说明未预先安装，则执行下一步。
2. 执行以下命令，在 `/etc/yum.repos.d/` 下创建 `MariaDB.repo` 文件。 
```
vi /etc/yum.repos.d/MariaDB.repo
```
3. 按 “**i**” 切换至编辑模式，并写入以下内容。
```
# MariaDB 10.4 CentOS repository list - created 2019-11-05 11:56 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.4/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
```
>?您可前往 [MariaDB 官网](https://downloads.mariadb.org/) 获取其他版本操作系统的安装信息。
>
5.  按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
6.  执行以下命令，安装 MariaDB。
```
yum -y install MariaDB-client MariaDB-server
```
7. 依次执行以下命令，启动 MariaDB 服务，并设置为开机自启动。
```
systemctl start mariadb
```
```
systemctl enable mariadb
```
8. 执行以下命令，验证 MariaDB 是否安装成功。
```
mysql
```
显示结果如下，则成功安装。
![](https://main.qcloudimg.com/raw/bfe9a604457f6de09933206c21fde13b.png)
9. 执行以下命令，退出 MariaDB。
```
\q
```

### 步骤4：安装配置 PHP
1. 依次执行以下命令，更新 yum 中 PHP 的软件源。
```
rpm -Uvh https://mirrors.cloud.tencent.com/epel/epel-release-latest-7.noarch.rpm 
```
```
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
```
2. 执行以下命令，安装 PHP 7.0.33 所需要的包。
```
yum -y install php70w php70w-opcache php70w-mbstring php70w-gd php70w-xml php70w-pear php70w-fpm php70w-mysql php70w-pdo
```
3. 执行以下命令，修改 Apache 配置文件。
```
vi /etc/httpd/conf/httpd.conf
```
4. 按 “**i**” 切换至编辑模式，并依次修改为如下图所示的内容。
![](https://main.qcloudimg.com/raw/0b478ca5aa21124a531cfd5c8860cb70.png)
![](https://main.qcloudimg.com/raw/aeeb6fff1af9cf71735cae558455ee94.png)
![](https://main.qcloudimg.com/raw/cc840587150c3282c972a6b23e0c1a68.png)
![](https://main.qcloudimg.com/raw/de36e94d0e4791d1d84f141120125456.png)
 1. 在 `ServerName www.example.com:80` 下另起一行，输入以下内容：
 ```
ServerName localhost:80
```
 2. 将 `<Directory>` 中的 `Require all denied` 修改为 `Require all granted`。
 3. 将 `<IfModule dir_module>` 中内容替换为 `DirectoryIndex index.php index.html`。
 4. 在 `AddType application/x-gzip .gz .tgz` 下另起一行，输入以下内容：
```
AddType application/x-httpd-php .php
AddType application/x-httpd-php-source .phps
```
5. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
6. 执行以下命令，重启 Apache 服务。
```
systemctl restart httpd
```

## 验证环境配置
1. 执行以下命令，创建测试文件。
```
echo "<?php phpinfo(); ?>" >> /var/www/html/index.php
```
2. 在本地浏览中访问以下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP/index.php
```
显示结果如下，则说明 LAMP 环境配置成功。
![](https://main.qcloudimg.com/raw/64681fb76bad29072de9ddc3250e66d1.png)

## 相关操作
在完成了 LAMP 环境搭建后，您可在此基础上进行 [手动搭建 Drupal 网站](https://cloud.tencent.com/document/product/213/38617) 实践，了解并掌握更多关于云服务器的相关功能。


## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考[ IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。
