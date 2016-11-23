## 开发准备

### SDK获取

对象存储服务 Java SDK下载地址：[github项目](https://github.com/tencentyun/cos-java-sdk)

### 开发环境

JDK 1.7

### SDK配置

- maven安装

pom.xml 添加依赖

```xml
<dependency>
            <groupId>com.qcloud</groupId>
            <artifactId>cos_api</artifactId>
            <version>3.3</version>
</dependency>
```

- 源码安装

从[github](https://github.com/tencentyun/cos-java-sdk)下载源码

### 卸载SDK

删除pom依赖或[源码](https://github.com/tencentyun/cos-java-sdk/tree/master)

## 文件操作

### 上传文件

#### 方法原型

```java
String uploadFile(UploadFileRequest request);
```

#### 参数说明

| 参数名     | 类型                | 默认值  | 参数描述     |
| :------ | :---------------- | :--- | :------- |
| request | UploadFileRequest | 无    | 上传文件类型请求 |

| request成员  | 类型              | 默认值                 | 设置方法       | 描述                                       |
| :--------- | :-------------- | :------------------ | :--------- | :--------------------------------------- |
| bucketName | String          | 无                   | 构造函数或set方法 | bucket名称                                 |
| cosPath    | String          | 无                   | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |
| localPath  | String          | 无                   | 构造函数或set方法 | 要上传的本地文件的绝对路径                            |
| bizAttr    | String          | 空                   | 构造函数或set方法 | 文件的备注，主要用于对该文件用途的描述                      |
| insertOnly | InsertOnly (枚举) | NO_OVER_WRITE (不覆盖) | set方法      | 是否直插入不覆盖已存在的文件, NO_OVER_WRITE表示只直插入不覆盖, 当文件存在返回错误 OVER_WRITE 表示允许覆盖 |

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess, 'data':\$data}, code为0表示成功,  message为SUCCESS或者失败原因, data中包含相关的属性, 详情请参见返回值模块 |

#### 示例

```java
UploadFileRequest uploadFileRequest = new UploadFileRequest(bucketName, 		"/sample_file.txt", "local_file_1.txt");
String uploadFileRet = cosClient.uploadFile(uploadFileRequest);
```

### 获取文件属性

#### 方法原型

```java
String statFile(StatFileRequest request);
```

#### 参数说明

| 参数名     | 参数类型            | 默认值  | 参数描述     |
| :------ | :-------------- | :--- | :------- |
| request | StatFileRequest | 无    | 获取文件属性请求 |

| request成员  | 类型     | 默认值  | 设置方法       | 描述                                       |
| :--------- | :----- | :--- | :--------- | :--------------------------------------- |
| bucketName | String | 无    | 构造函数或set方法 | bucket名称                                 |
| cosPath    | String | 无    | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess, 'data':\$data}, code为0表示成功,  message为SUCCESS或者失败原因, data中包含相关的属性, 详情请参见返回值模块 |

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

| 参数名     | 参数类型              | 默认值  | 参数描述     |
| :------ | :---------------- | :--- | :------- |
| request | UpdateFileRequest | 无    | 更新文件属性请求 |

| request成员          | 类型          | 默认值  | 设置方法       | 描述                                       |
| :----------------- | :---------- | :--- | :--------- | :--------------------------------------- |
| bucketName         | String      | 无    | 构造函数或set方法 | bucket名称                                 |
| cosPath            | String      | 无    | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |
| bizAttr            | String      | 无    | set方法      | 文件的备注，主要用于对改文件用途的描述                      |
| authority          | String (枚举) | 无    | set方法      | 文件权限，默认是继承bucket的权限合法取值: eInvalid(继承bucket), eWRPrivate(私有读写), eWPrivateRPublic(私有写, 公有读) |
| cacheControl       | String      | 无    | set方法      | 参见HTTP的Cache-Control                     |
| contentType        | String      | 无    | set方法      | 参见HTTP的Content-Type                      |
| contentLanguage    | String      | 无    | set方法      | 参见HTTP的Content-Language                  |
| contentDisposition | String      | 无    | set方法      | 参见HTTP的Content-Disposition               |
| x-cos-meta-        | String      | 无    | set方法      | 自定义HTTP 头，参数必须以x-cos-meta-开头，值由用户定义，可设置多个 |

**tips:** 更新属性可以选择其中的某几个，对于HTTP头部cache_control，content_type, content_disposition和x-cos-meta-, 如果本次只更新其中的某几个，其他的都会被抹掉，即这4个属性是整体更新。

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

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

### 移动文件(重命名文件)

#### 方法原型

```java
String moveFile(MoveFileRequest request);
```

#### 参数说明

| 参数名     | 参数类型            | 默认值  | 参数描述   |
| :------ | :-------------- | :--- | :----- |
| request | MoveFileRequest | 无    | 移动文件请求 |

| request成员  | 类型        | 默认值                     | 设置方法       | 描述                                       |
| :--------- | :-------- | :---------------------- | :--------- | :--------------------------------------- |
| bucketName | String    | 无                       | 构造函数或set方法 | bucket名称                                 |
| cosPath    | String    | 无                       | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |
| overWrite  | OverWrite | OverWrite.NO_OVER_WRITE | 构造函数或set方法 | 是否覆盖, 0(默认): 不覆盖, 1: 覆盖                  |

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

#### 示例

```java
MoveFileRequest moveFileRequest = new MoveFileRequest(bucketName, "/sample_file.txt", "/sample_file_move.txt");
String moveFileRet = cosClient.moveFile(moveFileRequest);
```

### 删除文件

#### 方法原型

```java
String delFile(DelFileRequest request);
```

#### 参数说明

| 参数名     | 参数类型           | 默认值  | 参数描述   |
| :------ | :------------- | :--- | :----- |
| request | DelFileRequest | 无    | 删除文件请求 |

| request成员  | 类型     | 默认值  | 设置方法       | 描述                                       |
| :--------- | :----- | :--- | :--------- | :--------------------------------------- |
| bucketName | String | 无    | 构造函数或set方法 | bucket名称                                 |
| cosPath    | String | 无    | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，文件路径不能以/结尾, 例如 /mytest/demo.txt |

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

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

| 参数名     | 参数类型                | 默认值  | 参数描述   |
| :------ | :------------------ | :--- | :----- |
| request | CreateFolderRequest | 无    | 创建目录请求 |

| request成员  | 类型     | 默认值  | 设置方法       | 描述                                       |
| :--------- | :----- | :--- | :--------- | :--------------------------------------- |
| bucketName | String | 无    | 构造函数或set方法 | bucket名称                                 |
| cosPath    | String | 无    | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |
| bizAttr    | String | 空    | set方法      | 目录的备注，主要用于对目录用途的描述                       |

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

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

| 参数名     | 参数类型              | 默认值  | 参数描述     |
| :------ | :---------------- | :--- | :------- |
| request | StatFolderRequest | 无    | 获取目录属性请求 |

| request成员  | 类型     | 默认值  | 设置方法       | 描述                                       |
| :--------- | :----- | :--- | :--------- | :--------------------------------------- |
| bucketName | String | 无    | 构造函数或set方法 | bucket名称                                 |
| cosPath    | String | 无    | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess, 'data':\$data}, code为0表示成功,  message为SUCCESS或者失败原因, data中包含相关的属性, 详情请参见返回值模块 |

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

