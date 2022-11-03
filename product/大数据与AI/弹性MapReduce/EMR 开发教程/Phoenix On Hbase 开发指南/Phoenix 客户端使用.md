Phoenix 查询引擎支持使用 SQL 进行 HBase 数据的查询，会将 SQL 查询转换为一个或多个 HBase API，协同处理器与自定义过滤器的实现，并编排执行。使用 Phoenix 进行简单查询，其性能量级是毫秒，对于百万级别的行数来说，其性能量级是秒。EMR 中选择 HBase 组件的集群，默认集成 phoenix 客户端。
1. 启动客户端
切换成 hadoop 用户，进入/usr/local/service/hbase/phoenix-client/bin 目录，使用 Phoenix 的 Python 命令行工具：
```
./sqlline.py
```
执行成功后显示：
![](https://qcloudimg.tencent-cloud.cn/raw/210a079d7008c510ca25ef6c38eb8a1c.png)

2. Phoenix 引擎支持使用 SQL 进数据查询，一些常见操作如下：
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
