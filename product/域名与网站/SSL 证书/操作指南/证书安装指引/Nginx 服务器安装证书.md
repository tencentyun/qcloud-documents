## 操作场景
本文档指导您如何在 Nginx 服务器中安装 SSL 证书。
>?
>- 本文档以证书名称 `www.domain.com` 为例。
>- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。
>
## 前提条件
- 已在 SSL 证书管理控制台 中下载并解压缩 `www.domain.com` 证书文件包到本地目录。
解压缩后，可获得 Nginx 文件夹和 CSR 文件：
 - **文件夹名称**：Nginx
 - **文件夹内容**：
    - `1_www.domain.com_bundle.crt` 证书文件
    - `2_www.domain.com.key` 私钥文件
  - **CSR 文件内容**：	`www.domain.com.csr` 文件
- 已准备远程拷贝软件 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 已在当前服务器中安装配置 Nginx 服务器。

>?CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
 
## 数据
安装 SSL 证书前需准备的数据如下：

| 名称 | 说明 | 取值样例 |
|---------|---------|---------|
| 服务器的 IP 地址 | 服务器的 IP 地址，用于 PC 连接到服务器。 | 192.168.22.10 |
| 用户名 | 登录服务器的用户名。 | root |
| 密码 | 登录服务器的密码。 | abc |

## 操作步骤

### 证书安装
1. 使用 “WinSCP”（即本地与远程计算机间的复制文件工具）登录 Nginx 服务器。
2. 将已获取到的 `1_www.domain.com_bundle.crt` 证书文件和 `2_www.domain.com.key` 私钥文件从本地目录拷贝到 Nginx 服务器的 `/usr/local/nginx/conf` 目录下。
>? 若无 `/usr/local/nginx/conf` 目录，可通过 `mkdir /usr/local/nginx/conf` 命令行创建。
3. 关闭 WinSCP 界面。
4. 使用远程登录工具，登录 Nginx 服务器。例如 “PuTTY” 工具。
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
 - **listen 443**：SSL 访问端口号为 443
 - **ssl on**：启用 SSL 功能
 - **ssl_certificate**：证书文件
 - **ssl_certificate_key**：私钥文件
 - **ssl_protocols**：使用的协议
 - **ssl_ciphers**：配置加密套件，写法遵循 openssl 标准
6. 在 Nginx 根目录下，通过执行以下命令确认配置文件是否存在问题。
```
./sbin/nginx -t
```
 - 若存在，请您重新配置或者根据提示修改存在问题。
 - 若不存在，请执行 [步骤7](#step7)。
<span id="step6"></span>
7. 重启 Nginx，即可使用 `https://www.domain.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）

若您不了解通过 HTTPS 访问网站的方式，可以通过配置服务器，让其自动将 HTTP 的请求重定向到 HTTPS。您可以通过以下操作设置：
1. 根据实际需求，选择以下配置方式：
 - 在页面中添加 JS 脚本。
 - 在后端程序中添加重定向。
 - 通过 Web 服务器实现跳转。
 - Nginx 支持 rewrite 功能。若您在编译时没有去掉 pcre，您可在 HTTP 的 server 中增加 `rewrite ^(.*) https://$host$1 permanent;`，即可将默认80端口的请求重定向为 HTTPS。修改如下内容：
```
server {
    listen 443;
    server_name www.domain.com; #填写绑定证书的域名
    ssl on;
    root /var/www/www.domain.com; #网站主页路径。此路径仅供参考，具体请您按照实际目录操作。
    index index.html index.htm;   
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
>?未添加注释的配置语句，您按照上述配置即可。
2. 若修改完成，重启 Nginx。即可使用 `http://www.domain.com` 进行访问。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。

