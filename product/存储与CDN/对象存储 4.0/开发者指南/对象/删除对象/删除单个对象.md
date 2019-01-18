## 适用场景

腾讯云 COS 支持直接删除一个或多个对象，当仅需要删除一个对象时，您只需要提供对象的名称（即对象键），就可以调用一个 API 请求来删除它。

## 使用方法

### 使用对象存储控制台
您可以使用对象存储控制台批量删除多个对象，请参阅 [删除对象](https://cloud.tencent.com/document/product/436/13323) 控制台指南文档。

### 使用 REST API

您可以直接使用 REST API 发起一个获取对象请求，可参考 [DELETE Object ](https://cloud.tencent.com/document/product/436/7743) 文档。

### 使用 C++ SDK

对象存储 COS 的 C++ SDK 中提供了此方法，可参考 [C++ SDK 接口文档 Delete Object 部分](https://cloud.tencent.com/document/product/436/12302#delete-object)。

#### 步骤说明

1. 传入配置文件路径初始化 CosConfig，初始化 CosAPI 对象。
2. 执行 DeleteObject() 方法来删除单个对象，需要提供存储桶名称和对象键名称。

#### 代码示例

下列的代码示例演示了如何删除单个对象：

``` cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";
std::string object_name = "test_object";

qcloud_cos::DeleteObjectReq req(bucket_name, object_name);
qcloud_cos::DeleteObjectResp resp;
qcloud_cos::CosResult result = cos.DeleteObject(req, &resp);
```

如果开启了多版本，可以通过指定参数 VersionId 来删除指定版本的对象：
``` cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";
std::string object_name = "test_object";

qcloud_cos::DeleteObjectReq req(bucket_name, object_name);
req.SetXCosVersionId("12345");
qcloud_cos::DeleteObjectResp resp;
qcloud_cos::CosResult result = cos.DeleteObject(req, &resp);
```
### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档 Delete Object 部分](https://cloud.tencent.com/document/product/436/12263#delete-object)。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 执行 deleteObject 方法删除对象，传入 bucketName 和要删除的 key。

#### 代码示例

  调用 deleteObject 创建 object，代码示例如下所示：

```java
// 1 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket名需包含appid
String bucketName = "mybucket-1251668577";
String key = "aaa/bbb.txt";
try {
    cosclient.deleteObject(bucketName, key);
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}

// 关闭客户端
cosclient.shutdown();
```
### 使用 JavaScript SDK

对象存储 COS 的 JavaScript SDK 中提供了此方法，可参考 [JavaScript SDK 接口文档 Delete Object 部分](https://cloud.tencent.com/document/product/436/12260#delete-object)。

#### 步骤说明

1. 准备好签名服务器，提供 auth.php 接口给前端获取签名，可以参考 [后端签名例子](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/server) 。

2. 创建测试文件 test.html，写入如下代码，放到静态服务器下，用` http://127.0.0.1/test.html `访问。

#### 代码示例

下列的代码示例演示了如何删除单个对象：

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

cos.deleteObject({
    Bucket: Bucket,
    Region: Region
}, function (err, data) {
    console.log(err || data);
});
</script>
```
### 使用 Node.js SDK

对象存储 COS 的 Node.js SDK 中提供了此方法，可参考 [Node.js SDK 接口文档 Delete Object 部分](https://cloud.tencent.com/document/product/436/12264#delete-object) 。

#### 步骤说明

1. 安装 npm 依赖包：
```shell
npm i cos-nodejs-sdk-v5
```

2. 创建测试文件 test.js，并命令行执行 ```node test.js``` 。

#### 代码示例

下列的代码示例演示了如何删除单个对象：

```javascript
var COS = require('cos-nodejs-sdk-v5');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
cos.deleteObject({
    Bucket: Bucket,
    Region: Region,
    Key: '1.jpg'
}, function (err, data) {
    console.log(err || data);
});
```
### 使用 PHP SDK

对象存储 COS 的 PHP SDK 中提供了此方法，可参考 [PHP SDK 接口文档删除文件部分](https://cloud.tencent.com/document/product/436/12267#.E5.88.A0.E9.99.A4.E6.96.87.E4.BB.B6)。

#### 步骤说明

1. 初始化客户端 cosClient。
2. 执行 deleteObject 删除单个对象，需要提供存储桶名称和对象键名称。

#### 代码示例

下列的代码示例演示了如何删除单个对象：

```php
try {
    $result = $cosClient->deleteObject(array(
        'Bucket' => 'bucket-125000000',
        'Key' => 'hello.txt'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 使用 Python SDK

对象存储 COS 的 Python SDK 中提供了此方法，可参考 [Python SDK 接口文档文件删除部分](https://cloud.tencent.com/document/product/436/12270#.E6.96.87.E4.BB.B6.E4.B8.8B.E8.BD.BD)。

#### 步骤说明

1. 通过 CosConfig 类来配置，初始化客户端 CosS3Client。
2. 执行 delete_object() 方法来删除单个对象，需要提供存储桶名称和对象键名称。

#### 代码示例

下列的代码示例演示了如何删除单个对象：

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
response = client.delete_object(
    Bucket=bucket,
    Key=file_name      
)
```

如果开启了多版本，可以通过指定参数 VersionId 来删除指定版本的对象：
```python
bucket = 'testbucket-123456789'
file_name = 'test.txt'
response = client.delete_object(
    Bucket=bucket,
    Key=file_name,
    VersionId='MTg0NDY3NDI1NjExNjQwNDUxMzU'    
)
```
