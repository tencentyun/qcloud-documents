## 操作场景
LNMP 环境代表 Linux 系统下 Nginx + MySQL + PHP 网站服务器架构。本文档介绍 openSUSE 下的 LNMP 环境搭建。
本文档包含软件安装内容，请确保您已熟悉软件安装方法。具体操作请参见  [openSUSE 环境下通过 YaST 安装软件](https://cloud.tencent.com/document/product/213/2047)。

## 前提条件
已登录 Linux 服务器。

## 操作步骤
### 安装和配置 Nginx
1. 执行以下命令，自动安装 Nginx。
``` 
yum install nginx
service nginx start
chkconfig --levels 235 nginx on
```
2. 执行以下命令，启动 Nginx 服务。
```
service nginx restart
```
3. 执行以下命令，测试 Nginx 服务是否正常运行。
```
wget http://127.0.0.1
```
若服务正常，显示结果如下：
```
--2013-02-20 17:07:26-- http://127.0.0.1/
Connecting to 127.0.0.1:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 151 [text/html]
Saving to: `index.html'
100%[===================================>] 151 --.-K/s in 0s 
2013-02-20 17:07:26 (37.9 MB/s) - `index.html' saved [151/151]
```
4. 打开浏览器，并访问 CentOS 云服务器公网 IP，测试 Nginx 服务是否正常运行。
若服务正常，显示结果如下：
![](//mc.qcloudimg.com/static/img/fce31b900d308c4a5d57b1d316574a58/image.png)

### 安装和配置 MySQL
1. 执行以下命令，安装 MySQL。
```
yum install mysql mysql-server mysql-devel
```
2. 执行以下命令，启动 MySQL 服务。
```
service mysqld start
```
3. 执行以下命令，登录 MySQL。
```
mysql -uroot -p
```
4. 执行以下命令，删除空用户。
```
mysql>select user,host,password from mysql.user;
mysql>drop user ''@localhost;
``` 
5. 执行以下命令，修改 root 密码。
```
mysql>update mysql.user set password = PASSWORD('此处输入您新设密码') where user='root';
mysql>flush privileges;
```

### 安装和配置 PHP
1. 执行以下命令，安装 PHP 。
```
yum install php lighttpd-fastcgi php-cli php-mysql php-gd php-imap php-ldap
php-odbc php-pear php-xml php-xmlrpc php-mbstring php-mcrypt php-mssql php-snmp php-soap
```
2. 执行以下命令，安装所需组件，使 PHP 支持 MySQL、FastCGI 模式。
```
yum install  php-tidy php-common php-devel php-fpm php-mysql
```

### Nginx 和 PHP-FPM 集成
1. 执行以下命令，新建配置文件 php-fpm.conf。
```
vim /etc/php5/fpm/php-fpm.conf
```
2. 将以下内容写入新建的 php-fpm.conf 配置文件中。
```
[global]
error_log = /var/log/php-fpm.log
[www]
user = nobody
group = nobody
listen = 127.0.0.1:9000
pm = dynamic
pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3
```
3. 执行以下命令，启动服务。
```
/etc/init.d/mysql start 
/etc/init.d/php-fpm start 
/etc/init.d/nginx start
```
如下图所示：
![](//mccdn.qcloud.com/img56b01d2fa2d5c.png)

### 环境配置和验证
1. 在 web 目录下，执行以下命令，创建 index.php 文件。
```
vim /usr/share/nginx/html/index.php
```
2. 将以下内容写入新建的  index.php 文件中。
```
<?php
echo "<title>Test Page</title>";
echo "hello world";
?>
```
3. 在浏览器中，访问 openSUSE 云服务器公网 IP，查看环境配置是否成功。
如果页面可以显示“hello world”，则说明配置成功。
