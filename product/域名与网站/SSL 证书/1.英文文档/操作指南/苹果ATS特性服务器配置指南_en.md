Configuration Guide:
1. You need to configure the encryption package in line with the PFS specification. The recommended configuration is:
`ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4`
2. You need to enable TLS1.2 in the TLS protocol of server. The recommended configuration is:
`TLSv1 TLSv1.1 TLSv1.2`

### 1.Nginx Certificate Configuration

Update the conf/nginx.conf file in the Nginx root directory as follows:
```
server {
	ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
	ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
}
```

### 2.Apache Certificate Configuration

Update the conf/httpd.conf file in the Apache root directory as follows:
```
<IfModule mod_ssl.c>
        <VirtualHost *:443>
		SSLProtocol TLSv1 TLSv1.1 TLSv1.2
		SSLCipherSuite ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4
		</VirtualHost>
</IfModule>
```

### 3.Tomcat Certificate Configuration
Update the %TOMCAT_HOME%\conf\server.xml file as follows:
```
<Connector port="443" protocol="HTTP/1.1" SSLEnabled="true"
    scheme="https" secure="true"
    SSLProtocol="TLSv1+TLSv1.1+TLSv1.2"
    SSLCipherSuite="ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4" />
```

### 4.IIS Certificate Configuration
#### 4.1 Method 1
Windows 2008 and earlier versions do not support TLS1_2 protocol and cannot be adjusted. 2008R2 TLS1_2 protocol is disabled by default and needs to be enabled to meet ATS requirements

Taking 2008 R2 as an example, there is no adjustment to the protocol and the suite after the certificate is imported.
It is detected that the suite supports ATS requirements after the certificate is imported. But protocol TLS1_2 required for ATS is not enabled. You can use SSL tools provided by TrustAsia. [Click here to download](http://www.trustasia.com/down/ssltools.zip) to enable TLS1_2 protocol

![1](https://mc.qcloudimg.com/static/img/bed43955994817ef3dcca0f8d617e117/1.png)

Select three TLS protocols and restart the system to complete the process.
If PFS is found not to be supported, select encryption suites with ECDHE and DHE.

#### 4.2 Method 2
Click **Start** -> **Run**. Enter regedit
Find HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols, and right-click it, then click **New** -> **Item** -> **Create TLS 1.1, TLS 1.2**
Right-click TLS 1.1 and TLS 1.2, and click **New** -> **Item** -> **Create Server, Client**
Create the following items (4 in total, DWORD 32-bit value) in the new Server and Client
DisabledByDefault [Value = 0]
Enabled [Value = 1]

![2](https://mc.qcloudimg.com/static/img/a6d5d5103f41996d2297e897f3b15b8f/2.png)

Restart the system after completion

Encryption suite adjustment
Adjustments can be made through the group policy editor if the forward privacy encryption suite is not supported.
Click **Start** -> **Run**, and enter gpedit.msc for encryption suite adjustment after enabling TLS1_2 protocol.

![3](https://mc.qcloudimg.com/static/img/edbf53965efe2fc929347479bbfa3ffc/3.png)
Double-click the **SSL cipher suite order**.

![4](https://mc.qcloudimg.com/static/img/0fd0450901a9ececba02576344cd5679/4.png)

Add the supported ECDHE cipher suites to the SSL cipher suites, separated by comma (,)
Open a blank WordPad document.
Copy the list of available suites on the right in the figure below and paste it into the document.
Sort suites in the correct order and delete any suites you do not want to use.
Type a comma at the end of each suite name (except for the last one). Make sure no space is added.
Remove all the line breaks so that the cipher suite names are in a single, long line.
Copy the cipher suite line to the clipboard and paste it into the edit box with the maximum length of 1,023 characters.

![5](https://mc.qcloudimg.com/static/img/846da62574cadaa8fa097c082c967cad/5.png)

The following suites can be added to the cipher suite
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

Attachment:
Recommended suite combination:
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA_P256
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA_P384
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA_P521
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P256
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P384
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P521
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P256
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P384
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P521
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P256
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P384
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P521
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
TLS_RSA_WITH_AES_128_CBC_SHA
TLS_RSA_WITH_AES_256_CBC_SHA
TLS_RSA_WITH_3DES_EDE_CBC_SHA
TLS_RSA_WITH_AES_128_CBC_SHA256
TLS_RSA_WITH_AES_256_CBC_SHA256
TLS_RSA_WITH_AES_128_GCM_SHA256
TLS_RSA_WITH_AES_256_GCM_SHA384

