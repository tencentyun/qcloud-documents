数据订阅 Kafka 版中，您可以直接通过0.11版本及以上的 Kafka 客户端进行消费订阅数据，本文为您提供了 Java、Go、Python 语言的客户端消费 Demo。

## 消费 Demo 下载（云数据库 MySQL、MariaDB）
参考下表下载数据订阅 Kafka 版客户端消费 Demo 代码：

| Demo 语言 | 下载地址                                             |
| ------------- | ------------------------------------------------------------ |
| Go            | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/subscribe_kafka_go_demo_1.1.1.zip) |
| Java          | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/subscribe_kafka_java_demo_1.1.1.zip) |
| Python3       | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/subscribe_kafka_python_demo_1.1.1.zip) |

## 消费 Demo 下载（TDSQL MySQL版）
参考下表下载数据订阅 Kafka 版客户端消费 Demo 代码：

| Demo 语言 | 下载地址                                             |
| ------------- | ------------------------------------------------------------ |
| Go            | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/tdsql_subscribe_kafka_go_demo_1.0.0.zip) |
| Java          | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/tdsql_subscribe_kafka_java_demo_1.0.0.zip) |
| Python       | [地址](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/tdsql_subscribe_kafka_python_demo_1.0.0.zip) |

## 配置参数说明
| 参数       | 说明                        |
| ---------- | --------------------------- |
| brokerlist | 数据订阅 Kafka 的内网访问地址 |
| topic      | 数据订阅通道的订阅 topic     |
| group      | 消费组名称                  |
| user        | 消费组账号名                |
| password   | 消费组密码                  |
| trans2sql  | 是否转换为 SQL 语句    | 


## [Demo 关键逻辑讲解](id:dgxljjj)
### 生产逻辑
下文对消息生产逻辑进行简要说明，助于用户理解消费逻辑。
我们采用 Protobuf 进行序列化，各语言 Demo 中均附带有 Protobuf 定义文件。文件中定义了几个关键结构：Envelope 是最终发送的 Kafka 消息结构；Entry 是单个订阅事件结构；Entries 是多个 Entry 的集合。

