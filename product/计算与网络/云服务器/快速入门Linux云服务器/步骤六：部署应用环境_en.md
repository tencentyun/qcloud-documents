This document describes the basic software installation and environment configuration in several Linux environments. You can choose whether to install the software as needed. <font color="red">It is not necessary for beginners to perform all of the following steps. Please determine the purpose of the server before performing relevant configuration. </font>You can also start the CVM by acquiring images from Service Marketplace. Many of the images from Service Marketplace have been integrated with the necessary services, eliminating your efforts in installation and configuration. For details, please see [Service Market](http://market.qcloud.com/?categoryId=64&page=1&orderby=2).

CentOS 7.1 64 bit is taken as an example to illustrate the processes throughout the document.

## 1. Install and start nginx
Enter the command `yum install nginx` to install nginx, and enter "y" to confirm when required.
![](//mccdn.qcloud.com/static/img/61147e054115619d36e6905673152e90/image.png)
![](//mccdn.qcloud.com/static/img/794e597a0e98fee3a01b1a84723d2f9f/image.png)

Enter `service nginx start` to start nginx service.
![](//mccdn.qcloud.com/static/img/e3119ba3fcb6e4d47073fd15314be999/image.png)

Enter `wget http://127.0.0.1` to test nginx service.
![](//mccdn.qcloud.com/static/img/0bb46762a9fe83ccd465d84000d559c3/image.png)

## 2. Install PHP and corresponding components
Enter the command `yum install php php-fpm` to install PHP and enter "y" to confirm when required.
![](//mccdn.qcloud.com/static/img/ec8844bef38f70027a97143a688f2dfc/image.png)
![](//mccdn.qcloud.com/static/img/5c2039fd3cc49c6e6956780bc08e47d7/image.png)

Enter `service php-fpm start` to start php-fpm service, and use the command `cat /etc/php-fpm.d/www.conf |grep -i 'listen ='` to view php-fpm configuration.
![](//mccdn.qcloud.com/static/img/8be48384350b88c1a2f46a4d6ce8a773/image.png)
![](//mccdn.qcloud.com/static/img/8f44a5ab11d6c6dd600b4fae0940d00f/image.png)

The above figure shows that the listener port of php-fpm by default is 9000. Now, you only need to modify the configuration and forward the request parsed by php to 127.0.0.0: 9000.

Use the command `nginx -t` to find the configuration file nginx, and use the command `vi` to modify this configuration file:
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

Save after modification, and enter `service nginx restart` to restart nginx service.

Create index.php under a web directory:

```
vi /usr/share/nginx/html/index.php
```

Write the following:

```
<?php
echo "<title>Test Page</title>";
echo "hello world";
?>
```

In the browser, visit the webpage named with Public IP of CentOS CVM + php to check whether the environment configuration is successful. If the webpage shows "hello world", it means the configuration is successful.
![](//mccdn.qcloud.com/static/img/eaf3dc9799b156e706225c3687f0ae60/image.png)
If you fail to access this webpage, check if your server is configured with any security group that prevents you from accessing the port.

## 3. Use Filezilla to upload files from local Windows system to Linux server and to download files from Linux server
This method only works for users who use a Windows system locally and can be used to upload local files to Linux server and to download files from Linux server. Users who use a Linux system locally can simply use the SCP command to upload and download files.

To install the Filezilla client locally, refer to the download link: https: //www.filezilla.cn/download/client

Click "File" - "Site Manager", click the "New Site" button and enter the following information:
![](//mccdn.qcloud.com/static/img/58132d70663ac9ce5169462eb9ccb944/image.png)

- Host Name: Public IP of the Linux CVM
- Port: remote connection port, which is 22 by default
- Protocol: select "SFTP" (SSH File Transfer Protocol)
- Login type: select "Normal"
- User: login user of the Linux CVM, which is root/ubuntu by default
- Password: the login password of Linux CVM

Click the "Connect" button and wait until the Linux CVM is connected.
![](//mccdn.qcloud.com/static/img/6653190a5e08b34c83d1f3d9ed9a84f6/image.png)

Once connected, you will see local files on the left and server-side files on the right.
When you need to upload local files to the server, right click on the files to upload on the left and click the "Upload" button to upload files to the server file directory on the right;
When you need to download server files to the local system, right click on the files to download on the right and click the "Download" button to download the files to local file directory on the left;