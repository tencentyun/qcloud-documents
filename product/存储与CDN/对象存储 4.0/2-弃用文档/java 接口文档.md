对象存储服务 XML Java SDK 操作成功会返回每种 API 对应的类型，失败会报出异常（CosClientException和CosServiception）。其中 CosClientException 是一些客户端异常，如网络异常，发送请求失败。CosServiceException 包含了客户请求被服务端处理为失败的原因，错误码等。如没有权限，访问一个不存在的文件。具体请参考文档最后异常类说明。
SDK 中使用每一个 API 的正确做法如下所示，为了简要，后续的 API 范例不再给出捕获异常的范例，仅给出 API 的使用范例。

```java
try {
   // bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
   String bucketName = "movie-1251668577";
   String key = "abc/def.jpg";
   cosClient.deleteObject(bucket, key);
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

- **方法原型**

```java
public Bucket createBucket(String  bucketName) throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |

- **返回值**
  - 成功：  Bucket 类，包含有关 Bucket 的描述（Bucket 的名称，owner 和创建日期）。
  - 失败： 发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
Bucket bucket = cosClient.createBucket(bucketName);
```

### Delete Bucket

删除已清空的 Bucket。

- **方法原型**

```java
 public void deleteBucket(String bucketName) throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为 {name}-{appid} ，name 由字母数字和中划线构成 | String |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
cosClient.deleteBucket(bucketName);
```

### Head Bucket

查询一个 Bucket 是否存在。

- **方法原型**

```java
public boolean doesBucketExist(String bucketName) 
  throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |

- **返回值**
  - 成功：存在返回 true，否则 false。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
boolean bucketExistFlag = cosClient.doesBucketExist(bucketName);
```

### Get Bucket Location

查询一个 Bucket 所在的 Region。

- **方法原型**

```java
public String getBucketLocation(String bucketName) 
throws CosClientException， CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为 {name}-{appid} ，name 由字母数字和中划线构成 | String |

- **返回值**
  - 成功：返回一个 Bucket 所在的 Region。 
  - 失败：发生错误（如 Bucket 不存在），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String location = cosClient.getBucketLocation("movie-1251668577");
```

### List Buckets

列出账户下所有的 Bucket

- **方法原型**

```java
public List<Bucket> listBuckets() throws CosClientException, CosServiceException;
```

- **参数说明**

无

- **返回值**
  - 成功：返回一个 所有 Bucket 类的列表，Bucket 类包含了 bucket 成员，location 等信息。
  - 失败：发生错误（如 Bucket 不存在），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常说明。
- **示例**

```java
List<Bucket> buckets = cosClient.listBuckets();
for (Bucket bucketElement : buckets) {
    String bucketName = bucketElement.getName();
    String bucketLocation = bucketElement.getLocation();
}
```

### Get Bucket（列出所有 Objects）

查询获取 COS 上的文件列表。

- **方法原型**

```java
// 获取文件列表
public ObjectListing listObjects(ListObjectsRequest listObjectsRequest)
            throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名             | 参数描述         | 参数类型           |
| ------------------ | ---------------- | ------------------ |
| listObjectsRequest | 获取文件列表请求 | ListObjectsRequest |

Request 成员说明 ：

| Request 成员 | 设置方法            | 描述                                                         | 类型   |
| ------------ | ------------------- | ------------------------------------------------------------ | ------ |
| bucketName   | 构造函数或 set 方法 | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |
| prefix       | 构造函数或 set 方法 | 标记 list 以 prefix 为前缀的成员，默认不进行限制，即 Bucket 下所有的成员。<br>默认值： "" | String |
|   marker   |  构造函数或 set 方法 | 标记 list 的起点位置，第一次为空，后续以上一次 list 的返回值中的 marker |String  
| delimiter  | 构造函数或 set 方法 | 分隔符，限制返回的是以 prefix 开头，并以 delimiter 一次出现的结束的路径 |String  
|  maxKeys   | 构造函数或 set 方法 |           最大返回的成员个数（不得超过 1000）   <br>默认值： 1000          |Integer |  

- **返回值**
  - 成功：返回 ObjectListing 类型， 包含所有的成员， 以及 nextMarker。  
  - 失败：抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";

// 获取 bucket 下成员（设置 delimiter）
ListObjectsRequest listObjectsRequest = new ListObjectsRequest();
listObjectsRequest.setBucketName(bucketName);
// 设置 list 的 prefix, 表示 list 出来的文件 key 都是以这个 prefix 开始
listObjectsRequest.setPrefix("");
// 设置 delimiter 为/, 即获取的是直接成员，不包含目录下的递归子成员
listObjectsRequest.setDelimiter("/");
// 设置 marker, (marker 由上一次 list 获取到, 或者第一次 list marker 为空)
listObjectsRequest.setMarker("");
// 设置最多 list 100个成员,（如果不设置, 默认为1000个，最大允许一次 list 1000个 key）
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

### Bucket ACL

设置 Bucket 的访问控制权限列表（Access Control List）。

Set Bucket  ACL 是覆盖操作，会覆盖已有的权限设置。

ACL 包括预定义权限策略（CannedAccessControlList）或者自定义的权限控制（AccessControlList）。两类权限当同时设置时将忽略预定义策略，以自定义策略为主。有关权限细节请参照权限章节。

- **方法原型**

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

- **参数说明**

方法3参数同时包含1和2，因此以方法3为例进行介绍。

| 参数名              | 参数描述       | 类型                |
| ------------------- | -------------- | ------------------- |
| setBucketAclRequest | 权限设置请求类 | SetBucketAclRequest |

Request 成员说明：

| Request 成员 | 设置方法            | 描述                                                         | 类型                    |
| ------------ | ------------------- | ------------------------------------------------------------ | ----------------------- |
| bucketName   | 构造函数或 set 方法 | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                  |
| acl          | 构造函数或 set 方法 | 自定义权限策略                                               | AccessControlList       |
| cannedAcl    | 构造函数或 set 方法 | 预定义策略如公有读、公有读写、私有读                         | CannedAccessControlList |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败）， 抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
// 设置自定义 ACL
AccessControlList acl = new AccessControlList();
Owner owner = new Owner();
owner.setId("qcs::cam::uin/2779643970:uin/2779643970");
acl.setOwner(owner);
String id = "qcs::cam::uin/2779643970:uin/734505014";
UinGrantee uinGrantee = new UinGrantee("qcs::cam::uin/2779643970:uin/734505014");
uinGrantee.setIdentifier(id);
acl.grantPermission(uinGrantee, Permission.FullControl);
cosClient.setBucketAcl(bucketName, acl);

// 设置预定义 ACL
// 设置私有读写（默认新建的 bucket 都是私有读写）
cosClient.setBucketAcl(bucketName, CannedAccessControlList.Private);
// 设置公有读私有写
cosClient.setBucketAcl(bucketName, CannedAccessControlList.PublicRead);
// 设置公有读写
cosClient.setBucketAcl(bucketName, CannedAccessControlList.PublicReadWrite);
```

### Get Bucket ACL

查询一个 Bucket 的访问策略 ACL。

- **方法原型**

```java
public AccessControlList getBucketAcl(String bucketName)
       throws CosClientException, CosServiceException
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |

