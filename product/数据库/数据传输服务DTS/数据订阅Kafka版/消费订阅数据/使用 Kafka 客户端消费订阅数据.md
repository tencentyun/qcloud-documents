## 操作场景

数据订阅 Kafka 版中，您可以通过0.11版本及以上的 [Kafka 客户端](http://kafka.apache.org/downloads) 进行消费订阅数据，本文为您提供了 Java、Go、Python 语言的客户端消费 Demo 示例，方便您快速测试消费数据的流程，了解数据格式解析的方法。

在配置订阅任务中，您可以选择不同的订阅数据格式，ProtoBuf、Avro 和 Json。ProtoBuf 和 Avro 采用二进制格式，消费效率更高，Json 采用轻量级的文本格式，更加简单易用。选择的订阅数据格式不同，参考的 Demo 示例也不同。

本场景提供 Protobuf 订阅版本的 Demo 示例，并且 Demo 中已包含 Protobuf 协议文件，无需另外下载。如果您选择自行下载 [Protobuf 协议文件]( https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/subscribe.proto)，请使用 Protobuf 3.X 版本进行代码生成，以便数据结构可以正确兼容。

## 注意事项

- **Demo 并不包含消费数据的用法演示，仅对数据做了打印处理，您需要在此基础上自行编写数据处理逻辑**，您也可以使用其他语言的 Kafka 客户端消费并解析数据。
- 目前不支持通过外网连接数据订阅的 Kafka 进行消费，只支持腾讯云内网的访问，并且订阅的数据库实例所属地域与数据消费的地域相同。
- DTS 订阅 Kafka 的消息投递语义采用的是至少一次（at least once），所以在特殊情况下消费到的数据可能存在重复。如订阅任务发生重启，重启后拉取源端的 Binlog 会从中断的位点往前多拉取一些，导致重复投递消息。控制台修改订阅对象、恢复异常任务等操作都可能会导致消息重复。如果业务对重复数据敏感，需要用户在消费 Demo 中根据业务数据增加去重逻辑。


## 消费 Demo 下载
| Demo 语言 | 云数据库 MySQL、MariaDB、TDSQL-C MySQL           | TDSQL MySQL                                | TDSQL PostgreSQL                             |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Go            | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/subscribe_kafka_go_demo_1.2.0.zip) | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/tdsql_subscribe_kafka_go_demo_1.0.3.zip) | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/tdsql_postgresql_subscribe_kafka_go_demo_1.0.0.zip) |
| Java          | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/subscribe_kafka_java_demo_1.2.0.zip) | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/tdsql_subscribe_kafka_java_demo_1.0.3.zip) | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/tdsql_postgresql_subscribe_kafka_java_demo_1.0.0.zip) |
| Python3       | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/subscribe_kafka_python_demo_1.2.0.zip) | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/tdsql_subscribe_kafka_python_demo_1.0.3.zip) | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/tdsql_postgresql_subscribe_kafka_python_demo_1.0.0.zip) |


## Java Demo 使用说明
编译环境：Maven 或者 Gradle 包管理工具，JDK8。
运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址），安装 JRE8 。
操作步骤：
1. 创建新版数据订阅任务，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Java Demo ，然后解压该文件。
4. 进入解压后的目录，为方便使用，目录下分别放置了 Maven 模型文件、pom.xml文件和 Gradle 相关配置文件，用户根据需要选用。
  - 使用 Maven 进行打包：mvn clean package 。
  - 使用 Gradle 进行打包：gradle fatJar 打包并包含所有依赖，或者 gradle jar 进行打包。
5. 运行 Demo。
 - 使用 Maven 打包后，进入目标文件夹 target ，运行 `java -jar sub_demo-1.0-SNAPSHOT-jar-with-dependencies.jar --brokers=xxx --topic=xxx --group=xxx--user=xxx --password=xxx --trans2sql`。
 - 使用 Gradle 打包后，进入文件夹 build/libs ，运行 `java -jar sub_demo-with-dependencies-1.0-SNAPSHOT.jar --brokers=xxx --topic=xxx --group=xxx--user=xxx --password=xxx --trans2sql`。
