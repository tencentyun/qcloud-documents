## 简介
Java SDK 提供获取请求预签名 URL 和生成签名接口，可以分发给客户端，用于下载或者上传。如果您的文件是私有读权限，那么请注意预签名链接只有一定的有效期。

## 获取请求预签名 URL 

#### 方法原型

```java
public URL generatePresignedUrl(GeneratePresignedUrlRequest req) throws CosClientException
```

#### 参数说明

| 参数名称 | 描述         | 类型                        |
| -------- | ------------ | --------------------------- |
| req      | 预签名请求类 | GeneratePresignedUrlRequest |

Request 成员说明：

| Request 成员    | 设置方法            | 描述                                                         | 类型                    |
| --------------- | ------------------- | ------------------------------------------------------------ | ----------------------- |
| method          | 构造函数或 set 方法 | HTTP 方法，可选：GET、POST、PUT、DELETE、HEAD                | HttpMethodName          |
| bucketName      | 构造函数或 set 方法 | 存储桶名称，存储桶的命名格式为 BucketName-APPID，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String |
| key             | 构造函数或 set 方法 | 对象键（Key）是对象在存储桶中的唯一标识，详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324#.E5.AF.B9.E8.B1.A1.E9.94.AE) | String                  |
| expiration      | set 方法            | 签名过期的时间                                               | Date                    |
| contentType     | set 方法            | 要签名的请求中的 Content-Type                                | String                  |
| contentMd5      | set 方法            | 要签名的请求中的 Content-Md5                                 | String                  |
| responseHeaders | set 方法            | 签名的下载请求中要覆盖的返回的 HTTP 头                       | ResponseHeaderOverrides |
| versionId | set 方法            | 在存储桶开启多版本的时候，指定对象的版本号                       | String |


#### 示例1

使用永久密钥生成一个带签名的下载链接，示例代码如下：

