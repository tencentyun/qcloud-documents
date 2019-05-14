## 概述

本文将为您介绍请求出错时返回的错误码和对应错误信息。

## 错误信息返回格式

### 返回头部

Content-Type：application/xml

对应 HTTP 状态码：3XX，4XX，5XX

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

| 元素名称  | 描述                                                         | 类型      |
| --------- | ------------------------------------------------------------ | --------- |
| Error     | 包含所有的错误信息                                         | Container |
| Code      | 错误码用来定位唯一的错误条件，用来确定错误场景，具体错误码见下文 | String    |
| Message   | 包含具体的错误信息                                         | String    |
| Resource  | 资源地址：Bucket 地址或者 Object 地址                         | String    |
| RequestId | 当请求发送时，服务端将会自动为请求生成一个唯一的 ID，使用遇到问题时，request-id 能更快地协助 COS 定位问题 | String    |
| TraceId   | 当请求出错时，服务端将会自动为这个错误生成一个唯一的 ID，使用遇到问题时，trace-id 能更快地协助 COS 定位问题。当请求出错时，trace-id 与 request-id 一一对应 | String    |

## 错误码列表

**3XX 类型错误**

| 错误码            | 描述                                                         | HTTP状态码            |
| ----------------- | ------------------------------------------------------------ | --------------------- |
| PermanentRedirect | 该资源已经被永久改变了位置，请利用 HTTP Location 来重定向到正确的新位置 | 301 Moved Permanently |
| TemporaryRedirect | 该资源已经被临时改变了位置，请利用 HTTP Location 来重定向到正确的新位置 | 302 Moved Temporarily |
| Redirect          | 临时重定向                                                   | 307 Moved Temporarily |
| TemporaryRedirect | 在 DNS 更新期间，您将被临时重定向                              | 307 Moved Temporarily |

**4XX 类型错误**

