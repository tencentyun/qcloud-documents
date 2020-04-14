>!您目前查阅的是历史版本 SDK 文档，已不再更新和维护，我们建议您查阅新版 [SDK 文档](https://cloud.tencent.com/document/product/436/6474)。

## 开发准备

### 相关资源

[cos java sdk v4 github ](https://github.com/tencentyun/cos-java-sdk-v4) 项目。

### 环境依赖

JDK 1.7（本版本 SDK 基于 JSON API 封装组成）。

### 安装 SDK

- maven 安装。
pom.xml 添加依赖
```xml
<dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cos_api</artifactId>
            <version>4.7</version>
</dependency>
```

- 源码安装。
从 [cos java sdk v4 github](https://github.com/tencentyun/cos-java-sdk-v4) 下载源码。

### 卸载SDK

删除 pom 依赖或源码。

### 历史版本

4.2版本是针对 COS 4.X系统，接口与3.x的基本一致，如果需要使用历史版本，请参见 [cos java sdk v3 github](https://github.com/tencentyun/cos-java-sdk/tree/master)。

## 生成客户端对象

### 初始化密钥信息

```java
long appId = 1000000;
String secretId = "xxxxxxxxxxxxxxxxxxxxxxxxxxx";
String secretKey = "xxxxxxxxxxxxxxxxxxxxxxxxxx";
// 设置要操作的bucket
String bucketName = "xxxxxxxxx";
// 初始化密钥信息
Credentials cred = new Credentials(appId, secretId, secretKey);
```

### 初始化客户端配置（如设置园区）

```java
// 初始化客户端配置
ClientConfig clientConfig = new ClientConfig();
// 设置bucket所在的区域，例如华南园区：gz； 华北园区：tj；华东园区：sh ；
clientConfig.setRegion("gz");
```

### 生成客户端

```java
// 初始化cosClient
COSClient cosClient = new COSClient(clientConfig, cred);
```

## 文件操作

### 上传文件

#### 方法原型

```java
String uploadFile(UploadFileRequest request);
```

#### 参数说明

|   参数名   |        类型         | 默认值  |   参数描述   |
| :-----: | :---------------: | :--: | :------: |
| request | UploadFileRequest |  无   | 上传文件类型请求 |

|    request成员    |       类型        |         默认值         |    设置方法    |                    描述                    |
| :-------------: | :-------------: | :-----------------: | :--------: | :--------------------------------------: |
|   bucketName    |     String      |          无          | 构造函数或 set 方法 |                 bucket名称                 |
|     cosPath     |     String      |          无          | 构造函数或 set 方法 | cos路径, 必须从 bucket 下的根`/`开始，文件路径不能以`/`结尾, 例如 `/mytest/demo.txt` |
|    localPath    |     String      |          无          | 构造函数或 set 方法 |             通过磁盘文件上传的本地绝对路径              |
|  contentBufer   |     byte[]      |          无          | 构造函数或 set 方法 |             通过内存上传的 buffer 内容              |
|     bizAttr     |     String      |          空          | 构造函数或 set 方法 | 文件的备注，主要用于对该文件用途的描述     |
| enableShaDigest |     boolean     |        false        |   set 方法    | 是否计算 sha 摘要，如果开启 sha，并且 bucket 下有相同内容文件，则会触发秒传。sha 计算会耗费一定的 CPU 和时间，建议大文件不开启 |
|     taskNum     |       int       |         16          |   set 方法    |      文件上传的并发数                 |

#### 返回值

| 返回值类型  |                  返回值描述                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess, 'data':\$data}，code 为0表示成功，message 为 SUCCESS 或者失败原因，data中包含相关的属性，详情请参见返回值模块 |

#### 示例

```java
UploadFileRequest uploadFileRequest = new UploadFileRequest(bucketName, 		"/sample_file.txt", "local_file_1.txt");
String uploadFileRet = cosClient.uploadFile(uploadFileRequest);
```



### 下载文件

#### 方法原型

```java
String getFileLocal(GetFileLocalRequest request);
```

#### 参数说明

|   参数名   |        参数类型         | 默认值  |  参数描述  |
| :-----: | :-----------------: | :--: | :----: |
| request | GetFileLocalRequest |  无   | 下载文件请求 |

**request 成员**

| request 成员  |   类型    |      默认值       |    设置方法    |                    描述                    |
| :--------: | :-----: | :------------: | :--------: | :--------------------------------------: |
| bucketName | String  |       无        | 构造函数或 set 方法 |                 bucket 名称                 |
|  cosPath   | String  |       无        | 构造函数或 set 方法 | cos 路径，必须从 bucket 下的根`/`开始，文件路径不能以`/`结尾，例如 `/mytest/demo.txt` |
| localPath  | String  |       无        | 构造函数或 set 方法 |                要下载到的本地路径                 |
|   useCDN   | boolean |      true      |   set 方法    |               是否通过 CDN 进行下载                |
|  referer   | String  |       空串       |   set 方法    |     设置 Referer（针对开启了 refer 防盗链的 bucket）      |
| rangeStart |  long   |       0        |   set 方法    |          要下载的字节起始，参见 HTTP Range           |
|  rangeEnd  |  long   | Long.MAX_VALUE |   set 方法    |          下载的字节结束，参见 HTTP Range           |

#### 示例

```java
String localPathDown = "src/test/resources/local_file_down.txt";
GetFileLocalRequest getFileLocalRequest =
  new GetFileLocalRequest(bucketName, cosFilePath, localPathDown);
getFileLocalRequest.setUseCDN(false);
getFileLocalRequest.setReferer("*.myweb.cn");
String getFileResult = cosClient.getFileLocal(getFileLocalRequest);
```



### 移动文件

#### 方法原型

```java
String moveFile(MoveFileRequest request);
```

#### 参数说明

|   参数名   |      参数类型       | 默认值  |  参数描述  |
| :-----: | :-------------: | :--: | :----: |
| request | MoveFileRequest |  无   | 移动文件请求 |

**request 成员**

| request成员  |   类型   |         默认值         |       设置方法        |                    描述                    |
| :--------: | :----: | :-----------------: | :---------------: | :--------------------------------------: |
| bucketName | String |          无          |    构造函数或set方法     |                 bucket名称                 |
|  cosPath   | String |          无          |    构造函数或set方法     | cos路径，必须从bucket下的根`/`开始，文件路径不能以`/`结尾, 例如 `/mytest/demo.txt` |
| dstCosPath | String |          无          |    构造函数或set方法     | 移动文件的目标地址，必须从bucket下的根`/`开始，文件路径不能以/结尾，例如`/mytest/demo.txt.move` |
| overWrite  |  枚举类型  | NO_OVER_WRITE (不覆盖) | set 方法 setOverWrite |       在移动的目标文件存在时，选择不覆盖还是覆盖，默认不覆盖        |

#### 示例

```java
String cosFilePath = "/sample_file.txt";
String dstCosFilePath = "/sample_file.txt.bak";
MoveFileRequest moveRequest =
  new MoveFileRequest(bucketName, cosFilePath, dstCosFilePath);
String moveFileResult = cosClient.moveFile(moveRequest);
```



### 获取文件属性

#### 方法原型

```java
String statFile(StatFileRequest request);
```

#### 参数说明

|   参数名   |      参数类型       | 默认值  |   参数描述   |
| :-----: | :-------------: | :--: | :------: |
| request | StatFileRequest |  无   | 获取文件属性请求 |

| request成员  |   类型   | 默认值  |    设置方法    |                    描述                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  无   | 构造函数或 set 方法 |                 bucket 名称                 |
|  cosPath   | String |  无   | 构造函数或 set 方法 | cos路径，必须从 bucket 下的根`/`开始，文件路径不能以`/`结尾，例如 `/mytest/demo.txt` |

#### 返回值

| 返回值类型  |                  返回值描述                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess, 'data':\$data}，code 为0表示成功，message 为 SUCCESS 或者失败原因，data 中包含相关的属性，详情请参见返回值模块 |

#### 示例

```java
StatFileRequest statFileRequest = new StatFileRequest(bucketName, "/sample_file.txt");
String statFileRet = cosClient.statFile(statFileRequest);
```



### 更新文件属性

#### 方法原型

```java
String updateFile(UpdateFileRequest request);
```

#### 参数说明

|   参数名   |       参数类型        | 默认值  |   参数描述   |
| :-----: | :---------------: | :--: | :------: |
| request | UpdateFileRequest |  无   | 更新文件属性请求 |

**request 成员**


|     request 成员      |     类型      | 默认值  |    设置方法    |                    描述                    |
| :----------------: | :---------: | :--: | :--------: | :--------------------------------------: |
|     bucketName     |   String    |  无   | 构造函数或 set 方法 |                 bucket 名称                 |
|      cosPath       |   String    |  无   | 构造函数或 set 方法 | cos 路径, 必须从 bucket 下的根`/`开始，文件路径不能以`/`结尾，例如 `/mytest/demo.txt` |
|      bizAttr       |   String    |  无   |   set 方法    |           文件的备注，主要用于对改文件用途的描述            |
|     authority      | String (枚举) |  无   |   set 方法    | 文件权限，默认是继承 bucket 的权限合法取值: eInvalid（继承bucket），eWRPrivate（私有读写）， eWPrivateRPublic（私有写, 公有读） |
|    cacheControl    |   String    |  无   |   set 方法    |           参见 HTTP 的 Cache-Control           |
|    contentType     |   String    |  无   |   set 方法    |           参见 HTTP 的 Content-Type            |
|  contentLanguage   |   String    |  无   |   set 方法    |         参见 HTTP 的 Content-Language          |
| contentDisposition |   String    |  无   |   set 方法    |        参见 HTTP 的 Content-Disposition        |
|    x-cos-meta-     |   String    |  无   |   set 方法    | 自定义 HTTP 头，参数必须以 x-cos-meta-开头，值由用户定义，可设置多个 |

**tips:** 更新属性可以选择其中的某几个，对于HTTP头部cache_control，content_type, content_disposition 和 x-cos-meta-，如果本次只更新其中的某几个，其他的都会被抹掉，即这4个属性是整体更新。

#### 返回值

| 返回值类型  |                  返回值描述                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess}，code为0表示成功，message 为 SUCCESS 或者失败原因，详情请参见返回值模块 |

#### 示例

```java
UpdateFileRequest updateFileRequest = new UpdateFileRequest(bucketName, "/sample_file.txt");

updateFileRequest.setBizAttr("测试目录");
updateFileRequest.setAuthority(FileAuthority.WPRIVATE);
updateFileRequest.setCacheControl("no cache");
updateFileRequest.setContentDisposition("cos_sample.txt");
updateFileRequest.setContentLanguage("english");
updateFileRequest.setContentType("application/json");
updateFileRequest.setXCosMeta("x-cos-meta-xxx", "xxx");
updateFileRequest.setXCosMeta("x-cos-meta-yyy", "yyy");

String updateFileRet = cosClient.updateFile(updateFileRequest);
```



### 删除文件

#### 方法原型

```java
String delFile(DelFileRequest request);
```

#### 参数说明

|   参数名   |      参数类型      | 默认值  |  参数描述  |
| :-----: | :------------: | :--: | :----: |
| request | DelFileRequest |  无   | 删除文件请求 |

**request 成员**

| request 成员  |   类型   | 默认值  |    设置方法    |                    描述                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  无   | 构造函数或 set 方法 |                 bucket 名称                 |
|  cosPath   | String |  无   | 构造函数或 set 方法 | cos 路径, 必须从 bucket 下的根`/`开始，文件路径不能以`/`结尾, 例如` /mytest/demo.txt` |

#### 返回值

| 返回值类型  |                  返回值描述                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess}, code 为0表示成功，message 为 SUCCESS 或者失败原因，详情请参见返回值模块 |

