## Apache HTTPS 双向认证配置流程

以第三方开发者域名 `www.example.com` 为例。

###  情况1：第三方开发者已有权威第三方签发的证书

1. 开发者准备权威第三方为 `www.example.com` 签发的证书 `www.example.com.crt` 和派发的私钥 `www.example.com.key`。注意必须是权威的第三方机构（如天威、globalsign 等）签发的证书。
1. 腾讯云给开发者后台提供用于验证请求方（腾讯）证书的 CA 证书 [TencentQQAuthCA.crt](http://share.weiyun.com/7d86303625fda66998bcc46f79320503)。
1. 参照 [Apache HTTPS 双向认证配置参考](#apache-https-.E5.8F.8C.E5.90.91.E8.AE.A4.E8.AF.81.E9.85.8D.E7.BD.AE.E5.8F.82.E8.80.83) 进行配置。

### 情况2：第三方开发者向腾讯云申请为域名签发证书

1. 第三方开发者向腾讯云申请为域名签发证书第三方开发者向腾讯云提供开发者后台域名，例如 `www.example.com`。
1. 腾讯云给开发者后台域名 `www.example.com` 签发证书和私钥，`www.example.com.crt` 和 `www.example.com.key`。
1. 腾讯云给开发者后台提供用于验证请求方（腾讯）证书的 CA 证书 [TencentQQAuthCA.crt](http://share.weiyun.com/7d86303625fda66998bcc46f79320503)。
2.  参照 [Apache HTTPS 双向认证配置参考](#apache-https-.E5.8F.8C.E5.90.91.E8.AE.A4.E8.AF.81.E9.85.8D.E7.BD.AE.E5.8F.82.E8.80.83) 进行配置。
	
## Apache HTTPS 双向认证配置参考

将 `www.example.com.crt`、`www.example.com.key` 和 `TencentQQAuthCA.crt` 拷贝到 Apache 的安装目录的 conf 文件夹下。修改 `httpd.conf` 配置文件，参考配置如下。

```
SSLEngine on  #开启 SSL
SSLCertificateFile "/usr/local/apache2/conf/example.com.crt"            #腾讯给第三方签发的证书
SSLCertificateKeyFile "/usr/local/apache2/conf/example.com.key"         #和证书配对的私钥
SSLCACertificateFile  "/usr/local/apache2/conf/TencentQQAuthCA.crt" #腾讯认证的 CA 证书
SSLVerifyClient require  #验证请求来源
```