## 操作场景
LNMP 环境是指在 Linux 系统下，由 Nginx + MySQL/MariaDB + PHP 组成的网站服务器架构。本文档介绍如何在腾讯云云服务器（CVM）上手动搭建 LNMP 环境。

进行手动搭建 LNMP 环境，您需要熟悉 Linux 命令，例如 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件的使用及版本兼容性比较了解。

>!腾讯云建议您可以通过云市场的镜像环境部署 LNMP 环境，手动搭建 LNMP 环境可能需要较长的时间。具体步骤可参考 [镜像部署 LNMP 环境](https://cloud.tencent.com/document/product/213/38053)。


## 示例软件版本
本文搭建的 LNMP 环境软件组成版本及说明如下：
Linux：Linux 操作系统，本文以 CentOS 6.9 为例。
Nginx：Web 服务器，本文以 Nginx 1.17.5 为例。
MySQL：数据库，本文以 MySQL 5.1.73 为例。
PHP：脚本语言，本文以 PHP 7.1.32 为例。

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
name=nginx repo
baseurl=https://nginx.org/packages/mainline/centos/6/$basearch/
gpgcheck=0
enabled=1
```
3. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 执行以下命令，安装 Nginx。
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
8. 按 **Esc**，输入 **:wq**，保存文件并返回。
9. 执行以下命令，启动 Nginx。
```
service nginx start
```
10. 依次执行以下命令，设置 Nginx 为开机自启动。
```bash
chkconfig --add nginx
```
```
chkconfig  nginx on
```
11. 在本地浏览器中访问以下地址，查看 Nginx 服务是否正常运行。
```
http://云服务器实例的公网 IP
```
显示结果如下，则说明 Nginx 安装配置成功。
![](https://main.qcloudimg.com/raw/fdc40877928729679d392eb304a3f12c.png)


### 步骤3：安装数据库
1. 执行以下命令，查看系统中是否已安装 MySQL。
```
rpm -qa | grep -i mysql
```
 - 返回结果如下所示，则表示已存在 MySQL。
![](https://main.qcloudimg.com/raw/74e544638637d39209cc1e474083d11d.png)
为避免安装版本不同造成冲突，请执行下面命令移除已安装的 MySQL。
```
yum remove -y 包名
``` 
 - 若返回结果为空，则说明未预先安装，则执行下一步。
2.  执行以下命令，安装 MySQL。
```
yum install -y mysql-devel.x86_64 mysql-server.x86_64 mysql-libs.x86_64
```
3. 执行以下命令，启动 MySQL。
```
service mysqld start 
```
4. 依次执行以下命令，设置 MySQL 为开机自启动。
```bash
chkconfig --add mysqld
```
```
chkconfig mysqld  on 
```
5. 执行以下命令，验证 MySQL 是否安装成功。
```
mysql
```
显示结果如下，则成功安装。
![](https://main.qcloudimg.com/raw/9c9347ad0264ddad5e98c8dd48adcc6a.png)
6. 执行以下命令，退出 MySQL。
```
\q
```

### 步骤4：安装配置 PHP
1. 依次执行以下命令，更新 yum 中 PHP 的软件源。
```
rpm -Uvh https://mirrors.cloud.tencent.com/epel/epel-release-latest-6.noarch.rpm
```
```
rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm
```
2. 执行以下命令，安装 PHP 7.1.32 所需要的包。
```
yum -y install mod_php71w.x86_64 php71w-cli.x86_64 php71w-common.x86_64 php71w-mysqlnd php71w-fpm.x86_64
```
3. 执行以下命令，启动 PHP-FPM 服务。
```
service php-fpm start
```
3. 依次执行以下命令，设置 PHP-FPM 为开机自启动。
```bash
chkconfig --add php-fpm  
```
```
chkconfig php-fpm on
```


## 验证环境配置
1. 执行以下命令，创建测试文件。
```
echo "<?php phpinfo(); ?>" >> /usr/share/nginx/html/index.php
```
2. 执行以下命令，重启 Nginx。
```
service nginx restart
```
3. 在本地浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP
```
显示结果如下， 则说明环境配置成功。
![](https://main.qcloudimg.com/raw/64af927320f2121ae4daf15cf2eaba39.png)



## 相关操作

在完成了 LNMP 环境搭建之后，您可在此基础上进行 [手动搭建 Wordpress 个人站点](https://cloud.tencent.com/document/product/213/8044) 实践，了解并掌握更多关于云服务器的相关功能。

## 常见问题

如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：

- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。