- **返回值**
  - 成功：返回一个 Bucket 的 ACL。 
  - 失败：发生错误（如身份认证失败）， 抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
AccessControlList acl = cosClient.getBucketAcl(bucketName);
```

### Set Bucket CORS

设置 Bucket 的跨域访问规则。

- **方法原型**

```java
public void setBucketCrossOriginConfiguration(String bucketName, BucketCrossOriginConfiguration bucketCrossOriginConfiguration);
```

- **参数说明**

| 参数名                         | 参数描述                                                     | 类型                           |
| ------------------------------ | ------------------------------------------------------------ | ------------------------------ |
| bucketName                     | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                         |
| bucketCrossOriginConfiguration | 设置的 Bucket 跨域策略                                       | BucketCrossOriginConfiguration |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
BucketCrossOriginConfiguration bucketCORS = new BucketCrossOriginConfiguration();
List<CORSRule> corsRules = new ArrayList<>();
CORSRule corsRule = new CORSRule();
// 规则名称
corsRule.setId("set-bucket-cors-test");  
// 允许的 HTTP 方法
corsRule.setAllowedMethods(AllowedMethods.PUT, AllowedMethods.GET, AllowedMethods.HEAD);
corsRule.setAllowedHeaders("x-cos-grant-full-control");
corsRule.setAllowedOrigins("http://mail.qq.com", "http://www.qq.com",
        "http://video.qq.com");
corsRule.setExposedHeaders("x-cos-request-id");
corsRule.setMaxAgeSeconds(60);
corsRules.add(corsRule);
bucketCORS.setRules(corsRules);
cosClient.setBucketCrossOriginConfiguration(bucketName, bucketCORS);
```

### Get Bucket CORS

获取 Bucket 的跨域访问规则。

- **方法原型**

```java
public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(String bucketName)
throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |

- **返回值**
  - 成功：返回 Bucket 的跨域规则。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
BucketCrossOriginConfiguration corsGet = cosClient.getBucketCrossOriginConfiguration(bucketName);
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

- **方法原型**

```java
public void deleteBucketCrossOriginConfiguration(String bucketName)
throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
cosClient.deleteBucketCrossOriginConfiguration(bucketName);
```

### Set Bucket MultiVersioning

开启Bucket的版本控制, 开启版本控制后每个文件会保留多个版本。

- **方法原型**

```java
public void setBucketVersioningConfiguration(SetBucketVersioningConfigurationRequest setBucketVersioningConfigurationRequest)
    throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名                                  | 参数描述                                                     | 类型                                    |
| --------------------------------------- | ------------------------------------------------------------ | --------------------------------------- |
| bucketName                              | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                                  |
| setBucketVersioningConfigurationRequest | 版本控制配置                                                 | SetBucketVersioningConfigurationRequest |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
String bucketName = "movie-1251668577";

// 开启版本控制
cosClient.setBucketVersioningConfiguration(
        new SetBucketVersioningConfigurationRequest(bucketName,
                new BucketVersioningConfiguration(BucketVersioningConfiguration.ENABLED)));

// 关闭版本控制
cosClient.setBucketVersioningConfiguration(
        new SetBucketVersioningConfigurationRequest(bucketName,
                new BucketVersioningConfiguration(BucketVersioningConfiguration.SUSPENDED)));
```

### Get  Bucket MultiVersioning

获取 Bucket 的版本控制状态

- **方法原型**

```java
// 方法1 传入bucket名即可
public BucketVersioningConfiguration getBucketVersioningConfiguration(String bucketName)
            throws CosClientException, CosServiceException;

// 方法2 通过GetBucketVersioningConfigurationRequest获取			
public BucketVersioningConfiguration getBucketVersioningConfiguration(
    GetBucketVersioningConfigurationRequest getBucketVersioningConfigurationRequest)
        throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名                                  | 参数描述                                                     | 类型                                    |
| --------------------------------------- | ------------------------------------------------------------ | --------------------------------------- |
| bucketName                              | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                                  |
| getBucketVersioningConfigurationRequest | 获取版本控制配置请求                                         | SetBucketVersioningConfigurationRequest |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
String bucketName = "movie-1251668577";

// 获取版本控制
BucketVersioningConfiguration bvc =
        cosClient.getBucketVersioningConfiguration(bucketName);

// 获取版本控制
BucketVersioningConfiguration bvc2 = cosClient.getBucketVersioningConfiguration(
                new GetBucketVersioningConfigurationRequest(bucketName));
```

### Set Bucket Replication

设置 bucket 跨区域复制, 跨区域复制依赖于版本控制, 请先开启版本控制

- **方法原型**

```java
public void setBucketReplicationConfiguration(
        SetBucketReplicationConfigurationRequest setBucketReplicationConfigurationRequest)
                throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名                                   | 参数描述                                                     | 类型                                    |
| ---------------------------------------- | ------------------------------------------------------------ | --------------------------------------- |
| bucketName                               | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                                  |
| setBucketReplicationConfigurationRequest | 跨区域复制配置                                               | SetBucketVersioningConfigurationRequest |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
String bucketName = "movie-1251668577";

ReplicationRule replicationRule = new ReplicationRule();
replicationRule.setStatus(ReplicationRuleStatus.Enabled);
replicationRule.setPrefix("");

ReplicationDestinationConfig replicationDestinationConfig =
     new ReplicationDestinationConfig();
// bucketQCS用来描述要复制的目的bucket 格式是qcs:id/0:cos:${dest-region}:appid/${appid}:${bucketname-not-contain-appid}
String bucketQCS = "qcs:id/0:cos:ap-chongqing:appid/1251668577:moviebak-chongqing";
replicationDestinationConfig.setBucketQCS(bucketQCS);
replicationDestinationConfig.setStorageClass(StorageClass.Standard);
replicationRule.setDestinationConfig(replicationDestinationConfig);
BucketReplicationConfiguration bucketReplicationConfiguration =
     new BucketReplicationConfiguration();
// ruleName构成qcs::cam::uin/${uin}:uin/${uin}
String ruleName = "qcs::cam::uin/111222333:uin/111222333";
bucketReplicationConfiguration.setRoleName(ruleName);
// ruid 用来表述复制规则的 ID
String ruleId = "moviebak-chongqing-copy";
bucketReplicationConfiguration.addRule(ruleId, replicationRule);
cosClient.setBucketReplicationConfiguration(bucketName, bucketReplicationConfiguration);
```

### Get Bucket Replication

获取 bucket 跨区域复制。

- **方法原型**

```java
// 获取 bucket 跨区域复制配置方法1
public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(String bucketName)
        throws CosClientException, CosServiceException;

// 获取 bucket 跨区域复制方法2		
public BucketCrossOriginConfiguration getBucketCrossOriginConfiguration(
        GetBucketCrossOriginConfigurationRequest getBucketCrossOriginConfigurationRequest)
                throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名                                   | 参数描述                                                     | 类型                                     |
| ---------------------------------------- | ------------------------------------------------------------ | ---------------------------------------- |
| bucketName                               | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                                   |
| getBucketCrossOriginConfigurationRequest | 获取跨区域复制配置请求                                       | GetBucketCrossOriginConfigurationRequest |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
String bucketName = "movie-1251668577";

