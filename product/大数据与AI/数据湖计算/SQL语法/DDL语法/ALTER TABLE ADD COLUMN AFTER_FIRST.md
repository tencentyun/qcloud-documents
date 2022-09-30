## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：为数据表添加列。

## 标准语法
```
ALTER TABLE table_name ADD COLUMN column_name1 column_type [COMMENT col_comment] [FIRST|AFTER column_name2]
```

## 参数
- `table_name`：需要修改的表名字。
- `column_name1`: 需要添加的列。
- `column_type`: 添加列的类型。
- `col_comment`: 添加列的注释。
- `column_name2`: 添加的列放置到这个列的后面。

## 示例
```
ALTER TABLE `TBL` ADD COLUMN `COL2` STRING COMMENT 'test' AFTER `COL1`

ALTER TABLE `TBL` ADD COLUMN `COL2` STRING COMMENT 'test' FIRST
```



