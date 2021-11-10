返回表的列信息以及元数据信息。
## 语法
```
DESCRIBE [EXTENDED | FORMATTED] [db_name.]table_name [PARTITION partition_spec];
```
## 参数
- `[EXTENDED | FORMATTED]`：指定表的格式化形式。
- `[PARTITION partition_spec]`：该表的分区列表。

## 示例
```
DESCRIBE tbl;
DESCRIBE FORMATTED tbl PARTITION (date_id = '2019-01-07');
```

## 限制
- 这个语句目前只返回表的列名。
- partition_spec 暂时不支持对表的分区查询。
