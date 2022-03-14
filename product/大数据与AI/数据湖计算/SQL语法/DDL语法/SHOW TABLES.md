列出数据库中的所有基表和视图。
## 语法
```
SHOW TABLES [IN database_name] ['regular_expression']
```
## 参数 
- `[IN database_name]`：指定将从中列出表的数据库名称。如果省略，则假定当前上下文中的数据库。
- `['regular_expression']`：将表列表筛选为与指定的常规表达式匹配的表。只能使用表示任意字符的通配符\*，或表示字符之间。

## 示例
```
SHOW TABLES IN sampledb;
```
```
SHOW TABLES IN sampledb '*flights*';
```
