## 操作场景
本文以使用 **WordPress 5.7.1 社区版**的轻量应用服务器为例，介绍如何在服务器中安装 SSL 证书并开启 HTTPS 访问。该服务器中默认已安装 Nginx 软件，您可参考本文并结合实际情况进行操作。



<dx-alert infotype="explain" title="">
- 本文档以通过腾讯云SSL证书服务申请的付费、免费证书为例。腾讯云 SSL 证书服务相关信息可参考 [SSL 证书产品介绍](https://cloud.tencent.com/document/product/400/7572)、[SSL 证书购买指南](https://cloud.tencent.com/document/product/400/7994) 和 [申请免费 SSL 证书](https://cloud.tencent.com/document/product/400/6814)。
- 如您的轻量应用服务器使用 Discuz! Q 应用镜像，则可通过内置的宝塔 Linux 面板进行 SSL 证书安装，详情请参考宝塔 Linux 面板官方用户文档。
</dx-alert>

 


## 前提条件
- 已准备文件远程拷贝软件，例如 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具，例如 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 轻量应用服务器创建完成后，防火墙默认已开启 `443` 端口。建议您在安装 SSL 证书前，前往防火墙页面确认已开启 `443` 端口，避免证书安装后无法启用 HTTPS。详情请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577)。
- 安装 SSL 证书前需准备的数据如下：
<table>
<tr>
<th style="width:35%">名称</th>
<th>说明</th>
</tr>
<tr>
<td>轻量应用服务器的公网 IP 地址</td>
<td>服务器的 IP 地址，用于本地计算机连接到服务器。</td>
</tr>
<tr>
<td>用户名</td>
<td>登录轻量应用服务器操作系统的用户名，例如 root。</td>
</tr>
<tr>
<td>密码或 SSH 密钥</td>
<td>登录轻量应用服务器操作系统所使用的用户名对应的密码，或者已绑定的 SSH 密钥。</td>
</tr>
</table>
<dx-alert infotype="notice" title="">
您可以登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse) 找到对应的服务器实例，进入实例详情页查看服务器的公网 IP 地址。如果该实例创建后未执行重置密码或者绑定 SSH 密钥操作，请您执行重置密码操作并牢记密码，或绑定 SSH 密钥并保存私钥文件。详情请参见 [重置密码](https://cloud.tencent.com/document/product/1207/44575) 和 [绑定密钥](https://cloud.tencent.com/document/product/1207/44573)。
</dx-alert>




## 操作步骤

### 证书安装
1. 前往 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中下载 SSL 证书（名称以 `cloud.tencent.com` 为例）文件压缩包，并解压到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 Nginx 文件夹和 CSR 文件：
 - **文件夹名称**：Nginx
 - **文件夹内容**：
     - `1_cloud.tencent.com_bundle.crt` 证书文件
     - `2_cloud.tencent.com.key` 私钥文件
  - **CSR 文件内容**：	`cloud.tencent.com.csr` 文件
<dx-alert infotype="explain" title="">
CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
</dx-alert>
2. 在本地计算机中使用远程登录工具（如 WinSCP），通过用户名密码方式或者 SSH 密钥对方式登录轻量应用服务器。详情请参见 [远程登录Linux实例](https://cloud.tencent.com/document/product/1207/44578)。
3. 将已获取到的 `1_cloud.tencent.com_bundle.crt` 证书文件和 `2_cloud.tencent.com.key` 私钥文件从本地目录拷贝到轻量应用服务器 Nginx 默认配置文件目录中。
<dx-alert infotype="explain" title="">
WordPress 镜像的默认配置文件目录为 `/www/server/nginx/conf`。
</dx-alert>
4. [](id:Step4)对于 WordPress 镜像创建的实例则执行以下命令，编辑 Nginx 默认配置文件目录中的 `nginx.conf` 文件。
```
sudo vim /www/server/nginx/conf/nginx.conf
```
找到以下配置信息：
```
server {
    listen       80;
    server_name  localhost;

    location / {
        root   html;
        index  index.html index.htm;
    }

    location /server-status {
#       stub_status  on;
        allow        127.0.0.1;
        deny         all;
    }

    location /status {
        include      fastcgi.conf;
        fastcgi_pass 127.0.0.1:9000;
        allow        127.0.0.1;
        deny         all;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
}
```
参考以下配置对 `nginx.conf` 文件进行修改：
<dx-alert infotype="explain" title="">
此配置仅供参考，请参考注释并按照实际环境进行修改。您也可以参考 Nginx 官方文档按需进行配置。
</dx-alert>
```
server {
    listen 443 ssl;
    server_tokens off;
    keepalive_timeout 5;
    root /usr/local/lighthouse/softwares/wordpress; #填写您的网站根目录，例如：/usr/local/lighthouse/softwares/wordpress
    index index.php index.html;
    access_log logs/wordpress.log;
    error_log logs/wordpress.error.log;
    server_name cloud.tencent.com; #填写您的证书绑定的域名，例如：www.cloud.tencent.com
    ssl_certificate 1_cloud.tencent.com_bundle.crt; #填写您的证书文件名称，例如：1_cloud.tencent.com_bundle.crt
    ssl_certificate_key 2_cloud.tencent.com.key; #填写您的私钥文件名称，例如：2_cloud.tencent.com.key
    ssl_session_timeout 5m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;  # 可参考此 SSL 协议进行配置
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;   #可按照此加密套件配置，写法遵循 openssl 标准
    ssl_prefer_server_ciphers on;
    location ~* \.php$ {
        fastcgi_pass   127.0.0.1:9000;
        include fastcgi.conf;
        client_max_body_size 20m;
        fastcgi_connect_timeout 30s;
        fastcgi_send_timeout 30s;
        fastcgi_read_timeout 30s;
        fastcgi_intercept_errors on;
    }
}
```
5. 找到 http{...}，并输入以下配置信息。
```
ssl_certificate 1_cloud.tencent.com_bundle.crt;   #填写您的证书文件名称，例如：1_cloud.tencent.com_bundle.crt
ssl_certificate_key 2_cloud.tencent.com.key;    #填写您的私钥文件名称，例如：2_cloud.tencent.com.key
```
6. 保存修改后的 `nginx.conf` 文件后退出。
7. [](id:Step7)执行以下命令，验证配置文件是否存在问题。
```
sudo nginx -t
```
 - 若输出信息如下如所示，则为配置成功，请继续执行 [步骤8](#Step8)。
![](https://main.qcloudimg.com/raw/bead4ecd767b34c600f1ce4d5844cac0.png)
 - 若存在错误提示，请您重新配置或者根据提示修改存在问题。
8. [](id:Step8)执行以下命令，重启 Nginx。
```
sudo systemctl reload nginx
```
至此已安装成功。您可使用 `https://cloud.tencent.com`（示例）正常进行访问。

### 设置 HTTP 请求自动跳转 HTTPS（可选）

您可以通过配置服务器，让其自动将 HTTP 的请求重定向到 HTTPS。可以参考以下步骤进行设置：

1. Nginx 支持 rewrite 功能。若您在编译时没有删除 pcre，则可在 HTTP 的 server 中增加 `return 301 https://$host$request_uri;`，即可将默认80端口的请求重定向为 HTTPS。
您需要对 `nginx.conf` 文件进行修改，在“证书安装”中的 [步骤4](#Step4) 的配置之后继续添加如下配置：
```
server {
    listen 80;
    server_name cloud.tencent.com;    #填写您的证书绑定的域名，例如：cloud.tencent.com
    return 301 https://$host$request_uri;  	 #将http的域名请求转成https
}
```
2. 保存修改后的 `nginx.conf` 文件后退出，参考“证书安装”的 [步骤7](#Step7) 及 [步骤8](#Step8) 验证并重启 Nginx。
至此已成功设置 HTTPS 的自动跳转，您可使用 `http://cloud.tencent.com`（示例）自动跳转至 HTTPS 页面。如下图所示：
![](https://main.qcloudimg.com/raw/006c7e90aa5e5ca71bd6db6b270650c4.png)

