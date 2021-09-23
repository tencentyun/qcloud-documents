## SHOW CREATE TABLE
分析存在的表 table\_name，查询创建信息。
#### 语法
```
SHOW CREATE TABLE [catalog_name.][db_name.]table_name
```
#### 参数
`TABLE [db_name.]table_name`
- `db_name`：数据库名称。
- `table_name`：表名称。

#### 示例
```
SHOW CREATE TABLE tbl;
```

## SHOW VIEWS
列出指定数据库中的视图，如果省略数据库名称，则列出当前数据库中的视图。

#### 语法
```
SHOW VIEWS [IN database_name] LIKE ['regular_expression']
```
#### 参数
- `[IN database_name]`：指定要从中列出视图的数据库名称。如果省略，则假定当前上下文中的数据库。
- `[LIKE 'regular_expression']`：将视图列表筛选为与指定的常规表达式匹配的视图。只能使用表示任意字符的通配符\*，或表示字符之间可供选择。

#### 示例
```
SHOW VIEWS;
```
```
SHOW VIEWS IN db01 LIKE 'view*';
```

## SHOW TBLPROPERTIES
列出命名表的表属性。
#### 语法
```
SHOW TBLPROPERTIES table_name [('property_name')]
```
#### 参数 
`[('property_name')]`：如果包含，则只列出属性 name 和 value 值。

#### 示例
```
SHOW TBLPROPERTIES tb1;
```
```
SHOW TBLPROPERTIES orders('tb1');
```

## SHOW TABLES
列出数据库中的所有基表和视图。
#### 语法
```
SHOW TABLES [IN database_name] ['regular_expression']
```
#### 参数 
- `[IN database_name]`：指定将从中列出表的数据库名称。如果省略，则假定当前上下文中的数据库。
- `['regular_expression']`：将表列表筛选为与指定的常规表达式匹配的表。只能使用表示任意字符的通配符\*，或表示字符之间。

#### 示例
```
SHOW TABLES IN sampledb;
```
```
SHOW TABLES IN sampledb '*flights*';
```

## SHOW PARTITIONS
列出表中的所有分区。
#### 语法
```
SHOW PARTITIONS [db_name.]table_name [PARTITION(partition_spec)];
```
#### 参数
- `TABLE  [db_name.]table_name`：表名。
- `[PARTITION(partition_spec)]`：分区列，可以有多个分区列条件。

#### 示例
```
SHOW PARTITIONS db01.table PARTITION(ds='2010-03-03', hr='12');
```

## SHOW CREATE VIEW
展示创建视图的语句。
#### 语法
```
SHOW CREATE VIEW view_name
```
#### 参数
`view_name`：视图名称。

#### 示例
```
SHOW CREATE VIEW orders_by_date
```

## SHOW DATABASES
列出所有在该元数据中定义的所有数据库，可使用 DATABASES 或者 SCHEMAS 做相同的查询。
#### 语法
```
SHOW {DATABASES | SCHEMAS} [IN catalog_name] [LIKE 'regular_expression']
```
#### 参数
- `[IN catalog_name]`：数据源名称。
- `[LIKE 'regular_expression']`：过滤出匹配的数据库名称。

#### 示例
```
SHOW DATABASES;
SHOW DATABASES LIKE '.*analytics';
SHOW DATABASES IN catalog1 LIKE '.*analytics';
```

## SHOW COLUMNS
展示这个模式下的表或者视图的列信息。
#### 语法
```
SHOW COLUMNS IN table_name|view_name;
```
#### 示例
```
SHOW COLUMNS IN clicks;
```

## DROP VIEW
删除一个存在的视图。
#### 语法
```
DROP VIEW [ IF EXISTS ] view_name;
```
#### 参数
- `IF EXISTS`：可选，如果存在的意思。
- `table_name`：表名。

#### 示例
```
DROP VIEW orders_by_date;
DROP VIEW IF EXISTS orders_by_date;
```

## DROP TABLE
移除表定义为`table_name`的元数据表。
#### 语法
```
DROP TABLE [IF EXISTS] table_name；
```
#### 参数
- `IF EXISTS`：可选，如果存在的意思。
- `table_name`：表名。

#### 示例
```
DROP TABLE tbl
DROP TABLE IF EXISTS tbl
```

## MSCK REPAIR TABLE
使用 MSCK REPAIR TABLE 命令更新元数据的分区信息，修复表的分区信息，适用于分区表。
#### 语法
```
MSCK [REPAIR] TABLE table_name;
```
#### 参数
- `REPAIR`：可选。
- `table_name`：表名。

