## Generating Signature
### Feature of Sign
Generate signature
### Method prototype 1
```
static std::string Sign(const std::string& secret_id,
                        const std::string& secret_key,
                        const std::string& http_method,
                        const std::string& in_uri,
                        const std::map<std::string, std::string>& headers,
                        const std::map<std::string, std::string>& params);
```
#### Parameters 
| Parameter Name | Parameter Description | Type | 
|---------|---------|---------|
| secret_id  | The project identity ID owned by a developer, which is used for identity authentication  | String   |  
| secret_key | The project identity key owned by a developer  | String          |       
| http_method| HTTP method, such as POST/GET/HEAD/PUT. It is case-insensitive  | String   |   
| in_uri  | HTTP uri    | String      |    
| headers | Key-value pair of HTTP header   | map&lt;string,string&gt;| 
|params | Key-value pair of HTTP params      | map&lt;string,string&gt; |  

#### Returned result
A signature is returned, which can be used within the specified validity period (which is set via CosSysConfig and defaults to 60 sec). A returned empty string indicates the generation of signature failed.

### Method prototype 2
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
#### Parameters 
| Parameter Name | Parameter Description | Type |
|---------|---------|---------|
| secret_id  | The project identity ID owned by a developer, which is used for identity authentication  | String     |    
| secret_key | The project identity key owned by a developer  | String   |       
| http_method| HTTP method, such as POST/GET/HEAD/PUT. It is case-insensitive  | String|        
| in_uri   | HTTP uri | String     |     
| headers | Key-value pair of HTTP header     | map &lt;string,string&gt;|    
| params  | Key-value pair of HTTP params   |  map &lt;string,string&gt; |  
| start_time_in_s | Start time of the signature's validity period  | uint64_t   |    
| end_time_in_s | End time of the signature's validity period | uint64_t     |    

#### Returned result
- A signature (String) is returned, which can be used within the specified validity period. A returned empty string indicates the generation of signature failed.

## Service/Bucket/Object Operations
All Service/Bucket/Object-related method prototypes are shown as follows:
```
CosResult Operator(BaseReq, BaseResp)
```

### CosResult
CosResult encapsulates the error code and corresponding error message returned when an error occurs with the request. For more information, please see [Error Codes](/document/product/436/7730 "错误码").
> **Note:**
> The CoSResult object is always returned for requests encapsulated in the SDK. After an API call is completed, you can use the IsSucc() member function to determine whether the call is successful.**

#### Member Functions
| Function  | Description | 
|---------|---------|
| bool isSucc() | Returns a Boolean value to indicate whether this call is successful. <br>The CosResult member functions described below only apply when False is returned. <br>If True is returned, the response content can be obtained from OperatorResp. |
| string GetErrorCode() | Obtains the error code returned by COS to determine the error scenario. |
| string GetErrorMsg() | Contains details of error. |
| string GetResourceAddr() | Resource address: Bucket address or Object address. |    
| string GetXCosRequestId() | When a request is sent, the server automatically generates a unique ID for the request. <br>The request-id can be used by COS to quickly locate any problem occurred. |
| string GetXCosTraceId() | If an error occurs with a request, the server automatically generates a unique ID for the error. <br>The trace-id can be used by COS to quickly locate any problem occurred. <br>If an error occurs with a request, trace-id corresponds to request-id on an one-to-one basis.
| string GetErrorInfo() | Obtains the SDK internal error information. |
| int GetHttpStatus() | Obtains HTTP status code. |

#### BaseReq/BaseResp
BaseReq and BaseResp encapsulate the request and response, respectively. The caller only needs to generate OperatorReq, such as GetBucketReq as described below, based on the type of operation you want to perform, and populate it.
After the function is returned, call BaseResp's member functions to get the request result.

- For Request, you only need to focus on its constructors unless otherwise specified.

- Response for all methods has member functions that can be used to obtain common response headers. 
The common member functions of Response are as follows. For the descriptions of fields, please see [Common Response Headers](/document/product/436/7729 "公共返回头部").
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

## Bucket Operations
###  Get Bucket
#### Feature description
This API (Get Bucket) is equivalent to List Object. It is used to list some or all of the Objects under the Bucket. Read permission is required to initiate this request. For more information about this API, please see [Get Bucket](/document/product/436/7734).

