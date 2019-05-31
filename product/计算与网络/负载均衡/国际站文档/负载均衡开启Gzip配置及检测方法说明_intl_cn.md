在**公网有日租型**的负载均衡实例中，**http/https协议**支持用户开启Gzip压缩功能。用户开启Gzip压缩后，浏览器端不需要进行配置（主流浏览器都支持Gzip功能）。对于云服务器端，用户需要配置可使用Gzip的http最低版本为http 1.0。因为在腾讯云内部使用的是http1.0协议，而客户RS端如不做配置，使用的是nginx默认配置，即http1.1版本，因此会出现不兼容的问题。下面的例子展示了Gzip配置的修改方法。

示例RS运行环境：Debian 6
1. 使用vim依据用户路径打开Nginx配置文件：
```
vim /etc/nginx/nginx.conf
```
2. 找到如下代码进行修改：
```
gzip on;
gzip_min_length 1k;
gzip_buffers 4 16k;
gzip_http_version 1.0;
gzip_comp_level 2;
```
部分代码功能如下：
第1行：开启Gzip
第2行：不压缩临界值，大于1K的才压缩，一般不用改
第3行：buffer不用改
第4行：nginx默认是HTTP/1.1，腾讯云支持的最低版本是HTTP/1.0，因此需要改为 **gzip_http_version 1.0;**
第5行：压缩级别，1-10，数字越大压缩的越好，时间也越长

3. 将文件保存退出，进入到Nginx bin文件目录，执行如下命令重新加载Nginx
```
./nginx -s reload
```
4. 使用curl命令测试Gzip是否成功开启
```
curl -I -H "Accept-Encoding: gzip, deflate" "http://cloud.tencent.com/example/"
```
