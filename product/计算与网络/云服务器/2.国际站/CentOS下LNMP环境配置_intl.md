Make sure that you have followed the steps in [Installing Software via YUM in CentOS Environment](http://cloud.tencent.com/doc/product/213/CentOS%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%80%9A%E8%BF%87YUM%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6) to install the necessary software.
## 1. Configuration of nginx
1) Start nginx service

Start the nginx with the following command:
```
 service nginx restart
```

2) Test whether nginx service is working properly

Test with the following command:
```
wget http://127.0.0.1
```
If the result is as shown below and displays "'index.html' saved" at the end, it means the nginx service is working properly.

```
--2013-02-20 17:07:26-- http://127.0.0.1/
Connecting to 127.0.0.1:80... connected.
HTTP request sent, awaiting response... 200 OK
Length:  151 [text/html]
Saving to:  'index.html'
100%[==========================================================================================>] 151 --.-K/s in 0s 
2013-02-20 17:07:26 (37.9 MB/s) - 'index.html' saved [151/151]
```

3) In the browser, visit the Public IP of CentOS CVM to check if the nginx service is working properly.

The appearance of the following page indicates that nginx has been installed and configured successfully.

## 2. Configuration of PHP
2) Start php-fpm

Start php-fpm service with the following command
```
service php-fpm start
```

2) Modify the configurations of php-fpm and nginx to achieve the linkage between nginx and php.

View the php-fpm default configuration using the following command:

```
cat /etc/php-fpm.d/www.conf |grep -i 'listen ='
```
Returned results are:

```
listen = 127.0.0.1:9000
```
The above result suggests that the listener port of php-fpm by default is 9000. Now, you only need to modify the configuration and forward the request parsed by php to 127.0.0.0: 9000.

Use the following command to find nginx configuration file:

```
nginx -t
```
And use vi command to modify the configuration file:
![](//mccdn.qcloud.com/static/img/43addfa0593b6daa1fb19f957dad1425/image.png)

Locate the following segment in the configuration file and modify the red part.

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

After modification, press "Esc" key and enter ":wq", save the file and then return.

Check whether the configuration is correct using the following command:

```
cat /etc/nginx/nginx.conf
```

## 3. Restart the service
Restart nginx using the following command to make the configuration effective:

```
service nginx restart
```
The results are as follows:

```
Stopping nginx:  [ OK ]
Starting nginx:  [ OK ]
```

## 4. Environment configuration validation
Create index.php under a web directory using the following command:

```
vim /usr/share/nginx/html/index.php
```
Write the following:

```
<?php
echo "<title>Test Page</title>";
echo "hello world";
?>
```

In the browser, visit the Public IP of CentOS CVM to check whether the environment configuration is successful. If the webpage shows "hello world", it means the configuration is successful.
![](//mccdn.qcloud.com/static/img/eaf3dc9799b156e706225c3687f0ae60/image.png)
