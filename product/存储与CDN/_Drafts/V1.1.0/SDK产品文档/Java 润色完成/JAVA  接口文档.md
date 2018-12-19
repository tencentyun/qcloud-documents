对象存储服务 XML JAVA SDK 操作成功会返回每种 API 对应的类型，失败会报出异常（CosClientException和CosServiception）。其中 CosClientException 是一些客户端异常，如网络异常，发送请求失败。 CosServiceException 包含了客户请求被服务端处理为失败的原因，如没有权限，访问一个不存在的文件。具体请参考异常类说明。
> 关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

SDK 中使用每一个 API 的正确做法如下所示，为了简要， 后续的 API 范例不再给出捕获异常的范例，仅给出 API 的使用范例。

```java
try {
   String bucketName = "movie";
   String key = "abc/def.jpg";
   cosclient.deleteObject(bucket, key);
} catch (CosClientException cle) {
  // 自定义异常处理比如打印异常等
  log.error("del object failed.", cle);
  // ...
} catch (CosServiceException cse) {
   // 自定义异常处理比如打印异常等
  log.error("del object failed.", cse);
  // ...
}
```

## Bucket API 描述

### Put Bucket
新创建一个 Bucket。Bucket 是有限的资源，Bucket 不等同于目录，且 Bucket 下的文件数量无限，建议不要创建大量的 Bucket。Bucket 创建是低频操作，一般建议在控制台进行创建 Bucket，在 SDK 进行 Object 的操作。

#### 方法原型

```java
public Bucket createBucket(String  bucketName) throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |         参数描述        | 类型   | 
| -------- | ---- | -- | 
| bucketName | Bucket 名字（数字和字母的组合） |String | 

#### 返回值

**成功：**  Bucket 类，包含有关 Bucket 的描述（Bucket 的名称，owner 和创建日期）。

**失败：** 发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
Bucket bucket = cosClient.createBucket(bucketName);
```

### Delete Bucket

删除已清空的 Bucket。

#### 方法原型

```java
 public void deleteBucket(String bucketName) throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |      参数描述         | 类型   | 
| -------- | ---- | -- | 
| bucketName | Bucket 名称，由数字和小写字母构成 |String |

#### 返回值

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
cosClient.deleteBucket(bucketName);
```

### Head Bucket

查询一个 Bucket 是否存在。

#### 方法原型

```java
public boolean doesBucketExist(String bucketName) 
  throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |       参数描述         | 类型   | 
|  -------  |  ----  | ------ |   
| bucketName | Bucket 名称，由数字和小写字母构成 |String |   

#### 返回值

**成功：**   存在返回 true， 否则 false。

**失败：**   发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
boolean bucketExistFlag = cosClient.doesBucketExist(bucketName);
```

### Get Bucket Location

查询一个 Bucket 所在的 Region。

#### 方法原型

```java
public String getBucketLocation(String bucketName) 
  throws CosClientException， CosServiceException;
```

#### 参数说明

|    参数名     |          参数描述         |类型   |  
| ---------- | ------ | ---- |  
| bucketName | Bucket 名称，由数字和小写字母构成 |String |   

#### 返回值

**成功： ** 返回一个 Bucket 所在的 Region。 

**失败：**  发生错误（如 Bucket 不存在），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String location = cosClient.getBucketLocation("movie");
```

### Get Bucket (List Objects)

查询获取 COS 上的文件列表。

#### 方法原型

```java
// 获取文件列表
public ObjectListing listObjects(ListObjectsRequest listObjectsRequest)
            throws CosClientException, CosServiceException;
```

#### 参数说明

|        参数名         |      参数描述   |   参数类型        |  
| ------------------ | ------------------ | ---- |  
| listObjectsRequest | 获取文件列表请求 |ListObjectsRequest |   


| request成员  |     设置方法    |                    描述                    | 类型    |  
| ---------- | ------- | ---- | ---------- | 
| bucketName |  构造函数或 set 方法 |                Bucket 名称                 |String  |  
|   prefix   | 构造函数或 set 方法 | 标记 list 以 prefix 为前缀的成员，默认不进行限制，即 Bucket 下所有的成员。<br>默认值： ""  |String  | 
|   marker   |  构造函数或 set 方法 | 标记 list 的起点位置，第一次为空，后续以上一次 list 的返回值中的 marker |String  
| delimiter  | 构造函数或 set 方法 | 分隔符，限制返回的是以 prefix 开头，并以 delimiter 一次出现的结束的路径 |String  
|  maxKeys   | 构造函数或 set 方法 |           最大返回的成员个数(不得超过 1000)   <br>默认值： 1000          |Integer |  

#### 返回值

**成功：**   返回 ObjectListing 类型， 包含所有的成员， 以及 nextMarker。  

**失败：**   抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
// 获取 bucket 下成员（设置 delimiter）
ListObjectsRequest listObjectsRequest = new ListObjectsRequest();
listObjectsRequest.setBucketName(bucketName);
// 设置 list 的 prefix, 表示 list 出来的文件 key 都是以这个 prefix 开始
listObjectsRequest.setPrefix("");
// 设置 delimiter 为/, 即获取的是直接成员，不包含目录下的递归子成员
listObjectsRequest.setDelimiter("/");
// 设置 marker, (marker 由上一次 list 获取到, 或者第一次 list marker 为空)
listObjectsRequest.setMarker("");
// 设置最多 list 100 个成员,（如果不设置, 默认为 1000 个，最大允许一次 list 1000 个 key）
listObjectsRequest.setMaxKeys(100);

ObjectListing objectListing = cosClient.listObjects(listObjectsRequest);
// 获取下次 list 的 marker
String nextMarker = objectListing.getNextMarker();
// 判断是否已经 list 完, 如果 list 结束, 则 isTruncated 为 false, 否则为 true
boolean isTruncated = objectListing.isTruncated();
List<COSObjectSummary> objectSummaries = objectListing.getObjectSummaries();
for (COSObjectSummary cosObjectSummary : objectSummaries) {
    // 文件路径
    String key = cosObjectSummary.getKey();
    // 获取文件长度
    long fileSize = cosObjectSummary.getSize();
    // 获取文件ETag
    String eTag = cosObjectSummary.getETag();
    // 获取最后修改时间
    Date lastModified = cosObjectSummary.getLastModified();
    // 获取文件的存储类型
    String StorageClassStr = cosObjectSummary.getStorageClass();
}
```

