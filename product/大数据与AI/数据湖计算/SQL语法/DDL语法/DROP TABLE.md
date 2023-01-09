## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生表、外部表。
- 用途：移除元数据表。

## 语法
```
DROP TABLE [IF EXISTS] table_name；
```
## 参数
- `IF EXISTS`：可选，如果存在的意思。
- `table_name`：表名。

## 示例
```
DROP TABLE tbl
DROP TABLE IF EXISTS tbl
```
