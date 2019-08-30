

利用 COS Select，您可以使用简单的结构化查询语言（SQL）语句筛选 COS 对象的内容，以便仅检索所需的部分数据。通过使用 COS Select 筛选此数据，您可以减少 COS 传输的数据量，这将降低检索此数据所需的成本和延迟。

COS Select 适用于以 CSV、JSON  格式存储的对象，还适用于通过 GZIP 或 BZIP2 压缩的对象（仅对于 CSV 和 JSON 对象）和服务器端加密的对象。可以将结果的格式指定为 CSV 或 JSON，并且可以确定结果中记录的分隔方式。                      

您可以在请求中将 SQL 表达式传递给 COS。有关 COS Select 支持的 SQL 元素的更多信息，请参见 [SQL 函数](https://cloud.tencent.com/document/product/436/37637) 文档。

您可以使用 COS  SDK、SELECT Object Content API、COSCMD 或 COS 控制台执行 SQL 查询。使用 COS 控制台进行文件检索存在一定限制：最大支持检索128M文件，返回的数据量限定为40MB。若需检索更多数据，请使用其他方式进行。

## 要求和限制

以下是使用 COS Select 的要求：

- 您必须拥有所查询对象的 cos:GetObject 权限。                               
- 如果您查询的对象已使用客户提供的加密密钥（SSE-C）进行加密，则必须使用 HTTPS，并且您必须在请求中提供加密密钥。                               

使用 COS Select 时存在以下限制：

- SQL 表达式的最大长度为256KB。
- 结果中记录的最大长度为1MB。


## 发起请求

在发起请求时，您可以通过使用 InputSerialization 参数指定待查询对象的格式、分隔符等信息，通过 OutputSerialization 参数指定返回结果的格式、分隔符等信息。

有关发起 COS Select 请求的详细信息，请参见 [SELECT Object Content](https://cloud.tencent.com/document/product/436/37641) API 文档。


## 常见问题

如果在尝试执行查询时遇到问题，COS Select 将返回错误代码和关联的错误消息。有关错误代码和描述的列表，请参见 [特殊错误码](https://cloud.tencent.com/document/product/436/37641#errorcode)。                      
