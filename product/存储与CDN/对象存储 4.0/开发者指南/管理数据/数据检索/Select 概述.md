COS Select 功能通过结构化查询语句（SQL）筛选存储在 COS 上的对象，以便检索对象并获取用户所需的数据。通过 COS  Select 功能筛选对象数据，您可以减少 COS 传输的数据量，这将降低检索此数据所需的成本和延迟。

COS Select 功能目前支持检索以 CSV、JSON 和 Parquet 格式存储的对象，支持检索通过 GZIP 或 BZIP2 压缩的对象（仅对于 CSV、JSON 格式的对象）。此外，COS Select 功能还支持将结果的格式指定为 CSV 或 JSON，并且可以确定结果中记录的分隔方式。

您可以在请求中将 SQL 表达式传递给 COS。COS Select 目前只支持部分 SQL 表达式。有关 COS Select 支持的 SQL 表达式的更多信息，请参见 [SQL 函数](https://cloud.tencent.com/document/product/436/37637) 文档。

您可以使用 COS 控制台、API、SDK、COSCMD 等方式执行 SQL 查询。需要注意，使用 COS 控制台进行文件检索存在一定限制：最大支持检索128M文件，返回的数据量限定为40MB。若需检索更多数据，请使用其他方式进行。

>?
>- COS Select 所支持的数据类型和当前的保留字段，请参见 [数据类型](https://cloud.tencent.com/document/product/436/37639) 和 [保留字段](https://cloud.tencent.com/document/product/436/37638) 了解详情。
>- 目前检索功能仅支持中国大陆公有云地域，其他地域暂不支持此功能。

## 使用限制

使用 COS Select 时存在以下限制：

- 您必须拥有所查询对象的 `cos:GetObject` 权限，主账号默认拥有该权限。
- 仅支持标准存储类型的对象检索。
- SQL 表达式的最大长度为256KB。
- 检索结果中单条记录的最大长度为1MB。

COS Select 功能目前支持的 SQL 子句：

- SELECT 语句
- FROM 子句
- WHERE 子句
- LIMIT 子句

>?有关 SQL 子句的详细信息，请参见 [Select 命令](https://cloud.tencent.com/document/product/436/37636)。

COS Select 目前支持的函数例如下：

- 聚合函数：例如 AVG 函数、COUNT 函数、MAX 函数、MIN 函数、SUM 函数。
- 条件函数：例如 COALESCE 函数、NULLIF 函数。
- 转换函数：例如 CAST 函数。
- 日期函数：例如 DATE_ADD 函数、DATE_DIFF 函数、EXTRACT 函数、TO_STRING 函数、TO_TIMESTAMP 函数、UTCNOW 函数。
- 字符串函数：例如 CHAR_LENGTH 函数、CHARACTER_LENGTH 函数、LOWER 函数、SUBSTRING 函数、TRIM 函数、UPPER 函数。

>?有关 SQL 函数的详细信息，请参见 [SQL 函数](https://cloud.tencent.com/document/product/436/37637)。

COS Select 目前支持以下运算符：

- 逻辑运算符：`AND，NOT，OR`
- 比较运算符：`<，>，<=，>=，=，<>，!=，BETWEEN，IN`
- 模式匹配运算符：`LIKE`
- 数学运算符：`+，-，*，%`

>?有关运算符的详细信息，您可以参见 [运算符](https://cloud.tencent.com/document/product/436/37640)。



## 发起检索请求

您可以使用控制台、API、SDK 等多种方式发起检索请求：

- 使用控制台，您可参见 [检索数据](https://cloud.tencent.com/document/product/436/37642) 文档进行操作。
- 使用 API，请参见 [SELECT Object Content](https://cloud.tencent.com/document/product/436/37641) API 文档。
- 使用 SDK，您可以前往 [SDK 概览](https://cloud.tencent.com/document/product/436/6474) 选择所需的 SDK 接口。


## 常见问题

如果在尝试执行查询时遇到问题，COS Select 将返回错误代码和关联的错误消息。有关错误代码和描述的列表，请参见 [特殊错误码](https://cloud.tencent.com/document/product/436/37641#errorcode)。                      


