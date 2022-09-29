## 说明
- 支持内核：Presto、SparkSQL。
- 用途：修改视图属性。

## 标准语法
```
ALTER VIEW view_identifier SET TBLPROPERTIES ( property_key = property_val [ , ... ] )
```


## 参数
- `view_identifier`：需要修改属性视图的名称。
- `property_key`：属性名称。
- `property_val`：属性值。

## 示例
```
alter view view1 set tblproperties('comment' = 'view1')

alter view view1 set tblproperties('property1' = 'value1', 'property2' = 'value2')
```



