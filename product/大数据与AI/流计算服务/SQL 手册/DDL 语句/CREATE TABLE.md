CREATE TABLE 语句用来描述数据源（Source）或者数据目的（Sink）表。

**语法：**
```
CREATE TABLE `表名` (
	`字段名` 字段类型
	[, `字段名` 字段类型 ]*
	[, WATERMARK FOR BOUNDED(时间戳字段名, 最大容忍乱序时间) ]
	[, WATERMARK FOR ROWS(多少行生成一次 Watermark) ]
	[, PRIMARY KEY (主键字段1, … ) ]
) WITH (
	`参数名` = '参数值'
	[, `参数名` = '参数值' ]*
)
```
其中 BOUNDED 和 ROWS 属于 Event Time 时间模式（即数据源中自带时间戳字段）、ROWS 两种 WATERMARK 互斥，只可最多选择一项。
最大容忍乱序时间只在 Event Time 模式下有意义；而 Processing Time 模式不严格保证处理顺序，因为源数据没有时间戳定义。

**示例：**
```
CREATE TABLE KafkaSource1 (
  `time_` VARCHAR,
  `client_ip` VARCHAR,
  `method` VARCHAR(20),
) WITH (
  `type`='ckafka',
  `instanceId` = 'ckafka-cky18642',
  `encoding` = 'json',
  `topic` = 'test-input'
);
```

## Source 和 Sink
目前流计算 Oceanus 可以根据后续的插入语句（INSERT INTO）和选择语句（SELECT FROM）自动判断源和目的表，因而用户无需显式指定源和目的表的类型，但仍然需要注意 TencentDB（MySQL）只能用作数据源，且只能用于 JOIN 操作的右表。

用户可以在 CREATE TABLE 的 WITH 参数中指定数据源或数据目的类型，例如 type = ‘cdp’ 则表明使用 CDP；type = ‘ckakfa’ 则是使用 CKafka 作为数据源。

>**注意：**
>等号后面的参数必须使用半角单引号包围，不允许使用双引号或者全角引号。通常情况下，字段名不区分大小写（例如 `type` 和 `TYPE` 等同），但单引号内部的字符串在引用外部值时要区分大小写（例如 `root` 和 `ROOT` 作为用户名时是不同的）。

以下是各种数据源（Source）和数据目的（Sink）所需参数：

### CDP
| 参数	| 含义 |
| ----- | ----- |
| type	| 当数据源、数据目的为 CDP 时，需要指定值为 “cdp” 。|
| project	| CDP 的项目名。|
| topic	| CDP 指定项目的 topic。|
| startMode	| 可选项，值可以为 EARLIEST（从最早 Offset 读取）、LATEST（从最新 Offset 读取）。|
| timestampMode | 可选项，用于指定数据源或数据目的表时间戳格式，默认值为 “AUTO”：对于数据源表，默认将根据输入数据的格式自动判断（大于 99999999999 则视为 MILLISECOND，小于等于 99999999999 则视为 SECOND）；对于数据目的表，则默认按 MILLISECOND 格式输出时间戳。<br>若显式设定值为“MILLISECOND”，表示采用毫秒为单位的 Unix 时间戳；“SECOND” 表示采用秒为单位的 Unix 时间戳。**<br>注意：**由于 “AUTO” 模式会对每条数据做判断，可能会略微降低性能。若在低延时、高吞吐的环境下使用，请显式指定 timestampMode 参数以获得更好的性能。|

>**注意：**
> CDP 表分为 Tuple 和 Upsert 两类。Tuple 类型的表不设主键（即没有 PRIMARY KEY 语句），只支持 Append（只追加数据，不会更新之前写入的数据）操作，可接受大多数查询的结果（即Append 流）。

Upsert 类型的表定义了主键（即使用 PRIMARY KEY 定义了主键），支持插入或更新（Upsert）操作，可以接受由 DISTINCT、不含窗口的 JOIN、不含窗口的 GROUP BY 等操作产生的 Upsert 流（Upsert 是 Update OR Insert 的简写，即对于一条数据，如果之前输出过与其同主键的记录，则更新该记录；否则插入新的数据）。这些 Upsert 流只允许写入 Upsert 类型的 CDP 目的表，不能混用；且 Upsert 类型的 CDP 表不允许作为源表。

