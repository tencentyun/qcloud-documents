- 由于4层负载均衡（TCP 协议）服务可以直接在后端 CVM 获取来访者真实 IP 地址，无需进行额外的配置，下文介绍的均是7层（HTTP 协议）的负载均衡服务的相关内容。
- 7层负载均衡系统提供 X-Forwarded-For 的方式获取访问者真实 IP，LB 侧默认开启，需要后端服务做相应配置来获取 client IP。

下文将对常见的应用服务器配置方案进行介绍。

## IIS 6 配置方案
1. 安装插件 F5XForwardedFor.dll，根据自己的服务器操作系统版本将`x86\Release`或者`x64\Release`目录下的`F5XForwardedFor.dll`拷贝到某个目录，这里假设为`C:\ISAPIFilters`，同时确保对 IIS 进程对该目录有读取权限。
2. 打开 IIS 管理器，找到当前开启的网站，在该网站上右键选择【属性】，打开属性页。
3. 在属性页切换至【ISAPI筛选器】，单击【添加】，弹出添加窗口。
4. 在添加窗口“筛选器名称”中填写“F5XForwardedFor”，“可执行文件”填写`F5XForwardedFor.dll`的完整路径，单击【确定】。
5. 重启 IIS 服务器，等待配置生效。

## IIS 7 配置方案
1. 下载与安装插件 F5XForwardedFor 模块，根据自己的服务器操作系统版本将`x86\Release`或者`x64\Release`目录下的`F5XFFHttpModule.dll`和`F5XFFHttpModule.ini`拷贝到某个目录，这里假设为`C: \F5XForwardedFor`，确保对 IIS 进程对该目录有读取权限。
2. 选择【IIS服务器】选项，选择【模块功能】。
![](//mccdn.qcloud.com/static/img/9d7e43382b6b2bdf5753b67ccd248030/image.png)
3. 双击【模块】功能，单击【配置本机模块】。
![](//mccdn.qcloud.com/static/img/01620ccc1be3c03569b31dc8bbaa7d73/image.png)
4. 在弹出框中单击【注册】。
![](//mccdn.qcloud.com/static/img/27fd429c05788abbdc6e95adc215e39c/image.png)
5. 添加下载的 DLL 文件，如下图所示：
![](//mccdn.qcloud.com/static/img/9e68ee04ef61c911a8dcc7caaf77b678/image.png)
6. 添加完成后，勾选并单击【确定】。
![](//mccdn.qcloud.com/static/img/c9bf9c597d7c0b2538dade72ed10bd4e/image.png)
7. 把这两个 DLL 在 “API 和CGI限制”进行添加，并改为允许。
![](//mccdn.qcloud.com/static/img/bccab999282e71a49aeb144a4dc3c9ed/image.png)
8. 重启 IIS 服务器，等待配置生效。

## Apache 配置方案
1. 安装 Apache 第三方模块“mod_rpaf” 。
```
wget http://stderr.net/apache/rpaf/download/mod_rpaf-0.6.tar.gz
tar zxvf mod_rpaf-0.6.tar.gz
cd mod_rpaf-0.6
/usr/bin/apxs -i -c -n mod_rpaf-2.0.so mod_rpaf-2.0.c
```
2. 修改 Apache 配置`/etc/httpd/conf/httpd.conf`，在最末尾添加：
```
LoadModule rpaf_module modules/mod_rpaf-2.0.so
RPAFenable On
RPAFsethostname On
RPAFproxy_ips IP地址（这个IP地址首先不是负载均衡提供的公网IP，具体IP多少可以查看Apache日志，通常会有2个 都要写上）
RPAFheader X-Forwarded-For
```
3. 添加完成后，重启 Apache。
```
/usr/sbin/apachectl restart
```

## Nginx 配置方案
1. Nginx 作为负载均衡获取真实 IP 时使用 http_realip_module，默认安装的 Nginx 是没有安装这个模块的，需要重新编译 Nginx 增加 --with-http_realip_module。
```
wget  http://nginx.org/download/nginx-1.14.0.tar.gz 
tar  zxvf nginx-1.14.0.tar.gz 
cd nginx-1.14.0
./configure --user=www --group=www --with-http_stub_status_module --without-http-cache --with-http_ssl_module --with-http_realip_module
make
make install
```
2. 修改 nginx.conf。
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
set_real_ip_from IP地址;（这个IP地址首先不是负载均衡提供的公网IP，具体IP多少可以查看之前nginx日志，如果有多个都要写上。）
real_ip_header X-Forwarded-For;
 </font>
</pre>
</div>
3. 重启 Nginx。
```
service nginx restart
```