#### 示例

```java
DelFileRequest delFileRequest = new DelFileRequest(bucketName, "/sample_file_move.txt");
String delFileRet = cosClient.delFile(delFileRequest);
```


## 目录操作

### 创建目录

#### 方法原型

```java
String createFolder(CreateFolderRequest request);	
```

#### 参数说明

|   参数名   |        参数类型         | 默认值  |  参数描述  |
| :-----: | :-----------------: | :--: | :----: |
| request | CreateFolderRequest |  无   | 创建目录请求 |

**request 成员**

| request 成员  |   类型   | 默认值  |    设置方法    |                    描述                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  无   | 构造函数或 set 方法 |                 bucket 名称                 |
|  cosPath   | String |  无   | 构造函数或 set 方法 | cos路径，必须从 bucket 下的根`/`开始，目录路径必须以`/`结尾, 例如 `/mytest/dir/` |
|  bizAttr   | String |  空   |   set方法    |            目录的备注，主要用于对目录用途的描述            |

#### 返回值

| 返回值类型  |                  返回值描述                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess}，code 为0表示成功，message 为 SUCCESS 或者失败原因，详情请参见返回值模块 |

#### 示例

```java
CreateFolderRequest createFolderRequest = new CreateFolderRequest(bucketName, "/sample_folder/");
String createFolderRet = cosClient.createFolder(createFolderRequest);
```



