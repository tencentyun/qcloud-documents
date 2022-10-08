## 说明
- 支持内核：Presto、SparkSQL。
- 用途：变更视图名称。

## 标准语法
```
ALTER VIEW old_view_identifier RENAME TO new_view_identifier
```


## 参数
- `old_view_identifier`：修改前视图的名称。
- `new_view_identifier`：修改后视图的名称。

## 示例
```
alter view old_view rename to new_view
```



