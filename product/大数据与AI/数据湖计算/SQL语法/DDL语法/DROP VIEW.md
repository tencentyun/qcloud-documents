删除一个存在的视图。
## 语法
```
DROP VIEW [ IF EXISTS ] view_name;
```
## 参数
- `IF EXISTS`：可选，如果存在的意思。
- `table_name`：表名。

## 示例
```
DROP VIEW orders_by_date;
DROP VIEW IF EXISTS orders_by_date;
```
