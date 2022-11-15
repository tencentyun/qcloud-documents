## 操作场景
本文以使用 Windows Server 2012 R2 系统镜像的轻量应用服务器为例，介绍如何在服务器中安装 SSL 证书并开启 HTTPS 访问。

<dx-alert infotype="explain" title="">
本文档以通过腾讯云 SSL 证书服务申请的付费、免费证书为例。腾讯云 SSL 证书服务相关信息可参考 [SSL 证书产品介绍](https://cloud.tencent.com/document/product/400/7572)、[SSL 证书购买指南](https://cloud.tencent.com/document/product/400/7994) 和 [申请免费 SSL 证书](https://cloud.tencent.com/document/product/400/6814)。
</dx-alert>



## 示例信息
- **证书名称**：以 `cloud.tencent.com` 为例。
- **Apache 版本**：以 `Apache/2.4.53` 为例。您可前往 [Apache 官网](https://httpd.apache.org/download.cgi/) 进行下载，若您需要采用其余版本，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。
- **操作系统**：以 Windows Server 2012 R2 为例。若您实际使用的操作系统版本不同，则详细操作步骤可能略有区别。


## 前提条件
- 已在当前服务器中安装配置 Apache 服务。
- 轻量应用服务器创建完成后，防火墙默认已开启 `443` 及 `80` 端口。建议您在安装 SSL 证书前，前往防火墙页面确认已开启 `443` 及 `80` 端口，避免证书安装后无法启用 HTTPS。详情请参见 [管理防火墙](https://cloud.tencent.com/document/product/1207/44577)。
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
<td>登录轻量应用服务器操作系统的用户名，例如 Administrator。</td>
</tr>
<tr>
<td>密码</td>
<td>登录轻量应用服务器操作系统所使用的用户名对应的密码。</td>
</tr>
</table>
<dx-alert infotype="notice" title="">
您可以登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse) 找到对应的服务器实例，进入实例详情页查看服务器的公网 IP 地址。如果该实例创建后未重置密码，请您执行重置密码操作并牢记密码。详情请参见 [重置密码](https://cloud.tencent.com/document/product/1207/44575)。
</dx-alert>




## 操作步骤

### 上传证书文件
1. 请在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中选择您需要安装的证书并单击**下载**。
2. 在弹出的“证书下载”窗口中，服务器类型选择 **Apache**，单击**下载**并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
   解压缩后，可获得相关类型的证书文件。 其中包含 `cloud.tencent.com_apache` 文件：
 - **文件夹名称**：`cloud.tencent.com_apache`
 - **文件夹内容**：
    - `root_bundle.crt` 证书文件
    - `cloud.tencent.com.crt` 证书文件
    - `cloud.tencent.com.key` 私钥文件
    - `cloud.tencent.com.csr` CSR 文件
<dx-alert infotype="explain" title="">
CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
</dx-alert>
3. 参考 [使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/1207/44579)，登录轻量应用服务器。
4. [](id:Step4)将已获取到的 `root_bundle.crt` 证书文件、`cloud.tencent.com.crt` 证书文件以及 `cloud.tencent.com.key` 私钥文件从本地目录拷贝到 Apache 服务器。可参考 [如何将本地文件拷贝到轻量应用服务器](https://cloud.tencent.com/document/product/1207/53135) 上传证书文件。
本文以拷贝至 `\conf` 目录的下的 `ssl.crt` 与 `ssl.key` 文件夹为例，您可自定义文件位置。本文对应文件目录如下图所示：
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




### 配置文件
1. 使用文本编辑器，打开 Apache 服务器 `conf` 目录下 `httpd.conf` 文件，并删除以下字段前 `#` 注释符。
```plaintext
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
<dx-alert infotype="explain" title="">
若 `httpd-ssl.conf` 配置文件中无 `SSLCertificateChainFile` 项，则在对应位置添加即可。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6c992ecb83aeb1bf048d52b753f39704.png)
</dx-alert>
4. 重新启动 Apache 服务器，即可使用 `https://cloud.tencent.com` 进行访问。
若重启时报 “AH00526: Syntax error on line 18 of C:/apache/conf/extra/httpd-ahssl.conf:Cannot define multiple Listeners on the same IP:port” 错误，则说明监听端口有冲突，请将 `conf\extra\httpd-ahssl.conf` 中监听的 `443` 端口替换为其他端口。


### HTTP 自动跳转 HTTPS 的安全配置（可选）

1. 使用文本编辑器，打开 Apache 服务器 `conf` 目录下 `httpd.conf` 文件，并删除以下字段前 `#` 注释符。
```plaintext
#LoadModule rewrite_module modules/mod_rewrite.so
```
2. 并在网站运行目录配置字段。如： `<Directory "C:/xampp/htdocs">` 字段中添加如下内容：
```plaintext
<Directory "C:/xampp/htdocs">
RewriteEngine on
RewriteCond %{SERVER_PORT} !^443$
RewriteRule ^(.*)?$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]
</Directory>
```
3. 重新启动 Apache 服务器，即可使用 `http://cloud.tencent.com` 与 `https://cloud.tencent.com` 进行访问。访问后都将自动跳转到 `https://cloud.tencent.com`。


