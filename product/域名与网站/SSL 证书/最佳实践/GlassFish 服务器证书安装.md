## 操作场景
本文档指导您如何在 GlassFish 服务器中安装 SSL 证书。
>?
>- 本文档以证书名称 `www.domain.com` 为例。
>- GlassFish 版本以 `glassfish5` 为例。
>- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。

## 前提条件
- 已准备文件远程拷贝软件，例如 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具，例如 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 已在当前服务器中安装配置 GlassFish 服务。
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

>!
>- 在腾讯云官网购买的云服务器，您可以登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)  获取服务器 IP 地址、用户名及密码。
- 当您申请 SSL 证书时选择了 “粘贴 CSR” 方式，则不提供 Tomcat 证书文件的下载，需要您通过手动转换格式的方式生成密钥库。其操作方法如下： 
 - 访问 [转换工具](https://myssl.com/cert_convert.html)。
 - 将 Nginx 文件夹中的证书文件和私钥文件上传至转换工具中，并填写密钥库密码，单击【提交】，转换为 jks 格式证书。
- 当前 GlassFish 服务器安装在 `/usr/local` 目录下。


## 操作步骤
1. 已在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中下载并解压缩 `www.domain.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 Tomcat 文件夹和 CSR 文件：
 - **文件夹名称**：Apache
 - **文件夹内容**：
    - 1_root_bundle.crt 证书文件
    - 2_www.domain.com.crt 证书文件
    - 3_www.domain.com.key 私钥文件
  - **CSR 文件内容**：	`www.domain.com.csr` 文件
  >?CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
2. 远程登录 GlassFish 服务器。例如，使用 [“PuTTY” 工具](https://cloud.tencent.com/document/product/213/35699#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4) 登录。
3. 进入部署证书步骤，在 `/usr/local/jboss-7.1.1/standalone/configuration` 目录下执行命令 `mkdir cert` 创建 cert 文件夹。
4. 使用 “WinSCP” （即本地与远程计算机间的复制文件工具）登录 GlassFish 服务器，将已获取到的 `www.domain.com.jks` 密钥库文件从本地目录拷贝至 cert 文件夹。
5. 编辑在 `/usr/local/jboss-7.1.1/standalone/configuration` 目录下的 `standalone.xml` 文件。修改端口配置，如下内容：
6. 进入 `/usr/local/jboss-7.1.1/bin` 目录下，执行启动命令 `./standalone.sh`，确保正常启动。如下图所示：
7. 证书已部署完成，即可使用 `https://www.domain.com` 访问。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。

