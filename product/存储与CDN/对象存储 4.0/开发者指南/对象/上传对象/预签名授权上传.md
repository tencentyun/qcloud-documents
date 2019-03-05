## 适用场景

在默认情况下，存储桶和对象都是私有的。如果您希望第三方可以上传对象到存储桶，又不希望对方使用 CAM 账户或临时密钥等方式时，您可以使用预签名 URL 的方式将签名提交给第三方，以供完成临时的上传操作。收到有效预签名 URL 的任何人都可以上传对象。

预签名 URL 时，您可以在签名中设置将对象键包含在签名中，只许可上传指定路径。您还可以指定 HTTP 的请求方法，限制具体的对象操作，例如：上传、下载、删除等。您也可以在程序中指定预签名 URL 的有效时间，以保证超时后该 URL 不会被未授权方使用。

## 使用方法

### 使用 REST API

您可以直接使用 REST API 发起一个获取对象请求，可参考 [GET Object 文档说明](https://cloud.tencent.com/document/product/436/7753)。

### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档生成预签名链接部分](https://cloud.tencent.com/document/product/436/12263#.E7.94.9F.E6.88.90.E9.A2.84.E7.AD.BE.E5.90.8D.E9.93.BE.E6.8E.A5)。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 执行 generatePresignedUrl 方法获取上传签名，并传入 http 方法参数为 PUT。

#### 代码示例

以下代码示例演示了生成预签名的上传链接，并用其进行上传：

```java
// 1 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成 cos 客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket名需包含appid
String bucketName = "mybucket-1251668577";

String key = "aaa.txt";
Date expirationTime = new Date(System.currentTimeMillis() + 30 * 60 * 1000);
// 生成预签名上传 URL
URL url = cosclient.generatePresignedUrl(bucketName, key, expirationTime, HttpMethodName.PUT);

// 使用预签名的 URL 上传文件
try {
    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    connection.setDoOutput(true);
    connection.setRequestMethod("PUT");
    OutputStreamWriter out = new OutputStreamWriter(connection.getOutputStream());
    // 写入要上传的数据 
    out.write("This text uploaded as object.");
    out.close();
    int responseCode = connection.getResponseCode();
    System.out.println("Service returned response code " + responseCode);
} catch (ProtocolException e) {
    e.printStackTrace();
} catch (IOException e) {
    e.printStackTrace();
}

cosclient.shutdown();
```

### 使用 Node.js SDK

#### 步骤说明

1. 安装 npm 依赖包：
```shell
npm i cos-nodejs-sdk-v5
```

2. 创建测试文件 test.js，并命令行执行 ```node test.js``` 。

#### 代码示例

```javascript
var COS = require('cos-nodejs-sdk-v5');
var request = require('request');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
var url = cos.getObjectUrl({
    Bucket: Bucket,
    Region: Region,
    Method: 'PUT',
    Key: '1.jpg', // 替换要下载的文件路径
    Expires: 60
});
console.log(url);

// 自行上传文件
request({
    method: 'PUT',
    url: url,
    body: fs.readFileSync('./1.jpg'),
}, function (err, response, body) {
    console.log(response.statusCode);
    console.log(response.headers.etag);
    console.log(body);
});
```
