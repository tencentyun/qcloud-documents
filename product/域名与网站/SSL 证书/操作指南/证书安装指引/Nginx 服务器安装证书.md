## 操作场景
本文档指导您如何在 Nginx 服务器中安装 SSL 证书。

## 前提条件
由于操作系统的版本不同，详细操作步骤略有区别。以下条件仅针对当前服务器说明：
- 当前服务器的操作系统为 CentOS 7。
- 已在当前服务器中安装配置 Nginx 服务器。

## 操作步骤

### 证书安装
1. 使用“WinSCP”，即本地与远程计算机间的复制文件工具，登录 Nginx 服务器。
2. 将已获取到的`1_www.domain.com_bundle.crt` 证书文件和 `2_www.domain.com.key` 私钥文件从本地目录拷贝到 Nginx 服务器的 `/usr/local/nginx/conf` 目录下。
>? 若无 `/usr/local/nginx/conf` 目录，可通过`mkdir /usr/local/nginx/conf`命令行创建。
3. 关闭 WinSCP 界面。
4. 使用远程登录工具，登录 Nginx 服务器。例如 “PuTTY” 工具。
<span id="step5"></span>
5. 编辑 Nginx 根目录下的 conf/nginx.conf 文件。修改内容如下：
```
server {
        listen 443;
        server_name www.domain.com; #填写绑定证书的域名
        ssl on;
        ssl_certificate 1_www.domain.com_bundle.crt;#证书文件名称
        ssl_certificate_key 2_www.domain.com.key;#私钥文件名称
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; #请按照这个协议配置
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;#请按照这个套件配置
        ssl_prefer_server_ciphers on;
        location / {
            root /var/www/www.domain.com; #网站主页路径。此路径仅供参考，具体请您按照实际目录操作。
            index  index.html index.htm;
        }
    }
```
配置文件的主要参数说明如下：
 - listen 443：SSL 访问端口号为 443
 - ssl on：启用 SSL 功能
 - ssl_certificate：证书文件
 - ssl_certificate_key：私钥文件
 - ssl_protocols：使用的协议
 - ssl_ciphers：配置加密套件，写法遵循 openssl 标准
6. 在 Nginx 根目录下，通过执行以下命令确认配置文件是否存在问题。
```
./sbin/nginx -t
```
 - 若存在，请您重新检查 [步骤5](#step5)。
 - 若不存在，重启 Nginx。
7. 若启动成功，即可使用 `https://www.domain.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）

如果您不知道网站可以通过 HTTPS 方式访问的情况，我们可以通过配置服务器，让其自动将 HTTP 的请求重定向到 HTTPS。您可以通过以下方式设置：
- 您可以在页面中添加 JS 脚本，也可以在后端程序中添加重定向，还可以通过 Web 服务器实现跳转。
- 若您在编译时没有去掉 pcre，Nginx 支持 rewrite 功能。您可在 HTTP 的 server 中增加 `rewrite ^(.*) https://$host$1 permanent;`，即可将默认80端口的请求重定向为 HTTPS。修改如下内容：
```
server {
    listen 443;
    server_name www.domain.com; #填写绑定证书的域名
    ssl on;
    root /var/www/www.domain.com; #网站主页路径。此路径仅供参考，具体请您按照实际目录操作。
    index index.html index.htm;   #上面配置的文件夹里面的index.html
    ssl_certificate  1_www.domain.com_bundle.crt; #证书文件名称
    ssl_certificate_key 2_www.domain.com.key; #私钥文件名称
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    location / {
        index index.html index.htm;
    }
}
server {
    listen 80;
    server_name www.domain.com; #填写绑定证书的域名
    rewrite ^(.*)$ https://$host$1 permanent; #把http的域名请求转成https
}
``` 
若修改完成，重启 Nginx。即可使用 `http://www.domain.com` 进行访问。

