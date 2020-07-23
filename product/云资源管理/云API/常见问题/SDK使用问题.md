### Python证书问题

在 Mac 操作系统安装 Python 3.6或以上版本时，可能会遇到证书错误：
```
Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056).
```
这是因为在 Mac 操作系统下，Python 不再使用系统默认的证书，且本身也不提供证书。在进行 HTTPS 请求时，需要使用 `certifi` 库提供的证书，但 SDK 不支持指定，所以只能使用 
```
sudo "/Applications/Python 3.6/Install Certificates.command"
```

命令安装证书才能解决此问题。



### PHP证书问题

如果您的 PHP 环境证书有问题，可能会遇到报错，类似于
```
cURL error 60: See http://curl.haxx.se/libcurl/c/libcurl-errors.html
```

请尝试按如下步骤解决：

1. 到 https://curl.haxx.se/ca/cacert.pem 下载证书文件 `cacert.pem`，将其保存到 PHP 安装路径下。
2. 编辑 `php.ini` 文件，删除 `curl.cainfo` 配置项前的分号注释符（;），值设置为保存的证书文件 `cacert.pem` 的绝对路径。
3. 重启依赖 PHP 的服务。



### php_curl 扩展

此 SDK 依赖的 GuzzleHttp 需要开启 php_curl 扩展，查看环境上的 php.ini 环境确认是否已启用，例如在 Linux 环境下，PHP 7.1 版本，托管在 Apache 下的服务，可以打开 `/etc/php/7.1/apache2/php.ini` 中查看 extension=php_curl.dll 配置项是否已被注释，请删除此项配置前的注释符并重启 Apache。



### Java依赖冲突

目前，SDK 依赖 okhttp 2.5.0，如果和其他依赖 okhttp3 的包混用时，有可能会报错，例如：
```
Exception in thread "main" java.lang.NoSuchMethodError: okio.BufferedSource.rangeEquals(JLokio/ByteString;)Z
```
原因是 okhttp3 依赖 okio 1.12.0，而 okhttp 依赖 okio 1.6.0，maven 在解析依赖时的规则是路径最短优先和顺序优先，所以如果 SDK 在 pom.xml 依赖中先被声明，则 okio 1.6.0 会被使用，从而报错。在 SDK 没有升级到 okhttp3 前的解决办法：
1.在 pom.xml 中明确指定依赖 okio 1.12.0 版本（注意可能有其他包需要用到更高的版本，变通下取最高版本就可以了）；
2.将 SDK 放在依赖的最后（注意如果此前已经编译过，需要先删除掉 maven 缓存的 okhttp 包），以同时使用依赖 okhttp3 的 CMQ SDK 为例，形如（注意变通版本号）： 
```xml
    <dependency>
      <groupId>com.qcloud</groupId>
      <artifactId>cmq-http-client</artifactId>
      <version>1.0.7</version>
    </dependency>
    <dependency>
      <groupId>com.tencentcloudapi</groupId>
      <artifactId>tencentcloud-sdk-java</artifactId>
      <version>3.1.59</version>
    </dependency>
```



### .NET 依赖冲突

 SDK 依赖的 FluentClient 使用的是3.2版本，但这个包目前发布了4.0版本且不兼容低版本，在 nuget 中升级此包到4.0版本会导致无法调用或调用失败等问题。 



### 旧版SDK
旧版本的SDK存放于 QcloudApi 目录，详细使用请参考 [旧版 SDK](https://github.com/QcloudApi)，该版本已不再维护，推荐使用新版SDK。
