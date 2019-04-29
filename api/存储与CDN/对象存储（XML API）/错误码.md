## 概述

此文将为您介绍请求出错时返回的错误码和对应错误信息。

## 错误信息返回格式

### 返回头部

Content-Type：application/xml

对应HTTP状态码：3XX，4XX，5XX

### 返回内容

**语法格式**

```XML
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>[错误码]</Code>
  <Message>[错误信息]</Message>
  <Resource>[资源地址]</Resource>
  <RequestId>[请求ID]</RequestId>
  <TraceId>[错误ID]</TraceId>
</Error>
```
<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

**元素说明**

| 元素名称      | 描述                                       | 类型        |
| --------- | ---------------------------------------- | --------- |
| Error     | 包含所有的错误信息。                               | Container |
| Code      | 错误码用来定位唯一的错误条件，用来确定错误场景，具体错误码见下文。        | String    |
| Message   | 包含具体的错误信息。                               | String    |
| Resource  | 资源地址：Bucket地址或者Object地址。                 | String    |
| RequestId | 当请求发送时，服务端将会自动为请求生成一个唯一的 ID。使用遇到问题时，request-id能更快地协助 COS 定位问题。 | String    |
| TraceId   | 当请求出错时，服务端将会自动为这个错误生成一个唯一的 ID。使用遇到问题时，trace-id能更快地协助 COS 定位问题。当请求出错时，trace-id与request-id一一对应。 | String    |

## 错误码列表

**3XX类型错误**

| 错误码               | 描述                                       | HTTP状态码               |
| ----------------- | ---------------------------------------- | --------------------- |
| PermanentRedirect | 该资源已经被永久改变了位置，请利用HTTP Location来重定向到正确的新位置 | 301 Moved Permanently |
| TemporaryRedirect | 该资源已经被临时改变了位置，请利用HTTP Location来重定向到正确的新位置 | 302 Moved Temporarily |
| Redirect          | 临时重定向                                    | 307 Moved Temporarily |
| TemporaryRedirect | 在DNS更新期间，您将被临时重定向                        | 307 Moved Temporarily |

**4XX类型错误**

