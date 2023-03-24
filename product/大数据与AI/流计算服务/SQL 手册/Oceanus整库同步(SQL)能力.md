## 适用场景
在实时湖仓的数据链路建设过程中，将传统关系型数据库（如 Mysql 等）中的**整库数据**低延迟、高吞吐的同步到下游的 OLAP 数据库（如 Doris, ClickHouse）或者归档到对应的文件系统中（如 HDFS、Hive 表），是一个非常普遍和强烈的需求。

Oceanus 提供了非常方便的 CDAS（CREATE DATABASE AS）SQL 语法，来支持将数据库中的整库数据全量导入、增量实时同步写入到用户指定的下游系统中。

## 语法说明
```sql
CREATE DATABASE IF NOT EXISTS <target_database>
[COMMENT database_comment] 
[WITH (key1=val1, key2=val2, ...)] -- 指明写入目标库的参数
AS DATABASE <source_catalog>.<source_database> 	-- source_database 是被同步的源数据库
INCLUDING { ALL TABLES | TABLE 'table_name' }
-- INCLUDING ALL TABLES 表示同步数据库中的所有表
-- INCLUDING TABLE 'table' 表示同步数据库中特定的表，支持正则表达式，如 'order_.*';
-- 同步多张表时，可以写成 INCLUDING TABLE 'tableA|tableB|tableC'的格式
[EXCLUDING TABLE 'table_name']
-- EXCLUDING TABLE 'table' 表示不同步数据库中特定的表，支持正则表达式，如 'order_.*';
-- 排除多张表时，可以写成 EXCLUDING TABLE 'tableA|tableB|tableC'的格式
[/*+ OPTIONS(key1=val1, key2=val2, ... ) */] 
-- （可选，指明读取source的参数，如指定source serverId的范围，解析debezium时间戳字段类型等）
```

参数说明：

| 参数                               | 解释                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| target_database                    | 待写入的目标数据库名                                         |
| database_comment                   | 待写入的数据库注释                                           |
| WITH参数                           | 指明写入目标库的参数，目前会被翻译成下游 sink 表的描述参数   |
| `<source_catalog>.<source_database>` | 声明源 catalog 中需要同步的数据库                            |
| INCLUDING  ALL TABLES              | 同步源库中的所有表                                           |
| INCLUDING TABLE                    | 示同步数据库中特定的表，支持正则表达式，如 'order_.*' ； 同步多张表时，可以写成 INCLUDING TABLE 'tableA\|tableB'格式 |
| EXCLUDING TABLE                    | 表示不同步数据库中特定的表，支持正则表达式，如 'order_.*'; 排除多张表时，可以写成 EXCLUDING TABLE 'tableA\|tableB'格式 |
| OPTIONS                            | 可选，指明读取Source时覆盖的参数，如指定 source serverId 的范围等 |

>! 第三行 [WITH (key1=val1, key2=val2, ...)] 指明写入目标库的参数中， value 值支持将 Source 表的表名进行变量替换，使用方法是使用占位符 $tableName。如下整库同步到 Doris 的示例中，写入每一个 sink 的表中 $tableName 会替换为相对应 Mysql 库中源表表名。
>
```sql
create catalog my_mysql with(...);
create database if not exists sink_db
with (
  'connector' = 'doris',
  'table.identifier' = 'db1.$tableName_doris'
  ...
) 
including all tables
/*+ `OPTIONS`('server-time-zone' = 'Asia/Shanghai') */; -- 声明解析timestamp字段的时区类型
```


### MySQL-CDC 元数据字段读取

