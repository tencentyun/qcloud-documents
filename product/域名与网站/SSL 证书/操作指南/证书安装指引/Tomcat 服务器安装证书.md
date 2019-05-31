
## 操作场景
本文档指导您如何在 Tomcat 服务器中安装 SSL 证书。

## 前提条件
由于操作系统的版本不同，Tomcat 服务器中的 Tomcat 使用的版本以及安装在服务器上的路径不同，详细操作步骤略有区别。以下条件仅作为例子说明：
-  操作系统： CentOS 7 
- Tomcat 安装在服务器中路径：/usr 目录下存放
- JDK 安装在服务器中路径：/usr/java 目录下存放
- 默认端口：80

## 操作步骤

### 证书安装
1. 使用 “WinSCP” 工具，登录 Tomcat 服务器。
2. 将已获取到的 `www.domain.com.jks` 密钥库文件从本地目录拷贝至 `/usr/*/conf` 目录下。
 >!上述描述目录中的 * 为您在服务器上安装的 Tomcat 文件夹名称。例如`apache-tomcat-9.0.20`。
3. 关闭 “WinSCP” 界面。
4. 使用远程登录工具，登录 Tomcat 服务器。例如 “PuTTY” 工具。
5. 编辑在 `/usr/*/conf` 目录下的 `server.xml` 文件。添加如下内容：
```
<Connector port="443" protocol="HTTP/1.1" SSLEnabled="true"
  maxThreads="150" scheme="https" secure="true"
  keystoreFile="/*/*/www.domain.com.jks" #证书保存的路径
  keystorePass="******"
  clientAuth="false" sslProtocol="TLS" />
```
配置文件的主要参数说明如下：
 - keystoreFile：密钥库文件的存放位置，可以指定绝对路径，也可以指定相对于 &lt;CATALINA_HOME&gt; （Tomcat安装目录）环境变量的相对路径。如果此项没有设定，默认情况下，Tomcat 将从当前操作系统用户的用户目录下读取名为 “.keystore” 的文件。
 - keystorePass：密钥库密码，指定 keystore 的密码。申请证书时若设置了私钥密码，请填写私钥密码；若申请证书时未设置私钥密码，请填写 Tomcat 文件夹中 keystorePass.txt 文件的密码。
 - clientAuth：如果设为 true，表示 Tomcat 要求所有的 SSL 客户出示安全证书，对 SSL 客户进行身份验证。
 - sslProtocol：指定套接字（Socket）使用的加密/解密协议，默认值为 TLS。
4. 若 Tomcat 服务器没有启动，在 `/usr/*/bin` 目录下执行启动命令 `./startup.sh` 启动 Tomcat 服务器。
5. 若启动成功，即可使用 `https://www.domain.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置

1. 编辑  `/usr/*/conf` 目录下的 `web.xml` 文件，找到 `</welcome-file-list>` 标签。
2. 在 `</welcome-file-list>` 下面换行，并添加以下内容：
```
<login-config>
    <!-- Authorization setting for SSL -->
    <auth-method>CLIENT-CERT</auth-method>
    <realm-name>Client Cert Users-only Area</realm-name>
    </login-config>
    <security-constraint>
    <!-- Authorization setting for SSL -->
    <web-resource-collection>
    <web-resource-name>SSL</web-resource-name>
    <url-pattern>/*</url-pattern>
    </web-resource-collection>
    <user-data-constraint>
    <transport-guarantee>CONFIDENTIAL</transport-guarantee>
    </user-data-constraint>
    </security-constraint>
```
3. 编辑 `/usr/*/conf` 目录下的 `server.xml` 文件，将 redirectPort 参数修改为 SSL 的 connector 的端口，即443端口。如下所示：
```
<Connector port="8080" protocol="HTTP/1.1"
  connectionTimeout="20000"
  redirectPort="443" />
```
>? 此修改操作可将非 SSL 的 connector 可以跳转到 SSL 的 connector 中。
>
4. 在` /usr/*/bin` 目录下执行关闭命令`./shutdown.sh`之后，执行下列命令，确认配置是否有误。
```
./configtest.sh（需要在关闭tomcat下检验）
```
 - 是，请修改配置。
 - 否，启动 tomcat 即可正常访问。
5. 执行启动命令`./startup.sh`启动 Tomcat 服务器，即可使用`http://www.domain.com`进行访问。
