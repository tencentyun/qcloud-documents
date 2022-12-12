
## 说明
- 支持内核：SparkSQL。
- 适用表类型：外部 Iceberg 表、原生 Iceberg 表。
- 用途：变更字段名称。

## 语法
```
ALTER TABLE table_identifier 
RENAME COLUMN old_column_name TO new_column_name
```

## 参数
- `table_identifier`：数据表名称。
- `old_column_name`：需变更的字段名称。
- `new_column_name`：变更后的字段名称。

## 示例
```
alter table iceberg_rename rename column id to id_2
```



