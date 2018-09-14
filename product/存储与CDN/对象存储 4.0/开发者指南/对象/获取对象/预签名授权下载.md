## 适用场景

在默认情况下，存储桶和对象都是私有的。如果您希望第三方可以下载对象，又不希望对方使用 CAM 账户或临时密钥等方式时，您可以使用预签名 URL 的方式将签名提交给第三方，以供完成下载操作。收到有效预签名 URL 的任何人都可以下载对象。

预签名 URL 时，您可以在签名中设置将对象键包含在签名中，只许可下载指定的对象。您也可以在程序中指定预签名 URL 的有效时间，以保证超时后该 URL 不会被未授权方使用。

## 使用方法

### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档生成预签名链接部分](https://cloud.tencent.com/document/product/436/12263#.E7.94.9F.E6.88.90.E9.A2.84.E7.AD.BE.E5.90.8D.E9.93.BE.E6.8E.A5)。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 执行 generatePresignedUrl 方法获取下载签名，下载传入 http 方法为 GET。

#### 代码示例

（1）以下代码演示了生成预签名的下载链接：

```java
// 1 初始化用户身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// 设置bucket名, bucket名需包含appid
String bucketName = "mybucket-125110000";
String key = "aaa.txt";

GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
// 设置签名过期时间(可选), 过期时间不做限制，只需比当前时间大, 若未进行设置, 则默认使用ClientConfig中的签名过期时间(5分钟)
// 这里设置签名在半个小时后过期
Date expirationDate = new Date(System.currentTimeMillis() + 30 * 60 * 1000);
req.setExpiration(expirationDate);

URL url = cosclient.generatePresignedUrl(req);
System.out.println(url.toString());
```

（2）`GeneratePresignedUrlRequest` 支持设置下载时返回的http头，比如 content-type, content-disposition 等，示例代码如下：

```java
// 1 初始化用户身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// 设置bucket名, bucket名需包含appid
String bucketName = "mybucket-125110000";
String key = "aaa.txt";

GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
// 设置下载时返回的http头
ResponseHeaderOverrides responseHeaders = new ResponseHeaderOverrides();
String responseContentType = "image/x-icon";
String responseContentLanguage = "zh-CN";
String responseContentDispositon = "filename=\"abc.txt\"";
String responseCacheControl = "no-cache";
String expireStr =
        DateUtils.formatRFC822Date(new Date(System.currentTimeMillis() + 24 * 3600 * 1000));
responseHeaders.setContentType(responseContentType);
responseHeaders.setContentLanguage(responseContentLanguage);
responseHeaders.setContentDisposition(responseContentDispositon);
responseHeaders.setCacheControl(responseCacheControl);
responseHeaders.setExpires(expireStr);
req.setResponseHeaders(responseHeaders);
URL url = cosclient.generatePresignedUrl(req);

System.out.println(url.toString());
```

（3）`GeneratePresignedUrlRequest` 同时支持生成匿名 bucket 的下载链接，匿名 bucket 下载链接无需包含签名，因此无需传入密钥信息。示例代码如下：

```java
// 1 对于匿名bucket, 无需传入身份信息
COSCredentials cred = new AnonymousCOSCredentials();
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// 设置bucket名, bucket名需包含appid
String bucketName = "mybucket-125110000";
String key = "aaa.txt";

GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
URL url = cosclient.generatePresignedUrl(req);

System.out.println(url.toString());
```

### 使用 JavaScript SDK

#### 步骤说明

1. 准备好签名服务器，提供 auth.php 接口给前端获取签名，可以参考 [后端签名例子](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/server) 。

2. 创建测试文件 test.html，写入如下代码，放到静态服务器下，用` http://127.0.0.1/test.html `访问。

#### 代码示例

下列的代码示例演示了如何预签名授权下载：

```html
<script src="cos-js-sdk-v5.min.js"></script>
<script>
var Bucket = 'test-1250000000'; // 替换成用户的 Bucket
var Region = 'ap-guangzhou';    // 替换成用户的 Region

// 初始化实例
var cos = new COS({
    getAuthorization: function (options, callback) {
        // 异步获取签名
        var url = 'auth.php?method=' + options.Method.toLowerCase() + '&pathname=' + encodeURIComponent('/' + (options.Key || ''));
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onload = function (e) {
            callback(e.target.responseText);
        };
        xhr.send();
    }
});

cos.getObjectUrl({
    Bucket: Bucket,
    Region: Region,
    Key: '1.jpg', // 替换要下载的文件路径
    Expires: 60
}, function (err, data) {
    console.log(err || data.Url);
});
</script>
```

### 使用 Node.js SDK

#### 步骤说明

1. 安装 npm 依赖包：
```shell
npm i cos-nodejs-sdk-v5
```

2. 创建测试文件 test.js，并命令行执行 ```node test.js``` 。

#### 代码示例

下列的代码示例演示了如何预签名授权下载：

```javascript
var COS = require('cos-nodejs-sdk-v5');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
var url = cos.getObjectUrl({
    Bucket: Bucket,
    Region: Region,
    Key: '1.jpg', // 替换要下载的文件路径
    Expires: 60
});
console.log(url);
```
### 使用 Python SDK

#### 步骤说明

1. 通过 CosConfig 类来配置，初始化客户端 CosS3Client。
2. 执行 get_presigned_download_url() 方法获取预签名下载对象，需要提供存储桶名称和对象键名称。

#### 代码示例

下列的代码示例演示了如何预签名授权下载：

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'xxxxxxxx'      # 替换为用户的 secretId
secret_key = 'xxxxxxx'      # 替换为用户的 secretKey
region = 'ap-beijing-1'     # 替换为用户的 Region
token = ''                  # 使用临时密钥需要传入 Token，默认为空，可不填

config = CosConfig(Secret_id=secret_id, Secret_key=secret_key, Region=region, Token=token)
client = CosS3Client(config)

bucket = 'testbucket-123456789'
file_name = 'test.txt'
download_url = client.get_presigned_download_url(
    Bucket=bucket,
    Key=file_name,
)
print download_url
```
