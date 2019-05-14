## 生成签名

### Sign 功能说明

生成签名

### 方法原型一

```
static std::string Sign(const std::string& secret_id,
                        const std::string& secret_key,
                        const std::string& http_method,
                        const std::string& in_uri,
                        const std::map<std::string, std::string>& headers,
                        const std::map<std::string, std::string>& params);
```

#### 参数说明 

| 参数名称    | 参数描述                                              | 类型                     |
| ----------- | ----------------------------------------------------- | ------------------------ |
| secret_id   | 开发者拥有的项目身份识别 ID，用以身份认证             | String                   |
| secret_key  | 开发者拥有的项目身份密钥                              | String                   |
| http_method | HTTP 方法，如 POST/GET/HEAD/PUT 等， 传入大小写不敏感 | String                   |
| in_uri      | HTTP uri                                              | String                   |
| headers     | HTTP header 的键值对                                  | map&lt;string,string&gt; |
| params      | HTTP params 的键值对                                  | map&lt;string,string&gt; |

#### 返回结果说明

返回签名，可以在指定的有效期内（通过 CosSysConfig 设置，默认60s）使用，返回空串表示签名失败。

### 方法原型二

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

| 参数名称        | 参数描述                                             | 类型                      |
| --------------- | ---------------------------------------------------- | ------------------------- |
| secret_id       | 开发者拥有的项目身份识别 ID，用以身份认证            | String                    |
| secret_key      | 开发者拥有的项目身份密钥                             | String                    |
| http_method     | HTTP 方法，如 POST/GET/HEAD/PUT 等, 传入大小写不敏感 | String                    |
| in_uri          | HTTP uri                                             | String                    |
| headers         | HTTP header 的键值对                                 | map &lt;string,string&gt; |
| params          | HTTP params 的键值对                                 | map &lt;string,string&gt; |
| start_time_in_s | 签名生效的开始时间                                   | uint64_t                  |
| end_time_in_s   | 签名生效的截止时间                                   | uint64_t                  |

#### 返回结果说明

String， 返回签名，可以在指定的有效期内使用, 返回空串表示签名失败。

## Service/Bucket/Object 操作

所有与 Service/Bucket/Object 相关的方法原型，均表现为如下形式：

```
CosResult Operator(BaseReq, BaseResp)
```

### CosResult

CosResult 封装了请求出错时返回的错误码和对应错误信息，详见 [错误码](/document/product/436/7730 "错误码")。

>!SDK 内部封装的请求均会返回 CosResult 对象，每次调用完成后，均要使用 IsSucc() 成员函数判断本次调用是否成功。

#### 成员函数

| 函数                      | 函数描述                                                     |
| ------------------------- | ------------------------------------------------------------ |
| bool isSucc()             | 返回本次调用成功或失败<br>当返回 false 时：后续的 CosResult 成员函数才有意义<br>当返回 True 时：可以从OperatorResp 中获取具体返回内容 |
| string GetErrorCode()     | 获取 COS 返回的错误码，用来确定错误场景                    |
| string GetErrorMsg()      | 包含具体的错误信息                                         |
| string GetResourceAddr()  | 资源地址，Bucket 地址或 Object 地址                        |
| string GetXCosRequestId() | 当请求发送时，服务端将会自动为请求生成一个唯一的 ID<br>使用遇到问题时，request-id 能更快地协助 COS 定位问题 |
| string GetXCosTraceId() | 当请求出错时，服务端将会自动为这个错误生成一个唯一的 ID<br>使用遇到问题时，trace-id 能更快地协助 COS 定位问题<br>当请求出错时，trace-id 与 request-id 一一对应
| string GetErrorInfo() | 获取 SDK 内部错误信息|
| int GetHttpStatus() | 获取 HTTP 状态码|

#### BaseReq/BaseResp

BaseReq、BaseResp 封装了请求和返回， 调用者只需要根据不同的操作类型生成不同的 OperatorReq（如后文介绍的 GetBucketReq），并填充 OperatorReq 的内容即可。
函数返回后，调用对应 BaseResp 的成员函数获取请求结果。

- 对于 Request，如无特殊说明，仅需要关注 Request 的构造函数。
- 对于 Response，所有方法的 Response 均有获取公共返回头部的成员函数。 
  Response 的公共成员函数如下，具体字段含义参见 [公共返回头部](/document/product/436/7729 "公共返回头部")， 此处不再赘述：

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

## Bucket 操作

### Get Bucket

#### 功能说明

Get Bucket 请求等同于 List Object 请求，可以列出该 Bucekt 下部分或者所有 Object，发起该请求需要拥有 Read 权限。相关 API 文档参见 [Get Bucket](/document/product/436/7734)。

#### 方法原型

```cpp
CosResult GetBucket(const GetBucketReq& req, GetBucketResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                |
| ---- | --------------------------------------- |
| req  | GetBucketReq，GetBucket 操作的请求   |
| resp | GetBucketResp，GetBucket 操作的返回 |

GetBucketResp 提供以下成员函数，用于获取 Get Bucket 返回的 XML 格式中的具体内容。 

```C++
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

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

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

### Put Bucket

#### 功能说明

Put Bucket 接口请求可以在指定账号下创建一个 Bucket。该 API 接口不支持匿名请求，您需要使用帯 Authorization 签名认证的请求才能创建新的 Bucket 。创建 Bucket 的用户默认成为 Bucket 的持有者。相关 API 文档参见 [Put Bucket](/document/product/436/7738)。

#### 方法原型

```cpp
CosResult PutBucket(const PutBucketReq& req, PutBucketResp* resp);
```

#### 参数说明

| 参数 | 参数描述                              |
| ---- | ------------------------------------- |
| req  | PutBucketReq，PutBucket 操作的请求  |
| resp | PutBucketResp，PutBucket 操作的返回 |

PutBucketReq 提供以下成员函数：

