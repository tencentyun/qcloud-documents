## 介绍

消息队列 CMQ（Cloud Message Queue，以下简称 CMQ）是基于腾讯自研消息引擎的分布式消息队列系统，可以用作数据源（Source）和数据目的（Sink）。用户可以把流数据导入到 CMQ 的某个 Queue 中，通过 Flink 算子进行处理后，输出到相同或不同 CMQ 示例的另一个 Queue。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## 使用范围
CMQ 支持用作数据源表（Source），也可以作为 Tuple 数据流的目的表（Sink），暂不支持 Upsert 数据流。

## DDL 定义
### 用作数据源（Source）
#### JSON 格式输入
```sql
CREATE TABLE `cmq_source_json_table` (
    `id` INT,
    `name`STRING,
    PRIMARY KEY (`id`) NOT ENFORCED	-- 如果想做到数据去重的操作，则需要指定 PK，按照主键来区分不同的数据
) WITH (
    'connector' = 'cmq',			   -- 必须为 'cmq'
    'hosts' = 'http://cmq-nameserver-vpc-gz.api.tencentyun.com',	-- cmq 所在地域的 nameServer
    'queue' = 'queue_name',			-- cmq 的队列名
    'secret-id' = 'xxxx',			  -- 账号 secretId
    'secret-key' = 'xxxx',             -- 账号 secretKey
    'sign-method' = 'HmacSHA1',        -- 签名的方式
    'format' = 'json',                 -- 定义数据格式（JSON 格式）
    'json.fail-on-missing-field' = 'false',	 -- 如果设置为 false, 则遇到缺失字段不会报错。
    'json.ignore-parse-errors' = 'true',   	 -- 如果设置为 true，则忽略任何解析报错。
    'batch-size' = '16',               -- 批量消费消息的个数
    'request-timeout' = '5000ms',  	-- 请求的超时时间
    'polling-wait-timeout'= '10s', 	-- 获取不到数据情况下的等待时间
    'key-alive-timeout'= '5min'    	-- 含 primary key 的消息，CMQ 去重的有效时间
);
```

#### CSV 格式输入

```sql
CREATE TABLE `cmq_source_csv_table` (
    `id` int,
    `name` STRING,
    PRIMARY KEY (`id`) NOT ENFORCED -- 如果想做到数据去重的操作，则需要指定 PK，按照这个主键来区分不同的数据
) WITH (
	'connector' = 'cmq', 			 -- 必须为 'cmq'
    'hosts' = 'http://cmq-nameserver-vpc-gz.api.tencentyun.com',	-- cmq 所在地域的 nameServer
    'queue' = 'queue_name',	 	-- cmq 的队列名
    'secret-id' = 'xxxx',		   -- 账号 secretId
    'secret-key' = 'xxxx',          -- 账号 secretKey
    'sign-method' = 'HmacSHA1',     -- 签名的方式
    'format' = 'csv',               -- 定义数据格式（CSV 格式）
    'batch-size' = '16',            -- 批量消费消息的个数/批量发送消息的个数
    'request-timeout' = '5000ms',   -- 请求的超时时间
    'polling-wait-timeout'= '10s',  -- 获取不到数据情况下的等待时间
    'key-alive-timeout'= '5min'     -- 含 primary key 的消息，CMQ 去重的有效时间
);
```

### 用作数据目的（Sink）

#### JSON 格式输出

```sql
CREATE TABLE `cmq_sink_json_table` (
    `id` int,
    `name` STRING
) WITH (
	'connector' = 'cmq', 					 	-- 必须为 'cmq'
    'hosts' = 'http://cmq-nameserver-vpc-gz.api.tencentyun.com',    -- cmq 所在地域的 nameServer
    'queue' = 'queue_name',			 		-- cmq 的队列名
    'secret-id' = 'xxxx',				   	-- 账号 secretId
    'secret-key' = 'xxxx',         		 	-- 账号 secretKey
    'sign-method' = 'HmacSHA1',     			-- 签名的方式
    'format' = 'json',             		 	-- 定义数据格式（JSON 格式）
    'json.fail-on-missing-field' = 'false',	 -- 如果设置为 false, 则遇到缺失字段不会报错。
    'json.ignore-parse-errors' = 'true',         -- 如果设置为 true，则忽略任何解析报错。
    'batch-size' = '16',                        -- 批量发送消息的个数
    'request-timeout' = '5000ms',               -- 请求的超时时间
    'retry-times' = '3',                        -- 发送消息的重试次数
    'max-block-timeout' = '0s'                  -- 批量发送数据的最大等待时间
);
```