### Set Bucket ACL

设置 Bucket 的访问控制权限列表（Access Control List）。

Set Bucket  ACL 是覆盖操作，会覆盖已有的权限设置。

ACL 包括预定义权限策略（CannedAccessControlList）或者自定义的权限控制（AccessControlList）。两类权限当同时设置时将忽略预定义策略，以自定义策略为主。有关权限细节请参照权限章节。

#### 方法原型

```java
// 方法 1 (设置自定义策略)
public void setBucketAcl(String bucketName, AccessControlList acl)
  throws CosClientException, CosServiceException;
// 方法 2 (设置预定义策略)
public void setBucketAcl(String bucketName, CannedAccessControlList acl) throws CosClientException, CosServiceException;
// 方法 3 (以上两种方法的封装, 包含两种策略设置，如果同时设置以自定定义策略为主)
public void setBucketAcl(SetBucketAclRequest setBucketAclRequest) 
  throws CosClientException, CosServiceException;
```

#### 参数说明

方法3参数同时包含 1 和 2，因此以方法 3 为例进行介绍。

|         参数名         |        参数描述   |   类型          | 
| ------------------- | ------------------- | ---- | 
| setBucketAclRequest | 权限设置请求类 |SetBucketAclRequest | 

| request成员  |           设置方法    |         描述         |  类型            | 
| ---------- | ----------------------- | ---- | ---------- | 
| bucketName |        构造函数或 set 方法 |      Bucket 名称      |  String          |  
|    acl     |  构造函数或 set 方法 |      自定义权限策略       |  AccessControlList    |  
| cannedAcl  | 构造函数或 set 方法 | 预定义策略如公有读、公有读写、私有读 |CannedAccessControlList |  

#### 返回值

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败）， 抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
// 设置自定义 ACL
AccessControlList acl = new AccessControlList();
Owner owner = new Owner();
owner.setId("qcs::cam::uin/2779643970:uin/2779643970");
acl.setOwner(owner);
String id = "qcs::cam::uin/2779643970:uin/734505014";
UinGrantee uinGrantee = new UinGrantee("qcs::cam::uin/2779643970:uin/734505014");
uinGrantee.setIdentifier(id);
acl.grantPermission(uinGrantee, Permission.FullControl);
cosclient.setBucketAcl(bucketName, acl);

// 设置预定义 ACL
// 设置私有读写（默认新建的 bucket 都是私有读写）
cosclient.setBucketAcl(bucketName, CannedAccessControlList.Private);
// 设置公有读私有写
cosclient.setBucketAcl(bucketName, CannedAccessControlList.PublicRead);
// 设置公有读写
cosclient.setBucketAcl(bucketName, CannedAccessControlList.PublicReadWrite);
```

### Get Bucket ACL

查询一个 Bucket 的访问策略 ACL。

#### 方法原型

```java
public AccessControlList getBucketAcl(String bucketName)
       throws CosClientException, CosServiceException
```

#### 参数说明

|    参数名     |      参数描述         |类型   |   
| ---------- | ------ | ---- | 
| bucketName | Bucket 名称，由数字和小写字母构成 |String |  

#### 返回值

**成功**  返回一个 Bucket 的 ACL。 

**失败**  发生错误（如身份认证失败）， 抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
AccessControlList acl = cosclient.getBucketAcl(bucketName);
```

### Set Bucket CORS

设置 Bucket 的跨域访问规则。

#### 方法原型

```java
public void setBucketCrossOriginConfiguration(String bucketName, BucketCrossOriginConfiguration bucketCrossOriginConfiguration);
```

#### 参数说明

|    参数名        |     参数描述     |       类型          | 
| --------------- | ------------ | ---- | 
|     bucketName |  Bucket 名称，由数字和小写字母构成 |      String  | 
| bucketCrossOriginConfiguration |    设置的 Bucket 跨域策略    | BucketCrossOriginConfiguration |

#### 返回值

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
BucketCrossOriginConfiguration bucketCORS = new BucketCrossOriginConfiguration();
List<CORSRule> corsRules = new ArrayList<>();
CORSRule corsRule = new CORSRule();
// 规则名称
corsRule.setId("set-bucket-cors-test");  
// 允许的HTTP方法
corsRule.setAllowedMethods(AllowedMethods.PUT, AllowedMethods.GET, AllowedMethods.HEAD);
corsRule.setAllowedHeaders("x-cos-grant-full-control");
corsRule.setAllowedOrigins("http://mail.qq.com", "http://www.qq.com",
        "http://video.qq.com");