| 错误码                              | 描述                                                         | HTTP 状态码                         |
| ----------------------------------- | ------------------------------------------------------------ | ----------------------------------- |
| AppendPositionErr                   | Append 操作时，文件长度和 Position 不一致                       | 400 Bad Request                     |
| AttachmentFull                      | ACL 和 Policy 数量到达上限                                      | 400 Bad Request                     |
| BadDigest                           | 提供的 Content-MD5 值与服务端收到的文件 MD5 值不一致              | 400 Bad Request                     |
| EntityTooLarge                      | 上传的文件大小超过规定的最大值                               | 400 Bad Request                     |
| EntityTooSmall                      | 上传的文件大小 不足规定的最小值，常见于分块上传              | 400 Bad Request                     |
| IncorrectNumberOfFilesInPostRequest | Post 请求每次只允许上传一个文件                               | 400 Bad Request                     |
| InvalidArgument                     | 请求参数不合法                                               | 400 Bad Request                     |
| InvalidBucketName                   | Bucket 名称不合法                                             | 400 Bad Request                     |
| InvalidCopySource                   | 不合法的复制源                                               | 400 Bad Request                     |
| InvalidDigest                       | 给定的 Content-MD5 值不合法                                    | 400 Bad Request                     |
| InvalidPart                         | 分块缺失                                                     | 400 Bad Request                     |
| InvalidPartOrder                    | 分块上传编号不连续                                           | 400 Bad Request                     |
| InvalidRegionName                   | 不合法的 Region 名                                             | 400 Bad Request                     |
| InvalidRequest                      | 请求不合法                                                   | 400 Bad Request                     |
| InvalidSHA1Digest                   | 请求内容 SHA1 校验不合法                                       | 400 Bad Request                     |
| InvalidURI                          | URI 不合法                                                    | 400 Bad Request                     |
| KeyTooLong                          | Key 过长                                                      | 400 Bad Request                     |
| LifeCycleIdNotUnique                | 生命周期 ID 不唯一                                             | 400 Bad Request                     |
| LifeCycleRuleConflicted             | 生命周期设置存在冲突                                         | 400 Bad Request                     |
| MalformedPOSTRequest                | 该 POST 请求的 Body 内容不合法                                   | 400 Bad Request                     |
| MalformedXML                        | Body 的 XML 格式不符合 XML 语法                                   | 400 Bad Request                     |
| MissingAppid                        | 请求头中缺少 Appid                                            | 400 Bad Request                     |
| MissingContentMD5                   | 请求头中缺少 Content-MD5                                      | 400 Bad Request                     |
| MissingHost                         | 请求头中缺少 Host                                             | 400 Bad Request                     |
| MissingRequestBodyError             | 请求 Body 缺失                                                 | 400 Bad Request                     |
| MultiBucketNotSupport               | 跨区域复制只能设一个目的 Bucket                               | 400 Bad Request                     |
| NoSuchUpload                        | 分块上传时指定的 uploadid 不存在                               | 400 Bad Request                     |
| NoSuchVersion                       | 指定版本不存在                                               | 400 Bad Request                     |
| NotSupportedStorageClass            | 指定的存储类型不支持                                         | 400 Bad Request                     |
| ObjectNotAppendable                 | 指定的文件不能追加                                           | 400 Bad Request                     |
| PolicyFull                          | ACL 和 Policy 数量到达上限                                      | 400 Bad Request                     |
| RequestTimeOut                      | 读取数据超时，检查网络是否过慢或上传并发数过大               | 400 Bad Request                     |
| TooManyBuckets                      | Bucket 数目达到上限 200                                        | 400 Bad Request                     |
| UnexpectedContent                   | 请求不支持相关内容                                           | 400 Bad Request                     |
| VerifyAlgorithmNotSupported         | 校验算法不支持                                               | 400 Bad Request                     |
| WebsiteURLInvalid                   | 自定义域名 URL 不合法                                          | 400 Bad Request                     |
| XMLSizeLimit                        | XML 长度超过限制                                              | 400 Bad Request                     |
| AccessDenied                        | 签名或者权限不正确，拒绝访问                                 | 403 Forbidden                       |
| ExpiredToken                        | 签名串已过期                                                 | 403 Forbidden                       |
| InvalidAccessKeyId                  | SecretID 不存在                                               | 403 Forbidden                       |
| InvalidObjectState                  | 请求内容与 Object 属性相冲突                                   | 403 Forbidden                       |
| InvalidObjectStorage                | 不合法的存储类型                                             | 403 Forbidden                       |
| RequestTimeTooSkewed                | 本地时间与服务器时间相差过大，超过15分钟                     | 403 Forbidden                       |
| SignatureDoesNotMatch               | 客户端计算的签名与 COS 服务端计算的签名不一致                  | 403 Forbidden                       |
| NoSuchBucket                        | 指定的 Bucket 不存在                                           | 404 Not Found                       |
| NoSuchCopySource                    | 复制源不存在                                                 | 404 Not Found                       |
| NoSuchKey                           | 指定的 Key 不存在                                              | 404 Not Found                       |
| NoSuchTagSet                        | 指定的 TagSet 不存在                                           | 404 Not Found                       |
| NoSuchUpload                        | 指定的分块上传不存在                                         | 404 Not Found                       |
| NoSuchWebsiteConfiguration          | 自定义域名配置不存在                                         | 404 Not Found                       |
| MethodNotAllowed                    | 此资源不支持该 HTTP 方法                                       | 405 Method Not Allowed              |
| RestoreNonArchiveObject             | 不允许对非归档对象进行回热                                   | 405 Method Not Allowed              |
| BucketAlreadyExists                 | CreateBucket 指定的 BucketName 已经存在，请选择新的 BucketName   | 409 Conflict                        |
| BucketAlreadyExistsDiffRegion       | CreateBucket 指定的 BucketName 已经存在于其他地域               | 409 Conflict                        |
| BucketAlreadyOwnedByYou             | CreateBucket 指定的 BucketName 已经使用，请选择新的 BucketName   | 409 Conflict                        |
| BucketNotEmpty                      | DeleteBucket 前请先删除 Bucket 内存在的文件和未完成的分块上传任务 | 409 Conflict                        |
| InvalidBucketState                  | Bucket 状态与操作请求冲突，比如多版本管理与跨区域复制的冲突   | 409 Conflict                        |
| PathConflict                        | 存在同名文件的毫秒级并发冲突                                 | 409 Conflict                        |
| RestoreAlreadyInProgress            | 该对象正在回热中                                             | 409 Conflict                        |
| MissingContentLength                | Content-Length 请求头部缺失                                   | 411 Length Required                 |
| PreconditionFailed                  | 前置条件匹配失败                                             | 412 Precondition                    |
| InvalidRange                        | 请求的文件范围不合法                                         | 416 Requested Range Not Satisfiable |
| UnavailableForLegalReasons          | 因法律原因不可用                                             | 451 Unavailable For Legal   Reasons |

**5XX 类型错误**

| 错误码             | 描述                       | HTTP状态码              |
| ------------------ | -------------------------- | ----------------------- |
| InternalErrror     | 服务端内部错误             | 500 Internal Server     |
| NotImplemented     | Header 中存在无法处理的方法 | 501 Not Implemented     |
| ServiceUnavailable | 服务器内部错误，请重试     | 503 Service Unavailable |
| SlowDown           | 请降低访问频率             | 503 Slow Down           |
