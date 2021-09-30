Phoenix 引擎支持使用 SQL 进数据查询，一些常见操作如下：

- 创建表
```sql
0: jdbc:phoenix:> CREATE TABLE IF NOT EXISTS TEST (
	host char(50) not null,
	txn_count bigint
	CONSTRAINT pk PRIMARY KEY (host)
);
```
- 插入数据
```sql
0: jdbc:phoenix:>UPSERT INTO TEST(host,txn_count) VALUES('192.168.1.1',1);
0: jdbc:phoenix:>UPSERT INTO TEST(host,txn_count) VALUES('192.168.1.2',2);
```
- 查询数据
```sql
0: jdbc:phoenix:>SELECT * FROM TEST;
```
- 删除数据表
```sql
0: jdbc:phoenix:>DROP TABLE IF EXISTS TEST;
```

更多操作及说明，可参考 [社区文档](http://phoenix.apache.org/language/index.html)。
