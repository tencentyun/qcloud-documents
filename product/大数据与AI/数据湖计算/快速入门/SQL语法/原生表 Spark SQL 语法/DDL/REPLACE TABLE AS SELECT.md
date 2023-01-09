保留表 history 情况下，从目标表更新替换表快照 snapshot。
## 语法
```
CREATE OR REPLACE TABLE table_identifier
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
AS select_statement
```


## 示例
```
CREATE OR REPLACE TABLE dempts_replace
COMMENT 'table create as replace' 
PARTITIONED BY (eno, bucket(10, num))  
AS SELECT * from dempts;
```



