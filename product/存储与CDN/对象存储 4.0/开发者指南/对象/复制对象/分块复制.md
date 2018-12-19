## 适用场景

当需要复制一个超过 5 GB 的对象时，您需要选择分块复制的方法来实现。使用分块上传的 API 来创建一个新的对象，并使用 Part Copy 的功能，携带 `x-cos-copy-source` 头部来指定源对象，流程包括：

1. 初始化一个分块上传的对象。
2. 复制源对象的数据，可指定 `x-cos-copy-range` 头部，每次只可复制最多 5 GB 数据。
3. 完成分块上传。

使用腾讯云 COS 提供的 SDK 可以轻松完成分块复制的功能。

## 使用方法

### 使用 C++ SDK

对象存储 COS 的 C++ SDK 中提供了方法，可参考 C++ SDK 接口文档中的以下部分：

- [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/12302#initiate-multipart-upload)
- [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/12302#complete-multipart-upload)

#### 步骤说明

1. 传入配置文件路径初始化 CosConfig，初始化 CosAPI 对象。
2. 调用 InitMultiUpload() 来初始化分块上传，获取上传 Id。
3. 反复调用 UploadPartCopyData() 方法来复制一个分块，其中 UploadPartCopyDataReq 需要提供存储桶名称、对象键名称、上传 Id、分块号， 并使用 UploadPartCopyDataReq::SetXCosCopySource 设置待拷贝的源文件。
4. 执行 CompleteMultiUpload() 方法来完成一个分块上传，需要提供存储桶名、对象键名称、UploadId 以及所有分块信息。

#### 代码示例

下列的代码示例演示了如何分块复制对象：

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";
std::string object_name = "sevenyou";
std::string upload_id = ""; 
std::vector<std::string> etags;
std::vector<int64_t> part_nums;

// 1. 调用InitMultiUpload获取uploadId
qcloud_cos::InitMultiUploadReq req(bucket_name, object_name);
qcloud_cos::InitMultiUploadResp resp;
qcloud_cos::CosResult init_result = cos.InitMultiUpload(init_req, init_resp);

if (init_result.IsSucc()) {
    upload_id = init_resp.GetUploadId();
} else {
    // do sth
}

// 2.1 拷贝第一个分片
{
    std::string part_number = 1; 
    qcloud_cos::UploadPartCopyDataReq req(bucket_name, object_name, upload_id, part_number);
    req.SetXCosCopySource("sevenyousouthtest-12345656.cn-south.myqcloud.com/sevenyou_source_obj");
    qcloud_cos::UploadPartCopyDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartCopyData(req, &resp);
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_nums.push_back(part_number);
    }
}

// 2.2 拷贝第二个分片
{
    std::string part_number = 2; 
    qcloud_cos::UploadPartCopyDataReq req(bucket_name, object_name, upload_id, part_number);
    req.SetXCosCopySource("sevenyousouthtest-12345656.cn-south.myqcloud.com/sevenyou_source_obj");
    qcloud_cos::UploadPartCopyDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartCopyData(req, &resp);
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_nums.push_back(part_number);
    }
}

// 2.x 拷贝后续分片
...

// 3. 调用CompleteMultiUpload结束分片拷贝
qcloud_cos::CompleteMultiUploadReq comp_req(bucket_name, object_name, upload_id);
qcloud_cos::CompleteMultiUploadResp comp_resp;
comp_req.SetEtags(etags);
comp_req.SetPartNumbers(part_numbers);

qcloud_cos::CosResult comp_result = cos.CompleteMultiUpload(comp_req, &comp_resp);
```

可以通过 copy() 方法来复制一个对象，自动根据拷贝源对象的大小和所处地域来调用不同的接口，只需要提供存储桶名、对象键名称以及拷贝源存储桶、源对象键、源地域：

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";
std::string object_name = "sevenyou";

qcloud_cos::CopyReq req(bucket_name, object_name);
qcloud_cos::CopyResp resp;

req.SetXCosCopySource("sevenyou-54321.cos.ap-beijing.myqcloud.com/sevenyou_copy_test");
qcloud_cos::CosResult result = cos.Copy(req, &resp);
```
### 使用 Java SDK

