请确保您已按照[SUSE环境下通过YaST安装软件](http://www.qcloud.com/doc/product/213/SUSE%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%80%9A%E8%BF%87YaST%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6)的步骤进行必要软件的安装。
## 1. 配置nginx
1) 启动nginx服务

用以下命令启动nginx：
```
 service nginx restart
```

2) 测试nginx服务是否正常运行

用以下命令测试：
```
wget http://127.0.0.1
```
若结果如下，最后显示" 'index.html' saved "，说明nginx服务正常。

```
--2013-02-20 17:07:26-- http://127.0.0.1/
Connecting to 127.0.0.1:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 151 [text/html]
Saving to: `index.html'
100%[==========================================================================================>] 151 --.-K/s in 0s 
2013-02-20 17:07:26 (37.9 MB/s) - `index.html' saved [151/151]
```

3) 在浏览器中，访问通过CentOS云服务器公网IP查看nginx服务是否正常运行

如果显示如下，说明nginx安装配置成功：

![](//mccdn.qcloud.com/img56af51bf21d78.png)

## 2. 配置PHP
1) 新建一个配置文件php-fpm.conf，命令如下：

```
vim /etc/php5/fpm/php-fpm.conf
```
写入以下内容：

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

## 3. 启动服务
用以下命令启动所有服务：

```
/etc/init.d/mysql start; /etc/init.d/php-fpm start; /etc/init.d/nginx start
```

示例：

![](//mccdn.qcloud.com/img56b01d2fa2d5c.png)


## 4. 环境配置验证
用以下命令在web目录下创建index.php：

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

在浏览器中，访问SUSE云服务器公网IP查看环境配置是否成功，如果页面可以显示“hello world”，说明配置成功。

![](//mccdn.qcloud.com/img56b01b629ad2e.png)