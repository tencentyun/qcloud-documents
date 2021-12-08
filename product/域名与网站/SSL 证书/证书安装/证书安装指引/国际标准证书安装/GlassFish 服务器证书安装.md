## 操作场景
本文档指导您如何在 GlassFish 服务器中安装 SSL 证书。
>?
>- 本文档以证书名称 `cloud.tencent.com` 为例。
>- GlassFish 版本以 `glassfish-4.0` 为例。
>- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 GlassFish 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>- SSL 证书文件上传至服务器方法可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

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
- 当您申请 SSL 证书时选择 “粘贴 CSR” 方式，或购买的品牌证书为 Wotrus，则不提供 Tomcat 证书文件的下载，需要您通过手动转换格式的方式生成密钥库。其操作方法如下： 
 - 访问 [转换工具](https://myssl.com/cert_convert.html)。
 - 将 Nginx 文件夹中的证书文件和私钥文件上传至转换工具中，并填写密钥库密码，单击**提交**，转换为 jks 格式证书。
- 当前 GlassFish 服务安装在 `/usr/share` 目录下。


## 操作步骤
1. 请在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中选择您需要安装的证书并单击**下载**。
2. 在弹出的 “证书下载” 窗口中，服务器类型选择 **Apache**、**JKS**，单击**下载**并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 `cloud.tencent.com_apache` 文件夹、`cloud.tencent.com_jks` 文件夹：
 - **文件夹名称**：`cloud.tencent.com_apache`
    - `cloud.tencent.com.crt` 证书文件
    - `cloud.tencent.com.key` 私钥文件
  - **CSR 文件内容**：	`cloud.tencent.com.csr` 文件
>?CSR 文件是申请证书时由您上传或系统在线生成的，提供给 CA 机构。安装时可忽略该文件。
2. 远程登录 GlassFish 服务器。例如，使用 [“PuTTY” 工具](https://cloud.tencent.com/document/product/213/35699#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4) 登录。
3. 进入 `/usr/share/glassfish4/glassfish/bin` 目录下执行命令 `./asadmin` 后，需更换 domain 的管理密码，请执行命令 `change-master-password --savemasterpassword=true domain1`。如下图所示：
>!
>- domain1 安装默认路径为 `/usr/share/glassfish4/glassfish/domains`，domain 名称请根据实际情况填写。
>- 默认密码为 changeit，请输入回车后再输入新密码，新密码请填写申请证书时设置的**私钥密码**。
>- 若申请证书时未设置私钥密码，则填写 `cloud.tencent.com_jks` 文件夹中 `keystorePass.txt` 文件的密码。
>
4. 在 `/usr/share` 目录下执行命令 `mkdir temp` 创建 temp 文件夹。
5.  使用 “WinSCP” （即本地与远程计算机间的复制文件工具）登录 GlassFish 服务器，将 `cloud.tencent.com.crt` 证书文件、`cloud.tencent.com.key` 私钥文件从本地目录拷贝至 temp 文件夹。
6. 在 temp 目录执行以下命令生成 PKCS12 文件，并提示输入密码，请输入新设置的密码，即私钥密码。如下所示：
```
openssl pkcs12 -export -in cloud.tencent.com.crt -inkey cloud.tencent.com.key -out mycert.p12 -name s1as
```
7. 在 temp 目录下执行命令 `ls -l` 确认 PKCS12 文件是否包含您申请的证书。
8. 生成 `keystore.jks` 文件，请在 temp 目录执行以下命令，则生成的 `keystore.jks` 文件显示在此目录下。如下所示：
```
keytool -importkeystore -destkeystore keystore.jks -srckeystore mycert.p12 -srcstoretype PKCS12 -alias s1as
```
9. 生成 `cacert.jks` 文件，请在 temp 目录执行以下命令，则生成的 `cacert.jks` 文件显示在此目录下。若提示输入密码，输入新设置的密码，即私钥密码。如下所示：
```
keytool -importcert -trustcacerts -destkeystore cacerts.jks -file cloud.tencent.com.crt -alias s1as
```
执行命令后若提示是否信任此证书，请按图示进行操作。
![](https://main.qcloudimg.com/raw/aee68705e1e8b135d47bda9af499e15f.png)
10. 将步骤8和步骤9生成的文件替换 `domain1/config` 目录下的 `keystore.jks` 和 `cacert.jks` 文件。
11. 编辑 `/usr/share/glassfish4/glassfish/domains/domain1/config` 目录下的 `domain.xml` 文件，修改端口号。如下所示：
```
<network-listeners>
          <network-listener port="80" protocol="http-listener-1" transport="tcp" name="http-listener-1" thread-pool="http-thread-pool"></network-listener>
          <network-listener port="443" protocol="http-listener-2" transport="tcp" name="http-listener-2" thread-pool="http-thread-pool"></network-listener>
          <network-listener port="4848" protocol="admin-listener" transport="tcp" name="admin-listener" thread-pool="admin-thread-pool"></network-listener>
        </network-listeners>
```
12. 启动 GlassFish 服务器，即可使用 `https://cloud.tencent.com` 进行访问。如下图所示：
![](https://main.qcloudimg.com/raw/fcdf919a22f0c9b07bc837e4d9a5e269.png)

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。


