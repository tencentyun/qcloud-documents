>!您目前查阅的是历史版本 SDK 文档，已不再更新和维护，我们建议您查阅新版 [SDK 文档](https://cloud.tencent.com/document/product/436/6474)。

## 开发准备

### 相关资源

[C# SDK github项目下载地址](https://github.com/tencentyun/cos-donet-sdk-v4)

### 开发准备

1. SDK 依赖 C# 4.0版本及以上， 推荐使用相同的版本。
2. 从控制台获取 APP ID、SecretID、SecretKey。
3. 修改园区，CosCloud.cs文件内的URL定义，例如华东：`http://sh.file.myqcloud.com/files/v2/` 华北：`http://tj.file.myqcloud.com/files/v2/` 华南：`http://gz.file.myqcloud.com/files/v2/`
（本版本SDK基于JSON API封装组成）

### SDK 配置

直接下载 github 上提供的源代码，集成到开发环境。 

若需 HTTPS 支持，则将 cos_dotnet_sdk/Api/CosCloud.cs 文件中变量 COSAPI_CGI_URL 中的 HTTP 修改为 HTTPS 即可。

## 生成签名

### 多次有效签名

#### 方法原型

``` c#
public static string Signature(int appId, string secretId, string secretKey, long expired, string bucketName)
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| appId      | int    | 是      | AppId                                    |
| secretId   | string | 是      | Secret Id                                |
| secretKey  | string | 是      | Secret Key，以上三项从 [控制台](/document/product/436/6238) 获取。 |
| expired    | long   | 是      | 过期时间，Unix 时间戳                             |
| bucketName | string | 是      | bucket 名称，bucket 创建参见 [创建Bucket](/document/product/436/6245) |

#### 示例

``` c#
var sign = Sign.Signature(appId, secretId, secretKey, expired, bucketName); 
```

### 单次有效签名

#### 方法原型

``` c#
public static string SignatureOnce(int appId, string secretId, string secretKey, string remotePath, string bucketName)
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**                                 |
| ---------- | ------ | ------ | ---------------------------------------- |
| appId      | int    | 是      | AppId                                    |
| secretId   | string | 是      | Secret Id                                |
| secretKey  | string | 是      | Secret Key，以上三项从 [控制台](/document/product/436/6238) 获取。 |
| bucketName | string | 是      | bucket名称，bucket创建参见 [创建Bucket](/document/product/436/6245) |
| remotePath | string | 是      | 文件唯一的标识，格式 /appid/bucketname/filepath/filename，其中 /filepath/filename为文件在此 bucketname 下的全路径， |

#### 示例

``` c#
var sign = Sign.SignatureOnce(appId, secretId, secretKey,remotePath, bucketName); 
```

更多签名详细说明，请参考 [权限控制](/document/product/436/6247) 。

## 目录操作

### 创建目录

接口说明：用于目录的创建，可以通过此接口在指定 bucket 下创建目录。

#### 方法原型

``` c#
public string CreateFolder(string bucketName, string remotePath, Dictionary<string, string> parameterDic = null)
```

#### 参数说明

| **参数名**      | **类型** | **必填** | **参数描述**   |
| ------------ | ------ | ------ | ---------- |
| bucketName   | string | 是      | bucket 名称   |
| remotePath   | string | 是      | 需要创建目录的全路径 |
| parameterDic | string | 否      | 属性字典       |

属性字典说明

| 参数名      | 类型     | 必填   | 参数描述 |
| -------- | ------ | ---- | ---- |
| biz_attr | string | 否    | 目录属性 |

#### 返回结果说明

| **参数名** | **类型** | 必带   | **参数描述**                   |
| ------- | ------ | ---- | -------------------------- |
| code    | Int    | 是    | 错误码，成功时为 0                  |
| message | String | 是    | 错误信息                       |
| data    | Array  | 否    | 返回数据，请参考《Restful API 创建目录》 |

#### 示例

``` c#
var createFolderParasDic = new Dictionary<string, string>();                
    createFolderParasDic.Add(CosParameters.PARA_BIZ_ATTR,"new attribute");
var result = cos.CreateFolder(bucketName, folder, createFolderParasDic);
```

### 目录更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

``` c#
public string UpdateFolder(string bucketName, string remotePath, Dictionary<string, string>  parameterDic = null) 
```

#### 参数说明

| **参数名**      | **类型** | **必填** | **参数描述**   |
| ------------ | ------ | ------ | ---------- |
| bucketName   | string | 是      | bucket 名称   |
| remotePath   | string | 是      | 需要创建目录的全路径 |
| parameterDic | string | 是      | 目录更新参数字典   |

目录更新参数字典

| 参数名      | 类型     | 必填   | 参数描述 |
| -------- | ------ | ---- | ---- |
| biz_attr | string | 否    | 目录属性 |

#### 返回结果说明

| **参数名** | **类型** | 必选   | **参数描述**  |
| ------- | ------ | ---- | --------- |
| code    | Int    | 是    | 错误码，成功时为0 |
| message | String | 是    | 错误信息      |

#### 示例

``` c#
var updateParasDic = new Dictionary<string, string>();                
    updateParasDic.Add(CosParameters.PARA_BIZ_ATTR,"new attribute");
var result = cos.UpdateFolder(bucketName, folder, updateParasDic);
```

### 目录查询

接口说明：用于目录属性的查询，可以通过此接口查询目录的属性。

#### 方法原型

``` c#
public string GetFolderStat(string bucketName, string remotePath)  
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述** |
| ---------- | ------ | ------ | -------- |
| bucketName | string | 是      | bucket 名称 |
| remotePath | string | 是      | 目录的全路径   |

#### 返回结果说明

| **参数名** | **类型** | 必选   | **参数描述**                     |
| ------- | ------ | ---- | ---------------------------- |
| code    | Int    | 是    | 错误码，成功时为 0                    |
| message | String | 是    | 错误信息                         |
| data    | Array  | 否    | 目录属性数据，请参考《Restful API 目录查询》 |

#### 示例

``` c#
var result = cos.GetFolderStat(bucketName, folder);
```

### 目录删除

接口说明：用于目录的删除，可以通过此接口删除空目录，如果目录中存在有效文件或目录，将不能删除。

#### 方法原型

``` c#
public string DeleteFolder(string bucketName, string remotePath)
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述** |
| ---------- | ------ | ------ | -------- |
| bucketName | string | 是      | bucket 名称 |
| remotePath | string | 是      | 目录的全路径   |

#### 返回结果说明

| **参数名** | **类型** | 必选   | **参数描述**  |
| ------- | ------ | ---- | --------- |
| code    | Int    | 是    | 错误码，成功时为0 |
| message | String | 是    | 错误信息      |

#### 示例

``` c#
var result = cos.DeleteFolder(bucketName, folder);
```

### 列举目录下文件&目录

接口说明：用于列举目录下文件和目录，可以通过此接口查询目录下的文件和目录属性。

#### 方法原型

``` c#
public string GetFolderList(string bucketName, string remotePath, Dictionary<string, string>  parameterDic = null)
```

#### 参数说明

| **参数名**      | **类型**                     | **必填** | **参数描述** |
| ------------ | -------------------------- | ------ | -------- |
| bucketName   | string                     | 是      | bucket 名称 |
| remotePath   | string                     | 是      | 目录的全路径   |
| parameterDic | Dictionary<string, string> | 是      | 目录列表参数字典 |

目录列表参数字典

| 参数名      | **类型** | **必填** | 参数描述                         |
| -------- | ------ | ------ | ---------------------------- |
| num      | string | 是      | 要查询的目录/文件数量，最大1000           |
| listFlag | string | 否      | listFlag：大于0返回全部数据，否则返回部分数据  |
| context  | String | 否      | 透传字段，用于翻页，前端不需理解，需要往后翻页则透传回来 |
| prefix   | string | 否      | 搜索前缀                         |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**                   |
| ------- | ------ | ------ | -------------------------- |
| code    | Int    | 是      | API 错误码，成功时为0              |
| message | String | 是      | 错误信息                       |
| data    | Array  | 是      | 返回数据，请参考《Restful API 目录列表》 |

#### 示例

``` c#
var folderlistParasDic = new Dictionary<string, string>();                
	folderlistParasDic.Add(CosParameters.PARA_NUM,"100");
var result = cos.GetFolderList(bucketName, folder, folderlistParasDic);
```

## 文件操作

### 文件上传

接口说明：文件上传的统一接口，对于大于8m的文件，内部会通过多次分片的方式进行文件上传。没有断点续传功能，需要自己用分片上传接口实现。

#### 方法原型

``` c#
public string UploadFile(string bucketName, string remotePath, string localPath, 	Dictionary<string, string>  parameterDic = null)
```

#### 参数说明

| **参数名**      | **类型**                     | **必填** | **参数描述**                                 |
| ------------ | -------------------------- | ------ | ---------------------------------------- |
| bucketName   | string                     | 是      | bucket名称，bucket创建参见[创建Bucket](/document/product/430/5887) |
| remotePath   | string                     | 是      | 文件在服务端的全路径                               |
| localPath    | string                     | 是      | 文件本地路径                                   |
| parameterDic | Dictionary<string, string> | 否      | 文件上传参数字典                                 |

文件上传参数字典

| 参数名        | 类型     | 必填   | 参数描述                                     |
| ---------- | ------ | ---- | ---------------------------------------- |
| biz_attr   | string | 否    | 文件属性                                     |
| slice_size | string | 否    | 可选取值为：64*1024 512*1024，1*1024*1024（默认），2*1024*1024，3*1024*1024 |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**                   |
| ------- | ------ | ------ | -------------------------- |
| code    | Int    | 是      | 错误码，成功时为0                  |
| message | String | 是      | 错误信息                       |
| data    | Array  | 是      | 返回数据，请参考《Restful API 创建文件》 |

#### 示例

``` c#
var uploadParasDic = new Dictionary<string, string>();                
uploadParasDic.Add(CosParameters.PARA_BIZ_ATTR,"file attribute");
uploadParasDic.Add(CosParameters.PARA_INSERT_ONLY,"0");
uploadParasDic.Add(CosParameters.PARA_SLICE_SIZE,SLICE_SIZE.SLIZE_SIZE_3M.ToString());
result = cos.UploadFile(bucketName, remotePath, localPath, uploadParasDic);
```

### 文件属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

``` c#
public string UpdateFile(string bucketName, string remotePath, Dictionary<string, string> parameterDic = null)
```

#### 参数说明

| **参数名**      | **类型** | **必填** | **参数描述**   |
| ------------ | ------ | ------ | ---------- |
| bucketName   | string | 是      | bucket 名称   |
| remotePath   | string | 是      | 文件在 COS 的全路径 |
| parameterDic | string | 否      | 文件更新参数字典   |

文件更新参数字典

| 参数名                 | 类型     | 必填   | 参数描述                                     |
| ------------------- | ------ | ---- | ---------------------------------------- |
| biz_attr            | string | 否    | 待更新的文件属性信息                               |
| authority           | string | 否    | eInvalid（继承Bucket的读写权限）；eWRPrivate（私有读写）；eWPrivateRPublic（公有读私有写） |
| Cache-Control       | string | 否    | 指定请求和响应遵循的缓存机制，如：no-cache；max-age=200    |
| Content-Type        | string | 否    | 返回内容的 MIME 类型，如：text/html                  |
| Content-Disposition | string | 否    | 控制用户请求所得的内容存为一个文件的时候提供一个默认的文件名，如：attachment; filename="fname.ext" |
| Content-Language    | string | 否    | 使用的语言，如：zh-CN                            |
| x-cos-meta-自定义内容    | string | 否    | 表示以“x-cos-meta-”名字开头的参数，用户按照自身业务场景，设置需要在 Header 中传输什么参数 |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | 是      | 错误码，成功时为0 |
| message | String | 是      | 错误信息      |

#### 示例

``` c#
var optionParasDic = new Dictionary<string, string>();
	optionParasDic.Add(CosParameters.PARA_BIZ_ATTR,"new attribute");
    optionParasDic.Add(CosParameters.PARA_AUTHORITY,AUTHORITY.AUTHORITY_PRIVATEPUBLIC);
	optionParasDic.Add(CosParameters.PARA_CACHE_CONTROL,"no");
	optionParasDic.Add(CosParameters.PARA_CONTENT_TYPE,"application/text");
	optionParasDic.Add(CosParameters.PARA_CONTENT_DISPOSITION,"filename=\"test.pdf\"");
	optionParasDic.Add(CosParameters.PARA_CONTENT_LANGUAGE,"en");
	optionParasDic.Add("x-cos-meta-test","test");
result = cos.UpdateFile(bucketName, remotePath, optionParasDic);
```

### 文件查询

接口说明：用于文件的查询，可以通过此接口查询文件的各项属性信息。

#### 方法原型

``` c#
public string GetFileStat(string bucketName, string remotePath)
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**   |
| ---------- | ------ | ------ | ---------- |
| bucketName | string | 是      | bucket名称   |
| remotePath | string | 是      | 文件在Cos的全路径 |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**                     |
| ------- | ------ | ------ | ---------------------------- |
| code    | Int    | 是      | 错误码，成功时为0                    |
| message | String | 是      | 错误信息                         |
| data    | Array  | 是      | 文件属性数据，请参考《Restful API 文件查询》 |

#### 示例

``` c#
var result = cos.GetFileStat(bucketName, remotePath);
```

### 文件删除

接口说明：用于文件的删除，可以通过此接口删除已经上传的文件。

#### 方法原型

``` c#
public string DeleteFile(string bucketName, string remotePath) 
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**   |
| ---------- | ------ | ------ | ---------- |
| bucketName | string | 是      | bucket名称   |
| remotePath | string | 是      | 文件在服务端的全路径 |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | 是      | 错误码，成功时为0 |
| message | String | 是      | 错误信息      |

#### 示例

``` c#
var result = cos.DeleteFile(bucketName, remotePath);
```

### 分片上传list

接口说明：查询分片上传的情况

#### 方法原型

``` c#
public string UploadSliceList(string bucketName, string remotePath)
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**   |
| ---------- | ------ | ------ | ---------- |
| bucketName | string | 是      | bucket名称   |
| remotePath | string | 是      | 文件在服务端的全路径 |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | 是      | 错误码，成功时为0 |
| message | String | 是      | 错误信息      |
| data    | Array  | 是      | 分片上传信息    |

上传完成data的数据说明

| **参数名**       | **类型** | **必带** | **参数描述**                   |
| ------------- | ------ | ------ | -------------------------- |
| url           | String | 是      | 操作文件的 url                   |
| access_url    | String | 是      | 生成的文件下载 url                 |
| source_url    | String | 是      | 源地址                        |
| resource_path | String | 是      | 资源路径，格式： /appid/bucket/xxx |
| preview_url   | String | 否      | 预览地址                       |

上传未完成data的数据说明

| **参数名**    | **类型**     | **必带** | **参数描述**                                 |
| ---------- | ---------- | ------ | ---------------------------------------- |
| session    | String     | 是      | init返回的标识                                |
| filesize   | Int        | 是      | 文件大小                                     |
| slice_size | Int        | 是      | 分片大小（64K-3M） 大于1M 必须为1M 整数倍              |
| sha        | String     | 否      | 文件的全文sha值，init时若已带sha值，则返回该值                 |
| listparts  | Json Array | 是      | 已上传完成的分片，形如：[{“offset”:0, “datalen”:1024}, {}, {}]. |

#### 示例

``` c#
var fileSha = SHA1.GetFileSHA1(localPath);
var result = SliceUploadInit(bucketName, remotePath, localPath, fileSha, bizAttribute, sliceSize, insertOnly);
```

### 分片上传init

接口说明：分片上传的第一次握手,如果上一次分片上传未完成，会返回{"code":-4019,"message":"_ERROR_FILE_NOT_FINISH_UPLOAD"}init

接口说明：分片上传的第一次握手

#### 方法原型

``` c#
public string SliceUploadInit(string bucketName, string remotePath, string localPath, string fileSha,string bizAttribute = "", int sliceSize = SLICE_SIZE.SLIZE_SIZE_1M, int insertOnly = 1)
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**   |
| ---------- | ------ | ------ | ---------- |
| bucketName | string | 是      | bucket 名称   |
| remotePath | string | 是      | 文件在服务端的全路径 |
| localPath  | string | 是      | 本地文件路径     |
| fileSha    | string | 是      | 文件的 SHA 值    |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | 是      | 错误码，成功时为0 |
| message | String | 是      | 错误信息      |
| data    | Array  | 是      | 分片上传信息    |

data的数据说明

| **参数名**       | **类型** | **必带** | **参数描述**                           |
| ------------- | ------ | ------ | ---------------------------------- |
| session       | string | 否      | (非秒传的大部分情况会有)	唯一标识此文件传输过程的 ID       |
| slice_size    | Int    | 否      | (非秒传大部分情况下会有)	分片大小                 |
| serial_upload | int    | 否      | (非秒传大部分情况下会有) 1：只支持串行分片上传其它：支持并行分片 |

#### 示例

``` c#
var fileSha = SHA1.GetFileSHA1(localPath);
var result = SliceUploadInit(bucketName, remotePath, localPath, fileSha, bizAttribute, sliceSize, insertOnly);
```



### 分片上传

接口说明：分片上传数据

#### 方法原型

``` c#
public string SliceUploadData(string bucketName, string remotePath, string localPath, string fileSha, string session, long offset,int sliceSise,string sign)
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**       |
| ---------- | ------ | ------ | -------------- |
| bucketName | string | 是      | bucket名称       |
| remotePath | string | 是      | 文件在服务端的全路径     |
| localPath  | string | 是      | 本地文件路径         |
| fileSha    | string | 是      | 文件的Sha值        |
| session    | string | 是      | 唯一标识此文件传输过程的id |
| offset     | int    | 是      | 分片的偏移量         |
| sliceSize  | int    | 是      | 分片的大小          |
| sign       | string | 是      | 签名（多次）         |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | 是      | 错误码，成功时为0 |
| message | String | 是      | 错误信息      |
| data    | Array  | 是      | 分片上传信息    |

data的数据说明

| **参数名**       | **类型** | **必带** | **参数描述**                           |
| ------------- | ------ | ------ | ---------------------------------- |
| session       | string | 是     | (非秒传的大部分情况会有)	唯一标识此文件传输过程的 ID       |
| offset        | Int    | 是      | 当前分片的 offset                        |
| datalen       | int    | 是      |  分片长度 slice_size，返回的 datalen 就是当前分片的大小                |
| serial_upload | int    | 否      | (非秒传大部分情况下会有) 1：只支持串行分片上传其它：支持并行分片 |

#### 示例

``` c#
var fileSha = SHA1.GetFileSHA1(localPath);
var result = SliceUploadDataInit(bucketName, remotePath, localPath, fileSha, session, offset, sliceSize,sign);
```



### 分片上传 finish

接口说明：告诉COS所有分片上传成功。

#### 方法原型

``` c#
public string SliceUploadFinish(string bucketName, string remotePath, string localPath, string fileSha, string session)
```

#### 参数说明

| **参数名**    | **类型** | **必填** | **参数描述**       |
| ---------- | ------ | ------ | -------------- |
| bucketName | string | 是      | bucket名称       |
| remotePath | string | 是      | 文件在服务端的全路径     |
| localPath  | string | 是      | 本地文件路径         |
| fileSha    | string | 是      | 文件的Sha值        |
| session    | string | 是      | 唯一标识此文件传输过程的id |

#### 返回结果说明

| **参数名** | **类型** | **必带** | **参数描述**  |
| ------- | ------ | ------ | --------- |
| code    | Int    | 是      | 错误码，成功时为0 |
| message | String | 是      | 错误信息      |
| data    | Array  | 是      | 分片上传信息    |

data的数据说明

| **参数名** | **类型** | **必带** | **参数描述**                     |
| ------- | ------ | ------ | ---------------------------- |
| session | string | 是      | (非秒传的大部分情况会有)	唯一标识此文件传输过程的id |
| offset  | Int    | 是      | 当前分片的offset                  |
| datalen | int    | 是      | 分片文件长度                       |

#### 示例

``` c#
result = SliceUploadFinish(bucketName,remotePath,localPath,fileSha, sessionbizAttribute, sliceSize, insertOnly);
```