| 参数名     | 参数类型                | 默认值  | 参数描述     |
| :------ | :------------------ | :--- | :------- |
| request | UpdateFolderRequest | 无    | 更新目录属性请求 |

| request成员  | 类型     | 默认值  | 设置方法       | 描述                                       |
| :--------- | :----- | :--- | :--------- | :--------------------------------------- |
| bucketName | String | 无    | 构造函数或set方法 | bucket名称                                 |
| cosPath    | String | 无    | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |
| bizAttr    | String | 空    | set方法      | 目录的备注，主要用于对目录用途的描述                       |

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

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

| 参数名     | 参数类型              | 默认值  | 参数描述     |
| :------ | :---------------- | :--- | :------- |
| request | ListFolderRequest | 无    | 获取目录成员请求 |

| request成员  | 类型               | 默认值           | 设置方法       | 描述                                       |
| :--------- | :--------------- | :------------ | :--------- | :--------------------------------------- |
| bucketName | String           | 无             | 构造函数或set方法 | bucket名称                                 |
| cosPath    | String           | 无             | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |
| num        | int              | 199           | 构造函数或set方法 | 获取列表成员的数量，最大为199                         |
| pattern    | ListPattern (枚举) | BOTH          | 构造函数或set方法 | 获取列表成员类型, 合法取值       BOTH(获取文件和目录),       DIR_ONLY(只获取目录),     FILE_ONLY(只获取文件) |
| prefix     | String           | 空             | 构造函数或set方法 | 搜索成员的前缀, 例如prefix为test表示只搜索以test开头的文件或目录 |
| context    | String           | 空             | 构造函数或set方法 | 搜索上下文, 由上一次list的结果返回，作为这一次搜索的起点，用于循环获取一个目录下的所有成员 |
| order      | ListOrder (枚举)   | POSITIVE (正序) | 构造函数或set方法 | 搜索顺序, POSITIVE: 正序, NEGATIVE: 逆序         |

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess, 'data':\$data}, code为0表示成功,  message为SUCCESS或者失败原因, data中包含成员列表, 详情请参见返回值模块 |

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

