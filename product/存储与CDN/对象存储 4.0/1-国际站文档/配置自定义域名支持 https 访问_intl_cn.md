用户可通过自有域名（自定义域名，如`test.cos.com`）访问存储桶（Bucket）下的对象（Object）。具体操作指引如下：
- [开启 CDN 加速时配置自定义域名支持 HTTPS 访问](#开启 CDN 加速)
- [关闭 CDN 加速时配置自定义域名支持 HTTPS 访问](#关闭 CDN 加速)

<span id="开启 CDN 加速"></span>
## 开启 CDN 加速
### 一、绑定自定义域名
将存储桶绑定到您的自有域名，开启 CDN 加速。操作指引参考 [域名管理--自定义域名](/doc/product/436/6252#开启 CDN 加速)。
### 二、配置 HTTPS 访问
在 CDN 控制台进行 HTTPS 配置，操作指引参考 [HTTPS 配置](/doc/product/228/6295)。
<span id="关闭 CDN 加速"></span>
## 关闭 CDN 加速
本章节主要以示例的形式介绍在 COS 中通过反向代理配置自定义域名（关闭 CDN 加速）支持 https 访问的操作步骤。本示例将实现不开启 CDN 加速的情况下，直接通过自定义域名`https://test.cos.com`访问用户 APPID 为 12345678 、所属地域为华南、名称为 testhttps 的存储桶，具体操作步骤如下：

### 一、绑定自定义域名
将存储桶 testhttps 绑定到域名`https://test.cos.com`，关闭 CDN 加速。操作指引参考 [域名管理--自定义域名](/doc/product/436/6252#关闭 CDN 加速)。
### 二、为域名配置反向代理
在服务器上为域名`https://test.cos.com` 配置反向代理。具体配置参考如下（以下 Nginx 配置仅供参考）：
```
server {
    listen        443;
server_name  test.cos.com ;

    ssl on;
    ssl_certificate /usr/local/nginx/conf/server.crt;
    ssl_certificate_key /usr/local/nginx/conf/server.key;

    error_log logs/test.cos.com.error_log;
    access_log logs/test.cos.com.access_log;
    location / {
        root /data/www/;
        proxy_pass  http://testhttps-12345678.cosgz.myqcloud.com; //配置存储桶（Bucket）的默认下载域名 
    }
        
}
```
其中`server.crt;`、`server.key`是您的自有（自定义）域名的 HTTPS 证书。若您的域名还没有 HTTPS 证书 ，可以在 [腾讯云 SSL 证书](https://cloud.tencent.com/product/ssl) 页面申请。
若暂时没有证书，可以删除以下配置信息，但访问时会出现告警，点击继续即可访问：
```
    ssl on;
    ssl_certificate /usr/local/nginx/conf/server.crt;
    ssl_certificate_key /usr/local/nginx/conf/server.key;
```

### 三、解析域名到服务器
在您域名的 DNS 解析服务商处解析您的域名。若您使用的是腾讯云云解析，请前往 [云解析控制台](https://console.cloud.tencent.com/cns/domains)，将域名`test.cos.com`解析到步骤二中的服务器的 IP 上，指引参考 [域名解析](/doc/product/302/3446)。
### 进阶配置
#### 通过浏览器直接打开网页
在配置好自定义域名支持 HTTPS 访问后，就可以通过您的域名下载存储桶（Bucket）中的对象（Object）了。若根据业务需要，想直接在浏览器中访问网页、图片等，可通过静态网站功能实现。操作指引参考 [静态网站设置](/doc/product/436/6249)。
![图片1](//mc.qcloudimg.com/static/img/bdd63d54f805e4975e82c95b37f675f0/image.png)
配置完成后，在 Nginx 配置中增加一行信息，重启 Nginx，刷新浏览器缓存即可。
```
proxy_set_header Host $http_host;
```
#### 配置 refer 防盗链
若存储桶（Bucket）是公有的，会有被盗链的风险。用户可以通过防盗链设置，开启 Referer 白名单，防止被恶意盗链。具体操作步骤如下：
1. 在[COS 控制台](https://console.cloud.tencent.com/cos4/index) 开启防盗链设置功能，选择白名单。操作指引参考 [防盗链设置](/doc/product/436/6250)
![图片2](//mc.qcloudimg.com/static/img/788556013c4d3ebd6b728d8c22a8adb5/image.png)
2. 在 Nginx 配置中增加一行信息，再重启 Nginx，刷新浏览器缓存。
```
proxy_set_header   Referer www.test.com;
```
3. 设置完成后，直接打开文件会报错：`errorcode：-46616`；错误提示：未命中 refer 白名单。但是通过代理访问自定义域名，可以正常打开网页。
![图片3](//mc.qcloudimg.com/static/img/005099e6a30398c600bb945b6b1c34e7/image.png)
