### 引入 SDK 运行后，出现 java.lang.NoSuchMethodError 的异常？


原因一般是发生了 JAR 包冲突，例如，用户的工程中的 httpclient 库中 的 JAR 包版本没有A方法，但是  SDK 依赖的 JAR 包使用了 A 方法。此时，由于运行时加载顺序的问题，加载了用户工程中的 httpclient  库，运行时便会抛出 NoSuchMethodError 的异常。
解决方法：将工程中引起 NoSuchMethodError 包的版本，改成和 SDK 中 pom.xml 里的对应库的版本一致。



### SDK 上传速度慢，日志频繁打印 IOException？

原因与解决办法：

 a. 首先确认下是否是通过公网访问 COS，目前同地域 CVM 访问 COS 走内网（内网域名解析出的 IP 是10、100、169网段，有关 COS 域名请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)），如果是通过公网确认出口带宽是否较小，或者是否有其他程序占用带宽资源。
 b. 确保在生产环境中的日志级别不是 DEBUG，推荐使用 INFO 日志。
 c. 目前简单上传速度可达10MB，高级 API 在32并发的情况下速度可达60MB,如果速度远低于此两个值，请参考 a 和 b。
 d. 如果 WARN 日志打印 IOException 可以忽略，SDK 会进行重试. IOException 的原因可能是网速过慢，原因可参考 a 和 b。

### SDK 如何创建目录？

对象存储中文件和目录都是对象，目录只是以`/`结尾的对象。创建文件时，不需要创建目录。如创建一个对象键为 `xxx/yyy/zzz.txt`的文件，只用把 key 设置为`xxx/yyy/zzz.txt`即可，不用建立`xxx/yyy/`这个对象。在控制台上展示时，也会以`/`作为分隔，展示出目录的层级效果。但这些目录对象是不存在的。如果想创建一个目录对象，可使用以下的示例代码：

```java
String bucketName = "examplebucket-1250000000";
String key = "folder/images/";
// 目录对象即是一个/结尾的空文件，上传一个长度为 0 的 byte 流
InputStream input = new ByteArrayInputStream(new byte[0]);
ObjectMetadata objectMetadata = new ObjectMetadata();
objectMetadata.setContentLength(0);

PutObjectRequest putObjectRequest =
new PutObjectRequest(bucketName, key, input, objectMetadata);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);
```

### SDK 如何使用 HTTPS?

SDK 中相关的配置都统一放在 ClientConfig 类中，示例代码如下：

```java
// 初始化用户身份信息(secretId, secretKey)
String secretId = "COS_SECRETID";
String secretKey = "COS_SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
// 设置 bucket 的区域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 配置使用 https
clientConfig.setHttpProtocol(HttpProtocol.https);
// 生成 cos 客户端
COSClient cosClient = new COSClient(cred, clientConfig);
```

### SDK 如何使用代理？

对于需要使用代理访问 COS 的客户，可在 ClientConfig 类中，配置使用代理 IP （或域名）以及端口，示例代码如下：

```java
// 初始化用户身份信息(secretId, secretKey)
String secretId = "COS_SECRETID";
String secretKey = "COS_SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
// 设置 bucket 的区域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 配置使用代理(IP 和端口需要同时设置)
// 设置代理 IP (也可传入域名)
clientConfig.setHttpProxyIp("192.168.2.3");
// 设置代理端口
clientConfig.setHttpProxyPort(8080);
// 生成 cos 客户端
COSClient cosClient = new COSClient(cred, clientConfig);
```

### 如何设置自定义 EndpointBuilder？
您的场景也许需要指定 API 请求的 Endpoint，此时，您需要实现 EndpointBuilder 接口中的 buildGeneralApiEndpoint 和 buildGetServiceApiEndpoint 中的两个函数，分别为普通 API 请求和 GETService 请求指定远端的 Endpoint。使用示例如下：
```
// 步骤1：实现 EndpointBuilder 接口中的两个函数
class SelfDefinedEndpointBuilder implements EndpointBuilder {
    @Override
    public String buildGeneralApiEndpoint(String bucketName) {
        return String.format("%s.%s", bucketName, "mytest.com");
    }

    @Override
    public String buildGetServiceApiEndpoint() {
        return "service.mytest.com";
    }
}

// 步骤2：初始化客户端
String secretId = "COS_SECRETID";
String secretKey = "COS_SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
SelfDefinedEndpointBuilder selfDefinedEndpointBuilder = new SelfDefinedEndpointBuilder();
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing"));
clientConfig .setEndpointBuilder(selfDefinedEndpointBuilder);
COSClient cosClient = new COSClient(cred, clientConfig);
```

### SDK 的上传、下载、批量删除等操作中，使用的 key 值是否需要添加 '/' 前缀？
对象存储的 key 值无需携带 '/' 前缀。例如，您将对象 key 值设置为 exampleobject 上传的对象，可以通过 URL： `http://cos.ap-guangzhou.myqcloud.com/exampleobject`进行访问。
>!在批删请求中，请勿传入 '/' 前缀的 key，这将导致对象删除失败。
