下载得到的 www.domain.com.zip 文件，解压获得3个文件夹，分别是Apache、IIS、Nginx 服务器的证书文件，
下面提供了3类服务器证书安装方法的示例：

### 1. Apache 2.x 证书部署

#### 1.1 获取证书
Apache文件夹内获得证书文件 1_root_bundle.crt，2_www.domain.com_cert.crt 和私钥文件 3_www.domain.com.key,
1_root_bundle.crt 文件包括一段证书代码 “-----BEGIN CERTIFICATE-----”和“-----END CERTIFICATE-----”,
2_www.domain.com_cert.crt 文件包括一段证书代码 “-----BEGIN CERTIFICATE-----”和“-----END CERTIFICATE-----”,
3_www.domain.com.key 文件包括一段私钥代码“-----BEGIN RSA PRIVATE KEY-----”和“-----END RSA PRIVATE KEY-----”。

#### 1.2 证书安装
编辑Apache根目录下 conf/httpd.conf 文件，
找到 `#LoadModule ssl_module modules/mod_ssl.so` 和 `#Include conf/extra/httpd-ssl.conf`，去掉前面的`#`号注释；
编辑Apache根目录下 conf/extra/httpd-ssl.conf 文件，修改如下内容：
```
<VirtualHost www.domain.com:443>
    DocumentRoot "/var/www/html"
    ServerName www.domain.com
    SSLEngine on
    SSLCertificateFile /usr/local/apache/conf/2_www.domain.com_cert.crt
    SSLCertificateKeyFile /usr/local/apache/conf/3_www.domain.com.key
    SSLCertificateChainFile /usr/local/apache/conf/1_root_bundle.crt
</VirtualHost>
```
配置完成后，重新启动 Apache 就可以使用`https://www.domain.com`来访问了。

注：

| 配置文件参数 | 说明 |
|---------|---------|
| SSLEngine on | 启用SSL功能 |
| SSLCertificateFile | 证书文件 |
| SSLCertificateKeyFile | 私钥文件 |
| SSLCertificateChainFile | 证书链文件 |

### 2. Nginx 证书部署

#### 2.1 获取证书
Nginx文件夹内获得SSL证书文件 1_www.domain.com_bundle.crt 和私钥文件 2_www.domain.com.key,
1_www.domain.com_bundle.crt 文件包括两段证书代码 “-----BEGIN CERTIFICATE-----”和“-----END CERTIFICATE-----”,
2_www.domain.com.key 文件包括一段私钥代码“-----BEGIN RSA PRIVATE KEY-----”和“-----END RSA PRIVATE KEY-----”。

#### 2.2 证书安装
将域名 www.domain.com 的证书文件1_www.domain.com_bundle.crt 、私钥文件2_www.domain.com.key保存到同一个目录，例如/usr/local/nginx/conf目录下。
更新Nginx根目录下 conf/nginx.conf 文件如下：
```
server {
        listen 443;
        server_name www.domain.com; #填写绑定证书的域名
        ssl on;
        ssl_certificate 1_www.domain.com_bundle.crt;
        ssl_certificate_key 2_www.domain.com.key;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; #按照这个协议配置
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;#按照这个套件配置
        ssl_prefer_server_ciphers on;
        location / {
            root   html; #站点目录
            index  index.html index.htm;
        }
    }
```
配置完成后，先用`bin/nginx –t`来测试下配置是否有误，正确无误的话，重启nginx。就可以使 `https://www.domain.com` 来访问了。

注：

| 配置文件参数 | 说明 |
|---------|---------|
| listen 443 | SSL访问端口号为443 |
| ssl on | 启用SSL功能 |
| ssl_certificate | 证书文件 |
| ssl_certificate_key | 私钥文件 |
| ssl_protocols | 使用的协议 |
| ssl_ciphers | 配置加密套件，写法遵循openssl标准 |

#### 2.3 使用全站加密，http自动跳转https（可选）
对于用户不知道网站可以进行https访问的情况下，让服务器自动把http的请求重定向到https。
在服务器这边的话配置的话，可以在页面里加js脚本，也可以在后端程序里写重定向，当然也可以在web服务器来实现跳转。Nginx是支持rewrite的（只要在编译的时候没有去掉pcre）
在http的server里增加`rewrite   ^(.*) https://$host$1 permanent;`
这样就可以实现80进来的请求，重定向为https了。

