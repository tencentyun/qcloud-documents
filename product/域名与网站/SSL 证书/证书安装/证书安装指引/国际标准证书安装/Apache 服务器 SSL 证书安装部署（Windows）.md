## 操作场景
本文档指导您如何在 Apache 服务器中安装 SSL 证书。
>?
>- 本文档以证书名称 `cloud.tencent.com` 为例。
>- Apache 版本以 `Apache/2.4.6` 为例。默认端口为 `80`。
>- 当前服务器的操作系统为 Windows Server 2012 R2，由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 Apache 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>- SSL 证书文件上传至服务器方法可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

## 前提条件
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

### 步骤1：上传证书文件
1. 已在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中下载并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。 其中包含 `cloud.tencent.com_apache` 文件：
 - **文件夹名称**：`cloud.tencent.com_apache`
 - **文件夹内容**：
    - `root_bundle.crt` 证书文件
    - `cloud.tencent.com.crt` 证书文件
    - `cloud.tencent.com.key` 私钥文件
    - `cloud.tencent.com.csr` CSR 文件
>?CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
2. 通过 RDP 登录 Apache 服务器。
>?上传操作可参考：[通过 RDP 方式上传文件到云服务器](https://cloud.tencent.com/document/product/213/39101)。
>
3. 将已获取到的 `root_bundle.crt` 证书文件、`cloud.tencent.com.crt` 证书文件以及 `cloud.tencent.com.key` 私钥文件从本地目录拷贝到 Apache 服务器目录的 `\conf` 目录的下的 `ssl.crt` 与 `ssl.key` 文件夹。对应文件目录如下图所示：
 ![](https://main.qcloudimg.com/raw/ef118dd35480d06baf340a39183a87d5.png)
<table>
<thead>
  <tr>
    <th>SSL 证书文件</th>
    <th>对应文件夹</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>root_bundle.crt</td>
    <td rowspan="2">ssl.crt</td>
  </tr>
  <tr>
    <td>cloud.tencent.com.crt</td>
  </tr>
  <tr>
    <td>cloud.tencent.com.key</td>
    <td>ssl.key</td>
  </tr>
</tbody>
</table>



### 步骤2：配置文件
1. 使用文本编辑器，打开 Apache 服务器 `conf` 目录下 `httpd.conf` 文件，并删除以下字段前 `#` 注释符。
```java
#LoadModule ssl_module modules/mod_ssl.so
#Include conf/extra/httpd-ssl.conf
```
2. 使用文本编辑器，打开 Apache 服务器 `conf\extra` 目录下 `httpd-ssl.conf` 文件。如下图所示：
![](https://main.qcloudimg.com/raw/97142cb8fe3e2f0cbc267eb7a4c8279f.png)
3. 修改 `httpd-ssl.conf` 文件，将以下字段参数设置为上传的证书文件路径，如下所示：
```java
SSLCertificateFile "C:/apache/conf/ssl.crt/cloud.tencent.com.crt"
SSLCertificateKeyFile "C:/apache/conf/ssl.key/cloud.tencent.com.key"
SSLCertificateChainFile "C:/apache/conf/ssl.crt/root_bundle.crt"
```
4. 重新启动 Apache 服务器，即可使用 `https://cloud.tencent.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）

1. 使用文本编辑器，打开 Apache 服务器 `conf` 目录下 `httpd.conf` 文件，并删除以下字段前 `#` 注释符。
```java
#LoadModule rewrite_module modules/mod_rewrite.so
```
2. 并在网站运行目录配置字段。如： `<Directory "C:/xampp/htdocs">` 字段中添加如下内容：
```java
<Directory "C:/xampp/htdocs">
RewriteEngine on
RewriteCond %{SERVER_PORT} !^443$
RewriteRule ^(.*)?$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]
</Directory>
```
3. 重新启动 Apache 服务器，即可使用 `http://cloud.tencent.com` 与 `https://cloud.tencent.com` 进行访问。访问后都将自动跳转到 `https://cloud.tencent.com`。


