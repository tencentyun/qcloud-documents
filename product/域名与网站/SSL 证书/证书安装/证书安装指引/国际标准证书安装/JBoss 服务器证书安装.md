## 操作场景
本文档指导您如何在 JBoss 服务器中安装 SSL 证书。
>?
>- 本文档以证书名称 `cloud.tencent.com` 为例。
>- JBoss 版本以 `jboss-7.1.1` 为例。
>- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 JBoss 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>- SSL 证书文件上传至服务器方法可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

## 前提条件
- 已准备文件远程拷贝软件，例如 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具，例如 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 已在当前服务器中安装配置 JBoss 服务。
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
- 当前 JBoss 服务器安装在 `/usr/local` 目录下。


## 操作步骤
1. 请在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中选择您需要安装的证书并单击**下载**。
2. 在弹出的 “证书下载” 窗口中，服务器类型选择 **JKS**，单击**下载**并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 `cloud.tencent.com_jks` 文件夹：
 - **文件夹名称**：`cloud.tencent.com_jks`
 - **文件夹内容**：
    - `cloud.tencent.com.jks` 密钥库
    - `cloud.tencent.com.key` 私钥文件
    - `keystorePass.txt` 密码文件（若已设置私钥密码，则无 `keystorePass.txt` 密码文件）
3. 远程登录 JBoss 服务器。例如，使用 [“PuTTY” 工具](https://cloud.tencent.com/document/product/213/35699#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4) 登录。
4. 进入部署证书步骤，在 `/usr/local/jboss-7.1.1/standalone/configuration` 目录下执行命令 `mkdir cert` 创建 cert 文件夹。
5. 使用 “WinSCP” （即本地与远程计算机间的复制文件工具）登录 JBoss 服务器，将已获取到的 `cloud.tencent.com.jks` 密钥库文件从本地目录拷贝至 cert 文件夹。
6. 编辑在 `/usr/local/jboss-7.1.1/standalone/configuration` 目录下的 `standalone.xml` 文件。修改端口配置，如下所示：
 - 第一部分：
```
<interfaces>
        <interface name="management">
            <inet-address value="${jboss.bind.address.management:127.0.0.1}"/>
        </interface>
				<!--开启远程访问-->
        <interface name="public">
            <inet-address value="${jboss.bind.address:0.0.0.0}"/>
        </interface>
        <interface name="unsecure">
            <inet-address value="${jboss.bind.address.unsecure:127.0.0.1}"/>
        </interface>
    </interfaces>
    <socket-binding-group name="standard-sockets" default-interface="public" port-offset="${jboss.socket.binding.port-offset:0}">
        <socket-binding name="management-native" interface="management" port="${jboss.management.native.port:9999}"/>
        <socket-binding name="management-http" interface="management" port="${jboss.management.http.port:9990}"/>
        <socket-binding name="management-https" interface="management" port="${jboss.management.https.port:9443}"/>
        <socket-binding name="ajp" port="8009"/>
				<!--修改http端口-->
        <socket-binding name="http" port="80"/>
				<!--修改https端口-->
        <socket-binding name="https" port="443"/>
        <socket-binding name="osgi-http" interface="management" port="8090"/>
        <socket-binding name="remoting" port="4447"/>
        <socket-binding name="txn-recovery-environment" port="4712"/>
        <socket-binding name="txn-status-manager" port="4713"/>
        <outbound-socket-binding name="mail-smtp">
            <remote-destination host="localhost" port="25"/>
        </outbound-socket-binding>
    </socket-binding-group>
```
配置文件的主要调整说明如下：
    - **开启远程访问**：将 `${jboss.bind.address:127.0.0.1}` 调整为 `${jboss.bind.address:0.0.0.0}`。
    - **修改 http 端口**：将8080端口调整为80。
    - **修改 https 端口**：将8443端口调整为443。
 - 第二部分：添加证书相关配置。
```
<subsystem xmlns="urn:jboss:domain:web:1.1" default-virtual-server="default-host" native="false">
            <connector name="http" protocol="HTTP/1.1" scheme="http" socket-binding="http"/>
			<connector name="https" protocol="HTTP/1.1" scheme="https" socket-binding="https" secure="true">
                <ssl name="https" password="******" certificate-key-file="../standalone/configuration/cert/cloud.tencent.com.jks" cipher-suite="TLS_RSA_WITH_AES_256_CBC_SHA,TLS_DHE_RSA_WITH_AES_256_CBC_SHA,TLS_DHE_DSS_WITH_AES_128_CBC_SHA,SSL_RSA_WITH_3DES_EDE_CBC_SHA,SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA,SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA" protocol="TLSv1,TLSv1.1,TLSv1.2"/>
            </connector>
            <virtual-server name="default-host" enable-welcome-root="true">
                <alias name="localhost"/>
                <alias name="example.com"/>
            </virtual-server>
        </subsystem>
```
7. 进入 `/usr/local/jboss-7.1.1/bin` 目录下，执行启动命令 `./standalone.sh`，确保正常启动。如下图所示：
![](https://main.qcloudimg.com/raw/0dc9c0ee84b92f7978a7a133d35bcf27.png)
8. 证书已部署完成，即可使用 `https://cloud.tencent.com` 访问。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。


