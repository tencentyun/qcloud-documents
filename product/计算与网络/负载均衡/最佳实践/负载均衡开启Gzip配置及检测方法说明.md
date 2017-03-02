在**公网应用型负载均衡、公网有固定IP型负载均衡**实例中，**HTTP/HTTPS协议**支持用户开启Gzip压缩功能。用户开启Gzip压缩后，浏览器端不需要进行配置（主流浏览器都支持Gzip功能）。在云服务器端，由于腾讯云内部全网支持HTTP/1.1协议，因此用户也无需配置，使用的是nginx默认配置（HTTP/1.1）即可兼容。下面的例子讲解了Gzip的配置参数和检测方法。

示例RS运行环境：Debian 6

1 . 使用vim依据用户路径打开Nginx配置文件：
```
vim /etc/nginx/nginx.conf
```
2 . 找到如下代码：
```
gzip on;
gzip_min_length 1k;
gzip_buffers 4 16k;
gzip_http_version 1.1;
gzip_comp_level 2;
```
部分代码功能如下：
第1行：开启Gzip。
第2行：不压缩临界值，大于1K的才压缩，一般不需更改。
第3行：buffer不需更改。
第4行：代表可以使用Gzip功能的HTTP最低版本。Nginx默认是HTTP/1.1，由于腾讯云现已全网支持HTTP/1.1，因此无需进行更改。即使用户设置为***gzip_http_version 1.0***，依然可以向上兼容。
第5行：数字代表压缩级别，其范围从1-10，数字越大压缩的越好，时间也越长。

3 . 如对配置有修改，则首先将文件保存退出，进入到Nginx bin文件目录，执行如下命令重新加载Nginx
```
./nginx -s reload
```
4 . 最后使用curl命令测试Gzip是否成功开启
```
curl -I -H "Accept-Encoding: gzip, deflate" "http://www.qcloud.com/example/"
```