corsRule.setExposedHeaders("x-cos-request-id");
corsRule.setMaxAgeSeconds(60);
corsRules.add(corsRule);
bucketCORS.setRules(corsRules);
cosclient.setBucketCrossOriginConfiguration(bucketName, bucketCORS);
```

### Get Bucket CORS

获取 Bucket 的跨域访问规则。

#### 方法原型

```java
public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(String bucketName)
     throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |         参数描述         | 类型   | 
| ---------- | ------ | ---- |
| bucketName | Bucket 名称，由数字和小写字母构成 |String |  

#### 返回值

**成功：**  返回 Bucket 的跨域规则。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
BucketCrossOriginConfiguration corsGet = cosclient.getBucketCrossOriginConfiguration("movie");
List<CORSRule> corsRules = corsGet.getRules();
for (CORSRule rule : corsRules) {
    List<AllowedMethods> allowedMethods = rule.getAllowedMethods();
    List<String> allowedHeaders = rule.getAllowedHeaders();
    List<String> allowedOrigins = rule.getAllowedOrigins();
    List<String> exposedHeaders = rule.getExposedHeaders();
    int maxAgeSeconds = rule.getMaxAgeSeconds();
}
```

### Delete Bucket CORS

删除 Bucket 的跨域访问规则。

#### 方法原型

```java
public void deleteBucketCrossOriginConfiguration(String bucketName)
     throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |        参数描述         |类型   | 
| ---------- | ------ | ---- | 
| bucketName | Bucket名称，由数字和小写字母构成 | String | 

#### 返回值

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
cosclient.deleteBucketCrossOriginConfiguration(bucketName);
```

### Set Bucket LifeCycle

删除 Bucket 的生命周期规则。

#### 方法原型

```java
public void setBucketLifecycleConfiguration(String bucketName, BucketLifecycleConfiguration bucketLifecycleConfiguration) throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |      参数描述         |类型   | 
| ---------- | ------ | ---- | 
| bucketName |  Bucket 名称，由数字和小写字母构成 |String | 

#### 返回值

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
List<Rule> rules = new ArrayList<>();
// 规则1  30 天后删除路径以 hongkong_movie/ 为开始的文件
Rule deletePrefixRule = new Rule();
deletePrefixRule.setId("delete prefix xxxy after 30 days");
deletePrefixRule
        .setFilter(new LifecycleFilter(newLifecyclePrefixPredicate("hongkong_movie/")));
// 文件上传或者变更后, 30天后删除
deletePrefixRule.setExpirationInDays(30);
// 设置规则为生效状态
deletePrefixRule.setStatus(BucketLifecycleConfiguration.ENABLED);

// 规则2  20 天后沉降到低频，一年后删除
Rule standardIaRule = new Rule();
standardIaRule.setId("standard_ia transition");
standardIaRule.setFilter(new LifecycleFilter(new LifecyclePrefixPredicate("standard_ia/")));
List<Transition> standardIaTransitions = new ArrayList<>();
Transition standardTransition = new Transition();
standardTransition.setDays(20);
standardTransition.setStorageClass(StorageClass.Standard_IA.toString());
standardIaTransitions.add(standardTransition);
standardIaRule.setTransitions(standardIaTransitions);
standardIaRule.setStatus(BucketLifecycleConfiguration.ENABLED);
standardIaRule.setExpirationInDays(365);
		
// 将两条规则添加到策略集合中
rules.add(deletePrefixRule);
rules.add(standardIaRule);

// 生成 bucketLifecycleConfiguration
BucketLifecycleConfiguration bucketLifecycleConfiguration =
        new BucketLifecycleConfiguration();
bucketLifecycleConfiguration.setRules(rules);

String bucketName = "movie";
SetBucketLifecycleConfigurationRequest setBucketLifecycleConfigurationRequest =
      new SetBucketLifecycleConfigurationRequest(bucketName, bucketLifecycleConfiguration);

// 设置生命周期
cosclient.setBucketLifecycleConfiguration(setBucketLifecycleConfigurationRequest);
```

### Get Bucket LifeCycle

获取 Bucket 的生命周期规则。

#### 方法原型

```java
public BucketLifecycleConfiguration getBucketLifecycleConfiguration(String bucketName)
            throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |         参数描述         | 类型   | 
| ---------- | ------ | ---- | 
| bucketName |  Bucket 名称，由数字和小写字母构成 |String |  

#### 返回值

**成功：**  返回 BucketLifecycleConfiguration 类， 包含bucket的生命周期规则。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
BucketLifecycleConfiguration queryLifeCycleRet =
        cosclient.getBucketLifecycleConfiguration(bucketName);
List<Rule> ruleLists = queryLifeCycleRet.getRules();
```

### Delete Bucket LifeCycle

删除清空 Bucket 的生命周期规则。

#### 方法原型

```java
public void deleteBucketLifecycleConfiguration(String bucketName)
         throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |      参数描述         | 类型   | 
| ---------- | ------ | ---- |
| bucketName | Bucket名称，由数字和小写字母构成 |String |  

