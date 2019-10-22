## 操作场景
LAMP 环境是指 Linux 系统下，由 Apache  + MariaDB + PHP 及其它相关辅助组件组成的网站服务器架构。本文档以 CentOS 7.6 的 Linux 操作系统的腾讯云云服务器（CVM）为例，手动搭建 LAMP 环境。

LAMP 组成及使用版本说明：
- Linux：Linux 操作系统，本文使用 CentOS 7.6。
- Apache：Web 服务器软件，本文使用 Apache 2.4.6。
- MariaDB：数据库管理系统，本文使用 MariaDB 10.4。
- PHP：脚本语言，本文使用 PHP 7.0.33。

## 技能要求
进行手动搭建 LAMP 环境，您需要熟悉 Linux 命令，例如  [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件使用的版本特性比较了解。
>!腾讯云建议您可以通过云市场的镜像部署 LAMP 环境，手动搭建 LAMP 环境可能需要较长时间。具体步骤可参考 [使用镜像搭建 LAMP 环境](https://cloud.tencent.com/document/product/213/38364)。


## 前提条件
- 已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 已登录 Linux 云服务器。如果您还未登录，请准备好云服务器的登录密码及公网 IP，参考 [使用标准方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436) 完成登录。

## 操作步骤
当您登录 Linux 云服务器后，可以按照以下步骤分别安装 Apache，MariaDB 和 PHP。


### 步骤1：安装 Apache
1. 执行以下命令，安装 Apache。
```
yum install httpd -y
```
2. 依次执行以下命令，启动 Apache 并设置为开机自启动。
```
systemctl start httpd
systemctl enable httpd
```
3. 在浏览器中，访问 CentOS 云服务器实例公网 IP，查看 Apache 服务是否正常运行。
显示如下，则说明 Apache 安装成功。
![](https://main.qcloudimg.com/raw/f9dc3992f4d6e7e94bb63330fd5cadfe.png)


### 步骤2：安装配置 MariaDB
1. 执行以下命令，查看系统中是否存在 MariaDB 现有包。
```
rpm -qa | grep -i mariadb
```
 - 返回结果类似如下内容，则表示已存在 MariaDB，请执行 [步骤2](#step2) 依次移除。
 ![](https://main.qcloudimg.com/raw/6fa7fb51de4a61f4da08eb036b6c3e85.png)
 - 返回结果类似如下内容，则请执行 [步骤3](#step3) 开始安装 MariaDB。
![](https://main.qcloudimg.com/raw/2695390041ffef31032739281c91c228.png)
2. <span id="step2"></span>执行以下命令，删除 MariaDB 现有包。
```
yum -y remove 包名
```
3. <span id="step3"></span>执行以下命令，在 `/etc/yum.repos.d/` 下创建 `MariaDB.repo` 文件。 
```
vi /etc/yum.repos.d/MariaDB.repo
```
4. 按 “**i**” 或 “**Insert**” 切换至编辑模式，并写入以下内容。
```
# MariaDB 10.4 CentOS7-amd64
[mariadb]  
name = MariaDB  
baseurl = http://mirrors.cloud.tencent.com/mariadb/yum/10.4/centos7-amd64/
gpgkey = http://mirrors.cloud.tencent.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1
```
>?腾讯云软件源站每天从各软件源的官网同步一次软件资源，请从 [MariaDB 软件源](http://mirrors.cloud.tencent.com/mariadb/yum/) 中获取最新地址。
>
5.  按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
6.  执行以下命令，安装 MariaDB。
```
yum -y install MariaDB-client MariaDB-server
```
7. 依次执行以下命令，启动 MariaDB 服务，并设置为开机自启动。
```
systemctl start mariadb
systemctl enable mariadb
```
8. 执行以下命令，验证 MariaDB 是否安装成功。
```
mysql
```
显示结果如下，则成功安装。
![](https://main.qcloudimg.com/raw/bfe9a604457f6de09933206c21fde13b.png)

### 步骤3：安装配置 PHP
1. 依次执行以下命令，更新 yum 中 PHP 的软件源。
```
rpm -Uvh https://mirrors.cloud.tencent.com/epel/epel-release-latest-7.noarch.rpm 
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
按 “**i**” 或 “**Insert**” 切换至编辑模式：
 - 在 `ServerName www.example.com:80` 下另起一行，增加以下内容：
```
ServerName localhost:80
```
修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/b0ea5d5cea2883a89890482b98b9e81d.png)
 - 将 `<Directory>` 中的 `Require all denied` 修改为以下内容：
```
Require all granted
```
 修改完成后如下图所示：
 ![](https://main.qcloudimg.com/raw/5c4e2019b90e038d169ede1e1606dcba.png)
 - 将 `<IfModule dir_module>` 中内容替换为以下配置：
```
DirectoryIndex index.php index.html
```
 修改完成后如下图所示：
 ![](https://main.qcloudimg.com/raw/ae7ff73d2af51b3989474cb51971ddf0.png)
 - 在 `AddType application/x-gzip .gz .tgz` 后另起一行，输入以下内容：
```
AddType application/x-httpd-php .php
AddType application/x-httpd-php-source .phps
```
修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/57ff0ddb44c0bcbf20148b5df8bc0e38.png)
4. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
5. 执行以下命令，重启 Apache 服务。
```
systemctl restart httpd
```

### 环境配置验证
1. 执行以下命令，创建测试文件。
```
echo "<?php phpinfo(); ?>" >> /var/www/html/index.php
```
在浏览中访问以下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP
```
显示结果如下，则说明 LAMP 环境配置成功。
![](https://main.qcloudimg.com/raw/64681fb76bad29072de9ddc3250e66d1.png)

## 相关操作
在完成了 LAMP 环境搭建后，您可在此基础上进行 [手动搭建 Drupal 网站]() 实践，了解并掌握更多关于云服务器的相关功能。、


## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考[ IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。