#### 示例
```
MSCK REPAIR TABLE table_name;
```

## DROP DATABASE
删除命名数据库。如果数据库包含表，则必须在运行 drop database 之前删除这些表，或者使用 CASCADE 子句进行级联删除。
#### 语法
```
DROP {DATABASE | SCHEMA} [IF EXISTS] database_name [RESTRICT | CASCADE]
```
#### 参数
- `[IF EXISTS]`：如果名为 database_name 的库不存在删除就会报错。
- `[RESTRICT|CASCADE]`
 - RESTRICT：如果数据库包含表，则不会删除该数据库，如果不写默写是该模式。
 - CASCADE：会强制删除所有数据库表。

#### 示例
```
DROP DATABASE clickstreams;
DROP SCHEMA clickstreams;
DROP DATABASE `DB1` RESTRICT;
DROP DATABASE IF EXISTS `DB1` RESTRICT;
```

## CREATE DATABASE
创建一个数据库，也可以通过指定和改变表或者分区表的存储位置。
#### 语法
```
CREATE (DATABASE|SCHEMA) [IF NOT EXISTS] database_name
  [COMMENT 'database_comment']
  [LOCATION 'cosn_location']
  [WITH DBPROPERTIES ('property_name' = 'property_value') [, ...]]
```
#### 参数
- `[IF NOT EXISTS]`：如果存在执行将不报错。
- `[COMMENT database_comment]`：数据库名称注释。
- `[LOCATION S3_loc]`：指定数据库的存储位置。例如指定腾讯云 COS：cosn://bucket_id。
- `[WITH DBPROPERTIES ('property_name' = 'property_value') [, ...] ]`：允许针对数据库的属性元数据信息进行指定。

#### 示例
```
CREATE DATABASE db 
COMMENT 'db1_name' 
LOCATION 'cosn://path/to/db1' 
WITH DBPROPERTIES('k1' = 'v1','k2' = 'v2');
```

## CREATE TABLE
创建一个表同时带一些属性。
#### 语法
```
CREATE [ EXTERNAL ] TABLE [ IF NOT EXISTS ] table_identifier
    [ ( col_name1[:] col_type1 [ COMMENT col_comment1 ], ... ) ]
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name2[:] col_type2 [ COMMENT col_comment2 ], ... ) 
        | ( col_name1, col_name2, ... ) ]
    [ CLUSTERED BY ( col_name1, col_name2, ...) 
        [ SORTED BY ( col_name1 [ ASC | DESC ], col_name2 [ ASC | DESC ], ... ) ] 
        INTO num_buckets BUCKETS ]
    [ ROW FORMAT row_format ]
    [ STORED AS file_format ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( key1=val1, key2=val2, ... ) ]
```
#### 参数
- `[IF NOT EXISTS]`：如果存在执行将不报错。
- `[COMMENT database_comment]`：数据表指定注释。
- `[LOCATION 'cosn://bucket_name/[folder]/']`：指定数据表的存储位置。例如指定腾讯云 COS：cosn://bucket_id。
- `[WITH DBPROPERTIES ('property_name' = 'property_value') [, ...] ]`：允许针对数据表的属性元数据信息进行指定。

#### 限制
- OpenCSVSerde 限制
如果使用该 OpenCSVSerde 作为 row format 时，创建表的时候如果指定了该格式的时候，那么创建列的所有类型是 String 类型，这里可能会和实际创建表产生歧义，尽量如果都是 String 类型的时候使用，如果有特殊类型的时候不推荐使用。
- JSONSerde 限制
使用 JSONSerde 创建表时，不支持增加、修改、删除列。如果要使用 JSONSerde 创建表，需元数据不会发生改变或者创建时，可以预留出字段。

#### 示例
创建表：
```
CREATE DATABASE db 
COMMENT 'db1_name' 
LOCATION 'cosn://path/to/db1' 
WITH DBPROPERTIES('k1' = 'v1','k2' = 'v2');
```qw
复杂创建方式： 
```
CREATE TABLE t1 (
       ID  INTEGER
       NAME  STRING,
       HOBBY  ARRAY< STRING >,
       ADD  MAP< STRING, STRING >
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '-'
MAP KEYS TERMINATED BY ':'
COMMENT 'db1_name' 
LOCATION 'cosn://path/to/db1' 
WITH DBPROPERTIES('k1' = 'v1','k2' = 'v2');
```

