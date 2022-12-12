## 通过 COS 进行外部表数据导入
数据湖计算 DLC 支持在不迁移数据的情况下，直接对对象存储 COS 上的数据进行查询分析，所以您只需将数据导入对象存储 COS 即可开始使用数据湖计算 DLC 进行无缝数据分析，实现数据存储与计算完全解耦。目前支持上传 orc、parquet、arvo、json、csv 和文本文件等多种格式。
目前，对象存储 COS 提供了丰富的数据导入方式，您可根据自身情况选择以下方式进行数据导入。
- 登录 [对象存储 COS](https://console.cloud.tencent.com/cos)，直接进行文件上传，相关操作步骤可参见 [上传对象](https://cloud.tencent.com/document/product/436/13321)。
- 通过对象存储 COS 服务提供的多种上传工具将数据进行导入，工具支持列表可参见 [工具概览](https://cloud.tencent.com/document/product/436/6242)。
- 通过对象存储 COS 服务提供的 SDK 或 API 对数据进行导入，服务相关说明可参见 [上传接口文档](https://cloud.tencent.com/document/product/436/7749)。
- 如您需要将日志服务 CLS 内的日志导入进行分析，可按照分区直接将日志投递到对象存储 COS 后通过数据湖计算 DLC 直接进行分析查询。相关操作可参见 [使用 DLC（Hive）分析 CLS 日志](https://cloud.tencent.com/document/product/614/74783)。
- 如您需要将其他云服务（如数据库 CDB 等）数据导入对象存储 COS ，可以使用数据集成 DataInLong 进行导入。创建数据同步链路时，数据源选择需导出的云服务，目的端选择对象存储 COS 即可完成数据的导入。更多关于数据集成服务的使用介绍可参见 [数据集成](https://cloud.tencent.com/document/product/1580/73382)。

您在进行数据导入时，如遇到问题，可以通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 咨询我们为您提供解决方案。
将数据导入到 COS 后，您可通过数据湖计算 DLC 控制台、API、SDK 进行 SQL 查询，实现建表、分析、结果导出等操作，详细操作可参见 [一分钟入门 DLC 数据分析](https://cloud.tencent.com/document/product/1342/72493)。

## 数据导入原生表[](id:数据代入原生表)
为了提供更好的数据查询性能，数据湖计算 DLC 也支持将数据导入到原生表后进行查询分析。 DLC 原生表基于 Iceberg 表格式排布数据，在导入数据过程中对数据进行优化，如您有以下使用场景，建议使用原生表进行数据查询分析。
- 基于数据仓库分析场景下，希望借助 Iceberg 索引获得更好的分析性能。
- 对数据有更新需求，希望通过 DLC 服务通过 SQL 或数据作业实现 UPSERT 操作。
- 数据通过数据集成 DataInLong、Flink、流计算 Oceanus、Spark Streaming 实时写入更新，读写同时进行，需要事务性保障的数据处理业务。
- 希望使用 Iceberg 表相关特性，如时间旅行、多版本快照、隐藏式分区、分区进化等高级数据湖特性。

如您需要将数据导入到原生表，可根据自身情况选择以下方式进行数据导入。
- 通过 [数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc) 直接导入，详细操作步骤参见 [COS 数据导入](https://cloud.tencent.com/document/product/1342/71417)。
>! 通过控制台进行数据导入时，存在一定使用限制，主要用于快速测试，不建议生产使用。
- 如您的原始数据在 MySQL、Kafka 等业务中，需要将 MySQL binlog 、消息中间件数据分钟级实时写入/更新到 DLC ，可通过数据集成 DataInlong 的实时导入能力实现，详细操作步骤可参见 [DLC 数据实时导入与小文件合并](https://cloud.tencent.com/document/product/1580/81103)。或通过流计算 Oceanus 、Flink写入，如需操作指导可通过 [工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
- 如原始数据在 MySQL、Kafka、MangDB 等数据业务中，可通过数据集成 DataInLong 的离线同步任务（创建步骤参见 [创建离线同步任务](https://cloud.tencent.com/document/product/1580/77357)）将数据转存到原生表。数仓建模过程中，将外部表作为原始数据贴源层，把数据转存到原生表的过程中，可以通过构建稀疏索引等方式结合业务重新排布数据分布，以获得优异的原生表查询分析性能，如需要指导可以 [联系我们](https://yehe.woa.com/document/doc-cn/product-article/1342/52137)。
- 通过 SQL 语法 SELECT INSERT 的方式将外部表的数据查询后写入原生表。如：在数据湖计算 DLC 创建一张与外部表表结构相同的原生表后，通过 SparkSQL 引擎执行 SQL 语法完成转存。语法示例如下：
```
--- 外部表表名：outtertable，原生表表名：innertable
insert into innertable select * from outtertable
```

您在进行数据导入时，如遇到问题，可以通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 咨询我们为您提供解决方案。

## 多数据源联邦查询分析
如您不想将数据导出到对象存储 COS 或数据湖计算 DLC 的原生表中，数据湖计算 DLC 同时提供了数据联邦查询分析能力，支持您在不搬迁数据的情况下，通过 SQL 快速关联分析多个数据源的数据，目前已支持 MySQL、SQLServer、clickhouse、postgreSQL、EMR on HDFS、EMR on COS 等多种数据源。添加联邦分析数据目录操作指南可参见 [数据目录及数据库管理](https://cloud.tencent.com/document/product/1342/71246)。
使用联邦分析时需要数据源与数据引擎在同一个网络下，网络打通、管理可参见 [引擎网络配置](https://cloud.tencent.com/document/product/1342/80433)。
- 通过数据湖计算 DLC 联邦分析 EMR 的数据时，查询性能将会持平甚至超过 EMR 的性能，适用于生产环境，可以在不搬迁 EMR 服务的情况下充分利用 DLC 的全托管弹性能力降本增效。
- 联邦分析可快速联合多个数据源的数据进行分析，为数据洞察、快速分析提供了便利的方式，同时依托于 DLC 的全托管弹性能力，可有效降低使用成本。同时也可以支持使用 INSERT INTO/INSERT OVERWRITE 语法将联邦数据写入到 DLC 原生表，完成数据导入。
- 联邦分析其他数据源时，由于计算过程中需要将数据同步到 DLC 侧进行分析，相比原始数据源直接查询，性能存在一定的损耗，如对查询性能要求较高，可将数据导入到原生表后进行分析，操作方式可见 [数据导入原生表](#.E6.95.B0.E6.8D.AE.E5.AF.BC.E5.85.A5.E5.8E.9F.E7.94.9F.E8.A1.A8.3Ca-id.3D.22.E6.95.B0.E6.8D.AE.E4.BB.A3.E5.85.A5.E5.8E.9F.E7.94.9F.E8.A1.A8.22.3E.3C.2Fa.3E)。

