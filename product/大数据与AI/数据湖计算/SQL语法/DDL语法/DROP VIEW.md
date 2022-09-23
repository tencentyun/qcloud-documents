## 说明
- 支持内核：Presto、SparkSQL。
- 用途：删除视图。

## 语法
```
DROP VIEW [ IF EXISTS ] view_name;
```
## 参数
- `IF EXISTS`：可选，如果存在的意思。
- `view_name`：视图名称。


## 示例
```
DROP VIEW orders_by_date;
DROP VIEW IF EXISTS orders_by_date;
```
