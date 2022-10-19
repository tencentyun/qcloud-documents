## 说明
- 支持内核：SparkSQL。
- 适用表范围：原生 Iceberg 表。
- 用途：删除数据表中的指定行。

## 语法
```
DELETE FROM table_name [ [ AS ] alias ]
[ WHERE booleanExpression ]
```


## 参数说明
`table_identifier`：指定表名，支持三段式，例如：catalog.database.table


## 示例
```
DELETE FROM lineitem WHERE shipmode = 'AIR';

DELETE FROM lineitem
WHERE orderkey IN (SELECT orderkey FROM orders WHERE priority = 'LOW');

DELETE FROM orders;
```



