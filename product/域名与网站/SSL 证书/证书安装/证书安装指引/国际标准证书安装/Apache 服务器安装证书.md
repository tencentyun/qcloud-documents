## 操作场景
本文档指导您如何在 Apache 服务器中安装 SSL 证书。
>?
>- 本文档以证书名称 `cloud.tencent.com` 为例。
>- Apache 版本以 `Apache/2.4.6` 为例。默认端口为 `80`。
>- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 Apache 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>- SSL 证书文件上传至服务器方法可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

## 前提条件
- 已准备远程文件拷贝软件，例如 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具，例如 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 已在当前服务器中安装配置 Apache 服务。
- 安装 SSL 证书前需准备的数据如下：
<table>
<tr>
<td>名称</td>
<td>说明</td>
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
1. 已在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中下载并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。 其中包含 Apache 文件夹和 CSR 文件：
 - **文件夹名称**：`cloud.tencent.com_apache`
 - **文件夹内容**：
    - `root_bundle.crt` 证书文件
    - `cloud.tencent.com.crt` 证书文件
    - `cloud.tencent.com.key` 私钥文件
  - **CSR 文件内容**：	`cloud.tencent.com.csr` 文件
>?CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
2. 使用 “WinSCP”（即本地与远程计算机间的复制文件工具）登录 Apache 服务器。
3. 将已获取到的 `root_bundle.crt` 证书文件、`cloud.tencent.com.crt` 证书文件以及 `cloud.tencent.com.key` 私钥文件从本地目录拷贝到 Apache 服务器的 `/etc/httpd/ssl` 目录下。
>? 若无 `/etc/httpd/ssl` 目录，可通过 `mkdir /etc/httpd/ssl` 命令行创建。
4. 远程登录 Apache 服务器。例如，使用 [“PuTTY” 工具](https://cloud.tencent.com/document/product/213/35699#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4) 登录。
>?首次安装的 Apache 服务器，`conf.d`、`conf`、`conf.modules.d` 等目录默认在 `/etc/httpd` 目录下。
5. 在 `/etc/httpd/conf` 目录下的 httpd.conf 配置文件找到 `Include conf.modules.d/*.conf`（用于加载配置 SSL 的配置目录）配置语句，并确认该配置语句未被注释。若已注释，请去掉首行的注释符号（`#`），保存配置文件。
6. 在 `/etc/httpd/conf.modules.d` 目录下的 00-ssl.conf 配置文件找到 `LoadModule ssl_module modules/mod_ssl.so`（用于加载 SSL 模块）配置语句，并确认该配置语句未被注释，若已注释，请去掉首行的注释符号（`#`），保存配置文件。
>! 由于操作系统的版本不同，目录结构也不同，请根据实际操作系统版本进行查找。
> 若以上配置文件中均未找到 `LoadModule ssl_module modules/mod_ssl.so` 和 `Include conf.modules.d/*.conf` 配置语句，请确认是否已经安装 mod_ssl.so 模块。若未安装 mod_ssl.so 模块，您可通过执行`yum install mod_ssl` 命令进行安装。
7. 编辑 `/etc/httpd/conf.d` 目录下的 ssl.conf 配置文件。修改如下内容：
```
<VirtualHost 0.0.0.0:443>
		DocumentRoot "/var/www/html" 
		#填写证书名称
		ServerName cloud.tencent.com 
		#启用 SSL 功能
		SSLEngine on 
		#证书文件的路径
		SSLCertificateFile /etc/httpd/ssl/cloud.tencent.com.crt 
		#私钥文件的路径
		SSLCertificateKeyFile /etc/httpd/ssl/cloud.tencent.com.key 
		#证书链文件的路径
		SSLCertificateChainFile /etc/httpd/ssl/root_bundle.crt 
</VirtualHost>
```
8. 重新启动 Apache 服务器，即可使用 `https://cloud.tencent.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）
如果您需要将 HTTP 请求自动重定向到 HTTPS。您可以通过以下操作设置：
1. 编辑 `/etc/httpd/conf` 目录下的 httpd.conf 配置文件。
>!
>- Apache 的版本不同，目录结构也会有所区别。具体请您参阅 [Apache 官方 rewrite 的文档](http://httpd.apache.org/docs/2.4/mod/mod_rewrite.html)。
>- httpd.conf 配置文件所在目录不唯一，您可以根据 `/etc/httpd/*` 逐一查找。
2. 请确认该配置文件是否存在`LoadModule rewrite_module modules/mod_rewrite.so`。
 - 若存在，请去掉`LoadModule rewrite_module modules/mod_rewrite.so`前面的注释符号（`#`）号。并执行 [步骤4](#step4)。
 - 若不存在，请执行 [步骤3](#step3)。
[](id:step3)
3. 请您在`/etc/httpd/conf.modules.d`中新建一个 \*.conf 文件，例如 00-rewrite.conf。在新建文件中添加以下内容：
 ```
 LoadModule rewrite_module modules/mod_rewrite.so
```
[](id:step4)
4. 在 httpd.conf 配置文件中添加如下内容：
```
<Directory "/var/www/html"> 
# 新增
RewriteEngine on
RewriteCond %{SERVER_PORT} !^443$
RewriteRule ^(.*)?$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]
</Directory>
```
4. 重新启动 Apache 服务器，即可使用 `http://cloud.tencent.com` 进行访问。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。


