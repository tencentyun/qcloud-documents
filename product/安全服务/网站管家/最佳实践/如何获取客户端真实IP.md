## WAF 获取客户端真实 IP 说明
WAF 通过反向代理的方式实现网站安全防护，用户访问 WAF 防护的域名时，会在 HTTP 头部字段中添加一条 X-Forwarded-For 记录，用于记录用户真实 IP，其记录格式为 `X-Forwarded-For:用户 IP`。如果用户访问域名存在多级代理，WAF 将记录靠近 WAF 上一条的代理服务器 IP。例如：
场景一：用户＞WAF＞源站，X-Forwarded-For 记录为：`X-Forwarded-For:用户真实 IP`
场景二：用户＞CDN > WAF＞源站，X-Forwarded-For 记录为： `X-Forwarded-For:用户真实 IP,X-Forwarded-For:CDN 回源地址`。
>?
	>- 场景二中，需要在 WAF [添加域名](https://console.cloud.tencent.com/guanjia/waf/config/add) 时，选择代理情况为“是”，选择代理接入后，可能存在客户端 IP 被伪造的风险。如果您使用腾讯云 CDN，不存在客户端 IP 被伪造的风险，腾讯云 CDN 会对 X-Forwarded-For 信息进重置，只填写 CDN 获取的客户端 IP。（如果使用代理接入，攻击者需要在能直接对 WAF VIP 地址进行请求的情况下才会产生影响，代理接入时用户无法探测到 WAF VIP 地址，请避免代理接入时 WAF VIP 地址泄露）。
>- 负载均衡型 WAF 接入，请参见负载均衡中 [如何获取客户端真实 IP](https://cloud.tencent.com/document/product/214/3728)。

下文将对常见的应用服务器 X-Forwarded-For 配置方案进行介绍：
- [IIS 7 配置方案](#IIS7)
- [Apache 配置方案](#Apache)
- [Nginx 配置方案](#Nginx)

<span id="IIS7"></span>
## IIS 7 配置方案
1. 下载与安装插件 [F5XForwardedFor](https://devcentral.f5.com/s/articles/x-forwarded-for-log-filter-for-windows-servers) 模块，根据自己的服务器操作系统版本将`x86\Release`或者`x64\Release`目录下的`F5XFFHttpModule.dll`和`F5XFFHttpModule.ini`拷贝到某个目录，这里假设为`C:\F5XForwardedFor`，确保 IIS 进程对该目录有读取权限。
2. 选择【IIS 服务器】，双击【模块】功能。
![](https://main.qcloudimg.com/raw/1682f2fd88f83f059d871013f5e76451.png)
3. 单击【配置本机模块】。
![](https://main.qcloudimg.com/raw/bdc74f95150f9d3d88dcbb0f5e81ec9e.png)
4. 在弹出框中单击【注册】。
![](https://main.qcloudimg.com/raw/3638128094c12515cb30de141524bfd0.png)
5. 添加下载的 DLL 文件，如下图所示：
![](https://main.qcloudimg.com/raw/9f8fac869d34ac4e308bd3c428da10af.png)
6. 添加完成后，勾选并单击【确定】。
![](https://main.qcloudimg.com/raw/aa8de7ebd04123fde03e9d1d487447bf.png)
7. 在 IIS 服务器的 “ISAPI 和 CGI 限制”中，添加如上两个 DLL ，并将限制设置为允许。
![](https://main.qcloudimg.com/raw/57243f4da04233238db2de9690ed7f1d.png)
8. 重启 IIS 服务器，等待配置生效。

<span id="Apache"></span>
## Apache 配置方案
1. 安装 Apache 第三方模块“mod_rpaf”，需执行如下命令：
```
wget http://stderr.net/apache/rpaf/download/mod_rpaf-0.6.tar.gz
tar zxvf mod_rpaf-0.6.tar.gz
cd mod_rpaf-0.6
/usr/bin/apxs -i -c -n mod_rpaf-2.0.so mod_rpaf-2.0.c
```
2. 修改 Apache 配置`/etc/httpd/conf/httpd.conf`，需在最末尾添加：
<pre>
LoadModule rpaf_module modules/mod_rpaf-2.0.so
RPAFenable On
RPAFsethostname On
<font color="red">
RPAFproxy_ips IP地址   //IP 地址为 WAF 防护域名的回源 IP 地址，可以在 <a href="https://console.cloud.tencent.com/guanjia/waf/config">Web应用防火墙控制台</a>，防护配置域名列表中的回源 IP 地址中查看，也可以在服务器后台的日志中查看，只需要将所有需要查看的 IP 都填写上即可。
RPAFheader X-Forwarded-For
</font>
</pr>
3. 添加完成后，重启 Apache。
```
/usr/sbin/apachectl restart
```

<span id="Nginx"></span>
## Nginx 配置方案
1. 当 Nginx 作为服务器时，获取客户端真实 IP，需使用 http_realip_module 模块，默认安装的 Nginx 是没有安装 http_realip_module 模块的，需要重新编译 Nginx 增加 --with-http_realip_module。
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
set_real_ip_from IP地址;   //IP 地址为 WAF 防护域名的回源 IP 地址，可以在 <a href="https://console.cloud.tencent.com/guanjia/waf/config">Web应用防火墙控制台</a>，防护配置域名列表中的回源 IP 地址中查看。
real_ip_header X-Forwarded-For;
 </font>
</pre>
</div>

3. 重启 Nginx。
<pre>
service nginx restart
</pre>
