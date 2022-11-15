## 说明
- 支持内核：Presto、SparkSQL。
- 用途：创建一个数据库，也可以通过指定和改变表或者分区表的存储位置。

## 语法
```
CREATE {DATABASE|SCHEMA} [IF NOT EXISTS] database_name
     [COMMENT 'database_comment']
     [WITH DBPROPERTIES ('property_name' = 'property_value') [, ...]]
```
## 参数
- `DATABASE|SCHEMA`：同一个意思，都可以使用。
- `database_name`：数据库名称。
- `database_comment`：数据库注释。
- `[WITH DBPROPERTIES ('property_name' = 'property_value') [, ...]]`：以 `key-value` 的形式配置数据库参数。


## 示例
Create database `db` only if database with same name doesn't exist.
```
CREATE DATABASE IF NOT EXISTS db;
```

Create database `db` only if database with same name doesn't exist with `Comment` and `Database Properties`.
```
CREATE DATABASE db 
COMMENT 'db1_name' 
WITH DBPROPERTIES('k1' = 'v1','k2' = 'v2');
```