#### 返回值

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
cosclient.deleteBucketLifecycleConfiguration(bucketName);
```

## Object API 描述

### PUT Object（上传 Object）

将本地文件或者已知长度的输入流内容上传到 COS。适用于图片类小文件上传（20 MB 以下），最大支持 5 GB（含），5 GB 以上请使用分块上传。

#### 方法原型

```java
// 方法1  将本地文件上传到 COS
public PutObjectResult putObject(String bucketName, String key, File file)
            throws CosClientException, CosServiceException;
// 方法2  输入流上传到 COS
public PutObjectResult putObject(String bucketName, String key, InputStream input,
            ObjectMetadata metadata) throws CosClientException, CosServiceException;
// 方法3  对以上两个方法的包装, 支持更细粒度的参数控制, 如 content-type,  content-disposition 等
public PutObjectResult putObject(PutObjectRequest putObjectRequest)
            throws CosClientException, CosServiceException;
```

#### 参数说明

|       参数名        |    参数描述  |    参数类型       |
| ---------------- | ---------------- | ---- | 
| putObjectRequest | 上传文件请求 |PutObjectRequest | 

| request成员  |      设置方法    |          描述          |  类型       | 
| ---------- | -------------- | ---- | ---------- | 
| bucketName |  构造函数或 set 方法 |       Bucket 名称       |    String     |
|    key     |    构造函数或 set 方法 | COS 的文件路径，即从 Bucket 开始 | String     |  
|    file    |     构造函数或 set 方法 |         本地文件         | File      |  
|   input    | 构造函数或 set 方法 |         输入流          | InputStream   |  
|  metadata  | 构造函数或 set 方法 |        文件的元信息        |ObjectMetadata |  

#### 返回值

**成功：**  PutObjectResult，包含文件的 ETag 等信息。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
// 方法1 本地文件上传
File localFile = new File("/data/test.txt");
String key = "/aaa.txt";
PutObjectResult putObjectResult = cosClient.putObject(bucketName, key, localFile);
String etag = putObjectResult.getETag();  // 获取文件的etag

// 方法2 从输入流上传(需提前告知输入流的长度, 否则可能导致 oom)
FileInputStream fileInputStream = new FileInputStream(localFile);
ObjectMetadata objectMetadata = new ObjectMetadata();
// 设置输入流长度为 500
objectMetadata.setContentLength(500);  
// 设置 Content type, 默认是 application/octet-stream
objectMetadata.setContentType("application/pdf");
PutObjectResult putObjectResult = cosClient.putObject(bucketName, key, fileInputStream, objectMetadata);
String etag = putObjectResult.getETag();
// 关闭输入流...

// 方法3 提供更多细粒度的控制, 常用的设置如下
// 1 storage-class 存储类型, 用于设置标准(默认)、低频、近线
// 2 content-type, 对于本地文件上传, 默认根据本地文件的后缀进行映射, 如 jpg 文件映射 为image/jpeg
//   对于流式上传 默认是 application/octet-stream
// 3 上传的同时制定权限(也可通过调用 API set object acl 来设置)
File localFile = new File("/data/dog.jpg");
String key = "/mypic.jpg";
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, file);
// 设置存储类型为低频
putObjectRequest.setStorageClass(StorageClass.Standard_IA);
// 设置自定义属性(如 content-type, content-disposition 等)
ObjectMetadata objectMetadata = new ObjectMetadata();
// 设置 Content type, 默认是 application/octet-stream
objectMetadata.setContentType("image/jpeg");
putObjectRequest.setMetadata(objectMetadata);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);
String etag = putObjectResult.getETag();  // 获取文件的 etag
```

#### 分块文件上传

分块文件上传是通过将文件拆分成多个小块进行上传，多个小块可以并发上传，最大支持 40 TB。

分块文件上传的步骤为：

1. 初始化分块上传，获取 uploadid。（initiateMultipartUpload）
2. 分块数据上传（可并发）。（uploadPart）
3. 完成分块上传。（completeMultipartUpload）

另外还包可以获取已上传分块（listParts），终止分块上传（abortMultipartUpload）。分块上传的步骤与门槛较多，建议使用后文封装的高级 API 上传。

#### 方法原型

```java
// 方法1 初始化分块上传
public InitiateMultipartUploadResult initiateMultipartUpload(
    InitiateMultipartUploadRequest request) throws CosClientException, CosServiceException;
// 方法2 上传数据分块
public UploadPartResult uploadPart(UploadPartRequest uploadPartRequest)
            throws CosClientException, CosServiceException;
// 方法3 完成分块上传
public CompleteMultipartUploadResult completeMultipartUpload(
            CompleteMultipartUploadRequest request) throws CosClientException, CosServiceException;
// 方法4 罗列已上传分块
public PartListing listParts(ListPartsRequest request)
            throws CosClientException, CosServiceException;
// 方法5 终止分块上传
public void abortMultipartUpload(AbortMultipartUploadRequest request)
            throws CosClientException, CosServiceException;
```

#### 返回值

#### 方法1 （initiateMultipartUpload）

**成功：**  返回 InitiateMultipartUploadResult 类，包含后续分块上传必须使用的 upload id。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者CosServiceException。 具体请参照异常类说明。

#### 方法2 （uploadPart）

**成功：**  返回 UploadPartResult，包含该分块的 Etag 和 partNumber 。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者CosServiceException。 具体请参照异常类说明。

