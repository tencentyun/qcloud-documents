## 介绍
ClickHouse 数据目的表支持将数据写入到 ClickHouse。
>!ClickHouse 数据目的表的表引擎必须使用 CollapsingMergeTree。

## 示例

创建 ETL 作业后，进入**开发调试**页面。在数据目的表处单击**添加**。
![](https://main.qcloudimg.com/raw/ed72b4cfa8ed243f6e7c0c8387d8ee8b.png)
根据示例正确填写 ClickHouse 目的表相应信息。

>!折叠字段：ClickHouse 的 CollapsingMergeTree 引擎在合并算法中添加了折叠行的逻辑。折叠字段在使用 CollapsingMergeTree 引擎建表时所指定：`ENGINE = CollapsingMergeTree(Sign)` 。对 ClickHouse 折叠详细说明可参考 [ClickHouse 官方文档](https://clickhouse.tech/docs/zh/engines/table-engines/mergetree-family/collapsingmergetree/)。

![](https://main.qcloudimg.com/raw/ba73cb32b64832911968d7e751f5aa32.png)
如信息填写无误，ETL 作业会自动获取数据目的表中所有字段的名称和类型（前提为数据源表已正确录入）。
![](https://main.qcloudimg.com/raw/a2f88195451c7cfdd91a8394ca2da20f.png)

## 常见数据类型映射

关于 ClickHouse 支持的数据类型定义及其使用，可参考 [ClickHouse data-types](https://clickhouse.tech/docs/en/sql-reference/data-types/)，这里列举了常用的数据类型，及其与 Flink 类型的对应关系。

| Flink 数据类型                 | ClickHouse 对应数据类型                                      |
| :----------------------------- | :----------------------------------------------------------- |
| VARCHAR                        | String/FixedString(N)                                        |
| STRING                         | String/FixedString(N)                                        |
| BOOLEAN                        | 没有单独类型存储，可以使用 UInt8 来存储布尔类型，将取值限制为0或1；或者使用字符串存储 true/false 来表示 |
| DECIMAL                        | Decimal32(S)/Decimal64(S)/Decimal128(S)                      |
| TINYINT                        | Int8                                                         |
| SMALLINT                       | Int16                                                        |
| INTEGER                        | Int32                                                        |
| BIGINT                         | Int64                                                        |
| FLOAT                          | Float32                                                      |
| DOUBLE                         | Float64                                                      |
| DATE                           | Date                                                         |
| TIMESTAMP                      | DateTime                                                     |
| TIMESTAMP WITH LOCAL TIME ZONE | DateTime，示例 DateTime64(3, 'Asia/Shanghai')                 |

## 注意事项
#### 主键说明
使用 ClickHouse 数据目的表时，需要按照建表语句正确的定义主键，否则有可能无法正确同步修改与删除操作。

## WITH 参数
ClickHouse 数据目的表基于数据仓库 ClickHouse 开发，两者具有相同的WITH参数，具体参数含义用法可参考 [数据仓库 ClickHouse](https://cloud.tencent.com/document/product/849/53389) 。