其中，`broker` 为数据订阅 Kafka 的内网访问地址，`topic` 为数据订阅任务的订阅 topic，这两个可在 [订阅详情](https://cloud.tencent.com/document/product/571/59966) 页查看，`group`、`user`、`password` 分别为消费组的名称、账号和密码，可在 [消费管理](https://cloud.tencent.com/document/product/571/52378) 页查看，`trans2sql` 表示是否转换为 SQL 语句，java 代码中，携带该参数表示转换为 SQL 语句，不携带则不转换。
6. 观察消费情况。
![](https://main.qcloudimg.com/raw/fffa3de2a6e38b3752512183e1ffe785.png)

用户也可以使用 IDE 进行编译打包，打包完成后，工程根目录 target 文件夹下的 sub_demo-1.0-SNAPSHOT-jar-with-dependencies 即为一个包含了所需依赖的可运行的 jar 包。

## Golang Demo 使用说明
编译环境：Golang 1.12 及以上版本，配置好 Go Module 环境。
运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址）。
操作步骤：
1. 创建新版数据订阅任务，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Golang Demo，然后解压该文件。
4. 进入解压后的目录，运行 `go build -o subscribe ./main`，生成可执行文件 subscribe。
5. 运行 `./subscribe --brokers=xxx --topic=xxx --group=xxx --user=xxx --password=xxx --trans2sql=true`。
其中，`broker` 为数据订阅 Kafka 的内网访问地址，`topic` 为数据订阅任务的订阅 topic，这两个可在 [订阅详情](https://cloud.tencent.com/document/product/571/59966) 页查看，`group`、`user`、`password` 分别为消费组的名称、账号和密码，可在 [消费管理](https://cloud.tencent.com/document/product/571/52378) 页查看，`trans2sql` 表示是否转换为 SQL 语句。
6. 观察消费情况。
![](https://main.qcloudimg.com/raw/c94d9cfe2a62e903a6593e22ce2c60bf.png)

## Python3 Demo 使用说明
编译运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址），安装 Python3，pip3（用于依赖包安装）。
使用 pip3 安装依赖包：
```
pip install flag
pip install kafka-python
pip install protobuf
```
操作步骤：
1. 创建新版数据订阅任务，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Python3 Demo ，然后解压该文件。
4. 运行 `python main.py --brokers=xxx --topic=xxx --group=xxx --user=xxx --password=xxx --trans2sql=1`。
其中，`broker` 为数据订阅 Kafka 的内网访问地址，`topic` 为数据订阅任务的订阅 topic，这两个可在 [订阅详情](https://cloud.tencent.com/document/product/571/59966) 页查看，`group`、`user`、`password` 分别为消费组的名称、账号和密码，可在 [消费管理](https://cloud.tencent.com/document/product/571/52378) 页查看，`trans2sql` 表示是否转换为 SQL 语句。
5. 观察消费情况。
![](https://main.qcloudimg.com/raw/6055041985904335b43d7df8f4e75561.png)

## [Demo 关键逻辑讲解](id:dgxljjj)

### 消息生产逻辑

下文先对消息生产逻辑进行简要说明，助于用户理解消费逻辑。
我们采用 Protobuf 进行序列化，各语言 Demo 中均附带有 Protobuf 定义文件。文件中定义了几个关键结构：Envelope 是最终发送的 Kafka 消息结构；Entry 是单个订阅事件结构；Entries 是 Entry 的集合。主要数据结构关系如下所示：

![](https://qcloudimg.tencent-cloud.cn/raw/3dcceab6ea08686edf64c0517019d70d.png)

生产过程如下：

1. 拉取 Binlog 消息，将每个 Binlog Event 编码为一个 Entry 结构体。
```
message Entry { //Entry 是单个订阅事件结构，一个事件相当于 MySQL 的一个 binlog event
    Header header = 1;  //事件头
    Event event   = 2;  //事件体
}


message Header {
    int32       version        = 1;   //Entry 协议版本
    SourceType  sourceType     = 2;   //源库的类型信息，包括 MySQL，Oracle 等类型
    MessageType messageType    = 3;   //消息的类型，也就是 Event 的类型，包括 BEGIN、COMMIT、DML 等
    uint32 timestamp           = 4;   //Event 在原始 binlog 中的时间戳
    int64  serverId            = 5;   //源的 serverId
    string fileName            = 6;   //源 binlog 的文件名称
    uint64 position            = 7;   //事件在源 binlog 文件中的偏移量
    string gtid                = 8;   //当前事务的 gtid
    string schemaName          = 9;   //变更影响的 schema
    string tableName           = 10;  //变更影响的 table
    uint64 seqId               = 11;  //全局递增序列号
    uint64 eventIndex          = 12;  //如果大的 event 分片，每个分片从0开始编号，当前版本无意义，留待后续扩展用
    bool   isLast              = 13;  //当前 event 是否 event 分片的最后一块，是则为 true，当前版本无意义，留待后续扩展用
    repeated KVPair properties = 15;
}


message Event {
    BeginEvent      beginEvent      = 1;  //binlog 中的 begin 事件
    DMLEvent        dmlEvent        = 2;  //binlog 中的 dml 事件
    CommitEvent     commitEvent     = 3;  //binlog 中的 commit 事件
    DDLEvent        ddlEvent        = 4;  //binlog 中的 ddl 事件
    RollbackEvent   rollbackEvent   = 5;  //rollback 事件，当前版本无意义
    HeartbeatEvent  heartbeatEvent  = 6;  //源库定时发送的心跳事件
    CheckpointEvent checkpointEvent = 7;  //订阅后台添加的 checkpoint 事件，每10秒自动生成一个，用于 Kafka 生产和消费位点管理
    repeated KVPair properties      = 15;
}
```
2. 为减少消息量，将多个 Entry 合并，合并后的结构为 Entries，Entries.items 字段即为 Entry 顺序列表。合并的数量以合并后不超过 Kafka 单个消息大小限制为标准。对单个 Event 就已超过大小限制的，则不再合并，Entries 中只有唯一 Entry 。
```
message Entries {
        repeated Entry items = 1; //entry list
}
```
3. 对 Entries 进行 Protobuf 编码得到二进制序列。
4. 将 Entries 的二进制序列放入 Envelope 的 data 字段。当存在单个 Binlog Event 过大时，二进制序列可能超过 Kafka 单个消息大小限制，此时我们会将其分割为多段，每段装入一个 Envelope。
Evelope.total 和 Envelope.index 分别记录总段数和当前 Envelope 的序号（从0开始）。
```
message Envelope {
        int32  version                  = 1; //protocol version, 决定了 data 内容如何解码
        uint32 total                    = 2;
        uint32 index                    = 3;
        bytes  data                     = 4; //当前 version 为1, 表示 data 中数据为 Entries 被 PB 序列化之后的结果
        repeated KVPair properties      = 15;
}
```
5. 对上一步生成的一个或多个 Envelope 依次进行 Protobuf 编码，然后投递到 Kafka 分区。同一个 Entries 分割后的多个 Envelope 顺序投递到同一个分区。

### 消息消费逻辑

下文对消费逻辑进行简要说明。我们提供的三种语言的 Demo 均遵循相同的流程。

1. 创建 Kafka 消费者。
2. 启动消费。
3. 依次消费原始消息，并根据消息中的分区找到分区对应的 partitionMsgConsumer 对象，由该对象对消息进行处理。
4. partitionMsgConsumer 将原始消息反序列化为 Envelope 结构。
```
	// 将 Kafka 消息的 Value 值转换为 Envelope
	envelope := subscribe.Envelope{}
	err := proto.Unmarshal(msg.Value, &envelope)
```
5. partitionMsgConsumer 根据 Envelope 中记录的 index 和 total 连续消费一条或者多条消息，直到 Envlope.index 等于 Envelope.total-1（参见上面消费生产逻辑，表示收到了一个完整的 Entries ）。
6. 将收到的连续多条 Envelope 的 data 字段顺序组合到一起。将组合后的二进制序列用 Protobuf 解码为 Entries 。
```
	if envelope.Index == 0 {
		pmc.completeMsg = envelope
	} else {
        // 对进行过拆分的 Entries 二进制序列做拼接
		pmc.completeMsg.Data = append(pmc.completeMsg.Data, envelope.Data...)
	}
	if envelope.Index < envelope.Total-1 {
		return nil
	}
	// 将 Envelope.Data 反序列化为 Entries
	entries := subscribe.Entries{}
	err = proto.Unmarshal(pmc.completeMsg.Data, &entries)

```
7. 对 Entries.items 依次处理，打印原始 Entry 结构或者转化为 SQL 语句。
8. 当消费到 Checkpoint 消息时，做一次 Kafka 位点提交。Checkpoint 消息是订阅后台定时写入 Kafka 的特殊消息，每10秒一个。 

## 数据库字段映射和存储

本节介绍数据库字段类型和序列化协议中定义的数据类型之间的映射关系。
源数据库（如MySQL）字段值在 Protobuf 协议中用如下所示的 Data 结构来存储。

```
message Data {
     DataType     dataType = 1;
     string       charset  = 2;  //DataType_STRING 的编码类型, 值存储在 bv 里面
     string       sv       = 3;  //DataType_INT8/16/32/64/UINT8/16/32/64/Float32/64/DataType_DECIMAL 的字符串值
     bytes        bv       = 4;  //DataType_STRING/DataType_BYTES 的值
}
```
其中 DataType 字段代表存储的字段类型，可取枚举值如下图所示。
```
enum DataType {
     NIL     = 0; //值为 NULL
     INT8    = 1;
     INT16   = 2;
     INT32   = 3;
     INT64   = 4;
     UINT8   = 5;
     UINT16  = 6;
     UINT32  = 7;
     UINT64  = 8;
     FLOAT32 = 9;
     FLOAT64 = 10;
     BYTES   = 11;
     DECIMAL = 12;
     STRING  = 13;
     NA      = 14; //值不存在 (N/A)
}
```
其中 bv 字段存储 STRING 和 BYTES 类型的二进制表示，sv 字段存储 INT8/16/32/64/UINT8/16/32/64/DECIMAL 类型的字符串表示，charset 字段存储 STRING 的编码类型。

MySQL/TDSQL 原始类型与 DataType 映射关系如下（对 UNSIGNED 修饰的 MYSQL_TYPE_INT8/16/24/32/64 分别映射为 UINT8/16/32/32/64）：

> ?
> - `DATE`，`TIME`，`DATETIME` 类型不支持时区。
> - `TIMESTAMP` 类型支持时区，该类型字段表示：存储时，系统会从当前时区转换为 UTC（Universal Time Coordinated）进行存储；查询时，系统会从 UTC 转换为当前时区进行查询。
> - 综上，如下表中 "MYSQL_TYPE_TIMESTAMP" 和 "MYSQL_TYPE_TIMESTAMP_NEW" 字段会携带时区信息，用户在消费数据时可自行转换。（例如，DTS 输出的时间格式是带时区的字符串"2021-05-17 07:22:42 +00:00"，其中，"+00:00"表示 UTC 时间，用户在解析和转换的时候需要考虑时区信息。）

| MySQL 字段类型（TDSQL 支持与 MySQL 相同的类型） | 对应的 Protobuf DataType 枚举值 |
| ------------------------------------------- | ----------------------------- |
| MYSQL_TYPE_NULL                             | NIL                           |
| MYSQL_TYPE_INT8                             | INT8                          |
| MYSQL_TYPE_INT16                            | INT16                         |
| MYSQL_TYPE_INT24                            | INT32                         |
| MYSQL_TYPE_INT32                            | INT32                         |
| MYSQL_TYPE_INT64                            | INT64                         |
| MYSQL_TYPE_BIT                              | INT64                         |
| MYSQL_TYPE_YEAR                             | INT64                         |
| MYSQL_TYPE_FLOAT                            | FLOAT32                       |
| MYSQL_TYPE_DOUBLE                           | FLOAT64                       |
| MYSQL_TYPE_VARCHAR                          | STRING                        |
| MYSQL_TYPE_STRING                           | STRING                        |
| MYSQL_TYPE_VAR_STRING                       | STRING                        |
| MYSQL_TYPE_TIMESTAMP                        | STRING                        |
| MYSQL_TYPE_DATE                             | STRING                        |
| MYSQL_TYPE_TIME                             | STRING                        |
| MYSQL_TYPE_DATETIME                         | STRING                        |
| MYSQL_TYPE_TIMESTAMP_NEW                    | STRING                        |
| MYSQL_TYPE_DATE_NEW                         | STRING                        |
| MYSQL_TYPE_TIME_NEW                         | STRNG                         |
| MYSQL_TYPE_DATETIME_NEW                     | STRING                        |
| MYSQL_TYPE_ENUM                             | STRING                        |
| MYSQL_TYPE_SET                              | STRING                        |
| MYSQL_TYPE_DECIMAL                          | DECIMAL                       |
| MYSQL_TYPE_DECIMAL_NEW                      | DECIMAL                       |
| MYSQL_TYPE_JSON                             | BYTES                         |
| MYSQL_TYPE_BLOB                             | BYTES                         |
| MYSQL_TYPE_TINY_BLOB                        | BYTES                         |
| MYSQL_TYPE_MEDIUM_BLOB                      | BYTES                         |
| MYSQL_TYPE_LONG_BLOB                        | BYTES                         |
| MYSQL_TYPE_GEOMETRY                         | BYTES                         |

