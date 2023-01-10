数据湖计算 DLC 使用的 Iceberg 语法版本为1.13.1，详情语法说明可参考 [Iceberg 官网文档](https://iceberg.apache.org/docs/latest/)。

当您在使用 Iceberg 外部表时，SQL 语法与 Iceberg 原生表存在以下差异。
## CREATE TABLE
### 原生表
**语法**
```
CREATE TABLE [ IF NOT EXISTS ] table_identifier
    ( col_name[:] col_type [ COMMENT col_comment ], ... )
[ COMMENT table_comment ]
[ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
```
**示例**
```
CREATE TABLE dempts(
    id bigint COMMENT 'id number',
    num int,
    eno float,
    dno double,
    cno decimal(9,3),
    flag  boolean,
    data string,
    ts_year timestamp,
    date_month date,
    bno binary,
    point struct<x: double, y: double>,
    points array<struct<x: double, y: double>>,
    pointmaps map<struct<x: int>, struct<a: int>> 
    )
COMMENT 'table documentation' 
PARTITIONED BY (bucket(16,id), years(ts_year), months(date_month), identity(bno),  bucket(3,num),  truncate(10,data));
```


### 外部表
**语法**
```
CREATE TABLE [ IF NOT EXISTS ] table_identifier
    ( col_name[:] col_type [ COMMENT col_comment ], ... )
USING iceberg
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( property_name=property_value, ... ) ]
```
**示例**
```
CREATE TABLE dempts(
    id bigint COMMENT 'id number',
    num int,
    eno float,
    dno double,
    cno decimal(9,3),
    flag  boolean,
    data string,
    ts_year timestamp,
    date_month date,
    bno binary,
    point struct<x: double, y: double>,
    points array<struct<x: double, y: double>>,
    pointmaps map<struct<x: int>, struct<a: int>> 
    )
USING iceberg
COMMENT 'table documentation' 
PARTITIONED BY (bucket(16,id), years(ts_year), months(date_month), identity(bno),  bucket(3,num),  truncate(10,data))
LOCATION 'cosn://rickytest-1305424723/channing-test/loc'
TBLPROPERTIES ('write.format.default'='orc');
```

## CREATE TABLE AS SELECT
### 原生表
**语法**
```
CREATE TABLE [ IF NOT EXISTS ] table_identifier
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
AS select_statement
```
**示例**
```
CREATE TABLE IF NOT EXISTS dempts_copy
COMMENT 'table create as select'
PARTITIONED BY (eno, dno)
AS SELECT * from dempts;
```


### 外部表
**语法**
```
CREATE TABLE [ IF NOT EXISTS ] table_identifier
USING iceberg
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( property_name=property_value, ... ) ]
AS select_statement
```
**示例**
```
CREATE TABLE dempts_copy
USING iceberg
COMMENT 'table create as select' 
PARTITIONED BY (eno, dno) 
LOCATION 'cosn://rickytest-1305424723/channing-test/loc'
TBLPROPERTIES ('write.format.default'='avro') 
AS SELECT * from dempts;

```

## REPLACE TABLE AS SELECT
### 原生表
**语法**
```
CREATE OR REPLACE TABLE table_identifier
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
AS select_statement
```
**示例**
```
CREATE OR REPLACE TABLE dempts_replace
COMMENT 'table create as replace' 
PARTITIONED BY (eno, bucket(10, num))  
AS SELECT * from dempts;
```


### 外部表
**语法**
```
CREATE [OR REPLACE] TABLE table_identifier
USING iceberg
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( property_name=property_value, ... ) ]
AS select_statement
```
**示例**
```
CREATE OR REPLACE TABLE dempts_replace
USING iceberg
COMMENT 'table create as replace' 
PARTITIONED BY (eno, dno) 
LOCATION 'cosn://rickytest-1305424723/channing-test/loc'
TBLPROPERTIES ('write.format.default'='avro') 
AS SELECT * from dempts;
```

## Procedure
>! 迁移原表必须为 Hive 表或 Spark 表。

### 原生表
暂不支持。

### 外部表
- **snapshot**
基于原始表创建轻量级的临时表，临时表直接复用原始表快照。
**语法**
```
CALL `Catalog`.`system`.snapshot(source_table, table, [location], [properties]);
```
**示例**
```
CALL `DataLakeCatalog`.`system`.snapshot('validation.table_01', 'validation.snap');
CALL `DataLakeCatalog`.`system`.snapshot('validation.table_01', 'validation.snap2', 'cosn://channingdata-1305424723/example3/');
```

- **call**
更新替换表属性。
**语法**
```
CALL `Catalog`.`system`.migrate(table, [properties]);
```
**示例**
```
CALL `DataLakeCatalog`.`system`.migrate('validation.table_01');
CALL `DataLakeCatalog`.`system`.migrate('validation.table_01', map('data', 'name'));

```

- **add_files**
直接从 hive 中加载数据文件，可指定数据文件到指定分区。
**语法**
```
CALL `Catalog`.`system`.add_files(table, source_table, [partition_filter]);
```
**示例**
```
CALL `DataLakeCatalog`.`system`.add_files(`table`=>'validation.table_02', `source_table`=>'validation.table_01');
CALL `DataLakeCatalog`.`system`.add_files(`table`=>'validation.table_02', `source_table`=>'validation.table_01', `partition_filter`=>map('part_col', 'A'));
```