#### 方法3 （completeMultipartUpload）

**成功：**  返回 CompleteMultipartUploadResult，包含全文的Etag。 

**失败：**  发生错误（如身份认证失败）， 抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。

#### 方法4 （listParts）

**成功：**  返回 PartListing， 包含每一分块的 ETag 和编号，以及下一次 list 的起点 marker。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者CosServiceException。具体请参照异常类说明。

#### 方法5 (abortMultipartUpload)

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
// 初始化分块
InitiateMultipartUploadRequest initRequest =
                new InitiateMultipartUploadRequest(bucketName, key);
InitiateMultipartUploadResult initResponse = cosClient.initiateMultipartUpload(initRequest);
String uploadId = initResponse.getUploadId()
// 上传分块, 最多 1000 个分块, 分块大小支持为 1M * 5G.
// 分块大小设置为 4M. 如果总计 n 个分块, 则 1~n-1 的分块大小一致, 最后一块小于等于前面的分块大小
List<PartETag> partETags = new ArrayList<PartETag>();
int partNumber = 1;
int partSize = 4 * 1024 * 1024;
// partStream 代表 part 数据的输入流, 流长度为 partSize
UploadPartRequest uploadRequest =  new    UploadPartRequest().withBucketName(bucketName).
 withUploadId(uploadId).withKey(key).withPartNumber(partNumber).
  withInputStream(partStream).withPartSize(partSize);  
UploadPartResult uploadPartResult = cosClient.uploadPart(uploadRequest);
String eTag = uploadPartResult.getETag();  // 获取 part 的 Etag
partETags.add(new PartETag(partNumber, eTag));  // partETags 记录所有已上传的 part 的 Etag 信息
// ... 上传 partNumber 第 2 个到第 n 个分块

// complete 完成分块上传.
CompleteMultipartUploadRequest compRequest = new CompleteMultipartUploadRequest(bucketName, key,
           uploadId, partETags);
CompleteMultipartUploadResult result =  cosClient.completeMultipartUpload(compRequest);

// ListPart 用于在 complete 分块上传前或者 abort 分块上传前获取 uploadId 对应的已上传的分块信息, 可以用来构造 partEtags
ListPartsRequest listPartsRequest = new ListPartsRequest(bucket, key, uploadId);
do {
      partListing = cosclient.listParts(listPartsRequest);
      for (PartSummary partSummary : partListing.getParts()) {
           partETags.add(new PartETag(partSummary.getPartNumber(), partSummary.getETag()));
      }
      listPartsRequest.setPartNumberMarker(partListing.getNextPartNumberMarker());
} while (partListing.isTruncated());

// abortMultipartUpload 用于终止一个还未 complete 的分块上传
AbortMultipartUploadRequest abortMultipartUploadRequest = 
  									new AbortMultipartUploadRequest(bucket, key, uploadId);
cosclient.abortMultipartUpload(abortMultipartUploadRequest);
```

### Get Object

文件下载到本地或者获取下载文件下载输入流。

#### 方法原型

```java
String bucketName = "movie";
// 方法1 下载文件，并获取输入流
public COSObject getObject(GetObjectRequest getObjectRequest)
            throws CosClientException, CosServiceException;
// 方法2 下载文件到本地.
public ObjectMetadata getObject(GetObjectRequest getObjectRequest, File destinationFile)
            throws CosClientException, CosServiceException;
```

#### 参数说明

|       参数名        |    参数描述   |    参数类型       | 
| ---------------- | ---------------- | ---- | 
| getObjectRequest |下载文件请求  | GetObjectRequest | 
| destinationFile  |  本地的保存文件 |     File       |  

| request成员  |     设置方法    |          描述          | 类型   | 
| ---------- | ------ | ---- | ---------- | 
| bucketName | 构造函数或 set 方法 |      Bucket 名称       |String | 
|    key     |  构造函数或 set 方法 | COS 的文件路径，即从 Bucket 开始 |String | 
|   range    | set方法    |      下载的 range 范围      | Long[] |  

#### 返回值

#### 方法1 （获取下载输入流）

**成功：**  返回 COSObject 类，包含输入流以及文件属性。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 方法2 (下载文件到本地)

**成功：**  返回文件的属性 objectMetadata，包含文件的自定义头和 content-type 等属性

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

```java
String bucketName = "movie";
String key = "abc/def.jpg";
// 方法1 获取下载输入流
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
COSObject cosObject = cosClient.getObject(getObjectRequest);
COSObjectInputStream cosObjectInput = cosObject.getObjectContent();

// 方法2 下载文件到本地
File downFile = new File("src/test/resources/mydown.txt");
GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, key);
ObjectMetadata downObjectMeta = cosClient.getObject(getObjectRequest, downFile);
```

### Delete Object

删除 COS 上的文件。

#### 方法原型

```java
// 删除文件
public void deleteObject(String bucketName, String key)
            throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |        参数描述         | 类型   | 
| ---------- | ------ | ---- | 
| bucketName | Bucket 名称，由数字和小写字母构成 |String | 
|    key     |     文件路径         |String |  

#### 返回值

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
// 删除 COS 文件
String bucketName = "movie";
String key = "abc/def.jpg";
cosclient.deleteObject(bucket, key);
```

### Head Object

查询获取 COS 上的文件属性。

#### 方法原型

```java
// 获取文件属性
public ObjectMetadata getObjectMetadata(String bucketName, String key)
  throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |         参数描述         | 类型   | 
