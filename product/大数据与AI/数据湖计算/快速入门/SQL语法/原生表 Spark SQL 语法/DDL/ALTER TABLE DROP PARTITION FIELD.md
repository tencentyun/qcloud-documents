删除单个分区字段。
## 语法
```
ALTER TABLE table_identifier 
DROP PARTITION FIELD col_name|transform (col_name)
```


## 示例
```
ALTER TABLE dempts DROP PARTITION FIELD new_column_1
ALTER TABLE dempts DROP PARTITION FIELD bucket(3,new_column_2)
```



