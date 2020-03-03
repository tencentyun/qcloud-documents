## 简介
本文档提供关于跨域访问、生命周期、版本控制、跨地域复制相关的 API 概览以及 SDK 示例代码。

**跨域访问**

| API                                                          | 操作名       | 操作描述                       |
| ------------------------------------------------------------ | ------------ | ------------------------------ |
| [PUT Bucket cors](https://cloud.tencent.com/document/product/436/8279) | 设置跨域配置	 |  设置存储桶的跨域访问权限     |
| [GET Bucket cors](https://cloud.tencent.com/document/product/436/8274) | 查询跨域配置	 |   查询存储桶的跨域访问配置信息 |
| [DELETE Bucket cors](https://cloud.tencent.com/document/product/436/8283) | 删除跨域配置	|删除存储桶的跨域访问配置信息 |

**生命周期**

| API                                                          | 操作名       | 操作描述                         |
| ------------------------------------------------------------ | ------------ | -------------------------------- |
| [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/8280) | 	设置生命周期	|设置存储桶生命周期管理的配置 |
| [GET Bucket lifecycle](https://cloud.tencent.com/document/product/436/8278) | 查询生命周期	|  查询存储桶生命周期管理的配置   |
| [DELETE Bucket lifecycle](https://cloud.tencent.com/document/product/436/8284) | 删除生命周期	|  删除存储桶生命周期管理的配置   |

**版本控制**

| API | 操作名 | 操作描述 |
| ------------------- | ------------ | ------------------ |
| [PUT Bucket versioning](https://cloud.tencent.com/document/product/436/19889) | 设置版本控制   | 设置存储桶的版本控制功能 |
| [GET Bucket versioning](https://cloud.tencent.com/document/product/436/19888) | 查询版本控制 | 查询存储桶的版本控制信息 |

**跨地域复制**

| API | 操作名 | 操作描述 |
| ------------------- | ------------ | ------------------ |
| [PUT Bucket replication](https://cloud.tencent.com/document/product/436/19223) | 设置跨地域复制   | 设置存储桶的跨地域复制规则 |
| [GET Bucket replication](https://cloud.tencent.com/document/product/436/19222) | 查询跨地域复制 | 查询存储桶的跨地域复制规则 |
| [DELETE Bucket replication](https://cloud.tencent.com/document/product/436/19221) | 删除跨地域复制 | 删除存储桶的跨地域复制规则 |

## 跨域访问
### 设置跨域配置

#### 功能说明

设置存储桶的跨域访问权限。

#### 方法原型
```cpp
CosResult PutBucketCORS(const PutBucketCORSReq& req, PutBucketCORSResp* resp)
```

#### 请求示例
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

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
    // 可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

#### 参数说明

| 参数 | 参数描述                                      |
| ---- | --------------------------------------------- |
| req  | PutBucketCORSReq，PutBucketCORS 操作的请求  |
| resp | PutBucketCORSResp，PutBucketCORS 操作的返回 |

PutBucketCORSReq 提供以下成员函数：
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

### 查询跨域配置

#### 功能说明

查询存储桶的跨域访问配置信息。

#### 方法原型
```cpp
CosResult GetBucketCORS(const GetBucketCORSReq& req, GetBucketCORSResp* resp)
```

#### 请求示例
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

// GetBucketCORSReq 的构造函数需要传入 bucket_name
qcloud_cos::GetBucketCORSReq req(bucket_name);
qcloud_cos::GetBucketCORSResp resp;
qcloud_cos::CosResult result = cos.GetBucketCORS(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

#### 参数说明

| 参数 | 参数描述                                      |
| ---- | --------------------------------------------- |
| req  | GetBucketCORSReq，GetBucketCORS 操作的请求  |
| resp | GetBucketCORSResp，GetBucketCORS 操作的返回 |

GetBucketCORSResp 提供以下成员函数：
```
// 获取 CORSRules, CORSRule 定义参见 Put Bucket CORS
std::vector<CORSRule> GetCORSRules();
```

### 删除跨域配置

#### 功能说明

删除指定存储桶的跨域访问配置。

#### 方法原型

```cpp
CosResult DeleteBucketCORS(const DeleteBucketCORSReq& req, DeleteBucketCORSResp* resp)
```

#### 请求示例
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

// DeleteBucketCORSReq 的构造函数需要传入 bucket_name
qcloud_cos::DeleteBucketCORSReq req(bucket_name);
qcloud_cos::DeleteBucketCORSResp resp;
qcloud_cos::CosResult result = cos.DeleteBucketCORS(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

#### 参数说明

| 参数 | 参数描述                                            |
| ---- | --------------------------------------------------- |
| req  | DeleteBucketCORSReq，DeleteBucketCORS 操作的请求  |
| resp | DeleteBucketCORSResp，DeleteBucketCORS 操作的返回 |

## 生命周期
### 设置生命周期

#### 功能说明

设置指定存储桶的生命周期配置信息。

#### 方法原型

```cpp
CosResult PutBucketLifecycle(const PutBucketLifecycleReq& req, PutBucketLifecycleResp* resp)
```

#### 请求示例
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

// PutBucketLifecycleReq 的构造函数需要传入 bucket_name
qcloud_cos::PutBucketLifecycleReq req(bucket_name);
// 设置规则1
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

// 设置规则2
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

#### 参数说明

| 参数 | 参数描述                                                |
| ---- | ------------------------------------------------------- |
| req  | PutBucketLifecycleReq，PutBucketLifecycle 操作的请求  |
| resp | PutBucketLifecycleResp，PutBucketLifecycle 操作的返回 |

PutBucketLifecycleReq 提供以下成员函数：
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

### 查询生命周期

#### 功能说明

查询指定存储桶的生命周期配置信息。

#### 方法原型

```cpp
CosResult GetBucketLifecycle(const GetBucketLifecycleReq& req, GetBucketLifecycleResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

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

#### 参数说明

| 参数 | 参数描述                                                |
| ---- | ------------------------------------------------------- |
| req  | GetBucketLifecycleReq，GetBucketLifecycle 操作的请求  |
| resp | GetBucketLifecycleResp，GetBucketLifecycle 操作的返回 |

GetBucketLifecycleResp 提供以下成员函数：
```
// 获取 LifecycleRules
std::vector<LifecycleRule> GetRules()
```

其中， LifecycleRule 定义参见 [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/8280)。


### 删除生命周期

#### 功能说明

删除指定存储桶的生命周期配置信息。

#### 方法原型

```cpp
CosResult DeleteBucketLifecycle(const DeleteBucketLifecycleReq& req, DeleteBucketLifecycleResp* resp)
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

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


#### 参数说明

| 参数 | 参数描述                                                     |
| ---- | ------------------------------------------------------------ |
| req  | DeleteBucketLifecycleReq，DeleteBucketLifecycle 操作的请求 |
| resp | DeleteBucketLifecycleResp，DeleteBucketLifecycle 操作的返回 |


## 版本控制
### 设置版本控制

#### 功能说明

设置指定存储桶的版本控制功能。

#### 方法原型
```cpp
CosResult PutBucketVersioning(const PutBucketVersioningReq& request, PutBucketVersioningResp* response)
```

#### 请求示例
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

// PutBucketVersioningReq 的构造函数需要传入 bucket_name
qcloud_cos::PutBucketVersioningReq req(bucket_name);
req.SetStatus(true);
qcloud_cos::PutBucketVersioningResp resp;
qcloud_cos::CosResult result = cos.PutBucketVersioning(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

#### 参数说明
| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | PutBucketVersioningReq，PutBucketVersioning 操作的请求  |
| resp | PutBucketVersioningResp，PutBucketVersioning 操作的返回 |

PutBucketVersioningReq 提供以下成员函数：

```cpp
// 版本是否开启，一经开启不能关闭，只能suspend
void SetStatus(bool is_enable);
```

### 查询版本控制

#### 功能说明

查询指定存储桶的版本控制信息。

#### 方法原型
```cpp
CosResult GetBucketVersioning(const GetBucketVersioningReq& request, GetBucketVersioningResp* response) 
```

#### 请求示例
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

qcloud_cos::GetBucketVersioningReq req(bucket_name);
qcloud_cos::GetBucketVersioningResp resp;
qcloud_cos::CosResult result = cos.GetBucketVersioning(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

#### 参数说明
| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | GetBucketVersioningReq，GetBucketVersioning 操作的请求  |
| resp | GetBucketVersioningResp，GetBucketVersioning 操作的返回 |

GetBucketVersioningResp 提供以下成员函数：

```cpp
// 返回bucket的版本状态,0: 从未开启版本管理, 1: 版本管理生效中, 2: 暂停
int GetStatus() const
```

## 跨地域复制
### 设置跨地域复制

#### 功能说明

设置指定存储桶的跨地域复制规则。

#### 方法原型
```go
func (s *BucketService) PutBucketReplication(ctx context.Context, opt *PutBucketReplicationOptions) (*Response, error)
```

#### 请求示例
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

qcloud_cos::PutBucketReplicationReq req(bucket_name);
req.SetRole("qcs::cam::uin/100000000001:uin/100000000001");
qcloud_cos::ReplicationRule rule("", "qcs::cos:ap-guangzhou::examplebucket-1250000000", "", "", true);

req.AddReplicationRule(rule);
qcloud_cos::PutBucketReplicationResp resp;
qcloud_cos::CosResult result = cos.PutBucketReplication(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
}
```

#### 参数说明
| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | PutBucketReplicationReq，PutBucketReplication 操作的请求  |
| resp | PutBucketReplicationResp，PutBucketReplication 操作的返回 |

PutBucketReplicationReq 提供以下成员函数：

```
// 发起者身份标示：qcs::cam::uin/<OwnerUin>:uin/<SubUin>
void SetRole(const std::string& role)；
// 添加具体配置信息，最多支持1000个，所有策略只能指向一个目标存储桶
void AddReplicationRule(const ReplicationRule& rule)；

// ReplicationRule 结构如下：
struct ReplicationRule {
	bool m_is_enable;
	std::string m_id; // 非必须
	std::string m_prefix;
	std::string m_dest_bucket;
	std::string m_dest_storage_class; // 非必须 
}
```

### 查询跨地域复制

#### 功能说明

查询指定存储桶的跨地域复制规则。

#### 方法原型
```cpp
CosResult GetBucketReplication(const GetBucketReplicationReq& request, GetBucketReplicationResp* response)
```

#### 请求示例
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

qcloud_cos::GetBucketReplicationReq req(bucket_name);
qcloud_cos::GetBucketReplicationResp resp;
qcloud_cos::CosResult result = cos.GetBucketReplication(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

#### 参数说明
| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | GetBucketReplicationReq，GetBucketReplication 操作的请求  |
| resp | GetBucketReplicationResp，GetBucketReplication 操作的返回 |

GetBucketReplicationResp 提供以下成员函数：

```cpp
// 获取发起者身份标示：qcs::cam::uin/<OwnerUin>:uin/<SubUin>
std::string GetRole();
// 获取具体配置信息，最多支持 1000 个，所有策略只能指向一个目标存储桶
std::vector<ReplicationRule> GetRules();
// ReplicationRule 结构如PutBucketReplication中描述
```


### 删除跨地域复制

#### 功能说明

删除指定存储桶的跨地域复制规则。

#### 方法原型
```cpp
CosResult DeleteBucketReplication(const DeleteBucketReplicationReq& request, DeleteBucketReplicationResp* response)
```

#### 请求示例
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";

qcloud_cos::DeleteBucketReplicationReq req(bucket_name);
qcloud_cos::DeleteBucketReplicationResp resp;
qcloud_cos::CosResult result = cos.DeleteBucketReplication(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 可以调用 CosResult 的成员函数输出错误信息，如 requestID 等
} 
```

#### 参数说明
| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | DeleteBucketReplicationReq，DeleteBucketReplication 操作的请求  |
| resp | DeleteBucketReplicationResp，DeleteBucketReplication 操作的返回 |