对象存储 COS 的 Java SDK 中提供了此方法，可参考 [Java SDK 接口文档拷贝文件部分](https://cloud.tencent.com/document/product/436/12263#.E6.8B.B7.E8.B4.9D.E6.96.87.E4.BB.B6) 。

#### 步骤说明

1. 初始化客户端 cosclient。
2. 使用 TransferManager 中提供的高级 API copy 接口来完成拷贝。

#### 代码示例

对于 5G 以上的文件，需要通过分块上传中的 copypart 来实现，步骤较多，因此在 TransferManager 中封装了一个 copy 接口，不仅能根据文件大小自动的选择接口，同时能支持 5G 以上的文件拷贝。推荐使用该接口进行文件的 copy。示例代码如下：

```java
// 1 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);


ExecutorService threadPool = Executors.newFixedThreadPool(32);
// 传入一个threadpool, 若不传入线程池, 默认TransferManager中会生成一个单线程的线程池。
TransferManager transferManager = new TransferManager(cosclient, threadPool);

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
    Copy copy = transferManager.copy(copyObjectRequest);
    // 返回一个异步结果copy, 可同步的调用waitForCopyResult等待copy结束, 成功返回CopyResult, 失败抛出异常.
    CopyResult copyResult = copy.waitForCopyResult();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
} catch (InterruptedException e) {
    e.printStackTrace();
}

transferManager.shutdownNow();
cosclient.shutdown();
```



### 使用 PHP SDK

#### 步骤说明

1. 初始化客户端 cosClient。
2. 执行 Copy 分块复制对象，需要提供存储桶名称和对象键名称。

#### 代码示例

下列的代码示例演示了如何分块复制对象：

```php
try {
    $result = $cosClient->Copy($bucket = 'bucket-125000000',
        $key = 'hello.txt',
        $copysource = 'bucket-appid.region.myqcloud.com/cos_path',);
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
### 使用 Python SDK

对象存储 COS 的 Python SDK 中提供了此方法，可参考 Python SDK 接口文档中的以下部分：

- [创建分块上传](https://cloud.tencent.com/document/product/436/12270#.E5.88.9B.E5.BB.BA.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0)
- [完成分块上传](https://cloud.tencent.com/document/product/436/12270#.E5.AE.8C.E6.88.90.E5.88.86.E5.9D.97.E4.B8.8A.E4.BC.A0)

#### 步骤说明

1.通过 CosConfig 类来配置，初始化客户端 CosS3Client。

2.执行 create_multipart_upload() 方法来初始化一个分块上传，需要提供存储桶名称和对象键名称。

3.重复执行 upload_part_copy() 方法来复制一个分块，需要提供存储桶名称、对象键名称、UploadId 以及单个分块的内容。

4.执行 complete_multipart_upload() 方法来完成一个分块上传，需要提供存储桶名、对象键名称、UploadId 以及所有分块信息。

#### 代码示例

下列的代码示例演示了如何分块复制对象：

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
    
# 2.拷贝单个分块
copy_source = {
    'Bucket': 'test-121212121',
    'Key': '10GB.txt',
    'Region': 'ap-guangzhou'
}
lst = list()
part_number = 1

response = client.upload_part_copy(
        Bucket=bucket,
        Key=file_name,
        UploadId=uploadid,
        PartNumber=part_number,
        CopySource=copy_source,
        CopySourceRange='bytes=0-1048575'
)
lst.append({'PartNumber': part_number, 'ETag': response['ETag']})
part_number += 1

response = client.upload_part_copy(
        Bucket=bucket,
        Key=file_name,
        UploadId=uploadid,
        PartNumber=part_number,
        CopySource=copy_source,
        CopySourceRange='bytes=1048576-2097151'
)
lst.append({'PartNumber': part_number, 'ETag': response['ETag']})
part_number += 1
# more ...

# 3.完成分块上传
response = client.complete_multipart_upload(
    Bucket=bucket,
    Key=file_name,
    UploadId=uploadid,
    MultipartUpload={'Part': lst}
)
```

可以通过 copy() 方法来复制一个对象，自动根据拷贝源对象的大小和所处地域来调用不同的接口，只需要提供存储桶名、对象键名称以及拷贝源存储桶、源对象键、源地域：
```python
bucket = 'testbucket-123456789'
file_name = 'test.txt'
copy_source = {
    'Bucket': 'test-121212121',
    'Key': '10GB.txt',
    'Region': 'ap-guangzhou'
}
response = client.copy(
    Bucket=bucket,
    Key=file_name,
    CopySource=copy_source
)
```
