
> If you need to view or download the full development documents, please see [Development Guide for DCDB](https://cloud.tencent.com/document/product/557/7714).

#### Subquery

DCDB only supports the derived table with shardkey.
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
	

