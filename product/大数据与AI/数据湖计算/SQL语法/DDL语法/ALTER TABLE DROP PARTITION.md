## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：外部表。
- 用途：删除数据表的某个分区列。

## 标准语法
```
ALTER TABLE table_name DROP [IF EXISTS] PARTITION (partition_spec) [,PARTITION (partition_spec), ...]

partition_spec:
  : partition_column = partition_col_value, partition_column = partition_col_value, ...
```
## 参数
`table_name`：需要的表名字。
`partition_column`: 分区名。
`partition_col_value`：分区值。


## 示例
```
ALTER TABLE page_view DROP PARTITION (dt='2008-08-08', country='us')

ALTER TABLE `page_view` DROP
PARTITION (`dt` = '2008-08-08', `country` = 'us'),
PARTITION (`dt` = '2008-08-08', `country` = 'us'),
PARTITION (`dt` = '2008-08-08', `country` = 'us')
```
