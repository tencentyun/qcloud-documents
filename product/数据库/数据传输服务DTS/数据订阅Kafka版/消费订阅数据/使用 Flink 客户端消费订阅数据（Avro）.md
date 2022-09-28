## 操作场景

数据订阅 Kafka 版中，针对 Avro 格式的订阅数据，可以使用 Flink 客户端（仅支持客户端类型为 DataStream API）进行消费，本场景为您提供使用 flink-dts-connector 进行数据消费的 Demo 示例。

> ?当前仅 MySQL、TDSQL-C MySQL 支持 Avro 协议的数据消费。

## 前提条件

1. 已 [创建数据消费任务](https://cloud.tencent.com/document/product/571/73076)。
2. 已 [创建消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 已安装 [Flink](https://flink.apache.org/downloads.html) 并能够正常执行 Flink 任务。

## 注意事项

- **Demo 并不包含消费数据的用法演示，仅对数据做了打印处理，您需要在此基础上自行编写数据处理逻辑**，您也可以使用其他语言的 Kafka 客户端消费并解析数据。
- 目前不支持通过外网连接数据订阅的 Kafka 进行消费，只支持腾讯云内网的访问，并且订阅的数据库实例所属地域与数据消费的地域相同。
- DTS 中内置的 Kafka 处理单条消息有一定上限，当源库中的单行数据超过10MB时，这行数据有可能会被丢弃。
- DTS 订阅 Kafka 的消息投递语义采用的是至少一次（at least once），所以在特殊情况下消费到的数据可能存在重复。如订阅任务发生重启，重启后拉取源端的 Binlog 会从中断的位点往前多拉取一些，导致重复投递消息。控制台修改订阅对象、恢复异常任务等操作都可能会导致消息重复。如果业务对重复数据敏感，需要用户在消费 Demo 中根据业务数据增加去重逻辑。

## 消费 Demo 下载

| Demo 语言 | 云数据库 MySQL、TDSQL-C MySQL           |
| ------------- | ------------------------------------------------------------ |
| Java          | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/consumerDemo-avro-flink.zip) |


## Java Flink Demo 使用说明
编译环境：Maven 或者 Gradle 包管理工具，JDK8。用户可自行选择打包工具，如下以 Maven 为例进行介绍。
运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址），安装 JRE8。
操作步骤：

1. 下载 Java Flink Demo，然后解压该文件。
2.  进入解压后的目录，为方便使用，目录下分别放置了 Maven 模型文件、pom.xml 文件，用户根据需要选用。 
`java -jar avro-tools-1.8.2.jar compile -string schema Record.avsc` ：代码生成路径。    
3. 在  pom.xml 文件中修改 Flink 的版本，如下代码中的 version 需要与客户使用的 Flink 版本保持一致。   
```
<dependency>
             <groupId>org.apache.flink</groupId>
             <artifactId>flink-connector-kafka_${scala.binary.version}</artifactId>
             <version>1.13.6</version>
</dependency>
<dependency>
             <groupId>org.apache.flink</groupId>
             <artifactId>flink-streaming-java_${scala.binary.version}</artifactId>
             <version>1.13.6</version>
             <scope>provided</scope>
</dependency>
<dependency>
             <groupId>org.apache.flink</groupId>
             <artifactId>flink-avro</artifactId>
             <version>1.13.6</version>
</dependency>
```   
4. 进入 pom 文件所在的目录，使用 Maven 进行打包，也直接使用 IEDA 打包。
   使用 Maven 进行打包：mvn clean package。
5. 针对 Flink 客户端类型为 DataStream API 的场景，使用 Flink 客户端命令提交任务，启动消费。
`./bin/flink run consumerDemo-avro-flink-1.0-SNAPSHOT.jar --brokers xxx --topic xxx --group xxx --user xxx --password xxx —trans2sql`。
 - `broker` 为数据订阅 Kafka 的内网访问地址，`topic` 为数据订阅任务的订阅 topic，这两个可在 [订阅详情](https://cloud.tencent.com/document/product/571/59966) 页查看。
 - `group`、`user`、`password` 分别为消费组的名称、账号和密码，可在 [消费管理](https://cloud.tencent.com/document/product/571/52378) 页查看。
 - `trans2sql` 表示是否转换为 SQL 语句，java 代码中，携带该参数表示转换为 SQL 语句，不携带则不转换。
6. 观察消费情况。
   查看正在运行的任务。
   ![](https://qcloudimg.tencent-cloud.cn/raw/dfcd7f2b7170394bd821847104f9ab00.png)   
   查看任务详情。
   ![](https://qcloudimg.tencent-cloud.cn/raw/030783f22dc4997310fae8a18e7d6ebe.png)

## [Demo 关键逻辑讲解](id:dgxljjj)
Demo 中的文件说明如下。
- `consumerDemo-avro-flink\src\main\resources\avro-tools-1.8.2.jar`：是用来生成 Avro 协议相关代码的工具。
- `consumerDemo-avro-flink\src\main\java\com\tencent\subscribe\avro`：Avro 工具生成代码的目录。
- `consumerDemo-avro-flink\src\main\resources\Record.avsc`：协议定义文件。

Record.avsc 中我们定义了14个结构（Avro 中叫做 schema），其中主要的数据结构为 Record，用于表示 binlog 中的一条数据，Record 的结构如下，其他数据结构可以在 Record.avsc 中查看：
```
 {
    "namespace": "com.tencent.subscribe.avro",    //Record.avsc 中的最后1个 schema，"name" 显示为 "Record"
    "type": "record",    
    "name": "Record",     //"name" 显示为 "Record"，表示从 kafka 中消费的数据格式
    "fields": [
      {
        "name": "id",     //id 表示全局递增 ID，更多 record 取值解释如下表
        "type": "long",
        "doc": "unique id of this record in the whole stream"
      },
      {
        "name": "version",  //version 表示协议版本
        "type": "int",
        "doc": "protocol version"  
      },
      {
        "name": "messageType",   //消息类型
        "aliases": [
          "operation"
        ],
        "type": {
          "namespace": "com.tencent.subscribe.avro",
          "name": "MessageType",
          "type": "enum",
          "symbols": [
            "INSERT",
            "UPDATE",
            "DELETE",
            "DDL",
            "BEGIN",
            "COMMIT",
            "HEARTBEAT",
            "CHECKPOINT",
            "ROLLBACK"
          ]
        }
      },  
      {
       ……
      },     
 }    
```

Record 中的字段类型解释如下：

| Record 中的字段名称       | 说明                                                   |
| ------------------------ | ------------------------------------------------------------ |
| id                       | 全局递增 ID。                                                 |
| version                  | 协议版本。                                                   |
| messageType              | 消息类型。                                                   |
| fileName                 | binlog 文件名。                                              |
| position                 | binlog 位点。                                                |
| safePosition             | 事务开始的 binlog 位点。                                     |
| timestamp                | binlog 中的时间戳。                                          |
| gtid                     | 事务 gtid。                                                  |
| transactionId            | 事务 ID。                                                    |
| serverId                 | 源库 serverId。                                              |
| threadId                 | 源库线程 ID。                                                |
| sourceType               | 源库的数据库类型。                                           |
| sourceVersion            | 源库版本。等价于 `select version();`。                      |
| schemaName               | 库名。                                                       |
| tableName                | 表名。                                                       |
| objectName               | 库名.表名。                                                  |
| columns                  | 列元数据。                                                   |
| oldColumns               | DML 前的列值。                                               |
| newColumns               | DML 后的列值。                                               |
| sql                      | SQL 语句。                                                   |
| executionTime            | DDL 执行时长。                                                |
| heartbeatTimestamp       | 心跳消息的时间戳。只有 heartbeat 事件有意义。                  |
| syncedGtid               | 已解析 GTID 集合。                                           |
| fakeGtid                 | 是否为构造的假 GTID。                                        |
| pkNames                  | 主键字段。只有 DML 可能有值。                                  |
| readerTimestamp          | 后台处理这条数据的时间，单位为毫秒。                       |
| tags                     | 一些附加的字段。                                             |
| tags.lowerCaseTableNames | 表名大小写敏感。                                             |
| total                    | 如果消息分片，记录分片总数。当前版本 (version=1) 无意义，预留扩展。 |
| index                    | 如果消息分片，记录分片总数。当前版本 (version=1) 无意义，预留扩展。 |

Record 中描述列属性的字段为 "Field"，包含如下四个属性：

- name：列名。
- dataTypeNumber：是 binlog 中记录的数据类型。取值详见 [MySQL](https://dev.mysql.com/doc/internals/en/com-query-response.html)。
- isKey：是否主键。
- originalType：DDL 中定义的类型。

## 数据库字段映射关系

如下为数据库（如 MySQL）字段类型和 Avro 协议中定义的数据类型之间的映射关系。 

| MySQL 类型               | 对应 Avro 中的类型                                     |
| ------------------------ | ------------------------------------------------------ |
| MYSQL_TYPE_NULL          | EmptyObject                                            |
| MYSQL_TYPE_INT8          | Integer                                                |
| MYSQL_TYPE_INT16         | Integer                                                |
| MYSQL_TYPE_INT24         | Integer                                                |
| MYSQL_TYPE_INT32         | Integer                                                |
| MYSQL_TYPE_INT64         | Integer                                                |
| MYSQL_TYPE_BIT           | Integer                                                |
| MYSQL_TYPE_YEAR          | DateTime                                               |
| MYSQL_TYPE_FLOAT         | Float                                                  |
| MYSQL_TYPE_DOUBLE        | Float                                                  |
| MYSQL_TYPE_VARCHAR       | Character                                              |
| MYSQL_TYPE_STRING        | Character，如果原类型为 binary，则对应 BinaryObject    |
| MYSQL_TYPE_VAR_STRING    | Character，如果原类型为 varbinary，则对应 BinaryObject |
| MYSQL_TYPE_TIMESTAMP     | Timestamp                                              |
| MYSQL_TYPE_DATE          | DateTime                                               |
| MYSQL_TYPE_TIME          | DateTime                                               |
| MYSQL_TYPE_DATETIME      | DateTime                                               |
| MYSQL_TYPE_TIMESTAMP_NEW | Timestamp                                              |
| MYSQL_TYPE_DATE_NEW      | DateTime                                               |
| MYSQL_TYPE_TIME_NEW      | DateTime                                               |
| MYSQL_TYPE_DATETIME_NEW  | DateTime                                               |
| MYSQL_TYPE_ENUM          | TextObject                                             |
| MYSQL_TYPE_SET           | TextObject                                             |
| MYSQL_TYPE_DECIMAL       | Decimal                                                |
| MYSQL_TYPE_DECIMAL_NEW   | Decimal                                                |
| MYSQL_TYPE_JSON          | TextObject                                             |
| MYSQL_TYPE_BLOB          | BinaryObject                                           |
| MYSQL_TYPE_TINY_BLOB     | BinaryObject                                           |
| MYSQL_TYPE_MEDIUM_BLOB   | BinaryObject                                           |
| MYSQL_TYPE_LONG_BLOB     | BinaryObject                                           |
| MYSQL_TYPE_GEOMETRY      | BinaryObject                                           |

