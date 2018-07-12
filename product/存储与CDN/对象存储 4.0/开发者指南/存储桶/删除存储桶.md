## 适用场景
当您在某些情况下需要删除存储桶时，您可以通过控制台、API 或 SDK 的方式来删除存储桶。

> **注意：**
> 目前仅支持删除已经清空的存储桶，如果存储桶中仍有对象，将会删除失败。请在执行删除存储桶前确保存储桶内已经没有对象。

当删除存储桶时，您需要确保操作的身份已被授权该操作，并确认传入了正确的存储桶名称（Bucket）和地域（Region）参数。

## 使用方法
### 使用对象存储控制台
您如需使用对象存储控制台删除存储桶，请参阅 [创建与删除](https://cloud.tencent.com/document/product/436/13309) 控制台指南文档。

### 使用 REST API
您可以直接使用 REST API 发起一个删除存储桶请求，可参考 [Delete Bucket 文档说明](https://cloud.tencent.com/document/product/436/7732)。

### 使用 C++ SDK

对象存储 COS 的 C++ SDK 中提供了此方法，可参考 [C++ SDK 接口文档 Delete Bucket 部分](https://cloud.tencent.com/document/product/436/12302#delete-bucket)。

#### 步骤说明

1. 传入配置文件路径初始化 CosConfig：初始化 CosAPI 对象。
2. 执行 DeleteBucket() 方法来删除一个存储桶，需要提供存储桶名称且确保存储桶为空。

#### 代码示例

下面的代码示例演示了如何删除存储桶：

``` cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";

// DeleteBucketReq的构造函数需要传入bucket_name
qcloud_cos::DeleteBucketReq req(bucket_name);
qcloud_cos::DeleteBucketResp resp;
qcloud_cos::CosResult result = cos.DeleteBucket(req, &resp);
```
### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档 Delete Bucket 部分](https://cloud.tencent.com/document/product/436/12263#delete-bucket)。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 执行 deleteBucket 删除 Bucket，Bucket 必须不包含任何数据，否则需要先清空数据。

#### 代码示例

调用 deleteBucket 创建 Bucket，代码示例如下所示：

```java
// 1 初始化用户身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);

// bucket名称需包含appid
String bucketName = "publicreadbucket-1251668577";
// 删除bucket, 只能删除不包含任何数据的bucket
cosclient.deleteBucket(bucketName);
```

### 使用 JavaScript SDK

对象存储 COS 的 JavaScript SDK 中提供了此方法，可参考 [JavaScript SDK 接口文档 Delete Bucket 部分](https://cloud.tencent.com/document/product/436/12260#delete-bucket)。

#### 步骤说明

1. 准备好签名服务器，提供 auth.php 接口给前端获取签名，可以参考 [后端签名例子](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/server) 。

2. 创建测试文件 test.html，写入如下代码，放到静态服务器下，用` http://127.0.0.1/test.html `访问。

#### 代码示例

下面的代码示例演示了如何删除存储桶：

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

cos.deleteBucket({
    Bucket: Bucket,
    Region: Region
}, function (err, data) {
    console.log(err || data);
});
</script>
```
### 使用 Node.js SDK

对象存储 COS 的 Node.js SDK 中提供了此方法，可参考 [Node.js SDK 接口文档 Delete Bucket 部分](https://cloud.tencent.com/document/product/436/12264#delete-bucket)。

#### 步骤说明

1. 安装 npm 依赖包：
```shell
npm i cos-nodejs-sdk-v5
```

2. 创建测试文件 test.js，并命令行执行 ```node test.js``` 。

#### 代码示例

下面的代码示例演示了如何删除存储桶：

```javascript
var COS = require('cos-nodejs-sdk-v5');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
cos.deleteBucket({
    Bucket: Bucket,
    Region: Region
}, function (err, data) {
    console.log(err || data);
});
```
### 使用 PHP SDK

对象存储 COS 的 PHP SDK 中提供了此方法，可参考 [PHP SDK 接口文档删除 Bucket 部分](https://cloud.tencent.com/document/product/436/12267#.E5.88.A0.E9.99.A4bucket)。

#### 步骤说明

1. 初始化客户端 cosClient。
2. 执行 deleteBucket  删除存储桶，需要提供存储桶名称。

#### 代码示例

以下代码演示了删除存储桶的步骤：

```php
try {
    $result = $cosClient->deleteBucket(array(
        'Bucket' => 'testbucket-125000000'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 使用 Python SDK

对象存储 COS 的 Python SDK 中提供了此方法，可参考 [Python SDK 接口文档删除 Bucket 部分](https://cloud.tencent.com/document/product/436/12270#.E5.88.A0.E9.99.A4-bucket)。

#### 步骤说明

1. 通过 CosConfig 类来配置，初始化客户端 CosS3Client。
2. 执行 delete_bucket() 方法来删除一个存储桶，需要提供存储桶名称且确保存储桶为空。

#### 代码示例

下面的代码示例演示了如何删除存储桶：

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
response = client.delete_bucket(
    Bucket=bucket    
)
```
