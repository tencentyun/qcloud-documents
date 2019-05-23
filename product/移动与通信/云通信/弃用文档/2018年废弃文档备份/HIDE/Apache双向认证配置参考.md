## Apache HTTPS双向认证配置

以第三方开发者域名www.example.com为例。

### 第三方开发者已有权威第三方签发的证书

	开发者准备权威第三方为www.example.com签发的证书www.example.com.crt和派发的私钥www.example.com.key；注意必须是权威的第三方机构（如天威、globalsign等）签发的证书；
	腾讯云给开发者后台提供用于验证请求方（腾讯）证书的CA证书[TencentQQAuthCA.crt](http://share.weiyun.com/62eb46af9661c94ef7903def73e7a10c)。

### 第三方开发者向腾讯云申请为域名签发证书

	第三方开发者向腾讯云申请为域名签发证书第三方开发者向腾讯云提供开发者后台域名，例如www.example.com；
	腾讯云给开发者后台域名www.example.com签发证书和私钥，www.example.com.crt和www.example.com.key；
	腾讯云给开发者后台提供用于验证请求方（腾讯）证书的CA证书TencentQQAuthCA.crt。
	
### Apache配置参考

开发者后台配置Apache。将www.example.com.crt、www.example.com.key和TencentQQAuthCA.crt拷贝到Apache的安装目录的conf文件夹下。修改httpd.conf配置文件，参考配置如下。
SSLEngine on  #开启SSL
SSLCertificateFile "/usr/local/apache2/conf/example.com.crt"            #腾讯给第三方签发的证书
SSLCertificateKeyFile "/usr/local/apache2/conf/example.com.key"         #和证书配对的私钥
SSLCACertificateFile  "/usr/local/apache2/conf/TencentQQAuthCA.crt" #腾讯认证的CA证书
SSLVerifyClient require  #验证请求来源