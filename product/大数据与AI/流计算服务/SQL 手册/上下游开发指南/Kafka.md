## 介绍
Kafka  数据管道是流计算系统中最常用的数据源（Source）和数据目的（Sink）。用户可以把流数据导入到 Kafka 的某个 Topic 中，通过 Flink 算子进行处理后，输出到相同或不同 Kafka 示例的另一个 Topic。

Kafka 支持同一个 Topic 多分区读写，数据可以从多个分区读入，也可以写入到多个分区，以提供更高的吞吐量，减少数据倾斜和热点。

## 使用范围
Kafka 支持用作数据源表（Source），也可以作为 Tuple 数据流的目的表（Sink），暂不支持 Upsert 数据流。

Kafka 还可以与 [Debezium](https://debezium.io/documentation/reference/1.2/tutorial.html)、[Canal](https://github.com/alibaba/canal) 等联用，对 MySQL、PostgreSQL 等传统数据库的变更进行捕获和订阅，然后 Flink 即可对这些变更事件进行进一步的处理。

## 示例
### 用作数据源（Source）
#### JSON 格式输入
```sql
CREATE TABLE `Data-Input` (
      `time` VARCHAR,
      `client_ip` VARCHAR,
      `method` VARCHAR
) WITH (
    -- 定义 Kafka 参数
    'connector' = 'kafka',
    'topic' = 'Data-Input',  -- 替换为您要消费的 Topic
    'scan.startup.mode' = 'latest-offset', -- 可以是 latest-offset / earliest-offset / specific-offsets / group-offsets / timestamp 的任何一种
    'properties.bootstrap.servers' = '172.28.28.13:9092',  -- 替换为您的 Kafka 连接地址
    'properties.group.id' = 'testGroup', -- 必选参数, 一定要指定 Group ID

    -- 定义数据格式 (JSON 格式)
    'format' = 'json',
    'json.fail-on-missing-field' = 'false',  -- 如果设置为 false, 则遇到缺失字段不会报错。
    'json.ignore-parse-errors' = 'true'    -- 如果设置为 true，则忽略任何解析报错。
);
```

#### CSV 格式输入
```sql
CREATE TABLE `Data-Input` (
      `time` VARCHAR,
      `client_ip` VARCHAR,
      `method` VARCHAR
) WITH (
    -- 定义 Kafka 参数
    'connector' = 'kafka',
    'topic' = 'Data-Input',  -- 替换为您要消费的 Topic
    'scan.startup.mode' = 'latest-offset', -- 可以是 latest-offset / earliest-offset / specific-offsets / group-offsets / timestamp 的任何一种
    'properties.bootstrap.servers' = '172.28.28.13:9092',  -- 替换为您的 Kafka 连接地址
    'properties.group.id' = 'testGroup', -- 必选参数, 一定要指定 Group ID

    -- 定义数据格式 (CSV 格式)
    'format' = 'csv'
);
```

#### Debezium 格式输入
```sql
CREATE TABLE `Data-Input` (
      `time` VARCHAR,
      `client_ip` VARCHAR,
      `method` VARCHAR
) WITH (
    -- 定义 Kafka 参数
    'connector' = 'kafka',
    'topic' = 'Data-Input',  -- 替换为您要消费的 Topic
    'scan.startup.mode' = 'latest-offset', -- 可以是 latest-offset / earliest-offset / specific-offsets / group-offsets / timestamp 的任何一种
    'properties.bootstrap.servers' = '172.28.28.13:9092',  -- 替换为您的 Kafka 连接地址
    'properties.group.id' = 'testGroup', -- 必选参数, 一定要指定 Group ID

    -- 定义数据格式 (Debezium 输出的 JSON 格式)
    'format' = 'debezium-json'
);
```

### 用作数据目的（Sink）
#### JSON 格式输出
```sql
CREATE TABLE `Data-Output` (
      `time` VARCHAR,
      `client_ip` VARCHAR,
      `method` VARCHAR
) WITH (
    -- 定义 Kafka 参数
    'connector' = 'kafka',
    'topic' = 'Data-Output',  -- 替换为您要写入的 Topic
    'properties.bootstrap.servers' = '172.28.28.13:9092',  -- 替换为您的 Kafka 连接地址

    -- 定义数据格式 (JSON 格式)
    'format' = 'json',
    'json.fail-on-missing-field' = 'false',  -- 如果设置为 false, 则遇到缺失字段不会报错。
    'json.ignore-parse-errors' = 'true'    -- 如果设置为 true，则忽略任何解析报错。
);
```

#### CSV 格式输出
```sql
CREATE TABLE `Data-Output` (
      `time` VARCHAR,
      `client_ip` VARCHAR,
      `method` VARCHAR
) WITH (
    -- 定义 Kafka 参数
    'connector' = 'kafka',
    'topic' = 'Data-Output',  -- 替换为您要写入的 Topic
    'properties.bootstrap.servers' = '172.28.28.13:9092',  -- 替换为您的 Kafka 连接地址

    -- 定义数据格式 (CSV 格式)
    'format' = 'csv'
);
```

## 通用 WITH 参数

| 参数值                        |      必填       |    默认值     |                             描述                             |
| :---------------------------- | :--------------: | :-----------: | :----------------------------------------------------------: |
| connector  |        是        |      无       | 建议输入 `'kafka'`，并在内置 Connector 选框中选择 `flink-connector-kafka`。如果确实有读写旧版 Kafka 的需求，可以输入 `'kafka-0.11'`，并选择 `flink-connector-kafka-0.11`。 |
| topic                         |        是        |      无       |                  要读写的 Kafka Topic 名。                   |
| properties.bootstrap.servers  |        是        |      无       |              逗号分隔的 Kafka Bootstrap 地址。               |
| properties.group.id           | 作为数据源时必选 |      无       |                  Kafka 消费时的 Group ID。                   |
| format                        |        是        |      无       | Kafka 消息的输入输出格式。目前支持`'csv'`、`'json'`、`'avro'`、`'debezium-json'`以及`'canal-json'`。 |
| scan.startup.mode             |        否        | group-offsets | Kafka 消费时的起始坐标，目前支持`'earliest-offset'`、`'latest-offset'`、`'group-offsets'`、`'timestamp'`以及`'specific-offsets'`。 |
| scan.startup.specific-offsets |        否        |      无       | 如果 `scan.startup.mode` 的值为`'specific-offsets'`，则必须使用本参数指定具体起始读取的偏移量。例如 `'partition:0,offset:42;partition:1,offset:300'`。 |
| scan.startup.timestamp-millis |        否        |      无       | 如果`scan.startup.mode` 的值为`'timestamp'`，则必须使用本参数来指定开始读取的时间点（毫秒为单位的 Unix 时间戳）。 |
| sink.partitioner              |        否        |      无       | Kafka 输出时所用的分区器。目前支持的分区器如下：<li>`fixed`：一个 Flink 分区对应不多于一个 Kafka 分区。</li><li>`round-robin`：一个Flink 分区依次被分配到不同的 Kafka 分区。</li><li>自定义分区：也可以通过继承 `FlinkKafkaPartitioner` 类，实现该逻辑。</li> |

## JSON 格式 WITH 参数

| 参数值                         | 必填 | 默认值 | 描述                                                         |
| ------------------------------ | ----- | ------ | ------------------------------------------------------------ |
| json.fail-on-missing-field     | 否    | false  | 如果为 true，则遇到缺失字段时，会让作业失败。如果为 false（默认值），则只会把缺失字段设置为 null 并继续处理。 |
| json.ignore-parse-errors       | 否    | false  | 如果为 true，则遇到解析异常时，会把这个字段设置为 null 并继续处理。如果为 false，则会让作业失败。 |
| json.timestamp-format.standard | 否    | SQL    | 指定 JSON 时间戳字段的格式，默认是 SQL（格式是`yyyy-MM-dd HH:mm:ss.s{可选精度}`）。也可以选择 ISO-8601，格式是 `yyyy-MM-ddTHH:mm:ss.s{可选精度}`。 |

## CSV 格式 WITH 参数

| 参数值                      | 必填 | 默认值     | 描述                                                         |
| --------------------------- | ----- | ---------- | ------------------------------------------------------------ |
| csv.field-delimiter         | 否    | ,          | 指定 CSV 字段分隔符，默认是半角逗号。                        |
| csv.line-delimiter          | 否    | U&'\\000A' | 指定 CSV 的行分隔符，默认是换行符`\n`，SQL 中必须用`U&'\000A'`表示。如果需要使用回车符`\r`，SQL 中必须使用`U&'\000D'`表示。 |
| csv.disable-quote-character | 否    | false| 禁止字段包围引号。如果为 true，则 'csv.quote-character' 选项不可用。|
| csv.quote-character         | 否    | ''         | 字段包围引号，引号内部的作为整体看待。默认是`''`。          |
| csv.ignore-parse-errors     | 否    | false      | 忽略处理错误。对于无法解析的字段，会输出为 null。            |
| csv.allow-comments          | 否    | false     | 忽略 # 开头的注释行，并输出为空行（请务必将 csv.ignore-parse-errors 设为 true）。|
| csv.array-element-delimiter | 否    | ;          | 数组元素的分隔符，默认是`;`。                               |
| csv.escape-character        | 否    | 无         | 指定转义符，默认禁用转义。                                   |
| csv.null-literal            | 否    | 无         | 将指定的字符串看作 null 值。                                 |

## Debezium 格式 WITH 参数

| 参数值                                  | 必填 | 默认值 |                             描述                             |
| :-------------------------------------- | :---: | :----: | :----------------------------------------------------------: |
| debezium-json.schema-include            |  否   | false  | 设置 Debezium Kafka Connect 时，如果指定了`'value.converter.schemas.enable'`参数，那么 Debezium 发来的 JSON 数据里会包含 Schema 信息，该选项需要设置为 true。 |
| debezium-json.ignore-parse-errors       |  否   | false  |   忽略处理错误。对于无法解析的字段，会输出为 null。      |
| debezium-json.timestamp-format.standard |  否   |  SQL   | 指定 JSON 时间戳字段的格式，默认是 SQL（格式是 `yyyy-MM-dd HH:mm:ss.s{可选精度}`）。也可以选择 ISO-8601，格式是`yyyy-MM-ddTHH:mm:ss.s{可选精度}`。 |
