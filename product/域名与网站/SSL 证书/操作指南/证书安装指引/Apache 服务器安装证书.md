## 操作场景
本文档指导您如何在 Apache 服务器中安装 SSL 证书。

## 前提条件
由于操作系统的版本不同，详细操作步骤略有区别。以下条件仅针对当前服务器说明：
- 当前服务器的操作系统为 CentOS 7。
- 已在当前服务器中安装配置 Apache 服务器。

## 操作步骤

### 证书安装
1. 使用“WinSCP”，即本地与远程计算机间的复制文件工具，登录 Apache 服务器。
2. 将已获取到的 `1_root_bundle.crt` 证书文件、`2_www.domain.com.crt` 证书文件以及 `3_www.domain.com.key` 私钥文件从本地目录拷贝到 Apache 服务器的 `/etc/httpd/ssl` 目录下。
>? 若无 `/etc/httpd/ssl` 目录，可通过`mkdir /etc/httpd/ssl`命令行创建。
3. 关闭 WinSCP 界面。
4. 使用远程登录工具，登录 Apache 服务器。例如 “PuTTY” 工具。
5. 找到 `LoadModule ssl_module modules/mod_ssl.so`（用于加载 SSL 模块）和 `Include conf.modules.d/*.conf`（用于加载配置 SSL 的配置目录）配置语句，并确认该配置语句是否被注释。
 - 若已注释，请去掉首行的注释符号（`#`），并保存配置文件。
 - 若未注释，请执行下一步。
>? 由于操作系统的版本不同，目录结构也不同，请根据实际操作系统版本进行查找。`LoadModule ssl_module modules/mod_ssl.so` 和 `Include conf.modules.d/*.conf` 配置语句可能配置在以下配置文件中：
> - `conf.modules.d` 目录下的 00-ssl.conf 配置文件。
> - httpd.conf 配置文件。
> - http-ssl.conf 配置文件。
> 
> 若以上配置文件中均未找到 `LoadModule ssl_module modules/mod_ssl.so` 和 `Include conf.modules.d/*.conf` 配置语句，请确认是否已经安装 mod_ssl.so 模块。若未安装 mod_ssl.so 模块，您可通过执行`yum install mod_ssl` 命令进行安装。
> 
6. 编辑 `/etc/httpd/conf.d` 目录下的 ssl.conf 配置文件。修改如下内容：
>?首次安装的 Apache 服务器，`conf.d`目录默认在`/etc/httpd`下。
>
```
<VirtualHost 0.0.0.0:443>
		DocumentRoot "/var/www/html"
		ServerName www.domain.com
		SSLEngine on
		SSLCertificateFile /etc/httpd/ssl/2_www.domain.com_cert.crt
		SSLCertificateKeyFile /etc/httpd/ssl/3_www.domain.com.key
		SSLCertificateChainFile /etc/httpd/ssl/1_root_bundle.crt
</VirtualHost>
```
配置文件的主要参数说明如下：
 - SSLEngine on： 启用 SSL 功能
 - SSLCertificateFile：证书文件的路径
 - SSLCertificateKeyFile：私钥文件的路径
 - SSLCertificateChainFile：证书链文件的路径
7. 重新启动 Apache 服务器，即可使用 `https://www.domain.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）
如果您不知道网站可以通过 HTTPS 方式访问的情况，我们可以通过配置服务器，让其自动将 HTTP 的请求重定向到 HTTPS。您可以通过以下操作设置：
1. 编辑 `/etc/httpd/conf.d` 目录下的 httpd.conf 配置文件。
2. 请确认该配置文件是否存在`LoadModule rewrite_module modules/mod_rewrite.so`这一行。
 - 若存在，去掉`LoadModule rewrite_module modules/mod_rewrite.so`前面的 # 号。
 - 若不存在，可在`/etc/httpd/conf.modules.d`中新建一个 \*.conf 文件，例如 00-rewrite.conf。在新建文件中添加以下内容：
 ```
 LoadModule rewrite_module modules/mod_rewrite.so
```
 >?Apache 的版本不同，目录结构也会有所区别。具体请您参阅 Apache 官方的 rewrite 的文档 http://httpd.apache.org/docs/2.4/mod/mod_rewrite.html。
3. 修改如下内容：
```
<Directory "/var/www/html/app/src/htdocs_www"> 
# 新增
RewriteEngine on
RewriteCond %{SERVER_PORT} !^443$
RewriteRule ^(.*)?$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]
</Directory>
```
4. 重新启动 Apache 服务器，即可使用 `http://www.domain.com` 进行访问。

>!操作过程如果出现问题，请您 [联系我们]()。

