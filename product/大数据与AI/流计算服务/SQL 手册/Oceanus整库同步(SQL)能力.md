## 适用场景
在实时湖仓的数据链路建设过程中，将传统关系型数据库(如 Mysql 等)中的**整库数据**低延迟、高吞吐的同步到下游的 OLAP 数据库 (如 Drois, Clickhouse)或者归档到对应的文件系统中(如 HDFS、Hive 表)，是一个非常普遍和强烈的需求。

Oceanus 提供了非常方便的 CDAS（CREATE DATABASE AS）SQL 语法，来支持将数据库中的整库数据全量导入、增量实时同步写入到用户指定的下游系统中。

## 语法说明
```sql
CREATE DATABASE IF NOT EXISTS <target_database>
[COMMENT database_comment] 
[WITH (key1=val1, key2=val2, ...)] -- 指明写入目标库的参数
AS DATABASE <source_catalog>.<source_database> 	-- 需要同步的数据库
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
| WITH参数                           | 指明写入目标库的参数，目前会被翻译成下游 sink 表的描述参数     |
| <source_catalog>.<source_database> | 声明源 catalog 中需要同步的数据库                              |
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


## 使用方法
1. 首先注册 Mysql 的 Catalog，作为待同步的数据源表，示例如下：
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

## 使用提醒
1. 目前只支持同步 Mysql 类型数据库作为整库同步的源表。
2. 目前同步到目标端时，除 Hudi 作为目标表为，其它的目标端还不支持自动建表，需要事先在目标端中建立和 Mysql 库中数据表对应的表结构。
3. 推荐搭配 Mysql CDC Source 复用功能开启，一起使用，可以降低对 DB 的压力。
4. CDAS 语法没有限制下游输出的类型，理论上可以同步到**任意的**下游类型。
5. 当同步的表的数量非常多的时候，flink 生成的单个 task 的 name 会非常长，导致 metric 系统占用大量的内存，影响作业稳定性，Oceanus 针对这种情况引入了 `pipeline.task-name-length` 参数来限制 taskName 的长度，能极大的提高作业稳定性和日志可读性。（适用 Flink 1.13 和1.14版本）。
可以在作业的中配置生效：
```sql
set pipeline.task-name-length=80;
```

   
