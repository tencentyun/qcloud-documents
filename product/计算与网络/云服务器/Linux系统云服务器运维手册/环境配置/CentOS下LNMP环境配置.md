请确保您已按照[CentOS环境下通过YUM安装软件](http://www.qcloud.com/doc/product/213/CentOS%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%80%9A%E8%BF%87YUM%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6)的步骤进行必要软件的安装。
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
1) 启动php-fpm

用以下命令启动php-fpm服务
```
service php-fpm start
```

2) 修改php-fpm和nginx的配置，实现nginx和php联动

用以下命令查看php-fpm默认配置：

```
cat /etc/php-fpm.d/www.conf |grep -i 'listen ='
```
返回结果为：

```
listen = 127.0.0.1:9000
```
以上结果表明php-fpm的默认配置的监听端口为9000，现在只用修改配置，将php解析的请求转发到127.0.0.0：9000处理即可。

使用以下命令查找nginx配置文件：

```
nginx -t
```
并使用`vi`命令修改该配置文件：
![](//mccdn.qcloud.com/static/img/43addfa0593b6daa1fb19f957dad1425/image.png)

在配置文件中找到以下片段，修改红色部分。

<div class="code">
<p>
</p>
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

修改完成后，按“Esc”键，输入“:wq”，保存文件并返回。

通过下面的命令，查看配置是否正确：

```
cat /etc/nginx/nginx.conf
```

## 3. 重启服务
用以下命令重启nginx，使配置生效：

```
service nginx restart
```
结果如下：

```
Stopping nginx: [ OK ]
Starting nginx: [ OK ]
```

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

在浏览器中，访问CentOS云服务器公网IP查看环境配置是否成功，如果页面可以显示“hello world”，说明配置成功。
![](//mccdn.qcloud.com/static/img/eaf3dc9799b156e706225c3687f0ae60/image.png)