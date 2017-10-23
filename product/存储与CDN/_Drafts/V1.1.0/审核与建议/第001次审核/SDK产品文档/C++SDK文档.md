## 开发准备

### 相关资源

> <font size=4 color=red> 如果在标准的包管理工具，比如ruby的gem之类的，可以在这里说一下</font>
> by stongdong


> <font size=4 color=red>  把Demo的地址附上来，可以引导用户去demo里面查看</font>
> by stongdong


依赖静态库: jsoncpp boost_system boost_thread Poco (在lib文件夹下)
依赖动态库: ssl crypto rt z (需要安装)

1. 安装boost的库和头文件 [http://www.boost.org/](http://www.boost.org/)
2. 安装cmake工具 [http://www.cmake.org/download/](http://www.cmake.org/download/)
3. 安装openssl的库和头文件 http://www.openssl.org/source/  
4. 安装Poco的库和头文件 [https://pocoproject.org/download/index.html](https://pocoproject.org/download/index.html)
5. 从控制台获取APP ID、SecretID、SecretKey。



sdk中提供了Poco、jsoncpp的库以及头文件，以上库编译好后替换掉sdk中相应的库和头文件即可，如果以上库已经安装到系统里，也可删除sdk中相应的库和头文件。
可以修改CMakeList.txt文件中，指定本地boost头文件路径，修改如下语句： SET(BOOST_HEADER_DIR "/root/boost_1_61_0")

### SDK 配置

> <font size=4 color=red> 如果在标准的IDE或者工程之类的工具，可以在这里说一下</font>
> by stongdong


直接下载github上提供的源代码，集成到您的开发环境。

执行下面的命令 ：
``` bash
cd ${cos-cpp-sdk}
mkdir -p build
cd build
cmake ..
make
```

cos_demo.cpp里面有常见API的例子。生成的cos_demo可以直接运行，生成的静态库名称为：libcossdk.a。生成的 libcossdk.a 放到你自己的工程里lib路径下，include 目录拷贝到自己的工程的include路径下。

## 初始化操作

### 初始化
接口说明：在使用COS操作之前，需要首先进行COS系统参数的设置，然后分别创建CosConfig以及CosAPI对象，COS的操作都是基于CosAPI对象进行的。

> <font size=4 color=red> 这个接口说明在这里有点，不知道要说什么</font>
> by stongdong


> <font size=4 color=red> 关键的数据appid region secretId 和 secretKey从哪里获取，要写出来，并给出链接</font>
> by stongdong

### 配置文件

```
"AppID":********,
"AccessKey":"*********************************",
"SecretKey":"********************************",
"Region":"cn-north",                // COS区域, 一定要保证正确
"SignExpiredTime":360,              // 签名超时时间, 单位s
"ConnectTimeoutInms":6000,          // connect超时时间, 单位ms
"HttpTimeoutInms":60000,            // http超时时间, 单位ms
"UploadPartSize":1048576,           // 上传文件分块大小，1M~5G, 默认为1M
"UploadThreadPoolSize":5,           // 单文件分块上传线程池大小
"DownloadSliceSize":4194304,        // 下载文件分片大小
"DownloadThreadPoolSize":5,         // 单文件下载线程池大小
"AsynThreadPoolSize":2,             // 异步上传下载线程池大小
"LogoutType":1,                     // 日志输出类型,0:不输出,1:输出到屏幕,2输出到syslog
"LogLevel":3                        // 日志级别:1: ERR, 2: WARN, 3:INFO, 4:DBG
```

### COS API对象构造原型

```
CosConfig(const string& config_file); // config_file是配置文件所在路径
CosAPI(CosConfig& config);
```


> <font size=4 color=red> 这里需要是使用的范例， 不是接口说明哈！！ </font>
> by stongdong




> <font size=4 color=red> 关键的几个过程 文档上传、下载需要把使用的范例给出来。 </font>
> by stongdong


## 生成签名

### Sign
#### 功能说明
 生成签名

#### 方法原型1
```
static std::string Sign(const std::string& secret_id,
                        const std::string& secret_key,
                        const std::string& http_method,
                        const std::string& in_uri,
                        const std::map<std::string, std::string>& headers,
                        const std::map<std::string, std::string>& params);
```

#### 参数说明

- secret_id   —— String             开发者拥有的项目身份识别 ID，用以身份认证
- secret_key  —— String             开发者拥有的项目身份密钥
- http_method —— String             http方法,如POST/GET/HEAD/PUT等, 传入大小写不敏感
- in_uri      —— String             http uri
- headers     —— map<string,string> http header的键值对
- params      —— map<string,string> http params的键值对

#### 返回结果说明

- 返回签名，可以在指定的有效期内(通过CosSysConfig设置, 默认60s)使用, 返回空串表示签名失败

#### 方法原型2
```
static std::string Sign(const std::string& secret_id,
                        const std::string& secret_key,
                        const std::string& http_method,
                        const std::string& in_uri,
                        const std::map<std::string, std::string>& headers,
                        const std::map<std::string, std::string>& params,
                        uint64_t start_time_in_s,
                        uint64_t end_time_in_s);
```
#### 参数说明

- secret_id   —— String             开发者拥有的项目身份识别 ID，用以身份认证
- secret_key  —— String             开发者拥有的项目身份密钥
- http_method —— String             http方法,如POST/GET/HEAD/PUT等, 传入大小写不敏感
- in_uri      —— String             http uri
- headers     —— map<string,string> http header的键值对
- params      —— map<string,string> http params的键值对
- start_time_in_s —— uint64_t       签名生效的开始时间
- end_time_in_s —— uint64_t         签名生效的截止时间

#### 返回结果说明
- String, 返回签名，可以在指定的有效期内使用, 返回空串表示签名失败


## Service/Bucket/Object 操作
所有与Service/Bucket/Object相关的方法原型，均是如下形式`CosResult Operator(BaseReq, BaseResp)`。

### CosResult
 封装了请求出错时返回的错误码和对应错误信息，详见[官网链接](https://www.qcloud.com/document/product/436/773 "错误码")。
**sdk内部封装的请求均会返回CosResult对象，每次调用完成后，均要使用IsSucc()成员函数判断本次调用是否成功。**

#### 成员函数：
`bool isSucc()`, 返回本次调用成功或失败，当返回false时， 后续的CosResult成员函数才有意义。当返回True时，可以从OperatorResp中获取具体返回内容。

`string GetErrorCode()`， 获取cos返回的错误码，用来确定错误场景。

`string GetErrorMsg()`， 包含具体的错误信息。

`string GetResourceAddr()`， 资源地址：Bucket地址或者Object地址。    

`string GetXCosRequestId()`， 当请求发送时，服务端将会自动为请求生成一个唯一的 ID。使用遇到问题时，request-id能更快地协助 COS 定位问题。

`string GetXCosTraceId()`， 当请求出错时，服务端将会自动为这个错误生成一个唯一的 ID。使用遇到问题时，trace-id能更快地协助 COS 定位问题。当请求出错时，trace-id与request-id一一对应。

`string GetErrorInfo()`, 获取sdk内部错误信息。

`int GetHttpStatus()`， 获取http状态码。

#### BaseReq/BaseResp
BaseReq、BaseResp 封装了请求和返回， 调用者只需要根据不同的操作类型生成不同的OperatorReq（比如后文介绍的GetBucketReq), 并填充OperatorReq的内容即可。
函数返回后，调用对应BaseResp的成员函数获取请求结果。

对于Request，如无特殊说明，仅需要关注request的构造函数。
对于Response，所有方法的response均有获取公共返回头部的成员函数。
Response的公共成员函数如下， 具体字段含义见[公共返回头部](https://www.qcloud.com/document/product/436/7729 "公共返回头部")， 此处不再赘述：
```
uint64_t GetContentLength();
std::string GetContentType();
std::string GetEtag();
std::string GetConnection();
std::string GetDate();
std::string GetServer();
std::string GetXCosRequestId();
std::string GetXCosTraceId();
```


## Bucket操作

###  Get Bucket

#### 功能说明

Get Bucket请求等同于List Object请求，可以列出该Bucekt下部分或者所有Object，发起该请求需要拥有Read权限。详见:https://www.qcloud.com/document/product/436/773

#### 方法原型

```cpp
CosResult GetBucket(const GetBucketReq& req, GetBucketResp* resp);
```

#### 参数说明

- req   —— GetBucketReq GetBucket操作的请求

- resp   —— GetBucketResp GetBucket操作的返回

GetBucketResp提供以下成员函数，用于获取GetBucket返回的xml格式中的具体内容。
```C++
std::vector<Content> GetContents();
std::string GetName();
std::string GetPrefix();
std::string GetMarker();
uint64_t GetMaxKeys();
bool IsTruncated();
std::vector<std::string> GetCommonPrefixes();
```
#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5";

// GetBucketReq的构造函数需要传入appId与bucket_name
qcloud_cos::GetBucketReq req(bucket_name);
qcloud_cos::GetBucketResp resp;
qcloud_cos::CosResult result = cos.GetBucket(req, &resp);

// 调用成功，调用resp的成员函数获取返回内容
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

## Object操作

###  Get Object

#### 功能说明

Get Object 请求可以将一个文件（Object）下载至本地或指定流中。该操作需要对目标 Object 具有读权限或目标 Object 对所有人都开放了读权限（公有读）。

#### 方法原型

```cpp
// 将Object下载到本地文件中
CosResult GetObject(const GetObjectByFileReq& req, GetObjectByFileResp* resp);

// 将Object下载到流中
CosResult GetObject(const GetObjectByStreamReq& req, GetObjectByStreamResp* resp);

// 将Object下载到本地文件中（多线程）
CosResult GetObject(const MultiGetObjectReq& req, MultiGetObjectResp* resp);
```

#### 参数说明

- req   —— GetObjectByFileReq/GetObjectByStreamReq/MultiGetObjectReq GetObject操作的请求

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

- resp   —— GetObjectByFileResp/GetObjectByStreamResp/MultiGetObjectResp GetObject操作的返回

GetObjectResp除了读取公共头部的成员函数外，还提供以下成员函数，
```C++
// 获取object最后被修改的时间, 字符串格式Date, 类似"Wed, 28 Oct 2014 20:30:00 GMT"
std::string GetLastModified();

// 获取object type, 表示object是否可以被追加上传，枚举值：normal 或者 appendable
std::string GetXCosObjectType();

// 获取Object 的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE
std::string GetXCosStorageClass();

// 以map形式返回所有自定义的meta, map的key均不包含"x-cos-meta-"前缀
std::map<std::string, std::string> GetXCosMetas();

// 获取自定义的meta, 参数可以为x-cos-meta-*中的*
std::string GetXCosMeta(const std::string& key);
```
#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5";
std::string object_name = "object_name";
std::string local_path = "/tmp/object_name";

// 下载到本地文件
{
    // request需要提供appid、bucketname、object,以及本地的路径（包含文件名）
    qcloud_cos::GetObjectByFileReq req(bucket_name, object_name, local_path);
    qcloud_cos::GetObjectByFileResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // 下载成功，可以调用GetObjectByFileResp的成员函数
    } else {
        // 下载失败，可以调用CosResult的成员函数输出错误信息，比如requestID等
    }
}

// 下载到流中
{
    // request需要提供appid、bucketname、object, 以及输出流
    std::ostringstream os;
    qcloud_cos::GetObjectByStreamReq req(bucket_name, object_name, os);
    qcloud_cos::GetObjectByStreamResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // 下载成功，可以调用GetObjectByStreamResp的成员函数
    } else {
        // 下载失败，可以调用CosResult的成员函数输出错误信息，比如requestID等
    }
}

// 多线程下载文件到本地
{
    // request需要提供appid、bucketname、object,以及本地的路径（包含文件名）
    qcloud_cos::MultiGetObjectReq req(bucket_name, object_name, local_path);
    qcloud_cos::MultiGetObjectResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // 下载成功，可以调用MultiGetObjectResp的成员函数
    } else {
        // 下载失败，可以调用CosResult的成员函数输出错误信息，比如requestID等
    }
}
```

###  Head Object

#### 功能说明

Head Object 请求可以取回对应 Object 的元数据，Head的权限与 Get 的权限一致。

#### 方法原型

```cpp
CosResult HeadObject(const HeadObjectReq& req, HeadObjectResp* resp);
```

#### 参数说明
- req   —— HeadObjectReq HeadObject操作的请求

- resp   —— HeadObjectResp HeadObject操作的返回

HeadObjectResp除了读取公共头部的成员函数外，还提供以下成员函数，
```C++
std::string GetXCosObjectType();

std::string GetXCosStorageClass();

// 获取自定义的meta, 参数可以为x-cos-meta-*中的*
std::string GetXCosMeta(const std::string& key);

// 以map形式返回所有自定义的meta, map的key均不包含"x-cos-meta-"前缀
std::map<std::string, std::string> GetXCosMetas()
```
#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5";
std::string object_name = "object_name";
qcloud_cos::HeadObjectReq req(bucket_name, object_name);
qcloud_cos::HeadObjectResp resp;
qcloud_cos::CosResult result = cos.HeadObject(req, &resp);
if (result.IsSucc()) {
    // 下载成功，可以调用HeadObjectResp的成员函数
} else {
    // 下载失败，可以调用CosResult的成员函数输出错误信息，比如requestID等
}
```

###  Put Object

#### 功能说明

Put Object请求可以将一个文件（Oject）上传至指定Bucket。

#### 方法原型

```cpp
/// 通过Stream进行上传
CosResult PutObject(const PutObjectByStreamReq& req, PutObjectByStreamResp* resp);

/// 上传本地文件
CosResult PutObject(const PutObjectByFileReq& req, PutObjectByFileResp* resp);
```

#### 参数说明
- req   ——PutObjectByStreamReq/PutObjectByFileReq PutObject操作的请求

```C++
/// Cache-Control RFC 2616 中定义的缓存策略，将作为 Object 元数据保存
void SetCacheControl(const std::string& str);

/// Content-Disposition RFC 2616 中定义的文件名称，将作为 Object 元数据保存
void SetContentDisposition(const std::string& str);

/// Content-Encoding    RFC 2616 中定义的编码格式，将作为 Object 元数据保存-
void SetContentEncoding(const std::string& str);

/// Content-Type    RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存
void SetContentType(const std::string& str);

/// Expect  当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容
void SetExpect(const std::string& str);

/// Expires RFC 2616 中定义的过期时间，将作为 Object 元数据保存
void SetExpires(const std::string& str);

/// 允许用户自定义的头部信息,将作为 Object 元数据返回.大小限制2K
void SetXCosMeta(const std::string& key, const std::string& value);

/// x-cos-storage-class 设置 Object 的存储级别，枚举值：STANDARD,STANDARD_IA，NEARLINE，
/// 默认值：STANDARD（目前仅支持华南园区）
void SetXCosStorageClass(const std::string& storage_class);

/// 定义Object的ACL属性,有效值：private,public-read-write,public-read
/// 默认值：private
void SetXcosAcl(const std::string& str);

/// 赋予被授权者读的权限.格式：x-cos-grant-read: id=" ",id=" ".
/// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
/// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantRead(const std::string& str);

/// 赋予被授权者写的权限,格式：x-cos-grant-write: id=" ",id=" "./
/// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
/// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantWrite(const std::string& str);

/// 赋予被授权者读写权限.格式：x-cos-grant-full-control: id=" ",id=" ".
/// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
/// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantFullControl(const std::string& str);
```

- resp   ——PutObjectByStreamResp/PutObjectByFileResp PutObject操作的返回

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5";
std::string object_name = "object_name";

// 简单上传(流)
{
    std::istringstream iss("put object");
    // request的构造函数中需要传入istream
    qcloud_cos::PutObjectByStreamReq req(bucket_name, object_name, iss);
    // 调用Set方法设置元数据或者ACL等
    req.SetXCosStorageClass("STANDARD_IA");
    qcloud_cos::PutObjectByStreamResp resp;
    qcloud_cos::CosResult result = cos.PutObject(req, &resp);

    if (result.IsSucc()) {
        // 调用成功，调用resp的成员函数获取返回内容
        do sth
    } else {
        // 调用失败，调用result的成员函数获取错误信息
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
    // request的构造函数中需要传入本地文件路径
    qcloud_cos::PutObjectByFileReq req(bucket_name, object_name, "/path/to/local/file");
    // 调用Set方法设置元数据或者ACL等
    req.SetXCosStorageClass("STANDARD_IA");
    qcloud_cos::PutObjectByFileResp resp;
    qcloud_cos::CosResult result = cos.PutObject(req, &resp);
        if (result.IsSucc()) {
        // 调用成功，调用resp的成员函数获取返回内容
        do sth
    } else {
        // 调用失败，调用result的成员函数获取错误信息
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


## 分块上传操作

###  Initiate Multipart Upload

#### 功能说明

Initiate Multipart Upload请求实现初始化分片上传，成功执行此请求以后会返回Upload ID用于后续的Upload Part请求。

#### 方法原型

```cpp
CosResult InitMultiUpload(const InitMultiUploadReq& req, InitMultiUploadResp* resp);
```

#### 参数说明
- req   —— InitMultiUploadReq InitMultiUpload操作的请求

```
/// Cache-Control RFC 2616 中定义的缓存策略，将作为 Object 元数据保存
void SetCacheControl(const std::string& str);

/// Content-Disposition RFC 2616 中定义的文件名称，将作为 Object 元数据保存
void SetContentDisposition(const std::string& str);

/// Content-Encoding    RFC 2616 中定义的编码格式，将作为 Object 元数据保存-
void SetContentEncoding(const std::string& str);

/// Content-Type    RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存
void SetContentType(const std::string& str);

/// Expires RFC 2616 中定义的过期时间，将作为 Object 元数据保存
void SetExpires(const std::string& str);

/// 允许用户自定义的头部信息,将作为 Object 元数据返回.大小限制2K
void SetXCosMeta(const std::string& key, const std::string& value);

/// x-cos-storage-class 设置 Object 的存储级别，枚举值：STANDARD,STANDARD_IA，NEARLINE，
/// 默认值：STANDARD
void SetXCosStorageClass(const std::string& storage_class);

/// 定义Object的ACL属性,有效值：private,public-read-write,public-read
/// 默认值：private
void SetXcosAcl(const std::string& str);

/// 赋予被授权者读的权限.格式：x-cos-grant-read: id=" ",id=" ".
/// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
/// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantRead(const std::string& str);

/// 赋予被授权者写的权限,格式：x-cos-grant-write: id=" ",id=" "./
/// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
/// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantWrite(const std::string& str);

/// 赋予被授权者读写权限.格式：x-cos-grant-full-control: id=" ",id=" ".
/// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
/// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantFullControl(const std::string& str);
```

- resp   —— InitMultiUploadResp InitMultiUpload操作的返回

如果成功执行此请求后，返回的response中会包含bucket、key、uploadId， 分别表示分片上传的目标 Bucket、object名称以及后续分片上传所需的编号。

``` C++
std::string GetBucket();
std::string GetKey();
std::string GetUploadId();
```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);
std::string bucket_name = "cpp_sdk_v5";
std::string object_name = "object_name";

qcloud_cos::InitMultiUploadReq req(bucket_name, object_name);
qcloud_cos::InitMultiUploadResp resp;
qcloud_cos::CosResult result = cos.InitMultiUpload(req, &resp);

std::string upload_id = "";
if (result.IsSucc()) {
    upload_id = resp.GetUploadId();
}
```

###  Upload Part

#### 功能说明

Upload Part请求实现在初始化以后的分块上传，支持的块的数量为1到10000，块的大小为1 MB 到5 GB。在每次请求Upload Part时候，需要携带partNumber和uploadID，partNumber为块的编号，支持乱序上传。

#### 方法原型

```cpp
CosResult UploadPartData(const UploadPartDataReq& request, UploadPartDataResp* response);
```

#### 参数说明
- req   —— UploadPartDataReq UploadPartData操作的请求

UploadPartDataReq在构造时，需要指明请求的appid、bucket、object、初始化成功后获取的uploadId, 以及上传的数据流(*调用完成后，流由调用方自己负责关闭*)。
```
UploadPartDataReq(const std::string& bucket_name,
                    const std::string& object_name, const std::string& upload_id,
                    std::istream& in_stream);
```
此外，请求还需要设置分片编号, 这个分片在完成分片上传时也会用到。
```
void SetPartNumber(uint64_t part_number);
```

- resp   —— UploadPartDataResp UploadPartData操作的返回


#### 示例

```cpp
// 上传第一个分片
{
    std::fstream is("demo_5M.part1");
    qcloud_cos::UploadPartDataReq req(bucket_name, object_name,
                                      upload_id, is);
    req.SetPartNumber(1);
    qcloud_cos::UploadPartDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartData(req, &resp);

    // 上传成功需要记录分片编号以及返回的etag
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_numbers.push_back(1);
    }
    is.close();
}

// 上传第二个分片
{
    std::fstream is("demo_5M.part2");
    qcloud_cos::UploadPartDataReq req(bucket_name, object_name,
                                      upload_id, is);
    req.SetPartNumber(2);
    qcloud_cos::UploadPartDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartData(req, &resp);

    // 上传成功需要记录分片编号以及返回的etag
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_numbers.push_back(2);
    }
    is.close();
}
```

###  Complete Multipart Upload

#### 功能说明

Complete Multipart Upload用来实现完成整个分块上传。当您已经使用Upload Parts上传所有块以后，你可以用该API完成上传。在使用该API时，您必须在Body中给出每一个块的PartNumber和ETag，用来校验块的准确性。

#### 方法原型

```cpp
CosResult CompleteMultiUpload(const CompleteMultiUploadReq& request, CompleteMultiUploadResp* response);
```

#### 参数说明
- req   —— CompleteMultiUploadReq CompleteMultiUploadReq操作的请求

CompleteMultiUploadReq在构造时，需要指明请求的appid、bucket、object、初始化成功后获取的uploadId。
```
CompleteMultiUploadReq(const std::string& bucket_name,
                       const std::string& object_name, const std::string& upload_id)
```
此外，request还需要设置所有上传的分片编号和Etag。

```
// 调用下列方法时，应注意编号和etag的顺序必须一一对应
void SetPartNumbers(const std::vector<uint64_t>& part_numbers);
void SetEtags(const std::vector<std::string>& etags) ;

// 添加part_number和etag对
void AddPartEtagPair(uint64_t part_number, const std::string& etag);
```

- resp   —— CompleteMultiUploadResp CompleteMultiUpload操作的请求

CompleteMultiUploadResp 的返回内容中包括Location、Bucket、Key、ETag，分别表示创建的Object的外网访问域名、分块上传的目标Bucket、Object的名称、合并后文件的 MD5 算法校验值。可以调用下列成员函数对response中的内容进行访问。

```
std::string GetLocation();
std::string GetKey();
std::string GetBucket();
std::string GetEtag();
```
#### 示例

```cpp
qcloud_cos::CompleteMultiUploadReq req(bucket_name, object_name, upload_id);
qcloud_cos::CompleteMultiUploadResp resp;
req.SetEtags(etags);
req.SetPartNumbers(part_numbers);

qcloud_cos::CosResult result = cos.CompleteMultiUpload(req, &resp);
```

###  Multipart Upload

#### 功能说明

Multipart Upload封装了初始化分块上传、分块上传、完成分块上传三步, 只需要在请求中指明上传的文件。

#### 方法原型

```cpp
CosResult MultiUploadObject(const MultiUploadObjectReq& request,        MultiUploadObjectResp* response);
```

#### 参数说明

- req   —— MultiUploadObjectReq MultiUploadObject操作的请求

MultiUploadObjectReq需要在构造的时候指明bucket、object以及待上传文件的本地路径， 如果不指明本地路径，则默认是当前工作路径下与object同名的文件。

```
MultiUploadObjectReq(const std::string& bucket_name,
                     const std::string& object_name, const std::string& local_file_path = "");
```

- resp —— MultiUploadObjectResp MultiUploadObject操作的返回

分块上传成功的情况下，该Response的返回内容与CompleteMultiUploadResp一致。
分块上传失败的情况下，该Response根据不同的失败情况，返回内容与InitMultiUploadResp、UploadPartDataResp、CompleteMultiUploadResp一致。可调用`GetRespTag()`来获取具体失败在哪一步。

```
// 返回Init、Upload、Complete
std::string GetRespTag();
```

#### 示例

```cpp
qcloud_cos::MultiUploadObjectReq req( bucket_name, object_name, "/temp/demo_6G.tmp");
qcloud_cos::MultiUploadObjectResp resp;
qcloud_cos::CosResult result = cos.MultiUploadObject(req, &resp);

if (result.IsSucc()) {
    std::cout << resp.GetLocation() << std::endl;
    std::cout << resp.GetKey() << std::endl;
    std::cout << resp.GetBucket() << std::endl;
    std::cout << resp.GetEtag() << std::endl;
} else {
    // 获取具体失败在哪一步
    std::string resp_tag = resp.GetRespTag();
    if ("Init" == resp_tag) {
        // print result
    } else if ("Upload" == resp_tag) {
        // print result
    } else if ("Complete" == resp_tag) {
        // print result
    }
}
```

###  Abort Multipart Upload

#### 功能说明

Abort Multipart Upload用来实现舍弃一个分块上传并删除已上传的块。当您调用Abort Multipart Upload时，如果有正在使用这个Upload Parts上传块的请求，则Upload Parts会返回失败。

#### 方法原型

```cpp
CosResult AbortMultiUpload(const AbortMultiUploadReq& request, AbortMultiUploadResp* response);
```

#### 参数说明
- req    —— AbortMultiUploadReq AbortMultiUpload操作的请求

AbortMultiUploadReq需要在构造的时候指明bucket、object以及upload_id。
``` C++
AbortMultiUploadReq(const std::string& bucket_name,
                    const std::string& object_name, const std::string& upload_id);
```

- resp —— AbortMultiUploadResp AbortMultiUpload操作的返回
无特殊方法，可调用BaseResp的成员函数来获取公共头部内容。

#### 示例

```cpp
qcloud_cos::AbortMultiUploadReq req(bucket_name, object_name,
                                                    upload_id);
qcloud_cos::AbortMultiUploadResp resp;
qcloud_cos::CosResult result = cos.AbortMultiUpload(req, &resp);
```
