## 说明
- 支持内核：SparkSQL。
- 适用表范围：原生 Iceberg 表。
- 用途：更新数据表中的指定行。


## 语法
```
UPDATE tablePrimary
SET assign [, assign ]*
[ WHERE booleanExpression ]
```

## 参数
- `tablePrimary`：指定表名，支持三段式，例如：catalog.database.table。
- `assign`：需要修改的式子，例如：col1 = 'new_data'。
- `booleanExpression`：布尔表达式。


## 示例
```
UPDATE prod.db.table
SET c1 = 'update_c1', c2 = 'update_c2'
WHERE ts >= '2020-05-01 00:00:00' and ts < '2020-06-01 00:00:00'

UPDATE prod.db.all_events
SET session_time = 0, ignored = true
WHERE session_time < (SELECT min(session_time) FROM prod.db.good_events)

UPDATE prod.db.orders AS t1
SET order_status = 'returned'
WHERE EXISTS (SELECT oid FROM prod.db.returned_orders WHERE t1.oid = oid)
```



