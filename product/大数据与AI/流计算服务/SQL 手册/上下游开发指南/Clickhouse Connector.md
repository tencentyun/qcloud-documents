## 介绍
ClickHouse Sink Connector 提供了对 ClickHouse 数据仓库的写入支持。

## 使用范围
ClickHouse 不支持标准的 update 和 delete 操作，且 ClickHouse 通过 mutation 实现的 update 和 delete 功能是异步的。基于这些限制当前版本的 Connector 只支持 SQL 作业 INSERT 数据到 ClickHouse 表，请确保您的任务在使用过程中没有 update 和 delete 操作。对于 JAR 作业（ Java/Scala 编写的作业可以参考 [JDBC](https://cloud.tencent.com/document/product/849/48312) 方式写入 ClickHouse，这里不做阐述）。

## 示例：用作数据目的（Sink）
```SQL
CREATE TABLE clickhouse (
    `id` BIGINT,
    `name` STRING,
    `age` INT,
    `weight` DOUBLE
) WITH (
    -- 指定数据库连接参数
    'connector' = 'clickhouse',                    -- 指定使用clickhouse连接器
    'url' = 'clickhouse://172.28.28.160:8123',     -- 指定集群地址，可以通过ClickHouse集群界面查看
    -- 如果ClickHouse集群未配置账号密码可以不指定
    --'username' = 'root',                         -- ClickHouse集群用户名
    --'password' = 'root',                         -- ClickHouse集群的密码
    'database-name' = 'db',                        -- 数据写入目的数据库
    'table-name' = 'table'                         -- 数据写入目的数据表
);
```

>!目前云数据仓库 ClickHouse 尚未支持用户名和密码鉴权，如果您使用的版本不需要配置用户名密码，忽略对应参数即可。

## 通过 WITH 参数

|         参数值          | 必填 |     默认值      |                             描述                             |
| :---------------------: | :--: | :-------------: | :----------------------------------------------------------: |
|        connector        |  是  |       -        | 当要使用 ClickHouse 作为数据目的（Sink）需要填写，取值 clickhouse |
|           url           |  是  |       -        | ClickHouse 集群连接 url，可以通过集群界面查看，举例 'clickhouse://127.1.1.1:8123' |
|        username         |  否  |       -        |                    ClickHouse 集群用户名                     |
|        password         |  否  |       -        |                     ClickHouse 集群密码                      |
|      database-name      |  是  |       -        |                    ClickHouse 集群数据库                     |
|       table-name        |  是  |       -        |                    ClickHouse 集群数据表                     |
|     sink.batch-size     |  否  |      1000       |                  connector batch 写入的条数                   |
|   sink.flush-interval   |  否  | 1000 （单位 ms） |          connector 异步线程刷新写入 ClickHouse 间隔          |
|    sink.max-retries     |  否  |        3        |                     写入失败时的重试次数                     |
|    sink.write-local     |  否  |      false      | 是否写入本地表。默认 false 不开启写入本地表策略，而通过集群地址写入。<br>当设置为 true 时：</br><li>table-name 参数需要指定为 local table 名字</li><li> 需要通过 sink.write-local-nodes 参数指定 local node ip 和 port 列表</li><li>配合 sink.partition-strategy 指定写 local node 策略</li> |
| sink.write-local-nodes  |  否  |       -        |   local node 列表，举例 '127.1.1.10:8123,127.1.2.13:8123'    |
| sink.partition-strategy |  否  |    balenced     | 数据分发策略，支持 balanced/shuffle/hash。当设置 sink.write-local 为 true 时启用。取值为 hash 时需要配合 sink.partition-key 使用。取值说明：<li>balanced 轮询模式写入</li><li>shuffle 随机挑选节点写入</li><li>hash 根据 partition-key hash 值选择节点写入</li> |
|   sink.partition-key    |  否  |       -        | 当设置 sink.write-loal 为 true 且 sink.partition-strategy 为 hash 时需要设置，值为所定义表中的字段 |

>!定义 WITH 参数时，通常只需要填写必填参数即可。当您启用非必须参数时，请您一定要明确参数含义以及可能对数据写入产生的影响。
 
## 常见数据类型映射
关于 ClickHouse 支持的数据类型定义及其使用，可参考 [ClickHouse data-types](https://clickhouse.tech/docs/en/sql-reference/data-types/)，这里列举常用的数据类型，及其与 Flink 类型的对应关系。

|         Flink 数据类型         |                   ClickHouse 对应数据类型                    |
| :----------------------------: | :----------------------------------------------------------: |
|            VARCHAR             |                    String/FixedString(N)                     |
|             STRING             |                    String/FixedString(N)                     |
|            BOOLEAN             | 没有单独类型存储，可以使用 UInt8 来存储布尔类型，将取值限制为0或1；或者使用字符串存储 true/false 来表示 |
|            DECIMAL             |           Decimal32(S)/Decimal64(S)/Decimal128(S)            |
|            TINYINT             |                             Int8                             |
|            SMALLINT            |                            Int16                             |
|            INTEGER             |                            Int32                             |
|             BIGINT             |                            Int64                             |
|             FLOAT              |                           Float32                            |
|             DOUBLE             |                           Float64                            |
|              DATE              |                             Date                             |
|           TIMESTAMP            |                           DateTime                           |
| TIMESTAMP WITH LOCAL TIME ZONE |         DateTime，示例DateTime64(3, 'Asia/Shanghai')         |
