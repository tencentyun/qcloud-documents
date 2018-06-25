## 适用场景

腾讯云 COS 支持按照前缀顺序列出对象键，您也可以在对象键中使用 `/` 字符来实现类似传统文件系统的层级结构，COS 也支持按照分隔符来做层级结构的选择和浏览。

您可以列出单个存储桶中的所有对象键，根据前缀的 UTF-8 二进制顺序列出，或选择指定前缀过滤对象键的列表。例如加入参数 `t` 将列出 `tapd`  的对象，而跳过以 `a` 或其他字符为前缀的对象。

加入 `/` 分隔符可将根据此分隔符重新组织对象键，您可以结合前缀和分隔符来实现类似文件夹检索的功能。例如加入前缀参数 `t`  并加入分隔符 `/` 将会直接列出类似 `tapd/file` 的对象键。

腾讯云 COS 在单个存储桶中支持无限数量的对象，因此对象键列表可能非常大。为了管理方便，单个列出对象接口将最多返回 1000 个键值的结果内容，同时会返回指示器来告知是否存在截断。您可以根据指示器和分隔符来发送一系列的列出对象键请求，实现列出所有键值，或寻找您所需要的内容。

## 使用方法

### 使用 REST API

您可以直接使用 REST API 发起一个获取对象请求，可参考 [Get Bucket 文档说明](https://cloud.tencent.com/document/product/436/7734)。

### 使用 C++ SDK

对象存储 COS 的 C++ SDK 中提供了此方法，可参考 [C++ SDK 接口文档 Get Bucket 部分](https://cloud.tencent.com/document/product/436/12302#get-bucket)。

#### 步骤说明

1. 传入配置文件路径初始化 CosConfig，初始化 CosAPI 对象。
2. 执行 GetBucket() 方法来列出对象，需要提供存储桶名称。

#### 代码示例

下列的代码示例演示了如何列出对象键：

``` cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";

// GetBucketReq的构造函数需要传入bucket_name
qcloud_cos::GetBucketReq req(bucket_name);
qcloud_cos::GetBucketResp resp;
qcloud_cos::CosResult result = cos.GetBucket(req, &resp);
```

可以通过指定参数来控制列出的对象键，MaxKeys 指定本次最多返回的对象个数，Prefix 指定只返回指定前缀的对象键，Delimiter 指定只返回指定分隔符的对象键：
``` cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";

// GetBucketReq的构造函数需要传入bucket_name
qcloud_cos::GetBucketReq req(bucket_name);
req.SetPrefix("prefix");
req.SetDelimiter(";");
qcloud_cos::GetBucketResp resp;
qcloud_cos::CosResult result = cos.GetBucket(req, &resp);
```
### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档  Get Bucket (List Objects) 部分](https://cloud.tencent.com/document/product/436/12263#get-bucket-(list-objects))。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 使用 listObjects 列出 object，每次最多列出 1000 个 object，如果需要列出所有的或者超过 1000 个, 则需要循环调用 listObjects。

#### 代码示例
（1） `ListObjectsRequest`包含了列出 Object 的请求, 可设置列出的 Object 的前缀, 分隔符, 示例代码如下:

```java
// 1 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket名需包含appid
String bucketName = "mybucket-1251668577";

ListObjectsRequest listObjectsRequest = new ListObjectsRequest();
// 设置bucket名称
listObjectsRequest.setBucketName(bucketName);
// prefix表示列出的object的key以prefix开始
listObjectsRequest.setPrefix("aaa/bbb");
// deliter表示分隔符, 设置为/表示列出当前目录下的object, 设置为空表示列出所有的object
listObjectsRequest.setDelimiter("");
// 如果object的路径中含有特殊字符, 建议使用url编码方式, 得到object的key后, 需要进行url decode
listObjectsRequest.setEncodingType("url");
// 设置最大遍历出多少个对象, 一次listobject最大支持1000
listObjectsRequest.setMaxKeys(1000);
ObjectListing objectListing = null;
try {
    objectListing = cosclient.listObjects(listObjectsRequest);
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}
// common prefix表示表示被delimiter截断的路径, 如delimter设置为/, common prefix则表示所有子目录的路径
List<String> commonPrefixs = objectListing.getCommonPrefixes();

// object summary表示所有列出的object列表
List<COSObjectSummary> cosObjectSummaries = objectListing.getObjectSummaries();
for (COSObjectSummary cosObjectSummary : cosObjectSummaries) {
    // 文件的路径key
    String key = cosObjectSummary.getKey();
    // 如果使用的encodingtype是url, 则进行url decode
    try {                                                               
        key = URLDecoder.decode(key, "utf-8"); 
    } catch (UnsupportedEncodingException e) {                          
        continue;                                                       
    }
    // 文件的etag
    String etag = cosObjectSummary.getETag();
    // 文件的长度
    long fileSize = cosObjectSummary.getSize();
    // 文件的存储类型
    String storageClasses = cosObjectSummary.getStorageClass();
}

cosclient.shutdown();
```
（2）如果要获取超过 maxkey 数量的 Object 或者获取所有的 Object, 则需要循环调用 listobject, 用上一次返回的 next marker 作为下一次调用的 marker, 直到返回的 truncated 为 false。

```java
// 1 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// bucket名需包含appid
String bucketName = "mybucket-1251668577";

ListObjectsRequest listObjectsRequest = new ListObjectsRequest();
// 设置bucket名称
listObjectsRequest.setBucketName(bucketName);
// prefix表示列出的object的key以prefix开始
listObjectsRequest.setPrefix("aaa/bbb");
// deliter表示分隔符, 设置为/表示列出当前目录下的object, 设置为空表示列出所有的object
listObjectsRequest.setDelimiter("");
// 如果object的路径中含有特殊字符, 建议使用url编码方式, 得到object的key后, 需要进行url decode
listObjectsRequest.setEncodingType("url");
// 设置最大遍历出多少个对象, 一次listobject最大支持1000
listObjectsRequest.setMaxKeys(1000);
ObjectListing objectListing = null;
do {

    try {
        objectListing = cosclient.listObjects(listObjectsRequest);
    } catch (CosServiceException e) {
        e.printStackTrace();
        return;
    } catch (CosClientException e) {
        e.printStackTrace();
        return;
    }
    // common prefix表示表示被delimiter截断的路径, 如delimter设置为/, common prefix则表示所有子目录的路径
    List<String> commonPrefixs = objectListing.getCommonPrefixes();

    // object summary表示所有列出的object列表
    List<COSObjectSummary> cosObjectSummaries = objectListing.getObjectSummaries();
    for (COSObjectSummary cosObjectSummary : cosObjectSummaries) {
        // 文件的路径key
        String key = cosObjectSummary.getKey();
        // 如果使用的encodingtype是url, 则进行url decode
        try {
            key = URLDecoder.decode(key, "utf-8");
        } catch (UnsupportedEncodingException e) {
            continue;
        }
        // 文件的etag
        String etag = cosObjectSummary.getETag();
        // 文件的长度
        long fileSize = cosObjectSummary.getSize();
        // 文件的存储类型
        String storageClasses = cosObjectSummary.getStorageClass();
    }
    
    // 获取下一次请求的next marker
    String nextMarker = "";
    try {
        nextMarker = URLDecoder.decode(objectListing.getNextMarker(), "utf-8");
    } catch (UnsupportedEncodingException e) {
        e.printStackTrace();
        return;
    }
    listObjectsRequest.setMarker(nextMarker);
} while (objectListing.isTruncated());

cosclient.shutdown();
```

### 使用 JavaScript SDK

对象存储 COS 的 JavaScript SDK 中提供了此方法，可参考 [JavaScript SDK 接口文档 Get Bucket 部分](https://cloud.tencent.com/document/product/436/12260#get-bucket)。

#### 步骤说明

1. 准备好签名服务器，提供 auth.php 接口给前端获取签名，可以参考 [后端签名例子](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/server) 。

2. 创建测试文件 test.html，写入如下代码，放到静态服务器下，用` http://127.0.0.1/test.html `访问。

#### 代码示例

下列的代码示例演示了如何列出对象键：

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

cos.getBucket({
    Bucket: Bucket,
    Region: Region,
}, function (err, data) {
    console.log(err, data);
});
</script>
```
### 使用 Node.js SDK

对象存储 COS 的 Node.js SDK 中提供了此方法，可参考 [Node.js SDK 接口文档 Get Bucket 部分](https://cloud.tencent.com/document/product/436/12264#get-bucket)。

#### 步骤说明

1. 安装 npm 依赖包：
```shell
npm i cos-nodejs-sdk-v5
```

2. 创建测试文件 test.js，并命令行执行 ```node test.js``` 。

#### 代码示例

下列的代码示例演示了如何列出对象键：

```javascript
var COS = require('cos-nodejs-sdk-v5');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
cos.getBucket({
    Bucket: Bucket,
    Region: Region,
    Prefix: '',    // 前缀,
    MaxKeys: '100' // 列出数目
}, function (err, data) {
    console.log(err || data);
});
```
### 使用 PHP SDK

对象存储 COS 的 PHP SDK 中提供了此方法，可参考 [PHP SDK 接口文档获取 Bucket 列表](https://cloud.tencent.com/document/product/436/12267#.E8.8E.B7.E5.8F.96bucket.E5.88.97.E8.A1.A8)。

#### 步骤说明

1. 初始化客户端 cosClient。
2. 执行 listObjects 列出对象，需要提供存储桶名称。

#### 代码示例

下列的代码示例演示了如何列出对象键：

```php
try {
    $result = $cosClient->listObjects(array(
        'Bucket' => 'testbucket-125000000'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 使用 Python SDK

对象存储 COS 的 Python SDK 中提供了此方法，可参考 [Python SDK 接口文档获取文件列表部分](https://cloud.tencent.com/document/product/436/12270#.E8.8E.B7.E5.8F.96.E6.96.87.E4.BB.B6.E5.88.97.E8.A1.A8)。

#### 步骤说明

1. 通过 CosConfig 类来配置, 初始化客户端 CosS3Client。
2. 执行 list_objects() 方法来列出对象，需要提供存储桶名称。

#### 代码示例

下列的代码示例演示了如何列出对象键：

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
response = client.list_objects(
    Bucket=bucket       
)
```

可以通过指定参数来控制列出的对象键，MaxKeys 指定本次最多返回的对象个数，Prefix 指定只返回指定前缀的对象键，Delimiter 指定只返回指定分隔符的对象键：
```python
bucket = 'testbucket-123456789'
response = client.list_objects(
    Bucket=bucket,
    Delimiter='/',
    MaxKeys=100,
    Prefix='test'
)
```
