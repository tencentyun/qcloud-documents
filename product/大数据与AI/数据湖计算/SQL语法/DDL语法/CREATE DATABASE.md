创建一个数据库，也可以通过指定和改变表或者分区表的存储位置。
## 语法
```
CREATE (DATABASE|SCHEMA) [IF NOT EXISTS] database_name
  [COMMENT 'database_comment']
  [LOCATION 'cosn_location']
  [WITH DBPROPERTIES ('property_name' = 'property_value') [, ...]]
```
## 参数
- `[IF NOT EXISTS]`：如果存在执行将不报错。
- `[COMMENT database_comment]`：数据库名称注释。
- `[LOCATION S3_loc]`：指定数据库的存储位置。例如指定腾讯云 COS：cosn://bucket_id。
- `[WITH DBPROPERTIES ('property_name' = 'property_value') [, ...] ]`：允许针对数据库的属性元数据信息进行指定。

## 示例
```
CREATE DATABASE db 
COMMENT 'db1_name' 
LOCATION 'cosn://path/to/db1' 
WITH DBPROPERTIES('k1' = 'v1','k2' = 'v2');
```
