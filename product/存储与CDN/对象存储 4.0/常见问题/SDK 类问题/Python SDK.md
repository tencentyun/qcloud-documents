### COS Python SDK 升级后，无法执行“移动文件”操作，该如何处理？

移动文件是 COS V4 的接口，COS V5 不支持。您可以采用 [PUT Object](https://cloud.tencent.com/document/product/436/10881) 和 [DELETE Object](https://cloud.tencent.com/document/product/436/7743) 接口实现。建议您在执行删除操作前校验数据的一致性。详细介绍请参见 [MD5校验](https://cloud.tencent.com/document/product/436/36427) 文档。

### COS Python SDK 如何获取下载文件的临时链接？

Python SDK 提供获取签名、获取请求预签名 URL 接口以及获取对象下载预签名 URL 接口。使用永久密钥或临时密钥获取预签名 URL 的调用方法相同，使用临时密钥时，需要在 header 或 query_string 中加上 x-cos-security-token。详情请参见 [预签名 URL](https://cloud.tencent.com/document/product/436/35153) 文档。

### 使用 COS Python SDK 时出现异常，该如何处理？

COS XML Python SDK 操作成功会返回一个 dict 或者 None。若调用 SDK 接口请求 COS 服务失败，系统将抛出 CosClientError（客户端异常）或者 CosServiceError（服务端异常）。

- 服务端返回的错误：指服务端处理一些不符合要求的客户端请求所返回的错误。例如访问不存在的文件，没有文件的访问权限等。更多服务端返回的错误码详细信息，请参见 [API 错误码](https://cloud.tencent.com/document/product/436/7730)。
- 客户端错误：主要指网络异常、文件读写 IO 异常、参数校验失败等。

