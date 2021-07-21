## 简介
Java SDK 提供对象访问 URL 的接口，可以分发给客户端，用于匿名下载或者分发。
>! 如果您的文件是**私有读**权限，那么本接口生成的 URL 不能直接用于访问资源。
>
生成的预签名 URL 包含协议名（HTTP 或者 HTTPS），该协议名与发起预签名请求的对象存储（Cloud Object Storage，COS）客户端设置的协议保持一致。具体使用请参见请求示例。

## 获取对象访问 URL

#### 方法原型

```java
public URL getObjectUrl(String bucketName, String key);
public URL getObjectUrl(String bucketName, String key, String versionId);
```



#### 请求示例1: 获取对象访问 URL

```java
// getObjectUrl 不需要验证身份信息
COSCredentials cred = new AnonymousCOSCredentials();
// 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-guangzhou"));
// 设置生成的 url 的协议名
clientConfig.setHttpProtocol(HttpProtocol.https);
// 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);

String key = "picture/photo.jpg";
String bucketName = "examplebucket-1250000000";

System.out.println(cosclient.getObjectUrl(bucketName, key));
```

#### 请求示例2: 获取指定版本的访问 URL

```java
// getObjectUrl 不需要验证身份信息
COSCredentials cred = new AnonymousCOSCredentials();
// 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-guangzhou"));
// 设置生成的 url 的协议名
clientConfig.setHttpProtocol(HttpProtocol.https);
// 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);

String key = "picture/photo.jpg";
String bucketName = "examplebucket-1250000000";
String versionId = "xxxyyyzzz111222333";

System.out.println(cosclient.getObjectUrl(bucketName, key, versionId));
```

#### 请求示例3: 获取指定域名的访问 URL

```java
// getObjectUrl 不需要验证身份信息
COSCredentials cred = new AnonymousCOSCredentials();
// 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-guangzhou"));
// 设置生成的 url 的协议名
clientConfig.setHttpProtocol(HttpProtocol.https);
// 设置自定义的域名
UserSpecifiedEndpointBuilder endpointBuilder = new UserSpecifiedEndpointBuilder("test.endpoint.com", "service.cos.myqcloud.com");
clientConfig.setEndpointBuilder(endpointBuilder);
// 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);

String key = "picture/photo.jpg";
String bucketName = "examplebucket-1250000000";
String versionId = "xxxyyyzzz111222333";

System.out.println(cosclient.getObjectUrl(bucketName, key, versionId));
```

#### 参数说明

| 参数名称   | 参数描述         |类型       | 是否必填         | 
| --------- | -------------- |---------- | ----------- |
| Bucket    | 存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
| Key       | 对象键（Key）是对象在存储桶中的唯一标识，详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324#.E5.AF.B9.E8.B1.A1.E9.94.AE) | String | 是 | 
| versionId | 在存储桶开启版本控制时，指定对象的版本号 | String | 否 |