### 获取目录属性

#### 方法原型

```java
String statFolder(StatFolderRequest request);
```

#### 参数说明

|   参数名   |       参数类型        | 默认值  |   参数描述   |
| :-----: | :---------------: | :--: | :------: |
| request | StatFolderRequest |  无   | 获取目录属性请求 |

**request 成员**

| request 成员  |   类型   | 默认值  |    设置方法    |                    描述                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  无   | 构造函数或set方法 |                 bucket名称                 |
|  cosPath   | String |  无   | 构造函数或set方法 | cos路径，必须从 bucket 下的根`/`开始，目录路径必须以`/`结尾，例如 `/mytest/dir/` |

#### 返回值

| 返回值类型  |                  返回值描述                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess, 'data':\$data}，code 为0表示成功，message 为 SUCCESS 或者失败原因，data 中包含相关的属性，详情请参见返回值模块 |

#### 示例

```java
StatFolderRequest statFolderRequest = new StatFolderRequest(bucketName, "/sample_folder/");
String statFolderRet = cosClient.statFolder(statFolderRequest);
```



### 更新目录属性

#### 方法原型

```java
String updateFolder(UpdateFolderRequest request);
```

#### 参数说明

|   参数名   |        参数类型         | 默认值  |   参数描述   |
| :-----: | :-----------------: | :--: | :------: |
| request | UpdateFolderRequest |  无   | 更新目录属性请求 |

