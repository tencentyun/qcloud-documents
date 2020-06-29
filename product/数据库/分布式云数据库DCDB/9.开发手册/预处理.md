如您需要阅读或下载全量开发文档，请参见 [TDSQL开发指南](https://cloud.tencent.com/document/product/557/7714)。


**TDSQL 支持预处理，使用方式与单机 MySQL 相同，此处只是作为列举**，例如：
- PREPARE Syntax
- EXECUTE Syntax

二进制协议的支持：

- COM_STMT_PREPARE
- COM_STMT_EXECUTE

示例：
```
	mysql> select * from test1;
	+---+------+
	| a | b    |
	+---+------+
	| 5 |    6 |
	| 3 |    4 |
	| 1 |    2 |
	+---+------+
	3 rows in set (0.03 sec)

	mysql> prepare ff from "select * from test1 where a=?";
	Query OK, 0 rows affected (0.00 sec)
	Statement prepared

	mysql> set @aa=3;
	Query OK, 0 rows affected (0.00 sec)

	mysql> execute ff using @aa;
	+---+------+
	| a | b    |
	+---+------+
	| 3 |    4 |
	+---+------+
	1 row in set (0.06 sec)
```