[//]: # (.cssg-snippet-get-presign-download-url)
```java
// 初始化永久密钥信息
String secretId = "COS_SECRETID";
String secretKey = "COS_SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
Region region = new Region("COS_REGION");
ClientConfig clientConfig = new ClientConfig(region);
// 生成 cos 客户端。
COSClient cosClient = new COSClient(cred, clientConfig);
// 存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式
String bucketName = "examplebucket-1250000000";
String key = "exampleobject";
GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
// 设置签名过期时间(可选), 若未进行设置, 则默认使用 ClientConfig 中的签名过期时间(1小时)
// 这里设置签名在半个小时后过期
Date expirationDate = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);
req.setExpiration(expirationDate);
URL url = cosClient.generatePresignedUrl(req);
System.out.println(url.toString());
cosClient.shutdown();
```

#### 示例2

使用临时密钥生成一个带签名的下载链接，并设置覆盖要返回的一些公共头部（例如 content-type，content-language），示例代码如下：

[//]: # (.cssg-snippet-get-presign-download-url-override-headers)
```java
// 传入获取到的临时密钥 (tmpSecretId, tmpSecretKey, sessionToken)
String tmpSecretId = "COS_SECRETID";
String tmpSecretKey = "COS_SECRETKEY";
String sessionToken = "COS_TOKEN";
COSCredentials cred = new BasicSessionCredentials(tmpSecretId, tmpSecretKey, sessionToken);
// 设置 bucket 的区域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
// clientConfig 中包含了设置 region, https(默认 http), 超时, 代理等 set 方法, 使用可参见源码或者常见问题 Java SDK 部分
Region region = new Region("COS_REGION");
ClientConfig clientConfig = new ClientConfig(region);
// 生成 cos 客户端
COSClient cosClient = new COSClient(cred, clientConfig);
// 存储桶的命名格式为 BucketName-APPID 
String bucketName = "examplebucket-1250000000";
String key = "exampleobject";
GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
// 设置下载时返回的 http 头
ResponseHeaderOverrides responseHeaders = new ResponseHeaderOverrides();
String responseContentType = "image/x-icon";
String responseContentLanguage = "zh-CN";
String responseContentDispositon = "filename=\"exampleobject\"";
String responseCacheControl = "no-cache";
String cacheExpireStr =
        DateUtils.formatRFC822Date(new Date(System.currentTimeMillis() + 24L * 3600L * 1000L));
responseHeaders.setContentType(responseContentType);
responseHeaders.setContentLanguage(responseContentLanguage);
responseHeaders.setContentDisposition(responseContentDispositon);
responseHeaders.setCacheControl(responseCacheControl);
responseHeaders.setExpires(cacheExpireStr);
req.setResponseHeaders(responseHeaders);
// 设置签名过期时间(可选)，若未进行设置，则默认使用 ClientConfig 中的签名过期时间(1小时)
// 这里设置签名在半个小时后过期
Date expirationDate = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);
req.setExpiration(expirationDate);
URL url = cosClient.generatePresignedUrl(req);
System.out.println(url.toString());
cosClient.shutdown();
```

#### 示例3

生成公有读 Bucket（匿名可读），不需要签名的链接，示例代码如下：

[//]: # (.cssg-snippet-get-presign-download-url-public)
```java
// 生成匿名的请求签名，需要重新初始化一个匿名的 cosClient
// 初始化用户身份信息, 匿名身份不用传入 SecretId、SecretKey 等密钥信息
COSCredentials cred = new AnonymousCOSCredentials();
// 设置 bucket 的区域，COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing"));
// 生成 cos 客户端
COSClient cosClient = new COSClient(cred, clientConfig);
// bucket 名需包含 appid
String bucketName = "examplebucket-1250000000";

String key = "exampleobject";
GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
URL url = cosClient.generatePresignedUrl(req);
System.out.println(url.toString());
cosClient.shutdown();
```

#### 示例4

生成一些预签名的上传链接，可直接分发给客户端进行文件的上传，示例代码如下：

[//]: # (.cssg-snippet-get-presign-upload-url)
```java
// 存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式
String bucketName = "examplebucket-1250000000";
String key = "exampleobject";
// 设置签名过期时间(可选), 若未进行设置, 则默认使用 ClientConfig 中的签名过期时间(1小时)
// 这里设置签名在半个小时后过期
Date expirationTime = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);
URL url = cosClient.generatePresignedUrl(bucketName, key, expirationTime, HttpMethodName.PUT);
System.out.println(url.toString());
cosClient.shutdown();
```

## 生成签名

COSSigner 类提供构造 COS 签名的方法，用于分发给移动端 SDK，进行文件的上传和下载。签名的路径和分发后要进行操作的 key 相匹配。

#### 方法原型

```java
// 构造 COS 签名
public String buildAuthorizationStr(HttpMethodName methodName, String resouce_path,
        COSCredentials cred, Date expiredTime);

// 构造 COS 签名
// 第二个方法比第一个方法额外提供对部分 HTTP Header 和所有传入的 URL 中的参数进行签名
// 用于更复杂的签名控制, 生成的签名必须在上传下载等操作时，也要携带对应的 header 和 param
public String buildAuthorizationStr(HttpMethodName methodName, String resouce_path,
        Map<String, String> headerMap, Map<String, String> paramMap, COSCredentials cred,
        Date expiredTime);
```

#### 参数说明

| 参数名称     | 描述                                                         | 类型           |
| ------------ | ------------------------------------------------------------ | -------------- |
| methodName   | HTTP 请求方法，可设置 PUT、GET、DELETE、HEAD、POST           | HttpMethodName |
| resouce_path | 要签名的路径, 同上传文件的 key，需要以`/`开始                | HttpMethodName |
| cred         | 密钥信息                                                     | COSCredentials |
| expiredTime  | 过期时间                                                     | Date           |
| headerMap    | 要签名的 HTTP Header map，只对传入的 Content-Type，Content-Md5 和以 x 开头的 header 进行签名 | Map            |
| paramMap     | 要签名的 URL Param map                                        | Map            |

#### 返回值
签名字符串，类型为 String。


#### 示例1：生成一个上传签名

[//]: # (.cssg-snippet-get-authorization-for-upload)
```java
String secretId = "COS_SECRETID";
String secretKey = "COS_SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
COSSigner signer = new COSSigner();
//设置过期时间为1个小时
Date expiredTime = new Date(System.currentTimeMillis() + 3600L * 1000L);
// 要签名的 key, 生成的签名只能用于对应此 key 的上传
String key = "/exampleobject";
String sign = signer.buildAuthorizationStr(HttpMethodName.PUT, key, cred, expiredTime);
```

#### 示例2：生成一个下载签名

[//]: # (.cssg-snippet-get-authorization-for-download)
```java
String secretId = "COS_SECRETID";
String secretKey = "COS_SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
COSSigner signer = new COSSigner();
// 设置过期时间为1个小时
Date expiredTime = new Date(System.currentTimeMillis() + 3600L * 1000L);
// 要签名的 key, 生成的签名只能用于对应此 key 的下载
String key = "/exampleobject";
String sign = signer.buildAuthorizationStr(HttpMethodName.GET, key, cred, expiredTime);
```

#### 示例3：生成一个删除签名

[//]: # (.cssg-snippet-get-authorization-for-delete)
```java
String secretId = "COS_SECRETID";
String secretKey = "COS_SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
COSSigner signer = new COSSigner();
// 设置过期时间为1个小时
Date expiredTime = new Date(System.currentTimeMillis() + 3600L * 1000L);
// 要签名的 key, 生成的签名只能用于对应此 key 的删除
String key = "/exampleobject";
String sign = signer.buildAuthorizationStr(HttpMethodName.DELETE, key, cred, expiredTime);
```
