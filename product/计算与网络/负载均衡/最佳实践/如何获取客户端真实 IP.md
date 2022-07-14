## 负载均衡获取客户端真实 IP 的说明
CLB 的四层（TCP/UDP/TCP SSL）和七层（HTTP/HTTPS）服务均支持直接在后端 CVM 上获取客户端真实 IP，无需进行额外配置。
- 四层负载均衡，在后端 CVM 上获取的源 IP 即为客户端 IP。
- 七层负载均衡，您可以通过 `X-Forwarded-For` 或 `remote_addr` 字段来直接获取客户端 IP。七层负载均衡的访问日志请参见 [配置访问日志到 CLS](https://cloud.tencent.com/document/product/214/41379)。 

>?
- 对于四层负载均衡来说，无需在后端 CVM 上做额外配置即可获取客户端 IP。
- 对于其他做了 SNAT 的七层负载均衡服务，您需要在后端 CVM 上配置，然后使用 X-Forwarded-For 的方式获取客户端的真实 IP。

下文将对常见的应用服务器配置方案进行介绍。

## IIS 6 配置方案
1. 下载与安装插件 [F5XForwardedFor](https://devcentral.f5.com/s/articles/x-forwarded-for-log-filter-for-windows-servers) 模块，根据自己的服务器操作系统版本将`x86\Release`或者`x64\Release`目录下的`F5XForwardedFor.dll`拷贝到某个目录，这里假设为`C:\ISAPIFilters`，同时确保对 IIS 进程对该目录有读取权限。
2. 打开 IIS 管理器，找到当前开启的网站，在该网站上右键选择**属性**，打开属性页。
3. 在属性页切换至 **ISAPI 筛选器**，单击**添加**，弹出添加窗口。
4. 在添加窗口“筛选器名称”中填写“F5XForwardedFor”，“可执行文件”填写`F5XForwardedFor.dll`的完整路径，单击**确定**。
5. 重启 IIS 服务器，等待配置生效。

## IIS 7 配置方案
1. 下载与安装插件 [F5XForwardedFor](https://devcentral.f5.com/s/articles/x-forwarded-for-log-filter-for-windows-servers) 模块，根据自己的服务器操作系统版本将`x86\Release`或者`x64\Release`目录下的`F5XFFHttpModule.dll`和`F5XFFHttpModule.ini`拷贝到某个目录，这里假设为`C:\x_forwarded_for`，确保对 IIS 进程对该目录有读取权限。
2. 选择 **IIS 服务器**，双击**模块**功能。
![](https://main.qcloudimg.com/raw/fd26a3b2e4bfd1f31ee71c9821639213.png)
3. 单击**配置本机模块**。
![](https://main.qcloudimg.com/raw/72fa2e2bd9a5c83c852a2debc6877f8e.png)
4. 在弹出框中单击**注册**。
![](https://main.qcloudimg.com/raw/be262498b081c68205618671f4086cbf.png)
5. 添加下载的 DLL 文件，如下图所示：
![](https://main.qcloudimg.com/raw/859107d872f77068ac9ce20f7732e184.png)
6. 添加完成后，勾选并单击**确定**。
![](https://main.qcloudimg.com/raw/3b2548c3279d838f800a034397e2d1cf.png)
7. 在 “ISAPI 和 CGI 限制”添加如上两个 DLL ，并将限制设置为允许。
![](https://main.qcloudimg.com/raw/5fda5595af334605ffb1f4e76d152139.png)
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
RPAFproxy_ips IP地址（这个 IP 地址首先不是负载均衡提供的公网 IP，具体 IP 多少可以查看 Apache 日志，通常会有2个 都要写上）
RPAFheader X-Forwarded-For
```
3. 添加完成后，重启 Apache。
```
/usr/sbin/apachectl restart
```

## Nginx 配置方案
1. Nginx 作为服务器时，获取客户端真实 IP 使用 http_realip_module，默认安装的 Nginx 未安装此模块，需要重新编译 Nginx 增加 `--with-http_realip_module`。
```
yum -y install gcc pcre pcre-devel zlib zlib-devel openssl openssl-devel
wget http://nginx.org/download/nginx-1.17.0.tar.gz
tar zxvf nginx-1.17.0.tar.gz
cd nginx-1.17.0
./configure --prefix=/path/server/nginx --with-http_stub_status_module --without-http-cache --with-http_ssl_module --with-http_realip_module
make
make install
```
2. 修改 nginx.conf 文件。
```
vi /etc/nginx/nginx.conf
```
修改如下红色部分的配置字段和信息：
>?其中 `xx.xx.xx.xx` 需要修改为实际的 IP 地址，此 IP 地址不是负载均衡提供的公网 IP，具体 IP 地址可查看之前 Nginx 日志。若有多个 IP 地址，则都需要写上。
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
<font color="#f2777a">
set_real_ip_from xx.xx.xx.xx;
real_ip_header X-Forwarded-For;
 </font>
</pre>
</div>
3. 重启 Nginx。
```
service nginx restart
```
4. 查看 Nginx 的访问日志，您可以获取客户端的真实 IP。
```
cat /path/server/nginx/logs/access.log
```