| ---------- | ------ | ---- | 
| bucketName | Bucket 名称，由数字和小写字母构成 |String |  
|    key     |      文件路径         |String |  

#### 返回值

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
// 获取COS文件属性
String bucketName = "movie";
String key = "abc/def.jpg";
ObjectMetadata objectMetadata = cosclient.getObjectMetadata(bucketName, key);
```

### Put Object Copy

拷贝 Object 到新的路径或者新的 Bucket。支持跨园区跨账号跨 Bucket 拷贝，需要拥有对源文件的读取权限以及目的文件的写入权限。

#### 方法原型

```java
// 获取文件属性
public CopyObjectResult copyObject(CopyObjectRequest copyObjectRequest)
      throws CosClientException, CosServiceException
```

#### 参数说明

|        参数名        |     参数描述  |   参数类型        | 
| ----------------- | ----------------- | ---- | 
| copyObjectRequest | 下载文件请求 |CopyObjectRequest |  

|          参数名          |              参数描述               | 类型   |  
| --------------------- | ------ | ---------------------------------- | -------------------------------- |
|      sourceAppid      | 源 APPID。默认值：和当前appid一致，表示同账号拷贝 |String |   
|  sourceBucketRegion   |  源 Bucket Region 。默认值：与当前 clientconfig 的 region 一致, 表示统一园区拷贝       |String | 
|   sourceBucketName    |         源 Bucket 名             |String |      
|       sourceKey       |            源文件路径               |String |              
|    sourceVersionId    | 源文件 version id （适用于开启了多版本的源 Bucket）。默认值：源文件当前最新版本  |String |    
| destinationBucketName |          目的 Bucket 名             |String |     
|    destinationKey     |              目的文件路径              |String |    
|     storageClass      |     拷贝的目的文件的存储类型（标准，低频，近线） 默认值： 标准     |String |   

#### 返回值

**成功：**  返回 CopyObjectResult，包含新文件的 Etag 等信息。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
// 同园区同账号拷贝
String srcBucketName = "movie";
String destBucketName = "movie";
String srcKey = "abc/def.jpg";
String destKey = "abc/def_cp.jpg";
CopyObjectRequest copyObjectRequest =
        new CopyObjectRequest(bucket, srcKey, bucket, destKey);
// 设置存储类型为低频, 默认是标准存储
copyObjectRequest.setStorageClass(StorageClass.Standard_IA);
CopyObjectResult copyObjectResult = cosclient.copyObject(copyObjectRequest);

// 跨账号跨园区拷贝（需要拥有对源文件的读取权限以及目的文件的写入权限）
String srcAppid = "12511000";
String srcRegion = "ap-guangzhou";
copyObjectRequest = new CopyObjectRequest(srcAppid, srcRegion, srcBucketName, srcKey, destBucketName, destKey);
CopyObjectResult copyObjectResult = cosclient.copyObject(copyObjectRequest);
```

### Set Object ACL

设置 Object 的访问控制权限列表（Access Control List）。Set Object ACL 是覆盖操作，会覆盖已有的权限设置。

ACL包括预定义权限策略（CannedAccessControlList）或者自定义的权限控制（AccessControlList）。两类权限当同时设置时将忽略预定义策略，以自定义策略为主。有关权限细节请参照权限章节。

#### 方法原型

```java
// 方法1 (设置自定义策略)
public void setObjectAcl(String bucketName, String key, AccessControlList acl)
       throws CosClientException, CosServiceException
// 方法2 (设置预定义策略)
public void setObjectAcl(String bucketName, String key, CannedAccessControlList acl)
       throws CosClientException, CosServiceException
// 方法3 (以上两种方法的封装, 包含两种策略设置，如果同时设置以自定定义策略为主)
public void setObjectAcl(SetObjectAclRequest setObjectAclRequest)
  throws CosClientException, CosServiceException;
```

#### 参数说明

方法 3 参数同时包含 1 和 2，因此以方法 3 为例进行介绍。

|         参数名         |    参数描述   |     类型          |  
| ------------------- | ------------------- | ---- |  
| SetObjectAclRequest | 权限设置请求类 |setObjectAclRequest |   

| request成员  |            设置方法    |         描述         | 类型            |  
| ---------- | ----------------------- | ---- | ---------- |  
| bucketName |       构造函数或 set 方法 |      Bucket 名称      |  String          | 
|    key     |         构造函数或 set 方法 |      文件路径 Key       |String          |   
|    acl     |  构造函数或 set 方法 |      自定义权限策略       |  AccessControlList    |   
| cannedAcl  |  构造函数或 set 方法 | 预定义策略如公有读、公有读写、私有读 |CannedAccessControlList |  


#### 返回值

**成功：**  无返回值。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
String key = "abc/def.jpg";
// 设置自定义 ACL
AccessControlList acl = new AccessControlList();
Owner owner = new Owner();
owner.setId("qcs::cam::uin/2779643970:uin/2779643970");
acl.setOwner(owner);
String id = "qcs::cam::uin/2779643970:uin/734505014";
UinGrantee uinGrantee = new UinGrantee("qcs::cam::uin/2779643970:uin/734505014");
uinGrantee.setIdentifier(id);
acl.grantPermission(uinGrantee, Permission.FullControl);
cosclient.setObjectAcl(buckeName, key, acl);

