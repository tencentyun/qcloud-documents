在**公网负载均衡、公网固定 IP 型负载均衡**实例中，**HTTP/HTTPS 协议**默认支持用户开启 gzip 压缩功能。开启 gzip 功能对网页进行压缩，可以有效降低网络传输的数据量，提升客户端浏览器的访问速度。在使用过程中，需要注意如下事项：

### 注意事项
- **需要后端 CVM 同步开启 GZIP 支持**
对于常见的 Nginx 服务容器，必须在其配置文件（默认为 nginx.conf）中，开启 GZIP 并重启服务
```
gzip on;
```
- **当前负载均衡支持的文件类型如下，您可以在 gzip_types 配置项中指定文件类型进行压缩**
```
application/atom+xml application/javascript application/json application/rss+xml application/vnd.ms-fontobject application/x-font-ttf application/x-web-app-manifest+json application/xhtml+xml application/xml font/opentype image/svg+xml image/x-icon text/css text/plain text/x-component;
```
>!负载均衡后端 CVM 业务软件中必须同步开启对上述文件类型的 GZIP 支持。
>
- **客户端请求中必须带有压缩请求标记**
需要启用压缩，还要求客户端请求时必须携带如下标记：
```
Accept-Encoding: gzip,deflate,sdch
```

### 后端 CVM 开启 GZIP 流程支持示例
示例云服务器运行环境：Debian 6
1. 使用 vim 依据用户路径打开 Nginx 配置文件：
```
vim /etc/nginx/nginx.conf
```
2. 找到如下代码：
```
gzip on;
gzip_min_length 1k;
gzip_buffers 4 16k;
gzip_http_version 1.1;
gzip_comp_level 2;
gzip_types text/html application/json;
```
上述代码的语法详解：
	- gzip：开启或关闭 gzip 模块。
语法：`gzip on/off`
作用域：http，server，location
	- gzip_min_length：设置允许压缩的页面最小字节数，页面字节数从 header 头中的 Content-Length 中进行获取。默认值是1k。
语法：`gzip_min_length length`
作用域：http，server，location
	- gzip_buffers：设置系统获取几个单位的缓存用于存储 gzip 的压缩结果数据流。16k代表以16k为单位，按照原始数据大小以16k为单位的4倍申请内存。
语法： `gzip_buffers number size`
作用域：http，server，location
	- gzip_http_version ：代表可以使用 gzip 功能的 HTTP 最低版本，设置 HTTP/1.0 代表了需要使用 gzip 功能的 HTTP 最低版本，因此可以向上兼容 HTTP/1.1。由于腾讯云现已全网支持 HTTP/1.1，因此无需进行更改。
语法: `gzip_http_version 1.0 | 1.1;`
作用域: http，server，location
	- gzip_comp_level：gzip 压缩比，范围为1 - 9。1压缩比最小处理速度最快，9压缩比最大但处理最慢（传输快但比较消耗 cpu）。
语法: `gzip_comp_level 1..9`
作用域: http，server，location
	- gzip_types：匹配 MIME 类型进行压缩，默认"text/html" 类型是会被压缩的。 此外，Nginx 下的 gzip 默认不压缩 javascript、图片等静态资源文件，可以通过gzip_types 指定需要压缩的 MIME 类型，非设置值则不进行压缩。 **例如，如果需要对 json 格式数据进行压缩，则需要在此语句中添加 application/json 类型数据**。
支持的类型如下：
```
text/html text/plain text/css application/x-javascript text/javascript application/xml
```
语法: `gzip_types mime-type [mime-type ...]`
作用域: http, server, location
3. 如对配置有修改，则首先将文件保存退出，进入到 Nginx bin 文件目录，执行如下命令重新加载 Nginx：
```
./nginx -s reload
```
4. 使用 curl 命令测试 gzip 是否成功开启：
```
curl -I -H "Accept-Encoding: gzip, deflate" "http://cloud.tencent.com/example/"
```

