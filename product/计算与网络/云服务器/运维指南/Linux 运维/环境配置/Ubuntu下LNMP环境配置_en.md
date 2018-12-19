Make sure that you have followed the steps in [Installing Software via Apt-get in Ubuntu Environment](http://cloud.tencent.com/doc/product/213/Ubuntu%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%80%9A%E8%BF%87Apt-get%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6) to install the necessary software.

## 1. Configuration of nginx
1) Start nginx service

Start the nginx with the following command:
```
sudo /etc/init.d/nginx start
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

3) In the browser, visit the Public IP of Ubuntu CVM to check if nginx service is working properly.

The appearance of the following page indicates that nginx has been installed and configured successfully:

![](//mccdn.qcloud.com/img56af51bf21d78.png)

## 2. Configuration of PHP
1) Confirm the starting mode of php
Confirm the starting mode in /etc/php5/fpm/pool.d/www.conf (The example environment is ubuntu12, php5.3, and the php configuration path may vary with different versions), and check the listener method of php by searching with the keyword listen:

```
listen = /var/run/php5-fpm.sock
Listen = 127.0.0.1:9000; can listen into the sock method above, and please add the line separately when using ip:port
```

2) Start php-fpm

Here, no configuration modifications are made to php under ubuntu12. Use the following command to start php-fpm service:
```
sudo /etc/init.d/php5-fpm start
```

3) Modify the configurations of php-fpm and nginx to achieve the linkage between nginx and php.

View the php-fpm default configuration using the following command:

```
sudo netstat -tunpl | grep php-fpm
```
Example:
![](//mccdn.qcloud.com/img56b01de8b9657.png)

The above result suggests that the listener port of php-fpm by default is 9000. Now, you only need to modify the configuration and forward the request parsed by php to 127.0.0.0: 9000.

Modify the configuration of nginx with the following command:

```
sudo vim /etc/nginx/sites-available/default
```
Locate the following contents, and add supported file type. After addition, it is shown as follows:

![](//mccdn.qcloud.com/img56b01e58b221e.png)

Enter the following content at the end of the configuration file:

```
location ~ \.php$ {
               fastcgi_pass 127.0.0.1:9000;
               #Fastcgi_pass unix:/var/run/php5-fpm.sock; # select the starting mode of php based on the actual listening result of php
               fastcgi_index index.php;
               include fastcgi_params;
}
```

After modification, press "Esc" key and enter ":wq", save the file and then return.

Check whether the configuration is correct using the following command:

```
sudo cat /etc/nginx/sites-available/default
```

## 3. Restart the service
1) Use the following command to restart php-fpm:

```
sudo /etc/init.d/php5-fpm restart
```
The results are as follows:

```
* Restarting PHP5 FastCGI Process Manager php5-fpm
  ...done.
```

2) Restart nginx using the following command to make the configuration effective:

```
sudo /etc/init.d/nginx restart
```
The results are as follows:


```
Restarting nginx:  nginx.
```

## 4. Environment configuration validation
Create index.php under a web directory using the following command:

```
sudo vim /usr/share/nginx/www/index.php
```
Write the following:

```
<?php
echo "<title>Test Page</title>";
echo "hello world";
?>
```

In the browser, visit the Public IP of Ubuntu CVM to check whether the environment configuration is successful. If the webpage shows "hello world", it means the configuration is successful.

![](//mccdn.qcloud.com/img56b01b629ad2e.png)