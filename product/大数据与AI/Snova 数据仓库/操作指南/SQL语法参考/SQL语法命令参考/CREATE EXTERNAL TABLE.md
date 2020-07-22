定义一个新的外部表，目前 CDW 只支持腾讯云 COS 外部表，不提供 gpfdist、file、s3、hdfs、http 的外部表。

## 概要

```sql
CREATE [READABLE] EXTERNAL TABLE table_name     
    ( column_name data_type [, ...] | LIKE other_table )
     LOCATION 
('cos:// {BUCKET}-{APPID}.cos.{REGION}.myqcloud.com/{PREFIX} secretKey=xxx secretId=xxx '
           [, ...])| ('cos://cos.{REGION}.myqcloud.com/{BUCKET}/{PREFIX} secretKey=xxx secretId=xxx ')
     [ON MASTER]
     FORMAT 'TEXT' 
           [( [HEADER]
              [DELIMITER [AS] 'delimiter' | 'OFF']
              [NULL [AS] 'null string']
              [ESCAPE [AS] 'escape' | 'OFF']
              [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
              [FILL MISSING FIELDS] )]
          | 'CSV'
           [( [HEADER]
              [QUOTE [AS] 'quote'] 
              [DELIMITER [AS] 'delimiter']
              [NULL [AS] 'null string']
              [FORCE NOT NULL column [, ...]]
              [ESCAPE [AS] 'escape']
              [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
              [FILL MISSING FIELDS] )]
          | 'AVRO' 
          | 'PARQUET'
          | 'CUSTOM' (Formatter=<formatter_specifications>)
    [ ENCODING 'encoding' ]
      [ [LOG ERRORS] SEGMENT REJECT LIMIT count
      [ROWS | PERCENT] ]
 
 
CREATE WRITABLE EXTERNAL TABLE table_name
    ( column_name data_type [, ...] | LIKE other_table )
     LOCATION('cos:// {BUCKET}-{APPID}.cos.{REGION}.myqcloud.com/{PREFIX} secretKey=xxx secretId=xxx '
           [, ...])| ('cos://cos.{REGION}.myqcloud.com/{BUCKET}/{PREFIX} secretKey=xxx secretId=xxx ' [, ...])
      FORMAT 'TEXT' 
               [( [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [ESCAPE [AS] 'escape' | 'OFF'] )]
          | 'CSV'
               [([QUOTE [AS] 'quote'] 
               [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [FORCE QUOTE column [, ...]] ]
               [ESCAPE [AS] 'escape'] )]
           | 'AVRO' 
           | 'PARQUET'
 
           | 'CUSTOM' (Formatter=<formatter specifications>)
    [ ENCODING 'write_encoding' ]
    [ DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY ]
 
```

## 描述
有关外部表的详细信息请参阅“数据库管理员指南”中的“装载和卸载数据”。

CREATE EXTERNAL TABLE 或 CREATE EXTERNAL WEB TABLE 在数据库中创建一个新的可读外部表定义。可读外部表通常用于快速并行数据加载。定义外部表后，可以使用 SQL 命令直接（并行）查询其数据。 例如用户可以选择加入或排序外部表数据。用户还可以创建外部表的视图。DML 操作（更新、插入、删除或 TRUNCATE）在可读外部表上不可操作，用户不能在可读外部表上创建索引。

CREATE WRITABLE EXTERNAL TABLE 或 CREATE WRITABLE EXTERNAL WEB TABLE 在数据库中创建一个新的可写外部表定义。可写外部表通常用于将数据从数据库卸载到一组文件或命名管道中。可写外部 Web 表也可用于将数据输出到可执行程序。一旦写入外部表被定义，可以从数据库表中选择数据并将其插入到可写外部表中。可写外部表仅允许插入 操作。选择、更新、删除或 TRUNCATE 不被允许。