### 3. IIS 证书部署

#### 3.1 获取证书

IIS文件夹内获得SSL证书文件 www.domain.com.pfx。

#### 3.2 证书安装
1、打开IIS服务管理器，点击计算机名称，双击‘服务器证书’
![3.2.1](//mccdn.qcloud.com/static/img/6d7b25b42c493bfd9d9d871b00c67398/image.png)

2、双击打开服务器证书后，点击右则的导入
![3.2.2](//mccdn.qcloud.com/static/img/9fbedac0a2c160c72f0ef95bfaca9e18/image.png)

3、选择证书文件，如果输入申请证书时有填写私钥密码需要输入密码，点击确定。[参考私钥密码指引](https://cloud.tencent.com/doc/product/400/4461)
![3.2.3](//mccdn.qcloud.com/static/img/77fdc7cd57281b03d41a19c81af1158d/image.png)

4、点击网站下的站点名称，点击右则的绑定
![3.2.4](//mccdn.qcloud.com/static/img/6c7eee199d1da5d141942af170022a09/image.png)

5、打开网站绑定界面后，点击添加
![3.2.5](//mccdn.qcloud.com/static/img/58e4ee6bb90307fbe1a238ebf818ff9b/image.png)

6、添加网站绑定内容：选择类型为https，端口443和指定对应的SSL证书，点击确定
![3.2.6](//mccdn.qcloud.com/static/img/813256e938d26fb71d3223cf1eb6082b/image.png)

7、添加完成后，网站绑定界面将会看到刚刚添加的内容
![3.2.7](//mccdn.qcloud.com/static/img/0748888723acf5671ba9a1ed7ef9ebd2/image.png)

### 4. Tomcat 证书部署

#### 4.1 获取证书

如果申请证书时有填写私钥密码，下载可获得Tomcat文件夹，其中有密钥库 www.domain.com.jks；
如果没有填写私钥密码，不提供Tomcat证书文件的下载，需要用户手动转换格式生成。

> 可以通过 Nginx 文件夹内证书文件和私钥文件生成jks格式证书
> 转换工具：https://www.trustasia.com/tools/cert-converter.htm
> 使用工具时注意填写 **密钥库密码** ，安装证书时配置文件中需要填写。

#### 4.2 证书安装

配置SSL连接器，将`www.domain.com.jks`文件存放到conf目录下，然后配置同目录下的`server.xml`文件：

```
<Connector port="443" protocol="HTTP/1.1" SSLEnabled="true"
	maxThreads="150" scheme="https" secure="true"
	keystoreFile="conf\www.domain.com.jks"
	keystorePass="changeit"
	clientAuth="false" sslProtocol="TLS" />
```

注：

| 配置文件参数 | 说明 |
|---------|---------|
| clientAuth | 如果设为true，表示Tomcat要求所有的SSL客户出示安全证书，对SSL客户进行身份验证 |
| keystoreFile | 指定keystore文件的存放位置，可以指定绝对路径，也可以指定相对于<CATALINA_HOME> （Tomcat安装目录）环境变量的相对路径。如果此项没有设定，默认情况下，Tomcat将从当前操作系统用户的用户目录下读取名为 “.keystore”的文件。 |
| keystorePass | 密钥库密码，指定keystore的密码。（如果申请证书时有填写私钥密码，密钥库密码即私钥密码）|
| sslProtocol | 指定套接字（Socket）使用的加密/解密协议，默认值为TLS|

#### 4.3 http自动跳转https的安全配置
到conf目录下的web.xml。在`</welcome-file-list>`后面，`</web-app>`，也就是倒数第二段里，加上这样一段
```
<web-resource-collection >
	<web-resource-name >SSL</web-resource-name>
	<url-pattern>/*</url-pattern>
</web-resource-collection>
<user-data-constraint>
	<transport-guarantee>CONFIDENTIAL</transport-guarantee>
</user-data-constraint>
```

这步目的是让非ssl的connector跳转到ssl的connector去。所以还需要前往server.xml进行配置：
```
<Connector port="8080" protocol="HTTP/1.1"
	connectionTimeout="20000"
	redirectPort="443" />
```
redirectPort改成ssl的connector的端口443，重启后便会生效。
