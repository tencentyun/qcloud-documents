请确保您已按照[Ubuntu环境下通过Apt-get安装软件](http://www.qcloud.com/doc/product/213/Ubuntu%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%80%9A%E8%BF%87Apt-get%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6)的步骤进行必要软件的安装。

## 1. 配置nginx
1) 启动nginx服务

用以下命令启动nginx：
```
sudo /etc/init.d/nginx start
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

3) 在浏览器中，访问通过Ubuntu云服务器公网IP查看nginx服务是否正常运行

如果显示如下，说明nginx安装配置成功：

![](//mccdn.qcloud.com/img56af51bf21d78.png)

## 2. 配置PHP
1) 确认php的启动方式
在/etc/php5/fpm/pool.d/www.conf里 (`示例环境为ubuntu12，php5.3，不同版本 该php配置路径可能不一样`) 确认一下启动方式，使用 `listen` 搜索关键字查看，php的listen监听方法：

```
listen = /var/run/php5-fpm.sock
listen = 127.0.0.1:9000  ; 可监听上边的sock方式，若使用ip:port时，请自行添加该行
```

2) 启动php-fpm

这里ubuntu12下没做php配置修改，用以下命令启动php-fpm服务
```
sudo /etc/init.d/php5-fpm start
```

3) 修改php-fpm和nginx的配置，实现nginx和php联动

用以下命令查看php-fpm默认配置：

```
sudo netstat -tunpl | grep php-fpm
```
示例：
![](//mccdn.qcloud.com/img56b01de8b9657.png)

以上结果表明php-fpm的默认配置的监听端口为9000，现在只用修改配置，将php解析的请求转发到127.0.0.0:9000处理即可。

修改nginx配置，修改命令如下：

```
sudo vim /etc/nginx/sites-available/default
```
找到下面的内容，增加支持的文件类型，增加后如下图所示：

![](//mccdn.qcloud.com/img56b01e58b221e.png)

在配置文件的后面，写入如下内容：

```
location ~ \.php$ {
               fastcgi_pass 127.0.0.1:9000;
               #fastcgi_pass unix:/var/run/php5-fpm.sock; #根据php实际listen监听情况，自行选择php的启动方法
               fastcgi_index index.php;
               include fastcgi_params;
}
```

修改完成后，按“Esc”键，输入“:wq”，保存文件并返回。

通过下面的命令，查看配置是否正确：

```
sudo cat /etc/nginx/sites-available/default
```

## 3. 重启服务
1) 用以下命令重启php-fpm：

```
sudo /etc/init.d/php5-fpm restart
```
结果如下：

```
* Restarting PHP5 FastCGI Process Manager php5-fpm
  ...done.
```

2) 用以下命令重启nginx，使配置生效：

```
sudo /etc/init.d/nginx restart
```
结果如下：


```
Restarting nginx: nginx.
```

## 4. 环境配置验证
用以下命令在web目录下创建index.php：

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

在浏览器中，访问Ubuntu云服务器公网IP查看环境配置是否成功，如果页面可以显示“hello world”，说明配置成功。

![](//mccdn.qcloud.com/img56b01b629ad2e.png)