常规外部表和外部 Web 表之间的主要区别是它们的数据源。常规可读外部表访问静态平面文件，而外部 Web 表访问动态数据源，无论是在 Web 服务器上还是通过执行 OS 命令或脚本。

该 FORMAT 子句用于描述外部表格文件的格式。有效的文件格式是分隔文本（TEXT）逗号分隔值（CSV）格式，与 PostgreSQL 可用的格式化选项类似 **COPY** 命令。如果文件中的数据不使用默认列分隔符、转义字符、空字符串等，则必须指定其他格式选项，以便外部文件中的数据被数据库正确读取。有关使用自定义格式的信息，请参阅“数据库管理员指南中”的“装载和卸载数据”。

在创建写入或从 COS 存储区中读取的外部表之前，必须配置数据库以支持协议。COS 外部表可以使用 CSV 或文本格式的文件可写的 COS 外部表仅支持插入操作。请参见 **COS 协议配置**。

## 参数

READABLE | WRITABLE
指定外部表的类型，默认可读。可读外部表用于将数据加载到数据库中。可写外部表用于卸载数据。

table_name
新外部表的名称。

column_name
在外部表定义中创建的列的名称。与常规表不同，外部表不具有列约束或默认值，因此不要指定。

LIKE other_table
该 LIKE 子句指定新的外部表自动复制所有列名，数据类型和分发策略的表。如果原始表指定了任何列约束或默认列值，那么它们将不会被复制到新的外部表定义中。

data_type
列的数据类型。

LOCATION ('protocol://host[:port]/path/file' [, ...])
对于可读外部表，指定用于填充外部表或 Web 表的外部数据源的 URI。常规可读外部表允许 gpfdist 或文件协议。外部 Web 表允许 http 协议。如果端口被省略，端口8080被假定为 http 和 gpfdist 协议，端口9000为 gphdfs 协议。如果使用 gpfdist 协议，the 路径是相对于 gpfdist 服务文件的目录（启动 gpfdistgpfdist 程序时指定的目录）。此外，gpfdist 使用通配符或其他 C-style 模式匹配（例如：空格符为 [[:space:]]）表示目录中的多个文件。例如：

```sql
'gpfdist://filehost:8081/*'
'gpfdist://masterhost/my_load_file'
'file://seghost1/dbfast1/external/myfile.txt'
'http://intranet.example.com/finance/expenses.csv'
'cos://{BUCKET}-{APPID}.cos.{REGION}.myqcloud.com/{PREFIX} secretKey=xxx secretId=xxx'
```
 
对于可写外部表，指定 cos 协议将会从的 Segment 收集输出的数据并将其写入一个或多个命名文件。 

在可选择的 #transform=trans_name 中，用户可以指定要在加载或提取数据时应用的转换。trans_name 是用户运行 gpfdist 实用程序指定的 YAML 配置文件的转换名称。当用户用 **COS** 协议创建一个外部表时，只支持 TEXT 和 CSV 格式。这些文件可以是 gzip 压缩格式。该 **COS** 协议识别 gzip 格式并解压缩文件。只支持 gzip 压缩格式。

EXECUTE 'command' [ON ...]
允许只读可读外部 Web 表或可写外部表。对于可读取的外部 Web 表，要指定由 Segment 实例执行的 OS 命令。该命令可以是单个 OS 命令或脚本。ON 子句用于指定哪些 Segment 实例将执行给定的命令。

FORMAT 'TEXT | CSV | AVRO | PARQUET' (options)
指定外部或 Web 表格数据的格式，纯文本（TEXT）或逗号分隔值（CSV）格式。
仅使用 gphdfs 协议支持 AVRO 和 PARQUET 格式。

FORMAT 'CUSTOM' (formatter=formatter_specification)
指定自定义数据格式。formatter_specification 指定用于格式化数据的函数，后跟格式化函数的逗号分隔参数。格式化程序规范的长度包括 Formatter= 的字符串的长度可以高达约50K字节。