#### 限制
`org.apache.hadoop.hive.serde2.OpenCSVSerde`使用 OpenCSVSerde 创建表时，如果有创建的表类型不是 string，当执行`show create table`的时候显示的列类型都是 string，如下图所示：
```
CREATE EXTERNAL TABLE `test`(
  `id` string COMMENT 'from deserializer', 
  `name` int COMMENT 'from deserializer'
  ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
WITH SERDEPROPERTIES ( 
  'quoteChar'='"', 
  'separatorChar'=',') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'cosn://dlc-122/data'
TBLPROPERTIES (
  'skip.header.line.count'='1', 
  'transient_lastDdlTime'='1623651887980');
)
```

![image-20210803151712077](/Users/majun/Library/Application Support/typora-user-images/image-20210803151712077.png)

如上图所示，此时的 name 是 int 类型，展示返回的为 string，这里可能会有歧义，尽量不要使用该 Serde 进行创建表。除了此限制，可能它的数据性能不是很适合超大数据量计算，建议可以考虑其它的存储格式。

## CREATE TABLE AS
创建一个表通过一个 `select` 查询。
#### 语法
- Spark 引擎：
```
CREATE EXTERNAL TABLE [ IF NOT EXISTS ] table_identifier
    [ ( col_name1[:] col_type1 [ COMMENT col_comment1 ], ... ) ]
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name2[:] col_type2 [ COMMENT col_comment2 ], ... ) 
        | ( col_name1, col_name2, ... ) ]
    [ CLUSTERED BY ( col_name1, col_name2, ...) 
        [ SORTED BY ( col_name1 [ ASC | DESC ], col_name2 [ ASC | DESC ], ... ) ] 
        INTO num_buckets BUCKETS ]
    [ ROW FORMAT row_format ]
    [ STORED AS file_format ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( key1=val1, key2=val2, ... ) ]
    [ AS select_statement ]
```
- Presto 引擎：
```
CREATE TABLE [ IF NOT EXISTS ] table_name [ ( column_alias, ... ) ]
    [ COMMENT table_comment ]
    [ WITH ( property_name = expression [, ...] ) ]
    AS query
    [ WITH [ NO ] DATA ]
```

#### 参数
- Spark 引擎：
 - `[IF NOT EXISTS]`：如果不存在创建表，存在则不创建。
 - `table_identifier`：表名。
 - `( column_alias, ... )`：猎德。
 - `[ COMMENT table_comment ]`：表名加注释。
 - `[ CLUSTERED BY ( col_name1, col_name2, ...) [ SORTED BY ( col_name1 [ ASC | DESC ], col_name2 [ ASC | DESC ], ... ) ] INTO num_buckets BUCKETS ]`：根据用其中几个列创建桶，并通过制指定字段进行排序。
 - `[ ROW FORMAT row_format ]`：指定 Row 的格式化参数。
 - `[ STORED AS file_format ]`：指定存储使用的文件格式，例如 OrcFile、Parquent。
 - `query SELECT`：查询语句。
- Presto 引擎：
`[ WITH ( property_name = expression [, ...] ) ]`：with 选项用于给新创建的表添加一些属性配置。

#### 限制
- OpenCSVSerde 限制
如果创建表指定 row format 为 OpenCSVSerde 的场景，那么创建列的所有元数据类型是`string`类型，这里可能会和实际创建表产生歧义，尽量都是 string 类型的情况下使用，有特殊类型（`map`、`struct`等）的时候不推荐使用。
- JSONSerde 限制
如果创建表指定 row format 为 JSONSerde 的场景，如果要增加、修改、删除列时是不支持的。尽量如果要使用 JSONSerde 在创建表的时候，尽量保证元数据不会发生改变或者创建时可以预留出字段。

#### 示例
- Spark 创建表并指定表的存储位置：
```
create external table table1 
comment 'db1_name' 
location 'cosn://path/to/tb1' 
as select * from table1;
```
- Presto 创建表并指定表的存储位置：
```sql
create table table1
comment 'test table'
with (
format='Parquet',
external_location='cosn://path/to/tb1')
as
select *
from orders
gourp by orderdate
```

## CREATE VIEW AS
从指定的 SELECT 查询创建新视图。视图是一个逻辑表，将来的查询可以引用它。视图不包含任何数据，也不写入数据。相反，每次您通过另一个查询引用视图时，视图指定的查询都会运行。
#### 语法
```
CREATE VIEW [IF NOT EXISTS] view_name
    [(column_name [COMMENT 'column_comment'][, ...])]
    [COMMENT 'view_comment']
  AS select_statement
```
#### 参数
`[IF NOT EXISTS]`：不存在则创建。
`view_name`：视图名。
`[(column_name [COMMENT 'column_comment'][, ...])]`：列的名字，同时后面可以带上列的注释。
`[COMMENT 'view_comment']`：视图的注释。
`select_statement`：查询语句。

