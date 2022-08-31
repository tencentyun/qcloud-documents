变更字段类型/备注信息。
## 语法
```
ALTER TABLE table_identifier 
ALTER COLUMN col_name 
{TYPE new_col_type | COMMENT col_comment}
```


## 参数说明
目前 Iceberg TYPE 变更，仅支持字段类型安全扩展：
- int/integer -> long/bigint
- float -> double
- decimal(P,S) -> decimal(P2,S)，其中P2 > P，即精准度提升

## 示例

```
ALTER TABLE dempts ALTER COLUMN new_column_2 TYPE bigint
ALTER TABLE dempts ALTER COLUMN new_column_2 comment 'alter docs'
```