| 参数名     | 参数类型             | 默认值  | 参数描述   |
| :------ | :--------------- | :--- | :----- |
| request | DelFolderRequest | 无    | 删除目录请求 |

| request成员  | 类型     | 默认值  | 设置方法       | 描述                                       |
| :--------- | :----- | :--- | :--------- | :--------------------------------------- |
| bucketName | String | 无    | 构造函数或set方法 | bucket名称                                 |
| cosPath    | String | 无    | 构造函数或set方法 | cos路径, 必须从bucket下的根/开始，目录路径必须以/结尾, 例如 /mytest/dir/ |

#### 返回结果说明

| 返回值类型  | 返回值描述                                    |
| :----- | :--------------------------------------- |
| String | {'code':\$code,  'message':$mess}, code为0表示成功,  message为SUCCESS或者失败原因, 详情请参见返回值模块 |

#### 示例

```java
DelFolderRequest delFolderRequest = new DelFolderRequest(bucketName, "/sample_folder/");
String delFolderRet = cosClient.delFolder(delFolderRequest);
```

## 签名管理

签名模块提供了生成多次签名、单次签名和下载签名的接口，其中多次签名和单次签名在文件和目录操作的api内部使用，用户不用关心，下载签名用于方便用户生成下载私有bucket的文件签名。

### 多次签名

#### 方法原型

```java
String getPeriodEffectiveSign(String bucketName, String cosPath, Credentials cred, long expired)
```

#### 使用场景

上传文件, 重命名文件, 创建目录, 获取文件目录属性, 拉取目录列表

#### 参数说明

| 参数名      | 参数类型        | 默认值  | 参数描述                                 |
| :------- | :---------- | :--- | :----------------------------------- |
| bucket   | String      | 无    | bucket名称                             |
| cos_path | String      | 无    | 要签名的cos路径                            |
| cred     | Credentials | 无    | 用户身份信息, 包括appid, secretId, secretkey |
| expired  | long        | 无    | 签名过期时间, UNIX时间戳                      |

#### 返回结果说明

base64编码的字符串

#### 示例

```java
Credentials cred = new Credentials(appId, secretId, secretKey);
long expired = System.currentTimeMillis() / 1000 + 600;
String signStr = Sign.getPeriodEffectiveSign(bucketName, "/pic/test.jpg", cred, expired);
```

### 单次签名

#### 方法原型

```java
String getOneEffectiveSign(String bucketName, String cosPath, Credentials cred)
```

#### 使用场景

删除和更新文件目录

#### 参数说明

| 参数名      | 参数类型        | 默认值  | 参数描述                                 |
| :------- | :---------- | :--- | :----------------------------------- |
| bucket   | unicode     | 无    | bucket名称                             |
| cos_path | unicode     | 无    | 要签名的cos路径                            |
| cred     | Credentials | 无    | 用户身份信息, 包括appid, secretId, secretkey |

#### 返回结果说明

base64编码的字符串

#### 示例

```java
Credentials cred = new Credentials(appId, secretId, secretKey);
String signStr = Sign.getOneEffectiveSign(bucketName, "/pic/test.jpg", cred);
```

### 下载签名

#### 方法原型

```java
String getDownLoadSign(String bucketName, String cosPath, Credentials cred, long expired)
```

#### 使用场景

生成文件的下载签名, 用于下载私有bucket的文件

#### 参数说明

| 参数名      | 参数类型        | 默认值  | 参数描述                                 |
| :------- | :---------- | :--- | :----------------------------------- |
| bucket   | unicode     | 无    | bucket名称                             |
| cos_path | unicode     | 无    | 要签名的cos路径                            |
| cred     | Credentials | 无    | 用户身份信息, 包括appid, secretId, secretkey |
| expired  | long        | 无    | 签名过期时间, UNIX时间戳                      |

#### 返回结果说明

base64编码的字符串

#### 示例

```java
Credentials cred = new Credentials(appId, secretId, secretKey);
long expired = System.currentTimeMillis() / 1000 + 600;
String signStr = Sign.getDownLoadSign(bucketName, "/pic/test.jpg", cred, expired);
```

## 操作返回值说明

| code | 含义                                   |
| :--- | :----------------------------------- |
| 0    | 操作成功                                 |
| -1   | 输入参数错误, 例如输入的本地文件路径不存在, cos文件路径不符合规范 |
| -2   | 网络错误, 如404等                          |
| -3   | 连接cos时发生异常，如连接超时                     |
| -71  | 操作频率过快，触发cos的频控                      |

