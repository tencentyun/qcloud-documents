## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生表、外部表。
- 用途：查看数据表列信息及元数据信息。

## 标准语法
```
DESCRIBE [EXTENDED | FORMATTED] [db_name.]table_name [PARTITION partition_spec];
```
## 参数
- `[EXTENDED | FORMATTED]`：指定表的格式化形式。
- `table_name`：需要的表名字。
- `[PARTITION partition_spec]`：该表的分区列表。

## 示例
```
DESCRIBE tbl;
DESCRIBE FORMATTED tbl PARTITION (date_id = '2019-01-07');
```