#### CSV 格式输出

```sql
CREATE TABLE `cmq_sink_csv_table` (
    `id` int,
    `name` STRING
) WITH (
	'connector' = 'cmq', 					     -- 必须为 'cmq'
    'hosts' = 'http://cmq-nameserver-vpc-gz.api.tencentyun.com',    -- cmq 所在地域的 nameServer
    'queue' = 'queue_name',				     -- cmq 的队列名
    'secret-id' = 'xxxx',			           -- 账号 secretId
    'secret-key' = 'xxxx',                      -- 账号 secretKey
    'sign-method' = 'HmacSHA1',                 -- 签名的方式
    'format' = 'csv',                           -- 定义数据格式（CSV 格式）
    'batch-size' = '16',                    	-- 批量发送消息的个数
    'request-timeout' = '5000ms',               -- 请求的超时时间
    'retry-times' = '3',                        -- 发送消息的重试次数
    'max-block-timeout' = '0s'                  -- 批量发送数据的最大等待时间
);
```

## WITH 参数
### 通用 WITH 参数

| 参数值               | 必填 |  默认值  |                             描述                             |
| :------------------- | :--: | :------: | :----------------------------------------------------------: |
| connector            |  是  |    无    |                     必须指定为 `'cmq'`。                     |
| hosts                |  是  |    无    | 队列所在地域的 nameServer，具体的地址可以参考 [TCP SDK](https://cloud.tencent.com/document/product/406/35818)。 |
| queue                |  是  |    无    |                      cmq 对应的队列名。                      |
| secret-id            |  是  |    无    |                       账号 secretId。                        |
| secret-key           |  是  |    无    |                       账号 secretKey。                       |
| sign-method          |  否  | HmacSHA1 |                       账号的签名方式。                       |
| format               |  是  |    无    |     CMQ 消息的输入输出格式。目前支持`'csv'`、`'json'`。      |
| batch-size           |  否  |    16    |                  批量发送/接收消息的个数。                   |
| request-timeout      |  否  |  5000ms  |                       请求的超时时间。                       |
| polling-wait-timeout |  否  |   10s    |                获取不到数据情况下的等待时间。                |
| key-alive-timeout    |  否  |   60s    | 含 primary key 的消息，CMQ 去重的有效时间。该参数设计是为了同一条数据不会重复消费，不保证全局不重复。 |
| retry-times          |  否  |    3     |                     发送消息的重试次数。                     |
| max-block-timeout    |  否  |    0s    | 批量发送数据的最大等待时间，`'0s'`表示不等待，有数据就直接发送。 |

### JSON 格式 WITH 参数

| 参数值                         | 必填 | 默认值 | 描述                                                         |
| ------------------------------ | ---- | ------ | ------------------------------------------------------------ |
| json.fail-on-missing-field     | 否   | false  | 如果为 true，则遇到缺失字段时，会让作业失败。如果为 false（默认值），则只会把缺失字段设置为 null 并继续处理。 |
| json.ignore-parse-errors       | 否   | false  | 如果为 true，则遇到解析异常时，会把这个字段设置为 null 并继续处理。如果为 false，则会让作业失败。 |
| json.timestamp-format.standard | 否   | SQL    | 指定 JSON 时间戳字段的格式，默认是 SQL（格式是`yyyy-MM-dd HH:mm:ss.s{可选精度}`）。也可以选择 ISO-8601，格式是 `yyyy-MM-ddTHH:mm:ss.s{可选精度}`。 |

### CSV 格式 WITH 参数

| 参数值                      | 必填 | 默认值     | 描述                                                         |
| --------------------------- | ---- | ---------- | ------------------------------------------------------------ |
| csv.field-delimiter         | 否   | ,          | 指定 CSV 字段分隔符，默认是半角逗号。                        |
| csv.line-delimiter          | 否   | U&'\\000A' | 指定 CSV 的行分隔符，默认是换行符`\n`，SQL 中必须用`U&'\000A'`表示。如果需要使用回车符`\r`，SQL 中必须使用`U&'\000D'`表示。 |
| csv.disable-quote-character | 否   | false      | 禁止字段包围引号。如果为 true，则 'csv.quote-character' 选项不可用。 |
| csv.quote-character         | 否   | ''         | 字段包围引号，引号内部的作为整体看待。默认是`''`。           |
| csv.ignore-parse-errors     | 否   | false      | 忽略处理错误。对于无法解析的字段，会输出为 null。            |
| csv.allow-comments          | 否   | false    | 忽略 # 开头的注释行，并输出为空行（请务必将 csv.ignore-parse-errors 设为 true）。 |
| csv.array-element-delimiter | 否   | ;          | 数组元素的分隔符，默认是`;`。                                |
| csv.escape-character        | 否   | 无         | 指定转义符，默认禁用转义。                                   |
| csv.null-literal            | 否   | 无         | 将指定的字符串看作 null 值。                                 |

## 代码示例

```sql
CREATE TABLE `cmq_source_json_table` (
    `id` int,
    `name` STRING,
    PRIMARY KEY (`id`) NOT ENFORCED	-- 如果想做到数据去重的操作，则需要指定 PK，按照主键来区分不同的数据
) WITH (
    'connector' = 'cmq',			   -- 必须为 'cmq'
    'hosts' = 'http://cmq-nameserver-vpc-gz.api.tencentyun.com',	-- cmq 所在地域的 nameServer
    'queue' = 'queue_name',			-- cmq 的队列名
    'secret-id' = 'xxxx',			  -- 账号 secretId
    'secret-key' = 'xxxx',             -- 账号 secretKey
    'sign-method' = 'HmacSHA1',        -- 签名的方式
    'format' = 'json',                 -- 定义数据格式（JSON 格式）
    'json.fail-on-missing-field' = 'false',	 -- 如果设置为 false, 则遇到缺失字段不会报错。
    'json.ignore-parse-errors' = 'true',   	 -- 如果设置为 true，则忽略任何解析报错。
    'batch-size' = '16',               -- 批量消费消息的个数
    'request-timeout' = '5000ms',  	-- 请求的超时时间
    'polling-wait-timeout'= '10s', 	-- 获取不到数据情况下的等待时间
    'key-alive-timeout'= '5min'    	-- 含 primary key 的消息，CMQ 去重的有效时间
);
CREATE TABLE `cmq_sink_json_table` (
    `id` int,
    `name` STRING
) WITH (
	'connector' = 'cmq', 					 	-- 必须为 'cmq'
    'hosts' = 'http://cmq-nameserver-vpc-gz.api.tencentyun.com',    -- cmq 所在地域的 nameServer
    'queue' = 'queue_name',			 		-- cmq 的队列名
    'secret-id' = 'xxxx',				   	-- 账号 secretId
    'secret-key' = 'xxxx',         		 	-- 账号 secretKey
    'sign-method' = 'HmacSHA1',     			-- 签名的方式
    'format' = 'json',             		 	-- 定义数据格式（JSON 格式）
    'json.fail-on-missing-field' = 'false',	 -- 如果设置为 false, 则遇到缺失字段不会报错。
    'json.ignore-parse-errors' = 'true',         -- 如果设置为 true，则忽略任何解析报错。
    'batch-size' = '16',                        -- 批量发送消息的个数
    'request-timeout' = '5000ms',               -- 请求的超时时间
    'retry-times' = '3',                        -- 发送消息的重试次数
    'max-block-timeout' = '0s'                  -- 批量发送数据的最大等待时间
);
insert into cmq_sink_json_table select * from cmq_source_json_table;
```

## 注意事项
CMQ 作为数据源（Source）使用的时候，需要考虑如下几点：
1. 数据去重操作，可以设置主键（PRIMARY KEY）来指定去重 key，在一定的时间范围内可以做到数据去重，这个时间范围用户可以自定义，需要注意**这个时间范围设置的越长，消耗的内存越多**。
2. 强烈建议设置 CMQ 的消息隐藏时间大于 Flink 任务的 checkpoint 时间，否则消费的消息会再次被消费到，影响消息处理性能。
