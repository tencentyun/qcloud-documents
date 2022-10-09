数据订阅 Kafka 版中，您可以通过0.11版本及以上的 [Kafka 客户端](http://kafka.apache.org/downloads) 进行消费订阅数据， 本文为您提供了 Java、Go、Python 语言的客户端消费 Demo 示例，方便您快速测试消费数据的流程，了解数据格式解析的方法。

在配置订阅任务中，您可以选择不同的订阅数据格式，ProtoBuf、Avro 和 Json。ProtoBuf 和 Avro 采用二进制格式，消费效率更高，Json 采用轻量级的文本格式，更加简单易用。选择的订阅数据格式不同，参考的 Demo 示例也不同。

本场景提供 Json 订阅版本的 Demo 示例，并且 Demo 中已包含 Json 协议文件，无需另外下载。

> ?
>
> 当前仅 MySQL、TDSQL-C MySQL 支持 Json 协议的数据消费。

## 注意事项
- **Demo 并不包含消费数据的用法演示，仅对数据做了打印处理，您需要在此基础上自行编写数据处理逻辑**，您也可以使用其他语言的 Kafka 客户端消费并解析数据。
- 目前不支持通过外网连接数据订阅的 Kafka 进行消费，只支持腾讯云内网的访问，并且订阅的数据库实例所属地域与数据消费的地域相同。
- DTS 中内置的 Kafka 处理单条消息有一定上限，当源库中的单行数据超过10MB时，这行数据有可能会被丢弃。
- DTS 订阅 Kafka 的消息投递语义采用的是至少一次（at least once），所以在特殊情况下消费到的数据可能存在重复。如订阅任务发生重启，重启后拉取源端的 Binlog 会从中断的位点往前多拉取一些，导致重复投递消息。控制台修改订阅对象、恢复异常任务等操作都可能会导致消息重复。如果业务对重复数据敏感，需要用户在消费 Demo 中根据业务数据增加去重逻辑。
- 如果您使用过或者熟悉开源订阅工具 Canal，可以选择将这里消费出来的 Json 格式数据转换成 Canal 工具兼容的数据格式，再进行后续处理，我们的 Demo 中已经提供了相关支持，在启动 Demo 的参数中添加参数 trans2canal 即可实现。目前该功能仅限 Java 语言支持。  


## 消费 Demo 下载
| Demo 语言 | 云数据库 MySQL、TDSQL-C MySQL           |
| ------------- | ------------------------------------------------------------ |
| Go            | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/consumerDemo-json-go.zip) |
| Java          | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/consumerDemo-json-java-1.0.1.zip) |
| Python3       | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/consumerDemo-json-python.zip) |

## Java Demo 使用说明
编译环境：Maven 包管理工具，JDK8。用户可自行选择打包工具，如下以 Maven 为例进行介绍。
运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址），安装 JRE8。
操作步骤：
1. 创建新版数据订阅任务，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Java Demo ，然后解压该文件。
4. 进入解压后的目录，为方便使用，目录下分别放置了 Maven 模型文件、pom.xml 文件，用户根据需要选用。
    使用 Maven 进行打包：mvn clean package。
