## 操作场景
本文以使用 LAMP 应用镜像的轻量应用服务器为例，介绍如何在服务器中安装 SSL 证书并开启 HTTPS 访问。该服务器中默认已安装 Apache 软件，您可参考本文并结合实际情况进行操作。

<dx-alert infotype="explain" title="">
本文档以通过腾讯云 SSL 证书服务申请的付费、免费证书为例。腾讯云 SSL 证书服务相关信息可参考 [SSL 证书产品介绍](https://cloud.tencent.com/document/product/400/7572)、[SSL 证书购买指南](https://cloud.tencent.com/document/product/400/7994) 和 [申请免费 SSL 证书](https://cloud.tencent.com/document/product/400/6814)。
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
1. 前往 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl)，下载并解压缩 SSL 证书（名称以 `cloud.tencent.com` 为例）文件压缩包到本地目录。
解压缩后，获得相关类型的证书文件。其中包含 Apache 文件夹和 CSR 文件：
 - **文件夹名称**：Apache
 - **文件夹内容**：
    - `1_root_bundle.crt` 证书文件
    - `2_cloud.tencent.com.crt` 证书文件
    - `3_cloud.tencent.com.key` 私钥文件
 - **CSR 文件内容**：`cloud.tencent.com.csr` 文件
 <dx-alert infotype="explain" title="">
CSR 文件是申请证书时由您上传或系统在线生成的，用于提供给 CA 机构。安装时可忽略该文件。
</dx-alert>
2. 参考 [使用 WebShell 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录轻量应用服务器。
3. 依次执行以下命令，进入 Apache 安装目录并创建 ssl 文件夹。
```
cd /usr/local/lighthouse/softwares/apache
```
```
sudo mkdir ssl
```
4. 将已获取到的 `1_root_bundle.crt` 证书文件、`2_cloud.tencent.com.crt` 证书文件以及 `3_cloud.tencent.com.key` 私钥文件从本地目录拷贝到已创建的 `/usr/local/lighthouse/softwares/apache/ssl` 目录下。  
5. 执行以下命令，编辑配置文件 httpd.conf。
```
sudo vim /usr/local/lighthouse/softwares/apache/conf/httpd.conf
```
6. 按 **i** 进入编辑模式，进行如下修改：
   1. 删除 `#LoadModule ssl_module modules/mod_ssl.so` 行首的 `#`。
   2. 删除 `#LoadModule socache_shmcb_module modules/mod_socache_shmcb.so` 行首的 `#`。
   3. 将 `ServerName localhost` 中的 `localhost` 替换为证书名称。本文修改后示例如下：
```
ServerName cloud.tencent.com
```
   4. 删除 `#Include conf/extra/httpd-ssl.conf` 行首的 `#`。
7. 按 **Esc** 并输入 **:wq**，保存修改。
8. 执行以下命令，修改配置文件 httpd-ssl.conf。
```
sudo vim /usr/local/lighthouse/softwares/apache/conf/extra/httpd-ssl.conf
```
9. 按 **i** 进入编辑模式，在 `<VirtualHost _default_:443>` 中进行如下修改：
   1. 将 `ServerName www.example.com:443` 中的 `www.example.com:443` 替换为证书名称。本文修改后示例如下：
```
ServerName cloud.tencent.com
```
   2. 修改证书文件路径：
<dx-codeblock>
::: plaintext 
SSLCertificateFile "/usr/local/lighthouse/softwares/apache/ssl/2_cloud.tencent.com.crt"
SSLCertificateKeyFile "/usr/local/lighthouse/softwares/apache/ssl/3_cloud.tencent.com.key"
SSLCertificateChainFile "/usr/local/lighthouse/softwares/apache/ssl/1_root_bundle.crt"
:::
</dx-codeblock>
  3. 增加以下内容：
```
<Directory "/usr/local/lighthouse/softwares/apache/htdocs">
          Options Indexes FollowSymLinks
          AllowOverride all
          Require all granted
</Directory>
```
10. 按 **Esc** 并输入 **:wq**，保存修改。
11. 执行以下命令，重启 Apache 服务。
```
sudo /usr/local/lighthouse/softwares/apache/bin/httpd -k restart
```
重启成功后即可使用 `https://cloud.tencent.com` 进行访问。如下图所示：
![](https://main.qcloudimg.com/raw/29d3b81c61d0fbb974703a3ab9140f9f.png)

### 设置 HTTP 请求自动跳转 HTTPS（可选）
您可以通过配置服务器，让其自动将 HTTP 的请求重定向到 HTTPS。可以参考以下步骤进行设置：

1. 执行以下命令，编辑配置文件 httpd.conf。
```
sudo vim /usr/local/lighthouse/softwares/apache/conf/httpd.conf
```
2. 按 **i** 进入编辑模式，进行如下修改：
   1. 删除 `#LoadModule rewrite_module modules/mod_rewrite.so` 行首的 `#`。
   2. 找到 &lt;Directory &quot;/home/www/htdocs/&quot;&gt;，增加如下内容： 
```
RewriteEngine on
RewriteCond %{SERVER_PORT} !^443$
RewriteRule ^(.*)?$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R]
```
修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/bf7abb0339ef8093b2e6756a64b3b29e.png)
3. 按 **Esc** 并输入 **:wq**，保存修改。
4. 执行以下命令，重启 Apache 服务。
```
sudo /usr/local/lighthouse/softwares/apache/bin/httpd -k restart
```
至此已成功设置 HTTPS 的自动跳转，您可使用 `http://cloud.tencent.com` 自动跳转至 HTTPS 页面。
 
