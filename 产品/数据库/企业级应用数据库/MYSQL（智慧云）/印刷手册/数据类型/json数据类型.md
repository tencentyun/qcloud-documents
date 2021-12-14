支持存储Json格式的数据类型，以便更加有效的对Json进行处理，同时又能提早检查错误。
语句如下：
>!对Json类型的字段进行排序时，不支持混合类型排序。
例如，不能将String类型和Int类型做比较，同类型排序只支持数值类型和String类型，其它类型排序暂不处理。

```
mysql>  CREATE TABLE t1 (jdoc JSON,a int key);
Query OK, 0 rows affected (0.30 sec)

mysql> INSERT INTO t1 (jdoc,a)VALUES('{"key1": "value1", "key2": "value2"}',1);
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO t1 (jdoc,a)VALUES('{"key1": "value1", "key2": 2}',2);

mysql> select * from t1;
+--------------------------------------+---+
| jdoc                                 | a |
+--------------------------------------+---+
| {"key1": "value1", "key2": "value2"} | 1 |
| {"key1": "value1", "key2": 2}        | 2 |
+--------------------------------------+---+
2 rows in set (0.00 sec)
```
