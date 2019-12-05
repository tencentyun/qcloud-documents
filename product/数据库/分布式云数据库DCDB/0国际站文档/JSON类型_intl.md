
> If you need to view or download the full development documents, please see [Development Guide for DCDB](https://cloud.tencent.com/document/product/557/7714).

#### JSON

DCDB supports storing data in JSON format, making it more effective for JSON processing while you can check for errors as soon as possible. If you want to use JSON type, and have certain requirements for the capabilities of traditional databases such as data consistency, transactions, and JOINs, DCDB will be a good choice. There are still some differences between MongoDB and DCDB, whose JSON is based on MySQL. For more information, please see [Comparison of JSON in DCDB and MongoDB](https://cloud.tencent.com/document/product/557/15142).
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

The JSON-based orderby does not support the mixed-type sorting. For example, comparison for fields of string type and int type cannot be achieved. For sorting of the same type, only numeric fields can be sorted, but string and other types cannot be sorted.

