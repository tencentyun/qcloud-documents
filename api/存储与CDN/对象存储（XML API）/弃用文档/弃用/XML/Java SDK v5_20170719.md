## 开发准备

### 相关资源
v5 版本 COS Java SDK 相关资源地址：[github项目](https://github.com/tencentyun/cos-java-sdk-v5)

### 环境依赖
v5 版本 COS Java SDK 适用于 JDK 1.7 及以上版本。

### 安装SDK
安装 SDK 的方式有两种：maven 安装和源码安装。
- **maven 安装**
在 maven 工程中使用 pom.xml 添加相关依赖，内容如下：
```xml
<dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cos_api</artifactId>
            <version>5.2.0</version>
</dependency>
```

- **源码安装**
从 [github](https://github.com/tencentyun/cos-java-sdk-v5) 项目资源中下载源码, 通过 maven 导入项目中。比如 eclipse，选择 File->Import->maven->Existing Maven Projects，确认即可。

### 卸载SDK

卸载 SDK 的方式即删除 pom 依赖或源码。

## 快速入门

```java
// 1 初始化身份信息
COSCredentials cred = new BasicCOSCredentials("1250000", "AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosClient = new COSClient(cred, clientConfig);
// 操作API， 如下文所述.或者参照Demo(https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/Demo.java)
```

## 基本 API 描述

COS XML API JAVA SDK 操作成功会返回每种 API 对应的返回类型，失败会报出异常(CosClientException 和 CosServiception)。异常类型请见后文异常描述。

### 创建 Bucket

新创建一个当前账户下的 COS 中不存在的 Bucket (创建一个新 Bucket )。Bucket 是有限的资源，Bucket 不等同于目录, 且 Bucket 下的文件（Object）数量无限，建议不要创建大量的 Bucket。

#### 方法原型

```java
public Bucket createBucket(CreateBucketRequest createBucketRequest) 
  throws CosClientException, CosServiceException;
```
<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>
#### 参数说明

|         参数名         |         类型          | 默认值  |    参数描述    |
| :----------------- | :----------------- | :-- | :--------|
| createBucketRequest | CreateBucketRequest |  无   | 创建 Bucket 请求 |

| Request 对象成员变量  |           类型            | 默认值  |    设置方法    |             描述             |
| :--------------- | :--------------------- | :-- | :-------- | :------------------------ |
|    bucketName     |         String          |  无   | 构造函数或 set 方法 |    Bucket名称，由数字和小写字母构成     |
|     cannedAcl     | CannedAccessControlList |  无   |   set 方法    | 批量的权限设置，如私有读写, 私有写公有读,公有读写 |
| accessControlList |    AccessControlList    |  无   |   set 方法    |            权限设置            |

#### 成功返回值

| 返回值类型  |                返回值描述                |
| :---- | :---------------------------------|
| Bucket | 有关 Bucket 的描述(如 Bucket 的名称, owner 和创建日期) |

#### 示例

```java
String bucketName = "movie";
CreateBucketRequest createBucketRequest = new CreateBucketRequest(bucketName);
createBucketRequest.setCannedAcl(CannedAccessControlList.PublicReadWrite);
Bucket bucket = cosClient.createBucket(createBucketRequest);
```

### 删除Bucket

在当前账户下的 COS 中删除一个 Bucket，该 Bucket 需为空，即 Bucket 下没有任何的文件（Object）。

#### 方法原型

```java
public void deleteBucket(DeleteBucketRequest deleteBucketRequest)  throws CosClientException, CosServiceException;
```

#### 参数说明

|         参数名         |         类型          | 默认值  |    参数描述    |
| :----------------- | :----------------- | :-- | :-------- |
| deleteBucketRequest | DeleteBucketRequest |  无   | 删除 Bucket 请求 |

| Request 对象成员变量  |   类型   | 默认值  |    设置方法    |         描述          |
| :-------- | :---- | :-- | :-------- | :---------------- |
| bucketName | String |  无   | 构造函数或 set 方法 | Bucket 名称,由数字和小写字母构成 |

#### 成功返回值
该方法无返回值。

#### 示例

```java
String bucketName = "movie";
DeleteBucketRequest deleteBucketRequest = new DeleteBucketRequest(bucketName);
cosClient.deleteBucket(deleteBucketRequest);
```


### 简单文件上传

将本地文件或者已知长度的输入流内容上传到 COS 的 Bucket 中。推荐用于图片类小文件上传(20MB以下), 最大支持文件长度 5GB， 5GB 以上的文件上传请使用分块文件上传方式上传。 

#### 方法原型

```java
public PutObjectResult putObject(PutObjectRequest putObjectRequest)
            throws CosClientException, CosServiceException;
public PutObjectResult putObject(String bucketName, String key, File file)
            throws CosClientException, CosServiceException;
public PutObjectResult putObject(String bucketName, String key, InputStream input,
            ObjectMetadata metadata) throws CosClientException, CosServiceException;
```

#### 参数说明

|       参数名        |       参数类型       | 默认值  |  参数描述  |
| :-------------- | :-------------- | :--| :----|
| putObjectRequest | PutObjectRequest |  无   | 上传文件请求 |

| Request 对象成员变量  |       类型       | 默认值  |    设置方法    |          描述          |
| :-------- | :------------ | :--| :-------- | :----------------- |
| bucketName |     String     |  无   | 构造函数或set方法 |       Bucket 名称       |
|    key     |     String     |  无   | 构造函数或set方法 | COS 的文件路径, 即从 Bucket 开始 |
|    file    |      File      |  无   | 构造函数或set方法 |         本地文件         |
|   input    |  InputStream   |  无   | 构造函数或set方法 |         输入流          |
|  metadata  | ObjectMetadata |  无   | 构造函数或set方法 |        文件的元信息        |

#### 成功返回值

|      返回值类型      |        返回值描述        |
| :------------- | :----------------- |
| PutObjectResult | 文件上传成功后属性信息, 如 ETag |

#### 示例

```java
// 本地文件上传
File localFile = new File("/data/test.txt");
String key = "/aaa.txt";
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);

// 从输入流上传(需提前告知输入流的长度, 否则可能导致oom)
FileInputStream fileInputStream = new FileInputStream(localFile);
ObjectMetadata objectMetadata = new ObjectMetadata();
objectMetadata.setContentLength(500);  // 设置长度为500
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, fileInputStream, objectMetadata);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);
// 关闭输入流...
// ....
```

### 分块文件上传

分块文件上传是通过将文件拆分成多个小块进行上传，多个小块可以并发上传, 最大支持 40TB。
分块文件上传的步骤为:

1. 初始化分块上传，获取 uploadId 。(initiateMultipartUpload)
2. 分块数据上传（可并发）。  (uploadPart)
3. 完成分块上传。 (completeMultipartUpload)

另外在分块文件上传过程中还包含获取已上传分块(listParts)和终止分块上传(abortMultipartUpload)。分块上传的步骤较多，建议使用后文的高级 API 上传方式上传大型文件。

#### 方法原型

```java
// 初始化分块上传
public InitiateMultipartUploadResult initiateMultipartUpload(
    InitiateMultipartUploadRequest request) throws CosClientException, CosServiceException;
// 上传数据分块
public UploadPartResult uploadPart(UploadPartRequest uploadPartRequest)
            throws CosClientException, CosServiceException;
// 完成分块上传
public CompleteMultipartUploadResult completeMultipartUpload(
            CompleteMultipartUploadRequest request) throws CosClientException, CosServiceException;
// 罗列已上传分块
public PartListing listParts(ListPartsRequest request)
            throws CosClientException, CosServiceException;
// 终止分块上传
public void abortMultipartUpload(AbortMultipartUploadRequest request)
            throws CosClientException, CosServiceException;
```

#### 示例

```java
// 初始化分块
InitiateMultipartUploadRequest initRequest =
                new InitiateMultipartUploadRequest(bucketName, key);
InitiateMultipartUploadResult initResponse = cosClient.initiateMultipartUpload(initRequest);
String uploadId = initResponse.getUploadId()
// 上传分块, 最多1000个分块, 分块大小支持为1M * 5G.
// 分块大小设置为4M. 如果总计n个分块, 则1~n-1的分块大小一致, 最后一块小于等于前面的分块大小
List<PartETag> partETags = new ArrayList<PartETag>();
int partNumber = 1;
int partSize = 4 * 1024 * 1024;
// partStream代表part数据的输入流, 流长度为partSize
UploadPartRequest uploadRequest =  new    UploadPartRequest().withBucketName(bucketName).
 withUploadId(uploadId).withKey(key).withPartNumber(partNumber).
  withInputStream(partStream).withPartSize(partSize);  
UploadPartResult uploadPartResult = cosClient.uploadPart(uploadRequest);
String eTag = uploadPartResult.getETag();  // 获取part的Etag
partETags.add(new PartETag(partNumber, eTag));  // partETags记录所有已上传的part的Etag信息
// ... 上传partNumber第2个到第n个分块

// complete 完成分块上传.
CompleteMultipartUploadRequest compRequest = new CompleteMultipartUploadRequest(bucketName, key,
           uploadId, partETags);
CompleteMultipartUploadResult result =  cosClient.completeMultipartUpload(compRequest);

// ListPart用于在完成分块上传前或者终止分块上传前获取uploadId对应的已上传的分块信息, 可以用来构造partEtags
ListPartsRequest listPartsRequest = new ListPartsRequest(bucket, key, uploadId);
do {
      partListing = cosclient.listParts(listPartsRequest);
      for (PartSummary partSummary : partListing.getParts()) {
           partETags.add(new PartETag(partSummary.getPartNumber(), partSummary.getETag()));
      }
      listPartsRequest.setPartNumberMarker(partListing.getNextPartNumberMarker());
} while (partListing.isTruncated());

// abortMultipartUpload 用于终止一个分块上传
AbortMultipartUploadRequest abortMultipartUploadRequest = 
  									new AbortMultipartUploadRequest(bucket, key, uploadId);
cosclient.abortMultipartUpload(abortMultipartUploadRequest);

```

### 下载文件

将指定 Bucket 中的文件（Object）下载到本地或者获取下载文件下载输入流。

#### 方法原型

```java
// 下载文件，并获取输入流
public COSObject getObject(GetObjectRequest getObjectRequest)
            throws CosClientException, CosServiceException;
// 下载文件到本地.
public ObjectMetadata getObject(GetObjectRequest getObjectRequest, File destinationFile)
            throws CosClientException, CosServiceException;
```

#### 参数说明

|       参数名        |       参数类型       | 默认值  |  参数描述   |
| :-------------- | :-------------- | :-- | :----- |
| getObjectRequest | GetObjectRequest |  无   | 下载文件请求  |
| destinationFile  |       File       |  无   | 本地的保存文件 |

| Request 对象成员变量  |   类型   | 默认值  |    设置方法    |          描述          |
| :-------- | :---- | :-- | :-------- | :------------------|
| bucketName | String |  无   | 构造函数或 set 方法 |       Bucket 名称       |
|    key     | String |  无   | 构造函数或 set 方法 | COS 的文件路径，即从 Bucket 开始 |
|   range    | long[] |  无   |   set 方法    |      下载的 range 范围      |

#### 成功返回值

|     返回值类型      |    返回值描述    |
| :------------ | :--------- |
|   COSObject    | 文件的输入流以及元信息 |
| ObjectMetadata |  文件相关的属性信息  |

#### 示例

```java
// 下载文件到本地
File downFile = new File("src/test/resources/len5M_down.txt");
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
ObjectMetadata downObjectMeta = cosClient.getObject(getObjectRequest, downFile);

// 下载文件(获取输入流)
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
COSObject cosObject = cosClient.getObject(getObjectRequest);
COSObjectInputStream cosObjectInput = cosObject.getObjectContent();
```

### 删除文件

删除当前账户下 COS 中 Bucket 上的文件（Object）。

#### 方法原型

```java
// 删除文件
public void deleteObject(DeleteObjectRequest deleteObjectRequest)
            throws CosClientException, CosServiceException;
```

#### 参数说明

|         参数名         |        参数类型         | 默认值  |  参数描述  |
| :----------------- | :----------------- | :-- | :---- |
| deleteObjectRequest | DeleteObjectRequest |  无   | 删除文件请求 |

| Request 对象成员变量  |   类型   | 默认值  |    设置方法    |         描述          |
| :-------- | :---- | :-- | :-------- | :----------------- |
| bucketName | String |  无   | 构造函数或 set 方法 |      Bucket 名称       |
|    key     | String |  无   | 构造函数或 set 方法 | COS 的文件路径, 从 Bucket 开始 |

#### 成功返回值

该方法无返回值。

#### 示例

```java
// 删除当前账户下 COS 中 Bucket 文件
DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest(bucketName, key);
cosClient.deleteObject(deleteObjectRequest);
```


### 获取文件属性

查询获取当前账户下的 COS 中 Bucket 上的文件（Object）属性。

#### 方法原型

```java
// 获取文件属性
public ObjectMetadata getObjectMetadata(GetObjectMetadataRequest getObjectMetadataRequest)
            throws CosClientException, CosServiceException;
```

#### 参数说明

|           参数名            |           参数类型           | 默认值  |   参数描述   |
| :---------------------- | :---------------------- | :--| :------ |
| getObjectMetadataRequest | GetObjectMetadataRequest |  无   | 获取文件属性请求 |

| Request 对象成员变量  |   类型   | 默认值  |    设置方法    |         描述          |
| :-------- | :---- | :-- | :-------- | :----------------- |
| bucketName | String |  无   | 构造函数或 set 方法 |      Bucket 名称       |
|    key     | String |  无   | 构造函数或 set 方法 | COS 的文件路径, 从 Bucket 开始 |

#### 成功返回值

|     返回值类型      |   返回值描述   |
| :------------ | :------- |
| ObjectMetadata | 文件相关的属性信息 |

#### 示例

```java
// 获取文件属性
GetObjectMetadataRequest getObjectMetadataRequest =
                new GetObjectMetadataRequest(bucketName, key);
ObjectMetadata statObjectMeta = cosClient.getObjectMetadata(getObjectMetadataRequest);
```

### 获取文件列表

查询获取当前账户下的 COS 中 Bucket 上的文件（Object）成员列表。

#### 方法原型

```java
// 获取文件列表
public ObjectListing listObjects(ListObjectsRequest listObjectsRequest)
            throws CosClientException, CosServiceException;
```

#### 参数说明

|        参数名         |        参数类型        | 默认值  |   参数描述   |
| :---------------- | :---------------- | :--| :------ |
| listObjectsRequest | ListObjectsRequest |  无   | 获取文件列表请求 |

| Request 对象成员变量 |   类型    | 默认值  |    设置方法    |                    描述                    |
| :-------- | :----- | :-- | :-------- | :-------------------------------------- |
| bucketName | String  |  无   | 构造函数或 set 方法 |                 Bucket 名称                 |
|   prefix   | String  |  " "  | 构造函数或 set 方法 | 标记 list 以 prefix 为前缀的成员，默认不进行限制，即 Bucket 下所有的成员 |
|   marker   | String  |  无   | 构造函数或 set 方法 | 标记 list 的起点位置，第一次为空，后续以上一次 list 的返回值中的 marker |
| delimiter  | String  |  无   | 构造函数或 set 方法 | 分隔符，限制返回的是以 prefix 开头，并以 delimiter 一次出现的结束的路径 |
|  maxKeys   | Integer | 1000 | 构造函数或 set 方法 |           最大返回的成员个数(不得超过 1000)            |

#### 成功返回值

|     返回值类型     |   返回值描述    |
| :----------- | :-------- |
| ObjectListing | 包含 list 的子成员 |

#### 示例

```java
// 获取 Bucket 下成员(设置 delimiter)
ListObjectsRequest listObjectsRequest = new ListObjectsRequest();
listObjectsRequest.setBucketName(bucketName);
// 设置 delimiter 为/, 即获取的是直接成员，不包含目录下的递归子成员
listObjectsRequest.setDelimiter("/");
ObjectListing objectListing = cosClient.listObjects(listObjectsRequest);
List<COSObjectSummary> objectListSummary = objectListing.getObjectSummaries();
```


### 生成签名

COSSigner 提供构造 COS 签名的方法，用于给移动端分发签名，构造下载链接等。

#### 方法原型

```java
// 构造签名
public String buildAuthorizationStr(HttpMethodName methodName, String resourcePath,
            Map<String, String> headerMap, Map<String, String> paramMap, COSCredentials cred);
```

#### 参数说明

|     参数名      |        参数类型         | 默认值  |                  参数描述                  |
| :----------: | :-----------------: | :--: | :------------------------------------: |
|  methodName  |   HttpMethodName    |  无   | http 请求方法(PUT, GET, DELETE, HEAD, POST) |
| resourcePath |       String        |  无   |                  路径地址                  |
|  headerMap   | Map&lt;String, String&gt; |  无   |               要签发的 HTTP头部               |
|   paramMap   | Map&lt;String, String&gt; |  无   |              URL 路径中的参数 KV 对              |
|     cred     |   COSCredentials    |  无   |                  身份信息                  |

#### 成功返回值

| 返回值类型  | 返回值描述 |
| :---- | :--- |
| String |  签名   |

#### 示例

```java
 // 以下用于生成带下载签名的链接
COSSigner signer = new COSSigner();
signer.setSignExpiredTime(1800); // 设置签名有效时间为 1800 秒，默认是 3600 秒
// 生成签名
String origin_auth_str = signer.buildAuthorizationStr(HttpMethodName.GET, key, cred);
// 对签名进行 URL ENCODE
String auth_str = UrlEncoderUtils.encode(origin_auth_str);
StringBuilder strBuilder = new StringBuilder();
strBuilder.append("http://").append(bucketName).append("-").append(appid).append(".")
     .append("ap-beijing-1").append(".myqcloud.com")
     .append(UrlEncoderUtils.encodeEscapeDelimiter(key)).append("?sign=")
```

## 高级 API 文件上传(推荐)

高级 API 由类 TransferManger 通过封装上传以及下载接口，内部有一个线程池，接受用户的上传和下载请求，因此用户可选择异步的提交任务。用户上传或下载文件（Object）推荐使用高级 API 。

```java
// 生成 TransferManager
TransferManager transferManager = new TransferManager(cosClient);
// .....(提交上传下载请求, 如下文所述)
// 关闭 TransferManger
transferManager.shutdownNow();
```

### 上传文件

上传接口根据用户文件的长度自动选择简单上传或分块上传的方式将文件上传到 Bucket 中，降低用户的使用门槛。并且使用分块上传时用户不用关心每一个步骤情况，十分便捷。

#### 方法原型

```java
// 上传文件
public Upload upload(final PutObjectRequest putObjectRequest)
            throws CosServiceException, CosClientException;
```

#### 参数说明

|       参数名        |       参数类型       | 默认值  |  参数描述  |
| :-------------- | :-------------- | :-- | :---- |
| putObjectRequest | PutObjectRequest |  无   | 上传文件请求 |

| Request 对象成员变量  |       类型       | 默认值  |    设置方法    |          描述          |
| :-------- | :------------ | :--| :-------- | :------------------ |
| bucketName |     String     |  无   | 构造函数或 set 方法 |       Bucket 名称       |
|    key     |     String     |  无   | 构造函数或 set 方法 | COS 的文件路径, 即从 Bucket 开始 |
|    file    |      File      |  无   | 构造函数或 set 方法 |         本地文件         |
|   input    |  InputStream   |  无   | 构造函数或 set 方法 |         输入流          |
|  metadata  | ObjectMetadata |  无   | 构造函数或 set 方法 |        文件的元信息        |

#### 成功返回值

| 返回值类型  |      返回值描述      |
| :---- | :------------ |
| Upload | 用于查询上传结果，获取返回值。 |

#### 示例

```java
// 本地文件上传
Upload upload = transferManager.upload(putObjectRequest, localFile);
 // 等待传输结束(如果想同步的等待上传结束，则调用 waitForCompletion)
UploadResult uploadResult = upload.waitForUploadResult();
```

### 下载文件

将指定 Bucket 中的文件（Object）下载到指定的本地文件中。

#### 方法原型

```java
// 下载文件
public Download download(final GetObjectRequest GetObjectRequest, final File file);
```

#### 参数说明

|       参数名        |       参数类型       | 默认值  |  参数描述  |
| :-------------- | :-------------- | :-- | :---- |
| getObjectRequest | GetObjectRequest |  无   | 下载文件请求 |
|       file       |       File       |  无   | 下载目的地  |

| Request 对象成员变量  |       类型       | 默认值  |    设置方法    |          描述          |
| :-------- | :------------ | :-- | :-------- | :------------------ |
| bucketName |     String     |  无   | 构造函数或 set 方法 |      Bucket 名称       |
|    key     |     String     |  无   | 构造函数或 set 方法 |  COS 的文件路径, 即从 Bucket 开始 |
|    file    |      File      |  无   | 构造函数或 set 方法 |         本地文件         |
|   input    |  InputStream   |  无   | 构造函数或 set 方法 |         输入流          |
|  metadata  | ObjectMetadata |  无   | 构造函数或 set 方法 |        文件的元信息        |

#### 成功返回值

|  返回值  |     返回值描述      |
| :------ | :------------ |
| Download | 用于获取上传结果，获取返回值 |

#### 示例

```java
// 下载文件
Download download = transferManager.download(GetObjectRequest, localFile);
 // 等待传输结束(如果想同步的等待上传结束，则调用 waitForCompletion)
download.waitForCompletion();
```
