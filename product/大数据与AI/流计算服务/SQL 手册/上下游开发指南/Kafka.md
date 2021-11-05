## 介绍
Kafka 数据管道是流计算系统中最常用的数据源（Source）和数据目的（Sink）。用户可以把流数据导入到 Kafka 的某个 Topic 中，通过 Flink 算子进行处理后，输出到相同或不同 Kafka 示例的另一个 Topic。

Kafka 支持同一个 Topic 多分区读写，数据可以从多个分区读入，也可以写入到多个分区，以提供更高的吞吐量，减少数据倾斜和热点。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## 使用范围
Kafka 支持用作数据源表（Source），也可以作为 Tuple 数据流的目的表（Sink）。

Kafka 还可以与 [Debezium](https://debezium.io/documentation/reference/1.2/tutorial.html)、[Canal](https://github.com/alibaba/canal) 等联用，对 MySQL、PostgreSQL 等传统数据库的变更进行捕获和订阅，然后 Flink 即可对这些变更事件进行进一步的处理。

## DDL 定义

### 用作数据源（Source）

#### JSON 格式输入

```sql
CREATE TABLE `kafka_json_source_table` (
  `id` INT,
  `name` STRING
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
CREATE TABLE `kafka_csv_source_table` (
  `id` INT,
  `name` STRING
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
CREATE TABLE `kafka_debezium_source_table` (
  `id` INT,
  `name` STRING
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
CREATE TABLE `kafka_json_sink_table` (
  `id` INT,
  `name` STRING
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
CREATE TABLE `kafka_csv_sink_table` (
  `id` INT,
  `name` STRING
) WITH (
  -- 定义 Kafka 参数
  'connector' = 'kafka',
  'topic' = 'Data-Output',  -- 替换为您要写入的 Topic
  'properties.bootstrap.servers' = '172.28.28.13:9092',  -- 替换为您的 Kafka 连接地址

  -- 定义数据格式 (CSV 格式)
  'format' = 'csv'
);
```

## WITH 参数

| 参数值                        |      必填       |    默认值     |                             描述                             |
| :---------------------------- | :--------------: | :-----------: | :----------------------------------------------------------: |
| connector  |        是        |      无       |  固定值为 `'kafka'`。
| topic                         |        是        |      无       |                  要读写的 Kafka Topic 名。                   |
| properties.bootstrap.servers  |        是        |      无       |              逗号分隔的 Kafka Bootstrap 地址。               |
| properties.group.id           | 作为数据源时必选 |      无       |                  Kafka 消费时的 Group ID。                   |
| format                        |        是        |      无       | Kafka 消息的输入输出格式。目前支持`'csv'`、`'json'`、`'avro'`、`'debezium-json'`以及`'canal-json'`。 |
| scan.startup.mode             |        否        | group-offsets | Kafka consumer 的启动模式。可以是 `latest-offset`、`earliest-offset`、`specific-offsets`、`group-offsets`、`timestamp` 的任何一种。<li/>`'scan.startup.specific-offsets' = 'partition:0,offset:42;partition:1,offset:300'`，使用 `'specific-offsets'` 启动模式时需要指定每个 partition 对应的 offsets。<li/>`'scan.startup.timestamp-miles' = '1631588815000'`，使用 `'timestamp'` 启动模式时需要指定启动的时间戳（单位毫秒）。 |
| scan.startup.specific-offsets |        否        |      无       | 如果 `scan.startup.mode` 的值为`'specific-offsets'`，则必须使用本参数指定具体起始读取的偏移量。例如 `'partition:0,offset:42;partition:1,offset:300'`。 |
| scan.startup.timestamp-millis |        否        |      无       | 如果`scan.startup.mode` 的值为`'timestamp'`，则必须使用本参数来指定开始读取的时间点（毫秒为单位的 Unix 时间戳）。 |
| sink.partitioner              |        否        |      无       | Kafka 输出时所用的分区器。目前支持的分区器如下：<li>`fixed`：一个 Flink 分区对应不多于一个 Kafka 分区。</li><li>`round-robin`：一个Flink 分区依次被分配到不同的 Kafka 分区。</li><li>自定义分区：也可以通过继承 `FlinkKafkaPartitioner` 类，实现该逻辑。</li> |

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
| csv.allow-comments          | 否   | false      | 忽略 # 开头的注释行，并输出为空行（请务必将 csv.ignore-parse-errors 设为 true）。 |
| csv.array-element-delimiter | 否   | ;          | 数组元素的分隔符，默认是`;`。                                |
| csv.escape-character        | 否   | 无         | 指定转义符，默认禁用转义。                                   |
| csv.null-literal            | 否   | 无         | 将指定的字符串看作 null 值。                                 |

### Debezium 格式 WITH 参数

| 参数值                                  | 必填 | 默认值 |                             描述                             |
| :-------------------------------------- | :--: | :----: | :----------------------------------------------------------: |
| debezium-json.schema-include            |  否  | false  | 设置 Debezium Kafka Connect 时，如果指定了`'value.converter.schemas.enable'`参数，那么 Debezium 发来的 JSON 数据里会包含 Schema 信息，该选项需要设置为 true。 |
| debezium-json.ignore-parse-errors       |  否  | false  |      忽略处理错误。对于无法解析的字段，会输出为 null。       |
| debezium-json.timestamp-format.standard |  否  |  SQL   | 指定 JSON 时间戳字段的格式，默认是 SQL（格式是 `yyyy-MM-dd HH:mm:ss.s{可选精度}`）。也可以选择 ISO-8601，格式是`yyyy-MM-ddTHH:mm:ss.s{可选精度}`。 |

## 代码示例

```sql
CREATE TABLE `kafka_json_source_table` (
  `id` INT,
  `name` STRING
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
CREATE TABLE `kafka_json_sink_table` (
  `id` INT,
  `name` STRING
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
insert into kafka_json_sink_table select * from kafka_json_source_table;
```

## SASL 认证授权
### SASL/PLAIN 用户名密码认证授权
1. 参考 [消息队列 CKafka - 配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528)，设置 Topic 按用户名密码访问的 SASL_PLAINTEXT 认证方式。
2. 参考 [消息队列 CKafka - 添加路由策略](https://cloud.tencent.com/document/product/597/36348)，选择 SASL_PLAINTEXT 接入方式，并以该接入方式下的网络地址访问 Topic。
3. 作业配置 with 参数。
```
CREATE TABLE `YourTable` (
...
) WITH (
  ...
  'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule required username="ckafka-xxxxxxxx#YourUserName" password="YourPassword";',
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'PLAIN',
  ...
);
```

>? `username` 是`实例 ID` + `#` + `刚配置的用户名`，`password` 是刚配置的用户密码。

### SASL/GSSAPI Kerberos 认证授权
腾讯云 CKafka 暂时不支持 Kerberos 认证，您的自建 Kafka 如果开启了 Kerberos 认证，可参考如下步骤配置作业。
1. 获取您的自建 Kafka 集群的 Kerberos 配置文件，如果您基于腾讯云 EMR 集群自建，获取 krb5.conf、emr.keytab 文件，路径如下。
```
/etc/krb5.conf
/var/krb5kdc/emr.keytab
```
2. 对步骤1中获取的文件打 jar 包。
```
jar cvf kafka-xxx.jar krb5.conf emr.keytab
```
3. 校验 jar 的结构（可以通过 vim 命令查看 vim kafka-xxx.jar），jar 里面包含如下信息，请确保文件不缺失且结构正确。
```
META-INF/
META-INF/MANIFEST.MF
emr.keytab
krb5.conf
```
4. 在 [程序包管理](https://console.cloud.tencent.com/oceanus/resource) 页面上传 jar 包，并在作业参数配置里引用该程序包。
5. 获取 kerberos principal，用于作业 [高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
```
klist -kt /var/krb5kdc/emr.keytab

# 输出如下所示，选取第一个即可：hadoop/172.28.28.51@EMR-OQPO48B9
KVNO Timestamp     Principal
---- ------------------- ------------------------------------------------------
  2 08/09/2021 15:34:40 hadoop/172.28.28.51@EMR-OQPO48B9 
  2 08/09/2021 15:34:40 HTTP/172.28.28.51@EMR-OQPO48B9 
  2 08/09/2021 15:34:40 hadoop/VM-28-51-centos@EMR-OQPO48B9 
  2 08/09/2021 15:34:40 HTTP/VM-28-51-centos@EMR-OQPO48B9 
```
6. 作业 with 参数配置。
```
CREATE TABLE `YourTable` (
...
) WITH (
  ...
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'GSSAPI',
  'properties.sasl.kerberos.service.name' = 'hadoop',
  ...
);
```
>? 参数 `properties.sasl.kerberos.service.name` 的值必须与您选取的 principal 匹配，如果您选择的为 `hadoop/${IP}@EMR-OQPO48B9`，那么取值为 hadoop。
>
7. 作业 [高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
```
security.kerberos.login.principal: hadoop/172.28.2.13@EMR-4K3VR5FD
security.kerberos.login.keytab: emr.keytab
security.kerberos.login.conf: krb5.conf
security.kerberos.login.contexts: KafkaClient
fs.hdfs.hadoop.security.authentication: kerberos
```

>! 历史 Oceanus 集群可能不支持该功能，您可通过 [在线客服](https://cloud.tencent.com/act/event/Online_service?from=doc_849) 联系我们升级集群管控服务，以支持 Kerberos 访问。
