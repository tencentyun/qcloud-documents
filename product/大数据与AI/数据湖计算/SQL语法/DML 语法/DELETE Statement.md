>? 该语法仅支持通过 spark 引擎在 Iceberg 表上执行。
## 语法
```
DELETE FROM table_name [ [ AS ] alias ]
[ WHERE booleanExpression ]
```


## 参数说明
`table_identifier`：指定表名，支持三段式，例如：catalog.database.table。

## 示例
```
DELETE FROM lineitem WHERE shipmode = 'AIR';

DELETE FROM lineitem
WHERE orderkey IN (SELECT orderkey FROM orders WHERE priority = 'LOW');

DELETE FROM orders;
```



