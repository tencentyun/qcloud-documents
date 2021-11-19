向表中添加自定义或预定义的元数据属性，并给它们的赋值。
## 语法
```
ALTER TABLE table_name SET TBLPROPERTIES ('property_name' = 'property_value' [ , ... ])
```
## 参数
- `[table_name]`：表名。
- `[SET TBLPROPERTIES ('property_name' = 'property_value' [ , ... ])]`：指定表的元数据列的属性。

## 示例
```
ALTER TABLE orders 
SET TBLPROPERTIES ('notes'="Please don't drop this table.");
```
