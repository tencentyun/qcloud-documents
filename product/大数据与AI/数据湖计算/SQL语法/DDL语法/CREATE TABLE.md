创建一个表同时带一些属性。
## 语法
```
CREATE TABLE [ IF NOT EXISTS ] table_identifier
    [ ( col_name1 col_type1 [ COMMENT col_comment1 ], ... ) ]
    USING data_source
    [ OPTIONS ( key1=val1, key2=val2, ... ) ]
    [ PARTITIONED BY ( col_name1, col_name2, ... ) ]
    [ CLUSTERED BY ( col_name3, col_name4, ... ) 
        [ SORTED BY ( col_name [ ASC | DESC ], ... ) ] 
        INTO num_buckets BUCKETS ]
    [ LOCATION path ]
    [ COMMENT table_comment ]
    [ TBLPROPERTIES ( key1=val1, key2=val2, ... ) ]
```
## 参数说明
- `USING data_source`：建表时，数据的输入类型，目前有：CSV, ORC, PARQUET, ICEBERG 等。
- `table_identifier`：指定表名，支持三段式，例如：catalog.database.table。      
- ` PARTITIONED BY`：基于指定的列创建分区。        
- `EXTERNAL`： 是否为外表，存在即为外表。
- `row_format`：与表存储格式，对应每行数据的输入输出格式。
- `STORED AS`：表存储的文件格式，例如：parquet、orc 等。
- `COMMENT`：表的描述信息。
- `TBLPROPERTIES`：一组 k-v 值，用于指定表的参数。

## 示例
```
CREATE TABLE `TEST` (
  `col1` string, 
  `col2` string)
using  ICEBERG
LOCATION
  'cosn://dlc-test-1305424723/allen_test1'


CREATE TABLE TEST (id INT, name STRING, age INT)


CREATE TABLE TEST (id INT, name STRING, age INT)
    USING PARQUET
    PARTITIONED BY (age)
    CLUSTERED BY (Id) INTO 4 buckets
    LOCATION
  'cosn://dlc-test-1305424723/allen_test1'
```
支持使用 CREATE TABLE AS 语法，详情可参见：[CREATE TABLE AS](https://cloud.tencent.com/document/product/1342/61794)。
