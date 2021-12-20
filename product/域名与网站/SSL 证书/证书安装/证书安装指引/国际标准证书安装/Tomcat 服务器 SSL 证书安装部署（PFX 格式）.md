## 操作场景
本文档指导您如何在 Tomcat 服务器中安装 PFX 格式 SSL 证书。

>?
- 文档以证书名称 `cloud.tencent.com` 为例。
- Tomcat 版本以 `tomcat9.0.40` 为例。
- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。
- 若您需在 Tomcat 服务器中安装 JKS 格式 SSL 证书。具体可参考：[Tomcat 服务器 SSL 证书安装部署（JKS 格式）](https://cloud.tencent.com/document/product/400/35224)。
- 安装 SSL 证书前，请您在 Tomcat 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考：[服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
- SSL 证书文件上传至服务器方法可参考：[如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

## 前提条件
- 已准备文件远程拷贝软件，例如 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具，例如 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 已在当前服务器中安装配置 Tomcat 服务。
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

>!
>- 在腾讯云官网购买的云服务器，您可以登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)  获取服务器 IP 地址、用户名及密码。
- 当前 Tomcat 服务器安装在`/usr`目录下，例如，Tomcat 文件夹名称为 `tomcat9.0.40`。则 `/usr/*/conf` 实际为 `/usr/tomcat9.0.40/conf`。

# 操作步骤

### 证书安装

1. 请在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中选择您需要安装的证书并单击**下载**。
2. 在弹出的 “证书下载” 窗口中，服务器类型选择 **Tomcat**，单击**下载**并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含  `cloud.tencent.com_tomcat` 文件夹：
 - **文件夹名称**：`cloud.tencent.com_tomcat`
 - **文件夹内容**：
    - `cloud.tencent.com.pfx` 证书文件
    - `cloud.tencent.com.key` 密钥文件
    - `keystorePass.txt` 密码文件（若已设置私钥密码，则无 `keystorePass.txt` 密码文件）
3. 使用 “WinSCP” （即本地与远程计算机间的复制文件工具）登录 Tomcat 服务器。
4. 将已获取到的 `cloud.tencent.com.pfx` 证书文件从本地目录拷贝至 `/usr/*/conf` 目录下。
5. 远程登录 Tomcat  服务器。例如，使用 [“PuTTY” 工具](https://cloud.tencent.com/document/product/213/35699#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4) 登录。
6. 编辑在 `/usr/*/conf` 目录下的 `server.xml` 文件。并根据实际需求从以下方式中选择一种进行操作：
>?使用方式1配置时，Tomcat 将自动为您选择 SSL 的实现方式。如果您按照方式1无法完成后续配置，可能是因为您的环境不支持该实现方式。您可以根据环境属性，使用方式2手动选择 SSL 进行配置。
>
<dx-tabs>
::: 方式1：自动选择 SSL
修改 `server.xml` 文件 `Connector`的属性为以下内容：
```
<Connector port="443"  
protocol="HTTP/1.1"
    SSLEnabled="true"
    scheme="https"
    secure="true"
    keystoreFile="/usr/*/conf/cloud.tencent.com.pfx" #证书保存的路径
    keystoreType="PKCS12"
    keystorePass="证书密码"  # 请替换为 keystorePass.txt 密码文件中的内容。
    clientAuth="false"
    SSLProtocol="TLSv1.1+TLSv1.2+TLSv1.3"
    ciphers="TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256,TLS_RSA_WITH_AES_128_CBC_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA256"/>
```
:::
::: 方式2：手动选择 SSL 
修改 `server.xml` 文件 `Connector` 的属性为以下内容：
```
<Connector
    protocol="org.apache.coyote.http11.Http11NioProtocol"
    port="443" maxThreads="200"
    scheme="https" secure="true" SSLEnabled="true"
    keystoreFile="/usr/*/conf/cloud.tencent.com.pfx" keystorePass="证书密码" #pfx替换为证书保存的路径、证书密码请替换为 keystorePass.txt 密码文件中的内容。
    clientAuth="false" sslProtocol="TLS"/>
```
:::
</dx-tabs>

配置文件的主要参数说明如下：
 - **keystoreFile**：证书文件的存放位置，可以指定绝对路径，也可以指定相对于 &lt;CATALINA_HOME&gt; （Tomcat 安装目录）环境变量的相对路径。如果此项没有设定，默认情况下，Tomcat 将从当前操作系统用户的用户目录下读取名为 “.keystore” 的文件。
 - **keystorePass**：密码文件密码，指定 keystore 的密码。申请证书时若设置了私钥密码，请填写私钥密码；若申请证书时未设置私钥密码，请填写`cloud.tencent.com_tomcat` 文件夹中 keystorePass.txt 文件内的密码。
 - **clientAuth**：如果设为 true，表示 Tomcat 要求所有的 SSL 客户出示安全证书，对 SSL 客户进行身份验证。
 
7. 确认 Tomcat 服务器是否启动。
   - 若已启动，您需要在 `/usr/*/bin` 目录下依次执行以下命令，关闭和重启 Tomcat 服务器。
```
./shutdown.sh  (关闭 Tomcat 服务器)
./startup.sh   (启动 Tomcat 服务器)
```
 - 若未启动，您需要在 `/usr/*/bin` 目录下执行以下命令，启动 Tomcat 服务器。
 ```
./startup.sh
```
8. 若启动成功，即可使用 `https://cloud.tencent.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）
如果您需要将 HTTP 请求自动重定向到 HTTPS。您可以通过以下操作设置：

1. 编辑  `/usr/*/conf` 目录下的 `web.xml` 文件，找到 <\/welcome-file-list> 标签。
2. 请在结束标签 <\/welcome-file-list> 后面换行，并添加以下内容。
```
<login-config>  
    <!-- Authorization setting for SSL -->  
    <auth-method>CLIENT-CERT</auth-method>  
    <realm-name>Client Cert Users-only Area</realm-name>  
</login-config>  
<security-constraint>  
    <!-- Authorization setting for SSL -->  
    <web-resource-collection >  
        <web-resource-name >SSL</web-resource-name>  
        <url-pattern>/*</url-pattern>  
    </web-resource-collection>  
    <user-data-constraint>  
        <transport-guarantee>CONFIDENTIAL</transport-guarantee>  
    </user-data-constraint>  
</security-constraint>
```
3. 编辑 `/usr/*/conf` 目录下的 `server.xml` 文件，将 redirectPort 参数修改为 SSL 的 connector 的端口，即443端口。如下所示：
```
<Connector port="80" protocol="HTTP/1.1"
  connectionTimeout="20000"
  redirectPort="443" />
```
>? 此修改操作可将非 SSL 的 connector 跳转到 SSL 的 connector 中。
>
4. 在 `/usr/*/bin` 目录下执行以下命令，关闭 Tomcat 服务器。
```
./shutdown.sh
```
5. 执行以下命令，确认配置是否存在问题。
```
./configtest.sh
```
 - 若存在，请您重新配置或者根据提示修改存在问题。
 - 若不存在，请执行下一步。
6. 执行以下命令，启动 Tomcat 服务器，即可使用 `http://cloud.tencent.com` 进行访问。
```
./startup.sh
```

