## 简介

本文档提供关于如何使用在上传对象时开启服务端加密。服务端加密的密钥分为两种：

* COS 托管加密密钥
* 客户提供的加密密钥

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API 参考](https://cos-android-sdk-doc-1253960454.file.myqcloud.com/)。

### 使用 COS 托管加密密钥的服务端加密（SSE-COS）保护数据

#### 功能说明

由腾讯云 COS 托管主密钥和管理数据。COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用 COS 主密钥对数据进行 AES-256 加密。

#### 示例代码一

[//]: # (.cssg-snippet-put-object-sse)
```java
PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, cosPath, srcPath);
// 设置使用 COS 托管加密密钥的服务端加密（SSE-COS）保护数据
putObjectRequest.setCOSServerSideEncryption();

// 上传文件
COSXMLUploadTask cosxmlUploadTask = transferManager.upload(putObjectRequest, uploadId);
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/Android/app/src/androidTest/java/com/tencent/qcloud/cosxml/cssg/PutObjectSSE.java) 查看。

#### 使用客户提供的加密密钥的服务端加密 （SSE-C）保护数据

#### 功能说明

加密密钥由用户自己提供，用户在上传对象时，COS 将使用用户提供的加密密钥对用户的数据进行 AES-256 加密。

> !
>- 该加密所运行的服务需要使用 HTTPS 请求。
>- 用户需要提供一个32字节的字符串作为密钥，支持数字、字母、字符的组合，不支持中文。
>- 如果上传文件时设置了密钥加密，那么在使用 GET（下载）、HEAD（查询）源对象时也需要在请求中带上相同的密钥，才能正常响应。

#### 示例代码二

[//]: # (.cssg-snippet-put-object-sse-c)
```java
// 服务端加密密钥
String customKey = "服务端加密密钥";
PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, cosPath, srcPath);
// 设置使用客户提供的加密密钥的服务端加密 （SSE-C）保护数据
try {
    putObjectRequest.setCOSServerSideEncryptionWithCustomerKey(customKey);
} catch (CosXmlClientException e) {
    e.printStackTrace();
}

// 上传文件
COSXMLUploadTask cosxmlUploadTask = transferManager.upload(putObjectRequest, uploadId);
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/Android/app/src/androidTest/java/com/tencent/qcloud/cosxml/cssg/PutObjectSSE.java) 查看。