本文档将为您介绍通过 DDoS 高防直接获取真实 IP 的方法，以及针对 Tomcat、Apache、Nginx 和 IIS 服务器，介绍相应的 X-Forwarded-For 配置方案及获取真实 IP 的方法。
## 背景信息
通常情况下，当用户进行网站访问时，浏览器可能不是直达服务器，中间会部署 CDN 及 DDoS 高防等防护服务。例如，采用这样的架构：“用户 > CDN/DDoS 高防 > 源站服务器” 。

如果您已经使用 DDoS 高防服务，可直接通过高防服务获取访问者的真实 IP，您也可以通过配置网站服务器来获取访问者的真实 IP。DDoS 高防 IP 使用网站业务转发规则时，可利用 HTTP 头部的 X-Forwareded-For 字段获取客户端真实 IP。

X-Forwareded-For：是一个 HTTP 头部扩展字段，目的是使服务器可以识别通过代理等方式链接的客户端真正的 IP。
格式为：X-Forwareded-For：Client，proxy1，proxy2，proxy3……

当高防 IP 将用户的访问请求转到后端服务器时，会把请求用户的真实 IP 记录在 X-Forwareded-For 字段的首位。因此，源站应用只需要获取 HTTP 头部的 X-Forwarded-For 字段的内容即可。


## 通过 HTTP Header 获取真实 IP
DDoS 高防服务默认提供获取客户端真实 IP 的功能，下面推荐两种方式获取客户的来源 IP，您可以根据需要，选择任意一种方式进行使用：
- **方式1**：DDoS 高防服务使用 X-Forwarded-For 的方式获取客户端的真实 IP 地址。
	- 真实的客户端 IP 会被 DDoS 高防服务放在 HTTP 头部的 X-Forwarded-For 字段，格式如下：
```plaintext
X-Forwarded-For: 用户真实IP, 代理服务器1-IP， 代理服务器2-IP，...
```
>?当使用此方式获取客户端真实 IP 时，获取的第一个地址即为客户端真实 IP。
	- 各语言通过调用 SDK 接口获取 X-Forwarded-For 字段的方式如下：
		- ASP：
