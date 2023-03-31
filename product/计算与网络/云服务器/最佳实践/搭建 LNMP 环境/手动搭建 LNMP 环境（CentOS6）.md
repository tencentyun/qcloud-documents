## 操作场景
LNMP 环境是指在 Linux 系统下，由 Nginx + MySQL/MariaDB + PHP 组成的网站服务器架构。本文档介绍如何在腾讯云云服务器（CVM）上手动搭建 LNMP 环境。

进行手动搭建 LNMP 环境，您需要熟悉 Linux 命令，例如 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件的使用及版本兼容性比较了解。


<dx-alert infotype="notice" title="">
腾讯云建议您可以通过云市场的镜像环境部署 LNMP 环境，手动搭建 LNMP 环境可能需要较长的时间。具体步骤可参考 [镜像部署 LNMP 环境](https://cloud.tencent.com/document/product/213/38053)。
</dx-alert>




## 示例软件版本
本文搭建的 LNMP 环境软件组成版本及说明如下：
Linux：Linux 操作系统，本文以 CentOS 6.10 为例。
Nginx：Web 服务器，本文以 Nginx 1.19.5 为例。
MySQL：数据库，本文以 MySQL 5.6.24 为例。
PHP：脚本语言，本文以 PHP 5.6.23 为例。

## 前提条件
- 已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
- CentOS 6操作系统版本生命周期（EOL）于2020年11月30日结束，按照社区规则，CentOS 6的源地址 `http://mirror.centos.org/centos-6/` 内容已移除。请参考 [CentOS 6 切换 YUM 源](https://cloud.tencent.com/document/product/213/52559) 切换 YUM 源，避免在安装软件过程中出现报错。


## 操作步骤
### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)

### 步骤2：安装 Nginx
1. 执行以下命令，在 `/etc/yum.repos.d/` 下创建 `nginx.repo` 文件。
```shell
vi /etc/yum.repos.d/nginx.repo
```
2. 按 **i** 切换至编辑模式，写入以下内容。
```shell
[nginx]
name=nginx repo
baseurl=https://nginx.org/packages/mainline/centos/6/$basearch/
gpgcheck=0
enabled=1
```
3. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 执行以下命令，安装 Nginx。
```shell
yum install -y nginx
```
5. 执行以下命令，打开 `default.conf` 文件。
```shell
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
```shell
service nginx start
```
10. 依次执行以下命令，设置 Nginx 为开机自启动。
```shell
chkconfig --add nginx
```
```shell
chkconfig  nginx on
```
11. 在本地浏览器中访问以下地址，查看 Nginx 服务是否正常运行。
```shell
http://云服务器实例的公网 IP
```
显示结果如下，则说明 Nginx 安装配置成功。
![](https://main.qcloudimg.com/raw/fdc40877928729679d392eb304a3f12c.png)


### 步骤3：安装数据库
1. 依次执行以下命令，准备编译环境。
```shell
yum groupinstall "Server Platform Development"  "Development tools" -y
```
```shell
yum install cmake -y
```
2. 依次执行以下命令，准备 MySQL 数据存放目录。
  1. 新建 MySQL 数据存放目录。
```shell
mkdir /mnt/data
```
  2. 新建用户组 mysql。
```shell
groupadd -r mysql
```
  3. 新建用户 mysql。
```shell
useradd -r -g mysql -s /sbin/nologin mysql
```
  4. 查看用户是否创建成功。
```shell
id mysql
```
  4. 更改数据存放目录的属组和属主为 mysql。
```shell
chown -R mysql:mysql /mnt/data
```
3. 依次执行以下命令，下载稳定版源码包、解压并编译。
  1. 下载源码包。
```shell
wget https://dev.mysql.com/get/Downloads/mysql-5.6.24.tar.gz
```
  2. 解压源码包。
```shell
tar xvf mysql-5.6.24.tar.gz -C  /usr/local/src
``` 
  3. 进入 MySQL 源码包目录。
```shell
cd /usr/local/src/mysql-5.6.24
```
  4. 编译源码包。
```shell
cmake . -DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
-DMYSQL_DATADIR=/mnt/data \
-DSYSCONFDIR=/etc \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_ARCHIVE_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DWITH_READLINE=1 \
-DWITH_SSL=system \
-DWITH_ZLIB=system \
-DWITH_LIBWRAP=0 \
-DMYSQL_TCP_PORT=3306 \
-DMYSQL_UNIX_ADDR=/tmp/mysql.sock \
-DDEFAULT_CHARSET=utf8 \
-DDEFAULT_COLLATION=utf8_general_ci
```
```shell
make && make install
```
4. 依次执行以下命令，配置 MySQL。
  1. 修改安装目录的属组和属主为 mysql。
```shell
chown -R mysql:mysql /usr/local/mysql/
```
  2. 初始化数据库。
```shell
cd /usr/local/mysql
```
```shell
/usr/local/mysql/scripts/mysql_install_db --user=mysql --datadir=/mnt/data/
```
  3. 复制 MySQL 配置文件。
```shell
cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld
```
```shell
cp /usr/local/mysql/support-files/my-default.cnf /etc/my.cnf
```
  4. 为 MySQL 的启动脚本添加可执行权限。
```shell
chmod +x /etc/init.d/mysqld
```
  5. 添加 MySQL 至服务管理列表并设置开机自启动。
```shell
chkconfig --add mysqld
```
```shell
chkconfig mysqld  on 
```
  6. 修改配置文件中的安装路径及数据目录存放路径。
```shell
echo -e "basedir = /usr/local/mysql\ndatadir = /mnt/data\n" >> /etc/my.cnf
```
  7. 设置 PATH 环境变量。
```shell
echo "export PATH=$PATH:/usr/local/mysql/bin" > /etc/profile.d/mysql.sh      
```
```shell
source /etc/profile.d/mysql.sh
```
5. 执行以下命令，启动 MySQL。
```shell
service mysqld start 
```
6. 执行以下命令，连接 MySQL 数据库进行测试。
```shell
mysql -h 127.0.0.1
```
显示结果如下，则成功安装。
![](https://qcloudimg.tencent-cloud.cn/raw/0f88a192a066ec975264997eae6401c7.png)
6. 执行以下命令，退出 MySQL。
```shell
\q
```

### 步骤4：安装配置 PHP
1. 执行以下命令，安装依赖包。
```shell
yum install libmcrypt libmcrypt-devel mhash mhash-devel libxml2 libxml2-devel bzip2 bzip2-devel
```
2. 依次执行以下命令，下载稳定版源码包并解压、编译。
  1. 下载源码包。
```shell
wget http://cn2.php.net/get/php-5.6.23.tar.bz2/from/this/mirror
```
  2. 解压源码包。
```shell
cp mirror php-5.6.23.tar.bz2
```
```shell
tar xvf php-5.6.23.tar.bz2 -C /usr/local/src
```
  3. 进入 PHP 源码包目录。
```shell
cd /usr/local/src/php-5.6.23
```
  4. 编译源码包。
```shell
./configure --prefix=/usr/local/php \
--with-config-file-scan-dir=/etc/php.d \
--with-config-file-path=/etc \
--with-mysql=/usr/local/mysql \
--with-mysqli=/usr/local/mysql/bin/mysql_config \
--enable-mbstring \
--with-freetype-dir \
--with-jpeg-dir \
--with-png-dir \
--with-zlib \
--with-libxml-dir=/usr \
--with-openssl \
--enable-xml \
--enable-sockets \
--enable-fpm \
--with-mcrypt \
--with-bz2
```
```shell
make && make install
```
3. 依次执行以下命令，配置 PHP。 
 1. 添加 PHP 和 PHP-FPM 配置文件。
```shell
cp /usr/local/src/php-5.6.23/php.ini-production /etc/php.ini
```
```shell
cd /usr/local/php/etc/
```
```shell
cp php-fpm.conf.default php-fpm.conf
```
```shell
sed -i 's@;pid = run/php-fpm.pid@pid = /usr/local/php/var/run/php-fpm.pid@' php-fpm.conf
```
  2. 添加 PHP-FPM 启动脚本。
```shell
cp /usr/local/src/php-5.6.23/sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm
```
  3. 为 PHP-FPM 启动脚本添加可执行权限。
```shell
chmod +x /etc/init.d/php-fpm
``` 
  4. 添加 PHP-FPM 至服务列表并设置开机自启动。
```shell
chkconfig --add php-fpm  
``` 
```shell
chkconfig --list php-fpm  
``` 
```shell
chkconfig php-fpm on
``` 
5. 执行以下命令，启动 PHP-FPM 服务。
```shell
service php-fpm start
``` 


## 验证环境配置
1. 执行以下命令，创建测试文件。
```shell
echo "<?php phpinfo(); ?>" >> /usr/share/nginx/html/index.php
```
2. 执行以下命令，重启 Nginx。
```shell
service nginx restart
```
3. 在本地浏览器中访问如下地址，查看环境配置是否成功。
```shell
http://云服务器实例的公网 IP
```
显示结果如下， 则说明环境配置成功。
![](https://qcloudimg.tencent-cloud.cn/raw/3dd2ea5696afef3e03d0caa9b762e34a.png)



## 相关操作
在完成了 LNMP 环境搭建之后，您可在此基础上进行 [手动搭建 Wordpress 个人站点](https://cloud.tencent.com/document/product/213/8044) 实践，了解并掌握更多关于云服务器的相关功能。


## 常见问题

如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：

- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。

