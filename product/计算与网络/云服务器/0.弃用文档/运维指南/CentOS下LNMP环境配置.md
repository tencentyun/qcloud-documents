LNMP 环境代表 Linux 系统下 Nginx + MySQL + PHP 网站服务器架构。本文档介绍 CentOS 下的 LNMP 环境搭建。
本文档包含软件安装内容，请确保您已熟悉软件安装方法，请参见 [CentOS 环境下通过 YUM 安装软件](/doc/product/213/CentOS%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%80%9A%E8%BF%87YUM%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6) 。

## 安装配置 Nginx
1. 自动安装 Nginx。输入命令：
``` 
yum install nginx
service nginx start
chkconfig --levels 235 nginx on
```

2. 启动 Nginx 服务。
云服务器系统版本为 CentOS 7.0 及以上，可直接启动服务。系统版本为 CentOS 7.0 以下（如 CentOS 6.8），直接启动服务会失败，需要先修改 Nginx 的配置文件。
 1. 请先检查系统版本。CentOS 7.0 以下版本进行第 ii 步，CentOS 7.0 及以上版本进行第 iii 步。输入命令：
```
cat /etc/redhat-release
```
 2. 确定系统版本在 CentOS 7.0 以下后，修改 /etc/nginx/conf.d 下的 default.conf 文件，注释掉 [::]:80 配置行。
     - 注释前：
![](https://main.qcloudimg.com/raw/92464436c50f491e5af651c81da6a4ea.png)
     - 注释后：
![](https://main.qcloudimg.com/raw/6658bdfba8e32507a04e0e9dfd4428ff.png)
 3. 启动 Nginx 服务
```
service nginx restart 
```
 
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

4. 浏览器中测试 Nginx 服务是否正常运行。访问 CentOS 云服务器公网 IP。
若服务正常，显示结果如下。
![](//mc.qcloudimg.com/static/img/fce31b900d308c4a5d57b1d316574a58/image.png)

## 安装配置 MySQL
>**注意：**
从 CentOS 7 系统开始，MariaDB 成为 yum 源中默认的数据库安装包。在 CentOS 7 及以上的系统中使用 yum 安装 MySQL 包将无法使用 MySQL。您可以选择使用完全兼容的 MariaDB，或自行安装较低版本的 MySQL。

1. 安装 MySQL。输入以下命令：
 - 适用于 CentOS 7.0 或以后版本：
```
yum install mariadb mariadb-server
```
 -  适用于 CentOS 6.8 或以前版本：
```
yum install mysql mysql-server mysql-devel
```	

2. 启动 MySQL 服务。输入命令：
 - 适用于 CentOS 7.0 或以后版本：
```
systemctl start mariadb.service
```
 - 适用于 CentOS 6.8 或以前版本：
```
service mysqld start
```
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

## 安装配置 PHP
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
1. 启动 PHP-FPM。输入命令启动 PHP-FPM 服务：`service php-fpm start` 。

2. 输入命令查看 PHP-FPM 默认配置：`cat /etc/php-fpm.d/www.conf |grep -i 'listen ='`
返回结果为：`listen = 127.0.0.1:9000`，表明 PHP-FPM 默认配置的监听端口为 9000，只需修改配置，将 PHP 解析的请求转发到 127.0.0.0:9000 处理即可。

3. 修改 Nginx 配置。
输入命令查找 Nginx 配置文件：`nginx -t`
使用`vi`命令修改该配置文件：
![](//mccdn.qcloud.com/static/img/43addfa0593b6daa1fb19f957dad1425/image.png)
在配置文件中找到以下片段，修改红色部分：

<div class="code">
<pre>  
server {
 <font color="red"> listen       80;</font>
  <font color="red">root   /usr/share/nginx/html;</font>
 <font color="red"> server_name  localhost;</font>
  #charset koi8-r;
  #access_log  /var/log/nginx/log/host.access.log  main;
  <font color="red">location / {
      index  index.html index.htm;
  }</font>
  #error_page  404              /404.html;
  # redirect server error pages to the static page /50x.html
  #
  error_page   500 502 503 504  /50x.html;
  location = /50x.html {
      root   /usr/share/nginx/html;
  }
  # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
  #
  <font color="red">location ~ \.php$ {
      fastcgi_pass   127.0.0.1:9000;
      fastcgi_index   index.php;
      fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
      include        fastcgi_params;
  }</font>
}
</pre>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;4\. 修改完成后，按“ Esc ”键，输入“ :wq ”，保存文件并返回。

&nbsp;&nbsp;&nbsp;&nbsp;5\. 查看配置是否正确。输入命令：`cat /etc/nginx/nginx.conf` 。

&nbsp;&nbsp;&nbsp;&nbsp;6\. 配置完成后，重启服务。输入命令：`service nginx restart` 。

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

在浏览器中，访问 CentOS 云服务器公网 IP ，查看环境配置是否成功。如果页面可以显示“hello world”，说明配置成功。
