
> 如果您期望阅读或下载全量开发文档，请参考 [《TDSQL 开发指南》](https://cloud.tencent.com/document/product/557/7714)。

#### JSON

TDSQL 支持存储 Json 格式的数据，使得对 Json 处理更加有效，同时又能提早检查错误；如果您既希望使用 json 类型，又对数据一致性，事务，join 等传统数据库具备的能力也有一定要求的话，TDSQL 将是一个很好的选择，当然 TDSQL 的 JSON 是基于 MySQL 与 Mongodb 的使用仍有一些差异，如果您感兴趣，可以阅读 [TDSQL 与MongoDB 的 JSON 能力对比](https://cloud.tencent.com/document/product/557/15142)。
```
	mysql>  CREATE TABLE t1 (jdoc JSON,a int) shardkey=a;
	Query OK, 0 rows affected (0.30 sec)

	mysql> INSERT INTO t1 (jdoc,a)VALUES('{"key1": "value1", "key2": "value2"}',1);
	Query OK, 1 row affected (0.07 sec)

	mysql> INSERT INTO t1 (jdoc,a)VALUES('[1, 2,',5);
	ERROR 3140 (22032): Invalid JSON text: "Invalid value." at position 6 in value for column 't1.jdoc'.
	mysql> select * from t1;
	+--------------------------------------+------+
	| jdoc                                 | a    |
	+--------------------------------------+------+
	| {"key1": "value1", "key2": "value2"} |    1 |
	+--------------------------------------+------+
	1 row in set (0.03 sec)
```

针对 json 类型的 orderby 不支持混合类型排序，如不能将 string 类型和 int 类型做比较，同类型排序只支持数值类型，string 类型，其它类型排序不处理。