// 获取bucket跨区域复制配置方法1
BucketReplicationConfiguration brcfRet = cosClient.getBucketReplicationConfiguration(bucketName);

// 获取bucket跨区域复制配置方法2
BucketReplicationConfiguration brcfRet2 = cosClient.getBucketReplicationConfiguration(
                new GetBucketCrossOriginConfigurationRequest(bucketName));
```

### Delete Bucket Replication

删除 bucket 跨区域复制。

- **方法原型**

```java
// 删除 bucket 跨区域复制配置方法1
public void deleteBucketCrossOriginConfiguration(String bucketName)
        throws CosClientException, CosServiceException;

// 删除 bucket 跨区域复制方法2		
public void deleteBucketCrossOriginConfiguration(
        DeleteBucketCrossOriginConfigurationRequest deleteBucketCrossOriginConfigurationRequest)
                throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名                                      | 参数描述                                                     | 类型                                        |
| ------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| bucketName                                  | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                                      |
| deleteBucketCrossOriginConfigurationRequest | 删除跨区域复制配置请求                                       | DeleteBucketCrossOriginConfigurationRequest |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
String bucketName = "movie-1251668577";

// 删除 bucket 跨区域复制配置方法1
BucketReplicationConfiguration brcfRet =  cosClient.deleteBucketReplicationConfiguration(bucketName);

// 删除 bucket 跨区域复制配置方法2
BucketReplicationConfiguration brcfRet2 = cosClient.getBucketReplicationConfiguration(
                new DeleteBucketCrossOriginConfigurationRequest(bucketName));
```

### Set Bucket LifeCycle

设置 Bucket 的生命周期规则。

- **方法原型**

```java
public void setBucketLifecycleConfiguration(String bucketName, BucketLifecycleConfiguration bucketLifecycleConfiguration) 
        throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名                       | 参数描述                                                     | 类型                         |
| ---------------------------- | ------------------------------------------------------------ | ---------------------------- |
| bucketName                   | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                       |
| bucketLifecycleConfiguration | 生命周期配置                                                 | BucketLifecycleConfiguration |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
List<Rule> rules = new ArrayList<>();
// 规则1  30天后删除路径以 hongkong_movie/ 为开始的文件
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

// 生成 bucketLifecycleConfiguration
BucketLifecycleConfiguration bucketLifecycleConfiguration =
new BucketLifecycleConfiguration();
bucketLifecycleConfiguration.setRules(rules);

// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
SetBucketLifecycleConfigurationRequest setBucketLifecycleConfigurationRequest =
new SetBucketLifecycleConfigurationRequest(bucketName, bucketLifecycleConfiguration);

// 设置生命周期
cosClient.setBucketLifecycleConfiguration(setBucketLifecycleConfigurationRequest);
```

### Get Bucket LifeCycle

获取 Bucket 的生命周期规则。

- **方法原型**

```java
public BucketLifecycleConfiguration getBucketLifecycleConfiguration(String bucketName)
throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |

- **返回值**
  - 成功：返回 BucketLifecycleConfiguration 类， 包含 bucket 的生命周期规则。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
BucketLifecycleConfiguration queryLifeCycleRet =
        cosClient.getBucketLifecycleConfiguration(bucketName);
List<Rule> ruleLists = queryLifeCycleRet.getRules();
```

### Delete Bucket LifeCycle

删除清空 Bucket 的生命周期规则。

- **方法原型**

```java
public void deleteBucketLifecycleConfiguration(String bucketName)
throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
cosClient.deleteBucketLifecycleConfiguration(bucketName);
```

## Object API 描述

### PUT Object（上传 Object）

将本地文件或者已知长度的输入流内容上传到 COS。适用于图片类小文件上传（20MB 以下），最大支持 5GB（含），5GB 以上请使用分块上传或高级 API 上传。

- 上传过程中默认会对文件长度与 MD5 进行校验（关闭 MD5 校验参考示例代码）。
- 若 COS 上已存在同样 Key 的对象，上传时则会进行覆盖。
- 当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，上传时请不要设置，默认继承 Bucket 权限。
- 上传之后，您可以用同样的 `key`，调用 `GetObject` 接口将文件下载到本地，也可以生成预签名链接（下载请指定 method 为 `GET`，具体接口说明见下文），发送到其他端来进行下载。


- **方法原型**

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

- **参数说明**

| 参数名           | 参数描述     | 参数类型         |
| ---------------- | ------------ | ---------------- |
| putObjectRequest | 上传文件请求 | PutObjectRequest |

Request 成员说明：

| Request 成员 | 设置方法            | 描述                                                         | 类型           |
| ------------ | ------------------- | ------------------------------------------------------------ | -------------- |
| bucketName   | 构造函数或 set 方法 | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String         |
| key          | 构造函数或 set 方法 | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String         |
| file         | 构造函数或 set 方法 | 本地文件                                                     | File           |
| input        | 构造函数或 set 方法 | 输入流                                                       | InputStream    |
| metadata     | 构造函数或 set 方法 | 文件的元信息                                                 | ObjectMetadata |

- **返回值**
  - 成功：PutObjectResult，包含文件的 ETag 等信息。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
// 方法1 本地文件上传
File localFile = new File("/data/test.txt");
String key = "aaa.txt";
PutObjectResult putObjectResult = cosClient.putObject(bucketName, key, localFile);
String etag = putObjectResult.getETag();  // 获取文件的 etag

// 方法2 从输入流上传(需提前告知输入流的长度, 否则可能导致 oom)
FileInputStream fileInputStream = new FileInputStream(localFile);
ObjectMetadata objectMetadata = new ObjectMetadata();
// 设置输入流长度为500
objectMetadata.setContentLength(500);  
// 设置 Content type, 默认是 application/octet-stream
objectMetadata.setContentType("application/pdf");
PutObjectResult putObjectResult = cosClient.putObject(bucketName, key, fileInputStream, objectMetadata);
String etag = putObjectResult.getETag();
// 关闭输入流...

// 方法3 提供更多细粒度的控制, 常用的设置如下
// 1 storage-class 存储类型, 枚举值：Standard，Standard_IA，Archive。默认值：Standard
// 2 content-type, 对于本地文件上传, 默认根据本地文件的后缀进行映射, 如 jpg 文件映射 为image/jpeg
//   对于流式上传 默认是 application/octet-stream
// 3 上传的同时制定权限(也可通过调用 API set object acl 来设置)
// 4 若要全局关闭上传MD5校验, 则设置系统环境变量, 此设置会对所有的会影响所有的上传校验。 默认是进行校验的。
// 关闭校验  System.setProperty(SkipMd5CheckStrategy.DISABLE_PUT_OBJECT_MD5_VALIDATION_PROPERTY, "true");
// 再次打开校验  System.setProperty(SkipMd5CheckStrategy.DISABLE_PUT_OBJECT_MD5_VALIDATION_PROPERTY, null);
File localFile = new File("/data/dog.jpg");
String key = "mypic.jpg";
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

- **分块文件上传**

分块文件上传是通过将文件拆分成多个小块进行上传，多个小块可以并发上传，最大支持 40 TB。

分块文件上传的步骤为：

1. 初始化分块上传，获取 uploadid。（initiateMultipartUpload）
2. 分块数据上传（可并发）。（uploadPart）
3. 完成分块上传。（completeMultipartUpload）

另外还包可以获取已上传分块（listParts），终止分块上传（abortMultipartUpload）。分块上传的步骤与门槛较多，建议使用后文封装的高级 API 上传。

**Tips**： 分块上传过程中默认会对每一个分块的长度与 MD5 进行校验（关闭 MD5 校验参考示例代码请参考上节中关闭方法）。

- **方法原型**

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

- **返回值**
- **方法1 （initiateMultipartUpload）**
  - 成功：返回 InitiateMultipartUploadResult 类，包含后续分块上传必须使用的 upload id。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。
- **方法2 （uploadPart）**
  - 成功：返回 UploadPartResult，包含该分块的 Etag 和 partNumber 。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。
- **方法3 （completeMultipartUpload）**
  - 成功：返回 CompleteMultipartUploadResult，包含全文的 Etag。 
  - 失败：发生错误（如身份认证失败）， 抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。
- **方法4 （listParts）**
  - 成功：返回 PartListing， 包含每一分块的 ETag 和编号，以及下一次 list 的起点 marker。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **方法5 （abortMultipartUpload）**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。 具体请参照异常类说明。
- **示例**

```java
// bucket的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
// 初始化分块
InitiateMultipartUploadRequest initRequest =
                new InitiateMultipartUploadRequest(bucketName, key);
