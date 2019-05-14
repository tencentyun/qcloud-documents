- 由于4层负载均衡（TCP协议）服务可以直接在后端CVM上获取来访者真实IP地址，无需进行额外的配置，以下介绍的内容均是针对7层（HTTP协议）的负载均衡服务而言。
- 7层负载均衡系统提供X-Forwarded-For的方式获取访问者真实IP，默认开启。

以下针对常见的应用服务器配置方案进行介绍。

## IIS 6 配置方案
1) 安装插件F5XForwardedFor.dll，根据自己的服务器操作系统版本将x86\Release或者x64\Release目录下的`F5XForwardedFor.dll`拷贝到某个目录，这里假设为`C:\ISAPIFilters`，同时确保对IIS进程对该目录有读取权限。

2) 打开IIS管理器，找到当前开启的网站，在该网站上右键选择“属性”，打开属性页。

3) 在属性页切换至“ISAPI筛选器”，点击“添加”按钮，出现添加窗口。

4) 在添加窗口“筛选器名称”填写“F5XForwardedFor”，“可执行文件”填写`F5XForwardedFor.dll`的完整路径，点击确定。

5) 重启IIS服务器，等待配置生效。

## IIS 7 配置方案
1) 下载与安装插件F5XForwardedFor模块，根据自己的服务器操作系统版本将`x86\Release`或者`x64\Release`目录下的`F5XFFHttpModule.dll`和`F5XFFHttpModule.ini`拷贝到某个目录，这里假设为`C: \F5XForwardedFor`，确保对IIS进程对该目录有读取权限。

2) 选择“IIS服务器”选项，按图所示选择“模块”功能：
![](//mccdn.qcloud.com/static/img/9d7e43382b6b2bdf5753b67ccd248030/image.png)

3) 双击“模块”功能，点击“配置本机模块”：
![](//mccdn.qcloud.com/static/img/01620ccc1be3c03569b31dc8bbaa7d73/image.png)

4) 在弹出框中点击“注册”按钮：
![](//mccdn.qcloud.com/static/img/27fd429c05788abbdc6e95adc215e39c/image.png)

5) 添加下载的DLL文件，如下图：
![](//mccdn.qcloud.com/static/img/9e68ee04ef61c911a8dcc7caaf77b678/image.png)

6) 添加完成后，勾选并点击“确定”：
![](//mccdn.qcloud.com/static/img/c9bf9c597d7c0b2538dade72ed10bd4e/image.png)

7) 把这两个DLL在 “API 和CGI限制”进行添加，并改为允许：
![](//mccdn.qcloud.com/static/img/bccab999282e71a49aeb144a4dc3c9ed/image.png)

8) 重启IIS服务器，等待配置生效。

## Apache配置方案
1) 安装apache第三方模块“mod_rpaf” 


```
wget http://stderr.net/apache/rpaf/download/mod_rpaf-0.6.tar.gz
tar zxvf mod_rpaf-0.6.tar.gz
cd mod_rpaf-0.6
/usr/bin/apxs -i -c -n mod_rpaf-2.0.so mod_rpaf-2.0.c
```


2) 修改apache配置`/etc/httpd/conf/httpd.conf`，在最末尾添加：

```
LoadModule rpaf_module modules/mod_rpaf-2.0.so
RPAFenable On
RPAFsethostname On
RPAFproxy_ips ip地址（这个ip地址首先不是负载均衡提供的公网ip，具体ip多少可以看一下apache日志，通常会有2个 都要写上）
RPAFheader X-Forwarded-For
```

3) 添加完成后重启apache

```
/usr/sbin/apachectl restart
```

## Nginx配置方案
1) Nginx作为负载均衡获取真实ip是使用http_realip_module，默认安装的Nginx是没有安装这个模块的，需要重新编译Nginx增加 --with-http_realip_module：

```
wget http://soft.phpwind.me/top/nginx-1.0.12.tar.gz
tar zxvf nginx-1.0.12.tar.gz
cd nginx-1.0.12
./configure --user=www --group=www --with-http_stub_status_module --without-http-cache --with-http_ssl_module --with-http_realip_module
make
make install
```

2) 修改nginx.conf
```
vi /etc/nginx/nginx.conf
```

修改如下红色部分：
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
set_real_ip_from ip地址;（这个ip地址首先不是负载均衡提供的公网ip，具体ip多少可以看一下之前nginx日志，如果有多个都要写上。）
set_real_ip_from ip地址;（这个ip地址首先不是负载均衡提供的公网ip，具体ip多少可以看一下之前nginx日志，如果有多个都要写上。）
real_ip_header X-Forwarded-For;
 </font>


</pre>

</div>

3) 重启nginx

```
service nginx restart
```


