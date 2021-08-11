Oracle 只支持相同字段类型 UNION ALL 合并，TDSQL PostgreSQL版（Oracle 兼容）则支持不同字段类型的合并。

示例：
```
postgres=# select 1 as f1,2 as f2,'111' as f3 union all select 11,'22',33;
  f1 | f2 | f3  
----+----+-----
  1 |  2 | 111
  11 | 22 |  33
(2 rows)
```