有关使用自定义格式的信息，请参阅“数据库管理员指南”中的“装载和卸载数据”。

DELIMITER
指定单个 ASCII 字符，用于分隔每行数据中的列。默认值为 TEXT 模式下的制表符，CSV 格式为逗号。在可读外部表的 TEXT 模式下，对于将非结构化数据加载到单列表中的特殊用例，可以将分隔符设置为 OFF。

NULL
指定表示 NULL 值的字符串。在 TEXT 模式下，默认值是 \N（反斜杠-N），CSV 模式中不含引号的空值。在 TEXT 模式下用户可能更希望不想将 NULL 值与空字符串区分开的情况下，也能使用 NULL 字符串。使用外部和 Web 表时，与此字符串匹配的任何数据项将被视为 NULL 值。使用外部和 Web 表格时，与此字符串匹配的任何数据项将被视为 NULL 值。

作为 text 格式的示例，此 FORMAT 子句可用于指定两个单引号（''）的字符串为 NULL 值。

```sql
FORMAT 'text' (delimiter ',' null '\'\'\'\'' )
```

ESCAPE
指定用于 C 转义序列的单个字符（例如 \n、\t、\100等）以及用于转义可能被视为行或列分隔符的数据字符。 确保选择在实际列数据中的任何地方都不使用的转义字符。默认转义字符是文本格式文件的\（反斜杠）和 csv 格式文件的"（双引号），但是可以指定其他字符来表示转义，也可以禁用文本转义通过指定值 'OFF' 作为转义值，格式化的文件对于诸如文本格式的 Web 日志数据之类的数据非常有用，这些数据具有许多不希望转义的嵌入式反斜杠。

NEWLINE
指定数据文件中使用的换行符 – LF（换行符，x0A），CR（回车符号，0x0D）或 CRLF（回车加换行，0x0D 0x0A）。如果未指定，数据库的 Segment 将通过查看其接收的第一行数据并使用遇到的第一个换行符来检测换行类型。

HEADER
对于可读外部表，指定数据文件中的第一行是标题行（包含表列的名称），不应作为表的数据包含。如果使用多个数据源文件，则所有文件必须有标题行。

对于 s3 协议，标题行中的列名不能包含换行符 (\n) 或回车符 (\r)。

QUOTE
指定 CSV 模式的报价字符。默认值为双引号（"）。

FORCE NOT NULL 
在 CSV 模式下，处理每个指定的列，就像它被引用一样，因此不是一个 NULL 值。对于 CSV 模式中的默认空字符串（两个分隔符之间不存在），这将导致将缺少的值作为零长度字符串计算。

FORCE QUOTE
在可写外部表的 CSV 模式下，强制引用用于每个指定列中的所有非 NULL 值。NULL 输出从不引用。

FILL MISSING FIELDS
在可读外部表的 TEXT 和 CSV 模式下，指定 FILL MISSING FIELDS 时，当一行数据在行或行的末尾缺少数据字段时，将丢失尾字段值设置为 NULL（而不是报告错误）。空行，具有 NOT NULL 约束的字段和行上的尾随分隔符仍然会报告错误。

ENCODING 'encoding'
字符集编码用于外部表。指定一个字符串常量（如 'SQL_ASCII'），一个整数编码号或者 DEFAULT 来使用默认的客户端编码。 

LOG ERRORS
这是一个可选的子句，可以在 SEGMENT REJECT LIMIT 子句之前记录有关具有格式错误的行的信息。错误日志信息在内部存储，并使用数据库内置 SQL 函数 gp_read_error_log() 访问。

