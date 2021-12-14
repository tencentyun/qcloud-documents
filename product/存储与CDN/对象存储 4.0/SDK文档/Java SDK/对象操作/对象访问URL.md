## 简介

本文档提供关于生成对象访问 URL 的示例代码。
这里生成的 URL 显示了对象存在 COS 的路径。

>? 如果您的文件是**私有读**权限，那么本接口生成的 URL 不能直接用于访问资源。
>

### 获取对象访问 URL

#### 方法原型

```java
public URL getObjectUrl(String bucketName, String key);
```

#### 请求示例

```java
// 不需要验证身份信息
COSCredentials cred = new AnonymousCOSCredentials();

// ClientConfig 中包含了后续请求 COS 的客户端设置：
ClientConfig clientConfig = new ClientConfig();

// 设置 bucket 的地域
// COS_REGION 请参照 https://cloud.tencent.com/document/product/436/6224
clientConfig.setRegion = new Region("COS_REGION");

// 设置生成的 url 的请求协议, http 或者 https
// 5.6.53 及更低的版本，建议设置使用 https 协议
// 5.6.54 及更高版本，默认使用了 https
clientConfig.setHttpProtocol(HttpProtocol.https);

// 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);

// 存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式
String bucketName = "examplebucket-1250000000";
// 对象键(Key)是对象在存储桶中的唯一标识。详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324)
String key = "exampleobject";

System.out.println(cosclient.getObjectUrl(bucketName, key));
```

#### 参数说明

| 参数名称   | 参数描述         |类型       | 是否必填         | 
| --------- | -------------- |---------- | ----------- |
| Bucket    | 存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
| Key       | 对象键（Key）是对象在存储桶中的唯一标识，详情请参见 [对象键](https://cloud.tencent.com/document/product/436/13324#.E5.AF.B9.E8.B1.A1.E9.94.AE) | String | 是 | 
