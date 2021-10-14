增加一个或更多属性给数据库。
## 语法
```
ALTER DATABASE database_name
  SET DBPROPERTIES ('property_name'='property_value' [, ...]);
```
## 参数
```
SET DBPROPERTIES ('property_name'='property_value' [, ...])
```
为数据库增加一个属性或者修改某个属性，如果属性相同会覆盖。

## 示例
```
ALTER DATABASE db1 SET DBPROPERTIES ('key' = 'value')
```