5. 运行 Demo。
    使用 Maven 打包后，进入目标文件夹 target ，运行如下代码。
  `java -jar consumerDemo-json-1.0-SNAPSHOT.jar --brokers xxx --topic xxx --group xxx --user xxx --password xxx --trans2sql --trans2canal`。
 - `broker` 为数据订阅 Kafka 的内网访问地址，`topic` 为数据订阅任务的订阅 topic，这两个可在 [订阅详情](https://cloud.tencent.com/document/product/571/59966) 页查看。
 - `group`、`user`、`password` 分别为消费组的名称、账号和密码，可在 [消费管理](https://cloud.tencent.com/document/product/571/52378) 页查看，
 - `trans2sql` 表示是否转换为 SQL 语句，java 代码中，携带该参数表示转换为 SQL 语句，不携带则不转换。
 - `trans2canal` 表示是否转换为 Canal 格式打印出来，携带该参数表示转换为 Canal 格式，不携带则不转换。 
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
 - `broker` 为数据订阅 Kafka 的内网访问地址，`topic` 为数据订阅任务的订阅 topic，这两个可在 [订阅详情](https://cloud.tencent.com/document/product/571/59966) 页查看。
 - `group`、`user`、`password` 分别为消费组的名称、账号和密码，可在 [消费管理](https://cloud.tencent.com/document/product/571/52378) 页查看。
 - `trans2sql` 表示是否转换为 SQL 语句。
6. 观察消费情况。
![](https://main.qcloudimg.com/raw/c94d9cfe2a62e903a6593e22ce2c60bf.png)

## Python3 Demo 使用说明
编译运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址），安装 Python3，pip3（用于依赖包安装）。
使用 pip3 安装依赖包：
```
pip install flag
pip install kafka-python
```
操作步骤：
1. 创建新版数据订阅任务，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Python3 Demo ，然后解压该文件。
4. 运行 `python main.py --brokers=xxx --topic=xxx --group=xxx --user=xxx --password=xxx --trans2sql=1`。
 - `broker` 为数据订阅 Kafka 的内网访问地址，`topic` 为数据订阅任务的订阅 topic，这两个可在 [订阅详情](https://cloud.tencent.com/document/product/571/59966) 页查看。
 - `group`、`user`、`password` 分别为消费组的名称、账号和密码，可在 [消费管理](https://cloud.tencent.com/document/product/571/52378) 页查看。
 - `trans2sql` 表示是否转换为 SQL 语句。
5. 观察消费情况。
![](https://main.qcloudimg.com/raw/6055041985904335b43d7df8f4e75561.png)

## [协议文件说明](id:dgxljjj)
Demo 中我们采用 Json 进行序列化，各语言 Demo 中均附带有 Record 定义文件。
Java Demo 中的定义文件路径为 `consumerDemo-json-java\src\main\java\json\FlatRecord.java`。

### Record 中字段类型

| Record 中的字段名称      | 说明                                                   |
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
| sourceVersion            | 源库版本。等价于 `select version();`。           |
| schemaName               | 库名。                                                       |
| tableName                | 表名。                                                       |
| objectName               | 库名.表名。                                                  |
| columns                  | 列元数据。                                                   |
| oldColumns               | DML 前的列值。输出字符串。如果是 binary、geometry 等类型，则输出16进制。 |
| newColumns               | DML 后的列值。输出字符串。如果是 binary、geometry 等类型，则输出16进制。 |
| sql                      | SQL 语句。                                                   |
| executionTime            | DDL 执行时长。                                                |
| heartbeatTimestamp       | 心跳消息的时间戳。只有 heartbeat 事件有意义。                  |
| syncedGtid               | 已解析 GTID 集合。                                           |
| fakeGtid                 | 是否为构造的假 GTID。                                        |
| pkNames                  | 主键字段。只有 DML可能有值。                                  |
| readerTimestamp          | 后台处理这条数据的时间，单位为毫秒。                         |
| tags                     | 一些附加的字段。                                             |
| tags.lowerCaseTableNames | 表名大小写敏感。                                             |
| total                    | 如果消息分片，记录分片总数。当前版本 (version=1) 无意义，预留扩展。 |
| index                    | 如果消息分片，记录分片总数。当前版本 (version=1) 无意义，预留扩展。 |

### Record 中 MySQL 列属性
- name：列名。
- dataTypeNumber：是 binlog 中记录的数据类型。取值详见 [MySQL](https://dev.mysql.com/doc/internals/en/com-query-response.html)。
- isKey：是否主键。
- originalType：DDL 中定义的类型。

### MySQL 数据类型转换逻辑
在 Json 协议中，将 MySQL 类型全部转换成了字符串。
- 对于 varchar 等字符串类型，全部转成了 UTF8 编码。
- 对于数值类型，全部转成了与值相同的字符串，如 "3.0"。
- 对于时间类型，格式为：yyyy-dd-mm hh:MM:ss.milli。
- 对于时间戳类型，输出为毫秒数。
- 对于 binary、blob 等二进制类型，输出为与16进制值相同的字符串，如 "0xfff"。