InitiateMultipartUploadResult initResponse = cosClient.initiateMultipartUpload(initRequest);
String uploadId = initResponse.getUploadId()
// 上传分块, 最多1000个分块, 分块大小支持为 1M * 5G.
// 分块大小设置为4M. 如果总计 n 个分块, 则 1~n-1 的分块大小一致, 最后一块小于等于前面的分块大小
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
// ... 上传 partNumber 第2个到第 n 个分块

// complete 完成分块上传.
CompleteMultipartUploadRequest compRequest = new CompleteMultipartUploadRequest(bucketName, key,
           uploadId, partETags);
CompleteMultipartUploadResult result =  cosClient.completeMultipartUpload(compRequest);

// ListPart 用于在 complete 分块上传前或者 abort 分块上传前获取 uploadId 对应的已上传的分块信息, 可以用来构造 partEtags
ListPartsRequest listPartsRequest = new ListPartsRequest(bucket, key, uploadId);
do {
      partListing = cosClient.listParts(listPartsRequest);
      for (PartSummary partSummary : partListing.getParts()) {
           partETags.add(new PartETag(partSummary.getPartNumber(), partSummary.getETag()));
      }
      listPartsRequest.setPartNumberMarker(partListing.getNextPartNumberMarker());
} while (partListing.isTruncated());

// abortMultipartUpload 用于终止一个还未 complete 的分块上传
AbortMultipartUploadRequest abortMultipartUploadRequest = 
  									new AbortMultipartUploadRequest(bucket, key, uploadId);
cosClient.abortMultipartUpload(abortMultipartUploadRequest);
```

### Get Object

文件下载到本地或者获取下载文件下载输入流。

- **方法原型**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
// 方法1 下载文件，并获取输入流
public COSObject getObject(GetObjectRequest getObjectRequest)
            throws CosClientException, CosServiceException;
// 方法2 下载文件到本地.
public ObjectMetadata getObject(GetObjectRequest getObjectRequest, File destinationFile)
            throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名           | 参数描述       | 参数类型         |
| ---------------- | -------------- | ---------------- |
| getObjectRequest | 下载文件请求   | GetObjectRequest |
| destinationFile  | 本地的保存文件 | File             |

Request 成员说明：

| Request 成员 | 设置方法            | 描述                                                         | 类型   |
| ------------ | ------------------- | ------------------------------------------------------------ | ------ |
| bucketName   | 构造函数或 set 方法 | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |
| key          | 构造函数或 set 方法 | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |
| range        | set方法             | 下载的 range 范围                                            | Long[] |

- **返回值**
- **方法1 （获取下载输入流）**
  - 成功：返回 COSObject 类，包含输入流以及文件属性。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **方法2 （下载文件到本地）**
  - 成功：返回文件的属性 objectMetadata，包含文件的自定义头和 content-type 等属性。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
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

- **方法原型**

```java
// 删除文件
public void deleteObject(String bucketName, String key)
            throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |
| key        | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// 删除 COS 文件
// bucket的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
String key = "abc/def.jpg";
cosClient.deleteObject(bucket, key);
```

### Head Object

查询获取 COS 上的文件属性。

- **方法原型**

```java
// 获取文件属性
public ObjectMetadata getObjectMetadata(String bucketName, String key)
  throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |
| key        | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// 获取 COS 文件属性
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
String key = "abc/def.jpg";
ObjectMetadata objectMetadata = cosClient.getObjectMetadata(bucketName, key);
```

### Put Object Copy

拷贝 Object 到新的路径或者新的 Bucket。支持跨地域跨账号跨 Bucket 拷贝，需要拥有对源文件的读取权限以及目的文件的写入权限。最大支持5G 文件 copy，5G 以上文件请使用高级 API copy。

- **方法原型**

```java
// 获取文件属性
public CopyObjectResult copyObject(CopyObjectRequest copyObjectRequest)
      throws CosClientException, CosServiceException
```

- **参数说明**

| 参数名            | 参数描述     | 参数类型          |
| ----------------- | ------------ | ----------------- |
| copyObjectRequest | 拷贝文件请求 | CopyObjectRequest |

Request 成员说明：

| 参数名                | 参数描述                                                     | 类型   |
| --------------------- | ------------------------------------------------------------ | ------ |
| sourceBucketRegion    | 源 Bucket Region 。默认值：与当前 clientconfig 的 region 一致, 表示统一地域拷贝 | String |
| sourceBucketName      | 源 Bucket 名, bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |
| sourceKey             | 源对象键, 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |
| sourceVersionId       | 源文件 version id（适用于开启了版本控制的源 Bucket）。默认值：源文件当前最新版本 | String |
| destinationBucketName | 目的 Bucket 名, bucket 的命名规则为{name}-{appid} ，name由字母数字和中划线构成 | String |
| destinationKey        | 目的对象键, 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg，详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |
| storageClass          | 拷贝的目的文件的存储类型。枚举值：Standard，Standard_IA。默认值：Standard    | String |

- **返回值**
  - 成功：返回 CopyObjectResult，包含新文件的 Etag 等信息。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// 同地域同账号拷贝
// 源 bucket, bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String srcBucketName = "srcBucket-1251668577";
// 要拷贝的源文件
String srcKey = "aaa/bbb.txt";
// 目的 bucket, bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String destBucketName = "destBucket-1251668577";
// 要拷贝的目的文件
String destKey = "ccc/ddd.txt";
CopyObjectRequest copyObjectRequest = new CopyObjectRequest(srcBucketName, srcKey, destBucketName, destKey);
CopyObjectResult copyObjectResult = cosClient.copyObject(copyObjectRequest);

// 跨账号跨地域拷贝（需要拥有对源文件的读取权限以及目的文件的写入权限）
String srcBucketNameOfDiffAppid = "srcBucket-125100000";
Region srcBucketRegion = new Region("ap-shanghai");
copyObjectRequest = new CopyObjectRequest(srcBucketRegion, srcBucketNameOfDiffAppid, srcKey, destBucketName, destKey);
copyObjectResult = cosClient.copyObject(copyObjectRequest);
```

