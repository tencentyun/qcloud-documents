
如您需要阅读或下载全量开发文档，请参见 [TDSQL 开发指南](https://cloud.tencent.com/document/product/557/7714)。

### DML 语句语法（部分）

**SELECT**：建议在条件中带上 shardkey 字段，否则 TDSQL 无法判断 SQL 应该路由至哪些节点，需要进行全表扫描，然后在网关聚合，容易影响执行效率：
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
**INSERT/REPLACE**：字段必须包含 shardkey，因为 TDSQL 无法判断该条 SQL 应该发往哪个节点，乱发会导致数据异常，因此 TDSQL 将会直接拒绝执行无 shardkey 的 INSERT/REPLACE 语句：
```
	mysql> insert into test1 (b,c) values(4,"record3");
	ERROR 810 (HY000): Proxy ERROR:sql is too complex,need to send to only noshard table.
		Shard table insert must has field spec

	mysql> insert into test1 (a,c) values(4,"record3");
	Query OK, 1 row affected (0.01 sec)
```
**DELETE/UPDATE**：同上，为安全考虑，在分表和广播表执行该类 sql 时必须带有 where 条件，否则拒绝执行该 sql 命令：
```
	mysql> delete from test1;
	ERROR 810 (HY000): Proxy ERROR:sql is too complex,need to send to only noshard table.
		Shard table delete/update must have a where clause

	mysql> delete from test1 where a=1;
	Query OK, 1 row affected (0.01 sec)
```
