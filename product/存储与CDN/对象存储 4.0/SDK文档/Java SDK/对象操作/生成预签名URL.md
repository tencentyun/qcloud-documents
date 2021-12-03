## 简介

本文档提供关于生成对象预签名链接的示例代码。

>?
> - 建议用户[使用临时密钥](https://cloud.tencent.com/document/product/436/14048)生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄漏目标存储桶或对象之外的资源。
> - 如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。
> 

## 简单操作

简单操作由 COSClient 类型发起请求，使用简单操作之前必须先创建一个 COSClient 实例。

COSClient 实例是并发安全的，这里推荐一个进程只创建一个 COSClient 实例，当不会再通过这个实例发起请求的时候，再选择关闭这个实例。

### 创建 COSClient

调用 COS 的接口之前，必须先创建一个 COSClient 的实例。

```java
// 创建 COSClient 实例，这个实例用来后续调用请求
COSClient createCOSClient() {
    // 设置用户身份信息。
    // SECRETID 和 SECRETKEY 请登录访问管理控制台 https://console.cloud.tencent.com/cam/capi 进行查看和管理
    String secretId = "SECRETID";
    String secretKey = "SECRETKEY";
    COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);

    // ClientConfig 中包含了后续请求 COS 的客户端设置：
    ClientConfig clientConfig = new ClientConfig();

    // 设置 bucket 的地域
    // COS_REGION 请参照 https://cloud.tencent.com/document/product/436/6224
    clientConfig.setRegion = new Region("COS_REGION");

    // 设置请求协议, http 或者 https
    // 5.6.53 及更低的版本，建议设置使用 https 协议
    // 5.6.54 及更高版本，默认使用了 https
    clientConfig.setHttpProtocol(HttpProtocol.https);

    // 以下的设置，是可选的：

    // 设置 socket 读取超时，默认 30s
    clientConfig.setSocketTimeout(30*1000);
    // 设置建立连接超时，默认 30s
    clientConfig.setConnectionTimeout(30*1000);

    // 如果需要的话，设置 http 代理，ip 以及 port
    clientConfig.setHttpProxyIp("httpProxyIp");
    clientConfig.setHttpProxyPort("httpProxyPort");

    // 生成 cos 客户端。
    return new COSClient(cred, clientConfig);
}
```

### 使用临时密钥创建 COSClient

如果要使用临时密钥请求 COS，则需要用临时密钥创建 COSClient。
本 SDK 并不能生成临时密钥，而需要使用额外的操作来生成，参考 [临时密钥生成](https://cloud.tencent.com/document/product/436/14048#cos-sts-sdk)。

```java

// 创建 COSClient 实例，这个实例用来后续调用请求
COSClient createCOSClient() {
    // 这里需要已经获取到临时密钥的结果。
    // 临时密钥的生成参考 https://cloud.tencent.com/document/product/436/14048#cos-sts-sdk
    String tmpSecretId = "TMPSECRETID";
    String tmpSecretKey = "TMPSECRETKEY";
    String sessionToken = "SESSIONTOKEN";

    COSCredentials cred = new BasicSessionCredentials(tmpSecretId, tmpSecretKey, sessionToken);

    // ClientConfig 中包含了后续请求 COS 的客户端设置：
    ClientConfig clientConfig = new ClientConfig();

    // 设置 bucket 的地域
    // COS_REGION 请参照 https://cloud.tencent.com/document/product/436/6224
    clientConfig.setRegion = new Region("COS_REGION");

    // 设置请求协议, http 或者 https
    // 5.6.53 及更低的版本，建议设置使用 https 协议
    // 5.6.54 及更高版本，默认使用了 https
    clientConfig.setHttpProtocol(HttpProtocol.https);

    // 以下的设置，是可选的：

    // 设置 socket 读取超时，默认 30s
    clientConfig.setSocketTimeout(30*1000);
    // 设置建立连接超时，默认 30s
    clientConfig.setConnectionTimeout(30*1000);

    // 如果需要的话，设置 http 代理，ip 以及 port
    clientConfig.setHttpProxyIp("httpProxyIp");
    clientConfig.setHttpProxyPort("httpProxyPort");

    // 生成 cos 客户端。
    return new COSClient(cred, clientConfig);
}
```

### 生成预签名 URL

#### 方法原型

```java
public URL generatePresignedUrl(String bucketName, String key, Date expirationDate, HttpMethodName method, Map<String, String> headers, Map<String, String> params) throws CosClientException
```

#### 请求示例

```java
// 调用 COS 接口之前必须保证本进程存在一个 COSClient 实例，如果没有则创建
// 详细代码参见本页：简单操作 -> 创建 COSClient
COSClient cosClient = createCOSClient();

// 存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式
String bucketName = "examplebucket-1250000000";
// 对象键(Key)是对象在存储桶中的唯一标识。详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324)
String key = "exampleobject";

// 设置签名过期时间(可选), 若未进行设置则默认使用 ClientConfig 中的签名过期时间(1小时)
// 这里设置签名在半个小时后过期
Date expirationDate = new Date(System.currentTimeMillis() + 30 * 60 * 1000);

// 填写本次请求的参数
Map<String, String> params = new HashMap<String, String>();
params.put("param1", "value1");

// 填写本次请求的头部
Map<String, String> headers = new HashMap<String, String>();
headers.put("header1", "value1");

// 请求的 HTTP 方法，上传请求用 PUT，下载请求用 GET，删除请求用 DELETE
HttpMethodName method = HttpMethodName.GET;

cosClient.generatePresignedUrl(bucketName, key, expirationDate, method, headers, params)

URL url = cosclient.generatePresignedUrl(req);
System.out.println(url.toString());

// 确认本进程不再使用 cosClient 实例之后，关闭之
cosClient.shutdown();
```

#### 参数说明

| 参数名称 | 描述         | 类型                        |
| -------- | ------------ | --------------------------- |
| method          | HTTP 方法，可选：GET、POST、PUT、DELETE、HEAD                | HttpMethodName          |
| bucketName      | 存储桶名称，存储桶的命名格式为 BucketName-APPID，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String |
| key             | 对象键（Key）是对象在存储桶中的唯一标识，详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324#.E5.AF.B9.E8.B1.A1.E9.94.AE) | String                  |
| expiration      | 签名过期的时间，可以设置任意一个未来的时间，不设置则默认是1小时之后过期              | Date                    |
| headers         | 签名头部   | Map<String, String> |
| params         | 签名参数   | Map<String, String> |

### 生成覆盖返回头部的预签名下载 URL

#### 方法原型

```java
public URL generatePresignedUrl(GeneratePresignedUrlRequest req) throws CosClientException
```

#### 请求示例

```java
// 调用 COS 接口之前必须保证本进程存在一个 COSClient 实例，如果没有则创建
// 详细代码参见本页：简单操作 -> 创建 COSClient
COSClient cosClient = createCOSClient();

// 存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式
String bucketName = "examplebucket-1250000000";
// 对象键(Key)是对象在存储桶中的唯一标识。详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324)
String key = "exampleobject";

GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);

// 设置下载时返回的 http 头
ResponseHeaderOverrides responseHeaders = new ResponseHeaderOverrides();
String responseContentType = "image/x-icon";
String responseContentLanguage = "zh-CN";
// 设置返回头部里包含文件名信息
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

// 填写本次请求的参数
req.addRequestParameter("param1", "value1");
// 填写本次请求的头部
// host 必填
req.putCustomRequestHeader(Headers.HOST, cosClient.getClientConfig().getEndpointBuilder().buildGeneralApiEndpoint(bucketName));
req.putCustomRequestHeader("header1", "value1");

URL url = cosclient.generatePresignedUrl(req);
System.out.println(url.toString());

// 确认本进程不再使用 cosClient 实例之后，关闭之
cosClient.shutdown();
```

#### 参数说明

| 参数名称 | 描述         | 类型                        |
| -------- | ------------ | --------------------------- |
| req      | 预签名请求类 | GeneratePresignedUrlRequest |

Request 成员说明：

| Request 成员    | 设置方法            | 描述                                                         | 类型                    |
| --------------- | ------------------- | ------------------------------------------------------------ | ----------------------- |
| method          | 构造函数或 set 方法 | HTTP 方法，可选：GET、POST、PUT、DELETE、HEAD                | HttpMethodName          |
| bucketName      | 构造函数或 set 方法 | 存储桶名称，存储桶的命名格式为 BucketName-APPID，详情请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | String |
| key             | 构造函数或 set 方法 | 对象键（Key）是对象在存储桶中的唯一标识，详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324#.E5.AF.B9.E8.B1.A1.E9.94.AE) | String                  |
| expiration      | set 方法            | 签名过期的时间，可以设置任意一个未来的时间，不设置则默认是1小时之后过期              | Date                    |
| contentType     | set 方法            | 要签名的请求中的 Content-Type                                | String                  |
| contentMd5      | set 方法            | 要签名的请求中的 Content-Md5                                 | String                  |
| responseHeaders | set 方法            | 签名的下载请求中要覆盖的返回的 HTTP 头                       | ResponseHeaderOverrides |
| versionId | set 方法            | 在存储桶开启多版本的时候，指定对象的版本号                       | String |

### 生成签名

构造 COS 请求的签名。推荐谁用临时密钥来生成签名。

#### 使用临时密钥（推荐）

```java
// 这里需要已经获取到临时密钥的结果。
// 临时密钥的生成参考 https://cloud.tencent.com/document/product/436/14048#cos-sts-sdk
String tmpSecretId = "TMPSECRETID";
String tmpSecretKey = "TMPSECRETKEY";
String sessionToken = "SESSIONTOKEN";

COSCredentials cred = new BasicSessionCredentials(tmpSecretId, tmpSecretKey, sessionToken);

// 存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式
String bucketName = "examplebucket-1250000000";
// 对象键(Key)是对象在存储桶中的唯一标识。详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324)
String key = "exampleobject";

ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));

// 用来生成签名
COSSigner signer = new COSSigner();
// 设置签名过期时间(可选)，若未进行设置，则默认使用 ClientConfig 中的签名过期时间(1小时)
// 这里设置签名在半个小时后过期
Date expirationDate = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);

// 填写本次请求的参数
Map<String, String> params = new HashMap<String, String>();
params.put("param1", "value1");

// 填写本次请求的头部
Map<String, String> headers = new HashMap<String, String>();
// host 必填
headers.put(Headers.HOST, clientConfig.getEndpointBuilder().buildGeneralApiEndpoint(bucketName))
headers.put("header1", "value1");

// 请求的 HTTP 方法，上传请求用 PUT，下载请求用 GET，删除请求用 DELETE
HttpMethodName method = HttpMethodName.GET;

String sign = signer.buildAuthorizationStr(method, key, headers, params, cred, expirationDate);
```

### 使用永久密钥

```java
// 设置用户身份信息。
// SECRETID 和 SECRETKEY 请登录访问管理控制台 https://console.cloud.tencent.com/cam/capi 进行查看和管理
String secretId = "SECRETID";
String secretKey = "SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);

// 存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式
String bucketName = "examplebucket-1250000000";
// 对象键(Key)是对象在存储桶中的唯一标识。详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324)
String key = "exampleobject";

ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));

// 用来生成签名
COSSigner signer = new COSSigner();
// 设置签名过期时间(可选)，若未进行设置，则默认使用 ClientConfig 中的签名过期时间(1小时)
// 这里设置签名在半个小时后过期
Date expirationDate = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);

// 填写本次请求的参数
Map<String, String> params = new HashMap<String, String>();
params.put("param1", "value1");

// 填写本次请求的头部
Map<String, String> headers = new HashMap<String, String>();
// host 必填
headers.put(Headers.HOST, clientConfig.getEndpointBuilder().buildGeneralApiEndpoint(bucketName))
headers.put("header1", "value1");

// 请求的 HTTP 方法，上传请求用 PUT，下载请求用 GET，删除请求用 DELETE
HttpMethodName method = HttpMethodName.GET;

String sign = signer.buildAuthorizationStr(method, key, headers, params, cred, expirationDate);
```