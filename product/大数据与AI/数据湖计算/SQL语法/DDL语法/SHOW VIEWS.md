列出指定数据库中的视图，如果省略数据库名称，则列出当前数据库中的视图。

## 语法
```
SHOW VIEWS [IN database_name] LIKE ['regular_expression']
```
## 参数
- `[IN database_name]`：指定要从中列出视图的数据库名称。如果省略，则假定当前上下文中的数据库。
- `[LIKE 'regular_expression']`：将视图列表筛选为与指定的常规表达式匹配的视图。只能使用表示任意字符的通配符\*，或表示字符之间可供选择。

## 示例
```
SHOW VIEWS;
```
```
SHOW VIEWS IN db01 LIKE 'view*';
```
