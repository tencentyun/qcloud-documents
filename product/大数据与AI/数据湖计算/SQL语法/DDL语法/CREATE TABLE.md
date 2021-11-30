创建一个表同时带一些属性。
## 语法
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
## 参数
- `[IF NOT EXISTS]`：如果存在执行将不报错。
- `[COMMENT database_comment]`：数据表指定注释。
- `[LOCATION 'cosn://bucket_name/[folder]/']`：指定数据表的存储位置。例如指定腾讯云 COS：cosn://bucket_id。
- `[WITH DBPROPERTIES ('property_name' = 'property_value') [, ...] ]`：允许针对数据表的属性元数据信息进行指定。

#### 限制
- OpenCSVSerde 限制
如果使用该 OpenCSVSerde 作为 row format 时，创建表的时候如果指定了该格式的时候，那么创建列的所有类型是 String 类型，这里可能会和实际创建表产生歧义，尽量如果都是 String 类型的时候使用，如果有特殊类型的时候不推荐使用。
- JSONSerde 限制
使用 JSONSerde 创建表时，不支持增加、修改、删除列。如果要使用 JSONSerde 创建表，需元数据不会发生改变或者创建时，可以预留出字段。

## 示例
创建表：
```
CREATE DATABASE db 
COMMENT 'db1_name' 
LOCATION 'cosn://path/to/db1' 
WITH DBPROPERTIES('k1' = 'v1','k2' = 'v2');
```
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