### Set Object ACL

设置 Object 的访问控制权限列表（Access Control List）。Set Object ACL 是覆盖操作，会覆盖已有的权限设置。

> !当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请不要设置，默认继承 Bucket 权限。

ACL 包括预定义权限策略（CannedAccessControlList）或者自定义的权限控制（AccessControlList）。两类权限当同时设置时将忽略预定义策略，以自定义策略为主。有关权限细节请参照权限章节。

- **方法原型**

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

- **参数说明**
  - **方法3** 参数同时包含1和2，因此以方法3为例进行介绍。

| 参数名              | 参数描述 | 类型                |
| ------------------- | -------- | ------------------- |
| SetObjectAclRequest | 请求类   | setObjectAclRequest |

Request 成员说明：

| Request 成员 | 设置方法            | 描述                                                         | 类型                    |
| ------------ | ------------------- | ------------------------------------------------------------ | ----------------------- |
| bucketName   | 构造函数或 set 方法 | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                  |
| key          | 构造函数或 set 方法 | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String                  |
| acl          | 构造函数或 set 方法 | 自定义权限策略                                               | AccessControlList       |
| cannedAcl    | 构造函数或 set 方法 | 预定义策略如公有读、公有读写、私有读                         | CannedAccessControlList |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
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
cosClient.setObjectAcl(buckeName, key, acl);

// 设置预定义 ACL
// 设置私有读写（Object 的权限默认集成 Bucket的）
cosClient.setObjectAcl(buckeName, key, CannedAccessControlList.Private);
// 设置公有读私有写
cosClient.setObjectAcl(buckeName, key, CannedAccessControlList.PublicRead);
// 设置公有读写
cosClient.setObjectAcl(buckeName, key, CannedAccessControlList.PublicReadWrite);
```

### Get Object ACL

查询一个 Object 的访问策略 ACL。

- **方法原型**

```java
public AccessControlList getObjectAcl(String bucketName, String key)
  throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |
| key        | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |

- **返回值**
  - 成功：返回一个 Object 所在的 ACL。
  - 失败：发生错误（如身份认证失败）， 抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
String key = "abc/def.jpg";
AccessControlList acl = cosClient.getObjectAcl(bucketName, key);
```

### Post Object restore

可以将一个 archive 类型的对象恢复出一个临时的可读对象。

- **方法原型**

```java
public void restoreObject(RestoreObjectRequest restoreObjectRequest)
            throws CosClientException, CosServiceException;
```

- **参数说明**

| 参数名              | 参数描述 | 类型                |
| ------------------- | -------- | ------------------- |
| restoreObjectRequest | 请求类   | RestoreObjectRequest |

Request 成员说明：

| 参数名     | 参数描述                                                     | 类型   |
| ---------- | ------------------------------------------------------------ | ------ |
| bucketName | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |
| key        | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg，详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |
| expirationInDays | 恢复出的临时文件的过期天数 | int
| casJobParameters | 描述恢复类型的配置信息，可调用 setTier 函数设置为 Tier.Standard、Tier.Expedited、Tier.Bulk 三种恢复类型之一| CASJobParameters |

- **返回值**
  - 成功：无返回值。
  - 失败：发生错误（如身份认证失败）， 抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "mybucket-1251668577";
String key = "test/my_data.txt";
     
// 设置 restore 得到的临时副本过期天数为1天
RestoreObjectRequest restoreObjectRequest = new RestoreObjectRequest(bucketName, key, 1);
// 设置恢复模式为 Standard，其他的可选模式包括 Expedited 和 Bulk，三种恢复模式在费用和速度上不一样
CASJobParameters casJobParameters = new CASJobParameters();
casJobParameters.setTier(Tier.Standard);
restoreObjectRequest.setCASJobParameters(casJobParameters);
cosclient.restoreObject(restoreObjectRequest);
```

## 生成预签名链接

COSClient 提供构造 生成预签名的 URL，可以分发给客户端, 用于下载或者上传。但注意如果您的文件是私有读权限，那么预签名链接只有一定的有效期。

- **方法原型**

```java
// 构造预签名URL
public URL generatePresignedUrl(GeneratePresignedUrlRequest req) throws CosClientException
```

- **参数说明**

| 参数名 | 参数描述     | 类型                        |
| ------ | ------------ | --------------------------- |
| req    | 预签名请求类 | GeneratePresignedUrlRequest |

Request 成员说明：

| Request 成员    | 设置方法            | 描述                                                         | 类型                    |
| --------------- | ------------------- | ------------------------------------------------------------ | ----------------------- |
| method          | 构造函数或 set 方法 | HTTP 方法，PUT(用于上传), GET(用于下载), DELETE(用于删除)    | HttpMethodName          |
| bucketName      | 构造函数或 set 方法 | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String                  |
| key             | 构造函数或 set 方法 | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg，详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String                  |
| expiration      | set 方法            | 签名过期的时间                                               | Date                    |
| contentType     | set 方法            | 要签名的请求中的 Content-Type                                | String                  |
| contentMd5      | set 方法            | 要签名的请求中的 Content-Md5                                 | String                  |
| responseHeaders | set 方法            | 签名的下载请求中要覆盖的返回的 HTTP 头                       | ResponseHeaderOverrides |

- **返回值**

URL

- **示例**

示例1：生成一个带签名的下载链接，示例代码如下：

```java
// 生成一个下载链接
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "mybucket-1251668577";
String key = "aaa.txt";
GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
// 设置签名过期时间(可选), 若未进行设置, 则默认使用 ClientConfig 中的签名过期时间(1小时)
// 这里设置签名在半个小时后过期
Date expirationDate = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);
req.setExpiration(expirationDate);
URL downloadUrl = cosClient.generatePresignedUrl(req);
String downloadUrlStr = downloadUrl.toString();
```

示例2：生成一个带签名的下载链接，并设置覆盖要返回的一些公共头部（比如content-type, content-language）， 示例代码如下：

```java
// bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 
String bucketName = "mybucket-1251668577";
String key = "aaa.txt";
GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
// 设置下载时返回的 http 头
ResponseHeaderOverrides responseHeaders = new ResponseHeaderOverrides();
String responseContentType = "image/x-icon";
String responseContentLanguage = "zh-CN";
String responseContentDispositon = "filename=\"abc.txt\"";
String responseCacheControl = "no-cache";
String cacheExpireStr =
        DateUtils.formatRFC822Date(new Date(System.currentTimeMillis() + 24L * 3600L * 1000L));
responseHeaders.setContentType(responseContentType);
responseHeaders.setContentLanguage(responseContentLanguage);
responseHeaders.setContentDisposition(responseContentDispositon);
responseHeaders.setCacheControl(responseCacheControl);
responseHeaders.setExpires(cacheExpireStr);
req.setResponseHeaders(responseHeaders);
// 设置签名过期时间(可选), 若未进行设置, 则默认使用 ClientConfig 中的签名过期时间(1小时)
// 这里设置签名在半个小时后过期
Date expirationDate = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);
req.setExpiration(expirationDate);
URL url = cosClient.generatePresignedUrl(req);
```

