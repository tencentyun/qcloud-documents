LNMP 环境代表 Linux 系统下 Nginx + MySQL + PHP 网站服务器架构。本文档介绍 SUSE 下的 LNMP 环境搭建。
本文档包含软件安装内容，请确保您已熟悉软件安装方法，请参见  [SUSE 环境下通过 YaST 安装软件](doc/product/213/SUSE%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%80%9A%E8%BF%87YaST%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6) 。

## 安装配置 Nginx
1. 自动安装 Nginx。输入命令：
``` 
yum install nginx
service nginx start
chkconfig --levels 235 nginx on
```

2. 启动 Nginx 服务。输入命令：`service nginx restart `。

3. 命令行测试 Nginx 服务是否正常运行。输入命令：`wget http://127.0.0.1` 。
若服务正常，显示结果如下。
```
--2013-02-20 17:07:26-- http://127.0.0.1/
Connecting to 127.0.0.1:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 151 [text/html]
Saving to: `index.html'
100%[===================================>] 151 --.-K/s in 0s 
2013-02-20 17:07:26 (37.9 MB/s) - `index.html' saved [151/151]
```

3. 浏览器中测试 Nginx 服务是否正常运行。访问 CentOS 云服务器公网 IP。
若服务正常，显示结果如下。
![](//mc.qcloudimg.com/static/img/fce31b900d308c4a5d57b1d316574a58/image.png)

## 安装配置 MySQL
1. 安装 MySQL。输入命令：`yum install mysql mysql-server mysql-devel` 。

2. 启动 MySQL 服务。输入命令：`service mysqld start` 。

3. 登录 MySQL ，删除空用户。输入命令：
```
mysql>select user,host,password from mysql.user;
mysql>drop user ''@localhost;
``` 

4. 修改 root 密码。输入命令：
```
mysql>update mysql.user set password = PASSWORD('此处输入您新设密码') where user='root';
mysql>flush privileges;
```

## 安装配置PHP
1. 安装 PHP 。输入命令进行安装：
```
yum install php lighttpd-fastcgi php-cli php-mysql php-gd php-imap php-ldap
php-odbc php-pear php-xml php-xmlrpc php-mbstring php-mcrypt php-mssql php-snmp php-soap
```
2. 安装所需组件使 PHP 支持 MySQL、FastCGI 模式。
```
yum install  php-tidy php-common php-devel php-fpm php-mysql
```

## Nginx 与 PHP-FPM 集成
1. 新建配置文件 php-fpm.conf，输入命令：`vim /etc/php5/fpm/php-fpm.conf` 。

2. 写入以下内容：
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

3. 启动服务。输入命令：
```
/etc/init.d/mysql start 
/etc/init.d/php-fpm start 
/etc/init.d/nginx start
```
如图所示：
![](//mccdn.qcloud.com/img56b01d2fa2d5c.png)


## 环境配置验证
用以下命令在 web 目录下创建 index.php：
```
vim /usr/share/nginx/html/index.php
```
写入如下内容：
```
<?php
echo "<title>Test Page</title>";
echo "hello world";
?>
```
在浏览器中，访问 SUSE 云服务器公网 IP ，查看环境配置是否成功，如果页面可以显示“hello world”，说明配置成功。