* MySQL CDC connector除支持提取物理表的字段外，还支持了[元数据字段列表](https://cloud.tencent.com/document/product/849/52698#.E5.8F.AF.E7.94.A8.E5.85.83.E6.95.B0.E6.8D.AE.EF.BC.88flink1.13-.E5.8F.8A.E4.BB.A5.E4.B8.8A.E7.89.88.E6.9C.AC.E5.8F.AF.E4.BD.BF.E7.94.A8.EF.BC.89)可以提取。整库同步功能中也提供了一个 options 配置参数，可以用来控制同步所需的元数据字段。

| 参数                                   | 解释                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| oceanus.source.include-metadata.fields | 需要同步的 source 表的元字段，格式为 'table_name:table_name;meta.batch_id:batch_id', 元数据字段定义通过分号;分隔，每个元数据字段格式为 metadataColumn:alias， 第一部分为实际对应的元数据 column，第二部分为重命名后的值。 |

* 注意: 元数据字段会按照声明的顺序，追加到源表之后

使用实例:
```sql
SET table.optimizer.mysql-cdc-source.merge.enabled=true;

create catalog my_mysql with (
    'type' = 'jdbc',
    'default-database' = 'test',
    'username' = 'xx',
    'password' = 'xxx',
    'base-url' = 'xxx'
);

create database if not exists print_sink_db
comment 'test_sink'
with (
'connector' = 'print',
'print-identifier' = '$tableName')
as database `my_mysql`.`test`
including all tables
/*+ `OPTIONS`('server-time-zone' = 'Asia/Shanghai',
    'oceanus.source.include-metadata.fields'='table_name:table_name;database_name:database_name;op_ts:op_ts;meta.table_name:meta_table_name;meta.database_name:meta_database_name;meta.op_ts:meta_op_ts;meta.op_type:meta_op_type;meta.batch_id:meta_batch_id;meta.is_ddl:meta_id_ddl;meta.mysql_type:meta_mysql_type;meta.update_before:meta_update_before;meta.pk_names:meta_pk_names;meta.sql:meta_sql;meta.sql_type:meta_sql_type;meta.ts:meta_ts')
    */;
```




## 使用方法
1. 首先注册 MySQL 的 Catalog，作为待同步的数据源表，示例如下：
```sql
create catalog my_mysql with (
    'type' = 'jdbc',
    'default-database' = 'test',
    'username' = 'XXX',
    'password' = 'XXX',
    'base-url' = 'jdbc:mysql://ip:port'
);
```
2. 对于不支持的自动建表的下游系统，需要事先保证在下游系统中建立和上游 Mysql 表中一一对应的源表。
3. 使用整库同步语法指定需要同步的同步表，其中写入目标库的参数现在只支持填入下游 connector 的必要参数。

### 同步到 Hudi 示例
```sql
SET table.optimizer.mysql-cdc-source.merge.enabled=true;

create catalog my_mysql with (
    'type' = 'jdbc',
    'default-database' = 'test',
    'username' = 'root',
    'password' = 'XXX',
    'base-url' = 'jdbc:mysql://ip:port'
);

create database if not exists sink_db
comment 'test_sink'
with (
'connector' = 'hudi',
'path' = 'hdfs://namenode:8020/user/hive/warehouse/$tableName_mor'
) as database `my_mysql`.`trade_log`
including all tables
/*+ `OPTIONS`('server-time-zone' = 'Asia/Shanghai') */; -- 声明解析timestamp字段的时区类型
```

### 同步到 Doris 示例
```sql
SET table.optimizer.mysql-cdc-source.merge.enabled=true;

create catalog my_mysql with (
    'type' = 'jdbc',
    'default-database' = 'test',
    'username' = 'root',
    'password' = 'XXX',
    'base-url' = 'jdbc:mysql://ip:port'
);



create database if not exists sink_db
comment 'test_sink'  with (
'connector' = 'doris',
'table.identifier' = 'trade_log.$tableName',
'username' = 'admin',
'password' = 'xxx',
'sink.batch.size' = '500',
'sink.batch.interval' = '1s',
'fenodes' = 'ip:port'
) as database `my_mysql`.`trade_log`
including all tables
/*+ `OPTIONS`('server-time-zone' = 'Asia/Shanghai') */; -- 声明解析timestamp字段的时区类型
```



### 同步到 Hive 示例
```sql
SET table.optimizer.mysql-cdc-source.merge.enabled=true;

create catalog my_mysql with (
    'type' = 'jdbc',
    'default-database' = 'test',
    'username' = 'root',
    'password' = 'XXX',
    'base-url' = 'jdbc:mysql://ip:port'
);

create database if not exists sink_db
comment 'test_sink'  with (
'connector' = 'hive',
'hive-version' = '2.3.6',
'hive-database' = 'test_100',
'hive-table' = '$tableName',
'sink.partition-commit.policy.kind' = 'metastore'
) as database `my_mysql`.`trade_log`
including all tables
/*+ `OPTIONS`('append-mode' = 'true', 'server-time-zone' = 'Asia/Shanghai') */;  
-- 因为hive sink不支持变更数据，此处的hint会把原始cdc的变更数据转成成append流下发
```
作业运行拓扑图展开后如下：
![](https://qcloudimg.tencent-cloud.cn/raw/bf442eaef6fb0702161fdcdafab8ed78.png)

#### 同步到 Hive 自动建表示例:

* 作业需要提前配置连接 Hive 服务的 jar 包，详细配置可以参考 [获取 Hive 连接配置 jar 包](https://cloud.tencent.com/document/product/849/55238#hive-.E9.85.8D.E7.BD.AE)
* 因为 MySQL 中 timestamp 和 datetime 字段和 Hive 中相应类型精度不匹配，暂时不支持同步带有这两种字段的 Hive 表

```sql
SET table.optimizer.mysql-cdc-source.merge.enabled=true;

//注册mysql的catalog
create catalog my_mysql with (
    'type' = 'jdbc',
    'default-database' = 'test',
    'username' = 'root',
    'password' = 'XXX',
    'base-url' = 'jdbc:mysql://ip:port'
);

//注册hive端catalog
create catalog my_hive with (
    'type' = 'hive',
    'default-database' = 'default',
    'hive-version' = '2.3.5'
);

create database if not exists `my_hive`.`trade_log`
as database `my_mysql`.`trade_log`
including all tables
/*+ `OPTIONS`('append-mode' = 'true', 'server-time-zone' = 'Asia/Shanghai') */;  
-- 因为hive sink不支持变更数据，此处的hint会把原始cdc的变更数据转成成append流下发
```


## 使用提醒
1. 目前只支持同步 MySQL 类型数据库作为整库同步的源表。
2. 目前同步到目标端时，除 Iceberg、Elasticsearch、Hudi 和 Hive（需要提前注册 Hive Catalog）作为目标表外，其它的目标端还不支持自动建表，，需要事先在目标端中建立和 Mysql 库中数据表对应的表结构。
3. 推荐搭配 MySQL CDC Source 复用功能开启，一起使用，可以降低对数据库的压力。
4. CDAS 语法没有限制下游输出的类型，理论上可以同步到**任意的**下游类型。
5. 当同步的表的数量非常多的时候，flink 生成的单个 task 的 name 会非常长，导致 metric 系统占用大量的内存，影响作业稳定性，Oceanus 针对这种情况引入了 `pipeline.task-name-length` 参数来限制 taskName 的长度，能极大的提高作业稳定性和日志可读性。（适用 Flink-1.13 和 Flink-1.14 版本）。
可以在作业的中配置生效：
```sql
set pipeline.task-name-length=80;
```