示例3：生成一些公有 bucket（匿名可读），不需要签名的连接，示例代码如下：

```java
// 生成匿名的请求签名，需要重新初始化一个匿名的 cosClient
// 1 初始化用户身份信息, 匿名身份不用传入ak sk
COSCredentials cred = new AnonymousCOSCredentials();
// 2 设置 bucket 的区域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成 cos 客户端
COSClient cosClient = new COSClient(cred, clientConfig);
// bucket 名需包含 appid
String bucketName = "mybucket-1251668577";

String key = "aaa.txt";
GeneratePresignedUrlRequest req =
        new GeneratePresignedUrlRequest(bucketName, key, HttpMethodName.GET);
URL url = cosClient.generatePresignedUrl(req);

System.out.println(url.toString());

cosClient.shutdown();
```

示例4：生成一些预签名的上传链接，可直接分发给客户端进行文件的上传，示例代码如下：

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "mybucket-1251668577";

String key = "aaa.txt";
// 设置签名过期时间(可选), 若未进行设置, 则默认使用 ClientConfig 中的签名过期时间(1小时)
// 这里设置签名在半个小时后过期
Date expirationTime = new Date(System.currentTimeMillis() + 30L * 60L * 1000L);
URL url = cosClient.generatePresignedUrl(bucketName, key, expirationTime, HttpMethodName.PUT);
```

## 生成签名

COSSigner 类 提供构造 COS 签名的方法，用于分发给移动端 SDK，进行文件的上传和下载。
签名的路径和分发后要进行操作的 key 相匹配。

- **方法原型**

```java
// 构造 COS 签名
public String buildAuthorizationStr(HttpMethodName methodName, String resouce_path,
        COSCredentials cred, Date expiredTime);

// 构造 COS 签名
// 第二个方法比第一个方法额外提供对部分 HTTP Header 和所有传入的 URL 中的参数进行签名。
// 用于更复杂的签名控制, 生成的签名必须在上传下载等操作时，也要携带对应的 header 和 param.
public String buildAuthorizationStr(HttpMethodName methodName, String resouce_path,
        Map<String, String> headerMap, Map<String, String> paramMap, COSCredentials cred,
        Date expiredTime);
```

- **参数说明**

| 参数名       | 参数描述                                                     | 类型           |
| ------------ | ------------------------------------------------------------ | -------------- |
| methodName   | HTTP 请求方法，可设置 PUT、GET、DELETE、HEAD、POST            | HttpMethodName |
| resouce_path | 要签名的路径, 同上传文件的 key，需要以`/`开始                | HttpMethodName |
| cred         | 密钥信息                                                     | COSCredentials |
| expiredTime  | 过期时间                                                     | Date           |
| headerMap    | 要签名的 HTTP Header map，只对传入的 Content-Type，Content-Md5 和以 x 开头的 header 进行签名 | Map            |
| paramMap     | 要签名的URL Param map                                        | Map            |

- **返回值**
String

- **示例**

示例1：生成一个上传签名

```java
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
COSSigner signer = new COSSigner();
//设置过期时间为1个小时
Date expiredTime = new Date(System.currentTimeMillis() + 3600L * 1000L);
// 要签名的 key, 生成的签名只能用于对应此 key 的上传
String key = "/aaa.txt";
String sign = signer.buildAuthorizationStr(HttpMethodName.PUT, key, cred, expiredTime);
```

示例2：生成一个下载签名

```java
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
COSSigner signer = new COSSigner();
//设置过期时间为1个小时
Date expiredTime = new Date(System.currentTimeMillis() + 3600L * 1000L);
// 要签名的 key, 生成的签名只能用于对应此key的下载
String key = "/aaa.txt";
String sign = signer.buildAuthorizationStr(HttpMethodName.GET, key, cred, expiredTime);
```

示例3：生成一个删除签名

```java
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
COSSigner signer = new COSSigner();
//设置过期时间为1 个小时
Date expiredTime = new Date(System.currentTimeMillis() + 3600L * 1000L);
// 要签名的 key, 生成的签名只能用于对应此 key 的删除
String key = "/aaa.txt";
String sign = signer.buildAuthorizationStr(HttpMethodName.DELETE, key, cred, expiredTime);
```

## 高级 API 文件上传（推荐）

高级 API 由类 TransferManger 通过封装上传以及下载接口，内部有一个线程池，接受用户的上传和下载请求，因此用户可选择异步的提交任务。

```java
// 线程池大小，建议在客户端与COS网络充足(如使用腾讯云的CVM，同地域上传COS)的情况下，设置成16或32即可, 可较充分的利用网络资源
// 对于使用公网传输且网络带宽质量不高的情况，建议减小该值，避免因网速过慢，造成请求超时。
ExecutorService threadPool = Executors.newFixedThreadPool(32);
// 传入一个 threadpool, 若不传入线程池, 默认 TransferManager 中会生成一个单线程的线程池。
TransferManager transferManager = new TransferManager(cosClient, threadPool);
// .....(提交上传下载请求, 如下文所属)
// 关闭 TransferManger
transferManager.shutdownNow();
```

### 上传文件

上传接口根据用户文件的长度自动选择简单上传以及分块上传， 降低用户的使用门槛。用户不用关心分块上传的每个步骤。

Tips 有关其他一些设置属性，存储类别，MD5 校验等可参考 Put Object Api。

- **方法原型**

```java
// 上传文件
public Upload upload(final PutObjectRequest putObjectRequest)
            throws CosServiceException, CosClientException;
```

- **参数说明**

| 参数名           | 参数描述     | 参数类型         |
| ---------------- | ------------ | ---------------- |
| putObjectRequest | 上传文件请求 | PutObjectRequest |

Request 成员说明：

| Request 成员 | 设置方法            | 描述                                                         | 类型           |
| ------------ | ------------------- | ------------------------------------------------------------ | -------------- |
| bucketName   | 构造函数或 set 方法 | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String         |
| key          | 构造函数或 set 方法 | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String         |
| file         | 构造函数或 set 方法 | 本地文件                                                     | File           |
| input        | 构造函数或 set 方法 | 输入流                                                       | InputStream    |
| metadata     | 构造函数或 set 方法 | 文件的元信息                                                 | ObjectMetadata |

- **返回值**
  - 成功：返回 Upload，可以查询上传是否结束，也可同步的等待上传结束。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
String key = "/mypic.jpg";
File localFile = new File("/data/dog.jpg");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, file);
// 本地文件上传
Upload upload = transferManager.upload(putObjectRequest);
 // 等待传输结束（如果想同步的等待上传结束，则调用 waitForCompletion）
UploadResult uploadResult = upload.waitForUploadResult();
```

### 下载文件

将 COS 上的文件下载到本地。

- **方法原型**