**request 成员**

| request 成员  |   类型   | 默认值  |    设置方法    |                    描述                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  无   | 构造函数或 set 方法 |                 bucket 名称                 |
|  cosPath   | String |  无   | 构造函数或 set 方法 | cos路径，必须从 bucket 下的根`/`开始，目录路径必须以`/`结尾, 例如 `/mytest/dir/` |
|  bizAttr   | String |  空   |   set 方法    |            目录的备注，主要用于对目录用途的描述            |

#### 返回值

| 返回值类型  |                  返回值描述                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess}，code 为0表示成功，message 为 SUCCESS 或者失败原因，详情请参见返回值模块 |

#### 示例

```java
UpdateFolderRequest updateFolderRequest = new UpdateFolderRequest(bucketName, "/sample_folder/");
updateFolderRequest.setBizAttr("这是一个测试目录");
String updateFolderRet = cosClient.updateFolder(updateFolderRequest);
```



### 获取目录列表

#### 方法原型

```java
String listFolder(ListFolderRequest request);
```

#### 参数说明

|   参数名   |       参数类型        | 默认值  |   参数描述   |
| :-----: | :---------------: | :--: | :------: |
| request | ListFolderRequest |  无   | 获取目录成员请求 |

**request 成员**

| request 成员  |   类型   | 默认值  |    设置方法    |                    描述                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  无   | 构造函数或 set 方法 |                 bucket 名称                 |
|  cosPath   | String |  无   | 构造函数或 set 方法 | cos 路径, 必须从 bucket 下的根`/`开始，目录路径必须以`/`结尾, 例如 `/mytest/dir/` |
|    num     |  int   | 199  | 构造函数或 set 方法 |             获取列表成员的数量，最大为199             |
|   prefix   | String |  空   | 构造函数或 set 方法 | 搜索成员的前缀, 例如 prefix 为 test 表示只搜索以 test 开头的文件或目录 |
|  context   | String |  空   | 构造函数或 set 方法 | 搜索上下文, 由上一次 list 的结果返回，作为这一次搜索的起点，用于循环获取一个目录下的所有成员 |

#### 返回值

| 返回值类型  |                  返回值描述                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess, 'data':\$data}，code 为0表示成功，message 为 SUCCESS 或者失败原因，data 中包含成员列表，详情请参见返回值模块 |

#### 示例

```java
ListFolderRequest listFolderRequest = new ListFolderRequest(bucketName, "/sample_folder/");
String listFolderRet = cosClient.listFolder(listFolderRequest);
```



### 删除目录

#### 方法原型

```java
String delFolder(DelFolderRequest request);
```

#### 参数说明

|   参数名   |       参数类型       | 默认值  |  参数描述  |
| :-----: | :--------------: | :--: | :----: |
| request | DelFolderRequest |  无   | 删除目录请求 |

