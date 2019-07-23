## 简介
用户可通过自有域名（自定义域名，例如`test.cos.com`）访问存储桶（Bucket）下的对象（Object）。具体操作指引如下：
- [开启 CDN 加速时配置自定义域名支持 HTTPS 访问](#开启CDN加速)
- [关闭 CDN 加速时配置自定义域名支持 HTTPS 访问](#关闭CDN加速)


## 操作步骤
<span id="开启CDN加速"></span>
### 开启 CDN 加速

#### 1. 绑定自定义域名。
将存储桶绑定到您的自有域名，开启 CDN 加速，详细操作指引请参见 [域名管理](https://cloud.tencent.com/document/product/436/6252#%E5%BC%80%E5%90%AFCDN%E5%8A%A0%E9%80%9F) 文档中的配置自定义域名部分。
#### 2. 配置 HTTPS 访问。
在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 进行 HTTPS 配置，详细操作指引请参见 [HTTPS 配置](https://cloud.tencent.com/document/product/228/6295)。


<span id="关闭CDN加速"></span>
### 关闭 CDN 加速
本章节主要以示例的形式介绍在 COS 中通过反向代理配置自定义域名（关闭 CDN 加速）支持 HTTPS 访问的操作步骤。本示例将实现不开启 CDN 加速的情况下，直接通过自定义域名`https://test.cos.com`访问所属地域为华南、名称为 testhttps-12345678 的存储桶，具体操作步骤如下：

#### 1. 绑定自定义域名。
将存储桶 testhttps 绑定到域名`https://test.cos.com`，关闭 CDN 加速，详细操作指引请参见 [域名管理](https://cloud.tencent.com/document/product/436/6252#%E5%85%B3%E9%97%ADCDN%E5%8A%A0%E9%80%9F) 文档中的配置自定义域名部分。
#### 2. 为域名配置反向代理。
在服务器上为域名`https://test.cos.com`配置反向代理。具体配置参考如下（以下 Nginx 配置仅供参考）：
```shell
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
        proxy_pass  http://testhttps-12345678.cos.ap-guangzhou.myqcloud.com; //配置存储桶（Bucket）的默认下载域名 
    }
}
```
其中`server.crt;`、`server.key`是您的自有（自定义）域名的 HTTPS 证书。若您的域名还没有 HTTPS 证书 ，请前往 [腾讯云 SSL 证书](https://cloud.tencent.com/product/ssl) 页面进行申请。
若暂时没有证书，可以删除以下配置信息，但访问时会出现告警，单击继续即可访问：
```shell
ssl on;
ssl_certificate /usr/local/nginx/conf/server.crt;
ssl_certificate_key /usr/local/nginx/conf/server.key;
```
#### 3. 解析域名到服务器。
在您域名的 DNS 解析服务商处解析您的域名。若您使用的是腾讯云云解析，请前往 [云解析控制台](https://console.cloud.tencent.com/cns/domains)，将域名`test.cos.com`解析到步骤2中的服务器的 IP 上，详细指引请参见 [域名解析](https://cloud.tencent.com/document/product/302/3446)。

#### 进阶配置
#### 通过浏览器直接打开网页
在配置好自定义域名支持 HTTPS 访问后，就可以通过您的域名下载存储桶（Bucket）中的对象（Object）了。若根据业务需要，需要直接在浏览器中访问网页、图片等，可通过静态网站功能实现。详细操作指引请参见 [设置静态网站](https://cloud.tencent.com/document/product/436/14984) 文档。
配置完成后，在 Nginx 配置中增加一行信息，重启 Nginx，刷新浏览器缓存即可。
```bash
proxy_set_header Host $http_host;
```
#### 配置 refer 防盗链
若存储桶（Bucket）是公有的，会有被盗链的风险。用户可以通过防盗链设置，开启 Referer 白名单，防止被恶意盗链。具体操作步骤如下：
1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)， 开启防盗链设置功能，选择白名单。详细操作指引请参见 [设置防盗链](https://cloud.tencent.com/document/product/436/13319) 。
2. 在 Nginx 配置文件中，增加一行信息并重启 Nginx，刷新浏览器缓存。
```bash
proxy_set_header   Referer www.test.com;
```
3. 设置完成后，直接打开文件将提示报错`errorcode：-46616`。错误提示：未命中 refer 白名单，但是通过代理访问自定义域名，可以正常打开网页。
```json
{
	errorcode: -46616,
	errormsg: "not hit white refer, retcode:-46616"
}
```
