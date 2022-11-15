## SET：更新属性配置
### 语法
```
ALTER TABLE table_identifier 
SET TBLPROPERTIES (property_name=property_value, ...)
```


### 示例
```
ALTER TABLE dempts SET TBLPROPERTIES ('read.split.target-size'='268435456')
```


## UNSET：删除属性配置
### 语法
```
ALTER TABLE table_identifier 
UNSET TBLPROPERTIES (property_name, ...)
```


### 示例
```
ALTER TABLE dempts UNSET TBLPROPERTIES ('read.split.target-size')
```



