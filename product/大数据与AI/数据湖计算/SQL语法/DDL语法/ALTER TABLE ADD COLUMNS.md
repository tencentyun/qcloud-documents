向现有表中添加一列或多列。使用可选分区语法时，更新分区元数据。
## 语法
```
ALTER TABLE table_name 
 [PARTITION 
   (partition_col1_name = partition_col1_value
   [,partition_col2_name = partition_col2_value][,...])]
  ADD COLUMNS (col_name data_type) [RESTRICT | CASCADE];
```
## 参数
- table_name：表名。
- PARTITION：指定分区，分区列和值相对应。
- `ADD COLUMNS (col_name data_type [,col_name data_type,…])`：增加列给某个表，可以是一个列或者多个列。
 - col_name：列名。
 - data_type：数据类型。

## 示例
表：
```
ALTER TABLE events ADD COLUMNS (eventowner string);
ALTER TABLE events ADD COLUMNS (eventowner string) CASCADE;
```
分区表：
```
ALTER TABLE events PARTITION (year='2021') ADD COLUMNS (event string);
```

## 限制
如果创建表的时候采用了 `ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'`这种格式存储的表时，在创建表之后就不可以进行增加列情况，如果使用`JsonSerDe`方式创建表的时候请注意尽量确认表的结构，如果必须要增加列可以考虑删除表然后重建。
