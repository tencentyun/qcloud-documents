## 操作场景
LNMP 环境是指在 Linux 系统下，由 Nginx + MySQL/MariaDB + PHP 组成的网站服务器架构。本文档介绍如何在腾讯云云服务器（CVM）上手动搭建 LNMP 环境。

进行手动搭建 LNMP 环境，您需要熟悉 Linux 命令，例如 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件的使用及版本兼容性比较了解。

<dx-alert infotype="notice" title="">
腾讯云建议您可以通过云市场的镜像环境部署 LNMP 环境，手动搭建 LNMP 环境可能需要较长的时间。具体步骤可参考 [镜像部署 LNMP 环境](https://cloud.tencent.com/document/product/213/38053)。
</dx-alert>



## 示例软件版本
本文搭建的 LNMP 环境软件组成版本及说明如下：
- Linux：Linux 操作系统，本文以 CentOS 7.6 为例。
- Nginx：Web 服务器，本文以  Nginx 1.17.7 为例。
- MariaDB：数据库，本文以 MariaDB 10.4.8 为例。
- PHP：脚本语言，本文以 PHP 7.2.22 为例。


## 前提条件
已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。


## 操作步骤

### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)

### 步骤2：安装 Nginx
1. 执行以下命令，在 `/etc/yum.repos.d/` 下创建 `nginx.repo` 文件。
```
vi /etc/yum.repos.d/nginx.repo
```
2. 按 **i** 切换至编辑模式，写入以下内容。
```
[nginx] 
name = nginx repo 
baseurl = https://nginx.org/packages/mainline/centos/7/$basearch/ 
gpgcheck = 0 
enabled = 1
```
3. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 执行以下命令，安装 nginx。
```
yum install -y nginx
```
5. 执行以下命令，打开 `default.conf` 文件。
```
vim /etc/nginx/conf.d/default.conf
```
6. 按 **i** 切换至编辑模式，编辑 `default.conf` 文件。
7. 找到 `server{...}`，并将 `server` 大括号中相应的配置信息替换为如下内容。用于取消对 IPv6 地址的监听，同时配置 Nginx，实现与 PHP 的联动。
```
server {
	listen       80;
	root   /usr/share/nginx/html;
	server_name  localhost;
	#charset koi8-r;
	#access_log  /var/log/nginx/log/host.access.log  main;
	#
	location / {
		  index index.php index.html index.htm;
	}
	#error_page  404              /404.html;
	#redirect server error pages to the static page /50x.html
	#
	error_page   500 502 503 504  /50x.html;
	location = /50x.html {
	  root   /usr/share/nginx/html;
	}
	#pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
	#
	location ~ .php$ {
	  fastcgi_pass   127.0.0.1:9000;
	  fastcgi_index  index.php;
	  fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
	  include        fastcgi_params;
	}
}
```
7. 按 **Esc**，输入 **:wq**，保存文件并返回。
8. 执行以下命令启动 Nginx。
```
systemctl start nginx
```
9. 执行以下命令，设置 Nginx 为开机自启动。
```
systemctl enable nginx 
```
10. 在本地浏览器中访问以下地址，查看 Nginx 服务是否正常运行。
```
http://云服务器实例的公网 IP
```
显示如下，则说明 Nginx 安装配置成功。
![](https://main.qcloudimg.com/raw/fdc40877928729679d392eb304a3f12c.png)


### 步骤3：安装数据库
1. 执行以下命令，查看系统中是否已安装 MariaDB。 
```
rpm -qa | grep -i mariadb
```
 - 返回结果类似如下内容，则表示已存在 MariaDB。
![](https://main.qcloudimg.com/raw/6fa7fb51de4a61f4da08eb036b6c3e85.png)
为避免安装版本不同造成冲突，请执行以下命令移除已安装的 MariaDB。
```
yum -y remove 包名
```
 - 若返回结果为空，则说明未预先安装，则执行下一步。
2.  执行以下命令，在 `/etc/yum.repos.d/` 下创建 `MariaDB.repo` 文件。
```
vi /etc/yum.repos.d/MariaDB.repo
```
3. 按 **i** 切换至编辑模式，写入以下内容，添加 MariaDB 软件库。
<dx-alert infotype="explain" title="">
- 以下配置使用了腾讯云镜像源，腾讯云镜像源同步 MariaDB 官网源进行更新，可能会出现 MariaDB 10.4 版本源失效问题（本文以在 CentOS 7.6 上安装 MariaDB 10.4.22 版本为例），您可前往 [MariaDB 官网](https://downloads.mariadb.org) 获取其他版本及操作系统的 MariaDB 软件库安装信息。
- 若您的云服务器使用了 [内网服务](https://cloud.tencent.com/document/product/213/5225)，则可以将 `mirrors.cloud.tencent.com` 替换为 `mirrors.tencentyun.com` 内网地址，内网流量不占用公网流量且速度更快。
</dx-alert>
```
# MariaDB 10.4 CentOS repository list - created 2019-11-05 11:56 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
baseurl = https://mirrors.cloud.tencent.com/mariadb/yum/10.4/centos7-amd64
gpgkey=https://mirrors.cloud.tencent.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1
```
4. 按 **Esc**，输入 **:wq**，保存文件并返回。
5. 执行以下命令，安装 MariaDB。此步骤耗时较长，请关注安装进度，等待安装完毕。
```
yum -y install MariaDB-client MariaDB-server
```
6. 执行以下命令，启动 MariaDB 服务。
```
systemctl start mariadb
```
7. 执行以下命令，设置 MariaDB 为开机自启动。
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
2. 执行以下命令，安装 PHP 7.2 所需要的包。
```
yum -y install mod_php72w.x86_64 php72w-cli.x86_64 php72w-common.x86_64 php72w-mysqlnd php72w-fpm.x86_64
```
3. 执行以下命令，启动 PHP-FPM 服务。
```
systemctl start php-fpm
```
4. 执行以下命令，设置 PHP-FPM 服务为开机自启动。
```
systemctl enable php-fpm
```

## 验证环境配置
当您完成环境配置后，可以通过以下验证 LNMP 环境是否搭建成功。
1. 执行以下命令，创建测试文件。
```
echo "<?php phpinfo(); ?>" >> /usr/share/nginx/html/index.php
```
2. 执行以下命令，重启 Nginx 服务。
```
systemctl restart nginx
```
2. 在本地浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP
```
显示结果如下， 则说明环境配置成功。
![](https://main.qcloudimg.com/raw/640812413941a61efe29d7faa546ad80.png)


## 相关操作
在完成了 LNMP 环境搭建之后，您可在此基础上进行 [手动搭建 Wordpress 个人站点](https://cloud.tencent.com/document/product/213/8044) 实践，了解并掌握更多关于云服务器的相关功能。

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。
