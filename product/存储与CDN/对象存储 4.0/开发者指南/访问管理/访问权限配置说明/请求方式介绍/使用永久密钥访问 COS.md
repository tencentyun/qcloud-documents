## 背景介绍

通过 RESTful API 对对象存储（Cloud Object Storage，COS）可以发起 HTTP 匿名请求或 HTTP 签名请求。匿名请求一般用于需要公开访问的场景，例如托管静态网站；此外，绝大部分场景都需要通过签名请求完成。

签名请求相比匿名请求，多携带了一个签名值，签名是基于密钥（SecretId/SecretKey）和请求信息加密生成的字符串。SDK 会自动计算签名，您只需要在初始化用户信息时设置好密钥，无需关心签名的计算；对于通过 RESTful API 发起的请求，需要按照签名算法计算签名并添加到请求中。

## 获取永久密钥

您可以在访问管理控制台中的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取永久密钥，永久密钥包括 SecretId 和 SecretKey，代表了账号的永久身份，不会过期。
- SecretId：用于标识 API 调用者身份。
- SecretKey：用于加密签名字符串和服务端验证签名字符串的密钥。
![](https://qcloudimg.tencent-cloud.cn/raw/d00f0767b6423ea150cfbc54e421c345.png)

## 使用永久密钥访问 COS

### 通过 API 请求访问 COS

在使用 API 请求时，对于私有桶您必须使用签名请求。通过永久密钥生成签名，放入 Authorization 头部中，形成签名请求；请求发送到 COS，COS 会验证签名与请求是否一致。

>? 由于签名生成算法较为复杂，建议您直接使用 SDK 发起请求省略这一环节。
>

1. 通过永久密钥生成签名
签名算法的介绍可参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档，COS 同时提供了 [签名生成工具](https://cos5.cloud.tencent.com/static/cos-sign/)，也可以通过 SDK 生成签名，参考 [SDK 签名实现](https://cloud.tencent.com/document/product/436/7778#sdk-.E7.AD.BE.E5.90.8D.E5.AE.9E.E7.8E.B0)；您也可以自行编写程序生成签名，但签名算法较为复杂，一般不推荐这种方式。
2. 填入 Authorization 头部
发起 API 请求时，将签名填入标准 Http Authorization 头部，以下为 GetObject 请求的示例：
```
GET /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: q-sign-algorithm=sha1&q-ak=SecretId&q-sign-time=KeyTime&q-key-time=KeyTime&q-header-list=HeaderList&q-url-param-list=UrlParamList&q-signature=Signature
```

### 通过 SDK 工具访问 COS

1. 通过永久密钥初始化身份信息
安装 SDK 工具完成后，首先需要初始化用户身份信息，写入主账号或子账号的永久密钥（SecretId 和 SecretKey）。
2. 直接使用 SDK 请求 COS
初始化之后，您可以直接使用 SDK 工具进行上传、下载等基本操作，而无需像 API 请求一样自行生成签名，因为 SDK 工具代替您通过密钥生成了签名，向 COS 发起请求。

例如，如下 Java SDK 的代码，更多语言 demo 可参考 [SDK 概览](https://cloud.tencent.com/document/product/436/6474) 的快速入门文档。
```
// 1 初始化用户身份信息（secretId, secretKey）。
// SECRETID和SECRETKEY请登录访问管理控制台 https://console.cloud.tencent.com/cam/capi 进行查看和管理
String secretId = "SECRETID";
String secretKey = "SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
// 2 设置 bucket 的地域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
// clientConfig 中包含了设置 region, https(默认 http), 超时, 代理等 set 方法, 使用可参见源码或者常见问题 Java SDK 部分。
Region region = new Region("COS_REGION");
ClientConfig clientConfig = new ClientConfig(region);
// 这里建议设置使用 https 协议
// 从 5.6.54 版本开始，默认使用了 https
clientConfig.setHttpProtocol(HttpProtocol.https);
// 3 生成 cos 客户端。
COSClient cosClient = new COSClient(cred, clientConfig);

```