#### 示例
```
create or replace view db1.v1 as select x,y from tbl;
create view test_view (id comment 'test c1', name_length comment 'test name c2') as  select id, length(name) from test;
```

## ALTER DATABASE SET DBPROPERTIES
增加一个或更多属性给数据库。
#### 语法
```
ALTER DATABASE database_name
  SET DBPROPERTIES ('property_name'='property_value' [, ...]);
```
#### 参数
```
SET DBPROPERTIES ('property_name'='property_value' [, ...])
```
为数据库增加一个属性或者修改某个属性，如果属性相同会覆盖。

#### 示例
```
ALTER DATABASE db1 SET DBPROPERTIES ('key' = 'value')
```

## ALTER DATABASE SET LOCATION
修改某个数据库的存储位置。
#### 语法
```
ALTER DATABASE database_name SET LOCATION cos_path;
```
#### 参数
- `[database_name]`：数据库名字。
- `[cos_path]`：Tencent COS 对象存储路径。

#### 示例
```
ALTER DATABASE db01 SET LOCATION 'cosn:///new/path'
```

## ALTER TABLE SET TBLPROPERTIES
向表中添加自定义或预定义的元数据属性，并给它们的赋值。
#### 语法
```
ALTER TABLE table_name SET TBLPROPERTIES ('property_name' = 'property_value' [ , ... ])
```
#### 参数
- `[table_name]`：表名。
- `[SET TBLPROPERTIES ('property_name' = 'property_value' [ , ... ])]`：指定表的元数据列的属性。

#### 示例
```
ALTER TABLE orders 
SET TBLPROPERTIES ('notes'="Please don't drop this table.");
```

## ALTER TABLE SET LOCATION
改变表或者分区表的存储位置。
#### 语法
```
ALTER TABLE table_name [ PARTITION (partition_spec) ] SET LOCATION 'new location';
```
#### 参数
- `PARTITION (partition_spec)`：指定分区列。
 - `partition_col_name` 分区列名。
 - `partition_col_value` 分区列的值。
- `SET LOCATION 'new location'`：创建在一个新位置在 tencent cos 上。

## ALTER TABLE ADD COLUMNS
向现有表中添加一列或多列。使用可选分区语法时，更新分区元数据。
#### 语法
```
ALTER TABLE table_name 
 [PARTITION 
   (partition_col1_name = partition_col1_value
   [,partition_col2_name = partition_col2_value][,...])]
  ADD COLUMNS (col_name data_type) [RESTRICT | CASCADE];
```
#### 参数
- table_name：表名。
- PARTITION：指定分区，分区列和值相对应。
- `ADD COLUMNS (col_name data_type [,col_name data_type,…])`：增加列给某个表，可以是一个列或者多个列。
 - col_name：列名。
 - data_type：数据类型。

#### 示例
表：
```
ALTER TABLE events ADD COLUMNS (eventowner string);
ALTER TABLE events ADD COLUMNS (eventowner string) CASCADE;
```
分区表：
```
ALTER TABLE events PARTITION (year='2021') ADD COLUMNS (event string);
```

#### 限制
如果创建表的时候采用了 `ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'`这种格式存储的表时，在创建表之后就不可以进行增加列情况，如果使用`JsonSerDe`方式创建表的时候请注意尽量确认表的结构，如果必须要增加列可以考虑删除表然后重建。

## ALTER TABLE REPLACE COLUMNS
移除这个表中所有存在的列并用一个这个集合的列去替换原表中的列，可使用 REPLACE 语法来删除列并保留一些列。
#### 语法
```
ALTER TABLE table_name 
 [PARTITION 
   (partition_col1_name = partition_col1_value
   [,partition_col2_name = partition_col2_value][,...])]
 REPLACE COLUMNS (col_spec[, col_spec ...])
```
#### 参数
- table_name：表名。
- PARTITION：指定分区，分区列和值相对应。
- `(col_spec[, col_spec ...])`：用指定的列名和数据类型替换现有列。

#### 示例
表：
```
ALTER TABLE orders REPLACE COLUMNS 
(
    eid INT, 
    empid Int,
    ename STRING 
    name String
);
```
分区表：
```
ALTER TABLE orders PARTITION (year='2021') REPLACE COLUMNS 
(
    eid INT, 
    empid Int,
    ename STRING 
    name String
);
```

