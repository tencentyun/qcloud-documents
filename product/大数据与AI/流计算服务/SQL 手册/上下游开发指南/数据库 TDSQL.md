## 介绍
tdsql-subscribe connector 是针对腾讯云 TDSQL-MySQL 数据订阅的专有 connector，通过 [数据订阅](https://cloud.tencent.com/document/product/571/68060) 功能接入 TDSQL-MySQL 的增量 binlog 数据，使用前请确保数据订阅任务已经配置成功。
>! 数据库 TDSQL Connector 目前处于 Beta 版本，如有需求请您 [工单](https://console.cloud.tencent.com/workorder/category) 联系我们。

## 版本说明

| Flink 版本 | 说明  |
|:-------- |:--- |
| 1.11     | 不支持 |
| 1.13     | 支持  |
| 1.14     | 不支持 |

## 使用范围

tdsql-subscribe connector 支持用作数据源表（Source），不可以作为数据流的目的表（Sink）。

## DDL 定义

当 tdsql-subscribe connector 作为 source 时，with 参数大部分与 Kafka connector 参数类似，连接参数都可以在订阅任务中找到。
值得注意的是，在使用 tdsql-subscribe connector 时，`format` 必须指定为 `protobuf`格式，因为数据订阅中，发送到 Kafka 的消息格式为 `protobuf`； 相较于通常使用的 Kafka connector，tdsql-subscribe connector 会多了一些认证信息，认证信息也是源于订阅任务。

### 用作数据源（Source）

#### protobuf 格式输入

```sql
CREATE TABLE `DataInput` (
      `id` INT,
      `name` VARCHAR,
       `age` INT
) WITH (
    'connector' = 'tdsql-subscribe',   -- 注意选择对应的内置  Connector
    'topic' = 'topic-subs-5xop97nffk-tdsqlshard-xxx',  -- 替换为订阅任务消费的 Topic
    'scan.startup.mode' = 'latest-offset', -- 可以是 latest-offset / earliest-offset / specific-offsets / group-offsets 的任何一种
    'properties.bootstrap.servers' = 'guangzhou-kafka-2.cdb-dts.tencentcs.com.cn:3212',  -- 替换为您的订阅任务 Kafka 连接地址
    'properties.group.id' = 'consumer-grp-subs-xxx-kk', 
    'format' = 'protobuf', -- 只能是protobuf格式
    'properties.security.protocol'='SASL_PLAINTEXT', -- 认证协议
    'properties.sasl.mechanism'='SCRAM-SHA-512', -- 认证方式
    'properties.sasl.jaas.config'='org.apache.kafka.common.security.scram.ScramLoginModule required username="account-subs-xxx-username" password="psw";' --用户名和密码
);

CREATE TABLE `jdbc_upsert_sink_table` (
    id INT PRIMARY KEY NOT ENFORCED,  
    name STRING,
    age INT
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://172.28.28.138:3306/testdb', -- 请替换为您的实际 MySQL 连接参数
    'table-name' = 'sink', -- 需要写入的数据表
    'username' = 'user',      -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'psw'  -- 数据库访问的密码
);

INSERT INTO jdbc_upsert_sink_table SELECT * FROM DataInput;
```

## WITH 参数

| 参数值                           | 必填  | 默认值           | 描述                                                                                                                                                                                                                                                                                                                                                                |
|:----------------------------- |:---:|:-------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| connector                     | 是   | 无             | 固定值为 `'tdsql-subscribe'`。                                                                                                                                                                                                                                                                                                                                         |
| topic                         | 是   | 无             | 要读的 Kafka Topic 名。                                                                                                                                                                                                                                                                                                                                                |
| properties.bootstrap.servers  | 是   | 无             | 逗号分隔的 Kafka Bootstrap 地址。                                                                                                                                                                                                                                                                                                                                         |
| properties.group.id           | 是   | 无             | Kafka 消费时的 Group ID。                                                                                                                                                                                                                                                                                                                                              |
| format                        | 是   | 无             | Kafka 消息的输入格式。目前只支持 `protobuf`。                                                                                                                                                                                                                                                                                                                                   |
| scan.startup.mode             | 否   | group-offsets | Kafka consumer 的启动模式。可以是 `latest-offset`、`earliest-offset`、`specific-offsets`、`group-offsets`、`timestamp` 的任何一种。<li/>`'scan.startup.specific-offsets' = 'partition:0,offset:42;partition:1,offset:300'`，使用 `'specific-offsets'` 启动模式时需要指定每个 partition 对应的 offsets。<li/>`'scan.startup.timestamp-miles' = '1631588815000'`，使用 `'timestamp'` 启动模式时需要指定启动的时间戳（单位毫秒）。 |
| scan.startup.specific-offsets | 否   | 无             | 如果 `scan.startup.mode` 的值为`'specific-offsets'`，则必须使用本参数指定具体起始读取的偏移量。例如 `'partition:0,offset:42;partition:1,offset:300'`。                                                                                                                                                                                                                                          |
| scan.startup.timestamp-millis | 否   | 无             | 如果`scan.startup.mode` 的值为`'timestamp'`，则必须使用本参数来指定开始读取的时间点（毫秒为单位的 Unix 时间戳）。            |

## 注意事项

1. 如果订阅任务配置了多库多表或同库多表，需要保证表结构是相同的，才能正确接入订阅任务的数据。
2. 源表中文编码目前仅支持 `utf8` 和 `gbk` 两种。

