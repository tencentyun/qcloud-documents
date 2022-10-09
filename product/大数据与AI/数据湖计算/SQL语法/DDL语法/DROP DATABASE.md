## 说明
- 支持内核：Presto、SparkSQL。
- 用途：删除指定的数据库。

## 语法
```
DROP {DATABASE | SCHEMA} [IF EXISTS] database_name [RESTRICT | CASCADE]
```
## 参数
- `DATABASE|SCHEMA`：同一个意思，都可以使用。
- `database_name`：数据库名称。
- `RESTRICT`：如果数据库包含表，则不会删除该数据库，不填，默写是该模式。
- `CASCADE`：强制删除所有数据库表。

## 示例
```
-- Drop the database and it's tables
DROP DATABASE test CASCADE;

-- Drop the database using IF EXISTS
DROP DATABASE IF EXISTS test;
```