## ALTER TABLE ADD PARTITION
为某个表创建一个或多个分区列。
#### 语法
```
ALTER TABLE table_name ADD [IF NOT EXISTS]
  PARTITION
  (partition_col1_name = partition_col1_value
  [,partition_col2_name = partition_col2_value]
  [,...]);
```
#### 参数
- IF NOT EXISTS：如果存在就不报错。
- `PARTITION (partition_col_name = partition_col_value [,...])`：指定分区列。

#### 示例
```
ALTER TABLE tbl ADD PARTITION (p1=1, p2='a');
ALTER TABLE tbl ADD IF NOT EXISTS PARTITION ('P' = 1) PARTITION ('P' = 2);
```

## ALTER TABLE DROP PARTITION
从表中删除一个或者多个分区。
#### 语法
```
ALTER TABLE table_name DROP [IF EXISTS] PARTITION (partition_spec) [, PARTITION (partition_spec)];
```
#### 参数
- IF EXISTS：如果指定的分区不存在，则取消显示错误消息。
- `PARTITION (partition_spec)`：指定分区。

#### 示例
```
ALTER TABLE tbl DROP IF EXISTS PARTITION (P = 1);
```
```
alter table tbl drop 
    partition (p1='a',p2=1), partition(p1='b',p2=2), 
    partition(p1='c',p2=3);
```

## DESCRIBE TABLE
返回表的列信息以及元数据信息。
#### 语法
```
DESCRIBE [EXTENDED | FORMATTED] [db_name.]table_name [PARTITION partition_spec];
```
#### 参数
- `[EXTENDED | FORMATTED]`：指定表的格式化形式。
- `[PARTITION partition_spec]`：该表的分区列表。

#### 示例
```
DESCRIBE tbl;
DESCRIBE FORMATTED tbl PARTITION (date_id = '2019-01-07');
```

#### 限制
- 这个语句目前只返回表的列名。
- partition_spec 暂时不支持对表的分区查询。

## DESCRIBE VIEW
展示视图的所有列信息。
#### 语法
```
DESCRIBE [view_name];
```
#### 参数
view_name：视图名。

#### 示例
```
DESCRIBE view1;
```

## CREATE FUNCTION
该语句允许创建一个由类名实现的函数。
#### 语法
```
CREATE FUNCTION [db_name.]function_name AS class_name
  [USING JAR|FILE 'file_uri' [, JAR|FILE 'file_uri'] ]
```
#### 参数
- `[db_name.]function_name`：函数名，创建函数的时候后指定命名空间在`db_name 下`。
- class_name：类名。
- `[USING JAR|FILE 'file_uri' [, JAR|FILE 'file_uri'] ]`：使用 jar 包或者 File 创建函数，这里要指明远程文件系统 Tencent  COS 的路径。

#### 示例
```
CREATE FUNCTION udf_add2 AS 'udf_add2'
USING JAR 'cosn://xxxxx/udf/hive-test-udfs.jar.
```

## DROP FUNCTION
删除指定的函数。
#### 语法
```
DROP FUNCTION [ IF EXISTS ] function_name
```
#### 参数
- IF EXISTS：存在就删除。
- function_name：函数名。

#### 示例
```
DROP FUNCTION udf_add2;
```

## CALL Statement 
这里只有在使用 Spark 中使用 [Iceberg SQL 扩展](https://iceberg.apache.org/spark-configuration/#sql-extensions) 时，存储过程才可用。
#### 语法
```
CALL expression
```
#### 参数
`expression`：函数表达式。

#### 示例
```
CALL catalog_name.`system`.procedure_name(arg_name_2 => arg_2, arg_name_1 => arg_1)

#当按位置传递参数时，如果它们是可选的，则只能省略结束参数。
CALL catalog_name.system.procedure_name(arg_1, arg_2, ... arg_n)

#将当前快照设置为db.sample1：
CALL catalog_name.system.set_current_snapshot('db.sample', 1)
```

#### 更多使用
[Spark Procedures](https://iceberg.apache.org/spark-procedures/)。

## DESCRIBE SCHEMA|DATABASE [EXTENDED] DB_NAME
返回表的列信息以及元数据信息。
#### 语法
```
DESCRIBE SCHEMA|DATABASE [EXTENDED] DB_NAME;
```
#### 参数
- SCHEMA|DATABASE：指定库为 SCHEMA 或者 DATABASE。
- EXTENDED：该库是否为 EXTENDED。

#### 示例
```
DESCRIBE DATABASE db_name;
DESCRIBE DATABASE EXTENDED db_name;
```
