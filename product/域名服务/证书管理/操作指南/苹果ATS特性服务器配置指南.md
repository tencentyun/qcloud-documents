配置指南：
1. 需要配置符合PFS规范的加密套餐，目前推荐配置：
`ECDHE-RSA-AES128-GCM-SHA256:ECDH:AES:HIGH:!aNULL:!MD5:!ADH:!DH`
2. 需要在服务端TLS协议中启用TLS1.2，目前推荐配置：
`TLSv1 TLSv1.1 TLSv1.2`

### 1.Nginx 证书配置

更新Nginx根目录下 conf/nginx.conf 文件如下：
```
server {
	ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDH:AES:HIGH:!aNULL:!MD5:!ADH:!DH;
	ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
}
```

### 2.Apache 证书配置

更新Apache根目录下 conf/httpd.conf 文件如下：
```
<IfModule mod_ssl.c>
        <VirtualHost *:443>
		SSLProtocol TLSv1 TLSv1.1 TLSv1.2
		SSLCipherSuite ECDHE-RSA-AES128-GCM-SHA256:ECDH:AES:HIGH:!aNULL:!MD5:!ADH:!DH
		</VirtualHost>
</IfModule>
```

### 3.Tomcat 证书配置
更新 %TOMCAT_HOME%\conf\server.xml 文件如下：
```
<Connector port="443" protocol="HTTP/1.1" SSLEnabled="true"
    scheme="https" secure="true"
    SSLProtocol="TLSv1+TLSv1.1+TLSv1.2"
    SSLCipherSuite="ECDHE-RSA-AES128-GCM-SHA256:ECDH:AES:HIGH:!aNULL:!MD5:!ADH:!DH" />
```
