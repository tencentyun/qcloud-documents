
## select
建议带上 shardkey 字段，proxy 根据该字段的 hash 值直接将 SQL 请求路由至对应的数据库实例进行处理；否则就需要发送给集群中所有的数据库实例执行，然后 proxy 根据数据库返回的结果集进行聚合，影响执行效率：
```
mysql> select * from test1 where a=2;
+------+------+---------+
| a    | b    | c       |
+------+------+---------+
|    2 |    3 | record2 |
|    2 |    4 | record3 |
+------+------+---------+
2 rows in set (0.00 sec)
```

## insert/replace
字段必须包含 shardkey，否则会拒绝执行该 SQL，因为 proxy 不知道将该 SQL 发往哪个后端数据库：
```
mysql> insert into test1 (b,c) values(4,"record3");
ERROR 810 (HY000): Proxy ERROR:sql is too complex,need to send to only noshard table.
	Shard table insert must has field spec

mysql> insert into test1 (a,c) values(4,"record3");
Query OK, 1 row affected (0.01 sec)
```

## delete/update
为安全考虑，执行该类 SQL 时，必须带有 where 条件，否则拒绝执行该 SQL 命令：
```
mysql> delete from test1;
ERROR 810 (HY000): Proxy ERROR:sql is too complex,need to send to only noshard table.
	Shard table delete/update must have a where clause

mysql> delete from test1 where a=1;
Query OK, 1 row affected (0.01 sec)
```
