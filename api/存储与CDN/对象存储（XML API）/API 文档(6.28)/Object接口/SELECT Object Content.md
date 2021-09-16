## 概述

COS Select 接口可以使用结构化查询语句（Structured Query Language，SQL）从指定对象（CSV、JSON 或者 Parquet 格式）中检索内容。在检索过程中，您需要指定对象内容的分隔符，并使用合适的 SQL 函数进行检索，COS Select 将返回相匹配的检索结果，您可以指定检索结果的保存格式。

如您需要了解 COS Select 的更多介绍，请参见 COS [Select 概述](https://cloud.tencent.com/document/product/436/37635)。有关 COS Select 的 SQL 表达式的介绍，您可以在开发者指南中参见 [Select 命令](https://cloud.tencent.com/document/product/436/37636) 进一步了解。

>!Select Object Content 接口当前仅支持 virtual-hosted 方式访问，不支持 path-style 方式访问。

#### 权限限制

使用 COS Select，您必须具有`cos:GetObject`的授权。

- 如果您是主账号，则默认拥有该权限。
- 如果您是子账号，请联系您的主账号获取该操作的权限。有关权限设置，请参见 [授权子账号访问 COS](https://cloud.tencent.com/document/product/436/11714) 文档。

#### 对象数据格式

COS Select 支持检索以下格式的对象数据：

- CSV 格式：对象以 CSV 格式存储，并以固定的分隔符划分。
- JSON 格式：对象以 JSON 格式存储，可以是 JSON 文件或者 JSON 列表。
- Parquet 格式：对象以 Parquet 格式存储，可以包含嵌套结构。

> !
>- COS Select 的对象必须以 UTF-8 格式编码。
>- COS Select 支持检索 GZIP 或者 BZIP2 压缩的 CSV、JSON 对象；支持检索经过 GZIP 或 Snappy 列压缩的 Parquet 对象。
>- COS Select 支持检索 SSE-COS 加密的对象。

## 请求

#### 请求示例

```shell
POST /<ObjectKey>?select&select-type=2 HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: date
Authorization: Auth String

Request body
```

>?
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 请求参数中 select 和 select-type=2 参数均为必填参数，其中 select 代表发起 select 请求，select-type=2 代表这一接口的版本信息。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

以下请求展示了用户发起一个 COS Select 请求，检索 CSV 格式对象的所有内容，并将结果保存为 CSV 格式对象。 

```shell
<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from COSObject</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>GZIP</CompressionType>
        <CSV>
            <FileHeaderInfo>IGNORE</FileHeaderInfo>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
            <Comments>#</Comments>
            <AllowQuotedRecordDelimiter>FALSE</AllowQuotedRecordDelimiter>
        </CSV>
    </InputSerialization>
    <OutputSerialization>
        <CSV>
            <QuoteFields>ASNEEDED</QuoteFields>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        </CSV>
    </OutputSerialization>
    <RequestProgress>
        <Enabled>FALSE</Enabled>
    </RequestProgress>
</SelectRequest> 
```

以下请求展示了用户发起一个 COS Select 请求，检索 JSON 格式对象的所有内容，并将结果保存为 JSON 格式对象。                    

```shell
<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from COSObject</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>GZIP</CompressionType>
        <JSON>
            <Type>DOCUMENT</Type>
        </JSON>
    </InputSerialization>
    <OutputSerialization>
        <JSON>
            <RecordDelimiter>\n</RecordDelimiter>
        </JSON>                                  
    </OutputSerialization>
    <RequestProgress>
        <Enabled>FALSE</Enabled>
    </RequestProgress>                                  
</SelectRequest> 
```

以下请求展示了用户发起一个 COS Select 请求，检索 Parquet 格式对象的所有内容，并将结果保存为 JSON 格式对象。

```shell
<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from COSObject</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>GZIP</CompressionType>
        <Parquet>
        </Parquet>
    </InputSerialization>
    <OutputSerialization>
        <JSON>
            <RecordDelimiter>\n</RecordDelimiter>
        </JSON>                                  
    </OutputSerialization>
    <RequestProgress>
        <Enabled>FALSE</Enabled>
    </RequestProgress>                                  
</SelectRequest> 
```





>?
>- InputSerialization 元素描述了待检索的对象格式，为必填参数，该参数可以指定为 CSV 、JSON 或 Parquet 格式。
>- OutputSerialization 元素描述了检索结果的保存格式，该参数可以仅可指定为 CSV 或者 JSON 格式。
>- 待检索的对象格式无需和检索结果的保存格式互相匹配，您可以检索一个 JSON 格式的对象，并将检索结果保存为 CSV 格式。

下表展示了请求体中的各项元素组成：

| 名称                | 父节点        | 描述                                                         | 类型      | 是否必选 |
| ------------------- | ------------- | ------------------------------------------------------------ | --------- | -------- |
| Expression          | SelectRequest | SQL   表达式，代表您需要发起的检索操作。例如`SELECT s._1 FROM COSObject s`。这个表达式可以从 CSV   格式的对象中检索第一列内容。有关 SQL 表达式的详细介绍，请参见 [Select 命令](https://cloud.tencent.com/document/product/436/37636) | String    | 是       |
| ExpressionType      | SelectRequest | 表达式类型，该项为扩展项，目前只支持 SQL 表达式，仅支持 SQL 参数 | String    | 是       |
| InputSerialization  | SelectRequest | 描述待检索对象的格式                                         | Container | 是       |
| OutputSerialization | SelectRequest | 描述检索结果的输出格式                                       | Container | 是       |
| RequestProgress     | SelectRequest | 是否需要返回查询进度 QueryProgress 信息，如果选中 COS Select 将周期性返回查询进度 | Container | 否       |


**InputSerialization container element**

| 名称             | 父节点             | 描述                                                         | 类型      | 是否必选 |
| :--------------- | :----------------- | :----------------------------------------------------------- | :-------- | :------- |
| CompressionType  | InputSerialization | 描述待检索对象的压缩格式： 如果对象未被压缩过，则该项为 NONE。如果对象被压缩过，COS Select 目前支持的两种压缩格式为 GZIP 和 BZIP2，可选项为 NONE、GZIP、BZIP2，默认值为 NONE | String    | 否       |
| CSV/JSON/PARQUET | InputSerialization | 描述在相应的对象格式下所需的文件参数。例如 CSV 格式需要指定分隔符 | Container | 是       |

**CSV container element (InputSerialization 子元素)**

| 名称                       | 父节点 | 描述                                                         | 类型    | 是否必选 |
| -------------------------- | ------ | ------------------------------------------------------------ | ------- | -------- |
| RecordDelimiter            | CSV    | 将 CSV 对象中记录分隔为不同行的字符，默认您通过`\n`进行分隔。您可以指定任意8进制字符，如逗号、分号、Tab 等。该参数最多支持2个字节，即您可以输入`\r\n`这类格式的分隔符。默认值为`\n `。 | String  | 否       |
| FieldDelimiter             | CSV    | 指定分隔 CSV 对象中每一行的字符，默认您通过,进行分隔。您可以指定任意8进制字符，该参数最多支持1个字节。默认值为`, `。 | String  | 否       |
| QuoteCharacter             | CSV    | 如果您待检索的 CSV 对象中存在包含分隔符的字符串，您可以使用 QuoteCharacter 进行转义，避免该字符串被切割成几个部分。如 CSV 对象中存在`"a, b" `这个字符串，双引号"可以避免这一字符串被分隔成 `a` 和 `b` 两个字符。默认值为`" `。 | String  | 否       |
| QuoteEscapeCharacter       | CSV    | 如果您待检索的字符串中已经存在`"`，那您需要使用`"`进行转义以保证字符串可以正常转义。如您的字符串 `""" a , b """`将会被解析为`" a , b  "`。默认值为"。 | String  | 否       |
| AllowQuotedRecordDelimiter | CSV    | 指定待检索对象中是否存在与分隔符相同且需要用"转义的字符。设定为 TRUE 时，COS   Select 将会在检索进行转义，这会导致检索性能下降；设定为 FALSE 时，则不会做转义处理。默认值为 FALSE。 | Boolean | 否       |
| FileHeaderInfo             | CSV    | 待检索对象中是否存在列表头。该参数为存在 NONE、USE、IGNORE 三个选项。NONE 代表对象中没有列表头，USE 代表对象中存在列表头并且您可以使用表头进行检索（例如 `SELECT "name" FROM COSObject`），IGNORE 代表对象中存在列表头且您不打算使用表头进行检索（但您仍然可以通过列索引进行检索，如 `SELECT s._1 FROM COSObject s`）。合法值为 NONE、USE、IGNORE。 | Enum    | 否       |
| Comments                   | CSV    | 指定某行记录为注释行，该字符会被添加到该行记录的首字符。如果某一行记录被指定为注释，则 COS Select 将不对此行做任何分析。默认值为`#`。 | String  | 否       |

**JSON container element (InputSerialization 子元素)**

| 名称 | 父节点 | 描述                                                         | 类型 | 是否必选 |
| ---- | ------ | ------------------------------------------------------------ | ---- | -------- |
| Type | JSON   | JSON 文件的类型：<br><li>DOCUMENT 表示 JSON 文件仅包含一个独立的 JSON 对象，且该对象可以被切割成多行<br><li>LINES 表示 JSON 对象中的每一行包含了一个独立的 JSON 对象<br>合法值为 DOCUMENT 、LINES | Enum | 是       |

**OutputSerialization container element**

| 名称      | 父节点              | 描述                                              | 类型      | 是否必选                          |
| --------- | ------------------- | ------------------------------------------------- | --------- | --------------------------------- |
| CSV /JSON | OutputSerialization | 指定检索结果的输出格式，可选项为 CSV 或者 JSON | Container | 是，必须是 CSV 或者 JSON 中的一个 |

**CSV container element (OutputSerialization 子元素)**

| 名称                 | 父节点 | 描述                                                         | 类型   | 是否必选 |
| -------------------- | ------ | ------------------------------------------------------------ | ------ | -------- |
| QuoteFields          | CSV    | 指定输出结果为文件时，是否需要使用`"`进行转义。可选项包括 ALWAYS、ASNEEDED、ALWAYS 代表对所有本次输出的检索文件应用`"`，ASNEEDED 代表仅在需要时使用。合法值为 ALWAYS、ASNEEDED，默认值为 ASNEEDED。 | String | 是       |
| RecordDelimiter      | CSV    | 将输出结果中的记录分隔为不同行的字符，默认通过`\n `进行分隔。您可以指定任意8进制字符，如逗号、分号、Tab 等。该参数最多支持2个字节，即您可以输入`\r\n`这类格式的分隔符。默认值为`\n `。 | String | 否       |
| FieldDelimiter       | CSV    | 将输出结果中的每一行进行分列的字符，默认通过`,`进行分隔。您可以指定任意8进制字符，该参数最多支持1个字节。默认值为`, `。 | String | 否       |
| QuoteCharacter       | CSV    | 如果输出结果中存在包含分隔符的字符串，可以使用 QuoteCharacter 进行转义，保证该字符串不会在后续分析中被切割。如输出结果中存在`a,b`这个字符串，双引号`"`可以避免这一字符串被分隔成`a`和`b`两个字符，COS Select 将会将其转为`"a, b" `写入文件。默认值为`" `。 | String | 否       |
| QuoteEscapeCharacter | CSV    | 如果您即将输出的字符串中已经存在`"`，那您需要使用`"`进行转义以保证该字符串可以正常转义。如您的字符串`" a , b"` 将会被在写入文件时被转换为`""" a , b """`。默认值为`" `。 | String | 否       |

**JSON container element (OutputSerialization 子元素)**

| 名称            | 父节点 | 描述                                                         | 类型   | 是否必选 |
| --------------- | ------ | ------------------------------------------------------------ | ------ | -------- |
| RecordDelimiter | JSON   | 将输出结果中的记录分隔为不同行的字符，默认通过`\n `进行分隔。您可以指定任意8进制字符，如逗号、分号、Tab 等。该参数最多支持2个字节，即您可以输入`\r\n`这类格式的分隔符。默认值为`\n ` | String | 否       |

**RequestProgress container element**

| 名称    | 父节点          | 描述                                                       | 类型    | 是否必选 |
| ------- | --------------- | ---------------------------------------------------------- | ------- | -------- |
| Enabled | RequestProgress | 指定是否需要 COS Select 定期返回查询进度。默认值为 FALSE | Boolean | 否       |

## 响应

执行成功的检索操作将返回`200 OK`状态码。

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

由于响应体的大小无法预知，COS 将用户请求响应体以序列化形式展示，即将响应体切分成多个分块返回，如下展示了返回响应体的概览：

```shell
<Message 1>
<Message 2>
<Message 3>
......
<Message n>
```

#### 预响应（prelude）和响应结果（data）

COS 将检索结果切成多个分块，每个分块即一个 Message。每一个 Message 由预响应（prelude）和响应结果（data）组成。

- 预响应包含两个部分：
 - 所在分块 Message 的总长度。
  - 所有头部的总长度。
- 响应结果包含两个部分：
  - 响应报头（header）。
  - 响应正文（payload）。

预响应和响应结果均以4字节的经过大端编码（big-endian）的 CRC 校验码结尾。COS Select 使用 CRC32计算 CRC 校验码，有关 CRC32的详细信息，请参见 [RFC 文档](https://www.ietf.org/rfc/rfc1952.txt)。除了响应结果之外，COS Select 总共额外花费了16字节用于传输预响应和校验码信息。

> !所有分块 Message 中的整数值均以网络字节序，即大端编码，传输。

下图展示了分块 Message 以及检索结果中的响应报头 header 是如何构成的。每一个分块 Message 中可能包含多个 header 。
![Message construction](https://main.qcloudimg.com/raw/aeb1263d0c9af56842997327514f13aa.png)

如上图所示，每一个分块 Message 均由预响应 prelude，预响应校验码 prelude CRC（由两个记录字节数的信息组成），报头信息 header ，响应正文 Payload 和正文校验码 Message CRC 构成。从上图可以看到，整个响应体的长度计算方式如下：
```shell
响应体总长度 =  预响应长度 + 预响应校验码长度 + 响应正文长度 + 响应报头长度  + 响应正文校验码长度
```

由于校验码（prelude CRC 和 Message CRC）和预响应 prelude 总长度固定为16字节，因此响应体总长还可以通过如下方式快速计算：
```shell
响应体总长度 =  响应正文长度 + 响应报头长度 + 16
```

以下详细介绍响应体各部分组成：

| 组成&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                      | 描述                                                         |
| ------------------------- | ------------------------------------------------------------ |
| 预响应 prelude            | 分别记录了分块 Message 的总长度和所有报头的总长度，每个记录4字节，总长8字节：<br>1. `total byte-length`：所在分块 Message 的总长度，使用大端编码，包含该记录本身容量共4字节。<br>2. `headers byte-length`：所有报头的总长度，使用大端编码，不包含该记录所占空间共4字节。 |
| 预响应校验码 prelude CRC | 预响应的 CRC 校验码，使用大端编码，总共4字节。预响应校验码可以帮助程序快速识别预响应信息是否正确，减少缓冲时的阻塞。 |
| 报头信息 header          | 分块 Message 记录的检索结果的元数据信息，诸如数据类型，正文格式。根据数据类型的差异，本部分的字节长度也有所差异。响应报头以 kv 键值对形式存储，使用 UTF-8编码。响应报头中所记录的元数据信息可以以任意顺序展示，但每一项元数据仅记录一次。根据数据类型的差异，以下响应报头均有可能在 COS Select 返回的结果中出现：<br>1. `MessageType Header`：该报头代表响应类型。Key 值为":message-type"，合法的 Value 值为"error"或者"event"，"error"代表本条记录为报错信息，"event"代表本条记录为具体的事件。<br>2. `EventType Header`：该报头记录事件类型。Key 值为":event-type"，合法的 Value 值为"Records"，"Cont"，"Progress"，"Stats"或"End"。"Records"代表事件为返回检索记录，"Cont"代表事件为保持 TCP 连接，"Progress"代表事件为定期返回的检索结果，"Stats"代表事件为本次查询的统计信息，"End"代表本次查询结束。<br>3. `ErrorCode Header`：该报头记录报错类型。Key 值为":error-code"，合法的 Value 值为 [特殊错误码](#.E7.89.B9.E6.AE.8A.E9.94.99.E8.AF.AF.E7.A0.81) 中的错误码信息。<br>4. `ErrorMessage Header`：该报头记录错误码信息。Key 值为":error-message"，合法的 Value 值为服务端返回的错误码信息，可用于定位错误。 |
| 响应正文 Payload         | 记录检索结果，或者与请求相关的正式信息。                     |
| 正文校验码 Message CRC   | 使用大端编码的 CRC 校验码，总长4字节。                       |

同一个分块 Message 中可能记录了多个 header，每一个响应报头 header 由以下几部分组成：

| 组成&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                     | 描述                                                         |
| ------------------------ | ------------------------------------------------------------ |
| Header Name Byte-Length  | 记录 Header Name 的字节长度信息                              |
| Header Name              | 报头类型，合法值包括 ":message-type"， ":event-type"， ":error-code"和":error-message"<br><li>":message-type"代表该报头记录了响应类型<br><li> ":event-type"代表了该报头记录事件类型 <br><li>":error-code"代表该报头记录报错类型<br><li>":error-message"代表该报头记录错误码信息 |
| Header Value Type        | Header Value 的类型，对于 COS Select 而言这个值固定为7，代表类型为 String |
| Value String Byte-Length | Header Value 的字节长度信息，固定2字节                    |
| Header Value String      | 响应报头的正文，即响应正文的元数据信息，Header Value 的字节长度与响应类型相关 |

COS Select 的响应类型主要可以分为以下几种：

| 响应类型&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                   | 描述                                                         |
| ------------------------- | ------------------------------------------------------------ |
| Records message           | 检索信息，可以包含单条记录，部分记录或者多条记录，取决于检索结果的多少。一个响应体中可能包含多个 Records message |
| Continuation message      | 连接信息，COS Select 周期性地发送这些信息以保持 TCP 连接，这些信息随机出现在响应体中。客户端最好能够自动识别这类信息，并对其做过滤处理以免弄脏检索结果 |
| Progress message          | 进度信息，COS Select 周期性地返回这些信息以反馈当前查询进度 |
| Stats message             | 统计信息，COS Select 在查询结束后返回本次查询的相关统计信息 |
| End message               | 结束信息，代表本次查询已经结束，没有后续响应数据。只有在接受到该类型的信息时才能认为查询结束 |
| RequestLevelError message| 报错信息，COS Select 在查询出现错误时将会返回这一信息，包含请求的错误原因。如果 COS Select 返回了这一信息，则将不会再返回 End message 信息 |

下面将进一步介绍这些响应类型的详情。

#### Records message

- 报头格式
  Records message 包括":message-type"， ":event-type"， ":content-type"3种类型的报头。如下所示：
  ![Records message ](https://main.qcloudimg.com/raw/922e7b72b786ff478d022bf3a5b62166.png) 
- 正文格式
  Records message 正文可能包含单条记录，部分记录或者多条记录，取决于检索结果的多少。

#### Continuation Message

- 报头格式
  Continuation Message 包括":message-type"， ":event-type"2种类型的报头，如下所示：
  ![ Continuation Message ](https://main.qcloudimg.com/raw/46f32071a712ecf39af238629fd746fc.png) 
- 正文格式
  Continuation Message 中不包含正文内容。

#### Progress Message

- 报头格式
  Progress Message 包括":message-type"， ":event-type"， ":content-type"3种类型的报头，如下所示：
  ![Progress Message](https://main.qcloudimg.com/raw/fbbfc15950e7a063fdfa38cb349c40aa.png) 
- 正文格式
  Progress Message 的正文是一个包含了当前查询进度的 XML 文本，主要包含以下信息：
	- BytesScanned：如果文件是压缩文件，该数值代表文件解压前的字节大小。如果文件不是压缩文件，该数值即文件的字节大小。
	- BytesProcessed：如果文件是压缩文件，该数值代表文件解压后的字节大小。如果文件不是压缩文件，该数值即文件的字节大小。
	- BytesReturned：COS Select 目前返回的检索结果字节大小。

示例如下：

```shell
<?xml version="1.0" encoding="UTF-8"?>
<Progress>
     <BytesScanned>512</BytesScanned>
     <BytesProcessed>1024</BytesProcessed>
     <BytesReturned>1024</BytesReturned>
</Progress>
```

#### Stats Message

- 报头格式
  Stats Message 包括":message-type"， ":event-type"， ":content-type"3种类型的报头，如下所示：
  ![ Stats Message ](https://main.qcloudimg.com/raw/e565c09f71267eba208206fcaceaf991.png)
- 正文格式
  Stats message 的正文是一个包含了本次查询统计的 XML 文本，主要包含以下信息：
  - BytesScanned：如果文件是压缩文件，该数值代表文件解压前的字节大小；如果文件不是压缩文件，该数值即文件的字节大小。
  - BytesProcessed：如果文件是压缩文件，该数值代表文件解压后的字节大小；如果文件不是压缩文件，该数值即文件的字节大小。
  - BytesReturned：COS Select 在本次查询中返回的检索结果字节大小。

示例如下：

```shell
<?xml version="1.0" encoding="UTF-8"?>
<Stats>
     <BytesScanned>512</BytesScanned>
     <BytesProcessed>1024</BytesProcessed>
     <BytesReturned>1024</BytesReturned>
</Stats>
```

#### End Message

- 报头格式
  End messages 包括":message-type"，":event-type"2种类型的报头，如下所示：
  ![ End messages ](https://main.qcloudimg.com/raw/b079e8945f1a70aa474a0da7c7763311.png)
- 正文格式
  End messages 中不包含正文内容。

#### Request Level Error Message

- 报头格式
  Request Level Error Message 包括“:error-code”，“:error-message”，“:message-type”3种类型的报头，如下所示：
  ![ Request Level Error Message](https://main.qcloudimg.com/raw/2617ffc28532fb49f53de576e20629d4.png) 

如果您需要了解 Request Level Error Message 中记录的错误码详情，可以查看 [特殊错误码](#.E7.89.B9.E6.AE.8A.E9.94.99.E8.AF.AF.E7.A0.81)。

- 正文格式
  Request Level Error Message 信息中不包含正文内容。

<span id="errorcode"></span>
#### 特殊错误码

该请求常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档，特殊错误码信息如下所示：                     

| 错误码| 错误信息 | 含义|HTTP 状态码  |
| -- | -- | -- | -- |
| InvalidXML | The XML is invalid | XML 格式不合法 | 400 Bad Request|
| MissingRequiredParameter | The SelectRequest entity is missing a required parameter | 检索请求缺少必填参数项 | 400 Bad Request|
| MissingExpectedExpression | The SQL expression is missing | 缺少 SQL 表达式 | 400 Bad Request|
| MissingInputSerialization |  The input serialization is missing| 未指定输入 CSV 对象的数据序列化格式 | 400 Bad Request|
| InvalidCompressionFormat |  The file is not in a supported compression format. Only GZIP and BZIP2 are supported | 不合法的文件压缩格式，仅支持 GZIP 和 BZIP2 两种格式 | 400 Bad Request|
| MissingInputFormat | The input format is missing  | 缺少输入格式 | 400 Bad Request|
| InvalidFileHeaderInfo |  The input FileHeaderInfo is invalid. Only NONE, USE, and IGNORE are supported| 输入的文件表头信息不合法。仅支持 NONE，USE 和 IGNORE | 400 Bad Request|
| InvalidRequestParameter | The input RecordDelimiter of CSV is invalid  | 输入的 CSV 文件换行符不合法 | 400 Bad Request|
| InvalidRequestParameter | The input FieldDelimiter of CSV is invalid  | 输入的 CSV 文件列分隔符不合法 | 400 Bad Request|
| InvalidRequestParameter | The input QuoteCharacter of CSV is invalid  | 输入的 CSV 文件引用符不合法 | 400 Bad Request|
| InvalidRequestParameter |  The input AllowQuoteRecordDelimiter of csv is invalid. Only TRUE and FALSE are supported | 在输入 CSV 文件中启用转义符的配置不合法，仅支持 TRUE 和 FALSE | 400 Bad Request|
| InvalidJsonType |  The JsonType is invalid. Only DOCUMENT and LINES are supported| 不合法的 JSON 类型，仅支持 DOCUMENT 和 LINES | 400 Bad Request|
| MissingOutputSerialization |  The output serialization is missing. |  未指定输出 CSV 对象的数据序列格式| 400 Bad Request|
| MissingOutputFormat | The output format is missing  | 缺少输出格式 | 400 Bad Request|
| InvalidQuoteFields | The QuoteFields is invalid. Only ALWAYS and ASNEEDED are supported  | 不合法的转义规则，仅支持 ALWAYS 和 ASNEEDED | 400 Bad Request|
| InvalidRequestParameter |  The output RecordDelimiter of CSV is invalid | 输出的 CSV 文件换行符不合法 | 400 Bad Request|
| InvalidRequestParameter |  The output FieldDelimiter of CSV is invalid | 输出的 CSV 文件列分隔符不合法 | 400 Bad Request|
| InvalidRequestParameter | The output QuoteCharacter of CSV is invalid  | 输出的 CSV 文件转义符不合法 | 400 Bad Request|
| InvalidRequestParameter | The output QuoteEscapeCharacter of CSV is invalid  | 输出的 CSV 的双引号转义符不合法 | 400 Bad Request|
| InvalidRequestParameter |  The output RecordDelimiter of JSON is invalid | 输出的 JSON 文件换行符不合法 | 400 Bad Request|
| SQLParsingError | Encountered an error parsing the SQL expression  | 解析 SQL 表达式出现问题 | 400 Bad Request|
| SQLParsingError |  Other expressions are not allowed in the SELECT list when '\*' is used without dot notation. | SELECT list 不允许在未使用点符的时候使用`'*'` | 400 Bad Request|
| SQLParsingError |  The SQL expression contains an empty SELECT | SQL 表达式中包含了空的 SELECT 子句 | 400 Bad Request|
| SQLParsingError | GROUP is not supported in the SQL expression | SQL 表达式中不支持 GROUP 子句 | 400 Bad Request|
| SQLParsingError | UNION is not supported in the SQL expression | SQL 表达式中不支持 UNION 子句 | 400 Bad Request|
| SQLParsingError | FROM is missing in the SQL expression | SQL 表达式中缺少 FROM 子句 | 400 Bad Request|
| SQLParsingError | ORDER is not supported in the SQL expression | SQL 表达式中不支持 ORDER 子句 | 400 Bad Request|
| SQLParsingError | The column index is invalid in the SQL expression | SQL 表达式中指定的列索引不合法 | 400 Bad Request|
| SQLParsingError | The table alias is invalid in WHERE | WHERE 子句中的表别名不合法 | 400 Bad Request|
| Bzip2DecompressError | Encountered an error decompressing the bzip2 file | 解压 BZIP2 格式的文件时出现问题 | 400 Bad Request|
| Bzip2DecompressError |  BZIP2 is not applicable to the queried object | BZIP2 格式不适用于解压待查询对象 | 400 Bad Request|
| GzipDecompressError |  Encountered an error decompressing the gzip file | 解压 GZIP 格式的文件时出现问题 | 400 Bad Request|
| GzipDecompressError | GZIP is not applicable to the queried object  | GZIP 格式不适用于解压待查询对象 | 400 Bad Request|
| Busy |  The service is busy. Please retry later| 后端服务阻塞，请稍后重试 | 400 Bad Request|
| Overload | The service is overload. Please retry later | 后端服务过载，请稍后重试 | 400 Bad Request|
| AmbiguousFieldName |  Field name matches to multiple fields in the file| 指定的表头名称存在多个相同的值 | 400 Bad Request|
| ComparisonFailed | Attempt to compare failed | 匹配失败，请重试 | 400 Bad Request|
| CastFailed |  Attempt to convert from one data type to another using CAST failed in the SQL expression. | 在 SQL 表达式中通过 CAST 函数转换数据类型时出现错误 | 400 Bad Request|
| OverMaxRecordSize |  The length of a record in the input or result is greater than maxCharsPerRecord of 1 MB | 输入或输出的文件中，单行记录大小超过1MB限制 | 400 Bad Request|
| LastRecordParseFail |  Please check the last record in the input | 请检查输入文件的最后一行记录| 400 Bad Request|
| CSVParsingError | Encountered an error parsing the CSV file | 解析 CSV 格式文件的时候出现问题 | 400 Bad Request|
| JSONParsingError | Encountered an error parsing the JSON file  | 解析 JSON 格式文件的时候出现问题 | 400 Bad Request|
| ErrorWritingRow | Encountered an error parsing the SELECT result. Please try again  | 无法格式化您的查询结果，请检查文件并重试 | 400 Bad Request|
| InvalidRequestParameter | The input Comment of CSV is invalid  | 不合法的 CSV 文件注释符 | 400 Bad Request|
| InvalidTextEncoding | UTF-8 encoding is required. Please check the file and try again. | 检索文件和检索结果仅支持UTF-8编码 | 400 Bad Request|
| NoSuchKey | The specified key does not exist  | 指定的对象键不存在 | 404 Not Found|
| AccessDenied |  Access Denied| 签名或者权限不正确，拒绝访问 | 403 Forbidden|
| MethodNotAllowed | The specified method is not allowed against this resource | 当前资源不支持该 HTTP 方法 | 405 Method Not Allowed|
| InternalError | We encountered an internal error. Please try again  | 服务端内部错误 | 500 Internal Server|



## 示例

#### 示例 1: 从 CSV 格式的对象中检索内容

以下示例展示了调用该接口从 CSV 格式的对象中检索全部内容，并将检索结果输出为 CSV 格式的过程。待检索的对象名为`exampleobject.csv`，该对象存储于北京地域（ap-beijing）的存储桶 examplebucket-1250000000 中。

```shell
POST /exampleobject.csv?select&select-type=2 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 12 Jan 2019 11:49:52 GMT
Authorization: authorization string
Content-Length: content length

<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from COSObject</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>None</CompressionType>
        <CSV>
            <FileHeaderInfo>IGNORE</FileHeaderInfo>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
            <Comments>#</Comments>
        </CSV>
    </InputSerialization>
    <OutputSerialization>
        <CSV>
            <QuoteFields>ASNEEDED</QuoteFields>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        </CSV>                               
    </OutputSerialization>
</SelectRequest> 
```

如果您需要执行不同的检索指令，可以在 Expression 元素中修改 SQL 指令，有关指令的详细介绍，请参见 [Select 命令](https://cloud.tencent.com/document/product/436/37636)，以下为部分常见检索场景的简介。

- 假设您使用列索引筛选对象中的内容，您可以使用`s._n`筛选第`n`列的数据，`n`最小为1。如下指令将从对象中筛选第3列数值大于100的记录，并返回这些记录的第1和第2列： 
```shell
SELECT s._1, s._2 FROM COSObject s WHERE s._3 > 100
```

- 如果您的 CSV 对象中具有列表头，且您打算使用列表头的名称筛选对象中的内容（将`FileHeaderInfo`设置为`Use`），您可以使用`s.name`进行索引，如下指令将从对象中筛选表头名为`Id`和`FirstName`的对象：
```shell
SELECT s.Id, s.FirstName FROM COSObject s
```

- 您也可以在 SQL 表达式中指定函数，如下指令将统计出第一列中小于1的记录数：
```shell
SELECT count(*) FROM COSObject s WHERE s._1 < 1
```

如下为响应的例子：

```shell
HTTP/1.1 200 OK
x-cos-id-2: cos_id_demo
x-cos-request-id: cos_request_id_demo
Date: Tue, 12 Jan 2019 11:50:29 GMT

A series of messages
```

#### 示例2:  从 JSON 格式的对象中检索内容

以下示例展示了调用该接口从 JSON 格式的对象中检索全部内容，并将检索结果输出为 CSV 格式的过程。待检索的对象名为`exampleobject.json`，该对象存储于北京地域（ap-beijing）的存储桶 examplebucket-1250000000 中。

```shell
POST /exampleobject.json?select&select-type=2 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 12 Jan 2019 11:52:29 GMT
Authorization: authorization string
Content-Length: content length

<?xml version="1.0" encoding="UTF-8"?>
<SelectRequest>
    <Expression>Select * from COSObject</Expression>
    <ExpressionType>SQL</ExpressionType>
    <InputSerialization>
        <CompressionType>NONE</CompressionType>
        <JSON>
            <Type>DOCUMENT</Type>
        </JSON>
    </InputSerialization>
    <OutputSerialization>
        <CSV>
            <QuoteFields>ASNEEDED</QuoteFields>
            <RecordDelimiter>\n</RecordDelimiter>
            <FieldDelimiter>,</FieldDelimiter>
            <QuoteCharacter>"</QuoteCharacter>
            <QuoteEscapeCharacter>"</QuoteEscapeCharacter>
        </CSV>                               
    </OutputSerialization>
</SelectRequest> 
```

同样的，您也可以对 JSON 对象执行不同的检索指令，可以在 `Expression`元素中修改 SQL 指令，有关指令的详细介绍，请参见 [Select 命令](https://cloud.tencent.com/document/product/436/37636)，以下为部分常见检索场景的简介。

- 您可以通过 JSON 属性名称检索相应的数据，如下指令将从对象中筛选`city`数值为 Seattle 的记录，并返回这些记录的`country`和`city`信息：
```shell
SELECT s.country, s.city from COSObject s where s.city = 'Seattle'
```

- 您也可以在 SQL 表达式中指定函数，如下指令将统计出 JSON 对象中的记录总数：
```shell
SELECT count(*) FROM COSObject s
```

## 注意事项

与 [GET Object](https://cloud.tencent.com/document/product/436/7753) 接口不同， SELECT Object Content 不支持以下功能：

- 返回对象的某一片段：您不能通过 Range 这类参数指定返回对象的某一部分。
- 对于归档存储（ARCHIVE）和深度归档存储（DEEP_ARCHIVE）类型的对象，COS Select 无法直接进行检索，您需要取回数据后再进行操作。
