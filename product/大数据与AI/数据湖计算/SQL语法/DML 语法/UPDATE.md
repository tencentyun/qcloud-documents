>! 该语法仅支持 Spark 3.1及以上版本，如需升级 Spark 版本可 [提交工单](https://console.cloud.tencent.com/workorder/category ) 与我们沟通升级。

## 语法
```
UPDATE table_identifier [table_alias]
SET  { { column_name | field_name }  = expr } [, ...]
[WHERE clause]
```


## 示例
```
UPDATE dempts SET c1 = 'update_c1', c2 = 'update_c2'
WHERE ts >= '2020-05-01 00:00:00' and ts < '2020-06-01 00:00:00'

UPDATE dempts SET session_time = 0, ignored = true
WHERE session_time < (SELECT min(session_time) FROM prod.db.good_events)

UPDATE dempts AS t1 SET order_status = 'returned'
WHERE EXISTS (SELECT oid FROM prod.db.returned_orders WHERE t1.oid = oid)
```