// 设置预定义 ACL
// 设置私有读写（Object的权限默认集成 Bucket的）
cosclient.setObjectAcl(buckeName, key, CannedAccessControlList.Private);
// 设置公有读私有写
cosclient.setObjectAcl(buckeName, key, CannedAccessControlList.PublicRead);
// 设置公有读写
cosclient.setObjectAcl(buckeName, key, CannedAccessControlList.PublicReadWrite);
```

### Get Object ACL

查询一个 Object 的访问策略 ACL

#### 方法原型

```java
public AccessControlList getObjectAcl(String bucketName, String key)
  throws CosClientException, CosServiceException;
```

#### 参数说明

|    参数名     |       参数描述         | 类型   |  
| ---------- | ------ | ---- |  
| bucketName | Bucket 名称，由数字和小写字母构成 |String |   
|    key     |         文件路径         |String |   

#### 返回值

**成功：**  返回一个 Object 所在的 ACL

**失败：**  发生错误（如身份认证失败）， 抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
String key = "abc/def.jpg";
AccessControlList acl = cosclient.getObjectAcl(bucketName, key);
```

## 签名生成

COSSigner 提供构造 COS 签名的方法，用于给移动端分发签名，构造下载链接等。

#### 方法原型

```java
// 构造签名
public String buildAuthorizationStr(HttpMethodName methodName, String resourcePath,
            Map<String, String> headerMap, Map<String, String> paramMap, COSCredentials cred);
```

#### 参数说明

|     参数名      |                        参数描述                  |参数类型         |  
| ------------ | ------------------- | ---- |  
|  methodName  |    http 请求方法（PUT，GET，DELETE，HEAD，POST） |HttpMethodName    |  
| resourcePath |                 路径地址                  |    String        |   
|  headerMap   |            要签发的 HTTP 头部               | Map&lt;String, String> |   
|   paramMap   |            URL 路径中的参数 KV 对              | Map&lt;String, String> |   
|     cred     |                 身份信息                  |COSCredentials    |   

#### 返回值

签名字符串

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
     .append(UrlEncoderUtils.encodeEscapeDelimiter(key)).append("?sign=").append(auth_str);
```

## 高级 API 文件上传(推荐)

高级 API 由类 TransferManger 通过封装上传以及下载接口，内部有一个线程池，接受用户的上传和下载请求，因此用户可选择异步的提交任务。

```java
// 生成 TransferManager
TransferManager transferManager = new TransferManager(cosClient);
// .....(提交上传下载请求, 如下文所属)
// 关闭 TransferManger
transferManager.shutdownNow();
```

### 上传文件

上传接口根据用户文件的长度自动选择简单上传以及分块上传， 降低用户的使用门槛。用户不用关心分块上传的每个步骤。

#### 方法原型

```java
// 上传文件
public Upload upload(final PutObjectRequest putObjectRequest)
            throws CosServiceException, CosClientException;
```

#### 参数说明

|       参数名        |      参数描述  |  参数类型       |  
| ---------------- | ---------------- | ---- |  
| putObjectRequest | 上传文件请求 |PutObjectRequest |   

| request成员  |   设置方法    |          描述          |       类型       |  
| ---------- | -------------- | ---- | ---------- |  
| bucketName |    构造函数或 set 方法 |      Bucket 名称       | String     |   
|    key     |    构造函数或 set 方法 | COS 的文件路径，即从 Bucket 开始 | String     |  
|    file    |     构造函数或 set 方法 |         本地文件         | File      |   
|   input    | 构造函数或 set 方法 |         输入流          | InputStream   |   
|  metadata  |构造函数或 set 方法 |        文件的元信息        | ObjectMetadata |   

#### 返回值

**成功：**  返回 Upload，可以查询上传进度，也可同步的等待上传结束。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
String key = "/mypic.jpg";
File localFile = new File("/data/dog.jpg");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, file);
// 本地文件上传
Upload upload = transferManager.upload(putObjectRequest);
 // 等待传输结束（如果想同步的等待上传结束，则调用 waitForCompletion）
UploadResult uploadResult = upload.waitForUploadResult();
```


### 下载文件

接口根据用户文件的长度自动选择简单上传以及分块上传， 降低用户的使用门槛。用户不用关心分快上传的每个步骤。

#### 方法原型

```java
// 下载文件
public Download download(final GetObjectRequest GetObjectRequest, final File file);
```

#### 参数说明

|       参数名        |       参数描述  | 参数类型       |  
| ---------------- | ---------------- | ---- |  
| getObjectRequest | 下载文件请求 | GetObjectRequest |   
|       file       |     下载目的地  |   File       |   

| request成员  |         设置方法    |          描述          | 类型       |  
| ---------- | -------------- | ---- | ---------- |  
| bucketName |   构造函数或 set 方法 |       Bucket名称       |  String     |   
|    key     |     构造函数或 set 方法 | COS 的文件路径，即从 Bucket 开始 |String     |   
|    file    |     构造函数或 set 方法 |         本地文件         | File      |   
|   input    |  构造函数或 set 方法 |         输入流          |InputStream   |   
|  metadata  |  构造函数或 set 方法 |        文件的元信息        |ObjectMetadata |   

#### 返回值

**成功：**  返回 Download，可以查询下载进度，也可同步的等待下载结束。

