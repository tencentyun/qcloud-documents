## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生表、外部表。
- 用途：分析存在的表 table_name，查询创建信息。

## 语法
```
SHOW CREATE TABLE [catalog_name.][db_name.]table_name
```
## 参数
`TABLE [db_name.]table_name`
- `db_name`：数据库名称。
- `table_name`：表名称。

## 示例
```
SHOW CREATE TABLE tbl;
```
