## 适用场景

您可以在 COS 中将已存储的对象通过简单的复制操作，创建一个新的对象副本。在单个操作中，您可以复制最大 5 GB 的对象；当对象超过 5 GB 时，您必须使用分块上传的接口来实现复制。复制对象有以下功能：

- 创建一个新的对象副本。
- 复制对象并更名，删除原始对象，实现重命名。
- 修改对象的存储类型，在复制时选择相同的源和目标对象键，修改存储类型。
- 在不同的腾讯云 COS 地域复制对象。
- 修改对象的元数据，在复制时选择相同的源和目标对象键，并修改其中的元数据。

复制对象时，默认将继承原对象的元数据，但创建日期将会按新对象的时间计算。

## 使用方法

### 使用 REST API

您可以直接使用 REST API 发起一个复制对象请求，可参考 [Put Object Copy 文档说明](https://cloud.tencent.com/document/product/436/10881)。

### 使用 C++ SDK

对象存储 COS 的 C++ SDK 中提供了此方法，可参考 [C++ SDK 接口文档 Put Object Copy 部分](https://cloud.tencent.com/document/product/436/12302#put-object-copy)。

#### 步骤说明

1. 传入配置文件路径初始化 CosConfig，初始化 CosAPI 对象。
2. 执行 PutObjectCopy() 方法来复制对象，PutObjectReq 需要提供存储桶名称和对象键名称以及拷贝源存储桶、源对象键、源地域。

#### 代码示例

下列的代码示例演示了如何简单复制对象：

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";
std::string object_name = "sevenyou";

qcloud_cos::PutObjectCopyReq req(bucket_name, object_name);
req.SetXCosCopySource("sevenyousouthtest-12345656.cn-south.myqcloud.com/sevenyou_source_obj");
qcloud_cos::PutObjectCopyResp resp;
qcloud_cos::CosResult result = cos.PutObjectCopy(req, &resp);
```
### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档 Put Object Copy 部分](https://cloud.tencent.com/document/product/436/12263#put-object-copy)。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 使用 copyObject 接口来完成 copy。

#### 代码示例

`CopyObjectRequest`包含了 copy 对象的请求，通过设置源文件所在的园区，bucket 名称，路径以及目的文件的园区，bucket名称，路径。下列的代码示例演示了如何简单复制对象：

```java
// 1 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// 要拷贝的bucket region, 支持跨园区拷贝
Region srcBucketRegion = new Region("ap-shanghai");
// 源bucket, bucket名需包含appid
String srcBucketName = "srcBucket-1251668577";
// 要拷贝的源文件
String srcKey = "aaa/bbb.txt";
// 目的bucket, bucket名需包含appid
String destBucketName = "destBucket-1251668577";
// 要拷贝的目的文件
String destKey = "ccc/ddd.txt";

CopyObjectRequest copyObjectRequest = new CopyObjectRequest(srcBucketRegion, srcBucketName,
        srcKey, destBucketName, destKey);
try {
    CopyObjectResult copyObjectResult = cosclient.copyObject(copyObjectRequest);
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}
cosclient.shutdown();
```

### 使用 JavaScript SDK

对象存储 COS 的 JavaScript SDK 中提供了此方法，可参考 [JavaScript SDK 接口文档](https://cloud.tencent.com/document/product/436/12260#put-object-copy) Put Object Copy 部分。

#### 步骤说明

1. 准备好签名服务器，提供 auth.php 接口给前端获取签名，可以参考 [后端签名例子](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/server) 。

2. 创建测试文件 test.html，写入如下代码，放到静态服务器下，用` http://127.0.0.1/test.html `访问。

#### 代码示例

下列的代码示例演示了如何简单复制对象：

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

cos.putObjectCopy({
    Bucket: Bucket,
    Region: Region,
    Key: '1.new.jpg',
    CopySource: 'test-1250000000.cos.ap-guangzhou.myqcloud.com/1.jpg'
}, function (err, data) {
    console.log(err || data);
});
</script>
```
### 使用 Node.js SDK

#### 步骤说明

1. 安装 npm 依赖包：
```shell
npm i cos-nodejs-sdk-v5
```

2. 创建测试文件 test.js，并命令行执行`node test.js`。

#### 代码示例

下列的代码示例演示了如何复制对象：

```javascript
var COS = require('cos-nodejs-sdk-v5');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
cos.putObjectCopy({
    Bucket: Bucket,
    Region: Region,
    Key: '1.new.jpg',
    CopySource: 'test-1250000000.cos.ap-guangzhou.myqcloud.com/1.jpg'
}, function (err, data) {
    console.log(err || data);
});
```
### 使用 PHP SDK

对象存储 COS 的 PHP SDK 中提供了此方法，可参考 [PHP SDK 接口文档复制对象部分](https://cloud.tencent.com/document/product/436/12267#.E5.A4.8D.E5.88.B6.E5.AF.B9.E8.B1.A1)。

#### 步骤说明

1. 初始化客户端 cosClient。
2. 执行 Copy 分块复制对象，需要提供存储桶名称和对象键名称。

#### 代码示例

下列的代码示例演示了如何简单复制对象：
```php
try {
    $result = $cosClient->copyObject(array(
        'Bucket' => 'bucket-125000000',
        'CopySource' => 'bucket-appid.region.myqcloud.com/cos_path',
        'Key' => 'string',
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 使用 Python SDK

对象存储 COS 的 Python SDK 中提供了此方法，可参考 [Python SDK 接口文档文件拷贝部分](https://cloud.tencent.com/document/product/436/12270#.E6.96.87.E4.BB.B6.E6.8B.B7.E8.B4.9D)。

#### 步骤说明

1. 通过 CosConfig 类来配置，初始化客户端 CosS3Client。
2. 执行 copy_object() 方法来复制对象，需要提供存储桶名称和对象键名称以及拷贝源存储桶、源对象键、源地域。

#### 代码示例

下列的代码示例演示了如何简单复制对象：

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
response = client.copy_object(
    Bucket=bucket,
    Key=file_name,
    CopySource={
        'Bucket': 'test-121212121',
        'Key': '1MB.txt',
        'Region': 'ap-guangzhou'
    }      
)
```
