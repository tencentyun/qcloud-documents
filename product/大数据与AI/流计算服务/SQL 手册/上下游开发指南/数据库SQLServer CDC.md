## 介绍
SQLServer 的 CDC 源表（即 SQLServer 的流式源表），SQLServer CDC Connector 允许从 SQLServer 数据库读取全量数据和增量数据。本文档介绍如何设置 SQLServer CDC Connector。

## 版本说明

| Flink 版本 | 说明   |
| :-------- | :----- |
| 1.11      | 不支持 | 
| 1.13      | 支持   |
| 1.14      | 不支持 |

## 使用范围
SQLServer CDC 只支持作为源表。

## SQLServer 数据库配置
SQLServer 源表需要启用变更数据捕获。
1. 启用数据库变更捕获，参考云数据 SQL Server [变更数据捕获](https://cloud.tencent.com/document/product/238/59259)。
2. 为 SQLServer 源表启用变更数据捕获，参考文档 [sys.sp_cdc_enable_table](https://learn.microsoft.com/zh-cn/sql/relational-databases/system-stored-procedures/sys-sp-cdc-enable-table-transact-sql?view=sql-server-ver16)。
```sql
USE MyDB
GO

EXEC sys.sp_cdc_enable_table
@source_schema = N'dbo',     -- 指定源表所属的 schema 名
@source_name   = N'MyTable', -- 指定需要读取的源表名
@role_name     = NULL,  -- 指定一个角色 MyRole，您可以向该角色添加要对源表的捕获列授予 SELECT 权限的用户。sysadmin 或 db_owner 角色的用户也可以访问指定的源表。将 @role_name 的值设置为 NULL，以仅允许使用 sysadmin 或 db_owner 中的用户。
@filegroup_name = NULL, -- 要用于为捕获实例创建的更改表的文件组，可以为 NULL。 如果指定，则必须为当前数据库定义 filegroup_name 。 如果为 NULL，则使用默认文件组。
@supports_net_changes = 0 -- 是否为此捕获实例启用对查询净更改的支持。 如果表具有主键或表具有使用 @index_name 参数标识的唯一索引，则supports_net_changes 默认值为 1。 否则，该参数默认为 0。如果为 0，则只生成查询所有更改的支持函数。如果为 1，则还会生成查询净更改所需的函数。如果 supports_net_changes 设置为 1，则必须指定 index_name ，或者源表必须具有定义的主键。
GO
```

3. 检查源表是否启动变更数据捕获，参考文档 [sys.sp_cdc_help_change_data_capture](https://learn.microsoft.com/zh-cn/sql/relational-databases/system-stored-procedures/sys-sp-cdc-help-change-data-capture-transact-sql?view=sql-server-ver16)。
```sql
USE MyDB
GO

EXEC sys.sp_cdc_help_change_data_capture
GO
```



## DDL 定义
```sql
-- register a SqlServer table 'orders' in Flink SQL
CREATE TABLE orders (
    id INT,
    order_date DATE,
    purchaser INT,
    quantity INT,
    product_id INT,
    PRIMARY KEY (id) NOT ENFORCED
) WITH (
    'connector' = 'sqlserver-cdc',
    'hostname' = 'localhost',
    'port' = '1433',
    'username' = 'sa',
    'password' = 'Password!',
    'database-name' = 'inventory',
    'schema-name' = 'dbo',
    'table-name' = 'orders'
);

-- read snapshot and binlogs from orders table
SELECT * FROM orders;
```

## WITH 参数

| 参数                      | 必填                                            | 默认值 | 类型 | 描述                    |
| :------------------------ | :----------------------------------------------------------- | :------- | :------------------------ | ------------------------- |
| connector                 | 是                                          | 无      | String | 固定值为 `sqlserver-cd` |
| hostname         | 是   | 无     | String  | SQLSerer 数据库 IP 地址或主机名                              |
| username         | 是   | 无     | String  | SQLSerer 数据库用户名                                        |
| password         | 是   | 无     | String  | SQLSerer 数据库密码                                          |
| database-name    | 是   | 无     | String  | SQLSerer 源表所属数据库名                                    |
| schema-name      | 是   | 无     | String  | SQLSerer 源表所属 schema 名。支持 Java 正则表达式，例如 (dbo.*) 可匹配 dbo、dbo1、dbo_test，对于正则表达式，强烈建议放置于括号内，以防止与 table-name 组合时出现错误 |
| table-name       | 是   | 无     | String  | SQLServer 源表名。支持 Java 正则表达式，对于正则表达式，强烈建议放置于括号内，以防止与 schema-name 组合时出现错误 |
| port             | 否   | 1433   | Integer | SQLSerer 数据库端口                                          |
| server-time-zone | 否   | UTC    | String  | SQLSerer 数据库会话时区设置，例如 'Asia/Shanghai'            |
| debezium.*       | 否   | 无     | String  | Debezium 属性参数，从更细粒度控制 Debezium 客户端的行为。例如 'debezium.snapshot.mode' = 'initial_only'，详情参见 [Debezium's SQLServer Connector properties](https://debezium.io/documentation/reference/1.6/connectors/sqlserver.html#sqlserver-required-connector-configuration-properties) |

## 可用元数据

| 元数据名      | 数据类型                  | 描述                                                     |
| :------------ | ------------------------- | -------------------------------------------------------- |
| table_name    | STRING NOT NULL           | 包含该 Row 的表名称                                      |
| schema_name   | STRING NOT NULL           | 包含该 Row 的 schema 名称                                |
| database_name | STRING NOT NULL           | 包含该 Row 的数据库名称                                  |
| op_ts         | TIMESTAMP_LTZ(3) NOT NULL | Row 在数据库中进行更改的时间。全量阶段数据，该字段值为 0 |

元数据使用示例：
```
CREATE TABLE products (
    table_name STRING METADATA  FROM 'table_name' VIRTUAL,
    schema_name STRING METADATA  FROM 'schema_name' VIRTUAL,
    db_name STRING METADATA FROM 'database_name' VIRTUAL,
    operation_ts TIMESTAMP_LTZ(3) METADATA FROM 'op_ts' VIRTUAL,
    id INT NOT NULL,
    name STRING,
    description STRING,
    weight DECIMAL(10,3)
) WITH (
    'connector' = 'sqlserver-cdc',
    'hostname' = 'localhost',
    'port' = '1433',
    'username' = 'sa',
    'password' = 'Password!',
    'database-name' = 'inventory',
    'schema-name' = 'dbo',
    'table-name' = 'products'
);
```

## 类型映射

| SQLServer 类型                   | Flink SQL 类型   |
| :------------------------------- | ---------------- |
| char(n)                          | CHAR(n)          |
| varchar(n) nvarchar(n) nchar(n)  | VARCHAR(n)       |
| text ntext xml                   | STRING           |
| decimal(p, s) money smallmoney   | DECIMAL(p, s)    |
| numeric                          | NUMERIC          |
| float real                       | DOUBLE           |
| bit                              | BOOLEAN          |
| int                              | INT              |
| tinyint                          | SMALLINT         |
| smallint                         | SMALLINT         |
| bigint                           | BIGINT           |
| date                             | DATE             |
| time(n)                          | TIME(n)          |
| datetime2 datetime smalldatetime | TIMESTAMP(n)     |
| datetimeoffset                   | TIMESTAMP_LTZ(3) |

## 注意事项
### 全量阶段不能执行 checkpoint
全量阶段由于没有可恢复的位点，SQLServer CDC 无法执行 checkpoint。为了不执行 checkpoint，SqlServer CDC 将等待直到 checkpoint 超时失败。checkpoint 超时失败默认情况下将触发 Flink 作业的 failover。因此，如果数据库表很大，建议添加以下 Flink 配置，以避免由于 checkpoint 超时而发生故障切换：
```
execution.checkpointing.interval: 10min
execution.checkpointing.tolerable-failed-checkpoints: 100
restart-strategy: fixed-delay
restart-strategy.fixed-delay.attempts: 2147483647
```

### 单线程读取
SQLServer CDC 源无法并行读取，因为只有一个任务可以接收变更事件。