| request成员  |   类型   | 默认值  |    设置方法    |                    描述                    |
| :--------: | :----: | :--: | :--------: | :--------------------------------------: |
| bucketName | String |  无   | 构造函数或 set 方法 |                 bucket 名称                 |
|  cosPath   | String |  无   | 构造函数或 set 方法 | cos 路径, 必须从 bucket 下的根`/`开始，目录路径必须以`/`结尾, 例如 `/mytest/dir/` |

#### 返回值

| 返回值类型  |                  返回值描述                   |
| :----: | :--------------------------------------: |
| String | {'code':\$code,  'message':$mess}，code为 0 表示成功,  message 为 SUCCESS 或者失败原因，详情请参见返回值模块 |

#### 示例

```java
DelFolderRequest delFolderRequest = new DelFolderRequest(bucketName, "/sample_folder/");
String delFolderRet = cosClient.delFolder(delFolderRequest);
```


## 签名管理

签名模块提供了生成多次签名、单次签名和下载签名的接口，其中多次签名和单次签名在文件和目录操作的api内部使用，用户不用关心，下载签名用于方便用户生成下载私有 bucket 的文件签名。

### 多次签名

```java
String getPeriodEffectiveSign(String bucketName, String cosPath, Credentials cred, long expired)
```

#### 使用场景

上传文件，重命名文件，创建目录，获取文件目录属性，拉取目录列表。

#### 参数说明

| 参数名      |    参数类型     | 默认值  |                 参数描述                 |
| -------- | :---------: | :--: | :----------------------------------: |
| bucket   |   String    |  无   |               bucket 名称               |
| cos_path |   String    |  无   |              要签名的 cos 路径               |
| cred     | Credentials |  无   | 用户身份信息，包括 appid，secretId，secretkey |
| expired  |    long     |  无   |           签名过期时间，UNIX时间戳            |

#### 返回值

base64 编码的字符串。

#### 示例

```java
Credentials cred = new Credentials(appId, secretId, secretKey);
long expired = System.currentTimeMillis() / 1000 + 600;
String signStr = Sign.getPeriodEffectiveSign(bucketName, "/pic/test.jpg", cred, expired);
```

### 单次签名

```java
String getOneEffectiveSign(String bucketName, String cosPath, Credentials cred)
```

#### 使用场景

删除和更新文件目录。

#### 参数说明

|   参数名    |    参数类型     | 默认值  |                 参数描述                 |
| :------: | :---------: | :--: | :----------------------------------: |
|  bucket  |   unicode   |  无   |               bucket名称               |
| cos_path |   unicode   |  无   |              要签名的cos路径               |
|   cred   | Credentials |  无   | 用户身份信息，包括 appid，secretId，secretkey |

#### 返回值

base64 编码的字符串。

#### 示例

```java
Credentials cred = new Credentials(appId, secretId, secretKey);
String signStr = Sign.getOneEffectiveSign(bucketName, "/pic/test.jpg", cred);
```

### 下载签名

```java
String getDownLoadSign(String bucketName, String cosPath, Credentials cred, long expired)
```

#### 使用场景

生成文件的下载签名，用于下载私有 bucket 的文件。

#### 参数说明

|   参数名    |    参数类型     | 默认值  |                 参数描述                 |
| :------: | :---------: | :--: | :----------------------------------: |
|  bucket  |   unicode   |  无   |               bucket 名称               |
| cos_path |   unicode   |  无   |              要签名的 cos 路径               |
|   cred   | Credentials |  无   | 用户身份信息，包括 APPID，SecretId，Secretkey |
| expired  |    long     |  无   |           签名过期时间， UNIX 时间戳            |

#### 返回值

base64 编码的字符串。

#### 示例

```java
Credentials cred = new Credentials(appId, secretId, secretKey);
long expired = System.currentTimeMillis() / 1000 + 600;
String signStr = Sign.getDownLoadSign(bucketName, "/pic/test.jpg", cred, expired);
```



## 返回值

| code |                  含义                  |
| :--: | :----------------------------------: |
|  0   |                 操作成功                 |
|  -1  | 输入参数错误，例如输入的本地文件路径不存在，cos 文件路径不符合规范 |
|  -2  |             网络错误，例如404等              |
|  -3  |           连接 cos 时发生异常，如连接超时           |
