为某个表创建一个或多个分区列。
## 语法
```
ALTER TABLE table_name ADD [IF NOT EXISTS]
  PARTITION
  (partition_col1_name = partition_col1_value
  [,partition_col2_name = partition_col2_value]
  [,...]);
```
## 参数
- IF NOT EXISTS：如果存在就不报错。
- `PARTITION (partition_col_name = partition_col_value [,...])`：指定分区列。

## 示例
```
ALTER TABLE tbl ADD PARTITION (p1=1, p2='a');
ALTER TABLE tbl ADD IF NOT EXISTS PARTITION ('P' = 1) PARTITION ('P' = 2);
```