**失败：**  发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。

#### 示例

```java
String bucketName = "movie";
String key = "/mypic.jpg";
File localDownFile = new File("/data/dog.jpg");
GetObjectRequest getObjectRequest = new GetObjectRequest(bucket, key);
// 下载文件
Download download = transferManager.download(getObjectRequest, localDownFile);
 // 等待传输结束（如果想同步的等待上传结束，则调用 waitForCompletion）
download.waitForCompletion();
```

## 权限设置

COS 中的权限通过 SET/GET Object ACL 以及 SET/GET Bucket ACL 来进行设置与获取。主要的两个类为 AccessControlList 以及 CannedAccessList 来设置与获取。 以下是两个类的详细说明：

### AccessControlList

自定义访问控制策略, 用于设置对某个用户的策略控制。

AccessControlList 类成员

|     成员名     |        描述          |类型   |    
| ----------- | ------ | ------------------- |
| List&lt;Grant> |   包含所有要授权的信息      |数组   |     
|    owner    | 表示 Object 或者 Owner 的拥有者 |Owner类 | 

Grant类成员

|    成员名     |           描述            |  类型     |   
| ---------- | ---------- | ----------------------- |
|  grantee   |       被授权人的身份信息        | Grantee   |  
| permission | 被授权的权限信息（如可读，可写，可读可写） |Permission | 

Owner类成员

|     成员名     |         描述        |类型   | 
| ----------- | ------ | --------------- |
|     id      |    拥有者的身份信息     |String | 
| displayname | 拥有者的名字（目前和 id 相同） |String | 

#### 示例

```
// 权限信息中身份信息有格式要求, 对于根账户与子账户的范式如下：
// 下面的 root_uin 和 sub_uin 都必须是有效的 QQ 号
// 根账户 qcs::cam::uin/<root_uin>:uin/<root_uin> 表示授予根账户 root_uin 这个用户(即前后填的 uin 一样)
//  如 qcs::cam::uin/2779643970:uin/2779643970
// 子账户 qcs::cam::uin/<root_uin>:uin/<sub_uin> 表示授予 root_uin 的子账户 sub_uin 这个客户
//  如 qcs::cam::uin/2779643970:uin/73001122 

AccessControlList acl = new AccessControlList();
Owner owner = new Owner();
// 设置 owner 的信息, owner 只能是根账户
owner.setId("qcs::cam::uin/2779643970:uin/2779643970");
acl.setOwner(owner);

// 授权给根账户 73410000 可读可写权限
UinGrantee uinGrantee1 = new UinGrantee("qcs::cam::uin/73410000:uin/73410000");
acl.grantPermission(uinGrantee1, Permission.FullControl);
// 授权给 2779643970 的子账户 72300000 可读权限
UinGrantee uinGrantee2 = new UinGrantee("qcs::cam::uin/2779643970:uin/72300000");
acl.grantPermission(uinGrantee2, Permission.Read);
// 授权给 2779643970 的子账户 7234444 可写权限
UinGrantee uinGrantee3 = new UinGrantee("qcs::cam::uin/7234444:uin/7234444");
acl.grantPermission(uinGrantee3, Permission.Write);

// 设置 object 的 acl
cosclient.setObjectAcl(bucket, key, acl);
```

### CannedAccessControlList

CannedAccessControlList 表示预设的策略，针对的是所有人。是一个枚举类，枚举值如下所示。

|       枚举值       |             描述             |
| --------------- | -------------------------- |
|     Private     |     私有读写（仅有 owner 可以读写）      |
|   PublicRead    | 公有读私有写（ owner 可以读写， 其他客户可以读） |
| PublicReadWrite |      公有读写（即所有人都可以读写）     |



## 异常说明

SDK 失败时，抛出的异常皆是 RuntimeExcpetion， 目前 SDK 常见的异常有 CosClientException， CosServiceException 和 IllegalArgumentException。

### CosClientException

客户端异常，  用于指因为客户端原因导致无法和服务端完成正常的交互而导致的失败， 如客户端无法连接到服务端，无法解析服务端返回的数据， 读取本地文件发生 IO 异常等。CosClientException 集成自 RuntimeException，没有自定义的成员变量， 使用方法同 RuntimeException。

### CosServiceException

CosServiceException 服务异常， 用于指交互正常完成，但是操作失败的场景。例如客户端访问一个不存在 Bucket， 删除一个不存在的文件，没有权限进行某个操作， 服务端故障异常等。CosServiceException 包含了服务端返回的状态码， requestid， 出错明细等。捕获异常后， 建议对整个异常进行打印， 异常包含了必须的排查因素。以下是异常成员变量的描述：

|  request 成员   |                     描述                    | 类型     |  
| ------------ | --------- | ---------------------------------------- |
|  requestId   |        请求ID， 用于表示一个请求， 对于排查问题十分重要        |String   |  
|   traceId    |               辅助排查问题的 ID，                | String   |  
|  statusCode  |  response 的 status 状态码， 4xx 是指请求因客户端而失败， 5xx 是服务端异常导致的失败。 | String   |
|  errorType   | 枚举类， 表示异常的种类， 分为Client， Service， Unknown |ErrorType | 
|  errorCode   |         请求失败时 body 返回的 Error Code          | String   |  
| errorMessage |        请求失败时 body 返回的 Error Message         |String   |  
