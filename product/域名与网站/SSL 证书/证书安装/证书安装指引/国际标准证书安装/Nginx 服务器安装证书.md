以下视频将为您进一步介绍在 Nginx 服务器安装 SSL 证书的操作过程：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/3386-59866?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 操作场景
本文档指导您如何在 Nginx 服务器中安装 SSL 证书。
>?
>- 本文档以证书名称 `cloud.tencent.com` 为例。
>- Nginx 版本以 `nginx/1.18.0` 为例。
>- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 Nginx 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>- SSL 证书文件上传至服务器方法可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。
>
## 前提条件
- 已准备文件远程拷贝软件，例如 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具，例如 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 已在当前服务器中安装配置 Nginx 服务。
- 安装 SSL 证书前需准备的数据如下：
<table>
<tr>
<th>名称</th>
<th>说明</th>
</tr>
<tr>
<td>服务器的 IP 地址</td>
<td>服务器的 IP 地址，用于 PC 连接到服务器。</td>
</tr>
<tr>
<td>用户名</td>
<td>登录服务器的用户名。</td>
</tr>
<tr>
<td>密码</td>
<td> 登录服务器的密码。</td>
</tr>
</table>

>?在腾讯云官网购买的云服务器，您可以登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)  获取服务器 IP 地址、用户名及密码。


## 操作步骤

### 证书安装
1.  已在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中下载并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 Nginx 文件夹和 CSR 文件：
 - **文件夹名称**：`cloud.tencent.com_nginx`
 - **文件夹内容**：
     - `cloud.tencent.com_bundle.crt` 证书文件
     - `cloud.tencent.com_bundle.pem` 证书文件
     - `cloud.tencent.com.key` 私钥文件
     - `cloud.tencent.com.csr` CSR 文件
>?CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
2. 使用 “WinSCP”（即本地与远程计算机间的复制文件工具）登录 Nginx 服务器。
3. 将已获取到的 `cloud.tencent.com_bundle.crt` 证书文件和 `cloud.tencent.com.key` 私钥文件从本地目录拷贝到 Nginx 服务器的 `/usr/local/nginx/conf` 目录（此处为 Nginx 默认安装目录，请根据实际情况操作）下。
4. 远程登录 Nginx 服务器。例如，使用 [“PuTTY” 工具](https://cloud.tencent.com/document/product/213/35699#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4) 登录。
5. 编辑 Nginx 根目录下的 `conf/nginx.conf` 文件。修改内容如下：
>?
>- 此操作可通过执行 `vim /usr/local/nginx/conf/nginx.conf` 命令行编辑该文件。
>- 由于版本问题，配置文件可能存在不同的写法。例如：Nginx 版本为 `nginx/1.15.0` 以上请使用 `listen 443 ssl` 代替 `listen 443` 和 `ssl on`。
>
```
server {
        #SSL 访问端口号为 443
        listen 443 ssl; 
	    #填写绑定证书的域名
        server_name cloud.tencent.com; 
		#证书文件名称
        ssl_certificate cloud.tencent.com_bundle.crt; 
		#私钥文件名称
        ssl_certificate_key cloud.tencent.com.key; 
        ssl_session_timeout 5m;
	    #请按照以下协议配置
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; 
	    #请按照以下套件配置，配置加密套件，写法遵循 openssl 标准。
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; 
        ssl_prefer_server_ciphers on;
        location / {
		   #网站主页路径。此路径仅供参考，具体请您按照实际目录操作。
		   #例如，您的网站运行目录在/etc/www下，则填写/etc/www。
            root html; 
            index  index.html index.htm;
        }
    }
```
6. 在 Nginx 根目录下，通过执行以下命令验证配置文件问题。
```
./sbin/nginx -t
```
 - 若存在，请您重新配置或者根据提示修改存在问题。
 - 若不存在，请执行 [步骤7](#step7)。
[](id:step7)
7. 重启 Nginx，即可使用 `https://cloud.tencent.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）
如果您需要将 HTTP 请求自动重定向到 HTTPS。您可以通过以下操作设置：
1. 根据实际需求，选择以下配置方式：
 - 在页面中添加 JS 脚本。
 - 在后端程序中添加重定向。
 - 通过 Web 服务器实现跳转。
 - Nginx 支持 rewrite 功能。若您在编译时没有去掉 pcre，您可在 HTTP 的 server 中增加 `return 301 https://$host$request_uri;`，即可将默认80端口的请求重定向为 HTTPS。修改如下内容：
>?
>- 未添加注释的配置语句，您按照下述配置即可。
>- 由于版本问题，配置文件可能存在不同的写法。例如：Nginx 版本为 `nginx/1.15.0` 以上请使用 `listen 443 ssl` 代替 `listen 443` 和 `ssl on`。
>
```
server {
   listen 443 ssl;
	#填写绑定证书的域名
    server_name cloud.tencent.com; 
	#证书文件名称
	ssl_certificate  cloud.tencent.com_bundle.crt; 
	#私钥文件名称
    ssl_certificate_key cloud.tencent.com.key; 
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    location / {
			#网站主页路径。此路径仅供参考，具体请您按照实际目录操作。 
			#例如，您的网站运行目录在/etc/www下，则填写/etc/www。
		root html;
        index index.html index.htm;
    }
}
server {
    listen 80;
	#填写绑定证书的域名
    server_name cloud.tencent.com; 
	#把http的域名请求转成https
    return 301 https://$host$request_uri; 
}
``` 
2. 若修改完成，重启 Nginx。即可使用 `http://cloud.tencent.com` 进行访问。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。

