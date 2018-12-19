# 开发准备

## 相关资源

COS JAVA SDK GitHub地址 [github项目](https://github.com/tencentyun/cos-java-sdk-v5)

## 环境依赖

JDK 1.7, 1.8. 

JDK安装方式请参考 [JAVA安装与配置](https://cloud.tencent.com/document/product/436/10865)

## 安装SDK

- maven安装

pom.xml 添加依赖

```xml
<dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cos_api</artifactId>
            <version>5.2.0</version>
</dependency>
```

- 源码安装

从[github](https://github.com/tencentyun/cos-java-sdk-v5)下载源码, 通过maven导入。比如eclipse，选择File->Import->maven->Existing Maven Projects

## 卸载SDK

删除pom依赖或源码

# 快速入手

```java
// 1 初始化身份信息
COSCredentials cred = new BasicCOSCredentials("1250000", "AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosClient = new COSClient(cred, clientConfig);
// 操作API， 如下文所述.或者参照Demo(https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/Demo.java)
```

# API 调动方法描述

COS XML API  JAVA SDK操作成功会返回每种API对应的类型，失败会报出异常(CosClientException和CosServiception)。其中CosClientException是一些客户端异常，如网络异常，发送请求失败。 CosServiceException包含了客户请求被服务端处理为失败的原因，如没有权限，访问一个不存在的文件。具体请参考异常类说明。

SDK中使用每一个API的正确做法如下所示, 后续的API范例不再给出捕获异常的范例, 进给出API的使用范例.

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

## BUCKET API 描述

## Put Bucket

新创建一个bucket。bucket是有限的资源，bucket不等同于目录, 且bucket下的文件数量无限，建议不要创建大量的bucket. bucket创建是低频操作，一般建议在控制台进行创建bucket，在SDK进行object的操作。

### 方法原型

```java
public Bucket createBucket(String  bucketName) throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述        |
| :--------: | :----: | :--: | :----------------: |
| bucketName | String |  无   | bucket名字(数字和字母的组合) |

### 返回值

成功  Bucket   有关bucket的描述(bucket的名称, owner和创建日期)

失败 CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
Bucket bucket = cosClient.createBucket("movie");
```



## Delete Bucket

删除已清空的bucket

### 方法原型

```java
 public void deleteBucket(String bucketName) throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |

### 返回值

成功  Bucket   有关bucket的描述(bucket的名称, owner和创建日期)

失败  返回异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
cosClient.deleteBucket("movie");
```



## Head Bucket

查询一个bucket是否存在

### 方法原型

```java
public boolean doesBucketExist(String bucketName) 
  throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |

### 返回值

存在返回true, 否则false。发生错误(如身份认证失败), 抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
boolean bucketExistFlag = cosClient.doesBucketExist("movie");
```



## Get Bucket Location

查询一个bucket所在的region

### 方法原型

```java
public String getBucketLocation(String bucketName) 
  throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |

### 返回值

返回一个bucket所在的region, 或者(如bucket不存在)抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
String location = cosClient.getBucketLocation("movie");
```



## Get Bucket (List Objects)

查询获取COS上的文件列表

### 方法原型

```java
// 获取文件列表
public ObjectListing listObjects(ListObjectsRequest listObjectsRequest)
            throws CosClientException, CosServiceException;
```

### 参数说明

|        参数名         |        参数类型        | 默认值  |   参数描述   |
| :----------------: | :----------------: | :--: | :------: |
| listObjectsRequest | ListObjectsRequest |  无   | 获取文件列表请求 |

| request成员  |   类型    | 默认值  |    设置方法    |                    描述                    |
| :--------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String  |  无   | 构造函数或set方法 |                 bucket名称                 |
|   prefix   | String  |  ""  | 构造函数或set方法 | 标记list以prefix为前缀的成员，默认不进行限制，即bucket下所有的成员 |
|   marker   | String  |  无   | 构造函数或set方法 | 标记list的起点位置，第一次为空，后续以上一次list的返回值中的marker |
| delimiter  | String  |  无   | 构造函数或set方法 | 分隔符，限制返回的是以prefix开头，并以delimiter一次出现的结束的路径 |
|  maxKeys   | Integer | 1000 | 构造函数或set方法 |           最大返回的成员个数(不得超过1000)            |

### 返回值

成功返回ObjectListing类型, 包含所有的成员, 以及nextMarker.  失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
// 获取bucket下成员(设置delimiter)
ListObjectsRequest listObjectsRequest = new ListObjectsRequest();
listObjectsRequest.setBucketName("movie");
// 设置list的prefix, 表示list出来的文件key都是以这个prefix开始
listObjectsRequest.setPrefix("");
// 设置delimiter为/, 即获取的是直接成员，不包含目录下的递归子成员
listObjectsRequest.setDelimiter("/");
// 设置marker, (marker由上一次list获取到, 或者第一次list marker为空)
listObjectsRequest.setMarker("");
// 设置最多list 100个成员, (如果不设置, 默认为1000个，最大允许一次list 1000个key)
listObjectsRequest.setMaxKeys(100);

ObjectListing objectListing = cosClient.listObjects(listObjectsRequest);
// 获取下次list的marker
String nextMarker = objectListing.getNextMarker();
// 判断是否已经list完, 如果list结束, 则isTruncated为false, 否则为true
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

## Set Bucket Acl 

设置Bucket的访问控制权限列表(Access Control List). 

Set Bucket  Acl 是覆盖操作, 会覆盖已有的权限设置。

ACL包括预定义权限策略(CannedAccessControlList) 或者自定义的权限控制(AccessControlList). 两类权限当同时设置时将忽略预定义策略，以自定义策略为主。有关权限细节请参照权限章节。

### 方法原型

```java
// 方法1 (设置自定义策略)
public void setBucketAcl(String bucketName, AccessControlList acl)
  throws CosClientException, CosServiceException;
// 方法2 (设置预定义策略)
public void setBucketAcl(String bucketName, CannedAccessControlList acl) throws CosClientException, CosServiceException;
// 方法3 (以上两种方法的封装, 包含两种策略设置，如果同时设置以自定定义策略为主)
public void setBucketAcl(SetBucketAclRequest setBucketAclRequest) 
  throws CosClientException, CosServiceException;
```

### 参数说明

方法3参数同时包含1和2，因此以方法3为例进行介绍。

|         参数名         |         类型          | 默认值  |  参数描述   |
| :-----------------: | :-----------------: | :--: | :-----: |
| setBucketAclRequest | SetBucketAclRequest |  无   | 权限设置请求类 |

| request成员  |           类型            | 默认值  |    设置方法    |         描述         |
| :--------: | :---------------------: | :--: | :--------: | :----------------: |
| bucketName |         String          |  无   | 构造函数或set方法 |      bucket名称      |
|    acl     |    AccessControlList    |  无   | 构造函数或set方法 |      自定义权限策略       |
| cannedAcl  | CannedAccessControlList |  无   | 构造函数或set方法 | 预定义策略如公有读、公有读写、私有读 |

#### 

### 返回值

成功无返回，失败返回异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
// 设置自定义ACL
AccessControlList acl = new AccessControlList();
Owner owner = new Owner();
owner.setId("qcs::cam::uin/2779643970:uin/2779643970");
acl.setOwner(owner);
String id = "qcs::cam::uin/2779643970:uin/734505014";
UinGrantee uinGrantee = new UinGrantee("qcs::cam::uin/2779643970:uin/734505014");
uinGrantee.setIdentifier(id);
acl.grantPermission(uinGrantee, Permission.FullControl);
cosclient.setBucketAcl("movie", acl);

// 设置预定义ACL
// 设置私有读写(默认新建的bucket都是私有读写)
cosclient.setBucketAcl("movie", CannedAccessControlList.Private);
// 设置公有读私有写
cosclient.setBucketAcl("movie", CannedAccessControlList.PublicRead);
// 设置公有读写
cosclient.setBucketAcl("movie", CannedAccessControlList.PublicReadWrite);
```



## Get Bucket Acl

查询一个bucket的访问策略ACL

### 方法原型

```java
public AccessControlList getBucketAcl(String bucketName)
       throws CosClientException, CosServiceException
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |

### 返回值

返回一个bucket的ACL, 或者抛出异常(如bucket不存在), 抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
 AccessControlList acl = cosclient.getBucketAcl(bucket);
```



## Set Bucket CORS

设置bucket的跨域访问规则

### 方法原型

```java
public void setBucketCrossOriginConfiguration(String bucketName, BucketCrossOriginConfiguration bucketCrossOriginConfiguration);
```

### 参数说明

|              参数名               |               类型               | 默认值  |        参数描述         |
| :----------------------------: | :----------------------------: | :--: | :-----------------: |
|           bucketName           |             String             |  无   | bucket名称,由数字和小写字母构成 |
| bucketCrossOriginConfiguration | BucketCrossOriginConfiguration |  无   |    设置的bucket跨域策略    |

### 返回值

成功无返回，失败抛出异常(如bucket不存在), 抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
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
cosclient.setBucketCrossOriginConfiguration("movie", bucketCORS);
```



## Get Bucket CORS

获取bucket的跨域访问规则

### 方法原型

```java
public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(String bucketName)
     throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |

### 返回值

成功返回Bucket的跨域规则，失败抛出异常(如bucket不存在), 抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
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



## Delete Bucket CORS

删除bucket的跨域访问规则

### 方法原型

```java
public void deleteBucketCrossOriginConfiguration(String bucketName)
     throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |

### 返回值

成功无返回值，失败抛出异常(如bucket不存在), 抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
cosclient.deleteBucketCrossOriginConfiguration("movie");
```



## Set Bucket LifeCycle

删除bucket的生命周期规则.

### 方法原型

```java
public void setBucketLifecycleConfiguration(String bucketName, BucketLifecycleConfiguration bucketLifecycleConfiguration) throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |

### 返回值

成功无返回值，失败抛出异常(如bucket不存在), 抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
List<Rule> rules = new ArrayList<>();
// 规则1 30天后删除路径以hongkong_movie/为开始的文件
Rule deletePrefixRule = new Rule();
deletePrefixRule.setId("delete prefix xxxy after 30 days");
deletePrefixRule
        .setFilter(new LifecycleFilter(newLifecyclePrefixPredicate("hongkong_movie/")));
// 文件上传或者变更后, 30天后删除
deletePrefixRule.setExpirationInDays(30);
// 设置规则为生效状态
deletePrefixRule.setStatus(BucketLifecycleConfiguration.ENABLED);

// 规则2  20天后沉降到低频，一年后删除
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

// 生成bucketLifecycleConfiguration
BucketLifecycleConfiguration bucketLifecycleConfiguration =
        new BucketLifecycleConfiguration();
bucketLifecycleConfiguration.setRules(rules);
SetBucketLifecycleConfigurationRequest setBucketLifecycleConfigurationRequest =
      new SetBucketLifecycleConfigurationRequest("movie", bucketLifecycleConfiguration);

// 设置生命周期
cosclient.setBucketLifecycleConfiguration(setBucketLifecycleConfigurationRequest);
```



## Get Bucket LifeCycle

获取bucket的生命周期规则

### 方法原型

```java
public BucketLifecycleConfiguration getBucketLifecycleConfiguration(String bucketName)
            throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |

### 返回值

成功返回Bucket的生命周期规则，失败抛出异常(如bucket不存在), 抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

#### 示例

```java
BucketLifecycleConfiguration queryLifeCycleRet =
        cosclient.getBucketLifecycleConfiguration(bucket);
List<Rule> ruleLists = queryLifeCycleRet.getRules();
```



## Delete Bucket LifeCycle

获取bucket的生命周期规则

### 方法原型

```java
public void deleteBucketLifecycleConfiguration(String bucketName)
         throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |

### 返回值

成功无返回值，失败抛出异常(如bucket不存在), 抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
cosclient.deleteBucketLifecycleConfiguration("movie");
```





## Object API描述

### PUT Object (上传object)

将本地文件或者已知长度的输入流内容上传到COS. 适用于于图片类小文件上传(20MB以下), 最大支持5GB上限, 5GB以上请使用分块文件上传。

### 方法原型

```java
// 方法1  将本地文件上传到COS
public PutObjectResult putObject(String bucketName, String key, File file)
            throws CosClientException, CosServiceException;
// 方法2  输入流上传到COS
public PutObjectResult putObject(String bucketName, String key, InputStream input,
            ObjectMetadata metadata) throws CosClientException, CosServiceException;
// 方法3  对以上两个方法的包装, 支持更细粒度的参数控制, 如content-type, content-disposition等
public PutObjectResult putObject(PutObjectRequest putObjectRequest)
            throws CosClientException, CosServiceException;
```

### 参数说明

|       参数名        |       参数类型       | 默认值  |  参数描述  |
| :--------------: | :--------------: | :--: | :----: |
| putObjectRequest | PutObjectRequest |  无   | 上传文件请求 |

| request成员  |       类型       | 默认值  |    设置方法    |          描述          |
| :--------: | :------------: | :--: | :--------: | :------------------: |
| bucketName |     String     |  无   | 构造函数或set方法 |       bucket名称       |
|    key     |     String     |  无   | 构造函数或set方法 | cos的文件路径, 即从bucket开始 |
|    file    |      File      |  无   | 构造函数或set方法 |         本地文件         |
|   input    |  InputStream   |  无   | 构造函数或set方法 |         输入流          |
|  metadata  | ObjectMetadata |  无   | 构造函数或set方法 |        文件的元信息        |

#### 

### 返回值

成功返回PutObjectResult，包含etag等关键, 失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
String bucketName = "movie";
// 方法1 本地文件上传
File localFile = new File("/data/test.txt");
String key = "/aaa.txt";
PutObjectResult putObjectResult = cosClient.putObject(bucketName, key, localFile);
String etag = putObjectResult.getETag();  // 获取文件的etag

// 方法2 从输入流上传(需提前告知输入流的长度, 否则可能导致oom)
FileInputStream fileInputStream = new FileInputStream(localFile);
ObjectMetadata objectMetadata = new ObjectMetadata();
// 设置输入流长度为500
objectMetadata.setContentLength(500);  
// 设置Content type, 默认是application/octet-stream
objectMetadata.setContentType("application/pdf");
PutObjectResult putObjectResult = cosClient.putObject(bucketName, key, fileInputStream, objectMetadata);
String etag = putObjectResult.getETag();
// 关闭输入流...

// 方法3 提供更多细粒度的控制, 常用的设置如下
// 1 storage-class存储类型, 用于设置标准(默认)、低频、近线
// 2 content-type, 对于本地文件上传, 默认根据本地文件的后缀进行映射, 如jpg文件映射为image/jpeg
//   对于流式上传 默认是application/octet-stream
// 3 上传的同时制定权限(也可通过调用API set object acl来设置)
File localFile = new File("/data/dog.jpg");
String key = "/mypic.jpg";
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, file);
// 设置存储类型为低频
putObjectRequest.setStorageClass(StorageClass.Standard_IA);
// 设置自定义属性(如content-type, content-disposition等)
ObjectMetadata objectMetadata = new ObjectMetadata();
// 设置Content type, 默认是application/octet-stream
objectMetadata.setContentType("image/jpeg");
putObjectRequest.setMetadata(objectMetadata);
PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);
String etag = putObjectResult.getETag();  // 获取文件的etag
```



### 分块文件上传

分块文件上传是通过将文件拆分成多个小块进行上传，多个小块可以并发上传, 最大支持40TB。

分块文件上传的步骤为:

1. 初始化分块上传，获取uploadid。(initiateMultipartUpload)
2. 分块数据上传(可并发).  (uploadPart)
3. 完成分块上传。 (completeMultipartUpload)

另外还包可以获取已上传分块(listParts), 终止分块上传(abortMultipartUpload)。分块上传的步骤与门槛较多，建议使用后文封装的高级API上传。

### 方法原型

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

### 返回值

#### 方法1 (initiateMultipartUpload)

 成功返回InitiateMultipartUploadResult, 包含后续分块上传必须使用的upload id. 失败抛出异常      CosClientException或者CosServiceException. 具体请参照异常类说明

#### 方法2 (uploadPart)

 成功返回UploadPartResult, 包含该片的Etag和partNumber 失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

#### 方法3 (completeMultipartUpload)

 成功返回CompleteMultipartUploadResult, 包含全文的Etag. 失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

#### 方法4 (listParts)

 成功返回PartListing, 包含每一片的Etag和编号，以及下一次list的起点. 失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

#### 方法5 (abortMultipartUpload)

 成功无返回. 失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

#### 示例

```java
String bucketName = "movie";
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

// ListPart用于在complete分块上传前或者abort分块上传前获取uploadId对应的已上传的分块信息, 可以用来构造partEtags
ListPartsRequest listPartsRequest = new ListPartsRequest(bucket, key, uploadId);
do {
      partListing = cosclient.listParts(listPartsRequest);
      for (PartSummary partSummary : partListing.getParts()) {
           partETags.add(new PartETag(partSummary.getPartNumber(), partSummary.getETag()));
      }
      listPartsRequest.setPartNumberMarker(partListing.getNextPartNumberMarker());
} while (partListing.isTruncated());

// abortMultipartUpload 用于终止一个还未complete的分块上传
AbortMultipartUploadRequest abortMultipartUploadRequest = 
  									new AbortMultipartUploadRequest(bucket, key, uploadId);
cosclient.abortMultipartUpload(abortMultipartUploadRequest);
```



### Get Object

文件下载到本地或者获取下载文件下载输入流.

### 方法原型

```java
String bucketName = "movie";
// 方法1 下载文件，并获取输入流
public COSObject getObject(GetObjectRequest getObjectRequest)
            throws CosClientException, CosServiceException;
// 方法2 下载文件到本地.
public ObjectMetadata getObject(GetObjectRequest getObjectRequest, File destinationFile)
            throws CosClientException, CosServiceException;
```

### 参数说明

|       参数名        |       参数类型       | 默认值  |  参数描述   |
| :--------------: | :--------------: | :--: | :-----: |
| getObjectRequest | GetObjectRequest |  无   | 下载文件请求  |
| destinationFile  |       File       |  无   | 本地的保存文件 |

| request成员  |   类型   | 默认值  |    设置方法    |          描述          |
| :--------: | :----: | :--: | :--------: | :------------------: |
| bucketName | String |  无   | 构造函数或set方法 |       bucket名称       |
|    key     | String |  无   | 构造函数或set方法 | cos的文件路径, 即从bucket开始 |
|   range    | long[] |  无   |   set方法    |      下载的range范围      |

### 返回值

#### 方法1 (获取下载输入流)

 成功返回InitiateMultipartUploadResult, 包含输入流以及文件属性,  失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

#### 方法2 (下载文件到本地)

 成功返回文件的属性objectMetadata, 包含文件的自定义头和content-type等属性, 失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明示例

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

删除COS上的文件.

### 方法原型

```java
// 删除文件
public void deleteObject(String bucketName, String key)
            throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |
|    key     | String |  无   |        文件路径         |

### 返回值

成功无返回. 失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
// 删除COS文件
String bucketName = "movie";
String key = "abc/def.jpg";
cosclient.deleteObject(bucket, key);
```



### Head Object

查询获取COS上的文件属性

### 方法原型

```java
// 获取文件属性
public ObjectMetadata getObjectMetadata(String bucketName, String key)
  throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |
|    key     | String |  无   |        文件路径         |

### 返回值

成功无返回. 失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
// 获取COS文件属性
String bucketName = "movie";
String key = "abc/def.jpg";
ObjectMetadata objectMetadata = cosclient.getObjectMetadata(bucket, key);
```



### Put Object Copy

拷贝object到新的路径或者新的bucket. 支持跨园区跨账号跨bucket拷贝, 需要拥有对源文件的读取权限以及目的文件的写入权限

### 方法原型

```java
// 获取文件属性
public CopyObjectResult copyObject(CopyObjectRequest copyObjectRequest)
      throws CosClientException, CosServiceException
```

### 参数说明

|        参数名        |       参数类型        | 默认值  |  参数描述  |
| :---------------: | :---------------: | :--: | :----: |
| copyObjectRequest | CopyObjectRequest |  无   | 下载文件请求 |

|          参数名          |   类型   |                默认值                 |               参数描述               |
| :-------------------: | :----: | :--------------------------------: | :------------------------------: |
|      sourceAppid      | String |        和当前appid一致, 表示同账号拷贝         |              源APPID              |
|  sourceBucketRegion   | String | 与当前clientconfig的region一致, 表示统一园区拷贝 |          源Bucket Region          |
|   sourceBucketName    | String |                 无                  |             源bucket名             |
|       sourceKey       | String |                 无                  |              源文件路径               |
|    sourceVersionId    | String |            表示源文件当前最新版本             | 源文件version id(适用于开启了多版本的源bucket) |
| destinationBucketName | String |                 无                  |            目的bucket名             |
|    destinationKey     | String |                 无                  |              目的文件路径              |
|     storageClass      | String |                 标准                 |     拷贝的目的文件的存储类型(标准, 低频,近线)      |

### 返回值

成功返回CopyObjectResult. 包含新文件的Etag等, 失败抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

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

// 跨账号跨园区拷贝(需要拥有对源文件的读取权限以及目的文件的写入权限)
String srcAppid = "12511000";
String srcRegion = "ap-guangzhou";
copyObjectRequest = new CopyObjectRequest(srcAppid, srcRegion, srcBucketName, srcKey, destBucketName, destKey);
CopyObjectResult copyObjectResult = cosclient.copyObject(copyObjectRequest);
```



### Set Object ACL

设置Object的访问控制权限列表(Access Control List). 

Set Object Acl 是覆盖操作, 会覆盖已有的权限设置。

ACL包括预定义权限策略(CannedAccessControlList) 或者自定义的权限控制(AccessControlList). 两类权限当同时设置时将忽略预定义策略，以自定义策略为主。有关权限细节请参照权限章节。

### 方法原型

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

### 参数说明

方法3参数同时包含1和2，因此以方法3为例进行介绍。

|         参数名         |         类型          | 默认值  |  参数描述   |
| :-----------------: | :-----------------: | :--: | :-----: |
| SetObjectAclRequest | setObjectAclRequest |  无   | 权限设置请求类 |

| request成员  |           类型            | 默认值  |    设置方法    |         描述         |
| :--------: | :---------------------: | :--: | :--------: | :----------------: |
| bucketName |         String          |  无   | 构造函数或set方法 |      bucket名称      |
|    key     |         String          |  无   | 构造函数或set方法 |      文件路径Key       |
|    acl     |    AccessControlList    |  无   | 构造函数或set方法 |      自定义权限策略       |
| cannedAcl  | CannedAccessControlList |  无   | 构造函数或set方法 | 预定义策略如公有读、公有读写、私有读 |

#### 

### 返回值

成功无返回，失败返回异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
String bucketName = "movie";
String key = "abc/def.jpg";
// 设置自定义ACL
AccessControlList acl = new AccessControlList();
Owner owner = new Owner();
owner.setId("qcs::cam::uin/2779643970:uin/2779643970");
acl.setOwner(owner);
String id = "qcs::cam::uin/2779643970:uin/734505014";
UinGrantee uinGrantee = new UinGrantee("qcs::cam::uin/2779643970:uin/734505014");
uinGrantee.setIdentifier(id);
acl.grantPermission(uinGrantee, Permission.FullControl);
cosclient.setObjectAcl(buckeName, key, acl);

// 设置预定义ACL
// 设置私有读写(object的权限默认集成bucket的)
cosclient.setObjectAcl(buckeName, key, CannedAccessControlList.Private);
// 设置公有读私有写
cosclient.setObjectAcl(buckeName, key, CannedAccessControlList.PublicRead);
// 设置公有读写
cosclient.setObjectAcl(buckeName, key, CannedAccessControlList.PublicReadWrite);
```



## Get Object Acl

查询一个object的访问策略ACL

### 方法原型

```java
public AccessControlList getObjectAcl(String bucketName, String key)
  throws CosClientException, CosServiceException;
```

### 参数说明

|    参数名     |   类型   | 默认值  |        参数描述         |
| :--------: | :----: | :--: | :-----------------: |
| bucketName | String |  无   | bucket名称,由数字和小写字母构成 |
|    key     | String |  无   |        文件路径         |

### 返回值

返回一个objct所在的acl, 或者抛出异常(如bucket不存在), 抛出异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
String bucketName = "movie";
String key = "abc/def.jpg";
AccessControlList acl = cosclient.getObjectAcl(bucketName, key);
```

### 生成签名

COSSigner提供构造COS签名的方法，用于给移动端分发签名，构造下载链接等

#### 方法原型

```java
// 构造签名
public String buildAuthorizationStr(HttpMethodName methodName, String resourcePath,
            Map<String, String> headerMap, Map<String, String> paramMap, COSCredentials cred);
```

#### 参数说明

|     参数名      |        参数类型         | 默认值  |                  参数描述                  |
| :----------: | :-----------------: | :--: | :------------------------------------: |
|  methodName  |   HttpMethodName    |  无   | http请求方法(PUT, GET, DELETE, HEAD, POST) |
| resourcePath |       String        |  无   |                  路径地址                  |
|  headerMap   | Map<String, String> |  无   |               要签发的HTTP头部               |
|   paramMap   | Map<String, String> |  无   |              URL路径中的参数KV对              |
|     cred     |   COSCredentials    |  无   |                  身份信息                  |

#### 返回值

签名字符串

#### 示例

```java
 // 以下用于生成带下载签名的链接
COSSigner signer = new COSSigner();
signer.setSignExpiredTime(1800); // 设置签名有效时间为1800秒，默认是3600秒
// 生成签名
String origin_auth_str = signer.buildAuthorizationStr(HttpMethodName.GET, key, cred);
// 对签名进行URL ENCODE
String auth_str = UrlEncoderUtils.encode(origin_auth_str);
StringBuilder strBuilder = new StringBuilder();
strBuilder.append("http://").append(bucketName).append("-").append(appid).append(".")
     .append("ap-beijing-1").append(".myqcloud.com")
     .append(UrlEncoderUtils.encodeEscapeDelimiter(key)).append("?sign=").append(auth_str);
```



# 高级API文件上传(推荐)

高级API由类TransferManger通过封装上传以及下载接口，内部有一个线程池，接受用户的上传和下载请求，因此用户可选择异步的提交任务。

```java
// 生成TransferManager
TransferManager transferManager = new TransferManager(cosClient);
// .....(提交上传下载请求, 如下文所属)
// 关闭TransferManger
transferManager.shutdownNow();
```

## 上传文件

上传接口根据用户文件的长度自动选择简单上传以及分块上传， 降低用户的使用门槛。用户不用关心分快上传的每个步骤。

### 方法原型

```java
// 上传文件
public Upload upload(final PutObjectRequest putObjectRequest)
            throws CosServiceException, CosClientException;
```

### 参数说明

|       参数名        |       参数类型       | 默认值  |  参数描述  |
| :--------------: | :--------------: | :--: | :----: |
| putObjectRequest | PutObjectRequest |  无   | 上传文件请求 |

| request成员  |       类型       | 默认值  |    设置方法    |          描述          |
| :--------: | :------------: | :--: | :--------: | :------------------: |
| bucketName |     String     |  无   | 构造函数或set方法 |       bucket名称       |
|    key     |     String     |  无   | 构造函数或set方法 | cos的文件路径, 即从bucket开始 |
|    file    |      File      |  无   | 构造函数或set方法 |         本地文件         |
|   input    |  InputStream   |  无   | 构造函数或set方法 |         输入流          |
|  metadata  | ObjectMetadata |  无   | 构造函数或set方法 |        文件的元信息        |

### 返回值

成功返回Upload, 可以查询上传进度, 也可同步的等待上传结束。失败返回异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
// 本地文件上传
Upload upload = transferManager.upload(putObjectRequest, localFile);
 // 等待传输结束(如果想同步的等待上传结束，则调用waitForCompletion)
UploadResult uploadResult = upload.waitForUploadResult();
```



## 下载文件

接口根据用户文件的长度自动选择简单上传以及分块上传， 降低用户的使用门槛。用户不用关心分快上传的每个步骤。

### 方法原型

```java
// 下载文件
public Download download(final GetObjectRequest GetObjectRequest, final File file);
```

### 参数说明

|       参数名        |       参数类型       | 默认值  |  参数描述  |
| :--------------: | :--------------: | :--: | :----: |
| getObjectRequest | GetObjectRequest |  无   | 下载文件请求 |
|       file       |       File       |  无   | 下载目的地  |

| request成员  |       类型       | 默认值  |    设置方法    |          描述          |
| :--------: | :------------: | :--: | :--------: | :------------------: |
| bucketName |     String     |  无   | 构造函数或set方法 |       bucket名称       |
|    key     |     String     |  无   | 构造函数或set方法 | cos的文件路径, 即从bucket开始 |
|    file    |      File      |  无   | 构造函数或set方法 |         本地文件         |
|   input    |  InputStream   |  无   | 构造函数或set方法 |         输入流          |
|  metadata  | ObjectMetadata |  无   | 构造函数或set方法 |        文件的元信息        |

### 返回值

成功返回Download, 可以查询上传进度, 也可同步的等待上传结束。失败返回异常CosClientException或者CosServiceException. 具体请参照异常类说明

### 示例

```java
// 下载文件
Download download = transferManager.download(GetObjectRequest, localFile);
 // 等待传输结束(如果想同步的等待上传结束，则调用waitForCompletion)
download.waitForCompletion();
```



## 异常说明

SDK失败时, 抛出的异常皆是RuntimeExcpetion, 目前SDK常见的异常有CosClientException, CosServiceException和 IllegalArgumentException

## CosClientException

客户端异常,  用于指因为客户端原因导致无法和服务端完成正常的交互而导致的失败, 如客户端无法连接到服务端，无法解析服务端返回的数据, 读取本地文件发生IO异常等. CosClientException集成自RuntimeException, 没有自定义的成员变量, 使用方法同RuntimeException。

## CosServiceException

CosServiceException服务异常, 用于指交互正常完成，但是操作失败的场景。例如客户端访问一个不存在bucket, 删除一个不存在的文件，没有权限进行某个操作, 服务端故障异常等。CosServiceException包含了服务端返回的状态码, requestid, 出错明细等.捕获异常后, 建议对整个异常进行打印, 异常包含了必须的排查因素。以下是异常成员变量的描述.

|  request成员   |    类型     |                    描述                    |
| :----------: | :-------: | :--------------------------------------: |
|  requestId   |  String   |        请求ID, 用于表示一个请求, 对于排查问题十分重要        |
|   traceId    |  String   |                辅助排查问题的ID,                |
|  statusCode  |  String   | response的status状态码, 4xx是指请求因客户端而失败, 5xx是服务端异常导致的失败。 |
|  errorType   | ErrorType | 枚举类, 表示异常的种类, 分为Client, Service, Unknown |
|  errorCode   |  String   |          请求失败时body返回的Error Code          |
| errorMessage |  String   |        请求失败时body返回的Error Message         |

### 



