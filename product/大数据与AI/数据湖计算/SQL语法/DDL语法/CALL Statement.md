这里只有在使用 Spark 中使用 [Iceberg SQL 扩展](https://iceberg.apache.org/spark-configuration/#sql-extensions) 时，存储过程才可用。
## 语法
```
CALL expression
```
## 参数
`expression`：函数表达式。

## 示例
```
CALL catalog_name.`system`.procedure_name(arg_name_2 => arg_2, arg_name_1 => arg_1)

#当按位置传递参数时，如果它们是可选的，则只能省略结束参数。
CALL catalog_name.system.procedure_name(arg_1, arg_2, ... arg_n)

#将当前快照设置为db.sample1：
CALL catalog_name.system.set_current_snapshot('db.sample', 1)
```

## 更多使用

[Spark Procedures](https://iceberg.apache.org/spark-procedures/)。
