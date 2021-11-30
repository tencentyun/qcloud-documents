列出所有在该元数据中定义的所有数据库，可使用 DATABASES 或者 SCHEMAS 做相同的查询。
## 语法
```
SHOW {DATABASES | SCHEMAS} [IN catalog_name] [LIKE 'regular_expression']
```
## 参数
- `[IN catalog_name]`：数据源名称。
- `[LIKE 'regular_expression']`：过滤出匹配的数据库名称。

## 示例
```
SHOW DATABASES;
SHOW DATABASES LIKE '.*analytics';
SHOW DATABASES IN catalog1 LIKE '.*analytics';
```
