## 简介

利用 COS Select，您可以使用简单的结构化查询语言（SQL）语句筛选 COS 对象的内容，以便仅检索所需的部分数据。通过使用 COS Select 筛选此数据，您可以减少 COS 传输的数据量，这将减少检索此数据所需的成本和延迟。

COS Select 适用于以 CSV、JSON  格式存储的对象，还适用于通过 GZIP 或 BZIP2 压缩的对象（仅对于CSV 和 JSON 对象）和服务器端加密的对象。可以将结果的格式指定为 CSV 或 JSON，并且可以确定结果中记录的分隔方式。                      

您可以在请求中将 SQL 表达式传递给 COS。COS Select 支持一部分 SQL。有关 COS Select 支持的 SQL 元素的更多信息，请参见 [SQL 函数](https://cloud.tencent.com/document/product/436/37637)。

您可以使用 COS 开发工具包、SELECT Object Content REST API、COSCMD 或 COS 控制台执行 SQL 查询。COS 控制台将返回的数据量限定为40MB。若需检索更多数据，请使用 COSCMD 或 API。

## 要求和限制

以下是使用 COS Select 的要求：

- 您必须拥有所查询对象的`cos:GetObject`权限。                               
- 如果您查询的对象已使用客户提供的加密密钥（SSE-C）进行加密，则必须使用`https`，并且您必须在请求中提供加密密钥。                               

使用 COS Select 时存在以下限制：

- SQL 表达式的最大长度为256KB。
- 结果中记录的最大长度为1MB。

在将 COS Select 用于 Parquet 对象时，其他限制适用：

- COS Select 仅支持使用 GZIP 或 Snappy 的列式压缩。COS Select 对于 Parquet 对象不支持整个对象压缩。
- COS Select 不支持 Parquet 输出。您必须将输出格式指定为 CSV 或 JSON。
- 最大未压缩块大小为256MB。
- 最大列数为100。
- 您必须使用在对象的架构中指定的数据类型。
- 选择重复字段将只返回最后一个值。

## 构建请求

在构建请求时，您需提供通过使用`InputSerialization`对象查询的对象的详细信息。您提供要使用 `OutputSerialization` 对象返回结果的方式的详细信息。您还包含 COS 将用于筛选请求的 SQL 表达式。                      

有关构建 COS Select 请求的更多信息，请参见 [SELECT Object Content](https://cloud.tencent.com/document/product/436/37641) API 文档。                   

## 常见问题

如果在尝试执行查询时遇到问题，COS Select 将返回错误代码和关联的错误消息。有关错误代码和描述的列表，请参见 [特殊错误码](#)。                      