SEGMENT REJECT LIMIT count [ROWS | PERCENT]
在单行错误隔离模式下运行 COPY FROM 操作。如果输入行具有格式错误，则它们将被丢弃，前提是在加载操作期间在任何 Segment 实例上未达到拒绝限制计数。The 拒绝限制计数可以指定为行数（默认值）或总行数百分比（1-100）。如果使用 PERCENT，则每个 Segment 只有在处理了参数 gp_reject_percent_threshold 所指定的行数之后才开始计算坏行百分比。gp_reject_percent_threshold 的默认值为300行。诸如违反 NOT NULL、CHECK 或 UNIQUE 约束的约束错误仍将以“all-or-nothing”输入模式进行处理。如果没有达到限制，所有好的行将被加载，任何错误行被丢弃。

注解：读取外部表时，如果未首先触发 SEGMENT REJECT LIMIT 或未指定 SEGMENT REJECT LIMIT，则数据库将限制可能包含格式错误的初始行数。如果前1000行被拒绝，则 COPY 操作将被停止并回滚。

可以使用数据库服务器配置参数 gp_initial_bad_row_limit 更改初始拒绝行的数量限制。 

DISTRIBUTED BY (column, [ ... ] )
DISTRIBUTED RANDOMLY
用于为可写外部表格声明数据库分发策略。默认情况下，可写外部表是随机分布的。如果要从中导出数据的源表具有散列分发策略，则为可写外部表定义相同的分发密钥列可以通过消除在互连上移动行的需要来改善卸载性能。当用户发出诸如 INSERT INTO wex_table SELECT * FROM source_table 的卸载命令时，如果两个表具有相同的散列分布策略，则可以将卸载的行直接从 Segment 发送到输出位置。

## 示例
创建一个名为 cos_tbl 的可读外部表使用的 COS 协议和 COS 指定读取广州 simple-bucket 下的所有文件，文件格式为 csv：

```sql
CREATE READABLE EXTERNAL TABLE cos_tbl (c1 int, c2 text, c3 int)
LOCATION('cos://cos.ap-guangzhou.myqcloud.com/simple-bucket/from_cos/ secretKey=xxx secretId=xxx')
FORMAT 'csv';
```

## 注解
指定 LOG ERRORS 子句时，数据库会捕获读取外部表数据时发生的错误。用户可以查看和管理捕获的错误日志数据。
- 使用内置的 SQL 函数 gp_read_error_log('table_name')。它需要对 table_name 具有 SELECT 特权。此示例显示使用 COPY 命令加载到表 ext_expenses 中的数据的错误日志信息：
```sql
SELECT * from gp_read_error_log('ext_expenses');
```
如果 table_name 不存在，该函数返回 FALSE。
- 如果指定的表存在错误日志数据，新的错误日志数据将附加到现有的错误日志数据。错误日志信息不会复制到镜像 Segment。
- 使用内置的 SQL 函数 gp_truncate_error_log('table_name') 删除 table_name 的错误日志数据。它需要表所有者权限，此示例删除将数据移动到表中时捕获的错误日志信息 ext_expenses：
```sql
SELECT gp_truncate_error_log('ext_expenses'); 
```
如果 table_name 不存在，该函数返回 FALSE。

指定`\*`通配符以删除当前数据库中现有表的错误日志信息。指定字符串*.*以删除所有数据库错误日志信息，包括由于以前的数据库问题而未被删除的错误日志信息。如果指定\*，则需要数据库所有者权限。如果指定了*.*则需要操作系统超级用户权限。

