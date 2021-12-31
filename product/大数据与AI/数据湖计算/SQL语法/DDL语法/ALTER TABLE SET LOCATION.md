改变表或者分区表的存储位置。
## 语法
```
ALTER TABLE table_name [ PARTITION (partition_spec) ] SET LOCATION 'new location';
```
## 参数
- `PARTITION (partition_spec)`：指定分区列。
 - `partition_col_name` 分区列名。
 - `partition_col_value` 分区列的值。
- `SET LOCATION 'new location'`：创建在一个新位置在 tencent cos 上。时