#### Method prototype
```cpp
CosResult GetBucket(const GetBucketReq& req, GetBucketResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
|  req | GetBucketReq, the request for GetBucket operation.  | 
| resp | GetBucketResp, the response for GetBucket operation. |
GetBucketResp provides the following member functions to obtain the content of the response in XML format returned via Get Bucket. 
```C++
std::vector<Content> GetContents();
std::string GetName();
std::string GetPrefix();
std::string GetMarker();
uint64_t GetMaxKeys();
bool IsTruncated();
std::vector<std::string> GetCommonPrefixes();
```
Content is composed as follows:
```
struct Content {
    std::string m_key; // Object's Key
    std::string m_last_modified; // The time when Object was last modified
    std::string m_etag; // The MD-5 algorithm check value of the file
    std::string m_size; // File size (in bytes)
    std::vector<std::string> m_owner_ids; // Information of the Bucket owner
    std::string m_storage_class; // The storage class of Object. Enumerated values: STANDARD, STANDARD_IA
};
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of GetBucketReq
qcloud_cos::GetBucketReq req(bucket_name);
qcloud_cos::GetBucketResp resp;
qcloud_cos::CosResult result = cos.GetBucket(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
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

###  Put Bucket
#### Feature description
This API (Put Bucket) is used to create a Bucket under specified account. This API does not support anonymous requests. To create a Bucket, you should use a request with Authorization signature. The Bucket creator defaults to the Bucket owner. For more information about this API, please see [Put Bucket](/document/product/436/7738).

#### Method prototype
```cpp
CosResult PutBucket(const PutBucketReq& req, PutBucketResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
|  req | PutBucketReq, the request for PutBucket operation.  | 
| resp  | PutBucketResp, the response for PutBucket operation. | 
PutBucketReq provides the following member functions:
```C++
// Defines the ACL attribute of Bucket. Valid values: private, public-read-write, public-read
// Default: private
void SetXCosAcl(const std::string& str);

// Grants read permission to the authorized user. Format: x-cos-grant-read: id=" ",id=" ".
// For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantRead(const std::string& str);

// Grants write permission to the authorized user. Format: x-cos-grant-write: id=" ",id=" "./
// For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantWrite(const std::string& str);
    
// Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: id=" ",id=" ".
// For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantFullControl(const std::string& str);
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

qcloud_cos::PutBucketReq req(bucket_name);
qcloud_cos::PutBucketResp resp;
qcloud_cos::CosResult result = cos.PutBucket(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    Failed to create the Bucket. You can call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Delete Bucket
#### Feature description
This API (Delete Bucket) is used to delete a Bucket under a specified account. The Bucket must be empty before it can be deleted. The Bucket can be deleted only if its content is removed. For more information about this API, please see [Delete Bucket](/document/product/436/7732).

#### Method prototype
```cpp
CosResult DeleteBucket(const DeleteBucketReq& req, DeleteBucketResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req | DeleteBucketReq, the request for DeleteBucket operation.  | 
| resp | DeletBucketResp, the response for DeletBucket operation.  | 

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of DeleteBucketReq
qcloud_cos::DeleteBucketReq req(bucket_name);
qcloud_cos::DeleteBucketResp resp;
qcloud_cos::CosResult result = cos.DeleteBucket(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to delete the Bucket. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Put Bucket Replication
#### Feature description
This API (Put Bucket Replication) is used to add replication configuration to the bucket for which versioning is enabled. If the bucket already has a replication configuration, the request will replace the existing configuration. For more information about this API, please see [Put Bucket Replication](/document/product/436/11738).

#### Method prototype
```cpp
CosResult PutBucketReplication(const DPutBucketReplicationReq& req, PutBucketReplicationResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | PutBucketReplicationReq, the request for PutBucketReplication operation. | 
| resp | PutBucketReplicationResp, the response for PutBucketReplication operation.  | 

```
// Sets the Replication initiator's role. Format: qcs::cam::uin/[UIN]:uin/[Subaccount]
void SetRole(const std::string& role);

// Adds ReplicationRule
void AddReplicationRule(const ReplicationRule& rule);

// Sets ReplicationRules
void SetReplicationRule(const std::vector<ReplicationRule>& rules);
```

ReplicationRule is composed as follows:
```
struct ReplicationRule {
    bool m_is_enable; // Whether the Rule takes effect
    std::string m_id; // Optional field, used to specify the name of a specific Rule
    std::string m_prefix; // Prefix match policy. Prefixes cannot overlap, otherwise an error is returned. This is left empty for root directory.
    std::string m_dest_bucket; // Identifies destination Bucket. Resource identifier: qcs:id/0:cos:[region]:appid/[AppId]:[bucketname]
    std::string m_dest_storage_class; // Storage class (optional). Enumerated values: Standard, Standard_IA. The original bucket class is used if it is left empty.

    ReplicationRule();
    ReplicationRule(const std::string& prefix,
                    const std::string& dest_bucket,
                    const std::string& storage_class = "", 
                    const std::string& id = "", 
                    bool is_enable = true);
};
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of PutBucketReplicationReq
qcloud_cos::PutBucketReplicationReq req(bucket_name);
req.SetRole("qcs::cam::uin/***:uin/****");
qcloud_cos::ReplicationRule rule("sevenyou_10m", "qcs:id/0:cos:cn-south:appid/***:sevenyousouthtest", "", "RuleId_01", true);
req.AddReplicationRule(rule)

qcloud_cos::PutBucketReplicationResp resp;
qcloud_cos::CosResult result = cos.PutBucketReplication(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to set cross-origin replication. Call CosResult's member functions to output error information, such as requestID,    etc.
} 
```

###  Get Bucket Replication
#### Feature description
This API (Get Bucket Replication) is used to read the cross-origin replication configuration information in a bucket.
For more information about this API, please see [Get Bucket Replication](/document/product/436/11736).

#### Method prototype
```cpp
CosResult GetBucketReplication(const DGetBucketReplicationReq& req, GetBucketReplicationResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | GetBucketReplicationReq, the request for GetBucketReplication operation. | 
| resp | GetBucketReplicationResp, the response for GetBucketReplication operation.  | 
```
// Obtains the Replication initiator's role
std::string GetRole();

// Obtains ReplicationRules. For the definition of ReplicationRule, please see Put Bucket Replication
std::vector<ReplicationRule> GetRules();
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of GetBucketReplicationReq
qcloud_cos::GetBucketReplicationReq req(bucket_name);
qcloud_cos::GetBucketReplicationResp resp;
qcloud_cos::CosResult result = cos.GetBucketReplication(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to obtain cross-region replication configuration. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

### Delete Bucket Replication
#### Feature description
This API (Delete Bucket Replication) is used to delete the cross-origin replication configuration in a bucket. For more information about this API, please see [Delete Bucket Replication](/document/product/436/11737).

#### Method prototype
```cpp
CosResult DeleteBucketReplication(const DDeleteBucketReplicationReq& req, DeleteBucketReplicationResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | DeleteBucketReplicationReq, the request for DeleteBucketReplication operation. | 
| resp | DeleteBucketReplicationResp, the response for DeleteBucketReplication operation.  | 

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of DeleteBucketReplicationReq
qcloud_cos::DeleteBucketReplicationReq req(bucket_name);
qcloud_cos::DeleteBucketReplicationResp resp;
qcloud_cos::CosResult result = cos.DeleteBucketReplication(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to delete cross-region replication configuration. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Put Bucket Lifecycle
#### Feature description
COS allows you to manage the lifecycle of an Object in Bucket by configuring lifecycle. The lifecycle configuration contains one or more rule sets that will be applied to a group of object rules (each rule defines an operation for COS).
These operations are divided into the following two types:
- Transition: Specify the time when the storage class of an object is changed to another one. For example, you can specify that the storage class of an object is changed to STANDARD_IA (applicable to the objects that are accessed infrequently) 30 days after it is created.
-  Expiration: Specify the expiration time of Object. COS will automatically delete the expired objects.
This API (Put Bucket Lifecycle) is used to create a new lifecycle configuration for a Bucket. If lifecycle has been configured for the Bucket, you can use this API to create a new configuration to overwrite the existing one. For more information about this API, please see [Put Bucket Lifecycle](/document/product/436/8280).

#### Method prototype
```cpp
CosResult PutBucketLifecycle(const DPutBucketLifecycleReq& req, PutBucketLifecycleResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | PutBucketLifecycleReq, the request for PutBucketLifecycle operation.  | 
| resp | PutBucketLifecycleResp, the response for PutBucketLifecycle operation.  | 
```
// Adds LifecycleRule
void AddRule(const LifecycleRule& rule)

// Sets LifecycleRule
void SetRule(const std::vector<LifecycleRule>& rules)

```
LifecycleRule is composed as follows:
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
    std::string m_prefix; // Specifies the prefix to which the rule applies. The objects matching the prefix are subject to the rule. Only one prefix is allowed.
    std::vector<LifecycleTag> m_tags; // Tag. You can specify more than one tags, or leave it empty.
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
    // Using both Days and Date in the same rule is not allowed.
    uint64_t m_days; // Specifies the number of days from the last modification date of object until the operation specified by the rule is performed. It should be a non-negative integer.
    std::string m_date; // Indicates when the operation specified by the rule is performed.
    std::string m_storage_class; // Specifies the storage class to which the object is switched. Enumerated values: Standard_IA
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
    // Using both Days and Date in the same rule is not allowed.
    uint64_t m_days; // Specifies the number of days from the last modification date of object until the operation specified by the rule is performed. It should be a positive integer.
    std::string m_date; // Indicates when the operation specified by the rule is performed.
    bool m_expired_obj_del_marker; // Indicates whether to delete expired object. Enumerated value: True, False.
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
    uint64_t m_days; // Specifies the number of days from the last modification date of object until the operation specified by the rule is performed. It should be a non-negative integer.
    std::string m_storage_class; // Specifies the storage class to which the object is switched. Enumerated values: Standard_IA
};

class LifecycleNonCurrExpiration {
public:
    LifecycleNonCurrExpiration();
    
    uint64_t GetDays();

    void SetDays(uint64_t days);

    bool HasDays();

private:
    uint64_t m_days; // Specifies the number of days from the last modification date of object until the operation specified by the rule is performed. It should be a positive integer.
};

struct AbortIncompleteMultipartUpload {
    uint64_t m_days_after_init; // Indicates the number of days within which the multipart upload must be completed after it starts.
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
    bool m_is_enable; // Whether the rule takes effect
    std::string m_id; // Rule ID
    LifecycleFilter m_filter; / / Filter, which specifies the object scope on which the rule takes effect
    std::vector<LifecycleTransition> m_transitions; // Transition operation
    LifecycleExpiration m_expiration;// Expiration operation
    LifecycleNonCurrTransition m_non_curr_transition; // Transition operation on Object of non-current version
    LifecycleNonCurrExpiration m_non_curr_expiration; // Expiration operation on Object of non-current version
    AbortIncompleteMultipartUpload m_abort_multi_upload; // Sets the maximum time length allowed for a multipart upload.
}
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of PutBucketLifecycleReq
qcloud_cos::PutBucketLifecycleReq req(bucket_name);
// Sets rule 1
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

// Sets rule 2
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

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to set the lifecycle. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Get Bucket Lifecycle
#### Feature description
This API (Get Bucket Lifecycle) is used to obtain the lifecycle configuration of a Bucket. If no lifecycle rule is configured for the Bucket, NoSuchLifecycleConfiguration is returned. For more information about this API, please see [Get Bucket Lifecycle](/document/product/436/8278).

#### Method prototype
```cpp
CosResult GetBucketLifecycle(const GetBucketLifecycleReq& req, GetBucketLifecycleResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | GetBucketLifecycleReq, the request for GetBucketLifecycle operation.  | 
| resp | GetBucketLifecycleResp, the response for GetBucketLifecycleoperation.  | 
```
// Obtains LifecycleRules
std::vector<LifecycleRule> GetRules()
```
For the definition of LifecycleRule, please see Put Bucket Lifecycle.

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of GetBucketLifecycleReq
qcloud_cos::GetBucketLifecycleReq req(bucket_name);
qcloud_cos::GetBucketLifecycleResp resp;
qcloud_cos::CosResult result = cos.GetBucketLifecycle(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to obtain lifecycle configuration. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Delete Bucket Lifecycle
#### Feature description
This API (Delete Bucket Lifecycle) is used to delete the lifecycle configuration of a Bucket. If no lifecycle rule is configured for the Bucket, NoSuchLifecycleConfiguration is returned. For more information about this API, please see [Delete Bucket Lifecycle](/document/product/436/8284).

#### Method prototype
```cpp
CosResult DeleteBucketLifecycle(const DeleteBucketLifecycleReq& req, DeleteBucketLifecycleResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | DeleteBucketLifecycleReq, the request for DeleteBucketLifecycle operation.  | 
| resp | DeleteBucketLifecycleResp, the response for DeleteBucketLifecycle.  | 

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of DeleteBucketLifecycleReq
qcloud_cos::DeleteBucketLifecycleReq req(bucket_name);
qcloud_cos::DeleteBucketLifecycleResp resp;
qcloud_cos::CosResult result = cos.DeleteBucketLifecycle(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to delete lifecycle configuration. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Put Bucket CORS
#### Feature description
This API (Put Bucket CORS) is used to set cross-origin resource sharing permission for a Bucket by importing configuration files in XML format (file size limit: 64 KB). By default, the Bucket owner has the permission to use this API and can grant the permission to others. For more information about this API, please see [Put Bucket CORS](/document/product/436/8279).

#### Method prototype
```cpp
CosResult PutBucketCORS(const DPutBucketCORSReq& req, PutBucketCORSResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | PutBucketCORSReq, the request for PutBucketCORS operation.  | 
| resp | PutBucketCORSResp, the response for PutBucketCORS operation.  | 
```
// Adds CORSRule
void AddRule(const CORSRule& rule);

// Sets CORSRule
void SetRules(const std::vector<CORSRule>& rules)

```
CORSRule is composed as follows:
```
struct CORSRule {
    std::string m_id; // Sets rule ID (optional)
    std::string m_max_age_secs; // Sets the validity period of the results obtained by OPTIONS
    std::vector<std::string> m_allowed_headers; // When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported.
    std::vector<std::string> m_allowed_methods; // Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE.
    std::vector<std::string> m_allowed_origins; // Allowed access sources. Wildcard "*" is supported. Format: protocol://domain name[:port], for example, http://www.qq.com
    std::vector<std::string> m_expose_headers;  // Sets the custom header information that can be received by the browser from the server. |
};

```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of PutBucketCORSReq
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

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to set the cross-origin resource sharing permission. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Get Bucket CORS
#### Feature description
This API (Get Bucket CORS) is used by the Bucket owner to configure cross-origin resource sharing on a bucket. CORS (Cross-Origin Resource Sharing) is a W3C standard. By default, the Bucket owner has the permission to use this API and can grant the permission to others. For more information about this API, please see [Get Bucket CORS](/document/product/436/8274).

#### Method prototype
```cpp
CosResult GetBucketCORS(const DGetBucketCORSReq& req, GetBucketCORSResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | GetBucketCORSReq, the request for GetBucketCORS operation.  | 
| resp | GetBucketCORSResp, the response for GetBucketCORS operation.  | | 
```
// Obtains CORSRules. For the definition of CORSRule, please see Put Bucket CORS.
std::vector<CORSRule> GetCORSRules();
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of GetBucketCORSReq
qcloud_cos::GetBucketCORSReq req(bucket_name);
qcloud_cos::GetBucketCORSResp resp;
qcloud_cos::CosResult result = cos.GetBucketCORS(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to obtain CORS configuration. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Delete Bucket CORS
#### Feature description
This API (Delete Bucket CORS) is used to delete the CORS configuration of a Bucket. If no CORS information is configured for the Bucket, NoSuchCORSConfiguration is returned. For more information about this API, please see [Delete Bucket CORS](/document/product/436/8283).

#### Method prototype
```cpp
CosResult DeleteBucketCORS(const DDeleteBucketCORSReq& req, DeleteBucketCORSResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | DeleteBucketCORSReq, the request for DeleteBucketCORS operation.  | 
| resp | DeleteBucketCORSResp, the response for DeleteBucketCORS operation.  | 

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of DeleteBucketCORSReq
qcloud_cos::DeleteBucketCORSReq req(bucket_name);
qcloud_cos::DeleteBucketCORSResp resp;
qcloud_cos::CosResult result = cos.DeleteBucketCORS(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to delete CORS configuration. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Put Bucket ACL
#### Feature description
This API (Put Bucket ACL) is used to write ACL for a Bucket. You can import ACL information either by using Header: "x-cos-acl", "x-cos-grant-read", "x-cos-grant-write", "x-cos-grant-full-control", or by using Body in XML format. For more information about this API, please see [Put Bucket ACL](/document/product/436/7737).

#### Method prototype
```cpp
CosResult PutBucketACL(const DPutBucketACLReq& req, PutBucketACLResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | PutBucketACLReq, the request for PutBucketACL operation.  | 
| resp | PutBucketACLResp, the response for PutBucketACL operation.  | 
```
// Defines the ACL attribute of Bucket. Valid values: private, public-read-write, public-read
// Default: private
void SetXCosAcl(const std::string& str);

// Grants read permission to the authorized user. Format: x-cos-grant-read: id=" ",id=" ".
// For authorization to a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantRead(const std::string& str);

// Grants write permission to the authorized user. Format: x-cos-grant-write: id=" ",id=" "./
// For authorization to a sub-account, ,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantWrite(const std::string& str);

// Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: id=" ",id=" ".
//For authorization to a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantFullControl(const std::string& str);

// Bucket owner ID
void SetOwner(const Owner& owner);

// Sets the information of authorized user and permissions
void SetAccessControlList(const std::vector<Grant>& grants);

// Adds authorization information for a single Bucket
void AddAccessControlList(const Grant& grant);
        
```

> **Note:**
>   APIs such as SetXCosAcl, SetXCosGrantRead, SetXCosGrantWrite, and SetXCosGrantFullControl cannot be used with SetAccessControlList and AddAccessControlList. This is because the former kind of APIs are implemented by setting HTTP Header, while the latter kind of APIs are implemented by adding content in XML format to the Body. You can only use either of the two kinds of APIs. The first kinds of APIs are preferred in SDK.

ACLRule is composed as follows:
```
struct Grantee {
    // "type" can be RootAccount or SubAccount.
    // If type is RootAccount, you can enter account ID in "uin" or in "uin" of id, or replace uin/<OwnerUin> and uin/<SubUin> with "anyone" (all types of users).
    // If type is RootAcount, uin represents root account, and SubAccount represents sub-account.
    std::string m_type; 
    std::string m_id; // qcs::cam::uin/<OwnerUin>:uin/<SubUin>
    std::string m_display_name; // Optional
    std::string m_uri;
};

struct Grant {
    Grantee m_grantee; // Resource information of the authorized user
    std::string m_perm; // Indicates the permission granted to the authorized user. Enumerated values: READ, WRITE, and FULL_CONTROL
};

```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of PutBucketACLReq
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

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Sets the ACL. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Get Bucket ACL
#### Feature description
This API (Get Bucket ACL) is used to obtain the ACL (Access Control List) of a Bucket. Only the Bucket owner has the access to this API. For more information about this API, please see [Get Bucket ACL](/document/product/436/7733).

#### Method prototype
```cpp
CosResult GetBucketACL(const DGetBucketACLReq& req, GetBucketACLResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | GetBucketACLReq, the request for GetBucketACL operation.  | 
| resp | GetBucketACLResp, the response for GetBucketACL operation.  | 
```
std::string GetOwnerID();
std::string GetOwnerDisplayName();
std::vector<Grant> GetAccessControlList();
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";

// The bucket_name is required in the constructor of GetBucketACLReq
qcloud_cos::GetBucketACLReq req(bucket_name);
qcloud_cos::GetBucketACLResp resp;
qcloud_cos::CosResult result = cos.GetBucketACL(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to obtain the ACL. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

## Object Operations
Parameter object_name is the object key, which is the unique identifier of an object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg.

For more information about "object key", please see [Object Overview](https://cloud.tencent.com/document/product/436/13324).

###  Get Object
#### Feature description
This API (Get Object) is used to download a file (Object) locally or to a specified stream. This operation requires that the user have the read permission for the target Object or the read permission for the target Object be available for everyone (public-read).

#### Method prototype
```cpp
// Downloads Object to a local file
CosResult GetObject(const GetObjectByFileReq& req, GetObjectByFileResp* resp);

// Downloads Object to a stream
CosResult GetObject(const GetObjectByStreamReq& req, GetObjectByStreamResp* resp);

// Downloads Object to a local file (multi-thread)
CosResult GetObject(const MultiGetObjectReq& req, MultiGetObjectResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | GetObjectByFileReq/GetObjectByStreamReq/MultiGetObjectReq, the request for GetObject operation.  | 
| resp | GetObjectByFileResp/GetObjectByStreamResp/MultiGetObjectResp, the response for GetObject operation.  | 
The member functions are as follows:
```
// Sets the Content-Type parameter in the response header
void SetResponseContentType(const std::string& str);

// Sets the Content-Language parameter in the response header
void SetResponseContentLang(const std::string& str);

// Sets the Content-Expires parameter in the response header
void SetResponseExpires(const std::string& str);

// Sets the Cache-Control parameter in the response header
void SetResponseCacheControl(const std::string& str);

// Sets the Content-Disposition parameter in the response header
void SetResponseContentDisposition(const std::string& str);

// Sets the Content-Encoding parameter in the response header
void SetResponseContentEncoding(const std::string& str);
```
GetObjectResp not only reads the member functions of common headers, but also provides the following member functions:
```C++
// Obtains the last modification time of the Object. Date format (string): "28 Oct 2014 20:30:00 GMT"
std::string GetLastModified();

// Obtains Object type, which indicates whether the Object is appendable for upload. Enumerated values: normal or appendable
std::string GetXCosObjectType();

// Obtains the storage class of an Object. Enumerated values: STANDARD,STANDARD_IA
std::string GetXCosStorageClass();

// Returns all custom meta in the form of map. The key of a map does not contain the prefix "x-cos-meta-"
std::map<std::string, std::string> GetXCosMetas();

// Obtains the custom meta. The parameter can be "*" in "x-cos-meta-*"
std::string GetXCosMeta(const std::string& key);

// Obtains the algorithm used by server for encryption
std::string GetXCosServerSideEncryption(); 
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
std::string object_name = "object_name";
std::string local_path = "/tmp/object_name";

// Downloads to a local file
{
    // Parameters appid, bucketname and object, as well as the local path (including file name) are required for the request
    qcloud_cos::GetObjectByFileReq req(bucket_name, object_name, local_path);
    qcloud_cos::GetObjectByFileResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // Download is successful. Call GetObjectByFileResp's member functions
    } else {
        // Download failed. Call CosResult's member functions to output error information, such as requestID, etc.
    }
}

// Download to a stream
{
    // Parameters appid, bucketname and object, as well as output stream are required for the request
    std::ostringstream os;
    qcloud_cos::GetObjectByStreamReq req(bucket_name, object_name, os);
    qcloud_cos::GetObjectByStreamResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // Download is successful. Call GetObjectByStreamResp's member functions
    } else {
        // Download failed. Call CosResult's member functions to output error information, such as requestID, etc.
    }
}

// Downloads file locally in multiple threads
{
    // Parameters appid, bucketname and object, as well as the local path (including file name) are required for the request
    qcloud_cos::MultiGetObjectReq req(bucket_name, object_name, local_path);
    qcloud_cos::MultiGetObjectResp resp;
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    if (result.IsSucc()) {
        // Download is successful. Call MultiGetObjectResp's member functions
    } else {
        // Download failed. Call CosResult's member functions to output error information, such as requestID, etc.
    }
}
```

###  Head Object
#### Feature description
This API (Head Object) is used to get the metadata of an Object. It has the same permissions as Get Object.

#### Method prototype
```cpp
CosResult HeadObject(const HeadObjectReq& req, HeadObjectResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | HeadObjectReq, the request for HeadObject operation.  | 
| resp | HeadObjectResp, the response for HeadObject operation.  | 
HeadObjectResp not only reads the member functions of common headers, but also provides the following member functions:
```C++
std::string GetXCosObjectType();

std::string GetXCosStorageClass();

// Obtains the custom meta. The parameter can be "*" in "x-cos-meta-*"
std::string GetXCosMeta(const std::string& key);

// Returns all custom meta in the form of map. The key of a map does not contain the prefix "x-cos-meta-"
std::map<std::string, std::string> GetXCosMetas();

// Obtains the algorithm used by server for encryption
std::string GetXCosServerSideEncryption(); 
```
#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
std::string object_name = "object_name";
qcloud_cos::HeadObjectReq req(bucket_name, object_name);
qcloud_cos::HeadObjectResp resp;
qcloud_cos::CosResult result = cos.HeadObject(req, &resp);
if (result.IsSucc()) {
    // Download is successful. Call HeadObjectResp's member functions
} else {
    // Download failed. Call CosResult's member functions to output error information, such as requestID, etc.
}
```

###  Put Object
#### Feature description
This API (Put Object) is used to upload a file (Object) to the specified Bucket.

#### Method prototype
```cpp
/// Uploads via Stream
CosResult PutObject(const PutObjectByStreamReq& req, PutObjectByStreamResp* resp);

/// Uploads a local file
CosResult PutObject(const PutObjectByFileReq& req, PutObjectByFileResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | PutObjectByStreamReq/PutObjectByFileReq, the request for PutObject operation.  | 
| resp | PutObjectByStreamResp/PutObjectByFileResp, the response for PutObject operation.  | 

PutObject*Req contains the following member functions:

```C++
// Cache-Control, the caching policy defined in RFC 2616 and saved as Object metadata.
void SetCacheControl(const std::string& str);

// Content-Disposition, the file name defined in RFC 2616 and saved as Object metadata.
void SetContentDisposition(const std::string& str);

// Content-Encoding, the encoding format defined in RFC 2616 and saved as Object metadata.
void SetContentEncoding(const std::string& str);

// Content-Type, the content type (MIME) defined in RFC 2616 and saved as Object metadata.
void SetContentType(const std::string& str);

// Expect  If Expect: 100-continue is used, the request content will not be sent until the receipt of response from server.
void SetExpect(const std::string& str);

// Expires, the expiration time defined in RFC 2616 and saved as Object metadata.
void SetExpires(const std::string& str);

// The header information that can be defined by users, which is returned as Object metadata. The size is limited to 2 KB.
void SetXCosMeta(const std::string& key, const std::string& value);

// x-cos-storage-class, which is used to set the storage class of Object. Enumerated values: STANDARD, STANDARD_IA
// Default: STANDARD (supported only in South China region)
void SetXCosStorageClass(const std::string& storage_class);

// Defines the ACL attribute of Object. Valid values: private, public-read-write, public-read.
// Default: private
void SetXcosAcl(const std::string& str);

// Grants read permission to the authorized user. Format: x-cos-grant-read: id=" ",id=" ".
// For authorization to a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantRead(const std::string& str);

// Grants write permission to the authorized user. Format: x-cos-grant-write: id=" ",id=" "./
// For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantWrite(const std::string& str);

// Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: id=" ",id=" ".
//For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantFullControl(const std::string& str);

/// Sets the algorithm used by server for encryption. AES256 is supported.
void SetXCosServerSideEncryption(const std::string& str);
```

PutObject*Resp contains the following member functions:
```C++
/// Obtains the version number of Object. If multiple versions of an object are not enabled in a Bucket, empty string is returned.
std::string GetVersionId();

/// Algorithm used by server for encryption
std::string GetXCosServerSideEncryption();
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
std::string object_name = "object_name";

// Simple upload (stream)
{
    std::istringstream iss("put object");
    // istream is required in the constructor of the request
    qcloud_cos::PutObjectByStreamReq req(bucket_name, object_name, iss);
    // Calls Set method to set metadata or ACL
    req.SetXCosStorageClass("STANDARD_IA");
    qcloud_cos::PutObjectByStreamResp resp;
    qcloud_cos::CosResult result = cos.PutObject(req, &resp);
    
    if (result.IsSucc()) {
        // The call is successful. Call resp's member functions to obtain the response content
        do sth
    } else {
        // The call failed. Call result's member functions to obtain the response content
        std::cout << "ErrorInfo=" << result.GetErrorInfo() << std::endl;
        std::cout << "HttpStatus=" << result.GetHttpStatus() << std::endl;
        std::cout << "ErrorCode=" << result.GetErrorCode() << std::endl;
        std::cout << "ErrorMsg=" << result.GetErrorMsg() << std::endl;
        std::cout << "ResourceAddr=" << result.GetResourceAddr() << std::endl;
        std::cout << "XCosRequestId=" << result.GetXCosRequestId() << std::endl;
        std::cout << "XCosTraceId=" << result.GetXCosTraceId() << std::endl;
     }
}

// Simple upload (file)
{
    // The local file path is required in the constructor of the request
    qcloud_cos::PutObjectByFileReq req(bucket_name, object_name, "/path/to/local/file");
    // Calls Set method to set metadata or ACL
    req.SetXCosStorageClass("STANDARD_IA");
    qcloud_cos::PutObjectByFileResp resp;
    qcloud_cos::CosResult result = cos.PutObject(req, &resp);
        if (result.IsSucc()) {
        // The call is successful. Call resp's member functions to obtain the response content
        do sth
    } else {
        // The call failed. Call result's member functions to obtain the response content
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

###  Delete Object
#### Feature description
This API (Delete Object) is used to delete a file (Object) from a Bucket of COS. This operation requires that the user have the WRITE permission for the Bucket. For more information about this API, please see [Delete Object](/document/product/436/7743).

#### Method prototype
```cpp
CosResult DeleteObject(const DeleteObjectReq& req, DeleteObjectResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | DeleteObjectReq, the request for DeleteObject operation.  | 
| resp | DeletObjectResp, the response for DeletObject operation. | 

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
std::string object_name = "test_object";

qcloud_cos::DeleteObjectReq req(bucket_name, object_name);
qcloud_cos::DeleteObjectResp resp;
qcloud_cos::CosResult result = cos.DeleteObject(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to delete Object. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

## Multipart Upload Operations
###  Initiate Multipart Upload
#### Feature description
This API (Initiate Multipart Upload) is used to initialize multipart upload. After the request is executed successfully, Upload ID is returned for the subsequent Upload Part requests.

#### Method prototype
```cpp
CosResult InitMultiUpload(const InitMultiUploadReq& req, InitMultiUploadResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | InitMultiUploadReq, the request for InitMultiUpload operation.  | 
| resp | InitMultiUploadResp, the response for InitMultiUpload operation.  | 

InitMultiUploadReq contains the following member functions:
```
// Cache-Control, the caching policy defined in RFC 2616 and saved as Object metadata.
void SetCacheControl(const std::string& str);

// Content-Disposition, the file name defined in RFC 2616 and saved as Object metadata.
void SetContentDisposition(const std::string& str);

// Content-Encoding, the encoding format defined in RFC 2616 and saved as Object metadata.
void SetContentEncoding(const std::string& str);

// Content-Type, the content type (MIME) defined in RFC 2616 and saved as Object metadata.
void SetContentType(const std::string& str);

// Expires, the expiration time defined in RFC 2616 and saved as Object metadata.
void SetExpires(const std::string& str);

// The header information that can be defined by users, which is returned as Object metadata. The size is limited to 2 KB.
void SetXCosMeta(const std::string& key, const std::string& value);

// x-cos-storage-class, which is used to set the storage class of Object. Enumerated values: STANDARD, STANDARD_IA
// Default: STANDARD
void SetXCosStorageClass(const std::string& storage_class);

// Defines the ACL attribute of Object. Valid values: private, public-read-write, public-read.
// Default: private
void SetXcosAcl(const std::string& str);

// Grants read permission to the authorized user. Format: x-cos-grant-read: id=" ",id=" ".
// For authorization to a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantRead(const std::string& str);

// Grants write permission to the authorized user. Format: x-cos-grant-write: id=" ",id=" "./
// For authorization to a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantWrite(const std::string& str);

// Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: id=" ",id=" ".
// For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXcosGrantFullControl(const std::string& str);

/// Sets the algorithm used by server for encryption. AES256 is supported.
void SetXCosServerSideEncryption(const std::string& str);
```

When the request is executed successfully, the response containing bucket (destination Bucket of multipart upload), key (object name) and uploadId (ID required for the subsequent multipart uploads) is returned.

InitMultiUploadResp contains the following member functions:
``` C++
std::string GetBucket();
std::string GetKey();
std::string GetUploadId();

// Algorithm used by server for encryption
std::string GetXCosServerSideEncryption();
```

#### Example
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

###  Upload Part
#### Feature description
This API (Upload Part) is used to implement multipart upload after initialization. A file can be split into 10000 chunks at most (minimum is 1) for multipart upload, and the size of each file chunk should be between 1 MB and 5 GB. Parameters partNumber and uploadId are required for Upload Part (partNumber is the file chunk No. Out-of-order upload is supported).

#### Method prototype
```cpp
CosResult UploadPartData(const UploadPartDataReq& request, UploadPartDataResp* response);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | UploadPartDataReq, the request for UploadPartData operation.  | 
| resp | UploadPartDataResp, the response for UploadPartData operation.  | 
When constructing UploadPartDataReq, you need to specify request's APPID, Bucket, Object, UploadId obtained after the initialization is completed, and the data stream for upload (after calling this API, the caller needs to close the stream).
```
UploadPartDataReq(const std::string& bucket_name,
                    const std::string& object_name, const std::string& upload_id,
                    std::istream& in_stream);
```
In addition, file chunk No. is required in the request. This chunk is needed when the multipart upload is completed.
```
void SetPartNumber(uint64_t part_number);
```

UploadPartDataResp contains the following member functions:
```
/// Algorithm used by server for encryption
std::string GetXCosServerSideEncryption();
```

#### Example
```cpp
// Uploads the first chunk
{
    std::fstream is("demo_5M.part1");
    qcloud_cos::UploadPartDataReq req(bucket_name, object_name,
                                      upload_id, is);
    req.SetPartNumber(1);
    qcloud_cos::UploadPartDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartData(req, &resp);

    // After the upload is completed, record the chunk number and Etag returned
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_numbers.push_back(1);
    }
    is.close();
}

// Uploads the second chunk
{
    std::fstream is("demo_5M.part2");
    qcloud_cos::UploadPartDataReq req(bucket_name, object_name,
                                      upload_id, is);
    req.SetPartNumber(2);
    qcloud_cos::UploadPartDataResp resp;
    qcloud_cos::CosResult result = cos.UploadPartData(req, &resp);

    // After the upload is completed, record the chunk number and Etag returned 
    if (result.IsSucc()) {
        etags.push_back(resp.GetEtag());
        part_numbers.push_back(2);
    }
    is.close();
}
```

###  Complete Multipart Upload
#### Feature description
This API (Complete Multipart Upload) is used to complete the entire multipart upload. After you have uploaded all the file chunks using Upload Parts, you can use this API to complete the upload. When using this API, you need to provide the PartNumber and ETag for every chunk in Body, to verify the accuracy of chunks.

#### Method prototype
```cpp
CosResult CompleteMultiUpload(const CompleteMultiUploadReq& request, CompleteMultiUploadResp* response);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | CompleteMultiUploadReq, the request for CompleteMultiUpload operation.  | 
| resp | CompleteMultiUploadResp, the response for CompleteMultiUpload operation. | 
When constructing CompleteMultiUploadReq, you need to specify request APPID, Bucket, Object, and UploadId obtained after the initialization.
```
CompleteMultiUploadReq(const std::string& bucket_name,
                       const std::string& object_name, const std::string& upload_id)
```
In addition, the numbers and ETags of all the uploaded file chunks are also required for the request

```
// When the following methods are called, the numbers should correspond to Etags in sequence on an one-on-one basis.
void SetPartNumbers(const std::vector<uint64_t>& part_numbers);
void SetEtags(const std::vector<std::string>& etags) ;

// Adds part_number and ETag pairs
void AddPartEtagPair(uint64_t part_number, const std::string& etag);

/// Sets the algorithm used by server for encryption. AES256 is supported.
void SetXCosServerSideEncryption(const std::string& str);
```

The response returned for CompleteMultiUploadResp contains Location (domain name of the accessing public network of the created object), Bucket (the destination Bucket for multipart upload), Key (object name) and ETag (MD5 algorithm check value for the merged file). You can call the following member functions to access the response content.
```
std::string GetLocation();
std::string GetKey();
std::string GetBucket();
std::string GetEtag();

/// Algorithm used by server for encryption
std::string GetXCosServerSideEncryption();
```

#### Example
```cpp
qcloud_cos::CompleteMultiUploadReq req(bucket_name, object_name, upload_id);
qcloud_cos::CompleteMultiUploadResp resp;
req.SetEtags(etags);
req.SetPartNumbers(part_numbers);

qcloud_cos::CosResult result = cos.CompleteMultiUpload(req, &resp);
```

###  Multipart Upload
#### Feature description
Multipart Upload encapsulates three steps: initializing multipart upload, executing multipart upload, and completing multipart upload. You only need to specify the file to be uploaded in the request.

#### Method prototype
```cpp
CosResult MultiUploadObject(const MultiUploadObjectReq& request,        MultiUploadObjectResp* response);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | MultiUploadObjectReq, the request for MultiUploadObject operation. | 
| resp | MultiUploadObjectResp, the response for MultiUploadObject operation.  | 
When constructing MultiUploadObjectReq, you need to specify Bucket, Object, and the path of local file to be uploaded. If the path is not specified, the file with the same name as the Object under the current working path is used by default.
```
MultiUploadObjectReq(const std::string& bucket_name,
                     const std::string& object_name, const std::string& local_file_path = "");

/// Sets the algorithm used by server for encryption. AES256 is supported.
void SetXCosServerSideEncryption(const std::string& str);
```

- If multipart upload is successful, the response content is the same as that of CompleteMultiUploadResp.
- If multipart upload fails, the response content is same as that of InitMultiUploadResp, UploadPartDataResp or CompleteMultiUploadResp, depending on the failure type. You can call `GetRespTag()` to determine the step where the failure occurs.

```
// Returns Init, Upload, Complete
std::string GetRespTag();

/// Algorithm used by server for encryption
std::string GetXCosServerSideEncryption();
```

#### Example
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
    // Determines the specific step where the failure occurs.
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
#### Feature description
This API (Abort Multipart Upload) is used to abort a multipart upload operation and delete uploaded file chunks. When Abort Multipart Upload is called, a failure is returned for any request that is using Upload Parts.

#### Method prototype
```cpp
CosResult AbortMultiUpload(const AbortMultiUploadReq& request, AbortMultiUploadResp* response);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | AbortMultiUploadReq, the request for AbortMultiUpload.  | 
| resp | AbortMultiUploadResp, the response for AbortMultiUpload operation.  | 
When constructing AbortMultiUploadReq, you need to specify Bucket, Object and Upload_id.
``` C++
AbortMultiUploadReq(const std::string& bucket_name,
                    const std::string& object_name, const std::string& upload_id);
```
Call BaseResp's member functions to obtain common header unless otherwise specified.

#### Example
```cpp
qcloud_cos::AbortMultiUploadReq req(bucket_name, object_name,
                                                    upload_id);
qcloud_cos::AbortMultiUploadResp resp;
qcloud_cos::CosResult result = cos.AbortMultiUpload(req, &resp);
```

###  List Parts
#### Feature description
This API (List Parts) is used to query the uploaded file chunks in a specific multipart upload, listing all the uploaded chunks under the specified UploadId. For more information about this API, please see [List Parts](/document/product/436/7747).

#### Method prototype
```cpp
CosResult ListParts(const ListPartsReq& req, ListPartsResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | ListPartsReq, the request for ListParts operation.  | 
| resp | ListPartsResp, the response for ListParts operation.  | 
```
// Constructor: Bucket name, Object name, multipart upload ID
ListPartsReq(const std::string& bucket_name,                                                                                                                                      
             const std::string& object_name,
             const std::string& upload_id); 

// \brief The encoding format of the returned results.
void SetEncodingType(const std::string& encoding_type);

// \brief The maximum number of entries returned at a time. Default is 1,000.
void SetMaxParts(uint64_t max_parts);

// \brief Entries are listed in UTF-8 binary order by default, starting from marker
void SetPartNumberMarker(const std::string& part_number_marker);
```
```
// The destination Bucket for multipart upload
std::string GetBucket();

// The encoding format of returned results.
std::string GetEncodingType();

// Object name
std::string GetKey();

// The ID of current multipart upload.
std::string GetUploadId();

// The information of the initiator of current upload
Initiator GetInitiator();

// The information of the owner of these chunks
Owner GetOwner();

// Entries are listed in UTF-8 binary order by default, starting from marker
uint64_t GetPartNumberMarker();

// Returns information of each chunk
std::vector<Part> GetParts();

// If the list of returned entries is truncated, NextMarker represents the starting point of the next entry
uint64_t GetNextPartNumberMarker();

// Storage class of the file chunks. Enumerated values: Standard, Standard_IA
std::string GetStorageClass();

// Maximum number of entries returned at a time
uint64_t GetMaxParts();

// Whether the list of returned entries is truncated. Boolean: TRUE, FALSE
bool IsTruncated();
```

Part, Owner and Initiator are composed as follows:
```
struct Initiator {
    std::string m_id; // The unique identifier of creator
    std::string m_display_name; // User name description of creator
};

struct Owner {
    std::string m_id; // The unique identifier of user
    std::string m_display_name; // User name description
};

struct Part {
    uint64_t m_part_num; // File chunk number
    uint64_t m_size; // File chunk size (in bytes)
    std::string m_etag; // The MD5 algorithm check value of Object chunk
    std::string m_last_modified; // The last modification time of file chunk
};
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
std::string object_name = "test_object";

// uploadId is obtained by calling InitMultiUpload
qcloud_cos::ListPartsReq req(bucket_name, object_name, upload_id);
req.SetMaxParts(1);                                                                                                                                                               
req.SetPartNumberMarker("1");
qcloud_cos::ListPartsResp resp;
qcloud_cos::CosResult result = cos.ListParts(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to delete Object. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Put Object ACL
#### Feature description
This API (Put Object ACL) is used to write ACL for an Object. You can import ACL information either by using Header: "x-cos-acl", "x-cos-grant-read", "x-cos-grant-write", "x-cos-grant-full-control", or by using Body in XML format. For more information about this API, please see [Put Object ACL](/document/product/436/7748).

#### Method prototype
```cpp
CosResult PutObjectACL(const PutObjectACLReq& req, PutObjectACLResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | PutObjectACLReq, the request for PutObjectACL operation. | 
| resp | PutObjectACLResp, the response for PutObjectACL operation. | 
```
// Defines the ACL attribute of Object. Valid values: private, public-read-write, public-read.
// Default: private
void SetXCosAcl(const std::string& str);

// Grants read permission to the authorized user. Format: x-cos-grant-read: id=" ",id=" ".
// For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantRead(const std::string& str);

// Grants write permission to the authorized user. Format: x-cos-grant-write: id=" ",id=" "./
// For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantWrite(const std::string& str);

// Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: id=" ",id=" ".
// For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantFullControl(const std::string& str);

// Object owner ID
void SetOwner(const Owner& owner);

// Sets the information of authorized user and permissions
void SetAccessControlList(const std::vector<Grant>& grants);

// Adds the authorization information for a single Object
void AddAccessControlList(const Grant& grant);
        
```
> **Note: **
>  APIs such as SetXCosAcl, SetXCosGrantRead, SetXCosGrantWrite, and SetXCosGrantFullControl cannot be used with SetAccessControlList and AddAccessControlList. This is because the former kind of APIs are implemented by setting HTTP Header, while the latter kind of APIs are implemented by adding content in XML format to the Body. You can only use either of the two kinds of APIs. The first kinds of APIs are preferred in SDK. 

ACLRule is composed as follows:
```
struct Grantee {
    // "type" can be RootAccount or SubAccount.
    // If type is RootAccount, you can enter account ID in "uin" or in "uin" of id, or replace uin/<OwnerUin> and uin/<SubUin> with "anyone" (all types of users).
    // If type is RootAcount, uin represents root account, and SubAccount represents sub-account.
    std::string m_type; 
    std::string m_id; // qcs::cam::uin/<OwnerUin>:uin/<SubUin>
    std::string m_display_name; // Optional
    std::string m_uri;
};

struct Grant {
    Grantee m_grantee; // Resource information of the authorized user
    std::string m_perm; // Indicates the permission granted to the authorized user. Enumerated values: READ, WRITE, and FULL_CONTROL
};

```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-123456789";
std::string object_name = "sevenyou";

// 1. Configures ACL (through Body). You can configure the ACL through either Body or Header. You can only use one of these two methods, otherwise a conflict occurs. 
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
    // The call is successful. Call resp's member functions to obtain the response content
    if (result.IsSucc()) {
        // ...
    } else {
        // Sets the ACL. Call CosResult's member functions to output error information, such as requestID, etc.
    } 
}   

// 2. Configures ACL (through Header). You can configure the ACL through either Body or Header. You can only use one of these two methods, otherwise a conflict occurs.
{   
    qcloud_cos::PutObjectACLReq req(bucket_name, object_name);                                                                                                                    
    req.SetXCosAcl("public-read-write");

    qcloud_cos::PutObjectACLResp resp;
    qcloud_cos::CosResult result = cos.PutObjectACL(req, &resp);
    // The call is successful. Call resp's member functions to obtain the response content
    if (result.IsSucc()) {
        // ...
    } else {
        // Sets the ACL. Call CosResult's member functions to output error information, such as requestID, etc.
    } 
}   
```

###  Get Object ACL
#### Feature description
This API (Get Object ACL) is used to obtain the ACL (Access Control List) of an object (file). Only the Object owner has the access to this API. For more information about this API, please see [Get Object ACL](/document/product/436/7744).

#### Method prototype
```cpp
CosResult GetObjectACL(const DGetObjectACLReq& req, GetObjectACLResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | GetObjectACLReq, the request for GetObjectACL operation. | 
| resp | GetObjectACLResp, the response for GetObjectACL operation. | 
```
std::string GetOwnerID();
std::string GetOwnerDisplayName();
std::vector<Grant> GetAccessControlList();
```

#### Example
```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string Object_name = "cpp_sdk_v5-123456789";

The bucket_name is required in the constructor of GetObjectACLReq
qcloud_cos::GetObjectACLReq req(Object_name);
qcloud_cos::GetObjectACLResp resp;
qcloud_cos::CosResult result = cos.GetObjectACL(req, &resp);

// The call is successful. Call resp's member functions to obtain the response content
if (result.IsSucc()) {
    // ...
} else {
    // Failed to obtain the ACL. Call CosResult's member functions to output error information, such as requestID, etc.
} 
```

###  Put Object Copy
#### Feature description
This API (Put Object Copy) is used to copy a file from source path to the destination path. In the process of copying, file meta-attributes and ACLs can be modified. You can use this API to move or rename a file, modify file attributes and create a copy. The recommended file size is 1MB-5GB. For any file greater than 5 GB, use multipart upload (Upload - Copy). For more information about this API, please see [Put Object Copy](/document/product/436/10881).

#### Method prototype
```cpp
CosResult PutObjectCopy(const PutObjectCopyReq& req, PutObjectCopyResp* resp);
```

#### Parameters
| Parameter  | Description  | 
|---------|---------|
| req   | PutObjectCopyReq, the request for PutObjectCopy operation.  | 
| resp | PutObjectCopyResp, the response for PutObjectCopy operation. | 
```
// The path of source file URL. You can specify the history version with the versionid sub-resource
void SetXCosCopySource(const std::string& str);

// Indicates whether to copy metadata. Enumerated values: Copy, Replaced. Default is Copy.
// If it is marked as Copy, the file is copied directly, with the user metadata in header ignored;
// If it is marked as Replaced, the metadata is modified based on the Header information.
// If the destination path and the source path are the same (that is, the user attempts to modify the metadata), the value must be Replaced
void SetXCosMetadataDirective(const std::string& str);

// The operation is performed if the Object is modified after the specified time, otherwise error code 412 is returned.
// It can be used with x-cos-copy-source-If-None-Match. Using it with other conditions can cause a conflict.
void SetXCosCopySourceIfModifiedSince(const std::string& str);

// The action is performed if the Object has not been modified after the specified time, otherwise error code 412 is returned.
// It can be used with x-cos-copy-source-If-Match. Using it with other conditions can cause a conflict.
void SetXCosCopySourceIfUnmodifiedSince(const std::string& str);

// The operation is performed if the Etag of Object is the same as the given one, otherwise error code 412 is returned.
// It can be used with x-cos-copy-source-If-Unmodified-Since. Using it with other conditions can cause a conflict.
void SetXCosCopySourceIfMatch(const std::string& str);

// The operation is performed if the Etag of Object is different from the given one, otherwise error code 412 is returned.
// It can be used with x-cos-copy-source-If-Modified-Since. Using it with other conditions can cause a conflict.
void SetXCosCopySourceIfNoneMatch(const std::string& str);

// x-cos-storage-class, which is used to set the storage class of Object. Enumerated values: STANDARD, STANDARD_IA
// Default: STANDARD (supported only in South China region)
void SetXCosStorageClass(const std::string& storage_class);

// Defines the ACL attribute of Object. Valid values: private, public-read-write, public-read.
// Default: private
void SetXCosAcl(const std::string& str);

// Grants read permission to the authorized user. Format: x-cos-grant-read: id=" ",id=" ".
// For authorization to a sub-account, id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantRead(const std::string& str);

// Grants write permission to the authorized user. Format: x-cos-grant-write: id=" ",id=" "./
//For authorization to a sub-accountid="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantWrite(const std::string& str);

// Grants read and write permissions to the authorized user. Format: x-cos-grant-full-control: id=" ",id=" ".
// For authorization to a sub-account,id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>",
// For authorization to a root account, id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"
void SetXCosGrantFullControl(const std::string& str);

// The header information that can be defined by users, which is returned as Object metadata. The size is limited to 2 KB.
void SetXCosMeta(const std::string& key, const std::string& value);

/// Sets the algorithm used by server for encryption. AES256 is supported.
void SetXCosServerSideEncryption(const std::string& str);
```

```
// Returns the MD5 algorithm check value for the file. ETag value can be used to check whether the Object content has changed.
std::string GetEtag();

// Returns the last modification time of the file in GMT format
std::string GetLastModified();

// Returns the version number
std::string GetVersionId();

/// Algorithm used by server for encryption
std::string GetXCosServerSideEncryption();
```

#### Example
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

