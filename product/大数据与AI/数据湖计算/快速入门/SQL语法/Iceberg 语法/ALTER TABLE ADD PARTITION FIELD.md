新增单个分区字段。
## 语法

```
ALTER TABLE table_identifier 
ADD PARTITION FIELD col_name|transform (col_name) [AS alias]
```


## 示例

```
ALTER TABLE dempts ADD PARTITION FIELD new_column_1
ALTER TABLE dempts ADD PARTITION FIELD bucket(3,new_column_2)
```



