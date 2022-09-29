## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：删除数据表的某字段。

## 标准语法
```
ALTER TABLE table_name DROP COLUMN column_name
```


## 参数
- `table_name`：需要修改的表名字。
- `column_name`: 需要删除的列名称。

## 示例
```
ALTER TABLE `TBL` DROP COLUMN `COL2`
```



