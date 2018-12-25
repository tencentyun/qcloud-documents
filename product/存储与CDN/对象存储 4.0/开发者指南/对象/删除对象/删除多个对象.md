## 适用场景

腾讯云 COS 支持批量删除多个对象。您可以通过控制台、 API、SDK 等多种方式批量删除对象。

默认情况下，当删除任务都成功完成时，返回的内容通常为空。若有发生错误，则会返回错误信息。

>注意：单次请求最多可删除 1000 个对象，若需要删除更多对象，请将列表拆分后分别发送请求。

## 使用方法

### 使用对象存储控制台
您可以使用对象存储控制台批量删除多个对象，请参阅 [删除对象](https://cloud.tencent.com/document/product/436/13323) 控制台指南文档。

### 使用 REST API

您可以直接使用 REST API 发起一个获取对象请求，请查阅 [Delete Multiple Object ](https://cloud.tencent.com/document/product/436/8289) 文档。

### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档 Delete Object 部分](https://cloud.tencent.com/document/product/436/12263#delete-object)。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 执行 deleteObjects 方法删除对象，需提供要删除的对象键名称。
3. 执行成功会返回 DeleteObjectsResult 对象，包含所有已删除的对象键。如果部分成功部分失败（如对该对象没有删除权限），则返回 MultiObjectDeleteException 类。其他失败导致的异常返回异常类（CosClientException/CosServiceException），请参照 SDK 异常类说明。

#### 代码示例

（1）以下代码演示了删除多个对象（无多版本）的示例代码：

```java
// 1 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket名需包含appid
String bucketName = "mybucket-1251668577";

DeleteObjectsRequest deleteObjectsRequest = new DeleteObjectsRequest(bucketName);
// 设置要删除的key列表, 最多一次删除1000个
ArrayList<KeyVersion> keyList = new ArrayList<>();
// 传入要删除的文件名
keyList.add(new KeyVersion("aaa.txt"));
keyList.add(new KeyVersion("bbb.mp4"));
keyList.add(new KeyVersion("ccc/ddd.jpg"));
deleteObjectsRequest.setKeys(keyList);

// 批量删除文件
try {
    DeleteObjectsResult deleteObjectsResult = cosclient.deleteObjects(deleteObjectsRequest);
    List<DeletedObject> deleteObjectResultArray = deleteObjectsResult.getDeletedObjects();
} catch (MultiObjectDeleteException mde) { // 如果部分产出成功部分失败, 返回MultiObjectDeleteException
    List<DeletedObject> deleteObjects = mde.getDeletedObjects();
    List<DeleteError> deleteErrors = mde.getErrors();
} catch (CosServiceException e) { // 如果是其他错误, 比如参数错误， 身份验证不过等会抛出CosServiceException
    e.printStackTrace();
} catch (CosClientException e) { // 如果是客户端错误，比如连接不上COS
    e.printStackTrace();
}
```

（2）以下代码演示了删除多个对象（含有多版本）的示例代码：

```java
// 1 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket名需包含appid
String bucketName = "mybucket-1251668577";

DeleteObjectsRequest deleteObjectsRequest = new DeleteObjectsRequest(bucketName);
// 设置要删除的key列表, 最多一次删除1000个
ArrayList<KeyVersion> keyList = new ArrayList<>();
// 传入要删除的文件名
keyList.add(new KeyVersion("aaa.txt", "axbefagagaxxfafa"));
keyList.add(new KeyVersion("bbb.mp4", "awcafa1faxg0lx"));
keyList.add(new KeyVersion("ccc/ddd.jpg", "kafa1kxxaa2ymh"));
deleteObjectsRequest.setKeys(keyList);

// 批量删除文件
try {
    DeleteObjectsResult deleteObjectsResult = cosclient.deleteObjects(deleteObjectsRequest);
    List<DeletedObject> deleteObjectResultArray = deleteObjectsResult.getDeletedObjects();
} catch (MultiObjectDeleteException mde) { // 如果部分产出成功部分失败, 返回MultiObjectDeleteException
    List<DeletedObject> deleteObjects = mde.getDeletedObjects();
    List<DeleteError> deleteErrors = mde.getErrors();
} catch (CosServiceException e) { // 如果是其他错误, 比如参数错误， 身份验证不过等会抛出CosServiceException
    e.printStackTrace();
} catch (CosClientException e) { // 如果是客户端错误，比如连接不上COS
    e.printStackTrace();
}
```



### 使用 JavaScript SDK

对象存储 COS 的 JavaScript SDK 中提供了此方法，可参考  [JavaScript SDK 接口文档 Delete Object 部分](https://cloud.tencent.com/document/product/436/12260#delete-object)。

#### 步骤说明

1. 准备好签名服务器，提供 auth.php 接口给前端获取签名，可以参考 [后端签名例子](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/server) 。

2. 创建测试文件 test.html，写入如下代码，放到静态服务器下，用` http://127.0.0.1/test.html `访问。

#### 代码示例

下列的代码示例演示了如何删除多个对象：

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

cos.deleteMultipleObject({
    Bucket: Bucket,
    Region: Region,
    Objects: [
        {Key: '1mb.zip'},
        {Key: '3mb.zip'},
    ]
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

下列的代码示例演示了如何删除多个对象：

```javascript
var COS = require('cos-nodejs-sdk-v5');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
cos.deleteMultipleObject({
    Bucket: Bucket,
    Region: Region,
    Objects: [
        {Key: '1mb.zip'},
        {Key: '3mb.zip'},
    ]
}, function (err, data) {
    console.log(err || data);
});
```
### 使用 PHP SDK

对象存储 COS 的 PHP SDK 中提供了此方法，可参考 PHP SDK 接口文档  [PHP SDK 接口文档删除文件部分](https://cloud.tencent.com/document/product/436/12267#.E5.88.A0.E9.99.A4.E6.96.87.E4.BB.B6)。

#### 步骤说明

1. 初始化客户端 cosClient。
2. 执行 deleteObjects 删除多个对象，需要提供存储桶名称和对象键名称。

#### 代码示例

下列的代码示例演示了如何删除多个对象：

```php
try {
    $result = $cosClient->deleteObjects(array(
        'Bucket' => 'bucket-125000000',
        'Objects' => array(
            array(
                'Key' => 'string',
            ),
            // ... repeated
        ),
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 使用 Python SDK

对象存储 COS 的 Python SDK 中提供了此方法，可参考 [Python SDK 接口文档文件删除部分](https://cloud.tencent.com/document/product/436/12270#.E6.96.87.E4.BB.B6.E4.B8.8B.E8.BD.BD)。

#### 步骤说明

1. 通过 CosConfig 类来配置，初始化客户端 CosS3Client。
2. 执行 delete_objects() 方法来删除多个对象，需要提供存储桶名称和多个对象键名称。

#### 代码示例

下列的代码示例演示了如何删除多个对象：

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
response = client.delete_objects(
    Bucket=bucket,
    Delete={
        "Quiet": "true",
        "Object": [
            {
                "Key": "test1.txt"
            },
            {
                "Key": "test2.txt"
            }
        ]
    }    
)
```

如果开启了多版本，可以通过指定参数 VersionId 来删除指定版本的对象：
```python
bucket = 'testbucket-123456789'
response = client.delete_objects(
    Bucket=bucket,
    Delete={
        "Quiet": "true",
        "Object": [
            {
                "Key": "test1.txt",
                "VersionId": "MTg0NDY3NDI1NjExNjQwNDUxMzU"
            },
            {
                "Key": "test2.txt",
                "VersionId": "MTg0NDY3NDI1NjExNjQwNDUxMzA"
            }
        ]
    }    
)
```
