### Python 证书问题

在 Mac 操作系统安装 Python 3.6 或以上版本时，可能会遇到如下证书错误：
```
Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056).
```
执行以下命令，安装证书即可解决问题。
<dx-alert infotype="explain" title="">
Mac 操作系统下的 Python 不再使用系统默认的证书，且本身也不提供证书。在进行 HTTPS 请求时，需使用 `certifi` 库提供的证书。
</dx-alert>
```
sudo "/Applications/Python 3.6/Install Certificates.command"
```



### PHP 证书问题

如果您的 PHP 环境证书有问题，可能会遇到如下报错信息：
```
cURL error 60: See http://curl.haxx.se/libcurl/c/libcurl-errors.html
```
请参考以下步骤进行解决：
1. 前往 `https://curl.haxx.se/ca/cacert.pem` 下载证书文件 `cacert.pem`，将其保存到 PHP 安装路径下。
2. 编辑 `php.ini` 文件，删除 `curl.cainfo` 配置项前的分号注释符`;`，值设置为保存的证书文件 `cacert.pem` 的绝对路径。
3. 重启依赖 PHP 的服务。



### php_curl 扩展

此 SDK 依赖的 GuzzleHttp 需要开启 php_curl 扩展，查看环境上的 php.ini 环境确认是否已启用，例如在 Linux 环境下，PHP 7.1 版本，托管在 Apache 下的服务，可以打开 `/etc/php/7.1/apache2/php.ini` 中查看 extension=php_curl.dll 配置项是否已被注释，请删除此项配置前的注释符并重启 Apache。



### Java 依赖冲突

目前 SDK 依赖 okhttp 2.5.0，如果和其他依赖 okhttp3 的包混用时，可能会遇到如下报错信息：
```
Exception in thread "main" java.lang.NoSuchMethodError: okio.BufferedSource.rangeEquals(JLokio/ByteString;)Z
```
okhttp3 依赖 okio 1.12.0，而 okhttp 依赖 okio 1.6.0，maven 在解析依赖时的规则是路径最短优先和顺序优先，如果 SDK 在 pom.xml 依赖中先被声明，则 okio 1.6.0 会被使用，从而出现报错。在 SDK 未升级到 okhttp3 前的解决步骤如下：
1. 在 pom.xml 中明确指定依赖 okio 1.12.0 版本。如有其他包需使用更高版本，则取两者最高版本即可。
2. 将 SDK 引用放在 pom.xml 文件的最后，若此前已进行编译，则需要先删除 maven 缓存的 okhttp 包。以同时使用依赖 okhttp3 的 CMQ SDK 为例：
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

 SDK 依赖的 FluentClient 使用的是3.2版本，但 FluentClient 目前发布了4.0版本且不兼容低版本，若在 nuget 中升级此包到4.0版本会导致无法调用或调用失败等问题。 



### 旧版 SDK
旧版本 SDK 已不再维护，推荐使用新版SDK。旧版本 SDK 存放在 QcloudApi 目录下，详情请参见 [旧版 SDK](https://github.com/QcloudApi)，
