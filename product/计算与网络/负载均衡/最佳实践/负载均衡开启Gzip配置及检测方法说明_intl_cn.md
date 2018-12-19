在**公网应用型负载均衡、公网有固定IP型负载均衡**实例中，**HTTP/HTTPS协议**支持用户开启gzip压缩功能。开启gzip功能对网页进行压缩，可以有效降低网络传输的数据量，提升客户端浏览器的访问速度。

用户开启gzip压缩后，浏览器端不需要进行配置（主流浏览器都支持gzip功能）。在云服务器端，由于腾讯云内部全网支持HTTP/1.1协议，因此用户也***无需配置***，使用的是nginx默认配置（HTTP/1.1）即可兼容。下面的例子讲解了gzip模块的语法配置和检测方法。

示例云服务器运行环境：Debian 6

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
gzip_types text/html application/json;
```
上述代码的语法如下：
gzip：开启或关闭gzip模块。

> 	语法：gzip on/off	
>   作用域：http, server, location
	
gzip_min_length：设置允许压缩的页面最小字节数，页面字节数从header头中的Content-Length中进行获取。默认值是1k。

> 	语法：gzip_min_length length
>   作用域：http, server, location
	
gzip_buffers：设置系统获取几个单位的缓存用于存储gzip的压缩结果数据流。4 16k 代表以 16k 为单位，按照原始数据大小以 16k 为单位的4倍申请内存。

> 	语法: gzip_buffers number size
>   作用域: http, server, location
	
gzip_comp_level：gzip压缩比，范围为1~9。1 压缩比最小处理速度最快，9 压缩比最大但处理最慢（传输快但比较消耗cpu）。

> 	语法: gzip_comp_level 1..9
>   作用域: http, server, location
	
gzip_http_level：代表可以使用gzip功能的HTTP最低版本。由于腾讯云现已全网支持HTTP/1.1，因此无需进行更改。***即使用户设置为gzip_http_version 1.0，gzip依然可以生效。***由于设置HTTP/1.0代表了需要使用gzip功能的HTTP最低版本，因此可以向上兼容HTTP/1.1。

>   语法: gzip_http_version 1.0 | 1.1;
>   作用域: http, server, location

gzip_types：匹配MIME类型进行压缩，默认"text/html" 类型是会被压缩的。 此外，Nginx下的gzip默认不压缩javascript、图片等静态资源文件，可以通过gzip_types指定需要压缩的MIME类型,非设置值则不进行压缩 ***例如，如果需要对json格式数据进行压缩，则需要在此语句中添加application/json类型数据***
支持的类型如下：
>   text/html text/plain application/x-javascript text/css text/javascript application/xml

>   语法: gzip_types mime-type [mime-type ...]
>   作用域: http, server, location

3 . 如对配置有修改，则首先将文件保存退出，进入到Nginx bin文件目录，执行如下命令重新加载Nginx
```
./nginx -s reload
```
4 . 最后使用curl命令测试gzip是否成功开启
```
curl -I -H "Accept-Encoding: gzip, deflate" "http://cloud.tencent.com/example/"
```
