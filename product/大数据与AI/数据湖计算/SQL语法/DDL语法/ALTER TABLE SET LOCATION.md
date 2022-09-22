## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生Iceberg表、外部表。
- 用途：修改数据表的存储路径。

## 标准语法
```
ALTER TABLE table_name [ PARTITION (partition_spec) ] SET LOCATION 'new location';
```


## 参数
- `table_name`：数据表的名称。
- `PARTITION (partition_spec)`：指定分区列。
	- partition_col_name：分区列名。
	- partition_col_value：分区列的值。
- `'new location'`：新的表或者分区在 tencent cos 上的位置。

## 示例
```
ALTER TABLE tbl PARTITION (a='1', b='2') SET LOCATION '/path/to/part/ways';

ALTER TABLE tbl SET LOCATION '/path/to/part/ways';
```