```C++
// 定义 Bucket 的 ACL 属性,有效值：private,public-read-write,public-read
// 默认值：private
void SetXCosAcl(const std::string& str);

// 赋予被授权者读的权限.格式：x-cos-grant-read: id=" ",id=" ".
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantRead(const std::string& str);

// 赋予被授权者写的权限,格式：x-cos-grant-write: id=" ",id=" "./
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantWrite(const std::string& str);
    
// 赋予被授权者读写权限.格式：x-cos-grant-full-control: id=" ",id=" ".
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantFullControl(const std::string& str);
```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

qcloud_cos::PutBucketReq req(bucket_name);
qcloud_cos::PutBucketResp resp;
qcloud_cos::CosResult result = cos.PutBucket(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 创建 Bucket 失败，可以调用 CosResult 的成员函数输出错误信息，如requestID 等
} 
```

### Delete Bucket

#### 功能说明

Delete Bucket 接口请求可以在指定账号下删除 Bucket，删除之前要求 Bucket 内的内容为空，只有删除了 Bucket 内的信息，才能删除 Bucket 本身。相关 API 文档参见 [Delete Bucket](/document/product/436/7732)。

#### 方法原型

```cpp
CosResult DeleteBucket(const DeleteBucketReq& req, DeleteBucketResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                   |
| ---- | ------------------------------------------ |
| req  | DeleteBucketReq，DeleteBucket 操作的请求 |
| resp | DeletBucketResp，DeletBucket 操作的返回  |

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// DeleteBucketReq 的构造函数需要传入 bucket_name
qcloud_cos::DeleteBucketReq req(bucket_name);
qcloud_cos::DeleteBucketResp resp;
qcloud_cos::CosResult result = cos.DeleteBucket(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 删除 Bucket 失败，可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

### Put Bucket Replication

#### 功能说明

Put Bucket Replication 请求用于向开启版本管理的存储桶添加 replication 配置。如果存储桶已经拥有 replication 配置，那么该请求会替换现有配置。

#### 方法原型

```cpp
CosResult PutBucketReplication(const DPutBucketReplicationReq& req, PutBucketReplicationResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                                    |
| ---- | ----------------------------------------------------------- |
| req  | PutBucketReplicationReq，PutBucketReplication 操作的请求  |
| resp | PutBucketReplicationResp，PutBucketReplication 操作的返回 |

```
// 设置 Replication 的发起者身份标示，role 格式： qcs::cam::uin/[UIN]:uin/[Subaccount]
void SetRole(const std::string& role);

// 增加 ReplicationRule
void AddReplicationRule(const ReplicationRule& rule);

// 设置 ReplicationRules
void SetReplicationRule(const std::vector<ReplicationRule>& rules);
```

其中 ReplicationRule 的定义如下：

```
struct ReplicationRule {
    bool m_is_enable; // 该 Rule 是否生效
    std::string m_id; // 非必选字段，用来标注具体 Rule 的名称
    std::string m_prefix; // 前缀匹配策略，不可重叠，重叠返回错误。前缀匹配根目录为空
    std::string m_dest_bucket; // 标识目标 Bucket，资源标识符：qcs:id/0:cos:[region]:appid/[AppId]:[bucketname]
    std::string m_dest_storage_class; // 非必选字段，存储级别，枚举值：Standard, Standard_IA；为空表示保持原存储桶级别

    ReplicationRule();
    ReplicationRule(const std::string& prefix,
                    const std::string& dest_bucket,
                    const std::string& storage_class = "", 
                    const std::string& id = "", 
                    bool is_enable = true);
};
```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// PutBucketReplicationReq 的构造函数需要传入 bucket_name
qcloud_cos::PutBucketReplicationReq req(bucket_name);
req.SetRole("qcs::cam::uin/***:uin/****");
qcloud_cos::ReplicationRule rule("sevenyou_10m", "qcs:id/0:cos:cn-south:appid/***:sevenyousouthtest", "", "RuleId_01", true);
req.AddReplicationRule(rule)

qcloud_cos::PutBucketReplicationResp resp;
qcloud_cos::CosResult result = cos.PutBucketReplication(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 设置跨区域复制失败，可以调用 CosResult 的成员函数输出错误信息，如requestID 等
} 
```

### Get Bucket Replication

#### 功能说明

Get Bucket Replication 接口请求实现读取存储桶中用户跨区域复制配置信息。

#### 方法原型

```cpp
CosResult GetBucketReplication(const DGetBucketReplicationReq& req, GetBucketReplicationResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                                    |
| ---- | ----------------------------------------------------------- |
| req  | GetBucketReplicationReq，GetBucketReplication 操作的请求  |
| resp | GetBucketReplicationResp，GetBucketReplication 操作的返回 |

```
// 获取 Replication 的发起者身份
std::string GetRole();

// 获取 ReplicationRules, ReplicationRule 定义参见 Put Bucket Replication
std::vector<ReplicationRule> GetRules();
```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// GetBucketReplicationReq 的构造函数需要传入 bucket_name
qcloud_cos::GetBucketReplicationReq req(bucket_name);
qcloud_cos::GetBucketReplicationResp resp;
qcloud_cos::CosResult result = cos.GetBucketReplication(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 获取跨区域复制配置失败，可以调用 CosResult 的成员函数输出错误信息，如 requestI 等
} 
```

### Delete Bucket Replication

#### 功能说明

Delete Bucket Replication 接口请求实现删除存储桶中用户跨区域复制配置。

#### 方法原型

```cpp
CosResult DeleteBucketReplication(const DDeleteBucketReplicationReq& req, DeleteBucketReplicationResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                                     |
| ---- | ------------------------------------------------------------ |
| req  | DeleteBucketReplicationReq，DeleteBucketReplication 操作的请求 |
| resp | DeleteBucketReplicationResp，DeleteBucketReplication 操作的返回 |

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// DeleteBucketReplicationReq 的构造函数需要传入 bucket_name
qcloud_cos::DeleteBucketReplicationReq req(bucket_name);
qcloud_cos::DeleteBucketReplicationResp resp;
qcloud_cos::CosResult result = cos.DeleteBucketReplication(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 删除跨区域复制配置失败，可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

### Put Bucket Lifecycle

#### 功能说明

COS 支持用户以生命周期配置的方式来管理 Bucket 中 Object 的生命周期。生命周期配置包含一个或多个将应用于一组对象规则的规则集 (其中每个规则为 COS 定义一个操作)。
这些操作分为以下两种：

- 转换操作：定义对象转换为另一个存储类的时间。例如，您可以选择在对象创建 30 天后将其转换为 STANDARD_IA (IA，适用于不常访问) 存储类别。
- 过期操作：指定 Object 的过期时间。COS 将会自动为用户删除过期的 Object。
  Put Bucket Lifecycle 用于为 Bucket 创建一个新的生命周期配置。如果该 Bucket 已配置生命周期，使用该接口创建新的配置的同时则会覆盖原有的配置。相关 API 文档参见 [Put Bucket Lifecycle](/document/product/436/8280)。

#### 方法原型

```cpp
CosResult PutBucketLifecycle(const DPutBucketLifecycleReq& req, PutBucketLifecycleResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                                |
| ---- | ------------------------------------------------------- |
| req  | PutBucketLifecycleReq，PutBucketLifecycle 操作的请求  |
| resp | PutBucketLifecycleResp，PutBucketLifecycle 操作的返回 |

```
// 新增 LifecycleRule
void AddRule(const LifecycleRule& rule)

// 设置 LifecycleRule
void SetRule(const std::vector<LifecycleRule>& rules)
```

LifecycleRule 的定义比较复杂，具体如下：

```
struct LifecycleTag {
    std::string key;
    std::string value;
};

class LifecycleFilter {
public:
    LifecycleFilter();

    std::string GetPrefix();
    std::vector<LifecycleTag> GetTags();

    void SetPrefix(const std::string& prefix);
    void SetTags(const std::vector<LifecycleTag>& tags);
    void AddTag(const LifecycleTag& tag);

    bool HasPrefix();
    bool HasTags();

private:
    std::string m_prefix; // 指定规则所适用的前缀。匹配前缀的对象受该规则影响，Prefix 最多只能有一个
    std::vector<LifecycleTag> m_tags; // 标签，Tag 可以有零个或者多个
};

class LifecycleTransition {
public:
    LifecycleTransition();

    uint64_t GetDays();
    std::string GetDate();
    std::string GetStorageClass();

    void SetDays(uint64_t days);
    void SetDate(const std::string& date);
    void SetStorageClass(const std::string& storage_class);

    bool HasDays();
    bool HasDate();
    bool HasStorageClass();
    
private:
    // 不能在同一规则中同时使用 Days 和 Date
    uint64_t m_days; // 指明规则对应的动作在对象最后的修改日期过后多少天操作, 有效值是非负整数
    std::string m_date; // 指明规则对应的动作在何时操作
    std::string m_storage_class; // 指定 Object 转储到的目标存储类型，枚举值： Standard_IA
};

class LifecycleExpiration {
public:
    LifecycleExpiration();
    
    uint64_t GetDays();
    std::string GetDate();
    bool IsExpiredObjDelMarker();
    
    void SetDays(uint64_t days);
    void SetDate(const std::string& date);
    void SetExpiredObjDelMarker(bool marker);

    bool HasDays();
    bool HasDate();
    bool HasExpiredObjDelMarker();
    
private:
    // 不能在同一规则中同时使用 Days 和 Date
    uint64_t m_days; // 指明规则对应的动作在对象最后的修改日期过后多少天操作, 有效值为正整数
    std::string m_date; // 指明规则对应的动作在何时操作
    bool m_expired_obj_del_marker; // 删除过期对象删除标记，枚举值 true，false
};

class LifecycleNonCurrTransition {
public:
    LifecycleNonCurrTransition();

    uint64_t GetDays();
    std::string GetStorageClass();

    void SetDays(uint64_t days);  
    void SetStorageClass(const std::string& storage_class);

    bool HasDays();
    bool HasStorageClass();

private:
    uint64_t m_days; // 指明规则对应的动作在对象最后的修改日期过后多少天操作, 有效值是非负整数
    std::string m_storage_class; // 指定 Object 转储到的目标存储类型，枚举值： Standard_IA
};

class LifecycleNonCurrExpiration {
public:
    LifecycleNonCurrExpiration();
    
    uint64_t GetDays();

    void SetDays(uint64_t days);

    bool HasDays();

private:
    uint64_t m_days; // 指明规则对应的动作在对象最后的修改日期过后多少天操作, 有效值为正整数
};

struct AbortIncompleteMultipartUpload {
    uint64_t m_days_after_init; // 指明分片上传开始后多少天内必须完成上传
};

class LifecycleRule {
public:
    LifecycleRule();

    void SetIsEnable(bool is_enable);
    void SetId(const std::string& id);
    void SetFilter(const LifecycleFilter& filter);
    void AddTransition(const LifecycleTransition& rh);
    void SetExpiration(const LifecycleExpiration& rh);
    void SetNonCurrTransition(const LifecycleNonCurrTransition& rh);
    void SetNonCurrExpiration(const LifecycleNonCurrExpiration& rh);
    void SetAbortIncompleteMultiUpload(const AbortIncompleteMultipartUpload& rh);

    bool IsEnable();
    std::string GetId();
    LifecycleFilter GetFilter();
    std::vector<LifecycleTransition> GetTransitions();
    LifecycleExpiration GetExpiration();
    LifecycleNonCurrTransition GetNonCurrTransition();
    LifecycleNonCurrExpiration GetNonCurrExpiration();
    AbortIncompleteMultipartUpload GetAbortIncompleteMultiUpload();

    bool HasIsEnable();
    bool HasId();
    bool HasFilter();
    bool HasExpiration();
    bool HasNonCurrTransition();
    bool HasNonCurrExpiration();
    bool HasAbortIncomMultiUpload();

private:
    bool m_is_enable; // 规则是否生效
    std::string m_id; // 规则 ID
    LifecycleFilter m_filter; // 过滤器，用来指定规则生效的 Object 范围
    std::vector<LifecycleTransition> m_transitions; // 转换操作
    LifecycleExpiration m_expiration; // 过期操作
    LifecycleNonCurrTransition m_non_curr_transition; // 非当前版本转换操作
    LifecycleNonCurrExpiration m_non_curr_expiration; // 非当前版本过期操作
    AbortIncompleteMultipartUpload m_abort_multi_upload; // 设置允许分片上传保持运行的最长时间
}
```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// PutBucketLifecycleReq的构造函数需要传入bucket_name
qcloud_cos::PutBucketLifecycleReq req(bucket_name);
// 设置规则 1
{
    qcloud_cos::LifecycleRule rule;
    rule.SetIsEnable(true);
    rule.SetId("lifecycle_rule00");
    qcloud_cos::LifecycleFilter filter;
    filter.SetPrefix("sevenyou_e1");
    rule.SetFilter(filter);
    qcloud_cos::LifecycleExpiration expiration;
    expiration.SetDays(1);
    rule.SetExpiration(expiration);
    req.AddRule(rule);
}

// 设置规则 2
{
    qcloud_cos::LifecycleRule rule;
    rule.SetIsEnable(true);
    rule.SetId("lifecycle_rule01");
    qcloud_cos::LifecycleFilter filter;
    filter.SetPrefix("sevenyou_e2");
    rule.SetFilter(filter);
    qcloud_cos::LifecycleExpiration expiration;
    expiration.SetDays(3);
    rule.SetExpiration(expiration);
    req.AddRule(rule);
}

qcloud_cos::PutBucketLifecycleResp resp;
qcloud_cos::CosResult result = cos.PutBucketLifecycle(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 设置生命周期失败，可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

### Get Bucket Lifecycle

#### 功能说明

Get Bucket Lifecycle 用来查询 Bucket 的生命周期配置。如果该 Bucket 没有配置生命周期规则会返回 NoSuchLifecycleConfiguration。相关 API 文档参见 [Get Bucket Lifecycle](/document/product/436/8278)。

#### 方法原型

```cpp
CosResult GetBucketLifecycle(const GetBucketLifecycleReq& req, GetBucketLifecycleResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                                |
| ---- | ------------------------------------------------------- |
| req  | GetBucketLifecycleReq，GetBucketLifecycle 操作的请求  |
| resp | GetBucketLifecycleResp，GetBucketLifecycle 操作的返回 |

```
// 获取 LifecycleRules
std::vector<LifecycleRule> GetRules()
```

其中， LifecycleRule 定义参见 Put Bucket Lifecycle。

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// GetBucketLifecycleReq 的构造函数需要传入 bucket_name
qcloud_cos::GetBucketLifecycleReq req(bucket_name);
qcloud_cos::GetBucketLifecycleResp resp;
qcloud_cos::CosResult result = cos.GetBucketLifecycle(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 获取生命周期配置失败，可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

### Delete Bucket Lifecycle

#### 功能说明

Delete Bucket Lifecycle 用来删除 Bucket 的生命周期配置。如果该 Bucket 没有配置生命周期规则会返回 NoSuchLifecycleConfiguration。相关 API 文档参见 [Delete Bucket Lifecycle](/document/product/436/8284)。

#### 方法原型

```cpp
CosResult DeleteBucketLifecycle(const DeleteBucketLifecycleReq& req, DeleteBucketLifecycleResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                                     |
| ---- | ------------------------------------------------------------ |
| req  | DeleteBucketLifecycleReq，DeleteBucketLifecycle 操作的请求 |
| resp | DeleteBucketLifecycleResp，DeleteBucketLifecycle 操作的返回 |

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// DeleteBucketLifecycleReq 的构造函数需要传入 bucket_name
qcloud_cos::DeleteBucketLifecycleReq req(bucket_name);
qcloud_cos::DeleteBucketLifecycleResp resp;
qcloud_cos::CosResult result = cos.DeleteBucketLifecycle(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 删除生命周期配置失败，可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

### Put Bucket CORS

#### 功能说明

CPut Bucket CORS 接口用来请求设置 Bucket 的跨域资源共享权限，您可以通过传入 XML 格式的配置文件来实现配置，文件大小限制为64KB。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。相关 API 文档参见 [Put Bucket CORS](/document/product/436/8279)。

#### 方法原型

```cpp
CosResult PutBucketCORS(const DPutBucketCORSReq& req, PutBucketCORSResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                      |
| ---- | --------------------------------------------- |
| req  | PutBucketCORSReq，PutBucketCORS 操作的请求  |
| resp | PutBucketCORSResp，PutBucketCORS 操作的返回 |

```
// 新增 CORSRule
void AddRule(const CORSRule& rule);

// 设置 CORSRule
void SetRules(const std::vector<CORSRule>& rules)


```

CORSRule 定义如下：

```
struct CORSRule {
    std::string m_id; // 配置规则的 ID，可选填
    std::string m_max_age_secs; // 设置 OPTIONS 请求得到结果的有效期
    std::vector<std::string> m_allowed_headers; // 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 *
    std::vector<std::string> m_allowed_methods; // 允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE
    std::vector<std::string> m_allowed_origins; // 允许的访问来源，支持通配符 * ，格式为：协议://域名[:端口]如：http://www.qq.com
    std::vector<std::string> m_expose_headers;  // 设置浏览器可以接收到的来自服务器端的自定义头部信息
};


```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// PutBucketCORSReq 的构造函数需要传入 bucket_name
qcloud_cos::PutBucketCORSReq req(bucket_name);
qcloud_cos::CORSRule rule;
rule.m_id = "123";
rule.m_allowed_headers.push_back("x-cos-meta-test");
rule.m_allowed_origins.push_back("http://www.qq.com");
rule.m_allowed_origins.push_back("http://cloud.tentent.com");
rule.m_allowed_methods.push_back("PUT");
rule.m_allowed_methods.push_back("GET");
rule.m_max_age_secs = "600";
rule.m_expose_headers.push_back("x-cos-expose");
req.AddRule(rule);

qcloud_cos::PutBucketCORSResp resp;
qcloud_cos::CosResult result = cos.PutBucketCORS(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 设置生命周期失败，可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

### Get Bucket CORS

#### 功能说明

Get Bucket CORS 接口实现 Bucket 持有者在 Bucket 上进行跨域资源共享的信息配置。CORS 即跨域资源共享，全称 Cross-Origin Resource Sharing，是一个 W3C 标准。默认情况下，Bucket 的持有者直接有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。相关 API 文档参见 [Get Bucket CORS](/document/product/436/8274)。

#### 方法原型

```cpp
CosResult GetBucketCORS(const DGetBucketCORSReq& req, GetBucketCORSResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                      |
| ---- | --------------------------------------------- |
| req  | GetBucketCORSReq，GetBucketCORS 操作的请求  |
| resp | GetBucketCORSResp，GetBucketCORS 操作的返回 |

```
// 获取 CORSRules, CORSRule 定义参见 Put Bucket CORS
std::vector<CORSRule> GetCORSRules();

```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// GetBucketCORSReq 的构造函数需要传入 bucket_name
qcloud_cos::GetBucketCORSReq req(bucket_name);
qcloud_cos::GetBucketCORSResp resp;
qcloud_cos::CosResult result = cos.GetBucketCORS(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 获取生命周期配置失败，可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

### Delete Bucket CORS

#### 功能说明

Delete Bucket CORS 用来删除 Bucket 的生命周期配置。如果该 Bucket 没有配置生命周期规则会返回 NoSuchCORSConfiguration。相关 API 文档参见 [Delete Bucket CORS](/document/product/436/8283)。

#### 方法原型

```cpp
CosResult DeleteBucketCORS(const DDeleteBucketCORSReq& req, DeleteBucketCORSResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                            |
| ---- | --------------------------------------------------- |
| req  | DeleteBucketCORSReq，DeleteBucketCORS 操作的请求  |
| resp | DeleteBucketCORSResp，DeleteBucketCORS 操作的返回 |

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// DeleteBucketCORSReq 的构造函数需要传入 bucket_name
qcloud_cos::DeleteBucketCORSReq req(bucket_name);
qcloud_cos::DeleteBucketCORSResp resp;
qcloud_cos::CosResult result = cos.DeleteBucketCORS(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 删除生命周期配置失败，可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

### Put Bucket ACL

#### 功能说明

Put Bucket ACL 接口用来写入 Bucket 的 ACL（Access Control List）表，您可以通过 Header："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-write"，"x-cos-grant-full-control" 传入 ACL 信息，或者通过 Body 以 XML 格式传入 ACL 信息。相关 API 文档参见 [Put Bucket ACL](/document/product/436/7737)。

#### 方法原型

```cpp
CosResult PutBucketACL(const DPutBucketACLReq& req, PutBucketACLResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | PutBucketACLReq，PutBucketACL 操作的请求  |
| resp | PutBucketACLResp，PutBucketACL 操作的返回 |

```
// 定义 Bucket 的 ACL 属性,有效值：private,public-read-write,public-read
// 默认值：private
void SetXCosAcl(const std::string& str);

// 赋予被授权者读的权限.格式：x-cos-grant-read: id=" ",id=" ".
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantRead(const std::string& str);

// 赋予被授权者写的权限,格式：x-cos-grant-write: id=" ",id=" "./
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantWrite(const std::string& str);

// 赋予被授权者读写权限.格式：x-cos-grant-full-control: id=" ",id=" ".
// 当需要给子账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// 当需要给根账户授权时,id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantFullControl(const std::string& str);

// Bucket 持有者 ID
void SetOwner(const Owner& owner);

// 设置被授权者信息与权限信息
void SetAccessControlList(const std::vector<Grant>& grants);

// 添加单个 Bucket 的授权信息
void AddAccessControlList(const Grant& grant);
        

```

>!SetXCosAcl/SetXCosGrantRead/SetXCosGrantWrite/SetXCosGrantFullControl 这类接口与 SetAccessControlList/AddAccessControlList 不可同时使用。因为前者实际是通过设置 HTTP Header 实现，而后者是在 Body 中添加了 XML 格式的内容，二者只能二选一。 SDK 内部优先使用第一类。

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
    std::string m_perm; // 指明授予被授权者的权限信息，枚举值：READ，WRITE，FULL_CONTROL
};


```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// PutBucketACLReq 的构造函数需要传入 bucket_name
qcloud_cos::PutBucketACLReq req(bucket_name);
qcloud_cos::ACLRule rule;
rule.m_id = "123";
rule.m_allowed_headers.push_back("x-cos-meta-test");
rule.m_allowed_origins.push_back("http://www.qq.com");
rule.m_allowed_origins.push_back("http://cloud.tentent.com");
rule.m_allowed_methods.push_back("PUT");
rule.m_allowed_methods.push_back("GET");
rule.m_max_age_secs = "600";
rule.m_expose_headers.push_back("x-cos-expose");
req.AddRule(rule);

qcloud_cos::PutBucketACLResp resp;
qcloud_cos::CosResult result = cos.PutBucketACL(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 设置ACL，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

### Get Bucket ACL

#### 功能说明

Get Bucket ACL 接口用来获取 Bucket 的 ACL， 即存储桶（Bucket）的访问权限控制列表。 此 API 接口只有 Bucket 的持有者有权限操作。相关 API 文档参见 [Get Bucket ACL](/document/product/436/7733)。

#### 方法原型

```cpp
CosResult GetBucketACL(const DGetBucketACLReq& req, GetBucketACLResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | GetBucketACLReq，GetBucketACL 操作的请求  |
| resp | GetBucketACLResp，GetBucketACL 操作的返回 |

```
std::string GetOwnerID();
std::string GetOwnerDisplayName();
std::vector<Grant> GetAccessControlList();

```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// GetBucketACLReq 的构造函数需要传入 bucket_name
qcloud_cos::GetBucketACLReq req(bucket_name);
qcloud_cos::GetBucketACLResp resp;
qcloud_cos::CosResult result = cos.GetBucketACL(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 获取 ACL 失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

## Object 操作

object_name 即为对象键（Key），是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg。

关于“对象键”的具体信息，参见 [对象概述](https://cloud.tencent.com/document/product/436/13324)。

### Get Object

#### 功能说明

Get Object 请求可以将一个文件（Object）下载至本地或指定流中。该操作需要对目标 Object 具有读权限或目标 Object 对所有人都开放了读权限（公有读）。

#### 方法原型

```cpp
// 将 Object 下载到本地文件中
CosResult GetObject(const GetObjectByFileReq& req, GetObjectByFileResp* resp);

// 将 Object 下载到流中
CosResult GetObject(const GetObjectByStreamReq& req, GetObjectByStreamResp* resp);

// 将 Object 下载到本地文件中（多线程）
CosResult GetObject(const MultiGetObjectReq& req, MultiGetObjectResp* resp);
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

```C++
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

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
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
        // 下载失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
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

### Head Object

#### 功能说明

Head Object 请求可以取回对应 Object 的元数据，Head 的权限与 Get 的权限一致。

#### 方法原型

```cpp
CosResult HeadObject(const HeadObjectReq& req, HeadObjectResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                |
| ---- | --------------------------------------- |
| req  | HeadObjectReq，HeadObject 操作的请求  |
| resp | HeadObjectResp，HeadObject 操作的返回 |

HeadObjectResp 除了读取公共头部的成员函数外，还提供以下成员函数：

```C++
std::string GetXCosObjectType();

std::string GetXCosStorageClass();

// 获取自定义的 meta, 参数可以为 x-cos-meta-* 中的 *
std::string GetXCosMeta(const std::string& key);

// 以 map 形式返回所有自定义的 meta, map 的 key 均不包含"x-cos-meta-"前缀
std::map<std::string, std::string> GetXCosMetas();

// 获取Server端加密使用的算法
std::string GetXCosServerSideEncryption(); 
```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
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

### Put Object

#### 功能说明

Put Object 请求可以将一个文件（Object）上传至指定 Bucket。

- 上传过程中默认会对文件进行 MD5 校验（关闭上传 MD5 校验参考示例代码）。
- 当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请在上传时不要设置，默认继承 Bucket 权限。

#### 方法原型

```cpp
/// 通过 Stream 进行上传
CosResult PutObject(const PutObjectByStreamReq& req, PutObjectByStreamResp* resp);

/// 上传本地文件
CosResult PutObject(const PutObjectByFileReq& req, PutObjectByFileResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                                     |
| ---- | ------------------------------------------------------------ |
| req  | PutObjectByStreamReq/PutObjectByFileReq，PutObject 操作的请求 |
| resp | PutObjectByStreamResp/PutObjectByFileResp，PutObject 操作的返回 |

参数 Req 包括如下成员函数：

```C++
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

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
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
    // 关闭MD5校验，开启使用req.TurnOnComputeConentMd5()，默认情况开启
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

### Delete Object

#### 功能说明

Delete Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）删除。该操作需要请求者对 Bucket 有 WRITE 权限。相关 API 文档参见 [Delete Object](/document/product/436/7743)。

#### 方法原型

```cpp
CosResult DeleteObject(const DeleteObjectReq& req, DeleteObjectResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                   |
| ---- | ------------------------------------------ |
| req  | DeleteObjectReq，DeleteObject 操作的请求 |
| resp | DeletObjectResp，DeletObject 操作的返回  |

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
std::string object_name = "test_object";

qcloud_cos::DeleteObjectReq req(bucket_name, object_name);
qcloud_cos::DeleteObjectResp resp;
qcloud_cos::CosResult result = cos.DeleteObject(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 删除 Object 失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

## 分块上传操作

### Initiate Multipart Upload

#### 功能说明

Initiate Multipart Upload 请求实现初始化分片上传，成功执行此请求以后会返回 Upload ID 用于后续的 Upload Part 请求。

#### 方法原型

```cpp
CosResult InitMultiUpload(const InitMultiUploadReq& req, InitMultiUploadResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                          |
| ---- | ------------------------------------------------- |
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

/// 设置Server端加密使用的算法, 目前支持AES256
void SetXCosServerSideEncryption(const std::string& str);

```

当成功执行此请求后，返回的 response 中会包含 bucket、key、uploadId， 分别表示分片上传的目标 Bucket、Object 名称以及后续分片上传所需的编号。

InitMultiUploadResp 的成员函数如下:

```C++
std::string GetBucket();
std::string GetKey();
std::string GetUploadId();

// Server端加密使用的算法
std::string GetXCosServerSideEncryption();
```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);
std::string bucket_name = "cpp_sdk_v5-123456789";
std::string object_name = "object_name";

qcloud_cos::InitMultiUploadReq req(bucket_name, object_name);
qcloud_cos::InitMultiUploadResp resp;
qcloud_cos::CosResult result = cos.InitMultiUpload(req, &resp);

std::string upload_id = "";
if (result.IsSucc()) {
    upload_id = resp.GetUploadId();
}
```

### Upload Part

#### 功能说明

Upload Part 请求实现在初始化以后的分块上传，支持的块的数量为1到10000，块的大小为1MB到5GB。在每次请求 Upload Part 时，需要携带 partNumber 和 uploadID，partNumber 为块的编号，支持乱序上传。

>!上传过程中默认会对文件进行MD5校验（关闭上传MD5校验参考示例代码）。

#### 方法原型

```cpp
CosResult UploadPartData(const UploadPartDataReq& request, UploadPartDataResp* response);
```

#### 参数说明

| 参数 | 参数描述                                        |
| ---- | ----------------------------------------------- |
| req  | UploadPartDataReq，UploadPartData 操作的请求  |
| resp | UploadPartDataResp，UploadPartData 操作的返回 |

UploadPartDataReq 在构造时，需要指明请求的 APPID、Bucket、Object、初始化成功后获取的 UploadId，以及上传的数据流（调用完成后，流由调用方自己负责关闭）。

```
UploadPartDataReq(const std::string& bucket_name,
                    const std::string& object_name, const std::string& upload_id,
                    std::istream& in_stream);

```

此外，请求还需要设置分片编号, 这个分片在完成分片上传时也会用到。

```
void SetPartNumber(uint64_t part_number);

```

UploadPartDataResp 的成员函数如下：

```
/// Server端加密使用的算法
std::string GetXCosServerSideEncryption();

```

#### 示例

```cpp
// 上传第一个分片
{
    std::fstream is("demo_5M.part1");
    qcloud_cos::UploadPartDataReq req(bucket_name, object_name, upload_id, is);
    req.SetPartNumber(1);
    // 关闭MD5校验，开启使用req.TurnOnComputeConentMd5()，默认情况开启
    req.TurnOffComputeConentMd5();
    qcloud_cos::UploadPartDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartData(req, &resp);

    // 上传成功需要记录分片编号以及返回的 ETag
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

    // 上传成功需要记录分片编号以及返回的 ETag 
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_numbers.push_back(2);
    }
    is.close();
}
```

### Complete Multipart Upload

#### 功能说明

Complete Multipart Upload 用来实现完成整个分块上传。当您已经使用 Upload Parts 上传所有块以后，您可以用该 API 完成上传。在使用该 API 时，您必须在 Body 中给出每一个块的 PartNumber 和 ETag，用来校验块的准确性。

#### 方法原型

```cpp
CosResult CompleteMultiUpload(const CompleteMultiUploadReq& request, CompleteMultiUploadResp* response);
```

#### 参数说明

| 参数 | 参数描述                                                  |
| ---- | --------------------------------------------------------- |
| req  | CompleteMultiUploadReq，CompleteMultiUpload 操作的请求  |
| resp | CompleteMultiUploadResp，CompleteMultiUpload 操作的返回 |

CompleteMultiUploadReq 在构造时，需要指明请求的APPID、Bucket、Object、初始化成功后获取的 UploadId。

```
CompleteMultiUploadReq(const std::string& bucket_name,
                       const std::string& object_name, const std::string& upload_id)

```

此外，request 还需要设置所有上传的分片编号和 ETag。

```
// 调用下列方法时，应注意编号和 ETag 的顺序必须一一对应
void SetPartNumbers(const std::vector<uint64_t>& part_numbers);
void SetEtags(const std::vector<std::string>& etags) ;

// 添加 part_number 和 ETag 对
void AddPartEtagPair(uint64_t part_number, const std::string& etag);

/// 设置Server端加密使用的算法, 目前支持AES256
void SetXCosServerSideEncryption(const std::string& str);
```

CompleteMultiUploadResp 的返回内容中包括 Location、Bucket、Key、ETag，分别表示创建的 Object 的外网访问域名、分块上传的目标 Bucket、Object 的名称、合并后文件的 MD5 算法校验值。可以调用下列成员函数对 response 中的内容进行访问。

```
std::string GetLocation();
std::string GetKey();
std::string GetBucket();
std::string GetEtag();

/// Server端加密使用的算法
std::string GetXCosServerSideEncryption();

```

#### 示例

```cpp
qcloud_cos::CompleteMultiUploadReq req(bucket_name, object_name, upload_id);
qcloud_cos::CompleteMultiUploadResp resp;
req.SetEtags(etags);
req.SetPartNumbers(part_numbers);

qcloud_cos::CosResult result = cos.CompleteMultiUpload(req, &resp);
```

### Multipart Upload

#### 功能说明

Multipart Upload 封装了初始化分块上传、分块上传、完成分块上传三步，只需要在请求中指明上传的文件。

#### 方法原型

```cpp
CosResult MultiUploadObject(const MultiUploadObjectReq& request, MultiUploadObjectResp* response);
```

#### 参数说明

| 参数 | 参数描述                                              |
| ---- | ----------------------------------------------------- |
| req  | MultiUploadObjectReq，MultiUploadObject 操作的请求  |
| resp | MultiUploadObjectResp，MultiUploadObject 操作的返回 |

MultiUploadObjectReq 需要在构造的时候指明 Bucket、Object 以及待上传文件的本地路径， 如果不指明本地路径，则默认是当前工作路径下与 Object 同名的文件。

```
MultiUploadObjectReq(const std::string& bucket_name,
                     const std::string& object_name, const std::string& local_file_path = "");

/// 设置Server端加密使用的算法, 目前支持AES256
void SetXCosServerSideEncryption(const std::string& str);

```

- 分块上传成功的情况下，该 Response 的返回内容与 CompleteMultiUploadResp 一致。
- 分块上传失败的情况下，该 Response 根据不同的失败情况，返回内容与 InitMultiUploadResp、UploadPartDataResp、CompleteMultiUploadResp 一致。可调用`GetRespTag()`来获取具体失败在哪一步。

```
// 返回 Init、Upload、Complete
std::string GetRespTag();

/// Server端加密使用的算法
std::string GetXCosServerSideEncryption();

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

### Abort Multipart Upload

#### 功能说明

Abort Multipart Upload 用来实现舍弃一个分块上传并删除已上传的块。当您调用 Abort Multipart Upload 时，如果有正在使用这个 Upload Parts 上传块的请求，则 Upload Parts 会返回失败。

#### 方法原型

```cpp
CosResult AbortMultiUpload(const AbortMultiUploadReq& request, AbortMultiUploadResp* response);
```

#### 参数说明

| 参数 | 参数描述                                            |
| ---- | --------------------------------------------------- |
| req  | AbortMultiUploadReq，AbortMultiUpload 操作的请求  |
| resp | AbortMultiUploadResp，AbortMultiUpload 操作的返回 |

AbortMultiUploadReq 需要在构造的时候指明 Bucket、Object 以及 Upload_id。

```C++
AbortMultiUploadReq(const std::string& bucket_name,
                    const std::string& object_name, const std::string& upload_id);
```

无特殊方法，可调用 BaseResp 的成员函数来获取公共头部内容。

#### 示例

```cpp
qcloud_cos::AbortMultiUploadReq req(bucket_name, object_name, upload_id);
qcloud_cos::AbortMultiUploadResp resp;
qcloud_cos::CosResult result = cos.AbortMultiUpload(req, &resp);
```

### List Parts

#### 功能说明

List Parts 用来查询特定分块上传中的已上传的块，即罗列出指定 UploadId 所属的所有已上传成功的分块。相关 API 文档参见 [List Parts](/document/product/436/7747)。

#### 方法原型

```cpp
CosResult ListParts(const ListPartsReq& req, ListPartsResp* resp);
```

#### 参数说明

| 参数 | 参数描述                              |
| ---- | ------------------------------------- |
| req  | ListPartsReq，ListParts 操作的请求  |
| resp | ListPartsResp，ListParts 操作的返回 |

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

```
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

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
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
    // 删除 Object 失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

### Post Object Restore

#### 功能说明

对一个通过 COS 归档为 archive 类型的对象进行恢复。相关 API 文档参见 [Post Object Restore](https://cloud.tencent.com/document/product/436/12633)。

#### 方法原型

```cpp
CosResult ObjectOp::PostObjectRestore(const PostObjectRestoreReq& req, PostObjectRestoreResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | PostObjectRestoreReq，PostObjectRestore 操作的请求  |
| resp | PostObjectRestoreResp， PostObjectRestore 操作的返回 |

```
// 设置临时副本的过期时间
void SetExiryDays(uint64_t days);

// 枚举值： Expedited ，Standard ，Bulk；默认值：Standard
void SetTier(const std::string& tier);
```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
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

### Put Object ACL

#### 功能说明

Put Object ACL 接口用来写入 Object 的 ACL 表，您可以通过 Header："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-full-control" 传入 ACL 信息，或者通过 Body 以 XML 格式传入 ACL 信息。相关 API 文档参见 [Put Object ACL](/document/product/436/7748)。

>!当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请不要设置，默认继承 Bucket 权限。

#### 方法原型

```cpp
CosResult PutObjectACL(const PutObjectACLReq& req, PutObjectACLResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | PutObjectACLReq，PutObjectACL 操作的请求  |
| resp | PutObjectACLResp，PutObjectACL 操作的返回 |

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

>!SetXCosAcl/SetXCosGrantRead/SetXCosGrantWrite/SetXCosGrantFullControl 这类接口与  SetAccessControlList/AddAccessControlList 不可同时使用。因为前者实际是通过设置 HTTP Header 实现，而后者是在Body 中添加了 XML 格式的内容，二者只能二选一。SDK 内部优先使用第一类。

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

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
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
        // 设置 ACL，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
    } 
}   
```

### Get Object ACL

#### 功能说明

Get Object ACL 接口用来获取 Object 的 ACL， 即对象（文件，Object）的访问权限控制列表。 此 API 接口只有 Object 的持有者有权限操作。相关 API 文档参见 [Get Object ACL](/document/product/436/7744)。

#### 方法原型

```cpp
CosResult GetObjectACL(const DGetObjectACLReq& req, GetObjectACLResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | GetObjectACLReq，GetObjectACL 操作的请求  |
| resp | GetObjectACLResp，GetObjectACL 操作的返回 |

```
std::string GetOwnerID();
std::string GetOwnerDisplayName();
std::vector<Grant> GetAccessControlList();

```

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string Object_name = "cpp_sdk_v5-123456789";

// GetObjectACLReq 的构造函数需要传入 Object_name
qcloud_cos::GetObjectACLReq req(Object_name);
qcloud_cos::GetObjectACLResp resp;
qcloud_cos::CosResult result = cos.GetObjectACL(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 获取 ACL 失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
} 
```

### Put Object Copy

#### 功能说明

Put Object Copy 请求实现将一个文件从源路径复制到目标路径。在拷贝的过程中，文件元属性和 ACL 可以被修改。用户可以通过该接口实现文件移动，文件重命名，修改文件属性和创建副本。建议文件大小1MB到5GB，超过5GB的文件请使用分块上传 Upload - Copy。相关 API 文档参见 [Put Object Copy](/document/product/436/10881)。

#### 方法原型

```cpp
CosResult PutObjectCopy(const PutObjectCopyReq& req, PutObjectCopyResp* resp);
```

#### 参数说明

| 参数 | 参数描述                                      |
| ---- | --------------------------------------------- |
| req  | PutObjectCopyReq，PutObjectCopy 操作的请求  |
| resp | PutObjectCopyResp，PutObjectCopy 操作的返回 |

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

#### 示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
std::string object_name = "sevenyou";

qcloud_cos::PutObjectCopyReq req(bucket_name, object_name);                                                                                                                       
req.SetXCosCopySource("sevenyousouthtest-12345656.cn-south.myqcloud.com/sevenyou_source_obj");
qcloud_cos::PutObjectCopyResp resp;
qcloud_cos::CosResult result = cos.PutObjectCopy(req, &resp);
```
