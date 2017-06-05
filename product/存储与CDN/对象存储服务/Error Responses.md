
本文档详细介绍了 REST 错误相应信息和所有可能出现的错误代码。

## REST错误响应

当有错误时，头信息包含：

Content-Type：application / xml
适当的3xx，4xx或5xx HTTP状态代码
身体或响应还包含有关错误的信息。以下示例错误响应显示所有 REST 错误响应通用的响应元素的结构。

下表说明了 REST 错误响应元素

| 名称 | 描述 | 
|---------|---------|
| Code | 错误代码是唯一标识错误条件的字符串。它是由通过类型检测和处理错误的程序来读取和理解的。有关更多信息，[请参阅错误代码列表]()。类型：字符串　祖先：错误 | 
| Error | 所有错误元素的容器。类型：容器　祖先：无 | 
| Message| 错误信息包含英文错误状况的一般描述。它适用于人类观众。简单的程序如果遇到错误的情况，直接向最终用户显示消息，他们不知道如何或不在乎处理。具有更详尽的错误处理和正确国际化的复杂程序更有可能忽略错误消息。类型：字符串　祖先：错误 | 
| RequestId | 与错误相关联的请求的 ID。类型：字符串　祖先：错误| 
| Resource | 涉及到错误的桶或对象。类型：字符串　祖先：错误 | 

许多错误响应包含了其他的结构化数据，需要由开发人员阅读和理解来诊断程序错误。例如 你发送的 Content-MD5 头文件 和 REST PUT请求与服务器上的摘要值不匹配的话，你会收到一个 BadDigest 错误。错误响应通常包含我们计算反馈的详细摘要和你告诉我们的预期摘要信息。在开发期间，您可以使用此信息来诊断错误。在生产环境中，一个好的程序在错误日志中应该有此相关信息。

有关常规响应元素的信息，请转到[错误响应]()。

## 错误代码列表
下表列出了 COS 会出现所有错误代码。

