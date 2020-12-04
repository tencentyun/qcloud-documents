物化视图主要用于预先计算并保存表连接或聚合等耗时较多的操作结果；在执行查询任务时，可以避免进行一些耗时操作，从而快速的得到结果。这种物化视图使用查询重写（query rewrite）机制，不需要修改原有的查询语句，会选择合适的物化视图进行查询，完全对应用透明。
物化视图使用限制：
- 不支持子查询创建物化视图
- 不支持 union 语句创建物化视图

在本文档中，我们提供有关 SparkSql 中物化视图创建和管理的详细信息，并通过一些示例描述重写算法的当前覆盖范围和使用限制。
## 物化视图的创建


```
CREATE MATERIALIZED VIEW [IF NOT EXISTS] [db_name.]materialized_view_name
[DISABLE REWRITE]
[COMMENT materialized_view_comment]
[PARTITIONED ON (col_name, ...)]
[CLUSTERED ON (col_name, ...) | DISTRIBUTED ON (col_name, ...) SORTED ON (col_name, ...)]
[
[ROW FORMAT row_format]
[STORED AS file_format]
| STORED BY 'storage.handler.class.name' [WITH SERDEPROPERTIES (...)]
]
[LOCATION hdfs_path]
[TBLPROPERTIES (property_name=property_value, ...)]
AS
<query>;
```
>?
>- 这里建议不使用 DISABLE REWRITE 选项，否则将不能使用物化视图功能。同时，把 $db_name 设置为 mv_db，如果不设置为 mv_db，需修改参数 `spark.sql.materializedView.databases为$db_name`。
>- 建议用户建立独立的 mv_db，只用来存放 mv，可以提升 mv 匹配时获取元数据的效率。

## 物化视图示例
1. 准备基础数据
```
CREATE DATABASE  mv_database location "/mv";
use mv_database;
create external table if not exists mv_database.table1 (id int,name string) ;
create external table if not exists mv_database.table2 (id int, tags string);
insert into  table1  values (1,'1111'),(2,'2222') ;
insert into table1 values (123,'123123'),(678,'678678');
insert into table2 values (1,'iam1'),(2,'iam2'),(123,'iam123'),(678,'iam678');
```
2. 构建物化视图
```
$spark-sql --database mv_database --master yarn
spark-sql> set spark.sql.materializedView.enable=true;
spark-sql>set spark.sql.materializedView.databases=mv_db;
spark-sql> create materialized view mv_db.mv_test_join
as
select t1.id,t1.name,t2.tags
from mv_database.table1 t1 join
mv_database.table2 t2
where
t1.id=t2.id;
```
3. 测试物化视图
```
spark-sql> explain extended select t1.id,t1.name,t2.tags
         > from mv_database.table1 t1 join
         > mv_database.table2 t2
         > where
         > t1.id=t2.id;
== Parsed Logical Plan ==
'Project ['t1.id, 't1.name, 't2.tags]
+- 'Filter ('t1.id = 't2.id)
   +- 'Join Inner
      :- 'SubqueryAlias t1
      :  +- 'UnresolvedRelation [mv_database, table1]
      +- 'SubqueryAlias t2
         +- 'UnresolvedRelation [mv_database, table2]
== Analyzed Logical Plan ==
id: int, name: string, tags: string
Project [id#26, name#27, tags#29]
+- Filter (id#26 = id#28)
   +- Join Inner
      :- SubqueryAlias t1
      :  +- SubqueryAlias spark_catalog.mv_database.table1
      :     +- HiveTableRelation `mv_database`.`table1`, org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe, [id#26, name#27]
      +- SubqueryAlias t2
         +- SubqueryAlias spark_catalog.mv_database.table2
            +- HiveTableRelation `mv_database`.`table2`, org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe, [id#28, tags#29]
== Materialized Logical Plan ==
Project [id#40 AS id#26, name#41 AS name#27, tags#42 AS tags#29]
+- SubqueryAlias spark_catalog.mv_db.mv_test_join
   +- HiveTableRelation `mv_db`.`mv_test_join`, org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe, [id#40, name#41, tags#42]
== Optimized Logical Plan ==
HiveTableRelation `mv_db`.`mv_test_join`, org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe, [id#40, name#41, tags#42]
== Physical Plan ==
Scan hive mv_db.mv_test_join [id#40, name#41, tags#42], HiveTableRelation `mv_db`.`mv_test_join`, org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe, [id#40, name#41, tags#42]
```
其中，如下代码表示了命中构建的物化视图，通过重写（rewrite）了逻辑执行计划提升性能。
```
== Materialized Logical Plan ==
Project [id#40 AS id#26, name#41 AS name#27, tags#42 AS tags#29]
+- SubqueryAlias spark_catalog.mv_db.mv_test_join
   +- HiveTableRelation `mv_db`.`mv_test_join`, org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe, [id#40, name#41, tags#42]
```

## 物化视图 MATCH 策略
TianQiong-Spark 物化视图
```
set spark.sql.materializedView.matchPolicy=multiple;
set spark.sql.materializedView.multiplePolicy.limit=5;
```

## 物化视图重建
当实例化视图使用的源表中的数据发生更改时，例如，插入新数据或修改现有数据时，我们将需要刷新实例化视图的内容，以使其与这些更改保持最新。当前，物化视图的重建操作需要由用户触发。用户应执行以下语句：
```
ALTER MATERIALIZED VIEW [db_name.]materialized_view_name REBUILD;
```

## 物化视图重写方式
创建实例化视图后，优化器将能够利用其定义语义来使用实例化视图自动重写传入的查询，从而加快查询的执行速度。

用户可以有选择地启用/禁用实例化视图以进行重写。默认情况下，实例化视图已启用，可在创建时进行重写。若无需启用实例化视图，可使用如下语句关闭此功能：
```
ALTER MATERIALIZED VIEW [db_name.]materialized_view_name enable|disable REWRITE;
```
## 物化视图的删除及其他操作
当前我们支持的物化视图的操作有：
1. 删除物化视图
```
DROP MATERIALIZED VIEW [db_name.]materialized_view_name;
```
2. show 物化视图
```
SHOW MATERIALIZED VIEWS [IN database_name] ['identifier_with_wildcards’];
```
3. 展示指定信息的物化视图
```
DESCRIBE [EXTENDED | FORMATTED] [db_name.]materialized_view_name;
```
