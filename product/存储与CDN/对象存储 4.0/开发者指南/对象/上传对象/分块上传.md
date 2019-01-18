## 适用场景

分块上传适合于在弱网络或高带宽环境下上传较大的对象。COS 的控制台和 SDK 会协助您将单个对象切成一组分块并完成上传，您也可以自行切分对象并分别调用 API 上传各个分块。使用分块上传有一些优势：

- 在弱网络环境中，使用较小的分块可以将网络失败导致的中断影响降低，实现对象续传。
- 在高带宽环境中，并发上传对象分块能充分利用网络带宽，乱序上传并不影响最终组合对象。
- 使用分块上传，您可以随时暂停和恢复单个大对象的上传。除非发起终止操作，所有未完成的对象将可随时继续上传。
- 分块上传也适用于在未知对象总大小的情况下上传对象，您可以先发起上传，再组合对象以获得完整大小。

上传时，这组分块将会按连续的序号编号，您可以独立上传或者按照任意顺序上传各个分块，最终 COS 将会根据分块编号顺序重新组合出该对象。任意分块传输失败，都可以重新传输当前分块，不会影响其他分块和内容完整性。一般在弱网络环境中，当单个对象大于 20 MB 可优先考虑分块上传，在大带宽环境中可将超过 100 MB 的对象进行分块上传。

## 使用方法

### 使用 REST API

您可以直接使用 REST API 发起一个分块上传的请求，可参考以下 API 文档部分：

