## 概述
本文介绍了 HDFS 数据导入 ClickHouse 集群的两种方案。本文介绍两种可行的实践方案，一种适合数据量较少的场景。另一种适合大数据场景。**本文实战基于版本19.16.12.49。**
>?想获取更多关于 ClickHouse 技术交流，可通过 [售后支持](https://cloud.tencent.com/online-service?from=connect-us) 联系我们，届时会将您拉入 ClickHouse 技术交流群。

## 详细步骤
### 外表导入方案
这种方式适合数据量较少的场景，导入步骤如下：
- 在 ClickHouse 中建立 HDFS Engine 外表，用于读取 HDFS 数据。
- 在 ClickHouse 中创建普通表（通常是 MergeTree 系列）存储 HDFS 中的数据。
- 从外表中 SELECT 数据 INSERT 到普通表，完成数据导入。

#### 步骤1：创建 HDFS Engine 外表
```
CREATE TABLE source
(
    `id` UInt32, 
    `name` String, 
    `comment` String
)
ENGINE = HDFS('hdfs://172.30.1.146:4007/clickhouse/globs/*.csv', 'CSV')
```

HDFS Engine 使用方法`ENGINE = HDFS(URI, format)`，可参考 [Table Engine HDFS](https://clickhouse.tech/docs/en/operations/table_engines/hdfs/)。

`URI`为 HDFS 路径，如果包含通配符，则表是只读的。通配符的文件匹配在查询时执行，而不是在创建表时执行。也就是说，如果两次查询之间匹配的文件数目或者内容有变化，两次查询的结果才能够体现这种差异。支持的通配符如下：
- `*`匹配除路径分隔符`/`外的任意数量的字符，包括空字符串。
- `?`匹配一个字符。
- `{some_string,another_string,yet_another_one}`匹配`some_string`、`another_string`或者`yet_another_one`。
- `{N..M}`匹配 N 到 M 的数字，包括 N 和 M，例如`{1..3}`匹配1、2、3。

`format`支持的格式，详见 [Formats for Input and Output Data](https://clickhouse.tech/docs/en/interfaces/formats/#formats)。

#### 步骤2：创建普通表
```
CREATE TABLE dest
(
    `id` UInt32, 
    `name` String, 
    `comment` String
)
ENGINE = MergeTree()
ORDER BY id
```

#### 步骤3：导入数据
```
INSERT INTO dest SELECT *
FROM source
```

#### 步骤4：查询数据
```
SELECT *
FROM dest
LIMIT 2
```

### JDBC Driver 并行导入方案
ClickHouse 提供了 JDBC 的访问方式，并提供了官方的 Driver，此外还有第三方的 Driver，详情可参见 [JDBC Driver](https://clickhouse.tech/docs/en/interfaces/jdbc/)。

ClickHouse 与 Hadoop/Spark 等大数据生态紧密结合，通过开发 Spark 或者 MapReduce 应用，利用大数据平台的并发处理能力，可以将 HDFS 上的大批量数据的快速导入 ClickHouse。Spark 还支持 Hive 等其他数据源，因此这种方式也可实现 Hive 等其他数据源的导入。

**下面举例说明 Spark Python 并发导入数据：**

#### 步骤1：创建普通表
```
CREATE TABLE default.hdfs_loader_table
(
    `id` UInt32, 
    `name` String, 
    `comment` String
)
ENGINE = MergeTree()
PARTITION BY id
ORDER BY id
```

#### 步骤2：开发 Spark Python 应用
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from pyspark.sql import SparkSession
import sys
 
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: clickhouse-spark <path>", file=sys.stderr)
        sys.exit(-1)
 
    spark = SparkSession.builder \
        .appName("clickhouse-spark") \
        .enableHiveSupport() \
        .getOrCreate()
 
    url = "jdbc:clickhouse://172.30.1.15:8123/default"
    driver = 'ru.yandex.clickhouse.ClickHouseDriver'
    properties = {
        'driver': driver,
        "socket_timeout": "300000",
        "rewriteBatchedStatements": "true",
        "batchsize": "1000000",
        "numPartitions": "4",
        'user': 'default',
        'password': 'test'
    }
    spark.read.csv(sys.argv[1], schema="""id INT, name String, comment String""").write.jdbc(
        url=url,
        table='hdfs_loader_table',
        mode='append',
        properties=properties,
    )
```

url 的格式为`jdbc:clickhouse://host:port/database`，其中 port 为 clickhosue 的 HTTP 协议端口，默认为8123。

properties 中的部分参数含义如下：
- `socket_timeout` 为超时时间，单位 ms，详情可参考 [这里](https://github.com/ClickHouse/clickhouse-jdbc/issues/159#issuecomment-364423414)。
- `rewriteBatchedStatements` 打开 JDBC Driver 的批量执行 SQL 功能。
- `batchsize` 批量写入数据条数，可以适当调高，有利于提高写入性能。
- `numPartitions` 数据写入并行度，也决定了 JDBC 并发连接数。`batchsize` 和 `numPartitions` 可参考 [JDBC To Other Databases](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html)。

#### 步骤3：提交 Spark 任务
```
#!/usr/bin/env bash
 
spark-submit \
  --master yarn \
  --jars ./clickhouse-jdbc-0.2.4.jar,./guava-19.0.jar \
  clickhouse-spark.py hdfs:///clickhouse/globs
```
Spark Python 需要注意 `clickhouse-jdbc-0.2.4.jar` 依赖的 jar 版本，可以解压该 jar 文件，查看 pom.xml 中的配置，对比 Spark 环境的 jar 包是否版本匹配。版本不匹配时可能会出现错误 [Could not initialize class ru.yandex.clickhouse.ClickHouseUtil](https://github.com/ClickHouse/clickhouse-jdbc/issues/138)。这时需要下载正确版本的 jar 包，通过 spark-submit 命令行参数 `--jars` 提交。

#### 步骤4：查询数据
```
SELECT *
FROM hdfs_loader_table
LIMIT 2
```

## 补充阅读

下面介绍两种直接读写 HDFS 的方式，一般用作从 HDFS 导入数据到 ClickHouse。这两种方式的读写速度比较慢，且不支持如下功能，可参考 [Table Engine HDFS](https://clickhouse.tech/docs/en/operations/table_engines/hdfs/)：
- `ALTER`、`SELECT...SAMPLE` 操作
- 索引（Indexes）
- 复制（Replication）

### Table Engine
1. 创建表
```
CREATE TABLE hdfs_engine_table(id UInt32, name String, comment String) ENGINE=HDFS('hdfs://172.30.1.146:4007/clickhouse/hdfs_engine_table', 'CSV')
```
1. Insert 测试数据
```
INSERT INTO hdfs_engine_table VALUES(1, 'zhangsan', 'hello zhangsan'),(2, 'lisi', 'hello lisi')
```
1. 查询
```
SELECT * FROM hdfs_engine_table
┌─id─┬─name─────┬─comment────────┐
│  1 │ zhangsan │ hello zhangsan │
│  2 │ lisi     │ hello lisi     │
└────┴──────────┴────────────────┘
```
1. 查看 HDFS 文件
```
hadoop fs -cat /clickhouse/hdfs_engine_table
1,"zhangsan","hello zhangsan"
2,"lisi","hello lisi"
```

### Table Function
在使用上与 Table Engine 方式的区别仅是创建表语法稍有差异，示例如下：
```
CREATE TABLE hdfs_function_table AS hdfs('hdfs://172.30.1.146:4007/clickhouse/hdfs_function_table', 'CSV', 'id UInt32, name String, comment String')
```

## 参考资料
- [ClickHouse Documentation - Table Engine HDFS](https://clickhouse.tech/docs/en/operations/table_engines/hdfs/)
- [ClickHouse Documentation - Table Function hdfs](https://clickhouse.tech/docs/en/query_language/table_functions/hdfs/)
- [如何从 HDFS 导入数据到 ClickHouse？](https://blog.csdn.net/yangzhaohui168/article/details/88583489)
- [How to import my data from hdfs？](https://github.com/ClickHouse/ClickHouse/issues/1614)
- [ClickHouse Documentation - JDBC Driver](https://clickhouse.tech/docs/en/interfaces/jdbc/)
- [Spark JDBC 写 clickhouse 操作总结](https://toutiao.io/posts/m63yw89/preview)
- [将数据通过 spark 从 hive 导入到 Clickhouse](https://wchch.github.io/2018/12/20/将数据通过spark从hive导入到Clickhouse/)