| 错误码                                 | 描述                                | HTTP 状态码                             |
| ----------------------------------- | --------------------------------- | ----------------------------------- |
| InvalidSHA1Digest                        | 请求内容sha1校验不合法                        | 400 Bad Request  |
| NoSuchUpload                        |	分块上传时指定的uploadid不存在                    | 400 Bad Request  |
| InvalidPart                         |  分块缺失                                       | 400 Bad Request  |
| InvalidPartOrder                      | 分块上传编号不连续                               | 400 Bad Request  |
| ObjectNotAppendable                  | 指定的文件不能追加                               | 400 Bad Request  |
| AppendPositionErr                     | Append:文件长度和position不一致                 | 400 Bad Request  |
| NoSuchVersion                        | 指定版本不存在                                   | 400 Bad Request  |
| NoLifecycle                          | 生命周期不存在                                   | 400 Bad Request  |
| PreconditionFailed                   | 前置条件匹配失败                                  | 400 Bad Request  |
| UnexpectedContent                    | 请求不支持相关内容                                | 400 Bad Request  |
| MultiBucketNotSupport                 | 跨区域复制只能设一个目的bucket                    | 400 Bad Request  |
| NotSupportedStorageClass              | 指定的存储类型不合法                              | 400 Bad Request  |
| BadDigest                           | 提供的x-cos-SHA-1值与服务端收到的文件SHA-1值不符合 | 400 Bad Request                     |
| EntityTooSmall                      | 上传的文件大小 不足要求的最小值，常见于分片上传          | 400 Bad Request                     |
| EntityTooLarge                      | 上传的文件大小超过要求的最大值                   | 400 Bad Request                     |
| ImcompleteBody                      | 请求的实际内容长度和指定的Conent-Length不符            | 400 Bad Request                     |
| IncorrectNumberOfFilesInPostRequest | Post请求每次只允许上传一个文件                 | 400 Bad Request                     |
| InlineDataTooLarge                  | 内链数据大小高于要求的最大值                    | 400 Bad Request                     |
| InvalidArgument                     | 请求参数不合法                   | 400 Bad Request                     |
| InvalidBucketName                   | Bucket名称不合法                       | 400 Bad Request                     |
| InvalidDigest                       | x-cos-SHA-1值不合法                   | 400 Bad Request                     |
| InvalidPart                         | 分片缺失或者SectionID出错                 | 400 Bad Request                     |
| InvalidPolicyDocunment              | 策略配置文件不合法                         | 400 Bad Request                     |
| InvalidURI                          | URI不合法                            | 400 Bad Request                     |
| KeyTooLong                          | 自定义头部过长                            | 400 Bad Request                     |
| MalformedACLError                   | 描述的ACL策略不符合XML语法                  | 400 Bad Request                     |
| MalformedPOSTRequest                | 该POST请求的Body内容不合法         | 400 Bad Request                     |
| MalformedXML                        | body的XML格式不符合XML语法                 | 400 Bad Request                     |
| MaxMessageLengthExceeded            | 请求过长                              | 400 Bad Request                     |
| MaxPostPreDataLengthExceededError   | 该POST请求的数据前缀过长，常见于分片上传            | 400 Bad Request                     |
| MatadataTooLarge                    | 元数据大小超过要求的最大值                     | 400 Bad Request                     |
| MissingRequestBodyError             | 请求Body缺失                          | 400 Bad Request                     |
| MissingSecurityHeader               | 必要Header缺失                        | 400 Bad Request                     |
| MissingContentMD5             | 请求头中缺少Content-MD5                         | 400 Bad Request                     |
| MissingAppid                  |   请求头中缺少Appid  | 400 Bad Request                     |
| MissingHost                   |  请求头中缺少Host    | 400 Bad Request                     |
| RequestIsNotMultiPartContent        | Post请求 Content-Type不合法            | 400 Bad Request                     |
| RequestTimeOut                      | 读取数据超时，检查网络是否过慢或上传并发数过大          | 400 Bad Request           |
| TooManyBucket                       | bucket数量超过200限制                       | 400 Bad Request                     |
| UnexpectedContent                   | 请求不支持相关内容                         | 400 Bad Request                     |
| UnresolvableGrantByUID              | 提供的UID不存在                         | 400 Bad Request                     |
| UserKeyMustBeSpecified              | 针对Bucket的Post操作必须指定明确路径           | 400 Bad Request                     |
| ExpiredToken                       | 签名串已过期                                 | 403 Forbidden                       |
| AccessDenied                        | 签名或者权限不正确，拒绝访问                 | 403 Forbidden                       |
| AccountProblem                     | 您的账号拒绝了此次操作                       | 403 Forbidden                       |
| InvaildAccessKeyId                  | AccessKey不存在                      | 403 Forbidden                       |
| InvalidObjectState                  | 请求内容与Object属性相冲突                  | 403 Forbidden                       |
| InvalidSecurity                     | 签名串不合法                            | 403 Forbidden                       |
| RequestTimeTooSkewed                | 请求时间超过权限有效时间                      | 403 Forbidden                       |
| SignatureDoesNotMatch               | 提供的签名不符合规则                  | 403 Forbidden                       |
| NoSuchBucket                        | 指定的Bucket不存在                      | 404 Not Found                       |
| NoSuchUpload                        | 指定的分片上传不存在                        | 404 Not Found                       |
| NoSuchBucket                        | 指定的Bucket策略不存在                    | 404 Not Found                       |
| MethodMotAllowed                    | 此资源不支持该HTTP方法                     | 405 Method Not Allowed              |
| BucketAlreadyExists                 | CreateBucket指定的BucketName已经使用，请选择新的BucketName               | 409 Conflict                        |
| BucketNotEmpty                      | DeleteBucket前请先删除文件和未完成的分片上传任务                    | 409 Conflict                        |
| InvalidBucketState                  | bucket状态与操作请求冲突，比如多版本管理与跨区域复制的冲突                  | 409 Conflict                        |
| OperationAborted                    | 指定资源不支持此类操作或者文件传输不完整，有损坏，当下载的时候会报该错误码          | 409 Conflict   |
| MissingContentLength                | Header Content-Length缺失           | 411 Length Required                 |
| PreconditionFailed                  | 前置条件匹配失败                          | 412 Precondition                    |
| InvalidRange                        | 请求的文件范围不合法                        | 416 Requested Range Not Satisfiable |



**5XX类型错误**

| 错误码                | 描述               | HTTP状态码                 |
| ------------------ | ---------------- | ----------------------- |
| InternalErrror     | 服务端内部错误          | 500 Internal Server     |
| NotImplemented     | Header中存在无法处理的方法 | 501 Not Implemented     |
| ServiceUnavailable | 服务器内部错误，请重试   | 503 Service Unavailable |
| SlowDown           | 请降低访问频率          | 503 Slow Down           |

**其他类型错误**

| 错误码                     | 描述         | HTTP状态码 |
| ----------------------- | ---------- | ------- |
| InvaildAddressingHeader | 必须使用匿名角色访问 | N/A     |

