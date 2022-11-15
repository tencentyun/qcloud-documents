## 语法
```
CREATE TABLE [ IF NOT EXISTS ] table_identifier
USING iceberg
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( property_name=property_value, ... ) ]
AS select_statement
```


## 示例
```
CREATE TABLE dempts_copy
USING iceberg
COMMENT 'table create as select' 
PARTITIONED BY (eno, dno) 
TBLPROPERTIES ('write.format.default'='avro') 
LOCATION '/warehouse/db_001/dempts_copy'
AS SELECT * from dempts;

```


