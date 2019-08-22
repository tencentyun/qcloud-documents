## 简介

本文档提供关于对象的简单操作、分块操作等其他操作相关的 API 概览以及 SDK 示例代码。

**简单操作**

| API                                                          | 操作名         | 操作描述                       |
| ------------------------------------------------------------ | -------------- | ------------------------------ |
| [GET Bucket（List Object）](https://cloud.tencent.com/document/product/436/7734) | 查询对象列表   | 查询存储桶下的部分或者全部对象 |
| [PUT Object](https://cloud.tencent.com/document/product/436/7749) | 简单上传对象   | 上传一个对象至存储桶           |
| [HEAD Object](https://cloud.tencent.com/document/product/436/7745) | 查询对象元数据 | 查询对象元数据信息             |
| [GET Object](https://cloud.tencent.com/document/product/436/7753) | 下载对象       | 下载一个对象至本地             |
| [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) | 设置对象复制   | 复制文件到目标路径             |
| [DELETE Object](https://cloud.tencent.com/document/product/436/7743) | 删除单个对象   | 在存储桶中删除指定对象         |
| [DELETE Multiple Objects](https://cloud.tencent.com/document/product/436/8289) | 删除多个对象   | 在存储桶中批量删除对象         |

**分块操作**

| API                                                          | 操作名         | 操作描述                             |
| ------------------------------------------------------------ | -------------- | ------------------------------------ |
| [List Multipart Uploads](https://cloud.tencent.com/document/product/436/7736) | 查询分块上传   | 查询正在进行中的分块上传信息         |
| [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746) | 初始化分块上传 | 初始化分块上传任务                   |
| [Upload Part](https://cloud.tencent.com/document/product/436/7750) | 上传分块       | 分块上传文件                         |
| [Upload Part - Copy](https://cloud.tencent.com/document/product/436/8287) | 复制分块       | 将其他对象复制为一个分块             |
| [List Parts](https://cloud.tencent.com/document/product/436/7747) | 查询已上传块   | 查询特定分块上传操作中的已上传的块   |
| [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742) | 完成分块上传   | 完成整个文件的分块上传               |
| [Abort Multipart Upload](https://cloud.tencent.com/document/product/436/7740) | 终止分块上传   | 终止一个分块上传操作并删除已上传的块 |

**其他操作**

| API                                                          | 操作名       | 操作描述                           |
| ------------------------------------------------------------ | ------------ | ---------------------------------- |
| [POST Object restore](https://cloud.tencent.com/document/product/436/12633) | 恢复归档对象 | 将归档类型的对象取回访问           |
| [PUT Object acl](https://cloud.tencent.com/document/product/436/7748) | 设置对象 ACL | 设置存储桶中某个对象的访问控制列表 |
| [GET Object acl](https://cloud.tencent.com/document/product/436/7744) | 查询对象 ACL | 查询对象的访问控制列表             |

## 简单操作

### 查询对象列表

#### 功能说明

查询存储桶下的部分或者全部对象 。

#### 方法原型

```cpp
CosResult GetBucket(const GetBucketReq& req, GetBucketResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

// GetBucketReq 的构造函数需要传入 bucket_name
qcloud_cos::GetBucketReq req(bucket_name);
qcloud_cos::GetBucketResp resp;
qcloud_cos::CosResult result = cos.GetBucket(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    std::cout << "Name=" << resp.GetName() << std::endl;
    std::cout << "Prefix=" << resp.GetPrefix() << std::endl;
    std::cout << "Marker=" << resp.GetMarker() << std::endl;
    std::cout << "MaxKeys=" << resp.GetMaxKeys() << std::endl;
} else {
    std::cout << "ErrorInfo=" << result.GetErrorInfo() << std::endl;
    std::cout << "HttpStatus=" << result.GetHttpStatus() << std::endl;
    std::cout << "ErrorCode=" << result.GetErrorCode() << std::endl;
    std::cout << "ErrorMsg=" << result.GetErrorMsg() << std::endl;
    std::cout << "ResourceAddr=" << result.GetResourceAddr() << std::endl;
    std::cout << "XCosRequestId=" << result.GetXCosRequestId() << std::endl;
    std::cout << "XCosTraceId=" << result.GetXCosTraceId() << std::endl;
} 
```

#### 参数说明

| 参数 | 参数描述                            |
| ---- | ----------------------------------- |
| req  | GetBucketReq，GetBucket 操作的请求  |
| resp | GetBucketResp，GetBucket 操作的返回 |

GetBucketResp 提供以下成员函数，用于获取 Get Bucket 返回的 XML 格式中的具体内容。 

```cpp
std::vector<Content> GetContents();
std::string GetName();
std::string GetPrefix();
std::string GetMarker();
uint64_t GetMaxKeys();
bool IsTruncated();
std::vector<std::string> GetCommonPrefixes();
```

其中 Content 的定义如下：

```
struct Content {
    std::string m_key; // Object 的 Key
    std::string m_last_modified; // Object 最后被修改时间
    std::string m_etag; // 文件的 MD-5 算法校验值
    std::string m_size; // 文件大小，单位是 Byte
    std::vector<std::string> m_owner_ids; // Bucket 持有者信息
    std::string m_storage_class; // Object 的存储类别，枚举值：STANDARD，STANDARD_IA
};
```

### 简单上传对象

#### 功能说明

上传对象到指定的存储桶中。

#### 方法原型

```cpp
/// 通过 Stream 进行上传
CosResult PutObject(const PutObjectByStreamReq& req, PutObjectByStreamResp* resp)

/// 上传本地文件
CosResult PutObject(const PutObjectByFileReq& req, PutObjectByFileResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "object_name";

// 简单上传(流)
{
    std::istringstream iss("put object");
    // request 的构造函数中需要传入 istream
    qcloud_cos::PutObjectByStreamReq req(bucket_name, object_name, iss);
    // 调用 Set 方法设置元数据或者 ACL 等
    req.SetXCosStorageClass("STANDARD_IA");
    // 关闭MD5校验，开启使用req.TurnOnComputeConentMd5()，默认情况开启
    req.TurnOffComputeConentMd5();
    qcloud_cos::PutObjectByStreamResp resp;
    qcloud_cos::CosResult result = cos.PutObject(req, &resp);
    
    if (result.IsSucc()) {
        // 调用成功，调用 resp 的成员函数获取返回内容
        do sth
    } else {
        // 调用失败，调用 result 的成员函数获取错误信息
        std::cout << "ErrorInfo=" << result.GetErrorInfo() << std::endl;
        std::cout << "HttpStatus=" << result.GetHttpStatus() << std::endl;
        std::cout << "ErrorCode=" << result.GetErrorCode() << std::endl;
        std::cout << "ErrorMsg=" << result.GetErrorMsg() << std::endl;
        std::cout << "ResourceAddr=" << result.GetResourceAddr() << std::endl;
        std::cout << "XCosRequestId=" << result.GetXCosRequestId() << std::endl;
        std::cout << "XCosTraceId=" << result.GetXCosTraceId() << std::endl;
     }
}

// 简单上传(文件)
{
    // request 的构造函数中需要传入本地文件路径
    qcloud_cos::PutObjectByFileReq req(bucket_name, object_name, "/path/to/local/file");
    // 调用 Set 方法设置元数据或者 ACL 等
    req.SetXCosStorageClass("STANDARD_IA");
    // 关闭 MD5 校验，开启使用 req.TurnOnComputeConentMd5()，默认情况开启
    req.TurnOffComputeConentMd5();
    qcloud_cos::PutObjectByFileResp resp;
    qcloud_cos::CosResult result = cos.PutObject(req, &resp);
        if (result.IsSucc()) {
        // 调用成功，调用 resp 的成员函数获取返回内容
        do sth
    } else {
        // 调用失败，调用 result 的成员函数获取错误信息
        std::cout << "ErrorInfo=" << result.GetErrorInfo() << std::endl;
        std::cout << "HttpStatus=" << result.GetHttpStatus() << std::endl;
        std::cout << "ErrorCode=" << result.GetErrorCode() << std::endl;
        std::cout << "ErrorMsg=" << result.GetErrorMsg() << std::endl;
        std::cout << "ResourceAddr=" << result.GetResourceAddr() << std::endl;
        std::cout << "XCosRequestId=" << result.GetXCosRequestId() << std::endl;
        std::cout << "XCosTraceId=" << result.GetXCosTraceId() << std::endl;
     }
}
```

#### 参数说明

| 参数 | 参数描述                                                     |
| ---- | ------------------------------------------------------------ |
| req  | PutObjectByStreamReq/PutObjectByFileReq，PutObject 操作的请求 |
| resp | PutObjectByStreamResp/PutObjectByFileResp，PutObject 操作的返回 |

参数 Req 包括如下成员函数：

```cpp
// Cache-Control RFC 2616 中定义的缓存策略，将作为 Object 元数据保存
void SetCacheControl(const std::string& str);

// Content-Disposition RFC 2616 中定义的文件名称，将作为 Object 元数据保存
void SetContentDisposition(const std::string& str);

// Content-Encoding    RFC 2616 中定义的编码格式，将作为 Object 元数据保存-
void SetContentEncoding(const std::string& str);

// Content-Type    RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存
void SetContentType(const std::string& str);

// Expect  当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容
void SetExpect(const std::string& str);

// Expires RFC 2616 中定义的过期时间，将作为 Object 元数据保存
void SetExpires(const std::string& str);

// 允许用户自定义的头部信息,将作为 Object 元数据返回.大小限制2K
void SetXCosMeta(const std::string& key, const std::string& value);

// x-cos-storage-class 设置 Object 的存储级别，枚举值：STANDARD,STANDARD_IA，ARCHIVE
// 默认值：STANDARD
void SetXCosStorageClass(const std::string& storage_class);

// 定义 Object 的 ACL 属性,有效值：private,public-read
// 默认值：private
void SetXcosAcl(const std::string& str);

// 赋予被授权者读的权限.格式：x-cos-grant-read: id=" ",id=" ".
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantRead(const std::string& str);

// 赋予被授权者读写权限.格式：x-cos-grant-full-control: id=" ",id=" ".
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantFullControl(const std::string& str);

/// 设置Server端加密使用的算法, 目前支持AES256
void SetXCosServerSideEncryption(const std::string& str);
```

参数 Resp 包括如下成员函数：

```C++
/// 获取Object的版本号, 如果Bucket未开启多版本, 返回空字符串
std::string GetVersionId();

/// Server端加密使用的算法
std::string GetXCosServerSideEncryption();
```

### 查询对象元数据

#### 功能说明

查询对象元数据信息。

#### 方法原型

```cpp
CosResult HeadObject(const HeadObjectReq& req, HeadObjectResp* resp)
```

#### 请求示例

```cpp
key := "test/hello.txt"
resp, err := client.Object.Head(context.Background(), key, nil)
```

#### 参数说明

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "object_name";
qcloud_cos::HeadObjectReq req(bucket_name, object_name);
qcloud_cos::HeadObjectResp resp;
qcloud_cos::CosResult result = cos.HeadObject(req, &resp);
if (result.IsSucc()) {
    // 下载成功，可以调用 HeadObjectResp 的成员函数
} else {
    // 下载失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
}
```

#### 参数说明

| 参数 | 参数描述                              |
| ---- | ------------------------------------- |
| req  | HeadObjectReq，HeadObject 操作的请求  |
| resp | HeadObjectResp，HeadObject 操作的返回 |

HeadObjectResp 除了读取公共头部的成员函数外，还提供以下成员函数：

```cpp
std::string GetXCosObjectType();

std::string GetXCosStorageClass();

// 获取自定义的 meta, 参数可以为 x-cos-meta-* 中的 *
std::string GetXCosMeta(const std::string& key);

// 以 map 形式返回所有自定义的 meta, map 的 key 均不包含"x-cos-meta-"前缀
std::map<std::string, std::string> GetXCosMetas();

// 获取 Server 端加密使用的算法
std::string GetXCosServerSideEncryption(); 
```

### 下载对象

#### 功能说明

下载对象到本地（Get Object）。

#### 方法原型

```cpp
// 将 Object 下载到本地文件中
CosResult GetObject(const GetObjectByFileReq& req, GetObjectByFileResp* resp)

// 将 Object 下载到流中
CosResult GetObject(const GetObjectByStreamReq& req, GetObjectByStreamResp* resp)

// 将 Object 下载到本地文件中（多线程）
CosResult GetObject(const MultiGetObjectReq& req, MultiGetObjectResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "object_name";
std::string local_path = "/tmp/object_name";

// 下载到本地文件
{
    // request 需要提供 appid、bucketname、object,以及本地的路径（包含文件名）
    qcloud_cos::GetObjectByFileReq req(bucket_name, object_name, local_path);
    qcloud_cos::GetObjectByFileResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // 下载成功，可以调用 GetObjectByFileResp 的成员函数
    } else {
        // 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
    }
}

// 下载到流中
{
    // request 需要提供 appid、bucketname、object, 以及输出流
    std::ostringstream os;
    qcloud_cos::GetObjectByStreamReq req(bucket_name, object_name, os);
    qcloud_cos::GetObjectByStreamResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // 下载成功，可以调用 GetObjectByStreamResp 的成员函数
    } else {
        // 下载失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
    }
}

// 多线程下载文件到本地
{
    // request需要提供 appid、bucketname、object以及本地的路径（包含文件名）
    qcloud_cos::MultiGetObjectReq req(bucket_name, object_name, local_path);
    qcloud_cos::MultiGetObjectResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // 下载成功，可以调用 MultiGetObjectResp 的成员函数
    } else {
        // 下载失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
    }
}
```

#### 参数说明

| 参数 | 参数描述                                                     |
| ---- | ------------------------------------------------------------ |
| req  | GetObjectByFileReq/GetObjectByStreamReq/MultiGetObjectReq，GetObject 操作的请求 |
| resp | GetObjectByFileResp/GetObjectByStreamResp/MultiGetObjectResp，GetObject 操作的返回 |

成员函数如下：

```
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

GetObjectResp 除了读取公共头部的成员函数外，还提供以下成员函数：

```cpp
// 获取 Object 最后被修改的时间, 字符串格式 Date, 类似"Wed, 28 Oct 2014 20:30:00 GMT"
std::string GetLastModified();

// 获取 Object type, 表示 Object 是否可以被追加上传，枚举值：normal 或者 appendable
std::string GetXCosObjectType();

// 获取 Object 的存储类别，枚举值：STANDARD，STANDARD_IA
std::string GetXCosStorageClass();

// 以 map 形式返回所有自定义的 meta, map 的 key 均不包含"x-cos-meta-"前缀
std::map<std::string, std::string> GetXCosMetas();

// 获取自定义的 meta, 参数可以为 x-cos-meta-*中的*
std::string GetXCosMeta(const std::string& key);

// 获取Server端加密使用的算法
std::string GetXCosServerSideEncryption(); 
```

### 设置对象复制

复制文件到目标路径。

#### 方法原型

```cpp
CosResult PutObjectCopy(const PutObjectCopyReq& req, PutObjectCopyResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "sevenyou";

qcloud_cos::PutObjectCopyReq req(bucket_name, object_name);                                                                                                                       
req.SetXCosCopySource("sevenyousouthtest-12345656.cn-south.myqcloud.com/sevenyou_source_obj");
qcloud_cos::PutObjectCopyResp resp;
qcloud_cos::CosResult result = cos.PutObjectCopy(req, &resp);
```

#### 参数说明

| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | PutObjectCopyReq，PutObjectCopy 操作的请求  |
| resp | PutObjectCopyResp，PutObjectCopy 操作的返回 |

PutObjectCopyReq 包含以下成员函数：

```
// 源文件 URL 路径，可以通过 versionid 子资源指定历史版本
void SetXCosCopySource(const std::string& str);

// 是否拷贝元数据，枚举值：Copy, Replaced，默认值 Copy。
// 假如标记为 Copy，忽略 Header 中的用户元数据信息直接复制；
// 假如标记为 Replaced，按 Header 信息修改元数据。
// 当目标路径和原路径一致，即用户试图修改元数据时，必须为 Replaced
void SetXCosMetadataDirective(const std::string& str);

// 当 Object 在指定时间后被修改，则执行操作，否则返回 412。
// 可与 x-cos-copy-source-If-None-Match 一起使用，与其他条件联合使用返回冲突。
void SetXCosCopySourceIfModifiedSince(const std::string& str);

// 当 Object 在指定时间后未被修改，则执行操作，否则返回 412。
// 可与 x-cos-copy-source-If-Match 一起使用，与其他条件联合使用返回冲突。
void SetXCosCopySourceIfUnmodifiedSince(const std::string& str);

// 当 Object 的 Etag 和给定一致时，则执行操作，否则返回 412。
// 可与x-cos-copy-source-If-Unmodified-Since 一起使用，与其他条件联合使用返回冲突
void SetXCosCopySourceIfMatch(const std::string& str);

// 当 Object 的 Etag 和给定不一致时，则执行操作，否则返回 412。
// 可与 x-cos-copy-source-If-Modified-Since 一起使用，与其他条件联合使用返回冲突。
void SetXCosCopySourceIfNoneMatch(const std::string& str);

// x-cos-storage-class 设置 Object 的存储级别，枚举值：STANDARD,STANDARD_IA
// 默认值：STANDARD
void SetXCosStorageClass(const std::string& storage_class);

// 定义 Object 的 ACL 属性,有效值：private,public-read
// 默认值：private
void SetXCosAcl(const std::string& str);

// 赋予被授权者读的权限。格式：id="[OwnerUin]"  
void SetXCosGrantRead(const std::string& str);

// 赋予被授权者所有的权限。格式：id="[OwnerUin]"
void SetXCosGrantFullControl(const std::string& str);

// 允许用户自定义的头部信息,将作为 Object 元数据返回.大小限制2K
void SetXCosMeta(const std::string& key, const std::string& value);

/// 设置 Server 端加密使用的算法, 目前支持 AES256
void SetXCosServerSideEncryption(const std::string& str);

```

PutObjectCopyResp 包含以下成员函数：

```
// 返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 的内容是否发生变化。
std::string GetEtag();

// 返回文件最后修改时间，GMT 格式
std::string GetLastModified();

// 返回版本号
std::string GetVersionId();

/// Server端加密使用的算法
std::string GetXCosServerSideEncryption();

```

### 删除单个对象

#### 功能说明

在存储桶中删除指定对象。

#### 方法原型

```cpp
CosResult DeleteObject(const DeleteObjectReq& req, DeleteObjectResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "test_object";

qcloud_cos::DeleteObjectReq req(bucket_name, object_name);
qcloud_cos::DeleteObjectResp resp;
qcloud_cos::CosResult result = cos.DeleteObject(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

#### 参数说明

| 参数 | 参数描述                                 |
| ---- | ---------------------------------------- |
| req  | DeleteObjectReq，DeleteObject 操作的请求 |
| resp | DeletObjectResp，DeletObject 操作的返回  |

### 删除多个对象

#### 功能说明

在存储桶中批量删除对象。

#### 方法原型

```cpp
CosResult DeleteObjects(const DeleteObjectsReq& req, DeleteObjectsResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

std::vector<std::string> objects;
std::vector<ObjectVersionPair> to_be_deleted;
objects.push_back("batch_delete_test_00");
objects.push_back("batch_delete_test_01");
objects.push_back("batch_delete_test_02");
objects.push_back("batch_delete_test_03");
for (size_t idx = 0; idx < objects.size(); ++idx) {
	ObjectVersionPair pair;
    pair.m_object_name = objects[idx];
	to_be_deleted.push_back(pair);
}
qcloud_cos::DeleteObjectsReq req(bucket_name, to_be_deleted);             qcloud_cos::DeleteObjectsResp resp;                                       qcloud_cos::CosResult result = cos.DeleteObjects(req, &resp);
// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 

```

#### 参数说明

| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | DeleteObjectsReq，DeleteObjects 操作的请求  |
| resp | DeleteObjectsResp，DeleteObjects 操作的返回 |

DeleteObjectsReq 包含以下成员函数：

```cpp
// 添加对象，并指定版本
void AddObjectVersion(const std::string& object, const std::string& version)
// 添加对象，非多版本
void AddObject(const std::string& object)
```

DeleteObjectsResp 包含以下成员函数：

```cpp
// 获取删除成功的 objects 信息
std::vector<DeletedInfo> GetDeletedInfos() const

// 获取删除失败的 objects 信息
std::vector<ErrorInfo> GetErrorinfos() const
```

对应DeletedInfo 和 ErrorInfo 的结构如下：

```
struct DeletedInfo{
    std::string m_key; // object key
}
struct ErrorInfo{
    std::string m_key; // object key
    std::string m_code; // error code
    std::string m_message; // error message
}
```

## 分块操作

### 查询分块上传

#### 功能说明

查询指定存储桶中正在进行的分块上传（List Multipart Uploads）。

#### 方法原型

```cpp
CosResult CosAPI::ListMultipartUpload(const ListMultipartUploadReq& request, ListMultipartUploadResp* response)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "test_object";

qcloud_cos::ListMultipartUploadReq req(bucket_name, object_name);
qcloud_cos::ListMultipartUploadResp resp;
qcloud_cos::CosResult result = cos.ListMultipartUpload(req, &resp);

for (std::vector<qcloud_cos::Upload>::const_iterator itr = rst.begin(); itr != rst.end(); ++itr) {
	const qcloud_cos::Upload& upload = *itr;
	std::cout << "key = " << upload.m_key << ", uploadid= " << upload.m_uploadid << ", storagen class = " << upload.m_storage_class << ", m_initiated= " << upload.m_initiated << std::endl;
}   

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

#### 参数说明

| 参数 | 参数描述                                                |
| ---- | ------------------------------------------------------- |
| req  | ListMultipartUploadReq，ListMultipartUpload 操作的请求  |
| resp | ListMultipartUploadResp，ListMultipartUpload 操作的返回 |

ListMultipartUploadReq 成员函数：

```
// 限定返回的 Object key 必须以 Prefix 作为前缀。注意使用 prefix 查询时，返回的 key 中仍会包含 Prefix。
void SetPrefix(const std::string& prefix);

// 定界符为一个符号，对 Object 名字包含指定前缀且第一次出现 delimiter 字符之间的 Object 作为一组元素：common prefix。如果没有 prefix，则从路径起点开始
void SetDelimiter(const std::string& delimiter);

// 规定返回值的编码格式，合法值：url
void SetEncodingType(const std::string& encoding_type);

// 与 upload-id-marker 一起使用当 upload-id-marker 未被指定时，ObjectName 字母顺序大于 key-marker 的条目将被列出，当 upload-id-marker 被指定时，ObjectName 字母顺序大于 key-marker 的条目被列出，ObjectName 字母顺序等于 key-marker 同时 UploadID 大于 upload-id-marker 的条目将被列出。
void SetKeyMarker(const std::string& marker);

// 设置最大返回的 multipart 数量，合法取值从1到1000，默认1000
void SetMaxUploads(const std::string& max_uploads);

// 与 key-marker 一起使用，当 key-marker 未被指定时，upload-id-marker 将被忽略，当 key-marker 被指定时，ObjectName字母顺序大于 key-marker 的条目被列出，ObjectName 字母顺序等于 key-marker 同时 UploadID 大于 upload-id-marker 的条目将被列出。
void SetUploadIdMarker(const std::string& upload_id_marker);
```

ListMultipartUploadResp 成员函数：

```
// 获取Bucket中Object对应的元信息
std::vector<Upload> GetUpload()；
// Bucket 名称
std::string GetName()；
// 编码格式
std::string GetEncodingType() const；
// 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始
std::string GetMarker() const；
// 列出条目从该 UploadId 值开始
std::string GetUploadIdMarker() const；
// 假如返回条目被截断，则返回 NextKeyMarker 就是下一个条目的起点
std::string GetNextKeyMarker() const；
// 假如返回条目被截断，则返回 UploadId 就是下一个条目的起点
std::string GetNextUploadIdMarker() const；
// 最大返回的 multipart 数量，合法取值从0到1000
std::string GetMaxUploads () const；
// 响应请求条目是否被截断，布尔值：true，false
bool IsTruncated()；
// 返回的文件前缀
std::string GetPrefix() const；
// 获取定界符 
std::string GetDelimiter() const；
// 将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix
std::vector<std::string> GetCommonPrefixes() const
```

### 分块上传对象

分块上传对象可包括的操作：

- 分块上传对象： 初始化分块上传，  上传分块， 完成所有分块上传。
- 删除已上传分块。

### 初始化分块上传

#### 功能说明

初始化分块上传，获取对应的 uploadId（Initiate Multipart Upload）。

#### 方法原型

```cpp
CosResult InitMultiUpload(const InitMultiUploadReq& req, InitMultiUploadResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);
std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "object_name";

qcloud_cos::InitMultiUploadReq req(bucket_name, object_name);
qcloud_cos::InitMultiUploadResp resp;
qcloud_cos::CosResult result = cos.InitMultiUpload(req, &resp);

std::string upload_id = "";
if (result.IsSucc()) {
    upload_id = resp.GetUploadId();
}
```

#### 参数说明

| 参数 | 参数描述                                        |
| ---- | ----------------------------------------------- |
| req  | InitMultiUploadReq，InitMultiUpload 操作的请求  |
| resp | InitMultiUploadResp，InitMultiUpload 操作的返回 |

InitMultiUploadReq 的成员函数如下：

```
// Cache-Control RFC 2616 中定义的缓存策略，将作为 Object 元数据保存
void SetCacheControl(const std::string& str);

// Content-Disposition RFC 2616 中定义的文件名称，将作为 Object 元数据保存
void SetContentDisposition(const std::string& str);

// Content-Encoding    RFC 2616 中定义的编码格式，将作为 Object 元数据保存-
void SetContentEncoding(const std::string& str);

// Content-Type    RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存
void SetContentType(const std::string& str);

// Expires RFC 2616 中定义的过期时间，将作为 Object 元数据保存
void SetExpires(const std::string& str);

// 允许用户自定义的头部信息,将作为 Object 元数据返回.大小限制2K
void SetXCosMeta(const std::string& key, const std::string& value);

// x-cos-storage-class 设置 Object 的存储级别，枚举值：STANDARD,STANDARD_IA，ARCHIVE
// 默认值：STANDARD
void SetXCosStorageClass(const std::string& storage_class);

// 定义 Object 的 ACL 属性,有效值：private,public-read
// 默认值：private
void SetXcosAcl(const std::string& str);

// 赋予被授权者读的权限.格式：x-cos-grant-read: id=" ",id=" ".
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantRead(const std::string& str);

// 赋予被授权者读写权限.格式：x-cos-grant-full-control: id=" ",id=" ".
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantFullControl(const std::string& str);

/// 设置 Server 端加密使用的算法, 目前支持 AES256
void SetXCosServerSideEncryption(const std::string& str);

```

当成功执行此请求后，返回的 response 中会包含 bucket、key、uploadId， 分别表示分块上传的目标 Bucket、Object 名称以及后续分块上传所需的编号。

InitMultiUploadResp 的成员函数如下:

```cpp
std::string GetBucket();
std::string GetKey();
std::string GetUploadId();

// Server端加密使用的算法
std::string GetXCosServerSideEncryption();
```

### <span id = "MULIT_UPLOAD_PART"> 上传分块 </span>

上传分块（Upload Part）。

#### 方法原型

```cpp
CosResult UploadPartData(const UploadPartDataReq& request, UploadPartDataResp* response)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "test_object";

// 上传第一个分块
{
    std::fstream is("demo_5M.part1");
    qcloud_cos::UploadPartDataReq req(bucket_name, object_name, upload_id, is);
    req.SetPartNumber(1);
    // 关闭 MD5 校验，开启使用 req.TurnOnComputeConentMd5()，默认情况开启
    req.TurnOffComputeConentMd5();
    qcloud_cos::UploadPartDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartData(req, &resp);

    // 上传成功需要记录分块编号以及返回的 ETag
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_numbers.push_back(1);
    }
    is.close();
}

// 上传第二个分块
{
    std::fstream is("demo_5M.part2");
    qcloud_cos::UploadPartDataReq req(bucket_name, object_name,
                                      upload_id, is);
    req.SetPartNumber(2);
    qcloud_cos::UploadPartDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartData(req, &resp);

    // 上传成功需要记录分块编号以及返回的 ETag 
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_numbers.push_back(2);
    }
    is.close();
}
```

#### 参数说明

| 参数 | 参数描述                                      |
| ---- | --------------------------------------------- |
| req  | UploadPartDataReq，UploadPartData 操作的请求  |
| resp | UploadPartDataResp，UploadPartData 操作的返回 |

UploadPartDataReq 在构造时，需要指明请求的 APPID、Bucket、Object、初始化成功后获取的 UploadId，以及上传的数据流（调用完成后，流由调用方自己负责关闭）。

```
UploadPartDataReq(const std::string& bucket_name,
                    const std::string& object_name, const std::string& upload_id,
                    std::istream& in_stream);

```

此外，请求还需要设置分块编号, 这个分块在完成分块上传时也会用到。

```
void SetPartNumber(uint64_t part_number);

```

UploadPartDataResp 的成员函数如下：

```
/// Server 端加密使用的算法
std::string GetXCosServerSideEncryption();

```

### 复制分块

将其他对象复制为一个分块。

#### 方法原型

```cpp
CosResult UploadPartCopyData(const UploadPartCopyDataReq& request,UploadPartCopyDataResp* response)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "test_object";

std::string upload_id;
std::vector<uint64_t> numbers;
std::vector<std::string> etags;
std::string etag1 = "", etag2 = "";
InitMultiUpload(cos, bucket_name, object_name, &upload_id);

// First part
qcloud_cos::UploadPartCopyDataReq req(bucket_name, object_name, upload_id, 1);
req.SetXCosCopySource("sevenyousouth-1251668577.cos.ap-guangzhou.myqcloud.com/seven_10G.tmp");
req.SetXCosCopySourceRange("bytes=0-1048576000");                         qcloud_cos::UploadPartCopyDataResp resp;                                 qcloud_cos::CosResult result = cos.UploadPartCopyData(req, &resp);
if（result.IsSucc()) {
    etag1 = resp.GetEtag();
}
numbers.push_back(1);
etags.push_back(etag1);

// Second part
qcloud_cos::UploadPartCopyDataReq req2(bucket_name, object_name, upload_id, 2);                                                       req2.SetXCosCopySource("sevenyoutest-7319456.cos.cn-north.myqcloud.com/sevenyou_2G_part");
req2.SetXCosCopySourceRange("bytes=1048576000-2097152000");
qcloud_cos::UploadPartCopyDataResp resp2;
qcloud_cos::CosResult result = cos.UploadPartCopyData(req2, &resp2);
if（result.IsSucc()) {
    etag2 = resp2.GetEtag();
}
numbers.push_back(2)；
etags.push_back(etag2);

CompleteMultiUpload(cos, bucket_name, object_name, upload_id, etags, numbers);
```

#### 参数说明

| 参数 | 参数描述                                              |
| ---- | ----------------------------------------------------- |
| req  | UploadPartCopyDataReq，UploadPartCopyData 操作的请求  |
| resp | UploadPartCopyDataResp，UploadPartCopyData 操作的返回 |

```cpp
/// 设置本次分块复制的 ID
void SetUploadId(const std::string& upload_id)
/// 设置本次分块复制的编号
void SetPartNumber(uint64_t part_number)
/// 设置本次分块复制的源文件 URL 路径，可以通过 versionid 子资源指定历史版本
void SetXCosCopySource(const std::string& src)
/// 设置源文件的字节范围，范围值必须使用 bytes=first-last 格式。
void SetXCosCopySourceRange(const std::string& range)
 /// 当 Object 在指定时间后被修改，则执行操作，否则返回 412
void SetXCosCopySourceIfModifiedSince(const std::string& date)
/// 当 Object 在指定时间后未被修改，则执行操作，否则返回 412
void SetXCosCopySourceIfUnmodifiedSince(const std::string& date)
/// 当 Object 的 Etag 和给定一致时，则执行操作，否则返回 412 
void SetXCosCopySourceIfMatch(const std::string& etag)
/// 当 Object 的 Etag 和给定不一致时，则执行操作，否则返回 412
void SetXCosCopySourceIfNoneMatch(const std::string& etag)
```

```
/// 获取返回文件的MD5算法校验值。
std::string GetEtag() const
/// 返回文件最后修改时间，GMT 格式
std::string GetLastModified() const
/// Server端加密使用的算法
std::string GetXCosServerSideEncryption() const
```

### 查询已上传块

#### 功能说明

查询特定分块上传操作中的已上传的块。

#### 方法原型

```cpp
CosResult ListParts(const ListPartsReq& req, ListPartsResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "test_object";

// uploadId 是调用 InitMultiUpload 后获取的
qcloud_cos::ListPartsReq req(bucket_name, object_name, upload_id);
req.SetMaxParts(1);                                                                                                                                                               
req.SetPartNumberMarker("1");
qcloud_cos::ListPartsResp resp;
qcloud_cos::CosResult result = cos.ListParts(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

#### 参数说明

| 参数 | 参数描述                            |
| ---- | ----------------------------------- |
| req  | ListPartsReq，ListParts 操作的请求  |
| resp | ListPartsResp，ListParts 操作的返回 |

ListPartsReq 包含以下成员函数：

```
// 构造函数，Bucket 名、Object 名、分块上传的 ID
ListPartsReq(const std::string& bucket_name,                                                                                                                                      
             const std::string& object_name,
             const std::string& upload_id); 

// \brief 规定返回值的编码方式
void SetEncodingType(const std::string& encoding_type);

// \brief 单次返回最大的条目数量，若不设置，默认1000
void SetMaxParts(uint64_t max_parts);

// \brief 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始
void SetPartNumberMarker(const std::string& part_number_marker);

```

ListPartsResp 包含以下成员函数：

```
// 分块上传的目标 Bucket
std::string GetBucket();

// 规定返回值的编码方式
std::string GetEncodingType();

// Object 的名称
std::string GetKey();

// 标识本次分块上传的 ID
std::string GetUploadId();

// 用来表示本次上传发起者的信息
Initiator GetInitiator();

// 用来表示这些分块所有者的信息
Owner GetOwner();

// 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始
uint64_t GetPartNumberMarker();

// 返回每一个块的信息
std::vector<Part> GetParts();

// 假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点
uint64_t GetNextPartNumberMarker();

// 用来表示这些分块的存储级别，枚举值：Standard，Standard_IA，ARCHIVE
std::string GetStorageClass();

// 单次返回最大的条目数量
uint64_t GetMaxParts();

// 返回条目是否被截断，布尔值：TRUE，FALSE
bool IsTruncated();

```

其中 Part、Owner、Initiator 的定义如下：

```cpp
struct Initiator {
    std::string m_id; // 创建者的一个唯一标识
    std::string m_display_name; // 创建者的用户名描述
};

struct Owner {
    std::string m_id; // 用户的一个唯一标识
    std::string m_display_name; // 用户名描述
};

struct Part {
    uint64_t m_part_num; // 块的编号
    uint64_t m_size; // 块大小，单位 Byte
    std::string m_etag; // Object 块的 MD5 算法校验值
    std::string m_last_modified; // 块最后修改时间
};

```

### 完成分块上传

#### 功能说明

完成整个文件的分块上传。

#### 方法原型

```cpp
CosResult CompleteMultiUpload(const CompleteMultiUploadReq& request, CompleteMultiUploadResp* response)
```

#### 请求示例

```cpp
qcloud_cos::CompleteMultiUploadReq req(bucket_name, object_name, upload_id);
qcloud_cos::CompleteMultiUploadResp resp;
req.SetEtags(etags);
req.SetPartNumbers(part_numbers);

qcloud_cos::CosResult result = cos.CompleteMultiUpload(req, &resp);
```

#### 参数说明

| 参数 | 参数描述                                                |
| ---- | ------------------------------------------------------- |
| req  | CompleteMultiUploadReq，CompleteMultiUpload 操作的请求  |
| resp | CompleteMultiUploadResp，CompleteMultiUpload 操作的返回 |

CompleteMultiUploadReq 在构造时，需要指明请求的 APPID、Bucket、Object、初始化成功后获取的 UploadId。

```
CompleteMultiUploadReq(const std::string& bucket_name,
                       const std::string& object_name, const std::string& upload_id)

```

此外，request 还需要设置所有上传的分块编号和 ETag。

```
// 调用下列方法时，应注意编号和 ETag 的顺序必须一一对应
void SetPartNumbers(const std::vector<uint64_t>& part_numbers);
void SetEtags(const std::vector<std::string>& etags) ;

// 添加 part_number 和 ETag 对
void AddPartEtagPair(uint64_t part_number, const std::string& etag);

/// 设置 Server 端加密使用的算法, 目前支持 AES256
void SetXCosServerSideEncryption(const std::string& str);
```

CompleteMultiUploadResp 的返回内容中包括 Location、Bucket、Key、ETag，分别表示创建的 Object 的外网访问域名、分块上传的目标 Bucket、Object 的名称、合并后文件的 MD5 算法校验值。可以调用下列成员函数对 response 中的内容进行访问。

```
std::string GetLocation();
std::string GetKey();
std::string GetBucket();
std::string GetEtag();

// Server端加密使用的算法
std::string GetXCosServerSideEncryption();

```

### 终止分块上传

#### 功能说明

终止一个分块上传操作并删除已上传的块。

#### 方法原型

```cpp
CosResult AbortMultiUpload(const AbortMultiUploadReq& request, AbortMultiUploadResp* response)
```

#### 请求示例

```cpp
qcloud_cos::AbortMultiUploadReq req(bucket_name, object_name, upload_id);
qcloud_cos::AbortMultiUploadResp resp;
qcloud_cos::CosResult result = cos.AbortMultiUpload(req, &resp);
```

#### 参数说明

| 参数 | 参数描述                                          |
| ---- | ------------------------------------------------- |
| req  | AbortMultiUploadReq，AbortMultiUpload 操作的请求  |
| resp | AbortMultiUploadResp，AbortMultiUpload 操作的返回 |

AbortMultiUploadReq 需要在构造的时候指明 Bucket、Object 以及 Upload_id。

```cpp
AbortMultiUploadReq(const std::string& bucket_name,
                    const std::string& object_name, const std::string& upload_id);
```

无特殊方法，可调用 BaseResp 的成员函数来获取公共头部内容。

## 其他操作

### 恢复归档对象 

#### 功能说明

将归档类型的对象取回访问。

#### 方法原型

```cpp
CosResult PostObjectRestore(const PostObjectRestoreReq& req, PostObjectRestoreResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "sevenyou";

{   
    qcloud_cos::PostObjectRestoreReq req(bucket_name, object_name);
    req.SetExiryDays(30);
    req.SetTier("Standard");
    qcloud_cos::PostObjectRestoreResp resp;
    qcloud_cos::CosResult result = cos.PostObjectRestore(req, &resp);
    // 调用成功，调用 resp 的成员函数获取返回内容
    if (result.IsSucc()) {
        // ...
    } else {
        // 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
    } 
}   
```

#### 参数说明

| 参数 | 参数描述                                             |
| ---- | ---------------------------------------------------- |
| req  | PostObjectRestoreReq，PostObjectRestore 操作的请求   |
| resp | PostObjectRestoreResp， PostObjectRestore 操作的返回 |

PostObjectRestoreReq 包含以下成员函数：

```
// 设置临时副本的过期时间
void SetExiryDays(uint64_t days);

// 枚举值： Expedited ，Standard ，Bulk；默认值：Standard
void SetTier(const std::string& tier);
```

### 设置对象 ACL

#### 功能说明

设置对象的访问控制列表。

#### 方法原型

```cpp
CosResult PutObjectACL(const PutObjectACLReq& req, PutObjectACLResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "sevenyou";

// 1 设置 ACL 配置（通过 Body, 设置 ACL 可以通过 Body、Header 两种方式，但只能二选一，否则会有冲突）
{   
    qcloud_cos::PutObjectACLReq req(bucket_name, object_name);
    qcloud_cos::Owner owner = {"qcs::cam::uin/xxxxx:uin/xxx", "qcs::cam::uin/xxxxxx:uin/xxxxx" };
    qcloud_cos::Grant grant;
    req.SetOwner(owner);
    grant.m_grantee.m_type = "Group";
    grant.m_grantee.m_uri = "http://cam.qcloud.com/groups/global/AllUsers";
    grant.m_perm = "READ";
    req.AddAccessControlList(grant);

    qcloud_cos::PutObjectACLResp resp;
    qcloud_cos::CosResult result = cos.PutObjectACL(req, &resp);
    // 调用成功，调用 resp 的成员函数获取返回内容
    if (result.IsSucc()) {
        // ...
    } else {
        // 设置 ACL，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
    } 
}   

// 2 设置 ACL 配置（通过 Header, 设置 ACL 可以通过 Body、Header 两种方式，但只能二选一，否则会有冲突）
{   
    qcloud_cos::PutObjectACLReq req(bucket_name, object_name);                                                                                                                    
    req.SetXCosAcl("public-read-write");

    qcloud_cos::PutObjectACLResp resp;
    qcloud_cos::CosResult result = cos.PutObjectACL(req, &resp);
    // 调用成功，调用 resp 的成员函数获取返回内容
    if (result.IsSucc()) {
        // ...
    } else {
        // 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
    } 
}   
```



#### 参数说明

| 参数 | 参数描述                                  |
| ---- | ----------------------------------------- |
| req  | PutObjectACLReq，PutObjectACL 操作的请求  |
| resp | PutObjectACLResp，PutObjectACL 操作的返回 |

PutObjectACLReq 包含以下成员函数：

```
// 定义 Object 的 ACL 属性,有效值：private,public-read
// 默认值：private
void SetXCosAcl(const std::string& str);

// 赋予被授权者读的权限。格式：id="[OwnerUin]" 
void SetXCosGrantRead(const std::string& str);

// 赋予被授权者所有的权限。格式：id="[OwnerUin]"
void SetXCosGrantFullControl(const std::string& str);

// Object 持有者 ID
void SetOwner(const Owner& owner);

// 设置被授权者信息与权限信息
void SetAccessControlList(const std::vector<Grant>& grants);

// 添加单个 Object 的授权信息
void AddAccessControlList(const Grant& grant);
        

```

> !SetXCosAcl/SetXCosGrantRead/SetXCosGrantWrite/SetXCosGrantFullControl 这类接口与  SetAccessControlList/AddAccessControlList 不可同时使用。因为前者实际是通过设置 HTTP Header 实现，而后者是在Body 中添加了 XML 格式的内容，二者只能二选一。SDK 内部优先使用第一类。

ACLRule 定义如下：

```
struct Grantee {
    // type 类型可以为 RootAccount， SubAccount
    // 当 type 类型为 RootAccount 时，可以在 id 中 uin 填写帐号 ID，也可以用 anyone（指代所有类型用户）代替 uin/<OwnerUin> 和 uin/<SubUin>
    // 当 type 类型为 RootAccount 时，uin 代表根账户账号，Subaccount 代表子账户账号
    std::string m_type; 
    std::string m_id; // qcs::cam::uin/<OwnerUin>:uin/<SubUin>
    std::string m_display_name; // 非必选
    std::string m_uri;
};

struct Grant {
    Grantee m_grantee; // 被授权者资源信息
    std::string m_perm; // 指明授予被授权者的权限信息，枚举值：READ，FULL_CONTROL
};


```

### 查询对象 ACL

#### 功能说明

查询对象的访问控制列表。

#### 方法原型

```cpp
CosResult GetObjectACL(const DGetObjectACLReq& req, GetObjectACLResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "exampleobject";

// GetObjectACLReq 的构造函数需要传入 Object_name
qcloud_cos::GetObjectACLReq req(bucket_name, object_name);
qcloud_cos::GetObjectACLResp resp;
qcloud_cos::CosResult result = cos.GetObjectACL(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

#### 参数说明

| 参数 | 参数描述                                  |
| ---- | ----------------------------------------- |
| req  | GetObjectACLReq，GetObjectACL 操作的请求  |
| resp | GetObjectACLResp，GetObjectACL 操作的返回 |

GetObjectACLResp 包含以下成员函数：

```
std::string GetOwnerID();
std::string GetOwnerDisplayName();
std::vector<Grant> GetAccessControlList();
```

## 高级接口（推荐）

### 复合上传

#### 功能说明

封装分块上传各接口，并发上传。

#### 方法原型

```cpp
CosResult MultiUploadObject(const MultiUploadObjectReq& request, MultiUploadObjectResp* response)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "exampleobject";
std::string local_file = "./test"

qcloud_cos::MultiUploadObjectReq req(bucket_name, object_name, local_file);
// Complete 接口内部 chunk 保活，建议设置较长时间的 timeout。
req.SetRecvTimeoutInms(1000 * 60);
qcloud_cos::MultiUploadObjectResp resp;
qcloud_cos::CosResult result = cos.MultiUploadObject(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
	// 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

#### 参数说明

| 参数 | 参数描述                                            |
| ---- | --------------------------------------------------- |
| req  | MultiUploadObjectReq，MultiUploadObject 操作的请求  |
| resp | MultiUploadObjectResp，MultiUploadObject 操作的返回 |

MultiUploadObjectReq 包含以下成员函数：

```cpp
// 设置分块大小，若小于1M，则按1M计算；若大于5G，则按5G计算
void SetPartSize(uint64_t bytes)
// 允许用户自定义的头部信息，将作为 Object 元数据返回，大小限制2K 
void SetXCosMeta(const std::string& key, const std::string& value)
// 设置 Server 端加密使用的算法，目前支持 AES256
void SetXCosServerSideEncryption(const std::string& str)
// 设置内部线程池大小
void SetThreadPoolSize(int size)
```

MultiUploadObjectResp 包含以下成员函数：

```
std::string GetRespTag()
/// Server 端加密使用的算法 
std::string GetXCosServerSideEncryption() const
```

### 复合下载

#### 功能说明

并发 Range 下载。

#### 方法原型

```cpp
CosResult GetObject(const MultiGetObjectReq& request, 
MultiGetObjectResp* response)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "exampleobject";
std::string file_path = "./test";

qcloud_cos::MultiGetObjectReq req(bucket_name, object_name, file_path);   qcloud_cos::MultiGetObjectResp resp;                                     qcloud_cos::CosResult result = cos.GetObject(req, &resp); 

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

#### 参数说明

| 参数 | 参数描述                                 |
| ---- | ---------------------------------------- |
| req  | MultiGetObjectReq，GetObject 操作的请求  |
| resp | MultiGetObjectResp，GetObject 操作的返回 |

MultiGetObjectReq 包含以下成员函数：

```cpp
// 设置分块大小
void SetSliceSize(uint64_t bytes)
// 设置线程池大小
void SetThreadPoolSize(int size)
```

MultiGetObjectResp 包含以下成员函数：

```cpp
/// Server 端加密使用的算法
std::string GetXCosServerSideEncryption() const
```