|错误代码 | 描述 |	HTTP状态码 |SOAP故障代码前缀|
|---------|---------|---------|---------|
| AccessDenied | 拒绝访问 | 403禁止 |客户 |
| AccountProblem | 您的腾讯云帐户有一个问题，阻止操作成功完成。请使用[联系我们]()。 | 403禁止 |客户|
| AmbiguousGrantByEmailAddress | 您提供的电子邮件地址与多个帐户相关联。 | 400错误请求 |客户|
| BadDigest | 您指定的 Content-MD5 与我们收到的不一致。 | 400错误请求 |客户 |
| BucketAlreadyExists | 请求的桶名称不可用。桶命名空间由系统的所有用户共享。请选择其他名称，然后重试。| 409冲突 |客户 |
|BucketNotEmpty	|请清空存储桶再进行删除。|	409冲突|	客户|
|CredentialsNotSupported|	此请求不支持凭据。|400错误请求|	客户|
|CrossLocationLoggingProhibited	|不允许跨位置记录。一个地理位置的 Bucket 无法将信息记录到其他位置的存储桶。|	403禁止|客户|
|EntityTooSmall	|建议上传文件小于允许的最小对象大小。|400错误请求	|客户|
|EntityTooLarge	|上传文件超过允许的最大对象大小。|400错误请求	|客户|
|ExpiredToken	|您提供的令牌已过期。|	400错误请求	|客户|
|IllegalVersioningConfigurationException|	表示请求中指定的版本配置无效。|400错误请求	|客户|
|IncompleteBody	|您没有提供 Content-Length HTTP 头指定的字节数	|400错误请求|	客户|
|IncorrectNumberOfFilesInPostRequest	|POST每个请求只需要一个文件上传。|	400错误请求	|客户
|InlineDataTooLarge	|内联数据超出允许的最大大小。|	400错误请求	|客户|
|InternalError	|我们遇到内部错误。请再试一次。|	500内部服务器错误	|服务器|
|InvalidAccessKeyId	|我们的记录中不存在您提供的腾讯云访问密钥 ID。|	403禁止	|客户|
|InvalidAddressingHeader|	您必须指定匿名角色。|	N / A	|客户|
|InvalidArgument|	无效的论点	|400错误请求	|客户|
|InvalidBucketName|	指定的桶无效。|400错误请求	|客户|
|InvalidBucketState|	该请求对于桶的当前状态无效。|	409冲突|客户|
|InvalidDigest|	您指定的 Content-MD5 无效。|	400错误请求|客户|
|InvalidEncryptionAlgorithmError	|您指定的加密请求无效。有效值为 AES256。|400错误请求|客户|
|InvalidLocationConstraint	|指定的位置约束无效。有关区域的更多信息，[请参阅如何为您的桶选择一个区域]()。|400错误请求	|客户
|InvalidObjectState	|该操作对于对象的当前状态无效。|	403禁止	|客户|
|InvalidPart	|无法找到一个或多个指定的部件。该部分可能尚未上传，或指定的实体标签可能与该部分的实体标记不匹配。|	400错误请求|客户|
|InvalidPartOrder|	部件列表不是按升序排列。部件列表必须按部件号顺序指定。|400错误请求	|客户|
|InvalidPayer	|对该对象的所有访问都已禁用。|403禁止|客户|
|InvalidPolicyDocument|	表格的内容不符合政策文件中规定的条件。|	400错误请求|客户|
|InvalidRange	|请求的范围不能满足。|416请求范围不满	|客户|
|InvalidRequest	|请使用腾讯云 4-HMAC-SHA256。|400错误请求|N / A|
|InvalidRequest	|对于具有非 DNS 兼容名称的存储区，不支持 COS 传输加速。|	400错误请求|N / A|
|InvalidRequest	|在其名称中带有句点（。）的桶不支持 COS 传输加速。|400错误请求|N / A|
|InvalidRequest|	COS Transfer Acceleration 端点仅支持虚拟样式请求。|400错误请求|N / A|
|InvalidRequest	| COS 传输加速未在此存储区中配置。|400错误请	|N / A|
|InvalidRequest	|此桶上的COS Transfer Accelerate 被禁用。|	400错误请求	|N / A|
|InvalidRequest	|此桶不支持 COS 传输加速。联系腾讯云支持以获取更多信息。|400错误请求|	N / A|
|InvalidRequest	| COS 传输加速无法在此存储桶上启用。联系腾讯云支持以获取更多信息。|400错误请求|	N / A|
|InvalidSecurity	|所提供的安全凭证无效。|403禁止|客户|
|InvalidStorageClass	|您指定的存储类无效。|400错误请求|客户|
|InvalidTargetBucketForLogging|用于记录的目标桶不存在，不属于您，或者没有适当的日志传送组授权。|400错误请求	|客户|
|InvalidToken|	提供的令牌格式不正确或无效。|	400错误请求|	客户|
|InvalidURI	|无法解析指定的 URI。|	400错误请求	|客户|
|KeyTooLong	|您的密匙太长了|	400错误请求	|客户|
|MalformedACLError	|您提供的 XML 格式不正确或未验证我们发布的模式。|400错误请求|客户|
|MalformedPOSTRequest	|您的 POST 请求的正文没有格式良好的 multipart / form-data。|400错误请求	|客户|
|MalformedXML|	当用户发送配置的错误的 xml（xml不符合发布的xsd）时，会发生这种情况。错误消息是“您提供的 XML 格式不正确或没有验证我们已发布的模式”。|400错误请求|客户|
|MaxMessageLengthExceeded|	您的请求太大了	|400错误请求|	客户|
|MaxPostPreDataLengthExceededError|	上传文件之前的 POST 请求字段太大。|	400错误请求	|客户|
|MetadataTooLarge	|您的元数据标头超出允许的最大元数据大小。|400错误请求	|客户|
|MethodNotAllowed	|不允许使用指定的方法。|	405方法不允许|客户|
|MissingContentLength	|您必须提供Content-Length HTTP标头。|	411需要长度|	客户|
|MissingRequestBodyError	|当用户作为请求发送一个空的 xml 文档时，会发生这种情况。错误消息是“请求正文为空”。|400错误请求	|客户|
|MissingSecurityHeader	|您的请求缺少必需的标题。|400错误请求	|客户|
|NoLoggingStatusForKey	|没有一个键的记录状态子资源。|400错误请求	|客户|
|NoSuchBucket	|指定的桶不存在。|错误404	|客户|
|NoSuchKey	|指定的键不存在。|错误404	|客户|
|NoSuchLifecycleConfiguration	|生命周期配置不存在。|错误404	|客户|
|NoSuchUpload	|指定的多部分上传不存在。上传 ID 可能无效，或者多部分上传可能已被中止或已完成。|	错误404|客户|
|NoSuchVersion|	表示请求中指定的版本 ID 与现有版本不匹配。|错误404	|客户|
|NotImplemented|	您提供的标题意味着未实现的功能。|	501未实施	|服务器|
|NotSignedUp	|您的帐户未注册腾讯云账号。您必须先注册才能使用 COS 。您可以选择[注册与登录](https://www.qcloud.com/)	|403禁止|	客户|
|NoSuchBucketPolicy	|指定的桶没有桶策略。|错误404|	客户|
|OperationAborted|	当前正在对该资源进行冲突的条件操作。再试一次。|	409冲突	|客户|
|PermanentRedirect|	您尝试访问的存储桶必须使用指定的端点进行寻址。将所有将来的请求发送到此端点。|	301永久移动	|客户|
|PreconditionFailed	|您指定的至少一个前提条件不成立。|412前提条件失败	|客户|
|Redirect	|临时重定向	|307暂时移动	|客户|
|RestoreAlreadyInProgress	|对象还原已经在进行中。|	409冲突	|客户|
|RequestIsNotMultiPartContent	Bucket|  POST 必须是机箱型multipart / form-data。|	400错误请求	|客户|
|RequestTimeout	|与服务器的套接字连接在超时时间段内未被读取或写入。|	400错误请求	|客户|
|RequestTimeTooSkewed	|请求时间与服务器时间之间的差异太大。|403禁止|	客户|
|RequestTorrentOfBucketError	|不允许请求桶的种子文件。|400错误请求|	客户|
|SignatureDoesNotMatch|	我们计算的请求签名与您提供的签名不符。检查您的腾讯云密钥访问密钥和签名方法。有关详细信息，请参阅[ REST 身份验证]()|403禁止	|客户|
|ServiceUnavailable	|降低您的请求率。|503服务不可用	|服务器|
|SlowDown|	降低您的请求率。|	503减速|服务器|
|TemporaryRedirect	|当 DNS 更新时，您被重定向到存储桶。|307暂时移动|	客户|
|TokenRefreshRequired|	提供的令牌必须刷新。|	400错误请求|客户|
|TooManyBuckets	|您尝试创建更多的桶在允许的范围内。|400错误请求	|客户|
|UnexpectedContent	|此请求不支持内容。|	400错误请求|	客户|
|UnresolvableGrantByEmailAddress|	您提供的电子邮件地址与记录中的任何帐户不匹配。|400错误请求|	客户|
|UserKeyMustBeSpecified	|桶 POST 必须包含指定的字段名称。如果指定，请检查字段的顺序。|400错误请求|客户|
