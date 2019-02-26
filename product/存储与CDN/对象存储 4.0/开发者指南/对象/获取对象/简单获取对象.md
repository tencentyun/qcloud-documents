## 适用场景

您可以直接发起请求获取 COS 中的对象，获取对象支持以下功能：

- 获取完整的单个对象：直接发起 GET 请求即可获取完整的对象数据。
- 获取单个对象的部分内容：可在 GET 请求中传入 `Range` 请求头部，支持检索一个特定的字节范围。不支持检索多个范围。

对象的元数据将会作为 HTTP 响应头部随对象内容一同返回，GET 请求支持使用 URL 参数的方式覆盖响应的部分元数据值，例如 `Content-Dispositon` 的响应值。支持修改的响应头部包括：

- Content-Type
- Content-Language
- Expires
- Cache-Control
- Content-Disposition
- Content-Encoding

## 使用方法

### 使用 REST API

您可以直接使用 REST API 发起一个获取对象请求，可参考 [GET Object 文档说明](https://cloud.tencent.com/document/product/436/7753)。

### 使用 C++ SDK

对象存储 COS 的 C++ SDK 中提供了此方法，可参考 [C++ SDK 接口文档 Get Object 部分](https://cloud.tencent.com/document/product/436/12302#get-object)。

#### 步骤说明

1. 传入配置文件路径初始化 CosConfig，初始化 CosAPI 对象。
2. 执行 GetObject() 方法下载文件到本地或数据流中，需要提供存储桶名称和对象键名称。

#### 代码示例

下列的代码示例演示了如何简单获取对象：

``` cpp
// 下载到本地文件
{
    // request需要提供appid、bucketname、object,以及本地的路径（包含文件名）
    qcloud_cos::GetObjectByFileReq req(bucket_name, object_name, local_path);
    qcloud_cos::GetObjectByFileResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // 下载成功，可以调用GetObjectByFileResp的成员函数
    } else {
        // 下载失败，可以调用CosResult的成员函数输出错误信息，比如requestID等
    }
}

// 下载到流中
{
    // request需要提供appid、bucketname、object, 以及输出流
    std::ostringstream os;
    qcloud_cos::GetObjectByStreamReq req(bucket_name, object_name, os);
    qcloud_cos::GetObjectByStreamResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // 下载成功，可以调用GetObjectByStreamResp的成员函数
    } else {
        // 下载失败，可以调用CosResult的成员函数输出错误信息，比如requestID等
    }
}

// 多线程下载文件到本地
{
    // request需要提供appid、bucketname、object,以及本地的路径（包含文件名）
    qcloud_cos::MultiGetObjectReq req(bucket_name, object_name, local_path);
    qcloud_cos::MultiGetObjectResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // 下载成功，可以调用MultiGetObjectResp的成员函数
    } else {
        // 下载失败，可以调用CosResult的成员函数输出错误信息，比如requestID等
    }
}
```

可以通过设置 Request 的成员函数来设置特定的响应头部：

``` cpp
// 设置响应头部中的 Content-Type 参数
void SetResponseContentType(const std::string& str);

// 设置响应头部中的 Content-Language 参数
void SetResponseContentLang(const std::string& str);

// 设置响应头部中的 Content-Expires 参数
void SetResponseExpires(const std::string& str);

// 设置响应头部中的 Cache-Control 参数
void SetResponseCacheControl(const std::string& str);

// 设置响应头部中的 Content-Disposition 参数
void SetResponseContentDisposition(const std::string& str);

// 设置响应头部中的 Content-Encoding 参数
void SetResponseContentEncoding(const std::string& str);
```
### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档 Get Object 部分](https://cloud.tencent.com/document/product/436/12263#get-object)。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 执行 getObject 方法获取输入流或者将内容保存到本地。

#### 代码示例
（1）以下代码演示了如何下载对象（无版本控制）：

```java
// 1 初始化用户身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("1250000", "AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// 设置bucket名
String bucketName = "mybucket";
String key = "aaa.txt";

try {
    // 下载文件
    COSObject cosObject = cosclient.getObject(bucketName, key);
    // 获取输入流
    COSObjectInputStream cosObjectInput = cosObject.getObjectContent();
    // 关闭输入流
    cosObjectInput.close();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}
```
（2）`GetObjectRequest` 支持指定要从对象检索的数据字节范围，以下代码演示了指定字节的方法：

```java
// 1 初始化用户身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("1250000", "AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// 设置bucket名
String bucketName = "mybucket";
String key = "aaa.txt";

try {
    GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
    // 设置下载前11个字节
    getObjectRequest.setRange(0, 10);
    // 下载文件
    COSObject cosObject = cosclient.getObject(bucketName, key);
    // 获取输入流
    COSObjectInputStream cosObjectInput = cosObject.getObjectContent();
    // 关闭输入流
    cosObjectInput.close();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}
```
（3）检索对象时还可以用 `ResponseHeaderOverrides` 对象并设置相应的请求属性来替换响应头部值，以下是该方法的示例：

```java
// 1 初始化用户身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("1250000", "AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);
// 设置bucket名
String bucketName = "mybucket";
String key = "aaa.txt";

try {
    GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
    ResponseHeaderOverrides responseHeaders = new ResponseHeaderOverrides();
    String responseContentType="image/x-icon";
    String responseContentEncoding = "gzip,deflate,compress";
    String responseContentLanguage = "zh-CN";
    String responseContentDispositon = "filename=\"abc.txt\"";
    String responseCacheControl = "no-cache";
    String expireStr = DateUtils.formatRFC822Date(new Date(System.currentTimeMillis() + 24 * 3600 * 1000));
    responseHeaders.setContentType(responseContentType);
    responseHeaders.setContentEncoding(responseContentEncoding);
    responseHeaders.setContentLanguage(responseContentLanguage);
    responseHeaders.setContentDisposition(responseContentDispositon);
    responseHeaders.setCacheControl(responseCacheControl);
    responseHeaders.setExpires(expireStr);
    getObjectRequest.setResponseHeaders(responseHeaders);
    // 下载文件
    COSObject cosObject = cosclient.getObject(bucketName, key);
    // 获取输入流
    COSObjectInputStream cosObjectInput = cosObject.getObjectContent();
    // 关闭输入流
    cosObjectInput.close();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}
``` 
### 使用 Javascript SDK

#### 步骤说明

1. 准备好签名服务器，提供 auth.php 接口给前端获取签名，可以参考 [后端签名例子](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/server) 。

2. 创建测试文件 test.html，写入如下代码，放到静态服务器下，用` http://127.0.0.1/test.html `访问。

#### 代码示例

下列的代码示例演示了如何简单获取对象：

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

cos.getObject({
    Bucket: config.Bucket,
    Region: config.Region,
    Key: '1.txt',
}, function (err, data) {
    console.log(err || '文件内容大小：' + data.Body.length);
});
</script>
```

### 使用 Node.js SDK

#### 步骤说明

1. 安装 npm 依赖包：
```shell
npm i cos-nodejs-sdk-v5
```

2. 创建测试文件 test.js，并命令行执行 `node test.js` 。

#### 代码示例
下列的代码示例演示了如何简单获取对象：

```javascript
var fs = require('fs');
var path = require('path');
var COS = require('..');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
cos.getObject({
    Bucket: Bucket,
    Region: Region,
    Key: '1.jpg',
    Output: fs.createWriteStream(path.resolve(__dirname, '1.download.jpg'))
}, function (err, data) {
    console.log(err || data);
});
```
### 使用 PHP SDK

对象存储 COS 的 PHP SDK 中提供了此方法，可参考 [PHP SDK 接口文档文件下载部分](https://cloud.tencent.com/document/product/436/12267#.E4.B8.8B.E8.BD.BD.E6.96.87.E4.BB.B6)。

#### 步骤说明

1. 初始化客户端 cosClient。
2. 执行 getObject 方法获取对象，需要提供存储桶名称。
3. 添加 SaveAs 字段将获取的数据流保存为本地文件。

#### 代码示例

下列的代码示例演示了如何简单获取对象：

```php
try {
    $result = $cosClient->getObject(array(
        'Bucket' => 'testbucket-125000000',
        'Key' => 'hello.txt',
        'SaveAs' => 'hello.txt'));
    echo($result['Body']);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 使用 Python SDK

对象存储 COS 的 Python SDK 中提供了此方法，可参考 [Python SDK 接口文档文件下载部分](https://cloud.tencent.com/document/product/436/12270#.E6.96.87.E4.BB.B6.E4.B8.8B.E8.BD.BD)。

#### 步骤说明

1. 通过 CosConfig 类来配置，初始化客户端 CosS3Client。
2. 执行 get_object() 方法获取数据流，需要提供存储桶名称和对象键名称。

#### 代码示例

下列的代码示例演示了如何简单获取对象：

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
response = client.get_object(
    Bucket=bucket,
    Key=file_name,
)
# 获取对象至本地文件
response['Body'].get_stream_to_file('output.txt')
```

如果希望获取对象的文件流，可以通过 get_raw_stream() 方法来获取文件流对象：
```python
response = client.get_object(
    Bucket=bucket,
    Key=file_name,
)
fp = response['Body'].get_raw_stream()
# 调用read()方法读取文件流
print fp.read(2)
```

可以通过设置Range参数来获取指定范围的对象，格式为 bytes=first-last:
```python
# 获取对象的前10个字节
response = client.get_object(
    Bucket=bucket,
    Key=file_name,
    Range='bytes=0-9'
)
```

可以通过设置 Response Header 参数来设置特定的响应头部：
```python
response = client.get_object(
    Bucket=bucket,
    Key=file_name,
    ResponseCacheControl='no-cache',
    ResponseContentDisposition='attachment; filename=test.txt',
    ResponseContentEncoding='gzip',
    ResponseContentLanguage='zh-cn',
    ResponseContentType='text/html',
    ResponseExpires='Tue, 05 Dec 2017 10:01:19 GMT'
)
```
