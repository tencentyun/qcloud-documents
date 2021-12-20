列出表中的所有分区。
## 语法
```
SHOW PARTITIONS [db_name.]table_name [PARTITION(partition_spec)];
```
## 参数
- `TABLE  [db_name.]table_name`：表名。
- `[PARTITION(partition_spec)]`：分区列，可以有多个分区列条件。

## 示例
```
SHOW PARTITIONS db01.table PARTITION(ds='2010-03-03', hr='12');
```
