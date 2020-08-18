如您需要阅读或下载全量开发文档，请参见 [TDSQL开发指南](https://cloud.tencent.com/document/product/557/7714)。


TDSQL 目前只支持带 shardkey 的 derived table。
```
	mysql> select a from (select * from test1) as t;
	ERROR 7012 (HY000): Proxy ERROR:sql should has one shardkey
	mysql> select a from (select * from test1 where a=1) as t;
	+---+
	| a |
	+---+
	| 1 |
	+---+
	1 row in set (0.00 sec)
```
	
