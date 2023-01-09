## 新增多个字段
#### 语法
```
ALTER TABLE table_identifier 
ADD COLUMNS (col_name col_type [COMMENT col_comment], ...)
```


### 示例
```
ALTER TABLE dempts
ADD COLUMNS (
    new_column_1 string comment 'new_column_1 docs',
    new_column_2 int comment 'new_column_2 docs'
) 
```


## 新增单个字段
### 语法
```
ALTER TABLE table_identifier 
ADD COLUMN col_name col_type [COMMENT col_comment] 
[FIRST | AFTER target_col_name]
```


### 示例
```
ALTER TABLE dempts 
ADD COLUMN new_column_3 string comment 'new_column docs'
```



