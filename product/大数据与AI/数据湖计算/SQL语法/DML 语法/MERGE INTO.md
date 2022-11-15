## 说明
- 支持内核：SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：行级数据更新操作，可用于替换 INSERT OVERWRITE 操作。

## 语法
```
MERGE INTO tablePrimary1 [ [ AS ] alias ]
USING tablePrimary2
ON booleanExpression
[ WHEN MATCHED (AND matchedCond=booleanExpression)? THEN DELETE ]*
[ WHEN MATCHED (AND matchedCond=booleanExpression)? THEN UPDATE SET assign [, assign ]* ]*
[ WHEN NOT MATCHED (AND notMatchedCond=booleanExpression)? THEN INSERT VALUES '(' value [ , value ]* 
```


## 参数
- `tablePrimary1`：指定表名，支持三段式，例如：catalog.database.table。
- `alias`：别名。
- `tablePrimary2`：可以是表名，也可以是子查询。
- `booleanExpression`：布尔表达式。

## 示例
```
MERGE INTO catalog1.db2.tbl1 t
USING catalog1.db1.tbl1
ON t.col1 = tbl1.col1
WHEN MATCHED AND t.col1 = 14 THEN DELETE

MERGE INTO catalog1.db2.tbl1 t
USING (SELECT col1 FROM catalog1.db1.tbl1) s
ON t.col1 = s.col1
WHEN MATCHED AND t.col1 = 14 THEN UPDATE SET col1 = 2


MERGE INTO catalog1.db2.tbl1 t
USING (SELECT col1 FROM catalog1.db1.tbl1) s
ON t.col1 = s.col1
WHEN MATCHED AND t.col1 = 12 THEN UPDATE SET col1 = 0
WHEN MATCHED AND t.col1 = 13 THEN UPDATE SET col1 = 1
WHEN MATCHED AND t.col1 = 14 THEN UPDATE SET col1 = 2
WHEN MATCHED AND t.col1 = 15 or s.col1 = 16 THEN UPDATE SET col1 = t.col1 + 1
WHEN MATCHED AND t.col1 not in (12, 13, 14, 15) THEN UPDATE SET col1 = 4
WHEN NOT MATCHED AND t.col1 = 12 THEN INSERT (col1) VALUES (s.col1)
WHEN NOT MATCHED AND t.col1 = 13 THEN INSERT (col1) VALUES (s.col1 + 1)
WHEN NOT MATCHED AND t.col1 = 14 THEN INSERT (col1) VALUES (s.col1 + 2)


MERGE INTO catalog1.db2.tbl1 t
USING (SELECT col1, col2 FROM catalog1.db1.tbl1) s
ON t.col1 = s.col1
WHEN MATCHED AND t.col1 = fun1(s.col2) THEN DELETE
WHEN MATCHED AND t.col1 = db2.fun1(s.col2) THEN DELETE
WHEN MATCHED AND (t.col1 = length(s.col2) or t.col1 = catalog2.db2.fun3(s.col2)) THEN UPDATE SET col1 = 3
WHEN NOT MATCHED AND t.col1 = 12 THEN INSERT (col1) VALUES (db2.fun2(s.col2))
```