生产过程如下：
1. 拉取 Binlog 消息，将每个 Binlog Event 编码为一个 Entry 结构体。
![](https://main.qcloudimg.com/raw/2ba445362f3e0f65dd368742965ff921.png)
2. 为减少消息量，将多个 Entry 合并，合并后的结构为 Entries，Entries.items 字段即为 Entry 顺序列表。合并的数量以合并后不超过 Kafka 单个消息大小限制为标准。对单个 Event 就已超过大小限制的，则不再合并，Entries 中只有唯一 Entry 。
![](https://main.qcloudimg.com/raw/79f305c3d844b580940636cd228b2299.png)
3. 对 Entries 进行 Protobuf 编码得到二进制序列。
4. 将 Entries 的二进制序列放入 Envelope 的 data 字段。当存在单个 Binlog Event 过大时，二进制序列可能超过 Kafka 单个消息大小限制，此时我们会将其分割为多段，每段装入一个 Envelope。
Envelope.index 和 Evelope.total 分别记录总段数和当前 Envelope 的序号（从0开始）。
![](https://main.qcloudimg.com/raw/c997e3d7ae2211e772a9db25281e5768.png)
5. 对上一步生成的一个或多个 Envelope 依次进行 Protobuf 编码，然后投递到 Kafka 分区。同一个 Entries 分割后的多个 Envelope 顺序投递到同一个分区。

### 消费逻辑
下文对消费逻辑进行简要说明。我们提供的三种语言的 Demo 均遵循相同的流程。
1. 创建 Kafka 消费者。
2. 启动消费。
3. 依次消费原始消息，并根据消息中的分区找到分区对应的 partitionMsgConsumer 对象，由该对象对消息进行处理。
4. partitionMsgConsumer 将原始消息反序列化为 Envelope 结构。
![](https://main.qcloudimg.com/raw/0605c87fc818a9100fdb1ac941f83ea3.png)
5. partitionMsgConsumer 根据 Envelope 中记录的 index 和 total 连续消费一条或者多条消息，直到 Envlope.index 等于 Envelope.total-1（参见上面消费生产逻辑，表示收到了一个完整的 Entries ）。
6. 将收到的连续多条 Envelope 的 data 字段顺序组合到一起。将组合后的二进制序列用 Protobuf 解码为 Entries 。
![](https://main.qcloudimg.com/raw/a5368cd3c3ef9ec800a25d97ce5c13e0.png)
7. 对 Entries.items 依次处理，打印原始 Entry 结构或者转化为 SQL 语句。
![](https://main.qcloudimg.com/raw/dd45ebaeaed65efc50d3210c722b2806.png)

## Java Demo 使用说明
编译环境：Maven 或者 Gradle 包管理工具，JDK8。
运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址），安装 JRE8 。
操作步骤：
1. 创建新版数据订阅通道，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Java Demo ，然后解压该文件。
4. 进入解压后的目录，为方便使用，目录下分别放置了 Maven 模型文件、pom.xml文件和 Gradle 相关配置文件，用户根据需要选用。
  - 使用 Maven 进行打包：mvn clean package 。
  - 使用 Gradle 进行打包：gradle fatJar 打包并包含所有依赖，或者 gradle jar 进行打包。
5. 运行：使用 Maven 打包后，进入目标文件夹 target ，运行 `java -jar sub_demo-1.0-SNAPSHOT-jar-with-dependencies.jar --brokers=xxx --topic=xxx --group=xxx--user=xxx --password=xxx --trans2sql`。
使用 Gradle 打包后，进入文件夹 build/libs ，运行 `java -jar sub_demo-with-dependencies-1.0-SNAPSHOT.jar --brokers=xxx --topic=xxx --group=xxx--user=xxx --password=xxx --trans2sql`。
6. 观察消费情况。
![](https://main.qcloudimg.com/raw/fffa3de2a6e38b3752512183e1ffe785.png)

用户也可以使用 IDE 进行编译打包，以 IntelliJ IDEA 软件为例：
1. 打开 IntelliJ IDEA 软件，然后单击【Open】 。
![](https://main.qcloudimg.com/raw/9d199900b36a43840825dc52dfa2c567.png)
2. 在弹出的对话框，找到 Demo 解压的目录，参照下图找到目录下的 pom.xml 文件，单击【Open】。
![](https://main.qcloudimg.com/raw/1747158bf764aa898468bfa2bdb22054.png)
3. 在弹出对话框，单击【Open as Project】。
![](https://main.qcloudimg.com/raw/6b169744f3529f362fb81bb86becf593.png)
4. 在打开的窗口，双击右侧 Maven 管理窗口 Lifecycle 中的 package，进行打包。
![](https://main.qcloudimg.com/raw/63d85885b88dce1d65483abea6b9d3d3.png)
打包完成后。工程根目录 target 文件夹下的 sub_demo-1.0-SNAPSHOT-jar-with-dependencies 即为一个包含了所需依赖的可运行的 jar 包。
对于 Gradle 也是相似的操作流程。

## Golang Demo 使用说明
编译环境：Golang 1.12 及以上版本，配置好 Go Module 环境。
运行环境：腾讯云服务器（需要与订阅实例相同地域，才能够访问到 Kafka 服务器的内网地址）。
操作步骤：
1. 创建新版数据订阅通道，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Golang Demo，然后解压该文件。
4. 进入解压后的目录，运行`go build -o subscribe ./main`，生成可执行文件 subscribe。
5. 运行 `./subscribe --brokers=xxx --topic=xxx --group=xxx --user=xxx \--password=xxx --trans2sql=true`。
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
1. 创建新版数据订阅通道，详情请参见 [数据订阅 Kafka版](https://cloud.tencent.com/document/product/571/52412)。
2. 创建一个或多个消费组，详情请参见 [新增消费组](https://cloud.tencent.com/document/product/571/52377)。
3. 下载 Python3 Demo ，然后解压该文件。
4. 运行`python main.py --brokers=xxx --topic=xxx --group=xxx --user=xxx \--password=xxx --trans2sql=1`。
5. 观察消费情况。
![](https://main.qcloudimg.com/raw/6055041985904335b43d7df8f4e75561.png)
