保留表 history 情况下，从目标表更新替换表快照 snapshot。
## 语法
```
CREATE [OR REPLACE] TABLE table_identifier
USING iceberg
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( property_name=property_value, ... ) ]
AS select_statement
```


## 示例
```
CREATE OR REPLACE TABLE dempts_replace
USING iceberg
COMMENT 'table create as replace' 
PARTITIONED BY (eno, dno) 
TBLPROPERTIES ('write.format.default'='avro') 
LOCATION '/warehouse/db_001/dempts_replace'
AS SELECT * from dempts;
```