- [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746)
- [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742)
- [Upload Part](https://cloud.tencent.com/document/product/436/7750)
- [Abort Multipart Upload](https://cloud.tencent.com/document/product/436/7740)

### 使用 C++ SDK

对象存储 COS 的 C++ SDK 中提供了此方法，可参考 [C++ SDK 接口文档分块上传操作部分](https://cloud.tencent.com/document/product/436/12302#.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0.E6.93.8D.E4.BD.9C)。 

#### 步骤说明

1. 传入配置文件路径初始化 CosConfig，初始化 CosAPI 对象。
2. 调用 InitMultiUpload() 来初始化分块上传，获取上传 Id。
3. 反复调用 UploadPartData() 方法来上传一个分块，其中 UploadPartDataReq 需要提供存储桶名称、对象键名称、上传 Id、分块号以及上传的文件内容。
4. 执行 CompleteMultiUpload() 方法来完成一个分块上传，需要提供存储桶名、对象键名称、UploadId 以及所有分块信息。

#### 代码示例

下列的代码示例演示了如何分块上传对象：

``` cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";
std::string object_name = "sevenyou";
std::string upload_id = ""; 
std::vector<std::string> etags;
std::vector<int64_t> part_nums;

// 1. 调用InitMultiUpload获取uploadId
qcloud_cos::InitMultiUploadReq init_req(bucket_name, object_name);
qcloud_cos::InitMultiUploadResp init_resp;
qcloud_cos::CosResult init_result = cos.InitMultiUpload(init_req, init_resp);

if (init_result.IsSucc()) {
    upload_id = init_resp.GetUploadId();
} else {
    // do sth
}

// 2.1 上传第一个分块
{
    std::fstream is("demo_5M.part1");
    qcloud_cos::UploadPartDataReq req(bucket_name, object_name,
                                      upload_id, is);
    req.SetPartNumber(1);
    qcloud_cos::UploadPartDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartData(req, &resp);

    // 上传成功需要记录分块编号以及返回的etag
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_nums.push_back(1);
    }
    is.close();
}

// 2.2 上传第二个分块
{
    std::fstream is("demo_5M.part2");
    qcloud_cos::UploadPartDataReq req(bucket_name, object_name,
                                      upload_id, is);
    req.SetPartNumber(2);
    qcloud_cos::UploadPartDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartData(req, &resp);

    // 上传成功需要记录分块编号以及返回的etag
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_nums.push_back(2);
    }
    is.close();
}

// 2.x 上传后续分块
...

// 3. 结束分块上传
qcloud_cos::CompleteMultiUploadReq req(bucket_name, object_name, upload_id);
qcloud_cos::CompleteMultiUploadResp resp;
req.SetEtags(etags);
req.SetPartNumbers(part_nums);

qcloud_cos::CosResult result = cos.CompleteMultiUpload(req, &resp);

```

可以通过 AbortMultiUpload() 方法来终止一个分块上传，需要提供存储桶名、对象键名称以及 UploadId：
```cpp
qcloud_cos::AbortMultiUploadReq req(bucket_name, object_name, upload_id);
qcloud_cos::AbortMultiUploadResp resp;
qcloud_cos::CosResult result = cos.AbortMultiUpload(req, &resp);
```

可以通过 list_parts() 方法来列出一个分块上传，需要提供存储桶名、对象键名称以及 UploadId：
``` cpp
qcloud_cos::ListPartsReq req(bucket_name, object_name, upload_id);
qcloud_cos::ListPartsResp resp;
qcloud_cos::CosResult result = cos.ListParts(req, &resp);
```

### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档 PUT object 中的分块文件上传部分](https://cloud.tencent.com/document/product/436/12263#put-object.EF.BC.88.E4.B8.8A.E4.BC.A0-object.EF.BC.89)。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 使用 initiateMultipartUpload 初始化分块上传获取一个新的 uploadid，或者调用 listMultipartUploads 获取之前还未完成的分块上传，得到 uploadid。
3. 已上传的分块可使用 listParts 进行获取，未上传的分块使用 uploadPart 上传分块数据,  或者 copyPart 选择从另外一个文件 copy 分块到目前文件。以此达到断点续传的功能，如果对已上传的分块再次调用 uploadPart 或者 copyPart 则会覆盖已上传的分块数据。
4. 使用 completeMultipartUpload 完成分块上传或者调用 abortMultipartUpload 终止分块上传。

#### 代码示例

（1）`InitiateMultipartUploadRequest`是初始化分块上传的请求，包含了分快上传的路径，存储类型等信息。通过调用 initiateMultipartUpload 可获得一个新的分快上传 ID。

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
InitiateMultipartUploadRequest request = new InitiateMultipartUploadRequest(bucketName, key);
// 设置存储类型, 默认是标准(Standard), 低频(standard_ia) 
request.setStorageClass(StorageClass.Standard_IA);
try {
    InitiateMultipartUploadResult initResult = cosclient.initiateMultipartUpload(request);
    // 获取uploadid
    String uploadId =  initResult.getUploadId();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}

cosclient.shutdown();
```

（2） `UploadPartRequest`是分块上传请求，包含了要上传的数据，分块号。通过调用uploadPart 上传分块，并获取分块的 partEtag。

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
// uploadid(通过initiateMultipartUpload或者ListMultipartUploads获取)
String uploadId = "1512380198aecfed004aeaaca195d08232f718f7b52a91b8f6e9d36c7dfead2b3d1c917a6f";

// 生成要上传的数据, 这里初始化一个1M的数据
byte data[] = new byte[1024 * 1024];
UploadPartRequest uploadPartRequest = new UploadPartRequest();
uploadPartRequest.setBucketName(bucketName);
uploadPartRequest.setKey(key);
uploadPartRequest.setUploadId(uploadId);
// 设置分块的数据来源输入流
uploadPartRequest.setInputStream(new ByteArrayInputStream(data));
// 设置分块的长度
uploadPartRequest.setPartSize(data.length); // 设置数据长度
uploadPartRequest.setPartNumber(10);     // 假设要上传的part编号是10

try {
    UploadPartResult uploadPartResult = cosclient.uploadPart(uploadPartRequest);
    PartETag partETag = uploadPartResult.getPartETag();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}

cosclient.shutdown();
```

（3） `CompleteMultipartUploadRequest`是完成分块请求，需要传入之前上传的所有分块的partEtag。通过调用completeMultipartUpload完成分块上传。示例代码如下：

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
// uploadid(通过initiateMultipartUpload或者ListMultipartUploads获取)
String uploadId = "1512380198aecfed004aeaaca195d08232f718f7b52a91b8f6e9d36c7dfead2b3d1c917a6f";

// 这里初始化一个空的队列， 用于保存已上传的分片信息, 代码不能直接运行， 需要通过之前的uploadpart或者list parts的结果获取,加入到partEtags队列中 
List<PartETag> partETags = new LinkedList<>();

// 分片上传结束后，调用complete完成分片上传
CompleteMultipartUploadRequest completeMultipartUploadRequest =
        new CompleteMultipartUploadRequest(bucketName, key, uploadId, partETags);
try {
    CompleteMultipartUploadResult completeResult =
            cosclient.completeMultipartUpload(completeMultipartUploadRequest);
    String etag = completeResult.getETag();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}

cosclient.shutdown();
```

（4） `AbortMultipartUploadRequest`是终止分块上传请求，用于终止一个未 complete 的分块上传，表示中断销毁之前已上传的分块。通过调用 abortMultipartUpload 终止分块上传请求，示例代码如下：

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
// uploadid(通过initiateMultipartUpload或者ListMultipartUploads获取)
String uploadId = "1512380198aecfed004aeaaca195d08232f718f7b52a91b8f6e9d36c7dfead2b3d1c917a6f";

AbortMultipartUploadRequest abortMultipartUploadRequest = new AbortMultipartUploadRequest(bucketName, key, uploadId);
try {
    cosclient.abortMultipartUpload(abortMultipartUploadRequest);
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}

cosclient.shutdown();
```

（5）`ListPartsRequest`是列出已上传的分块的请求，可用于断点续传。通过调用 listParts 获取已上传的分块，示例代码如下：

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
// uploadid(通过initiateMultipartUpload或者ListMultipartUploads获取)
String uploadId = "1512380198aecfed004aeaaca195d08232f718f7b52a91b8f6e9d36c7dfead2b3d1c917a6f";

List<PartETag> partETags = new LinkedList<>();      // 用于保存已上传的分片信息
PartListing partListing = null;
ListPartsRequest listPartsRequest = new ListPartsRequest(bucketName, key, uploadId);
do {
    try {
        partListing = cosclient.listParts(listPartsRequest);
    } catch (CosServiceException e) {
        e.printStackTrace();
    } catch (CosClientException e) {
        e.printStackTrace();
    }
    for (PartSummary partSummary : partListing.getParts()) {
        partETags.add(new PartETag(partSummary.getPartNumber(), partSummary.getETag()));
    }
    listPartsRequest.setPartNumberMarker(partListing.getNextPartNumberMarker());
} while (partListing.isTruncated());

cosclient.shutdown();
```

（6）`CopyPartResult`是分块 copy 的请求，表示该分块的数据来源于另外一个文件的某一部分。通过要拷贝的源文件的路径，bucket 信息，字节范围。调用 copyPart 可实现分块copy。示例代码如下所示：

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
// uploadid(通过initiateMultipartUpload或者ListMultipartUploads获取)
String uploadId = "1512380198aecfed004aeaaca195d08232f718f7b52a91b8f6e9d36c7dfead2b3d1c917a6f";

CopyPartRequest copyPartRequest = new CopyPartRequest();
// 要拷贝的源文件所在的region
copyPartRequest.setSourceBucketRegion(new Region("ap-beijing-1"));
// 要拷贝的源文件的bucket名称
copyPartRequest.setSourceBucketName(bucketName);
// 要拷贝的源文件的路径
copyPartRequest.setSourceKey("aaa/ccc.txt");
// 指定要拷贝的源文件的数据范围(类似content-range)
copyPartRequest.setFirstByte(0L);
copyPartRequest.setLastByte(1048575L);
// 目的bucket名称
copyPartRequest.setDestinationBucketName(bucketName);
// 目的路径名称
copyPartRequest.setDestinationKey(key);

// uploadid
copyPartRequest.setUploadId(uploadId);
try {
    CopyPartResult copyPartResult = cosclient.copyPart(copyPartRequest);
    PartETag partETag = copyPartResult.getPartETag();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}

cosclient.shutdown();
```
### 使用 JavaScript SDK

对象存储 COS 的 JavaScript SDK 中提供了此方法，可参考 [JavaScript SDK 接口文档分块上传操作部分](https://cloud.tencent.com/document/product/436/12260#.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0.E6.93.8D.E4.BD.9C) 。

#### 步骤说明

1. 准备好签名服务器，提供 auth.php 接口给前端获取签名，可以参考 [后端签名例子](https://github.com/tencentyun/cos-js-sdk-v5/tree/master/server) 。

2. 创建测试文件 test.html，写入如下代码，放到静态服务器下，用` http://127.0.0.1/test.html `访问。

#### 代码示例

下列的代码示例演示了如何分块上传对象：

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

    cos.sliceUploadFile({
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

对象存储 COS 的 Node.js SDK 中提供了此方法，可参考 [Node.js SDK 接口文档分块上传操作部分](https://cloud.tencent.com/document/product/436/12264#.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0.E6.93.8D.E4.BD.9C)。

#### 步骤说明

1. 安装 npm 依赖包：
```shell
npm i cos-nodejs-sdk-v5
```

2. 把要上传的文件 1.jpg 放在当前目录。

3. 创建测试文件 test.js，并命令行执行 `node test.js` 。

#### 代码示例

下列的代码示例演示了如何分块上传对象：

```javascript
var COS = require('cos-nodejs-sdk-v5');

var SecretId = 'AKIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // 替换为用户的 SecretId
var SecretKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';    // 替换为用户的 SecretKey
var Bucket = 'test-1250000000';                        // 替换为用户操作的 Bucket
var Region = 'ap-guangzhou';                           // 替换为用户操作的 Region

var cos = new COS({SecretId: SecretId, SecretKey: SecretKey});
cos.sliceUploadFile({
    Bucket: Bucket,
    Region: Region,
    Key: '1.jpg',
    FilePath: '1.jpg'
}, function (err, data) {
    console.log(err || data);
});
```
### 使用 PHP SDK

对象存储 COS 的 PHP SDK 中提供了此方法，可参考 [PHP SDK 接口文档分块文件上传部分](https://cloud.tencent.com/document/product/436/12267#.E5.88.86.E5.9D.97.E6.96.87.E4.BB.B6.E4.B8.8A.E4.BC.A0)。

#### 步骤说明

1. 初始化客户端 cosClient。
2. 执行 upload 方法上传数据流，需要提供存储桶名称和对象键名称。
3. 通过 fopen 上传文件流。

#### 代码示例

下列代码示例演示了分块上传对象的步骤：

* 内存上传：
```php
try {
    $result = $cosClient->upload(
                 $bucket='testbucket-125000000',
                 $key = '111.txt',
                 $body = 'HELLO';
    print_r($result);
    } catch (\Exception $e) {
    echo "$e\n";
}
```
* 文件流上传：
```php
try {
    $result = $cosClient->upload(
                 $bucket='testbucket-125000000',
                 $key = '111.txt',
                 $body = fopen($pathToFile, 'r+'));
    print_r($result);
    } catch (\Exception $e) {
    echo "$e\n";
}
```
### 使用 Python SDK

对象存储 COS 的 Python SDK 中提供了此方法，可参考 Python SDK 接口文档中的以下部分：

- [创建分块上传](https://cloud.tencent.com/document/product/436/12270#.E5.88.9B.E5.BB.BA.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0)
- [上传分块](https://cloud.tencent.com/document/product/436/12270#.E4.B8.8A.E4.BC.A0.E5.88.86.E5.9D.97)
- [完成分块上传](https://cloud.tencent.com/document/product/436/12270#.E5.AE.8C.E6.88.90.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0)
- [放弃分块上传](https://cloud.tencent.com/document/product/436/12270#.E6.94.BE.E5.BC.83.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0)
- [列出分块上传](https://cloud.tencent.com/document/product/436/12270#.E5.88.97.E5.87.BA.E4.B8.8A.E4.BC.A0.E5.88.86.E5.9D.97)

#### 步骤说明

1. 通过 CosConfig 类来配置, 初始化客户端 CosS3Client。
2. 执行 create_multipart_upload() 方法来初始化一个分块上传，需要提供存储桶名称和对象键名称。
3. 重复执行 upload_part() 方法来上传一个分块，需要提供存储桶名称、对象键名称、UploadId 以及单个分块的内容。
4. 执行 complete_multipart_upload() 方法来完成一个分块上传，需要提供存储桶名、对象键名称、UploadId 以及所有分块信息。

#### 代码示例

下列的代码示例演示了如何分块上传对象：

```python
secret_id = 'xxxxxxxx'      # 替换为用户的 secretId
secret_key = 'xxxxxxx'      # 替换为用户的 secretKey
region = 'ap-beijing-1'     # 替换为用户的 Region
token = ''                  # 使用临时密钥需要传入 Token，默认为空，可不填

config = CosConfig(Secret_id=secret_id, Secret_key=secret_key, Region=region, Token=token)
client = CosS3Client(config)

bucket = 'testbucket-123456789'
file_name = 'test.txt'

# 1.初始化分块上传
response = client.create_multipart_upload(
    Bucket=bucket,
    Key=file_name       
)
uploadid = response['UploadId']
    
# 2.上传单个分块
lst = list()
part_number = 1
with open('test.txt', 'rb') as fp:
    while True:
        data = fp.read(1024*1024)
        if data == "":
            break
        response = client.upload_part(
            Bucket=bucket,
            Key=file_name,
            UploadId=uploadid,
            PartNumber=part_number,
            Body=data
        )
        lst.append({'PartNumber': part_number, 'ETag': response['ETag']})
        part_number += 1

# 3.完成分块上传
response = client.complete_multipart_upload(
    Bucket=bucket,
    Key=file_name,
    UploadId=uploadid,
    MultipartUpload={'Part': lst}
)
```

可以通过abort_multipart_upload() 方法来终止一个分块上传，需要提供存储桶名、对象键名称以及UploadId：
```python
response = client.abort_multipart_upload(
    Bucket=bucket,
    Key=file_name,
    UploadId=uploadid
)
```

可以通过list_parts() 方法来列出一个分块上传，需要提供存储桶名、对象键名称以及UploadId：
```python
response = client.list_parts(
    Bucket=bucket,
    Key=file_name,
    UploadId=uploadid
)
```

可以通过list_multipart_uploads() 方法来列出某个存储桶中所有未完成的分块上传，需要提供存储桶名：
```python
response = client.list_multipart_uploads(
    Bucket=bucket
)
```
#### 
