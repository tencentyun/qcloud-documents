## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：修改数据表的属性。

## 标准语法
```
ALTER TABLE table_name 
 [PARTITION 
   (partition_col1_name = partition_col1_value
   [,partition_col2_name = partition_col2_value][,...])]
  ADD COLUMNS (col_name data_type) [RESTRICT | CASCADE]
```
## 参数
- `table_name`：需要的表名字。
- `partition_col1_name`: 分区名。
- `partition_col1_value`：分区值。
- `col_name`：添加的列名。
- `data_type`：添加的列类型。


## 示例
```
ALTER TABLE events ADD COLUMNS (eventowner string);

ALTER TABLE events ADD COLUMNS (eventowner string) CASCADE;

ALTER TABLE events PARTITION (year='2021') ADD COLUMNS (event string);

```

>! 如果创建表的时候采用了 `ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'` 这种格式存储的表时，在创建表之后就不可以进行增加列情况，如果使用 JsonSerDe 方式创建表的时候请注意尽量确认表的结构，如果必须要增加列可以考虑删除表然后重建。

