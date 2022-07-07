数据订阅 Kafka 版中，您可以通过0.11版本及以上的 [Kafka 客户端](http://kafka.apache.org/downloads) 进行消费订阅数据，本文为您提供 Avro 订阅版本的 Demo 示例，方便您快速测试消费数据的流程，了解数据格式解析的方法。
Demo 中已包含 Avro 协议定义文件，您可以直接使用 Demo 代码，无需另外下载。

> ?当前仅 MySQL、TDSQL-C MySQL 支持 Avro 协议的数据消费。

## 注意事项

- **Demo 并不包含消费数据的用法演示，仅对数据做了打印处理，您需要在此基础上自行编写数据处理逻辑**，您也可以使用其他语言的 Kafka 客户端消费并解析数据。
- 目前不支持通过外网连接数据订阅的 Kafka 进行消费，只支持腾讯云内网的访问，并且订阅的数据库实例所属地域与数据消费的地域相同。
- DTS 中内置的 Kafka 处理单条消息有一定上限，当源库中的单行数据超过10M时，这行数据有可能会被丢弃。

## 消费 Demo 下载
| Demo 语言 | 云数据库 MySQL、TDSQL-C MySQL           |
| ------------- | ------------------------------------------------------------ |
| Go            | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/consumerDemo-avro-go.zip) |
| Java          | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/consumerDemo-avro-java.zip) |
| Python3       | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/consumerDemo-avro-python.zip) |


## Java Demo 使用说明
编译环境：Maven 或者 Gradle 包管理工具，JDK8。用户可自行选择打包工具，如下以 Maven 为例进行介绍。
运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址），安装 JRE8 。
操作步骤：
1. 创建新版数据订阅任务，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Java Demo ，然后解压该文件。
4. 进入解压后的目录，为方便使用，目录下分别放置了 Maven 模型文件、pom.xml 文件，用户根据需要选用。
使用 Maven 进行打包：mvn clean package 。
5. 运行 Demo。
使用 Maven 打包后，进入目标文件夹 target ，运行 `java -jar consumerDemo-avro-1.0-SNAPSHOT.jar --brokers xxx --topic xxx --group xxx --user xxx --password xxx --trans2sql=true`。
其中，`broker` 为数据订阅 Kafka 的内网访问地址，`topic` 为数据订阅任务的订阅 topic，这两个可在 [订阅详情](https://cloud.tencent.com/document/product/571/59966) 页查看，`group`、`user`、`password` 分别为消费组的名称、账号和密码，可在 [消费管理](https://cloud.tencent.com/document/product/571/52378) 页查看，`trans2sql` 表示是否转换为 SQL 语句，java 代码中，携带该参数表示转换为 SQL 语句，不携带则不转换。
> ?携带 trans2sql 时，将使用 `javax.xml.bind.DatatypeConverter.printHexBinary()` 将 byte 值转成16进制，请使用 JDK1.8 版本及以上避免不兼容。如果不需要转 SQL，可以注释此处代码。
6. 观察消费情况。
![](https://main.qcloudimg.com/raw/fffa3de2a6e38b3752512183e1ffe785.png)

## Golang Demo 使用说明
编译环境：Golang 1.12 及以上版本，配置好 Go Module 环境。
运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址）。
操作步骤：
1. 创建新版数据订阅任务，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Golang Demo，然后解压该文件。
4. 进入解压后的目录，运行 `go build -o subscribe ./main/main.go`，生成可执行文件 subscribe。
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
pip install avro
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
Demo 中的文件说明如下，以 Java Demo 为例进行介绍。
- `consumerDemo-avro-java\src\main\resources\avro-tools-1.8.2.jar`：是用来生成 Avro 协议相关代码的工具。
- `consumerDemo-avro-java\src\main\java\com\tencent\subscribe\avro`：Avro 工具生成代码的目录。
- `consumerDemo-avro-java\src\main\resources\Record.avsc`：协议定义文件。

Record.avsc 中我们定义了14个结构（Avro 中叫做 schema），其中主要的数据结构为 Record，用于表示 binlog 中的一条数据，Record 的结构如下，其他数据结构可以在 Record.avsc 中查看：
```
 {
    "namespace": "com.tencent.subscribe.avro",    //第14个，即最后1个 schema 开始，"name" 显示为 "Record"
    "type": "record",    
    "name": "Record",     //"name"显示为"Record"，表示该 schema 为从 kafka 中消费的数据格式
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
| sourceVersion            | 源库版本。等价于 `select version();`     。                      |
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
| readerTimestamp          | 后台处理这条数据的时间，单位为毫秒数。                       |
| tags                     | 一些附加的字段。                                             |
| tags.lowerCaseTableNames | 表名大小写敏感。                                             |
| total                    | 如果消息分片，记录分片总数。当前版本 (version=1) 无意义，预留扩展。 |
| index                    | 如果消息分片，记录分片总数。当前版本 (version=1) 无意义，预留扩展。 |

