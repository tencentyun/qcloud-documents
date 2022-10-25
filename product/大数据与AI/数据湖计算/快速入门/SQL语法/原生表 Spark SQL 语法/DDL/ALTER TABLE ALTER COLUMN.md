变更字段类型/备注信息。
## 语法
```
ALTER TABLE table_identifier 
ALTER COLUMN col_name 
{TYPE new_col_type | COMMENT col_comment}
```


## 示例
```
ALTER TABLE dempts ALTER COLUMN new_column_2 TYPE bigint
ALTER TABLE dempts ALTER COLUMN new_column_2 comment 'alter docs'
```