**示例：Tuple 类型 CDP 数据源和目的表，使用 Processing Time 时间模式**
对于时间模式和 WATERMARK 的介绍，参见下文 [WATERMARK](https://cloud.tencent.com/document/product/849/18034#watermark) 小节。
```
CREATE TABLE `traffic_output` (
  `f1` VARCHAR,
  `f2` BIGINT
) WITH (
  `type` = 'cdp',
  `project` = 'test',
  `topic` = 'Output',
  `startMode` = 'EARLIEST'
);
```
此时使用 Processing Time 模式，定义了一个包含 f1、f2、PROCTIME（自动生成，表示每条记录被处理时的时间戳，可用于时间窗口的描述）列的 CDP Tuple 类型的表，既可以作为数据源（Source），也可以作为数据目的（Sink）。

**示例：Tuple 类型 CDP 数据源和目的表，使用 Event Time 时间模式**
```
CREATE TABLE `public_traffic_output` (
  `rowtime` TIMESTAMP,
  `f1` VARCHAR,
  `f2` BIGINT,
　 WATERMARK FOR BOUNDED(`rowtime`, 5000)    -- 定义 Event Time 模式使用的时间戳字段和最大允许的乱序到达的时间范围
) WITH (
  `type` = 'cdp',
  `project` = 'test',
  `topic` = 'Output'
);
```
上述定义的表使用 Event Time 模式，定义了一个包含 f1、f2 列的 CDP Tuple 类型的表，既可以作为数据源，也可以作为数据目的表。

**示例：Upsert 类型 CDP 数据目的表**
```
CREATE TABLE `public_traffic_output` (
  `f1` VARCHAR,
  `f2` BIGINT,
  PRIMARY KEY(`f1`)  -- 定义主键的 CDP 表为 Upsert 类型
) WITH (
  `type` = 'cdp',
  `project` = 'test',
  `topic` = 'Output'
);
```
上述定义的表使用 Processing Time 模式，定义了一个包含 f1、f2 列的 CDP Upsert 类型的表，它只能作为数据目的表。

### CKakfa

| 参数	| 含义 |
| ----- | ----- |
| type	| 当数据源、数据目的为 CKafka 时，需要指定值为“ckafka”。|
| instanceId	| CKafka 的 instanceId。|
| encoding	| 可以为 json 或 csv，如果选择 csv 则必须同时指定 fieldDelimiter。|
| topic	| Ckafka 指定 instanceId 下的 topic。|
| timestampMode | 可选项，用于指定数据源或数据目的表时间戳格式，默认值为 “AUTO”：对于数据源表，默认将根据输入数据的格式自动判断（大于 99999999999 则视为 MILLISECOND，小于等于 99999999999 则视为 SECOND，字符串形式则视为 SQL）；对于数据目的表，则默认按  MILLISECOND 格式输出时间戳。<br>若显式设定值为“MILLISECOND”，表示采用毫秒为单位的 Unix 时间戳；“SECOND”表示采用秒为单位的 Unix 时间戳；“SQL”表示采用 yyyy-MM-dd HH:mm:SS 形式的字符串时间戳。<br>**注意：**由于 “AUTO” 模式会对每条数据做判断，可能会略微降低性能。若在低延时、高吞吐的环境下使用，请显式指定 timestampMode 参数以获得更好的性能。|
| fieldDelimiter	| encoding 为 CSV 时可选，指定 CSV 各字段的分隔符。默认为逗号分隔，即值为 ‘,’。|
| startMode	| 可选项，值可以为 EARLIEST（从最早 Offset 读取）、LATEST（从最新 Offset 读取）、GROUP（从指定 groupId 读取，必须同时使用 groupId 参数）。|
| groupId	| 指定读取的 groupId（仅用于 startMode = ‘GROUP’模式）。|
| ignoreErrors | 可选项，默认为 true，表示跳过错误的行；如果设为 false 则遇到错误数据会导致程序直接终止。|

>**注意：**
>- 如果数据中包含与分隔符相同的字符，则系统会自动使用双引号将该字符引起来以避免歧义。如果数据本身存在双引号，则会使用两个双引号(“”) 来替换每个出现的双引号。
>- CKafka 只支持 Append 类型流的写入，不支持 Upsert 流。如需写入 Upsert 流，请使用 CDP。

### TencentDB（仅支持作为 JOIN 条件的右表）
| 字段	| 含义 |
| ----- | ----- |
| instanceId	| TencentDB 的实例 ID，注意大小写敏感。|
| database |	数据库名，注意大小写敏感。|
| table	| 表名，注意大小写敏感。|
| user |	用户名，注意大小写敏感。|
| password	| 密码，注意大小写敏感。|

## WATERMARK
### Event Time / Processing Time
对于基于窗口的操作（例如 GROUP BY、OVER、JOIN 条件中时间段的指定），流计算 Oceanus 支持两种时间处理模式：Event Time 和 Processing Time 模式。
![](https://main.qcloudimg.com/raw/3b1452e12aa27378ad022b23cba6896c.png)
Event Time 模式使用输入数据自带的时间戳，容忍一定程度的乱序数据输入（例如更早的数据由于各节点处理能力以及网络波动等不可预知的原因来的却更晚），这个参数可以通过 BOUNDED 的第二个参数指定，单位是毫秒。该处理模式最精确，但对输入数据有自带时间戳的要求。目前只支持数据源中以 timestamp 类型定义的字段，未来将会支持虚拟列，可将其他类型的列应用处理函数转换为系统接受的时间戳。
Processing Time 处理模式不要求输入数据有时间戳，而是将该条数据被处理的时间戳自动加入数据，并以 PROCTIME（必须全为大写）字段命名。该列是隐藏的，SELECT * 时不会出现，只有用户手动使用时才会被读取。
>**注意：**
>对于同一个任务的所有数据源，只允许采用一种时间模式。若某个使用 Event Time 模式，则必须要求所有定义的 Table Source 都定义时间戳并声明 WATERMARK 时间戳字段。

### ROWS / BOUNDED
如果您希望处理基于窗口（Window）的数据，而数据中正好包含时间戳信息（以 SQL 规范的时间戳或 Unix 时间戳表示的列），则建议使用 Event Time 处理模式。例如数据有一个 generation_time 字段，最大允许的乱序误差是 1000 毫秒，则可以声明`WATERMARK FOR BOUNDED(`generation_time`, 1000)`以启用 Event Time 时间处理模式。

**示例：**
数据有一个 generation_time 字段，最大允许的乱序误差是 1000 毫秒，则可以声明：
WATERMARK FOR BOUNDED(`generation_time`, 1000) 

如果希望每隔 100 条数据生成一次Watermark，那么可以声明：
WATERMARK FOR ROWS(`generation_time`, 100) 

这两种声明都可以启用 Event Time 时间处理模式。

若不声明  WATERMARK 以指定时间戳字段，则会使用 Processing Time 时间模式，该模式以数据被处理的时间戳来生成 Watermark 并在后续使用，顺序和精确性不能得到保证，可用于时间精确度要求不高的应用场景。



