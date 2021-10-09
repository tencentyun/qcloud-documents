## 简介
C++ SDK 提供生成签名和获取请求预签名 URL 接口，详细操作请查看本文说明和示例。

>?
> - 建议用户使用临时密钥生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄漏目标存储桶或对象之外的资源。
> - 如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。
>



## 生成签名

### 功能说明

计算并生成签名。

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

返回签名字符串，可以在指定的有效期内（通过 CosSysConfig 设置，默认60s）使用，返回空串表示计算签名失败。

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
| http_method     | HTTP 方法，如 POST/GET/HEAD/PUT 等，传入大小写不敏感 | String                    |
| in_uri          | HTTP uri                                             | String                    |
| headers         | HTTP header 的键值对                                 | map &lt;string,string&gt; |
| params          | HTTP params 的键值对                                 | map &lt;string,string&gt; |
| start_time_in_s | 签名生效的开始时间                                   | uint64_t                  |
| end_time_in_s   | 签名生效的截止时间                                   | uint64_t                  |

#### 返回结果说明

返回签名字符串，可以在指定的有效期内（通过 CosSysConfig 设置，默认60s）使用，返回空串表示计算签名失败。


## 获取请求预签名 URL 

```go
std::string GeneratePresignedUrl(const GeneratePresignedUrlReq& req)
```

### 参数说明

| 参数 | 参数描述                                    |
| ---- | ------------------------------------------- |
| req  | GeneratePresignedUrlReq，GeneratePresignedUrl 操作的请求  |

HTTP_METHOD 枚举定义如下：

```
typedef enum {
	HTTP_HEAD,
    HTTP_GET,
    HTTP_PUT,
    HTTP_POST,
    HTTP_DELETE,
    HTTP_OPTIONS
} HTTP_METHOD;
```

## 预签名请求示例
可根据 CosConfig 类设置永久密钥或临时密钥发起预签名请求，具体配置文件内容请参见 [快速入门](https://cloud.tencent.com/document/product/436/12301) 文档。

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000";
std::string object_name = "exampleobject";

// 添加存储桶名称和对象键，以及 HTTP 请求方法。
qcloud_cos::GeneratePresignedUrlReq req(bucket_name, object_name, qcloud_cos::HTTP_GET);
std::string presigned_url = cos.GeneratePresignedUrl(req); 

```