```plaintext
Request.ServerVariables("HTTP_X_FORWARDED_FOR")
```
		- ASP.NET(C#)：
```plaintext
Request.ServerVariables["HTTP_X_FORWARDED_FOR"]
```
		- PHP：
```plaintext
$_SERVER["HTTP_X_FORWARDED_FOR"]
```
		- JSP:
```plaintext
request.getHeader("HTTP_X_FORWARDED_FOR")
```
- **方式2**：DDoS 高防服务支持使用 X-Real-IP 变量，获取客户的来源 IP（使用过程中考虑了后面所经过的多层反向代理对该变量的修改）。
各种语言通过调用 SDK 接口获取 X-Real-IP 字段的方式如下：
	- ASP：
```plaintext
Request.ServerVariables("HTTP_X_REAL_IP")
```
	- ASP.NET(C#)：
 ```plaintext
Request.ServerVariables["HTTP_X_REAL_IP"]
```
	- PHP：
```plaintext
$_SERVER["HTTP_X_REAL_IP"]
```
	- JSP：
```plaintext
request.getHeader("HTTP_X_REAL_IP")
```

## 访问日志打印真实 IP
### Tomcat 如何在访问日志中获取真实客户端的 IP 地址
如果您的源站部署了 Tomcat 服务器，可通过启用 Tomcat 的 X-Forwarded-For 功能，获取访问者的真实 IP 地址。
1. 打开 server.xml 文件（“tomcat/conf/server.xml”），AccessLogValve 日志记录功能部分内容如下：
```plaintext
<Host name="localhost"  appBase="webapps" unpackWARs="true" autoDeploy="true">
       <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
              prefix="localhost_access_log." suffix=".txt"
               pattern="%h %l %u %t "%r" %s %b" />
```
2. 在 pattern 中增加“%{X-Forwarded-IP}i”，修改后的 server.xml 为：
```plaintext
<Host name="localhost"  appBase="webapps" unpackWARs="true" autoDeploy="true">
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
               prefix="localhost_access_log." suffix=".txt"
               pattern="%{X-Forwarded-For}i %h %l %u %t "%r" %s %b" />
</Host>
```
3. 查看 localhost_access_log 日志文件，可获取 X-Forwarded-For 对应的访问者真实 IP。

### Apache 如何在访问日志中获取真实客户端的 IP 地址
如果您的源站部署了 Apache 服务器，可通过运行命令安装 Apache 的第三方模块 mod_remoteip，并修改 http.conf 文件获取客户 IP 地址。
1. 打开 httpd.conf 配置文件，并将文件内容修改为如下内容：
Apache 映射 xff 到 remote_addr，详情请参见 [安装 mod_remoteip](https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html)。

2. 定义日志格式。
```plaintext
LogFormat "%{X-Forwarded-For}i %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" common
```
3. 重启 Apache，使配置生效。
```
/[apached目录]/httpd/bin/apachectl restart
```
4. 查看 access.log 日志文件，可获取 X-Forwarded-For 对应的访问者真实 IP。

### Nginx 如何在访问日志中获取真实客户端的 IP 地址
如果您的源站部署了 Nginx 反向代理，可通过在 Nginx 反向代理配置 Location 信息，后端 Web 服务器即可通过类似函数获取客户的真实 IP 地址。
1. 根据源站 Nginx 反向代理的配置，在 Nginx 反向代理的相应 location 位置配置如下内容，获取客户 IP 的信息。
```plaintext
log_format main '$remote_addr [$http_x_forwarded_for]- $remote_user [$time_local] '
                    '"$request" $status $body_bytes_sent '
                    '"$http_referer" "$http_user_agent"'; 
```
2. 重启 nginx。

## 通过插件映射客户端真实 IP
### Tomcat 配置方案
Tomcat 配置 xff 映射到 remote_addr，详情请参见 [tomcat 配置文档]( https://tomcat.apache.org/tomcat-8.5-doc/api/org/apache/catalina/valves/RemoteIpValve.html)。
配置示例如下：
```plaintext
<Valve className="org.apache.catalina.valves.RemoteIpValve" 
 remoteIpHeader="x-forwarded-for" 
 proxiesHeader="x-forwarded-by" 
 internalProxies="192\.168\.0\.10|192\.168\.0\.11"
 trustedProxies="62\.234\.227\.\d{1,3}|212\.64\.62\.\d{1,3}"
 />
```

### Apache 配置方案
Apache 映射 xff 到 remote_addr，需 [安装 mod_remoteip](https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html) 进行操作。
配置示例如下：
```plaintext
RemoteIPHeader X-Forwarded-For
RemoteIPTrustedProxyList x.x.x.x/24
```

### IIS 6 配置方案
如果您的源站部署了 IIS 6 服务器，您可以通过安装 F5XForwardedFor.dll 插件，从 IIS 6 服务器记录的访问日志中获取访问者真实的 IP 地址。
1. 下载并安装 [F5XForwardedFor](https://devcentral.f5.com/s/articles/x-forwarded-for-log-filter-for-windows-servers) 模块。
2. 根据您服务器的操作系统版本将 x86\Release 或者 x64\Release 目录中的 F5XForwardedFor.dll 文件拷贝至指定目录（如 C:\ISAPIFilters），同时确保 IIS 进程对该目录有读取权限。
3. 打开 IIS 管理器，找到当前开启的网站，在该网站上右键单击**属性**，打开“属性”页面。
4. 在“属性”页面，切换至 ISAPI筛选器，单击**添加**，在弹出的窗口中，配置如下信息：
	- **筛选器名称**：F5XForwardedFor。
	- **可执行文件**：F5XForwardedFor.dll 的完整路径，例如：C:\ISAPIFilters\F5XForwardedFor.dll。 
5. 单击**确定**，重启 IIS 6 服务器。
6. 查看 IIS 6 服务器记录的访问日志（默认的日志路径为：C:\WINDOWS\system32\LogFiles\ ，IIS 日志的文件名称以 .log 为后缀），可获取 X-Forwarded-For 对应的访问者真实 IP。

### IIS 7 配置方案
如果您的源站部署了 IIS 7 服务器，您可以通过安装 F5XForwardedFor 模块，从 IIS 7 服务器记录的访问日志中，获取访问者真实的 IP 地址。
1. 下载并安装 [F5XForwardedFor](https://devcentral.f5.com/s/articles/x-forwarded-for-log-filter-for-windows-servers) 模块。
2. 根据服务器的操作系统版本将 x86\Release （或 x64\Release）目录中的 F5XFFHttpModule.dll 和 F5XFFHttpModule.ini 文件拷贝到指定目录（如 C:\x_forwarded_for\x86 或 C:\x_forwarded_for\x64 ），并确保 IIS 进程对该目录有读取权限。
3. 在 IIS 服务器的选择项中，双击**模块**，进入“模块”界面。
4. 单击**配置本机模块**，在弹出的对话框中，单击**注册**，按操作系统选择注册模块注册已下载的 DLL 文件。
	- x86 操作系统：注册模块 x_forwarded_for_x86
		- 名称：x_forwarded_for_x86
		- 路径：C:\x_forwarded_for\x86\F5XFFHttpModule.dll
	- x64 操作系统：注册模块 x_forwarded_for_x64 
		- 名称：x_forwarded_for_x64
		- 路径：C:\x_forwarded_for\x64\F5XFFHttpModule.dll
5. 注册完成后，勾选新注册的模块（x_forwarded_for_x86 或 x_forwarded_for_x64）并单击**确定**。
6. 在 ISAPI 和 CGI 限制中，按操作系统添加已注册的 DLL 文件，并将其“限制”改为“允许”。
	- x86 操作系统：
		- ISAPI 或 CGI 路径：C:\x_forwarded_for\x86\F5XFFHttpModule.dll
		- 描述：x86
	- x64 操作系统：
		- ISAPI 或 CGI 路径：“C:\x_forwarded_for\x64\F5XFFHttpModule.dll”
		- 描述：x64
7. 重启 IIS 7 服务器，等待配置生效。
8. 查看 IIS 7 服务器记录的访问日志（默认的日志路径为：C:\WINDOWS\system32\LogFiles\ ，IIS 日志的文件名称以 .log 为后缀），可获取 X-Forwarded-For 对应的访问者真实 IP。


