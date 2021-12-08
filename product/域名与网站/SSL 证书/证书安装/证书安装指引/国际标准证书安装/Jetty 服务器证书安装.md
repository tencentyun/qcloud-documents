## 操作场景
本文档指导您如何在 Jetty 服务器中安装 SSL 证书。
>?
>- 本文档以证书名称 `cloud.tencent.com` 为例。
>- Jetty 版本以 `jetty-distribution-9.4.28.v20200408` 为例。
>- 当前服务器的操作系统为 CentOS 7，由于操作系统的版本不同，详细操作步骤略有区别。
>- 安装 SSL 证书前，请您在 Jetty 服务器上开启 “443” 端口，避免证书安装后无法启用 HTTPS。具体可参考 [服务器如何开启443端口？](https://cloud.tencent.com/document/product/400/45144)
>- SSL 证书文件上传至服务器方法可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

## 前提条件
- 已准备文件远程拷贝软件，例如 WinSCP（建议从官方网站获取最新版本）。
- 已准备远程登录工具，例如 PuTTY 或者 Xshell（建议从官方网站获取最新版本）。
- 已在当前服务器中安装配置 Jetty 服务。
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
- 当您申请 SSL 证书时选择 “粘贴 CSR” 方式，或购买的品牌证书为 Wotrus，则不提供 JKS 证书文件的下载，需要您通过手动转换格式的方式生成密钥库。其操作方法如下： 
 - 访问 [转换工具](https://myssl.com/cert_convert.html)。
 - 将 Nginx 文件夹中的证书文件和私钥文件上传至转换工具中，并填写密钥库密码，单击**提交**，转换为 jks 格式证书。
- 当前 Jetty 服务器安装在 `/usr/local/jetty` 目录下。


## 操作步骤
1. 请在 [SSL 证书管理控制台](https://console.cloud.tencent.com/ssl) 中选择您需要安装的证书并单击**下载**。
2. 在弹出的 “证书下载” 窗口中，服务器类型选择 **JKS**，单击**下载**并解压缩 `cloud.tencent.com` 证书文件包到本地目录。
解压缩后，可获得相关类型的证书文件。其中包含 `cloud.tencent.com_jks` 文件夹：
 - **文件夹名称**：`cloud.tencent.com_jks`
 - **文件夹内容**：
    - `cloud.tencent.com.jks` 密钥库
    - `cloud.tencent.com.key` 私钥文件
    - `keystorePass.txt` 密码文件（若已设置私钥密码，则无 `keystorePass.txt` 密码文件）
3. 远程登录 Jetty 服务器。例如，使用 [“PuTTY” 工具](https://cloud.tencent.com/document/product/213/35699#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4) 登录。
4. 进入部署证书步骤，在 `/usr/local/jetty/jetty-distribution-9.4.28.v20200408/etc` 目录下执行命令 `mkdir cert` 创建 cert 文件夹。
5. 使用 “WinSCP” （即本地与远程计算机间的复制文件工具）登录 Jetty 服务器，将已获取到的 `cloud.tencent.com.jks` 密钥库文件从本地目录拷贝至 cert 文件夹。
6. 编辑 `/usr/local/jetty/jetty-distribution-9.4.28.v20200408/etc` 目录下的 `jetty-ssl-context.xml` 文件，如下所示：
>?
>- **KeyStorePath**：默认值 default 请填写证书存放的路径。
>- **KeyStorePassword**：默认值 default 请填写密钥库密码，指定 keystore 的密码。申请证书时若设置了私钥密码，请填写私钥密码；若申请证书时未设置私钥密码，请填写 `cloud.tencent.com_jks` 文件夹中 keystorePass.txt 文件的密码。
>- **KeyManagerPassword**：请填写 `cloud.tencent.com_jks` 文件夹中 keystorePass.txt 文件的密码。
>- **TrustStorePath**：默认值 default 请填写证书存放的路径。
>
```
<?xml version="1.0"?><!DOCTYPE Configure PUBLIC "-//Jetty//Configure//EN" "http://www.eclipse.org/jetty/configure_9_3.dtd">
<!-- ============================================================= --><!-- SSL ContextFactory configuration                              --><!-- ============================================================= -->
<!-- 
  To configure Includes / Excludes for Cipher Suites or Protocols see tweak-ssl.xml example at 
     https://www.eclipse.org/jetty/documentation/current/configuring-ssl.html#configuring-sslcontextfactory-cipherSuites
-->
<Configure id="sslContextFactory" class="org.eclipse.jetty.util.ssl.SslContextFactory$Server">
  <Set name="Provider"><Property name="jetty.sslContext.provider"/></Set>
  <Set name="KeyStorePath"><Property name="jetty.base" default="." />/<Property name="jetty.sslContext.keyStorePath" deprecated="jetty.keystore" default="etc/cert/cloud.tencent.com.jks"/></Set>
  <Set name="KeyStorePassword"><Property name="jetty.sslContext.keyStorePassword" deprecated="jetty.keystore.password" default="4d5jtdq238j1l"/></Set>
  <Set name="KeyStoreType"><Property name="jetty.sslContext.keyStoreType" default="JKS"/></Set>
  <Set name="KeyStoreProvider"><Property name="jetty.sslContext.keyStoreProvider"/></Set>
  <Set name="KeyManagerPassword"><Property name="jetty.sslContext.keyManagerPassword" deprecated="jetty.keymanager.password" default="4d5jtdq238j1l"/></Set>
  <Set name="TrustStorePath"><Property name="jetty.base" default="." />/<Property name="jetty.sslContext.trustStorePath" deprecated="jetty.truststore" default="etc/cert/cloud.tencent.com.jks"/></Set>
  <Set name="TrustStorePassword"><Property name="jetty.sslContext.trustStorePassword" deprecated="jetty.truststore.password"/></Set>
  <Set name="TrustStoreType"><Property name="jetty.sslContext.trustStoreType"/></Set>
  <Set name="TrustStoreProvider"><Property name="jetty.sslContext.trustStoreProvider"/></Set>
  <Set name="EndpointIdentificationAlgorithm"><Property name="jetty.sslContext.endpointIdentificationAlgorithm"/></Set>
  <Set name="NeedClientAuth"><Property name="jetty.sslContext.needClientAuth" deprecated="jetty.ssl.needClientAuth" default="false"/></Set>
  <Set name="WantClientAuth"><Property name="jetty.sslContext.wantClientAuth" deprecated="jetty.ssl.wantClientAuth" default="false"/></Set>
  <Set name="useCipherSuitesOrder"><Property name="jetty.sslContext.useCipherSuitesOrder" default="true"/></Set>
  <Set name="sslSessionCacheSize"><Property name="jetty.sslContext.sslSessionCacheSize" default="-1"/></Set>
  <Set name="sslSessionTimeout"><Property name="jetty.sslContext.sslSessionTimeout" default="-1"/></Set>
  <Set name="RenegotiationAllowed"><Property name="jetty.sslContext.renegotiationAllowed" default="true"/></Set>
  <Set name="RenegotiationLimit"><Property name="jetty.sslContext.renegotiationLimit" default="5"/></Set>
  <Set name="SniRequired"><Property name="jetty.sslContext.sniRequired" default="false"/></Set>
  <!-- Example of how to configure a PKIX Certificate Path revocation Checker
  <Call id="pkixPreferCrls" class="java.security.cert.PKIXRevocationChecker$Option" name="valueOf"><Arg>PREFER_CRLS</Arg></Call>
  <Call id="pkixSoftFail" class="java.security.cert.PKIXRevocationChecker$Option" name="valueOf"><Arg>SOFT_FAIL</Arg></Call>
  <Call id="pkixNoFallback" class="java.security.cert.PKIXRevocationChecker$Option" name="valueOf"><Arg>NO_FALLBACK</Arg></Call>
  <Call class="java.security.cert.CertPathBuilder" name="getInstance">
    <Arg>PKIX</Arg>
    <Call id="pkixRevocationChecker" name="getRevocationChecker">
      <Call name="setOptions">
        <Arg>
          <Call class="java.util.EnumSet" name="of">
            <Arg><Ref refid="pkixPreferCrls"/></Arg>
            <Arg><Ref refid="pkixSoftFail"/></Arg>
            <Arg><Ref refid="pkixNoFallback"/></Arg>
          </Call>
        </Arg>
      </Call>
    </Call>
  </Call>
  <Set name="PkixCertPathChecker"><Ref refid="pkixRevocationChecker"/></Set>
  -->
</Configure>
```
7. 编辑 `/usr/local/jetty/jetty-distribution-9.4.28.v20200408/etc` 目录下的 `jetty-ssl.xml` 文件，修改端口为443。如下所示：
```
 <Call  name="addConnector">
    <Arg>
      <New id="sslConnector" class="org.eclipse.jetty.server.ServerConnector">
        <Arg name="server"><Ref refid="Server" /></Arg>
        <Arg name="acceptors" type="int"><Property name="jetty.ssl.acceptors" deprecated="ssl.acceptors" default="-1"/></Arg>
        <Arg name="selectors" type="int"><Property name="jetty.ssl.selectors" deprecated="ssl.selectors" default="-1"/></Arg>
        <Arg name="factories">
          <Array type="org.eclipse.jetty.server.ConnectionFactory">
            <!-- uncomment to support proxy protocol
            <Item>
              <New class="org.eclipse.jetty.server.ProxyConnectionFactory"/>
            </Item>-->
          </Array>
        </Arg>
        <Set name="host"><Property name="jetty.ssl.host" deprecated="jetty.host" /></Set>
        <Set name="port"><Property name="jetty.ssl.port" deprecated="ssl.port" default="443" /></Set>
        <Set name="idleTimeout"><Property name="jetty.ssl.idleTimeout" deprecated="ssl.timeout" default="30000"/></Set>
        <Set name="acceptorPriorityDelta"><Property name="jetty.ssl.acceptorPriorityDelta" deprecated="ssl.acceptorPriorityDelta" default="0"/></Set>
        <Set name="acceptQueueSize"><Property name="jetty.ssl.acceptQueueSize" deprecated="ssl.acceptQueueSize" default="0"/></Set>
        <Get name="SelectorManager">
          <Set name="connectTimeout"><Property name="jetty.ssl.connectTimeout" default="15000"/></Set>
        </Get>
      </New>
    </Arg>
  </Call>
```
8. 编辑 `/usr/local/jetty/jetty-distribution-9.4.28.v20200408` 目录下的 `start.ini` 文件，添加如下内容：
```
etc/jetty-ssl.xml
etc/jetty-ssl-context.xml
etc/jetty-https.xml
```
9. 证书已部署完成，在 jetty 根目录下，执行启动命令 `java -jar start.jar`，即可使用 `https://cloud.tencent.com` 访问。

## 注意事项
证书部署成功后，使用 `https://cloud.tencent.com` 访问若显示如下：
![](https://main.qcloudimg.com/raw/2ad181d6ed021958c214b04df9fa67a6.png)
解决方案：您可以将 `/usr/local/jetty/jetty-distribution-9.4.28.v20200408/demo-base/webapps` 目录下的 ROOT 文件复制到 `/usr/local/jetty/jetty-distribution-9.4.28.v20200408/webapps` 目录下，重启 jetty，即可访问成功。

>!操作过程如果出现问题，请您 [联系我们](https://cloud.tencent.com/document/product/400/35259)。


