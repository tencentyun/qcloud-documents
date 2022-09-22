## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生Iceberg表、外部表。
- 用途：更新/删除数据表属性。

## SET：更新属性配置
### 语法
```
ALTER TABLE table_name 
SET TBLPROPERTIES (property_name=property_value, ...)
```

### 参数
- `table_name`：需要的表名字。
- `property_name`: 需要修改的属性名称。
- `property_value`：需要修改的属性值。

### 示例
```
ALTER TABLE orders SET TBLPROPERTIES ('notes'="Please don't drop this table.");
```


## UNSET：删除属性配置
### 语法
```
ALTER TABLE table_name 
UNSET TBLPROPERTIES (property_name, ...)
```

### 参数
- `table_name`：需要的表名字。
- `property_name`: 需要修改的属性名称。

### 示例
```
ALTER TABLE dempts UNSET TBLPROPERTIES ('read.split.target-size')
```