## COS 协议限制
- 只支持 COS 路径样式的 URL。
```sql
--COS V4： 
cos://cos.{REGION}.myqcloud.com/{BUCKET}/{PREFIX}
--COS V5： 
cos:// {BUCKET}-{APPID}.cos.{REGION}.myqcloud.com/{PREFIX}
```
- CREATE EXTERNAL TABLE 命令的 LOCATION 子句中只支持一个 URL。
- 如果在 CREATE EXTERNAL TABLE 命令中未指定 NEWLINE 参数，则在特定前缀的所有数据文件中，换行符必须相同。如果某些具有相同前缀的数据文件中的换行字符不同，则对文件的读取操作可能会失败。
- 对于可写入的 COS 外部表，只支持 INSERT 操作。不支持 UPDATE、DELETE 和 TRUNCATE 操作。
- 利用数据库执行的并行处理 Segment 实例中，只读 COS 表的 COS 位置中的文件的大小应类似，文件数量应允许多个 Segment 从 COS 位置下载数据。例如，如果数据库系统由16个 Segment 组成，网络带宽足够，在 COS 位置创建16个文件允许每个 Segment 从一个文件下载 COS 位置。相比之下，如果位置只包含1或2个文件，则只有1或2个 Segment 下载数据。

## 关于 COS 协议 URL
对于 COS 协议，用户可以在 CREATE EXTERNAL TABLE 命令的 LOCATION 子句中指定文件的位置和可选的配置文件位置。语法如下：

```sql
'cos://cos.{REGION}.myqcloud.com/{BUCKET}/{PREFIX} secretKey=xxx secretId=xxx'
'cos://{BUCKET}-{APPID}.cos.{REGION}.myqcloud.com/{PREFIX} secretKey=xxx secretId=xxx'
```

用户可以指定 COS 协议访问腾讯云 COS 上的数据。对于 COS 协议来说，LOCATION 子句指定数据文件为表上传的 COS 端点和存储桶名称。

REGION：cos 支持的地域，需要和实例在相同地域，可选值参考 [可用地域](https://cloud.tencent.com/document/product/436/6224)。
BUCKET：cos 桶名称。
PREFIX：cos 对象名称前缀。prefix 可以为空，可以包括多个斜杠。

在定义只读表场景下，prefix 指定需要读取的对象名前缀，如果 prefix 为空，读取 bucket 下所有文件；如果 prefix 以斜杠（/）结尾，则匹配改文件夹下面的所有文件及子文件夹中的文件；否则，读取前缀匹配的所有文件夹及子文件夹中的文件。例如 cos 对象包括：
read-bucket/simple/a.csv
read-bucket/simple/b.csv
read-bucket/simple/dir/c.csv
read-bucket/simple_prefix/d.csv

prefix 指定：simple 则读取所有文件，包括目录名称前缀匹配的 simple_prefix，对象列表：
read-bucket/simple/a.csv
read-bucket/simple/b.csv
read-bucket/simple/dir/c.csv
read-bucket/simple_prefix/d.csv

prefix 指定：simple/ 则读取包括 simple/ 的所有文件，包括：
read-bucket/simple/a.csv
read-bucket/simple/b.csv
read-bucket/simple/dir/c.csv

在只写表场景下，prefix 指定输出文件前缀，如果不指定 prefix，文件写入到 bucket 下；如果 prefix 以斜杠（/）结尾，文件写入到 prefix 指定的目录下，否则，以给定的 prefix 作为文件前缀。例如，需要创建的文件包括： 
a.csv、b.csv、c.csv。

如果指定 prefix 为 simple/ ， 则生成的对象为：
read-bucket/simple/a.csv
read-bucket/simple/b.csv
read-bucket/simple/b.csv

如果指定 prefix 为 simple\_， 则生成的对象为：
read-bucket/simple_a.csv
read-bucket/simple_b.csv
read-bucket/simple_b.csv

secretKey 和 secretId 分别是用户自己在腾讯云的密钥对。

**注解**：当上传或下载 COS 文件时，数据库可能需要在每个分 Segment 主机上最多可以使用 threadnum * chunksize 的内存。当用户配置总体的数据库内存时，请考虑此 cos 协议内存要求，并根据需要增加 **gp_vmem_protect_limit** 的值。

## 兼容性
CREATE EXTERNAL TABLE 是数据库扩展。SQL 标准没有规定外部表。

## 另见
CREATE TABLE AS、CREATE TABLE、COPY、SELECT INTO、INSERT
