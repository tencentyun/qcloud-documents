## 说明
- 支持内核：Presto、SparkSQL。
- 用途：为数据库添加一个或多个属性，如果属性相同则会进行覆盖。

## 标准语法
```
ALTER (DATABASE|SCHEMA) database_name SET DBPROPERTIES (property_name=property_value, ...)
```
## 参数
`database_name`：数据库名称。

## 示例
```
-- Alters the database to set properties `author`.
ALTER DATABASE product SET DBPROPERTIES ('author' = 'allen');
```
