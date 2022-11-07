Flink 核心是一个开源的分布式、高性能、高可用、准确的数据流执行引擎，其针对数据流的分布式计算提供了数据分布、数据通信以及容错机制等功能。基于流执行引擎，Flink 提供了更高抽象层的 API 以便您编写分布式任务。
- 分布式：表示 FLink 程序可以运行在多台机器上。
- 高性能：表示 Flink 处理性能比较高。
- 高可用：表示 Flink 支持程序的自动重启机制。
- 准确的：表示 Flink 可以保证处理数据的准确性。
![](https://qcloudimg.tencent-cloud.cn/raw/3c8a93de4b8e444fe1c5c7cd1074e53b.png)

下图中左边是数据源，从这里可以看出来，这些数据是实时生产的一些日志，或者是数据库，文件系统，kv 存储系统中的数据。中间是 Flink，负责对数据进行梳理。右边是目的地，Flink 可以将计算好的数据输出到其它应用系统中，或者存储系统中。总结的来说 Flink 的三大核心组件如下：
- Data Source：也就是图中左边的数据源。
- Transformations：算子（负责对数据进行处理）。
- Data Sink：输出组件（负责把计算好的数据输出到其它应用系统中）。
![](https://qcloudimg.tencent-cloud.cn/raw/daff84e47463d9ca82b107845b1e38b2.png)

## 使用场景
Flink 主要有以下三种应用场景：
- Extract-transform-load（实时 ETL 和数据流）
![](https://qcloudimg.tencent-cloud.cn/raw/607d06d06427a13c8d13f4da30971237.png)
- 实时数据分析
![](https://qcloudimg.tencent-cloud.cn/raw/3cc7a4362223ebde31ee000446f9b7ea.png)
- 事件驱动应用
![](https://qcloudimg.tencent-cloud.cn/raw/fd79b2239edc473ba13a46b89563fbff.png)
 
相关分层 API 请参考以下文档：
![](https://qcloudimg.tencent-cloud.cn/raw/d8faa64c904b167622097c0a5b8432d4.png)
- [Table API & SQL](https://nightlies.apache.org/flink/flink-docs-release-1.9/dev/table/) ：Table API 一般与 DataSet 或者 DataStream 紧密关联，可以通过一个 DataSet 或者 DataStream 创建出一个 Table，然后再使用类似 flilter、sum、join、select 等这种操作。最近还可以将一个 Table 对象转换成 DataSet 或者 DataStream。SQL API 的底层是基于 Apache Calcite，Apache Calcite 实现了标准 SQL，使用起来比其它 API 更加灵活，因为可以直接使用 SQL 语句。Table API 和 SQL API 可以很容易地结合在一块使用。因为它们都返回 Table 对象。
- [DataStream API](https://nightlies.apache.org/flink/flink-docs-release-1.9/dev/datastream_api.html) & [DataSet API](https://nightlies.apache.org/flink/flink-docs-release-1.9/dev/batch/) ：主要提供针对流数据和批数据的处理，是对低级 API 进行了一些封装，提供了 flilter、sum、max、min等高阶函数，简单易用，所以这些 API 在实际生产中应用还是比较广泛的。
- [Stateful Stream Processing](https://nightlies.apache.org/flink/flink-docs-release-1.9/dev/api_concepts.html) ：提供了对时间和状态的细粒度控制，简洁性和易用性较差，主要应用在一些复杂事件处理逻辑上。

## 环境信息
- Flink 默认部署在集群的 Master、Core 节点，安装了 Flink 组件的集群其功能都是开箱即用的。
- 登录机器后使用命令 su hadoop 切换到 hadoop 用户进行一些Flink的本地测试。
- Flink 软件路径在 /usr/local/service/flink 下。
- 相关日志路径在 /data/emr/flink/logs 下。
 
更多详细资料请参考 [社区文档](https://flink.apache.org/)。