```java
// 下载文件
public Download download(final GetObjectRequest GetObjectRequest, final File file);
```

- **参数说明**

| 参数名           | 参数描述           | 参数类型         |
| ---------------- | ------------------ | ---------------- |
| getObjectRequest | 下载文件请求       | GetObjectRequest |
| file             | 要下载到的本地文件 | File             |

Request 成员说明：

| Request 成员 | 设置方法            | 描述                                                         | 类型   |
| ------------ | ------------------- | ------------------------------------------------------------ | ------ |
| bucketName   | 构造函数或 set 方法 | bucket 的命名规则为{name}-{appid} ，name 由字母数字和中划线构成 | String |
| key          | 构造函数或 set 方法 | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |
| range        | set 方法            | 下载的 range 范围                                            | Long[] |

- **返回值**
  - 成功：返回 Download，可以查询下载是否结束，也可同步的等待下载结束。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// bucket的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String bucketName = "movie-1251668577";
String key = "/mypic.jpg";
File localDownFile = new File("/data/dog.jpg");
GetObjectRequest getObjectRequest = new GetObjectRequest(bucket, key);
// 下载文件
Download download = transferManager.download(getObjectRequest, localDownFile);
 // 等待传输结束（如果想同步的等待上传结束，则调用 waitForCompletion）
