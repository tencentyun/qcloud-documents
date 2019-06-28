## 操作场景
本文档指导您如何在 Apache 服务器中安装 SSL 证书。
>?
>- 本文档以证书名称 `www.domain.com` 为例。
>- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。

## 前提条件
- 已在 SSL 证书管理控制台 中下载并解压缩 `www.domain.com` 证书文件包到本地目录。
解压缩后，可获得 Apache 文件夹和 CSR 文件：
 - **文件夹名称**：Apache
 - **文件夹内容**：
    - `1_root_bundle.crt` 证书文件
    - `2_www.domain.com.crt` 证书文件
    - `3_www.domain.com.key` 私钥文件
  - **CSR 文件内容**：	`www.domain.com.csr` 文件。
- 已准备远程拷贝软件 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 已在当前服务器中安装配置 Apache 服务器。

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
1. 使用 “WinSCP”（即本地与远程计算机间的复制文件工具）登录 Apache 服务器。
2. 将已获取到的 `1_root_bundle.crt` 证书文件、`2_www.domain.com.crt` 证书文件以及 `3_www.domain.com.key` 私钥文件从本地目录拷贝到 Apache 服务器的 `/etc/httpd/ssl` 目录下。
>? 若无 `/etc/httpd/ssl` 目录，可通过 `mkdir /etc/httpd/ssl` 命令行创建。
3. 关闭 WinSCP 界面。
4. 使用远程登录工具，登录 Apache 服务器。例如 “PuTTY” 工具。
5. 找到 `LoadModule ssl_module modules/mod_ssl.so`（用于加载 SSL 模块）和 `Include conf.modules.d/*.conf`（用于加载配置 SSL 的配置目录）配置语句，并确认该配置语句是否被注释。
 >? 由于操作系统的版本不同，目录结构也不同，请根据实际操作系统版本进行查找。`LoadModule ssl_module modules/mod_ssl.so` 和 `Include conf.modules.d/*.conf` 配置语句可能配置在以下配置文件中：
> - `conf.modules.d` 目录下的 00-ssl.conf 配置文件。
> - httpd.conf 配置文件。
> - http-ssl.conf 配置文件。
> 
> 若以上配置文件中均未找到 `LoadModule ssl_module modules/mod_ssl.so` 和 `Include conf.modules.d/*.conf` 配置语句，请确认是否已经安装 mod_ssl.so 模块。若未安装 mod_ssl.so 模块，您可通过执行`yum install mod_ssl` 命令进行安装。
> 
 - 若已注释，请去掉首行的注释符号（`#`），保存配置文件，并执行 [步骤6](#step6)。
 - 若未注释，请执行 [步骤6](#step6)。
<span id="step6"></span>
6. 编辑 `/etc/httpd/conf.d` 目录下的 ssl.conf 配置文件。修改如下内容：
>?首次安装的 Apache 服务器，`conf.d` 目录默认在 `/etc/httpd` 目录下。
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
 - **SSLEngine on**： 启用 SSL 功能
 - **SSLCertificateFile**：证书文件的路径
 - **SSLCertificateKeyFile**：私钥文件的路径
 - **SSLCertificateChainFile**：证书链文件的路径
7. 重新启动 Apache 服务器，即可使用 `https://www.domain.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）
若您不了解通过 HTTPS 访问网站的方式，可以通过配置服务器，让其自动将 HTTP 的请求重定向到 HTTPS。您可以通过以下操作设置：
1. 编辑 `/etc/httpd/conf` 目录下的 httpd.conf 配置文件。
>!
>- Apache 的版本不同，目录结构也会有所区别。具体请您参阅 [Apache 官方 rewrite 的文档](http://httpd.apache.org/docs/2.4/mod/mod_rewrite.html)。
>- httpd.conf 配置文件所在目录不唯一，您可以根据 `/etc/httpd/*` 逐一查找。
2. 请确认该配置文件是否存在`LoadModule rewrite_module modules/mod_rewrite.so`。
 - 若存在，请去掉`LoadModule rewrite_module modules/mod_rewrite.so`前面的注释符号（`#`）号。并执行 [步骤4](#step4)。
 - 若不存在，请执行 [步骤3](#step3)。
 <span id="step3"></span>
3. 请您在`/etc/httpd/conf.modules.d`中新建一个 \*.conf 文件，例如 00-rewrite.conf。在新建文件中添加以下内容：
 ```
 LoadModule rewrite_module modules/mod_rewrite.so
```
<span id="step4"></span>
4. 在 httpd.conf 配置文件中添加如下内容：
```
<Directory "/var/www/html"> 
# 新增
RewriteEngine on
RewriteCond %{SERVER_PORT} !^443$
RewriteRule ^(.*)?$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]
</Directory>
```
4. 重新启动 Apache 服务器，即可使用 `http://www.domain.com` 进行访问。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。

