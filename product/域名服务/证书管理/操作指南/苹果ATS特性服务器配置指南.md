配置指南：
1. 需要配置符合PFS规范的加密套餐，目前推荐配置：
`ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4`
2. 需要在服务端TLS协议中启用TLS1.2，目前推荐配置：
`TLSv1 TLSv1.1 TLSv1.2`

### 1.Nginx 证书配置

更新Nginx根目录下 conf/nginx.conf 文件如下：
```
server {
	ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
	ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
}
```

### 2.Apache 证书配置

更新Apache根目录下 conf/httpd.conf 文件如下：
```
<IfModule mod_ssl.c>
        <VirtualHost *:443>
		SSLProtocol TLSv1 TLSv1.1 TLSv1.2
		SSLCipherSuite ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4
		</VirtualHost>
</IfModule>
```

### 3.Tomcat 证书配置
更新 %TOMCAT_HOME%\conf\server.xml 文件如下：
```
<Connector port="443" protocol="HTTP/1.1" SSLEnabled="true"
    scheme="https" secure="true"
    SSLProtocol="TLSv1+TLSv1.1+TLSv1.2"
    SSLCipherSuite="ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4" />
```

### 4.IIS 证书配置
#### 4.1 方法一
Windows 2008及更早的版本不支持TLS1_2协议  所以无法调整  2008R2 TLS1_2协议默认是关闭的  需要启用此协议达到ATS要求

以2008 R2为例，导入证书后没有对协议及套件做任何的调整。
证书导入后检测到套件是支持ATS需求的，但协议TLS1_2没有被启用，ATS需要TLS1_2的支持。可使用的ssltools工具（亚洲诚信提供，[单击下载](http://www.trustasia.com/down/ssltools.zip)）启用TLS1_2协议

![1](https://mc.qcloudimg.com/static/img/bed43955994817ef3dcca0f8d617e117/1.png)

勾选三个TLS协议并重启系统即可。
如果检查到PFS不支持，在加密套件中选中带ECDHE和DHE就可以了。

#### 4.2 方法二
开始——运行  输入regedit
找到HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols右键->新建->项->新建TLS 1.1,TLS 1.2
TLS 1.1和TLS 1.2 右键->新建->项->新建Server, Client
在新建的Server和Client中都新建如下的项(DWORD 32位值), 总共4个
DisabledByDefault [Value = 0]
Enabled [Value = 1]

![2](https://mc.qcloudimg.com/static/img/a6d5d5103f41996d2297e897f3b15b8f/2.png)

完成后重启系统

加密套件调整
对于前向保密加密套件不支持的话可通过组策略编辑器进行调整。
开始菜单——运行、输入gpedit.msc 进行加密套件调整  在此操作之前需要先开启TLS1_2协议

![3](https://mc.qcloudimg.com/static/img/edbf53965efe2fc929347479bbfa3ffc/3.png)
双击SSL密码套件顺序

![4](https://mc.qcloudimg.com/static/img/0fd0450901a9ececba02576344cd5679/4.png)

把支持的ECDHE加密套件加入SSL密码套件中  以逗号（,）分隔
打开一个空白写字板文档。
复制下图中右侧可用套件的列表并将其粘贴到该文档中。
按正确顺序排列套件；删除不想使用的所有套件。
在每个套件名称的末尾键入一个逗号(最后一个套件名称除外)。确保没有嵌入空格。
删除所有换行符，以便密码套件名称位于单独的一个长行上。
将密码套件行复制到剪贴板，然后将其粘贴到编辑框中。最大长度为 1023 个字符。

![5](https://mc.qcloudimg.com/static/img/846da62574cadaa8fa097c082c967cad/5.png)

可将以下套件加入密码套件中
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

附:
推荐套件组合：
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
