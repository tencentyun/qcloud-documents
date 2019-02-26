LNMP 环境代表 Linux 系统下 Nginx + MySQL + PHP 网站服务器架构。本文档介绍 Ubuntu 下的 LNMP 环境搭建。
本文档包含软件安装内容，请确保您已熟悉软件安装方法，请参见 [Ubuntu 环境下通过 Apt-get 安装软件](/doc/product/213/Ubuntu%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%80%9A%E8%BF%87Apt-get%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6) 。

## 安装配置 Nginx
1. 自动安装 Nginx。输入命令：` sudo apt-get install nginx `。为了确保获得最新的 Nginx，可以先使用 `sudo apt-get update `命令更新源列表。
1. 启动 Nginx 服务。输入命令：`sudo /etc/init.d/nginx start`

2.  命令行中测试 Nginx 服务是否正常运行。输入命令：`wget http://127.0.0.1`
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

3. 浏览器中测试 Nginx 服务是否正常运行。访问 Ubuntu 云服务器公网 IP。
若服务正常，显示结果如下。
![](//mc.qcloudimg.com/static/img/fce31b900d308c4a5d57b1d316574a58/image.png)

## 安装配置 MySQL
1. 安装 MySQL。输入命令：`sudo apt-get –y install MySQL-server mysql-client php7.1-mysql` 。

2. 设置 root 用户密码。安装过程中将会让您设置密码。

3. 端口查看。安装完成后，输入命令：`netstat -anp` ，会发现  3306 端口正在被监听，此时已可以编写 PHP 脚本来连接数据库。


## 安装配置 PHP
1. 安装 PHP 。输入命令进行安装：
```
sudo apt-add-repository ppa:ondrej/php
sudo apt-get update
sudo apt-get install php7.1 php7.1-fpm
```
>注意：
>直接运行 `sudo apt-get `命令安装 PHP 会报错误，原因是 PHP7 等并不在 Ubuntu 的软件库中，因此要使用 PPA ppa:ondrej/php 库。
1. 确认 PHP 启动方式。在`/etc/php7.1/fpm/pool.d/www.conf`路径里确认启动方式，使用 `listen` 搜索关键字查看 PHP 的 listen 监听方法。 
```
listen = /var/run/php7.1-fpm.sock
listen = 127.0.0.1:9000 ; 可监听上边的 sock 方式，若使用 ip:port 时，请自行添加该行
```
>**注意：**
>示例环境为 Ubuntu 12，不同版本 PHP 配置路径可能不一样。

## Nginx 与 PHP-FPM 集成
2. 启动 PHP-FPM。输入命令启动 PHP-FPM 服务：`sudo /etc/init.d/php7.1-fpm start` 。

3. 输入命令查看 PHP-FPM 默认配置：`sudo netstat -tunpl | grep php-fpm`，如下图。
![](//mccdn.qcloud.com/img56b01de8b9657.png)
以上结果表明 PHP-FPM 默认配置的监听端口为 9000，只需修改配置，将 PHP 解析的请求转发到 127.0.0.0:9000 处理即可。

4. 修改 Nginx 配置。输入修改命令：`sudo vim /etc/nginx/sites-available/default` 。
找到下面的内容。
![](//mccdn.qcloud.com/img56b01e58b221e.png)
在配置文件的后面，写入如下内容：
```
location ~ \.php$ {
               fastcgi_pass 127.0.0.1:9000;
               #fastcgi_pass unix:/var/run/php7.1-fpm.sock; #根据php实际listen监听情况，自行选择php的启动方法
               fastcgi_index index.php;
               include fastcgi_params;
}
```

5. 修改完成后，按“ Esc ”键，输入“ :wq ”，保存文件并返回。

6. 查看配置是否正确。输入命令：`sudo cat /etc/nginx/sites-available/default` 。

7. 配置完成后，重启服务。输入命令：
```
sudo /etc/init.d/nginx restart 
sudo /etc/init.d/php7.1-fpm restart
```

## 环境配置验证
用以下命令在 web 目录下创建 index.php：
```
sudo vim /usr/share/nginx/www/index.php
```
写入如下内容：
```
<?php
echo "<title>Test Page</title>";
echo "hello world";
?>
```
在浏览器中，访问 Ubuntu 云服务器公网 IP ，查看环境配置是否成功。如果页面可以显示“ hello world ”，说明配置成功。
