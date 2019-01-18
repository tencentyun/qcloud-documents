
After decompressing the downloaded `www.domain.com.zip` file, you get three folders containing certificate files for Apache, IIS, Nginx servers.

Here are examples of certificate installation on four types of servers:

### 1. Apache 2.x Certificate Deployment

#### 1.1 Obtain certificate

Obtain the certificate files `1_root_bundle.crt`, `2_www.domain.com_cert.crt` and private key file `3_www.domain.com.key` in the Apache folder
`1_root_bundle.crt` file contains certificate codes "-----BEGIN CERTIFICATE-----" and "-----END CERTIFICATE-----";
`2_www.domain.com_cert.crt` file contains certificate codes "-----BEGIN CERTIFICATE-----" and "-----END CERTIFICATE-----";
`3_www.domain.com.key` file contains private key codes "-----BEGIN RSA PRIVATE KEY-----" and "-----END RSA PRIVATE KEY-----".


#### 1.2 Install certificate
Edit the conf/httpd.conf file in the Apache root directory;
Find `#LoadModule ssl_module modules/mod_ssl.so` and `#Include conf/extra/httpd-ssl.conf`, and remove the `#` symbol;
Modify the content of the conf/extra/httpd-ssl.conf file in the Apache root directory as follows:
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
After the configuration is completed, restart Apache and you can access with `https://www.domain.com`.

Note:

| Configuration File Parameter | Description |
|---------|---------|
| SSLEngine on | Enables SSL feature |
| SSLCertificateFile | Certificate file |
| SSLCertificateKeyFile | Private key file |
| SSLCertificateChainFile | Certificate chain file |

### 2. Nginx Certificate Deployment

#### 2.1 Obtain certificate

Obtain certificate file `1_www.domain.com_bundle.crt` and private key file `2_www.domain.com.key` in Nginx folder
`1_www.domain.com_bundle.crt` file contains certificate codes "-----BEGIN CERTIFICATE-----" and "-----END CERTIFICATE-----";
`2_www.domain.com.key` file contains private key codes "-----BEGIN RSA PRIVATE KEY-----" and "-----END RSA PRIVATE KEY-----".

#### 2.2 Install certificate
Save certificate file `1_www.domain.com_bundle.crt` and private key file `2_www.domain.com.key` of domain name www.domain.com in the same directory, such as /usr/local/nginx/conf.

Update the conf/nginx.conf file in the Nginx root directory as follows:
```
server {
        listen 443;
        server_name www.domain.com; #fill in domain name to be bound to the certificate
        ssl on;
        ssl_certificate 1_www.domain.com_bundle.crt;
        ssl_certificate_key 2_www.domain.com.key;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; #configure according to the protocol
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;#configure according to the suite
        ssl_prefer_server_ciphers on;
        location / {
            root   html; #site directory
            index  index.html index.htm;
        }
    }
```
After the configuration is completed, use `bin/nginx -t` to test whether the configuration is correct. If correct, restart Nginx, and you can access through `https: // www.domain.com`.

Note:

| Configuration File Parameter | Description |
|---------|---------|
| listen 443 | SSL access port number is 443 |
| ssl on | Enables SSL feature |
| ssl_certificate | Certificate file |
| ssl_certificate_key | Private key file |
| ssl_protocols | Protocol used |
| ssl_ciphers | Configures cipher suites, following the OpenSSL standard |

#### 2.3 Use full site encryption, with HTTP automatically redirected to HTTPS (optional)
For users who do not know that the website supports HTTPS access, the server automatically redirects HTTP requests to HTTPS.
If you want to configure redirection on the server side, you can add js script in the page or write redirection in the backend programs. Also, redirection can be achieved in the web server side. Nginx supports rewrite (as long as pcre is not removed during compiling)
Add `rewrite   ^(.*) https://$host$1 permanent;` in HTTP server
Then requests from port 80 can be redirected to https.

### 3. IIS Certificate Deployment

#### 3.1 Obtain certificate


Obtain SSL certificate file `www.domain.com.pfx` in IIS folder.


