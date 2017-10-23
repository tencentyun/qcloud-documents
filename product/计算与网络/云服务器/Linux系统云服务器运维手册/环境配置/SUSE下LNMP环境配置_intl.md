Make sure that you have followed the steps in [Installing Software via YAST in SUSE Environment](http://cloud.tencent.com/doc/product/213/SUSE%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%80%9A%E8%BF%87YaST%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6) install the necessary software.
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
1) Create a new configuration file php-fpm.conf with the following command:

```
vim /etc/php5/fpm/php-fpm.conf
```
Write the following:

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

## 3. Start services
Start all services with the following commands:

```
/etc/init.d/mysql start; /etc/init.d/php-fpm start; /etc/init.d/nginx start
```

Example:

![](//mccdn.qcloud.com/img56b01d2fa2d5c.png)


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

In the browser, visit the Public IP of SUSE CVM to check whether the environment configuration is successful. If the webpage shows "hello world", it means the configuration is successful.
