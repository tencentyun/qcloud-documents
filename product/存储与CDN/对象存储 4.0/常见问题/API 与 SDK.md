## API 与其他 SDK 问题

### 调用 API 接口时，出现“Time out”等错误信息，该如何处理？

出现该提示，存在两种可能：
- 一是因为您发起请求的时间超过了签名的有效时间。
- 二是您的本地系统时间与北京时间不一致。

针对第一种可能，建议重新获取有效的请求签名再进行 API 操作。若是第二种可能，请将您的本地系统时间按照北京时间进行校正。

### 如何调用 API 删除掉未完成上传文件？

首先调用接口 ListMultipartUploads 列出未完成上传文件，然后调用 Abort Multipart upload 接口舍弃一个分块上传并删除已上传的块。

### 调用批量删除接口返回正确，但实际文件删除失败怎么办？

请检查删除的文件路径，文件路径不需要以`/`开头。

### 通过 JSON API 创建的存储桶和上传的对象，是否可以使用 XML API 管理？

可以，XML API 是基于 COS 底层架构，可以通过 XML API 操作由 JSON API 产生的数据。

### XML API 与 JSON API 之间的关系？

JSON API 接口即从2016年9月起用户接入 COS 使用的 API，上传域名为`<Region>.file.myqcloud.com`。 JSON API 接口将保持维护状态，可以正常使用但是不发展新特性。其与标准 XML API 底层架构相同，数据互通，可以交叉使用，但是接口不兼容，域名不一致。

### XML API 与 JSON API 的密钥是否通用？

通用。有关密钥信息可前往 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中的**云 API 密钥**页面进行查看和获取。

### XML API 与 JSON API 的签名是否通用？

不通用，XML API 和 JSON API 各自有各自的签名方式。详情请参见：

- [JSON API 签名](https://cloud.tencent.com/document/product/436/6054)
- [XML API 签名](https://cloud.tencent.com/document/product/436/7778)

### XML API 与 JSON API 设置的 ACL 权限是否通用？

不通用，XML API 和 JSON API 各自有各自的 ACL 权限。

### 如何获取 Python SDK 下载文件的临时链接？

详情请参见 [预签名 URL](https://cloud.tencent.com/document/product/436/35153) 文档。

### SDK 能否使用 CDN 加速域名进行访问？

支持，请根据您所使用的编程语言，并参见对应的 [SDK 文档](https://cloud.tencent.com/document/sdk) 进行操作。

## 小程序 SDK 类问题

### 小程序里请求多个域名，或者存储桶名称不确定，怎么解决白名单配置和限制问题？

SDK 实例化时，使用`ForcePathStyle:true`可以打开后缀式，只需要真正请求 url 格式如下`https://cos-ap-beijing.myqcloud.com/<BucketName-APPID>/<Key>`后缀式请求，在签名时会存储桶名称`/<BucketName-APPID>`也会加入签名计算。

### 小程序如何保存图片到本地？

先预先通过`cos.getObjectUrl`获取图片 url，而后调用`wx.downloadFile`下载图片得到临时路径，界面显示保存图片按钮，用户单击按钮后，调用`wx.saveImageToPhotosAlbum` 保存到相册。



## Java SDK 类问题

### 引入 SDK 运行后，出现 java.lang.NoSuchMethodError 的异常？


原因一般是发生了 JAR 包冲突，例如，用户的工程中的 httpclient 库中 的 JAR 包版本没有A方法，但是  SDK 依赖的 JAR 包使用了 A 方法。此时，由于运行时加载顺序的问题，加载了用户工程中的 httpclient  库，运行时便会抛出 NoSuchMethodError 的异常。
解决方法：将工程中引起 NoSuchMethodError 包的版本，改成和 SDK 中 pom.xml 里的对应库的版本一致。



### SDK 上传速度慢，日志频繁打印 IOException？

原因与解决办法：

 a. 首先确认下是否是通过公网访问 COS，目前同地域 CVM 访问 COS 走内网(内网域名解析出的 IP 是10、100、169网段，有关 COS 域名请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)，如果是通过公网确认出口带宽是否较小，或者是否有其他程序占用带宽资源。
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