#### 3.2 Certificate installation
1. Open the IIS service manager, click the computer name, and double-click the server certificate
![3.2.1](//mccdn.qcloud.com/static/img/6d7b25b42c493bfd9d9d871b00c67398/image.png)

2. After the server certificate is opened, click **Import** on the right
![3.2.2](//mccdn.qcloud.com/static/img/9fbedac0a2c160c72f0ef95bfaca9e18/image.png)

3. Select the certificate file. If a private key password is set when applying for the certificate, you need to enter the password, otherwise you need to enter the password content of the password file keystorePass.txt in the folder, and then click **OK**. Please see [Private Key Password](https://cloud.tencent.com/doc/product/400/4461)
![3.2.3](//mccdn.qcloud.com/static/img/77fdc7cd57281b03d41a19c81af1158d/image.png).

4. Click the site name, and click **Bind** on the right
![3.2.4](//mccdn.qcloud.com/static/img/6c7eee199d1da5d141942af170022a09/image.png)

5. After the **Website Binding** interface is opened, click **Add**
![3.2.5](//mccdn.qcloud.com/static/img/58e4ee6bb90307fbe1a238ebf818ff9b/image.png)

6. Add site binding contents: Select https as the type, enter 443 as the port, select the corresponding SSL certificate, and click **OK**
![3.2.6](//mccdn.qcloud.com/static/img/813256e938d26fb71d3223cf1eb6082b/image.png)

7. Then, the **Website Binding** interface shows the contents you just added
![3.2.7](//mccdn.qcloud.com/static/img/0748888723acf5671ba9a1ed7ef9ebd2/image.png)

### 4. Tomcat Certificate Deployment

#### 4.1 Obtain certificate


If a private key password is set when applying for the certificate, you can download the Tomcat folder containing the key store `www.domain.com.jks`;

If you do not fill in a private key password when applying for the certificate, the Tomcat folder of the certificate download package contains the key store file www.domain.com.jks and the key store password file keystorePass.txt
When you choose to paste the CSR, Tomcat certificate cannot be downloaded, but you have to convert the format manually to generate the the Tomacat certificate. Steps are as follows:

> You can generate jks certificate with the certificate file and private key file in Nginx folder.

> Conversion tool: `https://www.trustasia.com/tools/cert-converter.htm`

> If you use the conversion tool, **key store password** must be set for further use in configuration file when you install the certificate.

#### 4.2 Install certificate

Configure the SSL connector. Save the file `www.domain.com.jks` in conf directory, and then configure the file`server.xml` in the same directory:

```
<Connector port="443" protocol="HTTP/1.1" SSLEnabled="true"
	maxThreads="150" scheme="https" secure="true"
	keystoreFile="conf/www.domain.com.jks"
	keystorePass="changeit"
	clientAuth="false" sslProtocol="TLS" />
```

Note:

| Configuration File Parameter | Description |
|---------|---------|
| clientAuth | If it is set to true, Tomcat requires all SSL clients to present a security certificate for authentication |
| keystoreFile | Specifies where the keystore file is saved. You can specify an absolute path or the relative path to environment variables in Tomcat installation directory. If this parameter is not set, by default, Tomcat reads the file named ".keystore" from the user directory of the current operating system user. |
| keystorePass | Specify the key store password. (If you fill in a private key password when applying for the certificate, enter the private key password, otherwise enter the password in the key store password file)
| sslProtocol | Specify the encryption/decryption protocol used by the socket. The default value is TLS |

#### 4.3 Security configuration for automatic redirection from http to https
Open web.xml in conf directory. Insert the following codes between `</welcome-file-list>` and `</web-app>`, that is. the penultimate paragraph
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

This step is to allow non-ssl connector to be redirected to the ssl connector. So you also need to configure server.xml:
```
<Connector port="8080" protocol="HTTP/1.1"
	connectionTimeout="20000"
	redirectPort="443" />
```
Set the redirectPort to be the ssl connector port 443, which takes effect after restart.

