- As Layer-4 cloud load balance (TCP protocol) can directly access the real IP address of the visitor on the backend CVM, and no additional configuration is required. The following description is only for Layer-7 (HTTP protocol) cloud load balance.
- Layer-7 cloud load balance system provides X-Forwarded-For method to obtain the visitor's real IP, which is enabled by default.

The common options for application server configuration are described below.

## 1. IIS 6 Configuration Option
1) Install the plugin F5XForwardedFor.dll. Copy `F5XForwardedFor.dll` under the x86\Release or x64\Release directory to a specific directory according to your own server operating system version, which is assumed to be `C:\ISAPIFilters` here. In addition, you should ensure that the IIS process has read access to the directory.

2) Open the IIS manager, find the currently opened site, right-click on the site to select "Properties" and open the property page.

3) In the property page, go to "ISAPI Filter" and click "Add" button. The "Add" window will appear.

4) In the "Add" window, fill in "F5XForwardedFor" for "Filter Name", and the full path of `F5XForwardedFor.dll` for "Executable File" and then click OK.

5) Restart IIS server, waiting for the configuration to take effect.

## 2. IIS 7 Configuration Option
1) Download and install the plugin F5XForwardedFor module. Copy `F5XFFHttpModule.dll` and `F5XFFHttpModule.ini` under `x86\Release` or `x64\Release` directory to a specific directory according to your own server operating system version, which is assumed to be `C:  \F5XForwardedFor` here. Make sure that the IIS process has read access to the directory.

2) Select "IIS Server" option, and select the "Module" function as shown in the figure:
![](//mccdn.qcloud.com/static/img/9d7e43382b6b2bdf5753b67ccd248030/image.png)

3) Double-click the "Module" function, and click "Configure Local Module":
![](//mccdn.qcloud.com/static/img/01620ccc1be3c03569b31dc8bbaa7d73/image.png)

4) Click the "Register" button in the pop-up box:
![](//mccdn.qcloud.com/static/img/27fd429c05788abbdc6e95adc215e39c/image.png)

5) Add the downloaded DLL file, as shown below:
![](//mccdn.qcloud.com/static/img/9e68ee04ef61c911a8dcc7caaf77b678/image.png)

6) After the file is added, check it and click "OK":
![](//mccdn.qcloud.com/static/img/c9bf9c597d7c0b2538dade72ed10bd4e/image.png)

7) Add these two DLLs to "API and CGI Restrictions" and change their setting to "allow":
![](//mccdn.qcloud.com/static/img/bccab999282e71a49aeb144a4dc3c9ed/image.png)

8) Restart the IIS server, waiting for the configuration to take effect.

## 3. Apache Configuration Option
1) Install apache third party module "mod_rpaf" 


```
wget http://stderr.net/apache/rpaf/download/mod_rpaf-0.6.tar.gz
tar zxvf mod_rpaf-0.6.tar.gz
cd mod_rpaf-0.6
/usr/bin/apxs -i -c -n mod_rpaf-2.0.so mod_rpaf-2.0.c
```


2) Modify the apache configuration`/etc/httpd/conf/httpd.conf`, and add at the end:

```
LoadModule rpaf_module modules/mod_rpaf-2.0.so
RPAFenable On
RPAFsethostname On
RPAFproxy_ips ip address (this ip address is not the public network ip provided by the cloud load balancer, and the specific ip addresses can be viewed in the apache log. Usually, there are two, both of which should be added)
RPAFheader X-Forwarded-For
```

3) Restart apache after completing the adding

```
/usr/sbin/apachectl restart
```

## 4. Nginx Configuration Option
1) As cloud load balancer, Nginx uses http_realip_module to get real ip; since the default installation for Nginx does not include this module, you need to recompile Nginx to add --with-http_realip_module:

```
wget http://soft.phpwind.me/top/nginx-1.0.12.tar.gz
tar zxvf nginx-1.0.12.tar.gz
cd nginx-1.0.12
./configure --user=www --group=www --with-http_stub_status_module --without-http-cache --with-http_ssl_module --with-http_realip_module
make
make install
```

2) Modify nginx.conf
```
vi /etc/nginx/nginx.conf
```

Modify the following red parts:
<div class="code">
<p>
</p>
<pre>  
fastcgi connect_timeout 300;
fastcgi send_timeout 300;
fastcgi read_timeout 300;
fastcgi buffer_size 64k;
fastcgi buffers 4 64k;
fastcgi busy_buffers_size 128k;
fastcgi temp_file_write_size 128k;
<font color="red">
set_real_ip_from ip address; (this ip address is not the public network ip provided by the cloud load balancer, and the specific ip address can be viewed in previous nginx log. If there are more than one, all of them should be added.)
Real_ip_header X-Forwarded-For;
 </font>


</pre>

</div>

3) Restart nginx

```
service nginx restart
```



