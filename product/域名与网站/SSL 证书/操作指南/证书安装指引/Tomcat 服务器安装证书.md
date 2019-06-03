## 操作场景
本文档指导您如何在 Tomcat 服务器中安装 SSL 证书。

## 前提条件
由于操作系统的版本不同，详细操作步骤略有区别。以下条件仅作为例子说明：
- 当前服务器的操作系统为 CentOS 7。
- 已在当前服务器中安装配置 Tomcat 服务器。
 >!当前 Tomcat 服务器安装在`/usr`目录下，例如`apache-tomcat-9.0.20`。则`/usr/*/conf`实际为`/usr/apache-tomcat-9.0.20/conf`。
 
## 操作步骤

### 证书安装
1. 使用 “WinSCP” 工具，登录 Tomcat 服务器。
2. 将已获取到的 `www.domain.com.jks` 密钥库文件从本地目录拷贝至 `/usr/*/conf` 目录下。
3. 关闭 “WinSCP” 界面。
4. 使用远程登录工具，登录 Tomcat 服务器。例如 “PuTTY” 工具。
5. 编辑在 `/usr/*/conf` 目录下的 `server.xml` 文件。添加如下内容：
```
<Connector port="443" protocol="HTTP/1.1" SSLEnabled="true"
  maxThreads="150" scheme="https" secure="true"
  keystoreFile="/usr/*/conf/www.domain.com.jks" #证书保存的路径
  keystorePass="******"#密钥库密码
  clientAuth="false" sslProtocol="TLS" />
```
详细 server.xml 请参考如下内容：
```
 <?xml version="1.0" encoding="UTF-8"?>
  <Server port="8005" shutdown="SHUTDOWN">
    <Listener className="org.apache.catalina.startup.VersionLoggerListener" />
    <Listener className="org.apache.catalina.core.AprLifecycleListener" SSLEngine="on" />
    <Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener" />
    <Listener className="org.apache.catalina.mbeans.GlobalResourcesLifecycleListener" />
    <Listener className="org.apache.catalina.core.ThreadLocalLeakPreventionListener" />
 <GlobalNamingResources>
    <Resource name="UserDatabase" auth="Container"
              type="org.apache.catalina.UserDatabase"
              description="User database that can be updated and saved"
              factory="org.apache.catalina.users.MemoryUserDatabaseFactory"
              pathname="conf/tomcat-users.xml" />
  </GlobalNamingResources>
  <Service name="Catalina">
        <Connector port="80" protocol="HTTP/1.1" connectionTimeout="20000"  redirectPort="8443" />
        <Connector port="443" protocol="org.apache.coyote.http11.Http11Protocol"
               maxThreads="150" SSLEnabled="true" scheme="https" secure="true"
               clientAuth="false" sslProtocol="TLS"
                keystoreFile="/usr/*/conf/www.domain.com.jks"
                keystorePass="******" />
    <Connector port="8009" protocol="AJP/1.3" redirectPort="8443" />
   <Engine name="Catalina" defaultHost=“www.domain.com">
      <Realm className="org.apache.catalina.realm.LockOutRealm">
        <Realm className="org.apache.catalina.realm.UserDatabaseRealm"
               resourceName="UserDatabase"/>
      </Realm>
    <Host name=“www.domain.com"  appBase="webapps" 
        unpackWARs="true" autoDeploy="true" >
        <Context path="" docBase ="Knews" />
    <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
           prefix="localhost_access_log" suffix=".txt"  
           pattern="%h %l %u %t "%r" %s %b" />
      </Host>
    </Engine>
  </Service>
</Server>
```
配置文件的主要参数说明如下：
 - keystoreFile：密钥库文件的存放位置，可以指定绝对路径，也可以指定相对于 &lt;CATALINA_HOME&gt; （Tomcat安装目录）环境变量的相对路径。如果此项没有设定，默认情况下，Tomcat 将从当前操作系统用户的用户目录下读取名为 “.keystore” 的文件。
 - keystorePass：密钥库密码，指定 keystore 的密码。申请证书时若设置了私钥密码，请填写私钥密码；若申请证书时未设置私钥密码，请填写 Tomcat 文件夹中 keystorePass.txt 文件的密码。
 - clientAuth：如果设为 true，表示 Tomcat 要求所有的 SSL 客户出示安全证书，对 SSL 客户进行身份验证。
 - sslProtocol：指定套接字（Socket）使用的加密/解密协议，默认值为 TLS。
6. 若 Tomcat 服务器没有启动，在 `/usr/*/bin` 目录下执行启动命令 `./startup.sh` 启动 Tomcat 服务器。
7. 若启动成功，即可使用 `https://www.domain.com` 进行访问。

### HTTP 自动跳转 HTTPS 的安全配置（可选）

如果您不知道网站可以通过 HTTPS 方式访问的情况，我们可以通过配置服务器，让其自动将 HTTP 的请求重定向到 HTTPS。您可以通过以下操作设置：
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
3. 编辑 `/usr/*/conf` 目录下的 `server.xml` 文件，将 redirectPort 参数修改为 SSL 的 connector 的端口，即8443端口修改为443端口。如下所示：
```
<Connector port="80" protocol="HTTP/1.1"
  connectionTimeout="20000"
  redirectPort="443" />
```
>? 此修改操作可将非 SSL 的 connector 可以跳转到 SSL 的 connector 中。
>
4. 在` /usr/*/bin` 目录下执行关闭命令`./shutdown.sh`之后，执行下列命令，确认配置是否存在问题。
```
./configtest.sh（需要在关闭tomcat下检验）
```
 - 若存在，请修改配置。
 - 若不存在，启动 tomcat 即可正常访问。
5. 执行启动命令`./startup.sh`启动 Tomcat 服务器，即可使用`http://www.domain.com`进行访问。
