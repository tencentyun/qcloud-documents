为某个表创建一个或多个分区列。
## 语法
```
ALTER TABLE table_name ADD [IF NOT EXISTS]
  PARTITION (partition_spec)
  [PARTITION (partition_spec) ...]

partition_spec:
  : partition_column = partition_col_value, partition_column = partition_col_value, ...
```
## 参数
- `table_name`：需要的表名字。
- `partition_column`: 分区名。
- `partition_col_value`：分区值。

## 示例
```
ALTER TABLE tbl ADD PARTITION (p1=1, p2='a');
ALTER TABLE tbl ADD IF NOT EXISTS PARTITION ('P' = 1) PARTITION ('P' = 2);
```
