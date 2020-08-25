
如果需要对上传的对象进行加密，我们支持以下加密方式。

#### 使用 COS 托管加密密钥的服务端加密（SSE-COS）保护数据

由腾讯云 COS 托管主密钥和管理数据。COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用 COS 主密钥对数据进行 AES-256 加密。

SDK 通过调用 `setServerSideEncryption`和`setMetadata`等方法来完成，示例如下：

[//]: # (.cssg-snippet-put-object-sse)
```java
 // 初始化用户身份信息(secretId, secretKey)
 COSCredentials cred = new BasicCOSCredentials("COS_SECRETID", "COS_SECRETKEY");
 // 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
 ClientConfig clientConfig = new ClientConfig(new Region("ap-guangzhou"));
// 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket名需包含appid
String bucketName = "examplebucket-1250000000";

String key = "aaa/bbb.txt";
File localFile = new File("test.txt");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
ObjectMetadata objectMetadata = new ObjectMetadata();
// 设置加密算法为AES256
objectMetadata.setServerSideEncryption(SSEAlgorithm.AES256.getAlgorithm());
putObjectRequest.setMetadata(objectMetadata);
try {
    PutObjectResult putObjectResult = cosclient.putObject(putObjectRequest);
    // putobjectResult会返回文件的etag, 该md5值根据s3语义不是对象的md5，只是唯一性标志
    String etag = putObjectResult.getETag();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}
// 关闭客户端
cosclient.shutdown();
```

#### 使用客户提供的加密密钥的服务端加密 （SSE-C）保护数据

加密密钥由用户自己提供，用户在上传对象时，COS 将使用用户提供的加密密钥对用户的数据进行 AES-256 加密。SDK 通过调用`setHttpProtocol`和 `setSSECustomerKey` 等方法来完成。

> !
>- 该加密所运行的服务需要使用 HTTPS 请求。
>- base64EncodedKey：用户提供的服务端加密密钥的 Base64 编码。
>- 如果上传的源文件调用了该方法，那么在使用 GET（下载）、HEAD（查询）时对源对象操作的时候也要调用该方法。

[//]: # (.cssg-snippet-put-object-sse-c)
```java
 // 初始化用户身份信息(secretId, secretKey)
 COSCredentials cred = new BasicCOSCredentials("COS_SECRETID", "COS_SECRETKEY");
 // 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
 ClientConfig clientConfig = new ClientConfig(new Region("ap-guangzhou"));
// 要求https协议
clientConfig.setHttpProtocol(HttpProtocol.https);
// 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket名需包含appid
String bucketName = "examplebucket-1250000000";

String key = "aaa/bbb.txt";
File localFile = new File("test.txt");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
String base64EncodedKey = "MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=";
// sseCustomerKey是base64编码的密钥
SSECustomerKey sseCustomerKey = new SSECustomerKey(base64EncodedKey);
putObjectRequest.setSSECustomerKey(sseCustomerKey);
ObjectMetadata objectMetadata = cosclient.getObjectMetadata();
objectMetadata.getHttpExpiresDate();
try {
PutObjectResult putObjectResult = cosclient.putObject(putObjectRequest);
// putobjectResult会返回文件的etag, 该md5值根据s3语义不是对象的md5，只是唯一性标志
String etag = putObjectResult.getETag();
} catch (CosServiceException e) {
e.printStackTrace();
} catch (CosClientException e) {
e.printStackTrace();
}
// 关闭客户端
cosclient.shutdown();
```