download.waitForCompletion();
```

### 拷贝文件

copy 接口支持根据文件大小自动选择 copy 或者分块 copy. 用户不用关心 copy 的文件大小。

- **方法原型**

```java
// 上传文件
public Copy copy(final CopyObjectRequest copyObjectRequest);
```

- **参数说明**

| 参数名            | 参数描述     | 参数类型          |
| ----------------- | ------------ | ----------------- |
| copyObjectRequest | 拷贝文件请求 | CopyObjectRequest |

Request 成员说明：

| 参数名                | 参数描述                                                     | 类型   |
| --------------------- | ------------------------------------------------------------ | ------ |
| sourceBucketRegion    | 源 Bucket Region 。默认值：与当前 clientconfig 的 region 一致, 表示统一地域拷贝 | String |
| sourceBucketName      | 源 Bucket 名，bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String |
| sourceKey             | 源对象键，对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg，详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |
| sourceVersionId       | 源文件 version id（适用于开启了版本控制的源 Bucket）。默认值：源文件当前最新版本 | String |
| destinationBucketName | 目的 Bucket 名, bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式 | String |
| destinationKey        | 目的对象键，对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg` 中，对象键为 doc1/pic1.jpg, 详情参考 [对象键](https://cloud.tencent.com/document/product/436/13324) | String |
| storageClass          | 拷贝的目的文件的存储类型。枚举值：Standard，Standard_IA。默认值：Standard | String |

- **返回值**
  - 成功：返回 Copy，可以查询 Copy 是否结束，也可同步的等待上传结束。
  - 失败：发生错误（如身份认证失败），抛出异常 CosClientException 或者 CosServiceException。具体请参照异常类说明。
- **示例**

```java
// 要拷贝的 bucket region, 支持跨地域拷贝
Region srcBucketRegion = new Region("ap-shanghai");
// 源 bucket, bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String srcBucketName = "srcBucket-1251668577";
// 要拷贝的源文件
String srcKey = "aaa/bbb.txt";
// 目的 bucket, bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
String destBucketName = "destBucket-1251668577";
// 要拷贝的目的文件
String destKey = "ccc/ddd.txt";

// 生成用于获取源文件信息的 srcCOSClient
COSClient srcCOSClient = new COSClient(cred, new ClientConfig(srcBucketRegion));
CopyObjectRequest copyObjectRequest = new CopyObjectRequest(srcBucketRegion, srcBucketName,
        srcKey, destBucketName, destKey);
try {
    Copy copy = transferManager.copy(copyObjectRequest, srcCOSClient, null);
    // 返回一个异步结果 copy, 可同步的调用 waitForCopyResult 等待 copy 结束, 成功返回 CopyResult, 失败抛出异常.
    CopyResult copyResult = copy.waitForCopyResult();
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
} catch (InterruptedException e) {
    e.printStackTrace();
}
```

## 权限设置

COS 中的权限通过 SET/GET Object ACL 以及 SET/GET Bucket ACL 来进行设置与获取。主要的两个类为 AccessControlList 以及 CannedAccessList 来设置与获取。 object 默认继承 bucket 权限, 目前 COS 对一个账号(appid)仅支持设置1000条的 ACL, 因此建议只对个别和 bucket 权限不一致的 object 设置 ACL，避免权限数量超过阈值，支持无上限的 acl 功能目前正在开发中。

### AccessControlList

自定义访问控制策略，用于设置对某个用户的策略控制。

AccessControlList 类成员

| 成员名         | 描述                            | 类型     |
| -------------- | ------------------------------- | -------- |
| List&lt;Grant> | 包含所有要授权的信息            | 数组     |
| owner          | 表示 Object 或者 Owner 的拥有者 | Owner 类 |

Grant 类成员

| 成员名     | 描述                                       | 类型       |
| ---------- | ------------------------------------------ | ---------- |
| grantee    | 被授权人的身份信息                         | Grantee    |
| permission | 被授权的权限信息（如可读，可写，可读可写） | Permission |

Owner 类成员

| 成员名      | 描述                           | 类型   |
| ----------- | ------------------------------ | ------ |
| id          | 拥有者的身份信息               | String |
| displayname | 拥有者的名字（目前和 ID 相同） | String |

- **示例**

```java
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

// 授权给根账户73410000可读可写权限
UinGrantee uinGrantee1 = new UinGrantee("qcs::cam::uin/73410000:uin/73410000");
acl.grantPermission(uinGrantee1, Permission.FullControl);
// 授权给 2779643970 的子账户 72300000 可读权限
UinGrantee uinGrantee2 = new UinGrantee("qcs::cam::uin/2779643970:uin/72300000");
acl.grantPermission(uinGrantee2, Permission.Read);
// 授权给 2779643970 的子账户 7234444 可写权限
UinGrantee uinGrantee3 = new UinGrantee("qcs::cam::uin/7234444:uin/7234444");
acl.grantPermission(uinGrantee3, Permission.Write);

// 设置 object 的 acl
cosClient.setObjectAcl(bucket, key, acl);

```

### CannedAccessControlList

CannedAccessControlList 表示预设的策略，针对的是所有人。是一个枚举类，枚举值如下所示。

| 枚举值          | 描述                                             |
| --------------- | ------------------------------------------------ |
| Private         | 私有读写（仅有 owner 可以读写）                  |
| PublicRead      | 公有读私有写（ owner 可以读写， 其他客户可以读） |
| PublicReadWrite | 公有读写（即所有人都可以读写）                   |

## 客户端加密

Java sdk 支持客户端加密, 将文件加密后再进行上传, 并在下载时进行解密。客户端加密支持对称 AES 与非对称 RSA 加密。
这里的对称和非对称只是用来加密每次生成的随机密钥, 对文件数据的加密始终使用 AES256 对称加密.
客户端加密适用于存储敏感数据的客户，客户端加密会牺牲部分上传速度，SDK 内部对于分块上传会使用串行的方式进行上传。

### 使用客户端加密前准备事项

客户端加密内部使用 AES256 来对数据进行加密，默认 JDK6 - JDK8 早期的版本不支持256位加密，如果运行时会报出以下异常`java.security.InvalidKeyException: Illegal key size or default parameters`。那么我们需要补充 oracle 的 JCE 无政策限制权限文件，将其部署在 JRE 的环境中。 请根据目前使用的 JDK 版本，分别下载对应的文件，将其解压后保存在 JAVA_HOME下的 jre/lib/security目录下。

1. [JDK6 JCE 补充包](http://www.oracle.com/technetwork/java/javase/downloads/jce-6-download-429243.html)
2. [JDK7 JCE 补充包](http://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html)
3. [JDK8 JCE 补充包](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html)

### 上传加密流程

1. 每次上传一个文件对象前，我们随机生成一个对称加密密钥，随机生成的密钥通过用户的提供的对称或非对称密钥进行加密，将加密后的结果 base64 编码存储在对象的元信息中。
2. 进行文件对象的上传，上传时在内存使用 AES256 算法加密。

### 下载解密流程

1. 获取文件元信息中加密必要的信息，base64 解码后使用用户密钥进行解密，得到当时加密数据的密钥
2. 使用密钥对下载输入流进行使用 AES256 解密，得到解密后的文件输入流。


- **示例**

示例1：使用对称 AES256 加密每次生成的随机密钥示例，完整的示例代码请参考 [客户端对称密钥加密完整示例](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/SymmetricKeyEncryptionClientDemo.java)。

```java
// 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXXXXXXXXXX",
		"YYZZZZZZZZZZZZZZZZZ");
// 设置 bucket 的区域, COS 地域的简称请参照 https://www..com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));

// 加载保存在文件中的密钥, 如果不存在，请先使用 buildAndSaveSymmetricKey 生成密钥
// buildAndSaveSymmetricKey();
SecretKey symKey = loadSymmetricAESKey();

EncryptionMaterials encryptionMaterials = new EncryptionMaterials(symKey);
// 使用 AES/GCM 模式，并将加密信息存储在文件元信息中.
CryptoConfiguration cryptoConf = new CryptoConfiguration(CryptoMode.AuthenticatedEncryption)
		.withStorageMode(CryptoStorageMode.ObjectMetadata);

// 生成加密客户端 EncryptionClient, COSEncryptionClient 是 COSClient 的子类, 所有 COSClient 支持的接口他都支持。
// EncryptionClient 覆盖了 COSClient 上传下载逻辑，操作内部会执行加密操作，其他操作执行逻辑和 COSClient 一致
COSEncryptionClient cosEncryptionClient =
		new COSEncryptionClient(new COSStaticCredentialsProvider(cred),
				new StaticEncryptionMaterialsProvider(encryptionMaterials), clientConfig,
				cryptoConf);

// 上传文件
// 这里给出 putObject 的示例, 对于高级 API 上传，只用在生成TransferManager时传入COSEncryptionClient对象即可
String bucketName = "mybucket-1251668577";
String key = "xxx/yyy/zzz.txt";
File localFile = new File("src/test/resources/plain.txt");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
cosEncryptionClient.putObject(putObjectRequest);
```

示例2：使用非对称 RSA 加密每次生成的随机密钥示例，完整的示例代码请参考 [客户端非对称密钥加密完整示例](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/AsymmetricKeyEncryptionClientDemo.java)。

```java
// 初始化用户身份信息(secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXXXXXXXXXXXXXX",
		"YYZZZZZZZZZZZZZZZZZZ");
// 设置bucket的区域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));


// 加载保存在文件中的密钥, 如果不存在，请先使用 buildAndSaveAsymKeyPair 生成密钥
buildAndSaveAsymKeyPair();
KeyPair asymKeyPair = loadAsymKeyPair();

EncryptionMaterials encryptionMaterials = new EncryptionMaterials(asymKeyPair);
// 使用AES/GCM模式，并将加密信息存储在文件元信息中.
CryptoConfiguration cryptoConf = new CryptoConfiguration(CryptoMode.AuthenticatedEncryption)
		.withStorageMode(CryptoStorageMode.ObjectMetadata);

// 生成加密客户端EncryptionClient, COSEncryptionClient是COSClient的子类, 所有COSClient支持的接口他都支持。
// EncryptionClient覆盖了COSClient上传下载逻辑，操作内部会执行加密操作，其他操作执行逻辑和COSClient一致
COSEncryptionClient cosEncryptionClient =
		new COSEncryptionClient(new COSStaticCredentialsProvider(cred),
				new StaticEncryptionMaterialsProvider(encryptionMaterials), clientConfig,
				cryptoConf);

// 上传文件
// 这里给出putObject的示例, 对于高级API上传，只用在生成TransferManager时传入COSEncryptionClient对象即可
String bucketName = "mybucket-1251668577";
String key = "xxx/yyy/zzz.txt";
File localFile = new File("src/test/resources/plain.txt");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
cosEncryptionClient.putObject(putObjectRequest);
```

## 异常说明

SDK 失败时，抛出的异常皆是 RuntimeExcpetion，目前 SDK 常见的异常有 CosClientException， CosServiceException 和 IllegalArgumentException。

### CosClientException

客户端异常，用于指因为客户端原因导致无法和服务端完成正常的交互而导致的失败，如客户端无法连接到服务端，无法解析服务端返回的数据，读取本地文件发生 IO 异常等。CosClientException 集成自 RuntimeException，没有自定义的成员变量，使用方法同 RuntimeException。

### CosServiceException

CosServiceException 服务异常，用于指交互正常完成，但是操作失败的场景。例如客户端访问一个不存在 Bucket，删除一个不存在的文件，没有权限进行某个操作， 服务端故障异常等。CosServiceException 包含了服务端返回的状态码，requestid，出错明细等。捕获异常后，建议对整个异常进行打印，异常包含了必须的排查因素。以下是异常成员变量的描述：

| request 成员 | 描述                                                         | 类型      |
| ------------ | ------------------------------------------------------------ | --------- |
| requestId    | 请求 ID， 用于表示一个请求， 对于排查问题十分重要            | String    |
| traceId      | 辅助排查问题的 ID，                                          | String    |
| statusCode   | response 的 status 状态码， 4xx 是指请求因客户端而失败， 5xx 是服务端异常导致的失败。 请参照 [COS 错误信息](https://cloud.tencent.com/document/product/436/7730) | String    |
| errorType    | 枚举类， 表示异常的种类， 分为 Client， Service， Unknown    | ErrorType |
| errorCode    | 请求失败时 body 返回的 Error Code 请参照 [COS 错误信息](https://cloud.tencent.com/document/product/436/7730) | String    |
| errorMessage | 请求失败时 body 返回的 Error Message  请参照 [COS 错误信息](https://cloud.tencent.com/document/product/436/7730) | String    |

## 常见问题

若您在使用 Java SDK 过程中，有相关的疑问，请参阅 [常见问题](https://cloud.tencent.com/document/product/436/30746#java-sdk-.E7.B1.BB.E9.97.AE.E9.A2.98) 文档 Java SDK 部分。
