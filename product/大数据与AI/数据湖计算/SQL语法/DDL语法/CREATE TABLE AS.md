创建一个表通过一个 `select` 查询。
## 语法
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

## 参数
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

## 限制
- OpenCSVSerde 限制
如果创建表指定 row format 为 OpenCSVSerde 的场景，那么创建列的所有元数据类型是`string`类型，这里可能会和实际创建表产生歧义，尽量都是 string 类型的情况下使用，有特殊类型（`map`、`struct`等）的时候不推荐使用。
- JSONSerde 限制
如果创建表指定 row format 为 JSONSerde 的场景，如果要增加、修改、删除列时是不支持的。尽量如果要使用 JSONSerde 在创建表的时候，尽量保证元数据不会发生改变或者创建时可以预留出字段。

## 示例
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
