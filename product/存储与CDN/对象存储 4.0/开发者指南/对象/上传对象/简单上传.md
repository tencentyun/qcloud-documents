## 适用场景

该操作适用于在单个请求中上传一个小于 5 GB 大小的对象，对于大于 5 GB 的对象，您必须使用分块上传的方式。

当您的对象较大（例如 100 MB）时，我们建议您在高带宽或弱网络环境中，优先使用分块上传的方式。

## 使用方法
### 使用 REST API

您可以直接使用 REST API 发起一个简单上传对象请求，可参考 [PUT Object 文档说明](https://cloud.tencent.com/document/product/436/7749)。

### 使用 C++ SDK

对象存储 COS 的 C++ SDK 中提供了此方法，可参考 [C++ SDK 接口文档 Put Object 部分](https://cloud.tencent.com/document/product/436/12302#put-object)。

#### 步骤说明

1. 传入配置文件路径初始化 CosConfig，初始化 CosAPI 对象。
2. 执行 PutObject() 方法来上传对象，需要提供存储桶名称和对象键名称以及上传的内容。

#### 代码示例

下列的代码示例演示了如何简单上传对象：

``` cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";
std::string object_name = "object_name";
// request的构造函数中需要传入本地文件路径
qcloud_cos::PutObjectByFileReq req(bucket_name, object_name, "/path/to/local/file");
// 调用Set方法设置元数据或者ACL等
req.SetXCosStorageClass("STANDARD_IA");

qcloud_cos::PutObjectByFileResp resp;
qcloud_cos::CosResult result = cos.PutObject(req, &resp);
```

可以通过指定文件流对象来支持上传文件流到 COS：

``` cpp
std::istringstream iss("put object");

// request的构造函数中需要传入istream
qcloud_cos::PutObjectByStreamReq req(bucket_name, object_name, iss);
qcloud_cos::PutObjectByStreamResp resp;

qcloud_cos::CosResult result = cos.PutObject(req, &resp);
```
### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档 PUT Object 部分](https://cloud.tencent.com/document/product/436/12263#put-object.EF.BC.88.E4.B8.8A.E4.BC.A0-object.EF.BC.89) 。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 执行 putObject 方法上传对象，支持将本地文件或者输入流上传到 COS。

#### 代码示例

（1）`PutObjectRequest` 封装了简单上传的请求，通过传入本地文件路径以及 COS 路径，支持设置存储类型，权限信息等，上传完成后会返回`PutObjectResult` ，失败抛出异常。示例代码如下：

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
File localFile = new File("src/test/resources/len10M.txt");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
// 设置存储类型, 默认是标准(Standard), 低频(standard_ia)
putObjectRequest.setStorageClass(StorageClass.Standard_IA);
try {
    PutObjectResult putObjectResult = cosclient.putObject(putObjectRequest);
    // putobjectResult会返回文件的etag
    String etag = putObjectResult.getETag();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}

// 关闭客户端
cosclient.shutdown();
```

（2）`PutObjectRequest`同时支持传入输入流，从流式上传到COS，但需要指定长度，示例代码如下所示：

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
File localFile = new File("src/test/resources/len10M.txt");

InputStream input = new ByteArrayInputStream(new byte[10]);
ObjectMetadata objectMetadata = new ObjectMetadata();
// 从输入流上传必须制定content length, 否则http客户端可能会缓存所有数据，存在内存OOM的情况
objectMetadata.setContentLength(10);
// 设置contenttype默认下载时根据cos路径key的后缀返回响应的contenttype, 上传时设置contenttype会覆盖默认值
objectMetadata.setContentType("image/jpeg");

PutObjectRequest putObjectRequest =
        new PutObjectRequest(bucketName, key, input, objectMetadata);
// 设置存储类型, 默认是标准(Standard), 低频(standard_ia)
putObjectRequest.setStorageClass(StorageClass.Standard_IA);
try {
    PutObjectResult putObjectResult = cosclient.putObject(putObjectRequest);
    // putobjectResult会返回文件的etag
    String etag = putObjectResult.getETag();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}

// 关闭客户端        
cosclient.shutdown();
```
### 使用 JavaScript SDK

对象存储 COS 的 JavaScript SDK 中提供了此方法，可参考 [JavaScript SDK 接口文档 Put Object 部分](https://cloud.tencent.com/document/product/436/12260#put-object)。

#### 步骤说明

1. 准备好签名服务器，提供 auth.php 接口给前端获取签名，可以参考 [后端签名例子](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/server) 。

2. 创建测试文件 test.html，写入如下代码，放到静态服务器下，用` http://127.0.0.1/test.html `访问。

#### 代码示例

下列的代码示例演示了如何简单上传对象：

```html
<script src="dist/cos-js-sdk-v5.min.js"></script>
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

// 监听选文件
document.getElementById('file-selector').onchange = function () {
    
    var file = this.files[0];
    if (!file) return;

    cos.putObject({
        Bucket: Bucket,
        Region: Region,
        Key: file.name,
        Body: file,
    }, function (err, data) {
        console.log(err, data);
    });

};
</script>
```
### 使用 Node.js SDK

对象存储 COS 的 Node.js SDK 中提供了此方法，可参考 [Node.js SDK 接口文档 Put Object 部分](https://cloud.tencent.com/document/product/436/12264#put-object)。

#### 步骤说明

1. 安装 npm 依赖包：
```shell
npm i cos-nodejs-sdk-v5
```

2. 把要上传的文件 1.jpg 放在当前目录。
3. 创建测试文件 test.js，并命令行执行 `node test.js` 。

#### 代码示例

下列的代码示例演示了如何简单上传对象：

```javascript
var fs = require('fs');
var path = require('path');
var COS = require('cos-nodejs-sdk-v5');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
cos.putObject({
    Bucket: Bucket,
    Region: Region,
    Key: '1.jpg',
    Body: fs.readFileSync(path.resolve(__dirname, '1.jpg'))
}, function (err, data) {
    console.log(err || data);
});
```
### 使用 PHP SDK

对象存储 COS 的 PHP SDK 中提供了此方法，可参考 [PHP SDK 接口文档简单文件上传部分](https://cloud.tencent.com/document/product/436/12267#.E7.AE.80.E5.8D.95.E6.96.87.E4.BB.B6.E4.B8.8A.E4.BC.A0)。

#### 步骤说明

1. 初始化客户端 cosClient 。
2. 执行 putObject 方法上传数据流，需要提供存储桶名称和对象键名称。
3. 通过 fopen上传文件流。

#### 代码示例

以下代码示例演示了简单上传对象的步骤：

* 内存上传：
```php
try {
    $result = $cosClient->putObject(array(
        'Bucket' => 'testbucket-125000000',
        'Key' => '11',
        'Body' => 'Hello World!'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
* 文件流上传：
```php
try {
    $result = $cosClient->putObject(array(
        'Bucket' => 'testbucket-125000000',
        'Key' => '11',
        'Body'   => fopen($pathToFile, 'r+')));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
'Body'   => fopen($pathToFile, 'r+')
```
### 使用 Python SDK

对象存储 COS 的 Python SDK 中提供了此方法，可参考 [Python SDK 接口文档简单文件上传部分](https://cloud.tencent.com/document/product/436/12270#.E7.AE.80.E5.8D.95.E6.96.87.E4.BB.B6.E4.B8.8A.E4.BC.A0)。

#### 步骤说明

1. 通过 CosConfig 类来配置，初始化客户端 CosS3Client。
2. 执行 put_object() 方法来上传对象，需要提供存储桶名称和对象键名称以及上传的内容。

#### 代码示例

下列的代码示例演示了如何简单上传对象：

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

response = client.put_object(
    Bucket=bucket,
    Key=file_name,
    Body='1234'         
)
```

可以通过指定文件流对象来支持上传文件流到 COS：
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

# 生成一个文件
with open(file_name, 'wb') as fp:
    fp.write('helloworld!')
with open(file_name, 'rb') as fp:
    response = client.put_object(
        Bucket=bucket,
        Key=file_name,
        Body=fp
    )
```

可以通过设置特定的参数来设置对象的元信息：
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

response = client.put_object(
    Bucket=bucket,
    Key=file_name,
    Body='123',
    StorageClass='STANDARD',
    ACL='public-read',
    CacheControl='no-cache',
    ContentDisposition='attachment; filename=test.txt',
    ContentEncoding='gzip',
    ContentLanguage='zh-cn',
    ContentType='text/html',
    Expires='Tue, 05 Dec 2017 10:01:19 GMT',
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    }
)
```
